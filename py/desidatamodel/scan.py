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
            self.headers.append({'EXTNAME': m['extname']})
        #
        # Placeholders
        #
        self.filename = None
        self._basef = None
        self._modelname = None
        self._filesize = None
        self._hduname = None
        self._contents = None
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
            data_keywords = set([tmp[0] for tmp in stub_meta[i]['keywords']])
            model_keywords = set([tmp[0].split()[0] for tmp in modelhdumeta['keywords'] if '[1]_' not in tmp[0]])
            optional_keywords = set([tmp[0].split()[0] for tmp in modelhdumeta['keywords'] if '[1]_' in tmp[0]])
            if len(data_keywords - (model_keywords | optional_keywords)) > 0:
                log.warning('Data file %s has these keywords in HDU%d missing from model: %s',
                            s.filename, i, str(data_keywords - (model_keywords | optional_keywords)))
            if len(model_keywords - data_keywords) > 0:
                log.warning('Model file %s has these keywords in HDU%d missing from data: %s',
                            model.filename, i, str(model_keywords - data_keywords))
            #
            # Compare the keywords that are in both sets.
            #
            common_keywords = data_keywords & (model_keywords | optional_keywords)
            for kw in common_keywords:
                mkw_type = [tmp[2] for tmp in modelhdumeta['keywords'] if tmp[0].split()[0] == kw][0]
                dkw_type = [tmp[2] for tmp in stub_meta[i]['keywords'] if tmp[0] == kw][0]
                mkw_comment = [tmp[3] for tmp in modelhdumeta['keywords'] if tmp[0].split()[0] == kw][0]
                dkw_comment = [tmp[3] for tmp in stub_meta[i]['keywords'] if tmp[0] == kw][0]
                if mkw_type != dkw_type:
                    log.warning("File %s HDU%d keyword %s has different keyword type according to %s (%s != %s).",
                                s.filename, i, kw, model.filename, dkw_type, mkw_type)
                if mkw_comment != dkw_comment:
                    log.warning("File %s HDU%d keyword %s has different comment according to %s ('%s' != '%s').",
                                s.filename, i, kw, model.filename, dkw_comment, mkw_comment)


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
    return 0
