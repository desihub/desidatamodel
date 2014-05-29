# License information goes here
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
# The line above will help with 2to3 support.
def extrakey(key):
    """Return True if key is not a boring standard FITS keyword.

    To make the data model more human readable, we don't overwhelm the output
    with required keywords which are required by the FITS standard anyway.
    This list isn't exhaustive.

    Parameters
    ----------
    key : str
        A FITS keyword.

    Returns
    -------
    extrakey : bool
        ``True`` if the keyword is not boring.

    Examples
    --------
    >>> extrakey('SIMPLE')
    False
    >>> extrakey('BZERO')
    True
    """
    from re import match
    if match(r'TTYPE\d+', key) is not None:
        return False
    if match(r'TFORM\d+', key) is not None:
        return False
    if match(r'TUNIT\d+', key) is not None:
        return False
    if match(r'TCOMM\d+', key) is not None:
        return False
    if key in ('BITPIX', 'NAXIS', 'NAXIS1', 'NAXIS2', 'PCOUNT', 'GCOUNT',
        'TFIELDS', 'XTENSION', 'SIMPLE', 'EXTEND', 'COMMENT', 'HISTORY'):
        return False
    return True
