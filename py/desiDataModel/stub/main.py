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
    from . import get_uri, parse_header
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
        #
        # Create an element tree from template
        #
        tree = ET.ElementTree()
        root = tree.parse(template)
        uri = get_uri(root)
        #
        #- XML / HTML header stuff
        #
        basename = basename(f)
        try:
            modelname = basename[0:basename.index('-')]
        except ValueError:
            modelname = basename[0:basename.index('.')]
        root.find("{0}head/{0}title".format(uri)).text = "Datamodel: {0}".format(modelname)
        root.find('.//{0}div[@id="intro"]/{0}h1'.format(uri)).text = "Datamodel: {0}".format(modelname)
        #
        #- Introduction
        #
        root.find('.//{0}dd[@id="filesize"]'.format(uri)).text = file_size(f)
        filetype = root.find('.//{0}dd[@id="filetype"]'.format(uri))
        del filetype[0] # remove <i> tag
        filetype.text = 'FITS'
        #
        #- Read the file and parse the headers
        #
        fx = fitsio.FITS(sys.argv[1])
        nhdr = len(fx)
        body = root.find('{0}body'.format(uri))
        if nhdr < 2:
            #
            # Remove the extra section in the template
            #
            del body[2]
        if nhdr > 2:
            #
            # Add extra hdu sections
            #
            for k in range(2,nhdr):
                divid = "hdu{0}".format(k)
                div = ET.Element('{0}div'.format(uri),attrib={'id':divid})
                div.text="\n"
                div.tail="\n\n"
                h2 = ET.SubElement(div,'{0}h2'.format(uri))
                h2.text = "HDU{0}: [What's in this HDU?]".format(k)
                h2.tail = "\n"
                p = ET.SubElement(div,'{0}p'.format(uri))
                p.text='[Summarize contents of this HDU.]'
                p.tail="\n"
                body.insert(k+1,div)
        for k in range(nhdr):
            div = root.find('.//{0}div[@id="hdu{1}"]'.format(uri,k))
            if div is None:
                print('Could not find hdu{0}!'.format(k))
            if k == 0:
                #
                # Remove header table
                #
                del div[4]
            if k == 1:
                div[0].text= "HDU{0}: [What's in this HDU?]".format(k)
                del div[1:]
                p = ET.SubElement(div,'{0}p'.format(uri))
                p.text='[Summarize contents of this HDU.]'
                p.tail="\n"
            hdr = fx[k].read_header()
            parse_header(hdr,div)
        html = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html
     PUBLIC "-//W3C//DTD XHTML 1.1//EN"
     "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
"""
        html+=re.sub('html:','',re.sub('xmlns:html','xmlns',ET.tostring(root)))
        with open("{0}.html".format(modelname),'w') as f:
            f.write(html+"\n")
    return 0
