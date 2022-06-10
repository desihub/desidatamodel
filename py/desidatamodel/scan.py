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
from collections import Counter

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
    count : :class:`int`
        Number of files that will be examined. This is used to determine
        whether a keyword or column is mandatory, optional or unused.
    error : :class:`bool`, optional
        If ``True``, failure to extract certain required metadata raises an
        exception.
    """
    _o = '[1]_'  # Marker for optional keywords and columns.

    def __init__(self, model, count, error=False):
        self.model = model
        self.count = count
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
        # self.optional = [set([k[0].split()[0] for k in h['keywords'] if self._o in k[0]]) for h in self._hdumeta]
        # self.required = [set([k[0].split()[0] for k in h['keywords'] if self._o not in k[0]]) for h in self._hdumeta]
        self.counter = [{'keywords': Counter(), 'format': Counter()} for h in self._hdumeta]
        #
        # Remove all optional markers from union set.
        #
        for h in self._hdumeta:
            for k in range(len(h['keywords'])):
                key = h['keywords'][k]
                if self._o in key[0]:
                    h['keywords'][k] = (key[0].split()[0], key[1], key[2], key[3])
            if h['extension'] == 'BINTABLE':
                if h['format'][0] != Stub.columns_header:
                    h['format'] = [Stub.columns_header] + h['format']
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
        self._filetype = self.model.filetype.upper()
        self._filesize = self.model.filesize
        self._hduname = None
        self._contents = None
        return

    def update(self, hdu, data, columns=False):
        """Search for missing keywords or columns in `hdu` and add them if necessary.

        Parameters
        ----------
        hdu : :class:`int`
            The HDU number.
        data : :class:`list`
            List of keywords or columns to compare to the internal set.
        columns : :class:`bool`, optional
            If ``True``, `data` represents BINTABLE columns, rather than keywords.
        """
        metadata = self.hdumeta[hdu]
        m = 'keywords'
        it = 'keywords'
        data_set = set([k[0] for k in data])
        if columns:
            m = 'format'
            it = 'columns'
            try:
                data_set.remove('Name')
            except KeyError:
                pass
        model_set = set([k[0] for k in metadata[m]])
        try:
            model_set.remove('Name')
        except KeyError:
            pass
        #
        # Compare the items that are in both sets.
        #
        common_set = data_set & model_set
        for item in common_set:
            if item in self.counter[hdu][m]:
                self.counter[hdu][m][item] += 1
            else:
                self.counter[hdu][m][item] = 1
            meta_index = [i for i, k in enumerate(metadata[m]) if k[0] == item][0]
            data_index = [i for i, k in enumerate(data) if k[0] == item][0]
            original_item = metadata[m][meta_index]
            new_item = original_item
            if columns:
                foo, meta_type, meta_units, meta_comment = original_item
                foo, data_type, data_units, data_comment = data[data_index]
                if meta_type != data_type:
                    log.warning("HDU%d column %s has different type (%s != %s).",
                                hdu, item, data_type, meta_type)
                    new_item = (item, data_type, new_item[2], new_item[3])
                if data_units and not meta_units:
                    log.info("Adding unit '%s' to HDU%d column %s.", data_units, hdu, item)
                    new_item = (item, new_item[1], data_units, new_item[3])
                # if data_comment and not meta_comment:
                #     log.info("Adding comment '%s' to HDU%d column %s", data_comment, hdu, item)
                #     new_item = (item, new_item[1], new_item[2], data_comment)
            else:
                foo, meta_example, meta_type, meta_comment = original_item
                foo, data_example, data_type, data_comment = data[data_index]
                if data_example and not meta_example:
                    log.info("Adding example '%s' to HDU%d keyword %s.", data_example, hdu, item)
                    new_item = (item, data_example, new_item[2], new_item[3])
                if meta_type != data_type:
                    log.warning("HDU%d keyword %s has different type (%s != %s).",
                                hdu, item, data_type, meta_type)
                    new_item = (item, new_item[1], data_type, new_item[3])
                if data_comment and not meta_comment:
                    log.info("Adding comment '%s' to HDU%d keyword %s.", data_comment, hdu, item)
                    new_item = (item, new_item[1], new_item[2], data_comment)
            if new_item != original_item:
                log.debug("metadata['%s'][%d] = ('%s', '%s', '%s', '%s')",
                          m, meta_index, new_item[0], new_item[1], new_item[2], new_item[3])
                metadata[m][meta_index] = new_item
        #
        # Add missing items to the union model.
        #
        if len(data_set - model_set) > 0:
            log.info('Adding %s to HDU%d missing from model: %s', it, hdu,
                     str(data_set - model_set))
            for item in (data_set - model_set):
                if item not in self.counter[hdu][m]:
                    self.counter[hdu][m][item] = 1
                data_index = [i for i, k in enumerate(data) if k[0] == item][0]
                data[data_index]
                foo, data_type, data_units, data_comment = data[data_index]
                log.debug("metadata['%s'].append(('%s', '%s', '%s', '%s'))",
                          it, item, data[data_index][1], data[data_index][2], data[data_index][3])
                metadata[m].append((item, data[data_index][1], data[data_index][2], data[data_index][3]))
        #
        # Subtract keywords not in the data for marking as optional.
        #
        if len(model_set - data_set) > 0:
            log.info('These %s in HDU%d missing from data: %s', it, hdu,
                     str(model_set - data_set))
            for item in (model_set - data_set):
                if item not in self.counter[hdu][m]:
                    self.counter[hdu][m][item] = 0
        return

    def mark_optional(self):
        """Mark the keywords and columns that do not appear in every file as optional.
        """
        for i, hdu in enumerate(self.hdumeta):
            for j, keyword in enumerate(hdu['keywords']):
                k = keyword[0]
                if self.counter[i]['keywords'][k] == self.count:
                    log.debug("%s is a required keyword in HDU%d.", k, i)
                elif self.counter[i]['keywords'][k] > 0:
                    log.debug("%s is an optional keyword in HDU%d (%d).", k, i, self.counter[i]['keywords'][k])
                    ko = k + ' ' + self._o
                    hdu['keywords'][j] = (ko, keyword[1], keyword[2], keyword[3])
                else:
                    log.debug("%s is an unused keyword in HDU%d.", k, i)
                    hdu['keywords'][j] = (k, '**UNUSED**', keyword[2], keyword[3])
            if hdu['extension'] == 'BINTABLE':
                for j, column in enumerate(hdu['format']):
                    if j == 0:
                        continue
                    c = column[0]
                    if self.counter[i]['format'][c] == self.count:
                        log.debug("%s is a required column in HDU%d.", c, i)
                    elif self.counter[i]['format'][c] > 0:
                        log.debug("%s is an optional column in HDU%d (%d).", c, i, self.counter[i]['format'][c])
                        co = c + ' ' + self._o
                        hdu['format'][j] = (co, column[1], column[2], column[3])
                    else:
                        log.debug("%s is an unused column in HDU%d.", c, i)
                        hdu['format'][j] = (c, column[1], column[2], '**UNUSED**')
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
    union = UnionStub(model, len(stubs), error=error)
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
            union.update(i, stub_meta[i]['keywords'])
            #
            # Collect columns
            #
            if modelhdumeta['extension'] == 'BINTABLE':
                union.update(i, stub_meta[i]['format'], columns=True)
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
    parser.add_argument('-o', '--output', dest='output', metavar='FILE',
                        help='Specify output file or directory. Defaults to the name of the input file in the current directory.')
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
    if options.output is None:
        outfile = os.path.join('.', os.path.basename(options.section))
    elif os.path.isdir(options.output):
        outfile = os.path.join(os.path.realpath(options.output), os.path.basename(options.section))
    else:
        outfile = options.output
    with open(outfile, 'w') as f:
        f.write(str(u))
    return 0
