# License information goes here
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
# The line above will help with 2to3 support.
def parse_header(hdr,div):
    """Create a table of header keywords, omitting those required by FITS anyway.

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
    from cgi import escape
    from . import data_format, extrakey, get_uri
    uri = get_uri(div)
    keywords = list()
    for key in hdr.keys():
        if extrakey(key):
            #- Escape &, <, >, in strings, but don't choke on int/float
            value = hdr[key]
            if isinstance(value, str):
                value = escape(value)
                if value == 'T' or value == 'F':
                    ktype = 'bool'
                else:
                    ktype = 'str'
            if isinstance(value, int):
                value = str(value)
                ktype = 'int'
            if isinstance(value, float):
                value = str(value)
                ktype = 'float'
            keywords.append(dict(KEY=key, Value=value, Type=ktype,
                Comment=escape(hdr.get_comment(key))) )
    if len(keywords) == 0:
        p = ET.SubElement(div,'{0}p'.format(uri))
        p.text = 'This HDU has no non-standard required keywords.'
        p.tail = '\n'
    else:
        table = ET.SubElement(div,'{0}table'.format(uri),attrib={'class':'header'})
        table.text='\n'
        table.tail='\n\n'
        caption = ET.SubElement(table,'{0}caption'.format(uri))
        caption.text='Required Header Keywords'
        caption.tail='\n'
        tr = ET.SubElement(table,'{0}tr'.format(uri))
        tr.tail='\n'
        for k in ('KEY','Value','Type','Comment'):
            th = ET.SubElement(tr,'{0}th'.format(uri))
            th.text= k
        for kw in keywords:
            tr = ET.SubElement(table,'{0}tr'.format(uri))
            tr.tail='\n'
            for k in ('KEY','Value','Type','Comment'):
                td = ET.SubElement(tr,'{0}td'.format(uri))
                if kw[k] == '':
                    td.text = ' '
                else:
                    td.text = kw[k]
    data_format(hdr,div)
    return
