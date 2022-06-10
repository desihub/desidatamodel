# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""
===================
desidatamodel.check
===================

Check actual files against the data model for validity.
"""
import os
import re
from sys import argv
from argparse import ArgumentParser

from desiutil.log import log, DEBUG

from . import DataModelError
from .stub import Stub
from .unit import DataModelUnit


class DataModel(DataModelUnit):
    """Simple object to store data model data and metadata.

    Parameters
    ----------
    filename : :class:`str`
        The full path of the data model file.
    section : :class:`str`
        The full path to the section of the data model containing the file.
    """
    # Marker for optional keywords and columns.
    _o = '[1]_'
    # A mapping of human-readable metavariables to regular expressions.
    _d2r = {'BRICKNAME': '[0-9]+[pm][0-9]+',  # e.g. 3319p140
            'CAMERA': '[brz][0-9]',  # e.g. b0, r7
            'EXPID': '[0-9]{8}',  # zero-padded eight digit number.
            'GROUPID': '[0-9]+',  # Group id *directory* depending on type of GROUPTYPE
            # 'GROUPID': '([14]xsubset[1-6]|lowspeedsubset[1-6]|exp[0-9]{8}|thru[0-9]{8}|[0-9]{8})',  # Group id depending on type of GROUPTYPE
            'GROUPTYPE': '(1x_depth|4x_depth|lowspeed|cumulative|perexp|pernight)',  # Tile grouping, e.g. pernight, perexp
            'NIGHT': '[0-9]{8}',  # YYYYMMDD
            'NSIDE': '[0-9]+',  # Healpix sides, e.g. 64
            'PIXGROUP': '[0-9]+',  # Healpix group, e.g. 53
            'PIXPROD': '[a-z0-9_-]+',  # e.g. alpha-3
            'PIXNUM': '[0-9]+',  # Healpix pixel, e.g. 5302
            'PRODNAME': '[a-z0-9_-]+',  # e.g. dc3c
            'PROGRAM': '(backup|bright|dark|other)',  # observation program
            'SPECPROD': '[a-z0-9_-]+',  # replacement for PRODNAME
            'SPECTROGRAPH': '[0-9]',  # spectrograph number 0-9
            'SURVEY': '(cmx|main|special|sv1|sv2|sv3)',  # Survey name
            'TILEID': '[0-9]+',  # Tile ID, e.g. 70005 or 123456
            }
    # Matches titles.
    _titleline = re.compile(r'=+\n([^=]+)\n=+\n', re.M)
    # Matches HDU section headers.
    _hduline = re.compile(r'HDU(\d+)$')
    # Match HDU range specifications.
    _hduspan = re.compile(r'HDU(\d+)[-: ]+HDU(\d+)$')
    # Matches lines that contain regular expressions.
    _regexpline = re.compile(r':?regexp?:', re.I)
    # Matches the file-type line.
    _filetypeline = re.compile(r':?file type?:', re.I)
    # Matches lines that contain cross-references.
    _refline = re.compile(r'See (:doc:|)`([^<]+)<([^>]+)>`_?')
    # Matches table borders.
    _tableboundary = re.compile(r'[= ]+$')
    # The list of file types allowed by the data model.
    _expectedtypes = ('ascii', 'csv', 'ecsv', 'fits', 'yaml')

    def __init__(self, filename, section):
        shortname = filename.replace(f'{section}/', '')
        log.debug('Creating DataModel for %s.', shortname)
        self.filename = filename
        self.section = section
        self.title = None
        self.ref = None
        self.regexp = None
        self.filetype = None
        self.filesize = None
        self.hdumeta = None
        self.prototype = None
        self._metafile_data = None
        self._stub = None
        self._stub_meta = None
        return

    def get_regexp(self, root, error=False):
        """Obtain the regular expression used to match files on disk.

        Also internally updates the file type, if detected.

        Parameters
        ----------
        root : :class:`str`
            Path to real files on disk.
        error : :class:`bool`, optional
            If ``True``, failure to find a regular expression raises an
            exception instead of just a warning.

        Returns
        -------
        regular expression
            The regular expression found, or ``None`` if not found.
            The regular expression is also stored internally.

        Raises
        ------
        :exc:`~desimodel.DataModelError`
            If `error` is set and problems with the data model file are
            detected.
        """
        with open(self.filename) as dm:
            for line in dm.readlines():
                if line.startswith('See :doc:'):
                    self.ref = self._cross_reference(line)
                    log.debug("Cross reference detected %s -> %s.",
                              self.filename, self.ref)
                    break
                if self._regexpline.match(line) is not None:
                    d = os.path.dirname(self.filename).replace(self.section,
                                                               root)
                    for k in self._d2r:
                        d = d.replace(k, self._d2r[k])
                    r = line.strip().split()[1].replace('``', '')
                    self.regexp = re.compile(os.path.join(d, r))
                if self._filetypeline.match(line) is not None:
                    self.filetype, self.filesize = self._type_size(line)
        if self.regexp is None and self.ref is not None:
            with open(self.ref) as dm:
                for line in dm.readlines():
                    #
                    # Hopefully cross-references are not nested.
                    #
                    # if line.startswith('See :doc:'):
                    #     self.ref = self._cross_reference(line)
                    #     break
                    if self._regexpline.match(line) is not None:
                        d = os.path.dirname(self.filename).replace(self.section,
                                                                   root)
                        for k in self._d2r:
                            d = d.replace(k, self._d2r[k])
                        r = line.strip().split()[1].replace('``', '')
                        self.regexp = re.compile(os.path.join(d, r))
                    if self._filetypeline.match(line) is not None:
                        self.filetype, self.filesize = self._type_size(line)
        if self.regexp is None:
            m = "%s has no file regexp!"
            if error:
                log.critical(m, self.filename)
                raise DataModelError(m % self.filename)
            else:
                log.warning(m, self.filename)
        if self.filetype is None:
            m = "%s has missing or invalid file type!"
            if error:
                log.critical(m, self.filename)
                raise DataModelError(m % self.filename)
            else:
                log.warning(m, self.filename)
        else:
            if self.filetype not in self._expectedtypes:
                log.warning("Unusual file type, %s, detected for %s!", self.filetype, self.filename)
        return self.regexp

    def _type_size(self, line):
        """Obtain file type and size from a matching `line`.

        Parameters
        ----------
        line : :class:`str`
            Line from file that contains the type and size.

        Returns
        -------
        :class:`tuple`
            A tuple containing the type and size.
        """
        ts = line.lower().replace(':', '').replace('file type', '').strip().split(',')
        t = ts[0]
        try:
            i = ts[1].upper().index('B')
        except (ValueError, IndexError):
            s = 'Unknown'
        else:
            s = ts[1].upper()[:(i+1)].strip()
        return (t, s)

    def _cross_reference(self, line):
        """Obtain the path to a file referred to in another file.

        Parameters
        ----------
        line : :class:`str`
            Line from original file that *is* the cross-reference.

        Returns
        -------
        :class:`str`
            The path to the referenced file.
        """
        ref = None
        m = self._refline.match(line)
        if m is not None:
            reftype, refstring, reflink = m.groups()
            if reftype == ':doc:':
                r = os.path.abspath(os.path.join(os.path.dirname(self.filename),
                                                 reflink))
                if not r.endswith('.rst'):
                    r += '.rst'
                if os.path.exists(r):
                    ref = r
            else:
                rr = reflink.replace('.html', '.rst').split('#')
                r = os.path.abspath(os.path.join(os.path.dirname(self.filename),
                                    rr[0]))
                if os.path.exists(r):
                    ref = r + '#' + rr[1]
        return ref

    def _extract_columns(self, row, columns):
        """Given column sizes, extract the data in each column.

        Assumes a reStructuredText-compatible table.

        Parameters
        ----------
        row : :class:`str`
            A table row.
        columns : :class:`list`
            The sizes of the columns.

        Returns
        -------
        :func:`tuple`
            A tuple containing the extracted data.
        """
        lbound = [0] + [sum(columns[:i])+i for i in range(1, len(columns))]
        ubound = [lbound[i] + c for i, c in enumerate(columns)]
        ubound[-1] = None
        data = [row[lbound[i]:ubound[i]].strip() for i in range(len(columns))]
        return tuple(data)

    def extract_metadata(self, error=False):
        """Extract metadata from a data model file.

        Parameters
        ----------
        error : :class:`bool`, optional
            If ``True``, failure to extract certain required metadata raises an
            exception.

        Returns
        -------
        :class:`dict`
            Metadata in a form similar to :class:`~desidatamodel.stub.Stub`
            metadata. The keys are the ``EXTNAME`` header values.

        Raises
        ------
        :exc:`~desidatamodel.DataModelError`
            If `error` is set and the HDU has no ``EXTNAME`` keyword.
        """
        if self.hdumeta is not None:
            return self.hdumeta
        metafile = self.filename
        if self.ref is not None:
            metafile = self.ref
        if self._metafile_data is None:
            with open(metafile) as f:
                self._metafile_data = f.read()
        if self.title is None:
            m = self._titleline.match(self._metafile_data)
            if m is not None:
                self.title = m.groups()[0]
        lines = self._metafile_data.split('\n')
        hdu_sections = [i for i, l in enumerate(lines)
                        if (self._hduline.match(l) is not None or
                            self._hduspan.match(l) is not None)]
        self.hdumeta = dict()
        for k in range(len(hdu_sections)):
            try:
                section = lines[hdu_sections[k]:hdu_sections[k+1]]
            except IndexError:
                section = lines[hdu_sections[k]:]
            m = self._hduspan.match(section[0])
            if m is not None:
                #
                # Detected HDU span.
                #
                g = m.groups()
                spanstart = int(g[0])
                spanend = int(g[1])
                log.debug('Detected range specification from HDU %d to HDU %d',
                          spanstart, spanend)
                spanref = [l for l in section if l.startswith('Data:')][0]
                spanext = spanref[spanref.lower().index('see') + 4:].replace('.', '')
                try:
                    spanmeta = self.hdumeta[spanext]
                except KeyError:
                    m = "Cannot find EXTNAME = '%s' which is supposed to define HDU %d to HDU %d!"
                    log.critical(m, spanext, spanstart, spanend)
                    raise DataModelError(m % (spanext, spanstart, spanend))
                spanname = [l.split('=')[1].strip() for l in section
                            if l.startswith('EXTNAME = ')][0]
                extnames = [p.strip() for p in spanname.split(',')]
                if len(range(spanstart, spanend+1)) == len(extnames):
                    for i, l in enumerate(range(spanstart, spanend+1)):
                        meta = dict()
                        meta['number'] = l
                        meta['title'] = 'HDU{0:d}'.format(l)
                        meta['extname'] = extnames[i]
                        meta['extension'] = spanmeta['extension']
                        meta['format'] = spanmeta['format']
                        meta['keywords'] = spanmeta['keywords']
                        self.hdumeta[extnames[i]] = meta
                else:
                    log.warning(('Range specification from HDU %d to HDU %d ' +
                                 'does not have a matching EXTNAME specification!'),
                                spanstart, spanend)
                continue
            meta = dict()
            meta['number'] = k
            meta['title'] = section[0]
            hdu_cross_ref = [l for l in section if l.startswith('See `')]
            if hdu_cross_ref:
                log.debug("Found HDU cross-reference: %s", hdu_cross_ref[0])
                hcr = self._cross_reference(hdu_cross_ref[0]).split('#')
                log.debug("['%s', '%s']", hcr[0], hcr[1])
                hcr_meta = DataModel(hcr[0], self.section).extract_metadata()
                for key in hcr_meta:
                    if hcr_meta[key]['title'] == hcr[1].upper():
                        for subkey in ('extension', 'format', 'keywords', 'extname'):
                            meta[subkey] = hcr_meta[key][subkey]
                        self.hdumeta[key] = meta
                continue
            if 'Empty HDU.' in section:
                meta['extension'] = 'IMAGE'
                meta['format'] = 'Empty HDU.'
            image_data = [l for l in section if l.startswith('Data:')]
            if image_data:
                meta['extension'] = 'IMAGE'
                meta['format'] = image_data[0]
            try:
                rdtc = section.index('Required Data Table Columns')
            except ValueError:
                rdtc = None
            if rdtc is not None:
                meta['extension'] = 'BINTABLE'
                table = [i for i, l in enumerate(section[rdtc:])
                         if self._tableboundary.match(l) is not None][1:3]
                columns = list(map(len, section[rdtc:][table[0]].lstrip().split()))
                table_lines = section[rdtc:][table[0]+1:table[1]]
                meta['format'] = [self._extract_columns(t.lstrip(), columns)
                                  for t in table_lines]
                for mk in meta['format']:
                    if not mk[1]:
                        m = "Missing type for column %s in HDU %d of %s!"
                        if error:
                            log.critical(m, mk[0], k, metafile)
                            raise DataModelError(m % (mk[0], k, metafile))
                        else:
                            log.warning(m, mk[0], k, metafile)
                    if mk[2]:
                        bad_unit = self.check_unit(mk[2], error=error)
                        if bad_unit:
                            log.debug("Non-standard (but acceptable) unit %s detected for column %s in HDU %d of %s.",
                                      bad_unit, mk[0], k, metafile)
            try:
                rhk = section.index('Required Header Keywords')
            except ValueError:
                meta['keywords'] = []
            else:
                table = [i for i, l in enumerate(section[rhk:])
                         if self._tableboundary.match(l) is not None][1:3]
                columns = list(map(len, section[rhk:][table[0]].lstrip().split()))
                table_lines = section[rhk:][table[0]+1:table[1]]
                meta['keywords'] = [self._extract_columns(t.lstrip(), columns)
                                    for t in table_lines]
                for mk in meta['keywords']:
                    if not mk[2]:
                        m = "Missing type for keyword %s in HDU %d of %s!"
                        if error:
                            log.critical(m, mk[0], k, metafile)
                            raise DataModelError(m % (mk[0], k, metafile))
                        else:
                            log.warning(m, mk[0], k, metafile)
                    if mk[0] == 'BUNIT':
                        bad_unit = self.check_unit(mk[1], error=error)
                        if bad_unit:
                            log.debug("Non-standard (but acceptable) unit %s detected for column %s in HDU %d of %s.",
                                      bad_unit, mk[0], k, metafile)
            #
            # Need to know the format by this point!
            #
            try:
                foo = meta['format']
            except KeyError:
                m = "Unable to determine format for HDU %d in %s!"
                log.critical(m, k, metafile)
                raise DataModelError(m % (k, metafile))
            #
            # See https://github.com/desihub/desidatamodel/issues/69 for
            # the detailed policy on EXTNAME.
            #
            try:
                meta['extname'] = [l.split()[2] for l in section
                                   if l.startswith('EXTNAME = ')][0]
            except IndexError:
                meta['extname'] = 'HDU{0:02d}'.format(k)
                if (k > 0 or (k == 0 and meta['format'] != 'Empty HDU.')):
                    m = "HDU %d in %s has no EXTNAME!"
                    if error:
                        log.critical(m, k, metafile)
                        raise DataModelError(m % (k, metafile))
                    else:
                        log.warning(m, k, metafile)
                else:
                    if k == 0 and meta['format'] == 'Empty HDU.':
                        if len(meta['keywords']) > 0:
                            m = "HDU %d in %s should have EXTNAME = 'PRIMARY', since it has non-trivial keywords."
                            log.warning(m, k, metafile)
            else:
                #
                # If we reach here, meta['extname'] *is* defined.
                #
                if k == 0:
                    if meta['format'] == 'Empty HDU.':
                        if len(meta['keywords']) > 0 and meta['extname'] != 'PRIMARY':
                            m = "HDU %d in %s has acceptable alternative EXTNAME = '%s'."
                            log.debug(m, k, metafile, meta['extname'])
                    else:
                        if meta['extname'] == 'PRIMARY':
                            m = "HDU %d in %s should have a more meaningful EXTNAME than 'PRIMARY'."
                            log.warning(m, k, metafile)
            self.hdumeta[meta['extname']] = meta
        return self.hdumeta

    def validate_prototype(self, error=False, skip_keywords=False):
        """Compares a model's prototype data file to the data models.

        Parameters
        ----------
        error : :class:`bool`, optional
            If ``True``, failure to extract certain required metadata raises an
            exception.
        skip_keywords : :class:`bool`, optional
            If ``True``, don't check FITS header keywords

        Notes
        -----
        * Use set theory to compare the data headers to model headers.  This should
          automatically find missing headers, extraneous headers, etc.
        """
        if self.prototype is None:
            #
            # A warning should have been issued already, so just skip silently.
            #
            return
        log.info("Comparing %s to %s.", self.prototype, self.filename)
        if self._stub is None:
            self._stub = Stub(self.prototype, error=error)
        stub_meta = self._stub_meta = self._stub.hdumeta
        modelmeta = self.extract_metadata(error=error)
        #
        # Check number of headers.
        #
        if self._stub.nhdr != len(modelmeta.keys()):
            log.warning("Prototype file %s has the wrong number of " +
                        "sections (HDUs) according to %s.",
                        self.prototype, self.filename)
            return
        for i in range(self._stub.nhdr):
            dexex = stub_meta[i]['extname']
            if dexex == '' and i > 0:
                log.warning("Prototype file %s has no EXTNAME in HDU%d.",
                            self.prototype, i)
            try:
                modelhdumeta = modelmeta[dexex]
            except KeyError:
                try:
                    modelhdumeta = modelmeta['HDU{0:02d}'.format(i)]
                except KeyError:
                    #
                    # Fall back on trying to find HDU by number.
                    #
                    log.warning("Could not find EXTNAME = '%s' in %s; trying by HDU number.", dexex, self.filename)
                    for key in modelmeta:
                        if modelmeta[key]['number'] == i:
                            modelhdumeta = modelmeta[key]
            #
            # Check for EXTNAME
            #
            mexex = modelhdumeta['extname']
            if (dexex != '' and mexex != '' and dexex != mexex):
                log.warning("Prototype file %s has an EXTNAME mismatch " +
                            "in HDU%d (%s != %s) " +
                            "according to %s.",
                            self.prototype, i, dexex, mexex, self.filename)
            #
            # Compare keywords
            #
            if not skip_keywords:
                data_keywords = set([tmp[0] for tmp in stub_meta[i]['keywords']])
                model_keywords = set([tmp[0].split()[0] for tmp in modelhdumeta['keywords'] if self._o not in tmp[0]])
                optional_keywords = set([tmp[0].split()[0] for tmp in modelhdumeta['keywords'] if self._o in tmp[0]])
                if len(data_keywords - (model_keywords | optional_keywords)) > 0:
                    log.warning('Prototype file %s has these keywords in HDU%d missing from model: %s',
                                self.prototype, i, str(data_keywords - (model_keywords | optional_keywords)))
                if len(model_keywords - data_keywords) > 0:
                    log.warning('Model file %s has these keywords in HDU%d missing from data: %s',
                                self.filename, i, str(model_keywords - data_keywords))
                #
                # Compare the keywords that are in both sets.
                #
                common_keywords = data_keywords & (model_keywords | optional_keywords)
                for kw in common_keywords:
                    mkw_type = [tmp[2] for tmp in modelhdumeta['keywords'] if tmp[0].split()[0] == kw][0]
                    dkw_type = [tmp[2] for tmp in stub_meta[i]['keywords'] if tmp[0] == kw][0]
                    if mkw_type != dkw_type:
                        log.warning("File %s HDU%d keyword %s has different keyword type according to %s (%s != %s).",
                                    self.prototype, i, kw, self.filename, dkw_type, mkw_type)
            #
            # Check the extension type.
            #
            dex = stub_meta[i]['extension']
            try:
                mex = modelhdumeta['extension']
            except KeyError:
                mex = "Extension type not found"
            if dex != mex:
                log.warning("Prototype file %s has an extension type " +
                            "mismatch in HDU%d (%s != %s) " +
                            "according to %s.",
                            self.prototype, i, dex, mex, self.filename)
                continue
            #
            # If the extension type is correct, check the contents of the
            # extension.
            #
            dexf = stub_meta[i]['format']
            try:
                mexf = modelhdumeta['format']
            except KeyError:
                mexf = "Extension format not found"
            if dex == 'IMAGE':
                try:
                    icomma = dexf.index(',')
                except ValueError:
                    icomma = len(dexf)
                if dexf[:icomma] != mexf[:icomma]:
                    log.warning("Prototype file %s has an extension " +
                                "format mismatch in HDU%d " +
                                "according to %s.",
                                self.prototype, i, self.filename)
            else:
                dexf = dexf[1:]  # Get rid of header line.
                data_columns = set([tmp[0] for tmp in dexf])
                model_columns = set([tmp[0].split()[0] for tmp in mexf if self._o not in tmp[0]])
                optional_columns = set([tmp[0].split()[0] for tmp in mexf if self._o in tmp[0]])
                #
                # Do we really care if the number of columns is off?
                # We want all of the required columns to be there, but some or all
                # of the optional columns may be there as well.
                #
                # if len(datacolumns) != len(modelcolumns):
                #     log.warning("Prototype file %s has the wrong " +
                #                 "number of HDU%d columns according to %s.",
                #                 self.prototype, i, self.filename)
                if len(data_columns - (model_columns | optional_columns)) > 0:
                    log.warning('Prototype file %s has these columns in HDU%d missing from model: %s',
                                self.prototype, i, str(data_columns - model_columns))
                if len(model_columns - data_columns) > 0:
                    log.warning('Model file %s has these columns in HDU%d missing from data: %s',
                                self.filename, i, str(model_columns - data_columns))
                common_columns = data_columns & (model_columns | optional_columns)
                for column in common_columns:
                    #
                    # Compare type
                    #
                    mcol_type = [tmp[1] for tmp in mexf if tmp[0].split()[0] == column][0]
                    dcol_type = [tmp[1] for tmp in dexf if tmp[0] == column][0]
                    if mcol_type != dcol_type:
                        if mcol_type == 'char[*]' and dcol_type[:4] == 'char':
                            log.debug("File %s HDU%d column %s has an acceptable variable-length string according to %s.",
                                      self.prototype, i, column, self.filename)
                        else:
                            log.warning("File %s HDU%d column %s has different type according to %s (%s != %s).",
                                        self.prototype, i, column, self.filename, dcol_type, mcol_type)
                    #
                    # Compare unit
                    #
                    mcol_unit = [tmp[2] for tmp in mexf if tmp[0].split()[0] == column][0]
                    dcol_unit = [tmp[2] for tmp in dexf if tmp[0] == column][0]
                    if mcol_unit != '' and dcol_unit != '' and mcol_unit != dcol_unit:
                        log.warning("File %s HDU%d column %s has different units according to %s (%s != %s).",
                                    self.prototype, i, column, self.filename, dcol_unit, mcol_unit)
        return


def scan_model(section):
    """Find all data model files in a top-level directory.

    Parameters
    ----------
    section : :class:`str`
        Full path to a section of the data model.

    Returns
    -------
    :class:`list`
        The data model files found.
    """
    scan = list()
    for dirpath, dirnames, filenames in os.walk(section):
        scan += [DataModel(os.path.join(dirpath, f), section)
                 for f in filenames
                 if f.endswith('.rst') and f != 'index.rst']
    return scan


def files_to_regexp(root, files, error=False):
    """Convert a list of data model files into a list of regular expressions.

    Parameters
    ----------
    root : :class:`str`
        Path to real files on disk.
    files : :class:`list`
        List of files obtained from the data model.
    error : :class:`bool`, optional
        If ``True``, failure to find a regular expression raises an
        exception instead of just a warning.

    Raises
    ------
    :exc:`~desidatamodel.DataModelError`
        If `error` is set and data model files with malformed regular
        expressions are detected.
    """
    for f in files:
        f.get_regexp(root, error)
    return


def collect_files(root, files):
    """Scan a directory tree for files that correspond to data model files.

    Parameters
    ----------
    root : :class:`str`
        Path to real files on disk.
    files : :class:`list`
        A list of data model files.

    Notes
    -----
    Files are analyzed using this algorithm:

    * The first file that matches a regexp becomes the 'prototype' for that
      data model file.
    * If no files match a data model file, then files of that type are
      'missing'.
    * If a file does not match any regular expression, it is 'extraneous'.
    * If a file matches a regular expression that already has a prototype,
      it is 'ignored'.
    """
    ignore_directories = ('logs', 'scripts')
    include_extensions = ('.fits', '.fits.fz', '.fits.gz')
    for dirpath, dirnames, filenames in os.walk(root):
        for d in ignore_directories:
            try:
                dirnames.remove(d)
            except ValueError:
                pass
        include_filenames = list()
        for e in include_extensions:
            include_filenames += [f for f in filenames if f.endswith(e)]
        for f in include_filenames:
            extraneous_file = True
            fullname = os.path.join(dirpath, f)
            for r in files:
                if r.regexp is not None:
                    m = r.regexp.match(fullname)
                    if m is not None:
                        extraneous_file = False
                        if r.prototype is None:
                            r.prototype = fullname

            if extraneous_file:
                log.warning("Extraneous file detected: %s", fullname)
    #
    # Scan for missing files, but don't penalize (here) data models that
    # don't have a valid regular expression.  Files with bad regexeps will
    # be flagged elsewhere.
    #
    for r in files:
        if r.regexp is not None and r.prototype is None:
            log.warning("No files found matching %s!", r.filename)
    return


def validate_prototypes(files, error=False, skip_keywords=False):
    """Compares a set of prototype data files to their data models.

    Parameters
    ----------
    files : :class:`list`
        A list of data model files.
    error : :class:`bool`, optional
        If ``True``, failure to extract certain required metadata raises an
        exception.
    skip_keywords : :class:`bool`, optional
        If ``True``, don't check FITS header keywords

    Notes
    -----
    * Use set theory to compare the data headers to model headers.  This should
      automatically find missing headers, extraneous headers, etc.
    """
    for f in files:
        f.validate_prototype(error=error, skip_keywords=skip_keywords)
    return


def _options():
    """Parse command-line options.

    Returns
    -------
    :class:`~argparse.Namespace`
        The parsed options.
    """
    desc = """Check actual files against the data model for validity.
"""
    parser = ArgumentParser(description=desc, prog=os.path.basename(argv[0]))
    parser.add_argument('-d', '--datamodel-dir', dest='desidatamodel',
                        metavar='DIR',
                        help='Override the value of DESIDATAMODEL.')
    parser.add_argument('-F', '--compare-files', dest='files',
                        action='store_true',
                        help='Compare an individual data model to an individual file.')
    parser.add_argument('-K', '--skip-keywords', dest='skip_keywords', action='store_true',
                        help="Don't check FITS header keywords")
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true',
                        help='Set log level to DEBUG.')
    parser.add_argument('-W', '--warning-is-error', dest='error',
                        action='store_true',
                        help='Data model warnings raise exceptions.')
    parser.add_argument('section', metavar='MODEL_DIR_or_FILE',
                        help='Section of the data model or individual model file.')
    parser.add_argument('directory', metavar='DATA_DIR_or_FILE',
                        help='Check files in this top-level directory, or one individual file.')
    options = parser.parse_args()
    return options


def main():
    """Entry point for the check_model script.

    Returns
    -------
    :class:`int`
        An integer suitable for passing to :func:`sys.exit`.
    """
    options = _options()
    if options.verbose:
        log.setLevel(DEBUG)
    if 'DESIDATAMODEL' in os.environ:
        data_model_root = os.environ['DESIDATAMODEL']
    else:
        if options.desidatamodel is not None:
            data_model_root = options.desidatamodel
        else:
            log.critical(("DESIDATAMODEL is not defined. " +
                          "Cannot find data model files!"))
            return 1
    log.debug("DESIDATAMODEL=%s", data_model_root)
    if options.files:
        filename = os.path.join(data_model_root, 'doc', options.section)
        section = os.path.join(data_model_root, 'doc', options.section.split('/')[0])
        log.info("Loading individual data model: %s.", filename)
        files = [DataModel(filename, section)]
        log.info("Skipping regular expression processing.")
        # files[0].get_regexp(options.directory, error=options.error)
        log.info("Setting prototype file for %s to %s.", filename, options.directory)
        files[0].prototype = options.directory
    else:
        section = os.path.join(data_model_root, 'doc', options.section)
        log.info("Loading data model file in %s.", section)
        files = scan_model(section)
        log.info("Searching for data files in %s.", options.directory)
        files_to_regexp(options.directory, files, error=options.error)
        log.info("Identifying prototype files in %s.", options.directory)
        collect_files(options.directory, files)
    validate_prototypes(files, error=options.error, skip_keywords=options.skip_keywords)
    return 0
