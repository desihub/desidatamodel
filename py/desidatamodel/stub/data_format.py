# Licensed under a 3-clause BSD style license - see LICENSE.rst
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
            if 'BITPIX' in hdr:
                bitmap = {8:'char',16:'int16',32:'int32',64:'int64',-32:'float32',-64:'float64'}
                try:
                    datatype = bitmap[hdr['BITPIX']]
                except KeyError:
                    datatype = 'BITPIX={}'.format(hdr['BITPIX'])
            section.append('Data: FITS image [{0}]'.format(datatype))
            section.append('')
        else:
            section.append("Unknown extension type {0}".format(hdr['XTENSION']))
            section.append('')
    return section
