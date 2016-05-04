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
    d2r = {'BRICKNAME': '[0-9]+[pm][0-9]+',  # e.g. 3319p140
           'EXPID': '[0-9]{8}',  # YYYYMMDD
           'NIGHT': '[0-9]{8}',  # YYYYMMDD
           'PIXPROD': '[a-z0-9_-]+',  # e.g. alpha-3
           'PRODNAME': '[a-z0-9_-]+',  # e.g. dc3c
           'SPECPROD': '[a-z0-9_-]+',  # replacement for PRODNAME
           }
    f2r = dict()
    rline = re.compile(r':?regexp?:', re.I)
    for f in files:
        f2r[f] = None
        with open(f) as dm:
            for le in dm.readlines():
                if PY3:
                    l = le
                else:
                    l = le.decode('utf-8')
                if rline.match(l) is not None:
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
    from . import PY3
    import re
    with open(filename) as f:
        data = f.read()
        if not PY3:
            data = data.decode('utf-8')
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
                     if tableboundary.match(l) is not None][1:3]
            columns = list(map(len, section[rdtc:][table[0]].split()))
            table_lines = section[rdtc:][table[0]+1:table[1]]
            meta['format'] = [extract_columns(t, columns)
                              for t in table_lines]
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
    :class:`list`
        A list of warning messages.  If there were no warnings, the list
        will be empty.
    """
    from .stub import Stub
    wlist = list()
    for p in prototypes:
        stub = Stub(prototypes[p])
        modelmeta = extract_metadata(p)
        #
        # Check number of headers.
        #
        if stub.nhdr != len(modelmeta):
            w = ("Prototype file {0} has the wrong number of headers " +
                 "according to {1}.").format(prototypes[p], p)
            wlist.append(w)
            continue
        for i in range(stub.nhdr):
            dkw = stub.hdumeta[i]['keywords']
            mkw = modelmeta[i]['keywords']
            #
            # Check number of keywords.
            #
            if len(dkw) != len(mkw):
                w = ("Prototype file {0} has the wrong number of " +
                     "HDU{1:d} keywords according to " +
                     "{2}.").format(prototypes[p], i, p)
                wlist.append(w)
                continue
            #
            # If number of keywords is correct, check them individually.
            #
            for j in range(len(dkw)):
                if dkw[j][0] != mkw[j][0]:
                    w = ("Prototype file {0} has a keyword " +
                         "mismatch ({1} != {2}) in HDU{3:d} according to " +
                         "{3}.").format(prototypes[p],
                                        dkw[j][0], mkw[j][0], i, p)
                    wlist.append(w)
            #
            # Check the extension type.
            #
            dex = stub.hdumeta[i]['extension']
            mex = modelmeta[i]['extension']
            if dex != mex:
                w = ("Prototype file {0} has an extension type mismatch in " +
                     "HDU{1:d} ({2} != {3}) " +
                     "according to {4}.").format(protoypes[p], i, dex, mex, p)
                wlist.append(w)
                continue
            #
            # If the extension type is correct, check the contents of the
            # extension.
            #
            dexf = stub.hdumeta[i]['format']
            mexf = modelmeta[i]['format']
            if dex == 'IMAGE':
                if dexf != mexf:
                    w = ("Prototype file {0} has an extension format " +
                         "mismatch in HDU{1:d} " +
                         "according to {2}.").format(prototypes[p], i, p)
                    wlist.append(w)
            else:
                dexf = dexf[1:]  # Get rid of header line.
                if len(dexf) != len(mexf):
                    w = ("Prototype file {0} has the wrong number of " +
                         "HDU{1:d} columns according to " +
                         "{2}.").format(prototypes[p], i, p)
                    wlist.append(w)
                else:
                    for j in range(len(dexf)):
                        if dexf[j][0] != mexf[j][0]:
                            w = ("Prototype file {0} has a column name " +
                                 "mismatch ({1} != {2}) in HDU{3:d} " +
                                 "according to {3}.").format(prototypes[p],
                                                             dexf[j][0],
                                                             mexf[j][0], i, p)
                            wlist.append(w)
    return wlist


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
    if len(w) > 0:
        for m in w:
            print('WARNING: ' + str(m.message))
    w = validate_prototypes(p)
    if len(w) > 0:
        for m in w:
            print('WARNING: ' + m)
    return 0
