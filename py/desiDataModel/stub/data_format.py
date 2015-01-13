# License information goes here
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
# The line above will help with 2to3 support.
def data_format(hdr):
    """Decide which kind of header this is, and print its data format

    Parameters
    ----------
    hdr : an object returned by the fitsio method ``read_header()``
        The header to parse.

    Returns
    -------
    data_format : list
        A list of strings that can be appended to the main document.
    """
    from . import binary_table_format
    section = list()
    if 'XTENSION' in hdr:
        if hdr['XTENSION'].strip() == 'BINTABLE':
            section += binary_table_format(hdr)
        elif hdr['XTENSION'].strip() == 'IMAGE':
            datatype = ''
            if 'BITPIX' in hdr.keys():
                bitpix = hdr['BITPIX']
                if bitpix == 8:
                    datatype = '[char]'
                elif bitpix == 16:
                    datatype = '[int16]'
                elif bitpix == 32:
                    datatype = '[int32]'
                elif bitpix == -32:
                    datatype = '[float32]'
                elif bitpix == -64:
                    datatype = '[float64]'
                else:
                    datatype = '[BITPIX={}]'.format(bitpix)
                    
            section.append('Data: FITS image '+datatype)
            section.append('')
        else:
            section.append("Unknown extension type {0}".format(hdr['XTENSION']))
            section.append('')
    return section
