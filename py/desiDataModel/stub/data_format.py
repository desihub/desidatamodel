# License information goes here
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
# The line above will help with 2to3 support.
def data_format(hdr,div):
    """Decide which kind of header this is, and print its data format

    Parameters
    ----------
    hdr : an object returned by the fitsio method ``read_header()``
        The header to parse.
    div : xml.etree.ElementTree.Element
        A representation of the div that will contain the information.

    Returns
    -------
    None
    """
    from . import get_uri
    uri = get_uri(div)
    if 'XTENSION' in hdr:
        if hdr['XTENSION'].strip() == 'BINTABLE':
            binary_table_format(hdr,div)
        elif hdr['XTENSION'].strip() == 'IMAGE':
            p = ET.SubElement(div,'{0}p'.format(uri))
            p.text = 'Data: FITS image'
            p.tail = '\n'
        else:
            p = ET.SubElement(div,'{0}p'.format(uri))
            p.text = "Unknown extension type {0}".format(hdr['XTENSION'])
            p.tail = '\n'
    return
