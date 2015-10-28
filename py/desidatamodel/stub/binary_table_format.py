# License information goes here
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
# The line above will help with 2to3 support.
def binary_table_format(hdr):
    """Print format of binary table

    Parameters
    ----------
    hdr : an object returned by the fitsio method ``read_header()``
        The header to parse.

    Returns
    -------
    binary_table_format : list
        A list of strings that can be appended to the main document.
    """
    from cgi import escape
    from . import fits_column_format
    section = list()
    section.append('Required Data Table Columns')
    section.append('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    section.append('')
    columns_table =  [('Name','Type','Units','Description')]
    if hdr['TFIELDS'] < 10:
        jformat = '{0:d}'
    elif hdr['TFIELDS'] < 100:
        jformat = '{0:02d}'
    else:
        jformat = '{0:03d}'
    for j in range(hdr['TFIELDS']):
        jj = jformat.format(j)
        name = hdr['TTYPE'+jj].strip()
        ttype = fits_column_format(hdr['TFORM'+jj].strip())
        tunit = 'TUNIT'+jj
        if tunit in hdr:
            units = hdr[tunit]
        else:
            units = ''
        #- Check TCOMMnn keyword, otherwise use TTYPE comment for description
        commkey = 'TCOMM'+jj
        if commkey in hdr:
            description = escape(hdr[commkey])
        else:
            description = escape(hdr.get_comment('TTYPE'+jj))
        columns_table.append((name,ttype,units,description))
    colsizes = [max(map(len,col)) for col in zip(*columns_table)]
    highlight = ' '.join(['='*k for k in colsizes])
    colformat = ' '.join(['{{{0:d}:{1:d}}}'.format(i,s) for i,s in enumerate(colsizes)])
    section.append(highlight)
    for k in range(len(columns_table)):
        section.append(colformat.format(*columns_table[k]).rstrip())
        if k == 0:
            section.append(highlight)
    section.append(highlight)
    section.append('')
    return section
