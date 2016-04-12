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


def main():
    """Entry point for the check_model script.

    Returns
    -------
    :class:`int`
        An integer suitable for passing to :func:`sys.exit`.
    """
    from os.path import basename
    from sys import argv
    desc = """Check actual files against the data model for validity.
"""
    parser = ArgumentParser(description=desc, prog=basename(argv[0]))
    parser.add_argument('-r', '--root', metavar='DIR',
                        help='Set the section of the data model.')
    parser.add_argument('directory', metavar='DIR',
                        help='Check files in this top-level directory.')
    options = parser.parse_args()
    scan_model(options.root)
    return 0
