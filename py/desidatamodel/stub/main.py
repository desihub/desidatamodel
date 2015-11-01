# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""Generate an DESI data model stub for a given FITS file.

You will still need to hand edit the file to add descriptions, etc., but
it gives you a good starting point in the correct format.
"""
from __future__ import absolute_import, division, print_function, unicode_literals
from os.path import basename

def main():
    """Program to run if called as an executable.
    """
    from sys import argv, stderr
    from argparse import ArgumentParser
    from . import process_file
    try:
        import fitsio
    except ImportError:
        print("This script requires fitsio, available from https://github.com/esheldon/fitsio",file=stderr)
        return 1
    parser = ArgumentParser(description=__doc__,prog=basename(argv[0]))
    parser.add_argument('filename',help='A FITS file.',metavar='FILE',nargs='+')
    options = parser.parse_args()
    for f in options.filename:
        modelname, data = process_file(f)
        #
        # Write the file
        #
        with open("{0}.rst".format(modelname),'w') as m:
            m.write(data)
    return 0
