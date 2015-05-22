# License information goes here
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
# The line above will help with 2to3 support.
#
#- Adapted from stackoverflow answers for human readable size formatting
#
def file_size(filename):
    """Determine file size and return string with human readable size format.

    Parameters
    ----------
    filename : str
        A string containing a filename.

    Returns
    -------
    file_size : str
        A human-readable file size.

    Examples
    --------
    >>> file_size('one-gb-file.dat')
    '1 GB'
    """
    from os.path import getsize
    n = getsize(filename)
    for unit in ['bytes','KB','MB','GB']:
        if n < 1024:
            return "{0:d} {1}".format(int(n), unit)
        else:
            n /= 1024.0
    return "{0:3.1f} {1}".format(n, 'TB')
