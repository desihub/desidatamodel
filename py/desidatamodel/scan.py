# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""
==================
desidatamodel.scan
==================

Deep scan available files to obtain a comprehensive set of metadata.
"""
import os
import re
from sys import argv
from argparse import ArgumentParser
from random import choices

from desiutil.log import log, DEBUG

from . import DataModelError
from .stub import Stub
from .check import DataModel


class UnionStub(Stub):
    """Container for unified metadata for both existing models and data files.

    Initialize the metadata with a :class:`~desidatamodel.check.DataModel`
    object, then add additional :class:`~desidatamodel.stub.Stub` metadata.

    Parameters
    ----------
    model : :class:`~desidatamodel.check.DataModel`
        A data model file object.
    error : :class:`bool`, optional
        If ``True``, failure to extract certain required metadata raises an
        exception.
    """
    _o = '[1]_'  # Marker for optional keywords and columns.

    def __init__(self, model, error=False):
        self.model = model
        self.error = error
        if model.hdumeta is None:
            modelmeta = model.extract_metadata(error=error)
        self.headers = list()
        self.nhdr = len(list(model.hdumeta.keys()))
        self._hdumeta = sorted([model.hdumeta[k] for k in model.hdumeta],
                               key=lambda x: x['number'])
        for m in self._hdumeta:
            self.headers.append({'EXTNAME': m['extname'], 'XTENSION': m['extension']})
        #
        # Initial optional and required keywords.
        #
        self.optional = [set([k[0].split()[0] for k in h['keywords'] if self._o in k[0]]) for h in self._hdumeta]
        self.required = [set([k[0].split()[0] for k in h['keywords'] if self._o not in k[0]]) for h in self._hdumeta]
        self.in_all = [set() for h in self._hdumeta]
        self.in_none = [set() for h in self._hdumeta]
        self.col_in_all = [set() for h in self._hdumeta]
        self.col_in_none = [set() for h in self._hdumeta]
        #
        # Remove all optional markers from union set.
        #
        for h in self._hdumeta:
            for k in range(len(h['keywords'])):
                key = h['keywords'][k]
                if self._o in key[0]:
                    h['keywords'][k] = (key[0].split()[0], key[1], key[2], key[3])
            if h['extension'] == 'BINTABLE':
                for k in range(len(h['format'])):
                    col = h['format'][k]
                    if self._o in col[0]:
                        h['format'][k] = (col[0].split()[0], col[1], col[2], col[3])
        #
        # Placeholders
        #
        self.filename = self.model.filename
        self._basef = str(self.model.regexp).split('/')[-1].strip("')")
        self._modelname = self.model.title
        self._filetype = self.model.filetype
        self._filesize = self.model.filesize
        self._hduname = None
        self._contents = None
        return

    def add_keywords(self, hdu, keywords):
        """Search for missing keywords in `hdu` and add them if necessary.

        Parameters
        ----------
        hdu : :class:`int`
            The HDU number.
        keywords : :class:`list`
            List of keywords to compare to the internal set.
        """
        metadata = self.hdumeta[hdu]
        data_keywords = set([k[0] for k in keywords])
        model_keywords = set([k[0].split()[0] for k in metadata['keywords']])
        #
        # Compare the keywords that are in both sets.
        #
        common_keywords = data_keywords & model_keywords
        for kw in common_keywords:
            if kw not in self.in_all[hdu]:
                log.debug("self.in_all[%d].add('%s')", hdu, kw)
                self.in_all[hdu].add(kw)
            if kw in self.in_none[hdu]:
                log.debug("self.in_none[%d].remove('%s')", hdu, kw)
                self.in_none[hdu].remove(kw)
            meta_index = [i for i, k in enumerate(metadata['keywords']) if k[0] == kw][0]
            data_index = [i for i, k in enumerate(keywords) if k[0] == kw][0]
            original_keyword = metadata['keywords'][meta_index]
            foo, meta_example, meta_type, meta_comment = original_keyword
            foo, data_example, data_type, data_comment = keywords[data_index]
            new_keyword = original_keyword
            if data_example and not meta_example:
                log.info("Adding example '%s' to HDU%d keyword %s", data_example, hdu, kw)
                new_keyword = (kw, data_example, meta_type, meta_comment)
            if meta_type != data_type:
                log.warning("HDU%d keyword %s has different keyword type (%s != %s).",
                            hdu, kw, data_type, meta_type)
                new_keyword = (kw, new_keyword[1], data_type, new_keyword[3])
            if data_comment and not meta_comment:
                log.info("Adding comment '%s' to HDU%d keyword %s.", data_comment, hdu, kw)
                new_keyword = (kw, new_keyword[1], new_keyword[2], data_comment)
            if new_keyword != original_keyword:
                log.debug("metadata['keywords'][%d] = ('%s', '%s', '%s', '%s')",
                          meta_index, new_keyword[0], new_keyword[1], new_keyword[2], new_keyword[3])
                metadata['keywords'][meta_index] = new_keyword
        #
        # Add missing keywords to the union model.
        #
        if len(data_keywords - model_keywords) > 0:
            log.info('Adding keywords to HDU%d missing from model: %s', hdu,
                     str(data_keywords - model_keywords))
            for kw in (data_keywords - model_keywords):
                if kw not in self.in_all[hdu]:
                    log.debug("self.in_all[%d].add('%s')", hdu, kw)
                    self.in_all[hdu].add(kw)
                if kw in self.in_none[hdu]:
                    log.debug("self.in_none[%d].remove('%s')", hdu, kw)
                    self.in_none[hdu].remove(kw)
                data_index = [i for i, k in enumerate(keywords) if k[0] == kw][0]
                foo, data_example, data_type, data_comment = keywords[data_index]
                log.debug("metadata['keywords'].append(('%s', '%s', '%s', '%s'))",
                          kw, data_example, data_type, data_comment)
                metadata['keywords'].append((kw, data_example, data_type, data_comment))
        #
        # Subtract keywords not in the data for marking as optional.
        #
        if len(model_keywords - data_keywords) > 0:
            log.info('These keywords in HDU%d missing from data: %s', hdu,
                     str(model_keywords - data_keywords))
            for kw in (model_keywords - data_keywords):
                if kw in self.in_all[hdu]:
                    log.debug("self.in_all[%d].remove('%s')", hdu, kw)
                    self.in_all[hdu].remove(kw)
                if kw not in self.in_none[hdu]:
                    log.debug("self.in_none[%d].add('%s')", hdu, kw)
                    self.in_none[hdu].add(kw)
        return

    def add_columns(self, hdu, columns):
        """Search for missing columns in `hdu` and add them if necessary.

        Parameters
        ----------
        hdu : :class:`int`
            The HDU number.
        columns : :class:`list`
            List of columns to compare to the internal set.
        """
        metadata = self.hdumeta[hdu]
        #
        # The columns coming into here have the header row in them already.
        #
        data_columns = set([k[0] for k in columns[1:]])
        model_columns = set([k[0].split()[0] for k in metadata['format']])
        log.debug("data_columns = %s", data_columns)
        log.debug("model_columns = %s", model_columns)
        #
        # Compare the keywords that are in both sets.
        #
        common_columns = data_columns & model_columns
        for col in common_columns:
            if col not in self.col_in_all[hdu]:
                log.debug("self.col_in_all[%d].add('%s')", hdu, col)
                self.col_in_all[hdu].add(col)
            if col in self.col_in_none[hdu]:
                log.debug("self.col_in_none[%d].remove('%s')", hdu, col)
                self.col_in_none[hdu].remove(col)
            meta_index = [i for i, k in enumerate(metadata['format']) if k[0] == col][0]
            data_index = [i for i, k in enumerate(columns) if k[0] == col][0]
            original_column = metadata['format'][meta_index]
            foo, meta_type, meta_units, meta_comment = original_column
            foo, data_type, data_units, data_comment = columns[data_index]
            new_column = original_column
            if meta_type != data_type:
                log.warning("HDU%d column %s has different column type (%s != %s).",
                            hdu, col, data_type, meta_type)
                new_column = (col, data_type, new_column[2], new_column[3])
            if data_units and not meta_units:
                log.info("Adding unit '%s' to HDU%d column %s.", data_units, hdu, col)
                new_column = (col, new_column[1], data_units, new_column[3])
            # if data_comment and not meta_comment:
            #     log.info("Adding comment '%s' to HDU%d column %s", data_comment, hdu, col)
            #     new_column = (col, new_column[0], new_column[1], data_comment)
            if new_column != original_column:
                log.debug("metadata['format'][%d] = ('%s', '%s', '%s', '%s')",
                          meta_index, new_column[0], new_column[1], new_column[2], new_column[3])
                metadata['keywords'][meta_index] = new_keyword
        #
        # Add missing columns to the union model.
        #
        if len(data_columns - model_columns) > 0:
            log.info('Adding columns to HDU%d missing from model: %s', hdu,
                     str(data_columns - model_columns))
            for col in (data_columns - model_columns):
                if col not in self.col_in_all[hdu]:
                    log.debug("self.col_in_all[%d].add('%s')", hdu, col)
                    self.col_in_all[hdu].add(col)
                if col in self.col_in_none[hdu]:
                    log.debug("self.col_in_none[%d].remove('%s')", hdu, col)
                    self.col_in_none[hdu].remove(col)
                data_index = [i for i, k in enumerate(columns) if k[0] == col][0]
                foo, data_type, data_units, data_comment = columns[data_index]
                log.debug("metadata['format'].append(('%s', '%s', '%s', '%s'))",
                          col, data_type, data_units, data_comment)
                metadata['format'].append((col, data_type, data_units, data_comment))
        #
        # Subtract keywords not in the data for marking as optional.
        #
        if len(model_columns - data_columns) > 0:
            log.info('These columns in HDU%d missing from data: %s', hdu,
                     str(model_columns - data_columns))
            for col in (model_columns - data_columns):
                if col in self.col_in_all[hdu]:
                    log.debug("self.col_in_all[%d].remove('%s')", hdu, col)
                    self.col_in_all[hdu].remove(col)
                if col not in self.col_in_none[hdu]:
                    log.debug("self.col_in_none[%d].add('%s')", hdu, col)
                    self.col_in_none[hdu].add(col)
        return

    def mark_optional(self):
        """Mark the keywords and columns that do not appear in every file as optional.
        """
        for i, hdu in enumerate(self.hdumeta):
            for j, keyword in enumerate(hdu['keywords']):
                k = keyword[0]
                if k in self.in_all[i]:
                    log.debug("%s is a required keyword in HDU%d.", k, i)
                else:
                    if k in self.in_none[i]:
                        log.debug("%s is an unused keyword in HDU%d.", k, i)
                    else:
                        log.debug("%s is an optional keyword in HDU%d", k, i)
                        ko = k + ' ' + self._o
                        hdu['keywords'][j] = (ko, keyword[1], keyword[2], keyword[3])
            if hdu['extension'] == 'BINTABLE':
                for j, column in enumerate(hdu['format'][1:]):
                    k = column[0]
                    if k in self.col_in_all[i]:
                        log.debug("%s is a required column in HDU%d.", k, i)
                    else:
                        if k in self.col_in_none[i]:
                            log.debug("%s is an unused column in HDU%d.", k, i)
                        else:
                            log.debug("%s is an optional column in HDU%d", k, i)
                            ko = k + ' ' + self._o
                            hdu['format'][j] = (ko, column[1], column[2], column[3])
        return


def collect_files(root, model):
    """Scan a directory tree for all files that correspond to a data model files.

    Parameters
    ----------
    root : :class:`str`
        Path to real files on disk.
    model : :class:`~desidatamodel.check.DataModel`
        A data model file object.

    Returns
    -------
    :class:`list`
        All files in `root` that match `model`.
    """
    ignore_directories = ('logs', 'scripts')
    include_extensions = ('.fits', '.fits.fz', '.fits.gz')
    files = list()
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
            fullname = os.path.join(dirpath, f)
            m = model.regexp.match(fullname)
            if m is not None:
                files.append(fullname)
    return files


def union_metadata(model, stubs, error=False):
    """Combine all HDU metadata from `model` and `stubs`.

    Parameters
    ----------
    model : :class:`~desidatamodel.check.DataModel`
        The initial data model.
    stubs : :class:`list`
        A list of :class:`~desidatamodel.stub.Stub` objects.
    error : :class:`bool`, optional
        If ``True``, failure to extract certain required metadata raises an
        exception.

    Returns
    -------
    :class:`~desidatamodel.stub.Stub`
        A new :class:`~desidatamodel.stub.Stub` object containing the
        unified metadata of all the inputs.
    """
    log.debug("union = model.extract_metadata(error=%s)", error)
    modelmeta = model.extract_metadata(error=error)
    union = UnionStub(model, error=error)
    for s in stubs:
        if s.nhdr != len(modelmeta.keys()):
            log.warning("Data file %s has the wrong number of " +
                        "sections (HDUs) according to %s.",
                        s.filename, model.filename)
        stub_meta = s.hdumeta
        for i in range(s.nhdr):
            dexex = stub_meta[i]['extname']
            if dexex == '' and i > 0:
                log.warning("Data file %s has no EXTNAME in HDU%d.",
                            s.filename, i)
            try:
                modelhdumeta = modelmeta[dexex]
            except KeyError:
                try:
                    modelhdumeta = modelmeta['HDU{0:02d}'.format(i)]
                except KeyError:
                    #
                    # Fall back on trying to find HDU by number.
                    #
                    log.warning("Could not find EXTNAME = '%s' in %s; trying by HDU number.",
                                dexex, model.filename)
                    for key in modelmeta:
                        if modelmeta[key]['number'] == i:
                            modelhdumeta = modelmeta[key]
            #
            # Check for EXTNAME
            #
            mexex = modelhdumeta['extname']
            if (dexex != '' and mexex != '' and dexex != mexex):
                log.warning("Data file %s has an EXTNAME mismatch " +
                            "in HDU%d (%s != %s) " +
                            "according to %s.",
                            s.filename, i, dexex, mexex, model.filename)
            #
            # Collect keywords
            #
            union.add_keywords(i, stub_meta[i]['keywords'])
            #
            # Collect columns
            #
            if modelhdumeta['extension'] == 'BINTABLE':
                union.add_columns(i, stub_meta[i]['format'])
    #
    # Mark keywords and columns that don't appear in every file as optional.
    #
    union.mark_optional()
    return union


def _options():
    """Parse command-line options.

    Returns
    -------
    :class:`~argparse.Namespace`
        The parsed options.
    """
    desc = """Deep scan available files to obtain a comprehensive set of metadata.
"""
    parser = ArgumentParser(description=desc, prog=os.path.basename(argv[0]))
    parser.add_argument('-d', '--datamodel-dir', dest='desidatamodel',
                        metavar='DIR',
                        help='Override the value of DESIDATAMODEL.')
    parser.add_argument('-l', '--path-level', dest='level', metavar='N', type=int, default=0,
                        help='Map data directory to data model at N levels down (default %(default)s).')
    parser.add_argument('-n', '--number', dest='number', metavar='N', type=int, default=100,
                        help='Scan at most N files (default %(default)s).')
    # parser.add_argument('-F', '--compare-files', dest='files',
    #                     action='store_true',
    #                     help='Compare an individual data model to an individual file.')
    # parser.add_argument('-K', '--skip-keywords', dest='skip_keywords', action='store_true',
    #                     help="Don't check FITS header keywords")
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true',
                        help='Set log level to DEBUG.')
    parser.add_argument('-W', '--warning-is-error', dest='error',
                        action='store_true',
                        help='Data model warnings raise exceptions.')
    parser.add_argument('section', metavar='MODEL_FILE',
                        help='Individual data model file.')
    parser.add_argument('directory', metavar='DATA_DIR',
                        help='Check files in this top-level directory that match MODEL_FILE.')
    options = parser.parse_args()
    return options


def main():
    """Entry point for the deep_scan_metadata script.

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
    filename = os.path.join(data_model_root, 'doc', options.section)
    section = os.path.join(data_model_root, 'doc', '/'.join(options.section.split('/')[:(options.level+1)]))
    log.info("Loading individual data model: %s.", filename)
    log.debug("model = DataModel('%s', '%s')", filename, section)
    model = DataModel(filename, section)
    log.info("Processing regular expression.")
    log.debug("model.get_regexp('%s', error=%s)", options.directory, options.error)
    model.get_regexp(options.directory, error=options.error)
    log.debug("model.regexp = %s", model.regexp)
    log.info("Finding scannable files for %s in %s.", filename, options.directory)
    all_files = collect_files(options.directory, model)
    n_files = len(all_files)
    if n_files == 0:
        log.critical("No files found matching %s!", filename)
        return 1
    log.info("Found %d files matching %s.", n_files, filename)
    if n_files > options.number:
        log.info("Randomly down-sampling files to %d.", options.number)
        all_files = choices(all_files, k=options.number)
        n_files = len(all_files)
    try:
        stubs = [Stub(f, error=options.error) for f in all_files]
    except DataModelError:
        log.critical("Error detected while loading files!")
        return 1
    u = union_metadata(model, stubs, error=options.error)
    print(str(u))
    return 0
