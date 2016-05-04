# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
# The line above will help with 2to3 support.


def generate_fits():
    """Generate a FITS file for test purposes.
    """
    from os import remove
    from os.path import dirname, exists, join
    import numpy as np
    from astropy.io import fits
    from ..stub import process_file
    image = np.random.random_integers(0, 2**16-1,
                                      size=(100, 100)).astype(np.uint16)
    hdu0 = fits.PrimaryHDU(image, uint=True)
    hdu0.header.comments['BZERO'] = 'Data are really unsigned 16-bit int.'
    a1 = np.array(['NGC1001', 'NGC1002', 'NGC1003'])
    a2 = np.array([11.1, 12.3, 15.2], dtype='f')
    a3 = np.array([57.6, 99.43, 123.4])
    col1 = fits.Column(name='target', format='20A', array=a1)
    col2 = fits.Column(name='V_mag', format='E', array=a2, unit='mag')
    col3 = fits.Column(name='vdisp', format='D', array=a3, unit='km/s')
    cols = fits.ColDefs([col1, col2, col3])
    hdu1 = fits.BinTableHDU.from_columns(cols)
    hdu1.header['EXTNAME'] = ('Galaxies', 'Name of this HDU.')
    hdulist = fits.HDUList([hdu0, hdu1])
    filename = join(dirname(__file__), 't', 'fits_file.fits')
    if exists(filename):
        remove(filename)
    hdulist.writeto(filename)
    modelname, data = process_file(filename)
    modelfile = join(dirname(__file__), 't', modelname+'.rst')
    if exists(modelfile):
        remove(modelfile)
    with open(modelfile, 'w') as m:
        m.write(data)
    return 0


if __name__ == '__main__':
    from sys import exit
    exit(generate_fits())
