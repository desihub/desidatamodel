# License information goes here
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
# The line above will help with 2to3 support.
def fits_column_format(format):
    """Convert a FITS column format to a human-readable form.

    Parameters
    ----------
    format : str
        A FITS-style format string.

    Returns
    -------
    fits_column_format : str
        A human-readable version of the format string.

    Examples
    --------
    >>> fits_column_format('A')
    'char[1]'
    >>> fits_column_format('J')
    'int32'
    >>> fits_column_format('12E')
    'float32[12]'
    """
    fitstype=format[-1]
    if fitstype == 'A' and len(format) == 1:
        return 'char[1]'
    fmap = {'A':'char','I':'int16','J':'int32','K':'int64',
        'E':'float32','D':'float64', 'B':'bool'}
    if len(format) > 1:
        return fmap[fitstype] + '[' + format[0:len(format)-1] + ']'
    else:
        return fmap[fitstype]
