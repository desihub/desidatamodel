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


def scan_model(root):
    """Find all data model files in a top-level directory.

    Parameters
    ----------
    root : :class:`str`
        Directory to scan.

    Returns
    -------
    :class:`list`
        The data model files found
    """
    from os import walk
    from os.path import join
    scan = list()
    for dirpath, dirnames, filenames in walk(root):
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
    from . import PY3
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
    return f2r


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
    print(files)
    f2r = files_to_regex(scan_root, options.directory, files)
    print([f2r[p].pattern for p in f2r])
    return 0
