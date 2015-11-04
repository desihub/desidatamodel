# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
# The line above will help with 2to3 support.
def process_file(filename):
    """Process a single FITS file.

    Parameters
    ----------
    filename : str
        Name of a FITS file.

    Returns
    -------
    process_file : tuple
        A tuple containing the name of the model file and the data to write to it.
    """
    import re
    from astropy.io import fits
    from os.path import basename
    from . import file_size, parse_header, rst
    rstkeywords = dict()
    #
    # Create a title
    #
    basef = basename(filename)
    try:
        modelname = basef[0:basef.index('-')]
    except ValueError:
        modelname = basef[0:basef.index('.')]
    rstkeywords['title'] = modelname
    rstkeywords['titlehighlight'] = '='*len(rstkeywords['title'])
    rstkeywords['filename'] = basef
    rstkeywords['filetype'] = 'FITS'
    rstkeywords['filesize'] = file_size(filename)
    #
    #- Read the file and parse the headers
    #
    with fits.open(filename) as fx:
        nhdr = len(fx)
        if nhdr > 99:
            hduname = 'HDU{0:03d}'
        elif nhdr > 9:
            hduname = 'HDU{0:02d}'
        else:
            hduname = 'HDU{0:1d}'
        contents_table = [('Number','EXTNAME','Type','Contents')]
        headers = list()
        hdu_sections = list()
        for k in range(nhdr):
            headers.append(fx[k].header)
            if k > 0 and 'EXTNAME' in headers[k]:
                extname = headers[k]['EXTNAME'].strip()
            else:
                extname = ''
            if k > 0:
                exttype = headers[k]['XTENSION'].strip()
            else:
                exttype = 'IMAGE'
            contents_table.append((hduname.format(k)+'_',extname,exttype,'*Brief Description*'))
            sec_title = hduname.format(k)
            hdu_sections.append(sec_title)
            hdu_sections.append('-'*len(sec_title))
            hdu_sections.append('')
            if extname != '':
                hdu_sections.append('EXTNAME = '+extname)
                hdu_sections.append('')
            hdu_sections.append('*Summarize the contents of this HDU.*')
            hdu_sections.append('')
            hdu_sections += parse_header(headers[k])
    #
    # Construct the contents table.
    #
    colsizes = [max(map(len,col)) for col in zip(*contents_table)]
    highlight = ' '.join(['='*k for k in colsizes])+"\n"
    colformat = ' '.join(['{{{0:d}:{1:d}}}'.format(i,s) for i,s in enumerate(colsizes)])+"\n"
    rstkeywords['contents_table'] = highlight
    for k in range(nhdr+1):
        rstkeywords['contents_table'] += colformat.format(*contents_table[k])
        if k == 0:
            rstkeywords['contents_table'] += highlight
    rstkeywords['contents_table'] += highlight
    rstkeywords['hdu_sections'] = '\n'.join(hdu_sections)
    return (modelname, rst.format(**rstkeywords))
