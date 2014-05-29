# License information goes here
# -*- coding: utf-8 -*-
"""
Generate an DESI data model stub for a given FITS file.

You will still need to hand edit the file to add descriptions, etc. but
it gives you a good starting point in the correct format.
"""
from __future__ import absolute_import, division, print_function, unicode_literals
# The line above will help with 2to3 support.
def main():
    """Program to run if called as an executable."""
    import xml.etree.ElementTree as ET
    import re
    from sys import argv, stderr
    from argparse import ArgumentParser
    from os import getenv
    from os.path import basename, join
    from . import file_size, get_uri, parse_header, rst
    try:
        import fitsio
    except ImportError:
        print("This script requires fitsio, available from https://github.com/esheldon/fitsio",file=stderr)
        return 1
    parser = ArgumentParser(description=__doc__,prog=basename(argv[0]))
    parser.add_argument('filename',help='A FITS file.',metavar='FILE',nargs='+')
    options = parser.parse_args()
    template = join(getenv('DESIDATAMODEL_DIR'),'etc','template.html')
    for f in options.filename:
        rstkeywords = dict()
        #
        # Create a title
        #
        basef = basename(f)
        try:
            modelname = basef[0:basef.index('-')]
        except ValueError:
            modelname = basef[0:basef.index('.')]
        rstkeywords['title'] = 'Datamodel: {0}'.format(modelname)
        rstkeywords['titlehighlight'] = '='*len(rstkeywords['title'])
        rstkeywords['filename'] = f
        rstkeywords['filetype'] = 'FITS'
        rstkeywords['filesize'] = file_size(f)
        #
        #- Read the file and parse the headers
        #
        fx = fitsio.FITS(f)
        nhdr = len(fx)
        # nspace = ''
        # hduhighlight = '='*6
        if nhdr > 99:
            hduname = 'HDU{0:03d}'
            # nspace = ' '
            # hduhighlight += '='
        elif nhdr > 9:
            hduname = 'HDU{0:02d}'
        else:
            hduname = 'HDU{0:1d}'
        # rstkeywords['nspace'] = nspace
        # rstkeywords['hduhighlight'] = hduhighlight
        # rstkeywords['contentstable'] = ''
        contents_table = [('Number','EXTNAME','Type','Contents')]
        for k in range(nhdr):
            hdr = fx[k].read_header()
            if k > 0 and 'EXTNAME' in hdr:
                extname = hdr['EXTNAME']
            else:
                extname = ''
            if k > 0:
                exttype = hdr['XTENSION']
            else:
                exttype = 'IMAGE'
            contents_table.append((hduname.format(k)+'_',extname,exttype,'*Brief Description*'))
        # print(contents_table)
        colsizes = [max(map(len,col)) for col in zip(*contents_table)]
        highlight = ' '.join(['='*k for k in colsizes])+"\n"
        colformat = ' '.join(['{{{0:d}:{1:d}}}'.format(i,s) for i,s in enumerate(colsizes)])+"\n"
        rstkeywords['contents_table'] = highlight
        for k in range(nhdr):
            rstkeywords['contents_table'] += colformat.format(*contents_table[0])
            if k == 0:
                rstkeywords['contents_table'] += highlight
        rstkeywords['contents_table'] += highlight
        # for k in range(nhdr):
        #     div = root.find('.//{0}div[@id="hdu{1}"]'.format(uri,k))
        #     if div is None:
        #         print('Could not find hdu{0}!'.format(k))
        #     if k == 0:
        #         #
        #         # Remove header table
        #         #
        #         del div[4]
        #     if k == 1:
        #         div[0].text= "HDU{0}: [What's in this HDU?]".format(k)
        #         del div[1:]
        #         p = ET.SubElement(div,'{0}p'.format(uri))
        #         p.text='[Summarize contents of this HDU.]'
        #         p.tail="\n"
        #     hdr = fx[k].read_header()
        #     parse_header(hdr,div)
        with open("{0}.rst".format(modelname),'w') as f:
            f.write(rst.format(**rstkeywords))
    return 0
