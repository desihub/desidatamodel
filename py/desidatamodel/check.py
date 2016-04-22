# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""
===================
desidatamodel.check
===================

Check actual files against the data model for validity.
"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
# The line above will help with 2to3 support.


def scan_model(section):
    """Find all data model files in a top-level directory.

    Parameters
    ----------
    section : :class:`str`
        Full path to a section of the data model.

    Returns
    -------
    :class:`list`
        The data model files found
    """
    from os import walk
    from os.path import join
    scan = list()
    for dirpath, dirnames, filenames in walk(section):
        scan += [join(dirpath, f) for f in filenames
                 if f.endswith('.rst') and f != 'index.rst']
    return scan


def files_to_regex(section, root, files):
    """Convert a list of data model files into a list of regular expressions.

    Parameters
    ----------
    section : :class:`str`
        Section of the data model.
    root : :class:`str`
        Path to real files on disk.
    files : :class:`list`
        List of files obtained from the data model.

    Returns
    -------
    :class:`dict`
        A mapping of data model file name to regular expression.

    Raises
    ------
    :class:`~desidatamodel.DataModelWarning`
        If data model files with malformed regular expressions are detected.
    """
    from . import PY3, DataModelWarning
    from warnings import warn
    from os.path import dirname, join
    import re
    d2r = {'NIGHT': '[0-9]{8}',  # YYYYMMDD
           'EXPID': '[0-9]{8}'}  # YYYYMMDD
    f2r = dict()
    for f in files:
        f2r[f] = None
        with open(f) as dm:
            for le in dm.readlines():
                if PY3:
                    l = le
                else:
                    l = le.decode('utf-8')
                if l.startswith(':Regex:'):
                    d = dirname(f).replace(section, root)
                    for k in d2r:
                        d = d.replace(k, d2r[k])
                    r = l.strip().split()[1].replace('``', '')
                    f2r[f] = re.compile(join(d, r))
                    break
        if f2r[f] is None:
            warn("{0} has no file regex!".format(f), DataModelWarning)
    return f2r


def collect_files(root, regexes):
    """Scan a directory tree for files that correspond to data model files.

    Parameters
    ----------
    root : :class:`str`
        Path to real files on disk.
    regexes : :class:`dict`
        A mapping of data model files to regular expressions that match.

    Returns
    -------
    :class:`dict`
        A dictionary mapping data model files to the prototype files.

    Raises
    ------
    :class:`~desimodel.DataModelWarning`
        If 'missing' or 'extraneous' files are detected (defined below).

    Notes
    -----
    Files are analyzed using this algorithm:

    * The first file that matches a regex becomes the 'prototype' for that
      data model file.
    * If no files match a data model file, then files of that type are
      'missing'.
    * If a file does not match any regular expression, it is 'extraneous'.
    * If a file matches a regular expression that already has a prototype,
      it is 'ignored'.
    """
    from warnings import warn
    from . import DataModelWarning
    from os import walk
    from os.path import join
    prototypes = dict()
    for dirpath, dirnames, filenames in walk(root):
        for f in filenames:
            extraneous_file = True
            fullname = join(dirpath, f)
            for r in regexes:
                if regexes[r] is not None:
                    m = regexes[r].match(fullname)
                    if m is not None:
                        extraneous_file = False
                        if r not in prototypes:
                            prototypes[r] = fullname
            if extraneous_file:
                warn("Extraneous file detected: {0}".format(fullname),
                     DataModelWarning)
    #
    # Scan for missing files, but don't penalize (here) data models that
    # don't have a valid regular expression.  Files with bad regexes will
    # be flagged elsewhere.
    #
    for r in regexes:
        if regexes[r] is not None and r not in prototypes:
            warn("No files found matching {0}!".format(r), DataModelWarning)
    return prototypes


def extract_metadata(filename):
    """Extract metadata from a data model file.

    Parameters
    ----------
    filename : :class:`str`
        Name of a data model file.

    Returns
    -------
    :class:`list`
        Metadata in a form similar to :class:`~desidatamodel.stub.Stub`
        metadata.
    """
    import re
    with open(filename) as f:
        data = f.read()
    lines = data.split('\n')
    hduline = re.compile(r'HDU\d+$')
    tableboundary = re.compile(r'[= ]+$')
    hdu_sections = [i for i, l in enumerate(lines)
                    if hduline.match(l) is not None]
    hdumeta = list()
    for k in range(len(hdu_sections)):
        try:
            section = lines[hdu_sections[k]:hdu_sections[k+1]]
        except IndexError:
            section = lines[hdu_sections[k]:]
        meta = dict()
        meta['title'] = section[0]
        try:
            meta['extname'] = [l.split()[2] for l in section
                               if l.startswith('EXTNAME = ')][0]
        except IndexError:
            meta['extname'] = ''
        try:
            rhk = section.index('Required Header Keywords')
        except ValueError:
            meta['keywords'] = []
        else:
            table = [i for i, l in enumerate(section[rhk:])
                     if tableboundary.match(l) is not None][1:3]
            columns = list(map(len, section[rhk:][table[0]].split()))
            table_lines = section[rhk:][table[0]+1:table[1]]
            meta['keywords'] = [extract_columns(t, columns)
                                for t in table_lines]
        hdumeta.append(meta)
    return hdumeta


def extract_columns(row, columns):
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
    data = [row[lbound[i]:ubound[i]].strip() for i in range(len(columns))]
    return tuple(data)


def validate_prototypes(prototypes):
    """Compares a set of prototype data files to their data models.

    Parameters
    ----------
    prototypes : :class:`dict`
        A mapping of data model files to prototype data files.

    Returns
    -------
    None
    """
    from warnings import warn
    from .stub import Stub
    from . import DataModelWarning
    for p in prototypes:
        stub = Stub(prototypes[p])
        modelmeta = extract_metadata(p)
        if stub.nhdr == len(modelmeta):
            for i in range(stub.nhdr):
                nk = len(stub.hdumeta[i]['keywords'])
                nm = len(modelmeta[i]['keywords'])
                if nk > 0:
                    if nk == nm:
                        for j in range(nk):
                            if (stub.hdumeta[i]['keywords'][j][0] !=
                                modelmeta[i]['keywords'][j][0]):
                                w = ("Prototype file {0} has a keyword " +
                                     "mismatch ({1} != {2}) according to " +
                                     "{3}").format(prototypes[p],
                                                   stub.hdumeta[i]['keywords'][j][0],
                                                   modelmeta[i]['keywords'][j][0],
                                                   p)
                                warn(w, DataModelWarning)
                    else:
                        w = ("Prototype file {0} has the wrong number of " +
                             "HDU{1:d} keywords according to " +
                             "{2}.").format(prototypes[p], i, p)
                        warn(w, DataModelWarning)
        else:
            w = ("Prototype file {0} has the wrong number of headers " +
                 "according to {1}.").format(prototypes[p], p)
            warn(w, DataModelWarning)
    return


def main():
    """Entry point for the check_model script.

    Returns
    -------
    :class:`int`
        An integer suitable for passing to :func:`sys.exit`.
    """
    from os import environ
    from os.path import basename, join
    from sys import argv
    from argparse import ArgumentParser
    from warnings import catch_warnings
    desc = """Check actual files against the data model for validity.
"""
    parser = ArgumentParser(description=desc, prog=basename(argv[0]))
    parser.add_argument('-d', '--datamodel-dir', dest='desidatamodel',
                        metavar='DIR',
                        help='Override the value of DESIDATAMODEL.')
    parser.add_argument('root', metavar='DIR',
                        help='Set the section of the data model.')
    parser.add_argument('directory', metavar='DIR',
                        help='Check files in this top-level directory.')
    options = parser.parse_args()
    if 'DESIDATAMODEL' in environ:
        data_model_root = environ['DESIDATAMODEL']
    else:
        if options.desidatamodel is not None:
            data_model_root = options.desidatamodel
        else:
            print(("DESIDATAMODEL is not defined. " +
                   "Cannot find data model files!"))
            return 1
    scan_root = join(data_model_root, 'doc', options.root)
    files = scan_model(scan_root)
    # print(files)
    with catch_warnings(record=True) as w:
        f2r = files_to_regex(scan_root, options.directory, files)
        p = collect_files(options.directory, f2r)
        validate_prototypes(p)
    if len(w) > 0:
        for m in w:
            print('WARNING: ' + str(m.message))
    return 0
