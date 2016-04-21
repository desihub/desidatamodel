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
                if l.startswith('regex:'):
                    d = dirname(f).replace(section, root)
                    for k in d2r:
                        d = d.replace(k, d2r[k])
                    r = l.strip().split()[1].replace('``', '')
                    f2r[f] = re.compile(join(d, r))
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
    :func:`tuple`
        A tuple containing the prototype files and a list of extraneous files
        (defined below).

    Raises
    ------
    :class:`~desimodel.DataModelWarning`
        If 'missing' files are detected (defined below).

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
    extraneous = list()
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
                extraneous.append(fullname)
    #
    # Scan for missing files, but don't penalize (here) data models that
    # don't have a valid regular expression.  Files with bad regexes will
    # be flagged elsewhere.
    #
    for r in regexes:
        if regexes[r] is not None and r not in prototypes:
            warn("No files found matching {0}!".format(r), DataModelWarning)
    return (prototypes, extraneous)


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
    f2r = files_to_regex(scan_root, options.directory, files)
    # print([f2r[p].pattern for p in f2r])
    p, e = collect_files(options.directory, f2r)
    print(p)
    print(e)
    return 0
