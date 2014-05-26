# License information goes here
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
# The line above will help with 2to3 support.
def binary_table_format(hdr,div):
    """Print format of binary table

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
    import xml.etree.ElementTree as ET
    from . import get_uri
    uri = get_uri(div)
    table = ET.SubElement(div,'{0}table'.format(uri),attrib={'class':'columns'})
    table.text='\n'
    table.tail='\n\n'
    caption = ET.SubElement(table,'{0}caption'.format(uri))
    caption.text = 'Required Data Table Columns'
    caption.tail='\n'
    tr = ET.SubElement(table,'{0}tr'.format(uri))
    tr.tail='\n'
    for k in ('Name','Type','Units','Description'):
        th = ET.SubElement(tr,'{0}th'.format(uri))
        th.text = k
    for j in range(1, hdr['TFIELDS']+1):
        #- Check TCOMMnn keyword, otherwise use TTYPE comment for description
        commkey = 'TCOMM{0}'.format(j)
        if commkey in hdr:
            description = escape(hdr[commkey])
        else:
            description = escape(hdr.get_comment('TTYPE{0}'.format(j)))

        ### print(j, hdr['TTYPE{0}'.format(j)], hdr['TFORM{0}'.format(j)] )
        cols = dict(Name = hdr['TTYPE{0}'.format(j)].strip(),
                    Type = fits_column_format(hdr['TFORM{0}'.format(j)].strip()),
                    Description = description,
                    Units = ''
                    )
        tunit = 'TUNIT{0}'.format(j)
        if tunit in hdr:
            cols['Units'] = hdr[tunit]
        tr = ET.SubElement(table,'{0}tr'.format(uri))
        tr.tail='\n'
        for k in ('Name','Type','Units','Description'):
            td = ET.SubElement(tr,'{0}td'.format(uri))
            if cols[k] == '':
                td.text = ' '
            else:
                td.text = cols[k]
    return
