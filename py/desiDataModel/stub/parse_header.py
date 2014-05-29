# License information goes here
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
# The line above will help with 2to3 support.
def parse_header(hdr):
    """Create a table of header keywords, omitting those required by FITS anyway.

    Parameters
    ----------
    hdr : an object returned by the fitsio method ``read_header()``
        The header to parse.

    Returns
    -------
    parse_header : list
        A list of strings that can be appended to the main document.
    """
    from cgi import escape
    from . import data_format, extrakey
    section = list()
    keywords = list()
    for key in hdr.keys():
        if extrakey(key):
            #- Escape &, <, >, in strings, but don't choke on int/float
            value = hdr[key]
            if isinstance(value, bool):
                ktype = 'bool'
                value = ('F','T')[int(value)]
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
        section.append('This HDU has no non-standard required keywords.')
        section.append('')
    else:
        section.append('Required Header Keywords')
        section.append('~~~~~~~~~~~~~~~~~~~~~~~~')
        section.append('')
        keywords_table =  [('KEY','Value','Type','Comment')]
        for kw in keywords:
            keywords_table.append((kw['KEY'],kw['Value'],kw['Type'],kw['Comment']))
        colsizes = [max(map(len,col)) for col in zip(*keywords_table)]
        highlight = ' '.join(['='*k for k in colsizes])
        colformat = ' '.join(['{{{0:d}:{1:d}}}'.format(i,s) for i,s in enumerate(colsizes)])
        section.append(highlight)
        for k in range(len(keywords_table)):
            section.append(colformat.format(*keywords_table[k]))
            if k == 0:
                section.append(highlight)
        section.append(highlight)
        section.append('')
    #
    # Analyze any tables that might be present.
    #
    section += data_format(hdr)
    return section
