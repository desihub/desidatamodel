# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""Test desidatamodel.stub functions
"""
import os
import unittest
from unittest.mock import patch
from pkg_resources import resource_filename
from astropy.io import fits
from collections import OrderedDict

from .datamodeltestcase import DataModelTestCase
from .. import DataModelError
from ..stub import (Stub, extrakey, file_size, fits_column_format,
                    extract_keywords, log)


class sim_comments(dict):
    """Simulate a dictionary.
    """
    def __getitem__(self, key):
        return "This is the comment on {0}.".format(key)


class sim_header(OrderedDict):
    """Simulate a FITS header object.
    """
    comments = sim_comments()


class sim_hdu(object):
    """Simulate a FITS HDU.
    """
    def __init__(self, header):
        self.header = header
        return


class TestStub(DataModelTestCase):

    def test_Stub(self):
        """Test aspects of initialization of Stub objects.
        """
        #
        # Use a real file, and make sure no exceptions are raised.
        #
        with fits.open(resource_filename('desidatamodel.test',
                                         't/fits_file.fits')) as hdulist:
            stub = Stub(hdulist)
            self.assertEqual(stub.nhdr, 2)
        #
        # Several image extensions.
        #
        hdulist = list()
        hdr = sim_header()
        hdr['SIMPLE'] = True
        hdr['BITPIX'] = 8
        hdr['NAXIS'] = 0
        hdr['EXTEND'] = True
        hdulist.append(sim_hdu(hdr))
        for k in range(10):
            hdr = sim_header()
            hdr['XTENSION'] = 'IMAGE'
            hdr['BITPIX'] = -32
            hdr['NAXIS'] = 2
            hdr['NAXIS1'] = 10
            hdr['NAXIS2'] = 10
            hdr['EXTNAME'] = 'HDU{0:02d}'.format(k+1)
            hdulist.append(sim_hdu(hdr))
        stub = Stub(hdulist)
        self.assertEqual(stub.nhdr, 11)
        self.assertEqual(stub.hduname, 'HDU{0:02d}')
        #
        # Test a lot of image extensions.
        #
        hdulist = list()
        hdr = sim_header()
        hdr['SIMPLE'] = True
        hdr['BITPIX'] = 8
        hdr['NAXIS'] = 0
        hdr['EXTEND'] = True
        hdulist.append(sim_hdu(hdr))
        for k in range(100):
            hdr = sim_header()
            hdr['XTENSION'] = 'IMAGE'
            hdr['BITPIX'] = -32
            hdr['NAXIS'] = 2
            hdr['NAXIS1'] = 10
            hdr['NAXIS2'] = 10
            hdr['EXTNAME'] = 'HDU{0:02d}'.format(k+1)
            hdulist.append(sim_hdu(hdr))
        stub = Stub(hdulist)
        self.assertEqual(stub.nhdr, 101)
        self.assertEqual(stub.hduname, 'HDU{0:03d}')
        #
        # Test warnings for missing EXTNAME, etc.
        #
        hdulist = list()
        hdr = sim_header()
        hdr['SIMPLE'] = True
        hdr['BITPIX'] = 8
        hdr['NAXIS'] = 0
        hdr['EXTEND'] = True
        hdulist.append(sim_hdu(hdr))
        hdr = sim_header()
        hdr['XTENSION'] = 'IMAGE'
        hdr['BITPIX'] = -32
        hdr['NAXIS'] = 2
        hdr['NAXIS1'] = 10
        hdr['NAXIS2'] = 10
        hdr['EXTNAME'] = 'HDU1'
        hdulist.append(sim_hdu(hdr))
        hdr = sim_header()
        hdr['XTENSION'] = 'TABLE   '
        hdr['BITPIX'] = 8
        hdr['NAXIS'] = 2
        hdr['NAXIS1'] = 10
        hdr['NAXIS2'] = 10
        hdr['EXTNAME'] = 'HDU2'
        hdulist.append(sim_hdu(hdr))
        stub = Stub(hdulist)
        self.assertEqual(stub.nhdr, 3)
        meta = stub.hdumeta
        # self.assertLog(log, 0, 'HDU0 has no EXTNAME set!')
        self.assertLog(log, 0, 'Unknown extension type: TABLE.')
        self.assertEqual(meta[1]['format'],
                         'Data: FITS image [float32, 10x10]')
        self.assertEqual(meta[2]['format'],
                         'Unknown extension type: TABLE.')

    def test_Stub_empty_HDU(self):
        """Test with an empty HDU.
        """
        hdulist = list()
        hdr = sim_header()
        hdr['SIMPLE'] = True
        hdr['BITPIX'] = 8
        hdr['NAXIS'] = 0
        hdr['EXTEND'] = True
        hdr['EXTNAME'] = 'PRIMARY'
        hdulist.append(sim_hdu(hdr))
        stub = Stub(hdulist)
        sec = stub.section(0)
        expected_sec = ['HDU0',
                        '----',
                        '',
                        'EXTNAME = PRIMARY',
                        '',
                        '*Summarize the contents of this HDU.*',
                        '',
                        'This HDU has no non-standard required keywords.',
                        '',
                        'Empty HDU.',
                        '']
        self.assertEqual(len(sec), len(expected_sec))
        for k in range(len(sec)):
            self.assertEqual(sec[k], expected_sec[k])

    def test_Stub_compressed_image(self):
        """Test with a compressed image HDU.
        """
        hdulist = list()
        hdr0 = sim_header()
        hdr0['SIMPLE'] = True
        hdr0['BITPIX'] = 8
        hdr0['NAXIS'] = 0
        hdr0['EXTEND'] = True
        hdr0['EXTNAME'] = 'PRIMARY'
        hdulist.append(sim_hdu(hdr0))
        hdr = sim_header()
        hdr['XTENSION'] = 'BINTABLE'
        hdr['BITPIX'] = 8
        hdr['NAXIS'] = 2
        hdr['NAXIS1'] = 8
        hdr['NAXIS2'] = 10
        hdr['PCOUNT'] = 60
        hdr['GCOUNT'] = 1
        hdr['TFIELDS'] = 1
        hdr['TTYPE1'] = 'COMPRESSED_DATA'
        hdr['TFORM1'] = '1PB(6)'
        hdr['ZIMAGE'] = True
        hdr['ZTENSION'] = 'IMAGE'
        hdr['ZBITPIX'] = 16
        hdr['ZNAXIS'] = 2
        hdr['ZNAXIS1'] = 10
        hdr['ZNAXIS2'] = 10
        hdr['ZPCOUNT'] = 0
        hdr['ZGCOUNT'] = 1
        hdr['EXTNAME'] = 'COMPRESSED_IMAGE'
        hdulist.append(sim_hdu(hdr))
        stub = Stub(hdulist)
        stub.filename = 'fits_file.fits'
        stub._filesize = '10 MB'
        self.assertEqual(stub.hdumeta[1]['format'], 'Data: FITS image [int16 (compressed), 10x10]')
        del hdr['ZTENSION']
        stub = Stub(hdulist)
        stub.filename = 'fits_file.fits'
        stub._filesize = '10 MB'
        self.assertEqual(stub.hdumeta[1]['format'], 'Data: FITS image [int16 (compressed), 10x10]')
        del hdr['ZIMAGE']
        stub = Stub(hdulist)
        stub.filename = 'fits_file.fits'
        stub._filesize = '10 MB'
        self.assertEqual(stub.hdumeta[1]['extension'], 'BINTABLE')
        self.assertLog(log, -1, "Possible malformed compressed data in HDU 1 of fits_file.fits.")

    def test_Stub_BINTABLE_with_units(self):
        """Test BINTABLE HDU with units.
        """
        hdulist = list()
        hdr = sim_header()
        hdr['SIMPLE'] = True
        hdr['BITPIX'] = 8
        hdr['NAXIS'] = 0
        hdr['EXTEND'] = True
        hdr['EXTNAME'] = 'PRIMARY'
        hdulist.append(sim_hdu(hdr))
        hdr = sim_header()
        hdr['XTENSION'] = 'BINTABLE'
        hdr['BITPIX'] = 8
        hdr['NAXIS'] = 2
        hdr['NAXIS1'] = 32
        hdr['NAXIS2'] = 3
        hdr['PCOUNT'] = 0
        hdr['GCOUNT'] = 1
        hdr['TFIELDS'] = 4
        hdr['TTYPE1'] = 'target'
        hdr['TFORM1'] = '20A'
        hdr['TTYPE2'] = 'V_mag'
        hdr['TFORM2'] = 'E'
        hdr['TUNIT2'] = 'mag'
        hdr['TCOMM2'] = 'This is a TCOMM comment on V_mag.'
        hdr['TTYPE3'] = 'vdisp'
        hdr['TFORM3'] = 'D'
        hdr['TUNIT3'] = 'km/s'
        hdr['TTYPE4'] = 'vdisp'
        hdr['TFORM4'] = 'D'
        hdr['TUNIT4'] = 'mgy'
        hdr['EXTNAME'] = 'Galaxies'
        hdulist.append(sim_hdu(hdr))
        stub = Stub(hdulist)
        stub.filename = 'fits_file.fits'
        stub._filesize = '10 MB'
        self.assertEqual(stub.hdumeta[1]['format'][2], ('V_mag', 'float32', 'mag', 'This is a TCOMM comment on V_mag.'))
        self.assertLog(log, 0, "Non-standard (but acceptable) unit 'mgy' detected for column 3 in HDU 1 of fits_file.fits.")

    def test_Stub_BINTABLE_with_bad_units(self):
        """Test BINTABLE HDU with bad units.
        """
        erg_msg = self.badUnitMessage('ergs')
        hdulist = list()
        hdr = sim_header()
        hdr['SIMPLE'] = True
        hdr['BITPIX'] = 8
        hdr['NAXIS'] = 0
        hdr['EXTEND'] = True
        hdr['EXTNAME'] = 'PRIMARY'
        hdulist.append(sim_hdu(hdr))
        hdr = sim_header()
        hdr['XTENSION'] = 'BINTABLE'
        hdr['BITPIX'] = 8
        hdr['NAXIS'] = 2
        hdr['NAXIS1'] = 32
        hdr['NAXIS2'] = 3
        hdr['PCOUNT'] = 0
        hdr['GCOUNT'] = 1
        hdr['TFIELDS'] = 3
        hdr['TTYPE1'] = 'target'
        hdr['TFORM1'] = '20A'
        hdr['TTYPE2'] = 'luminosity'
        hdr['TFORM2'] = 'E'
        hdr['TUNIT2'] = 'ergs'
        hdr['TCOMM2'] = 'This is a TCOMM comment on luminosity.'
        hdr['TTYPE3'] = 'vdisp'
        hdr['TFORM3'] = 'D'
        hdr['TUNIT3'] = 'km/s'
        hdr['EXTNAME'] = 'Galaxies'
        hdulist.append(sim_hdu(hdr))
        stub = Stub(hdulist, error=False)
        stub.filename = 'fits_file.fits'
        stub._filesize = '10 MB'
        self.assertEqual(stub.hdumeta[1]['format'][2], ('luminosity', 'float32', 'ergs', 'This is a TCOMM comment on luminosity.'))
        # self.assertLog(log, 1, erg_msg)
        stub = Stub(hdulist, error=True)
        stub.filename = 'fits_file.fits'
        stub._filesize = '10 MB'
        with self.assertRaises(ValueError) as e:
            foo = stub.hdumeta[1]['format'][2]
        self.assertEqual(str(e.exception), erg_msg)

    def test_Stub_image_format(self):
        """Test format string for image HDUs.
        """
        erg_msg = self.badUnitMessage('10**-17 ergs/(cm**2*s*Angstrom)')
        hdr = sim_header()
        hdr['SIMPLE'] = True
        hdr['BITPIX'] = 8
        hdr['NAXIS'] = 0
        hdr['EXTEND'] = True
        stub = Stub([sim_hdu(hdr)], error=True)
        i = stub.image_format(hdr)
        self.assertEqual(i, 'Empty HDU.')
        hdr = sim_header()
        hdr['SIMPLE'] = True
        hdr['BITPIX'] = 8
        hdr['NAXIS'] = 1
        hdr['NAXIS1'] = 1000
        stub = Stub([sim_hdu(hdr)], error=True)
        i = stub.image_format(hdr)
        self.assertEqual(i, 'Data: FITS image [char, 1000]')
        hdr = sim_header()
        hdr['SIMPLE'] = True
        hdr['BITPIX'] = 16
        hdr['NAXIS'] = 2
        hdr['NAXIS1'] = 1000
        hdr['NAXIS2'] = 1000
        stub = Stub([sim_hdu(hdr)], error=True)
        i = stub.image_format(hdr)
        self.assertEqual(i, 'Data: FITS image [int16, 1000x1000]')
        hdr = sim_header()
        hdr['SIMPLE'] = True
        hdr['BITPIX'] = 128
        hdr['NAXIS'] = 2
        hdr['NAXIS1'] = 1000
        hdr['NAXIS2'] = 1000
        stub = Stub([sim_hdu(hdr)], error=True)
        i = stub.image_format(hdr)
        self.assertEqual(i, 'Data: FITS image [BITPIX=128, 1000x1000]')
        hdr = sim_header()
        hdr['SIMPLE'] = True
        hdr['BITPIX'] = 128
        hdr['NAXIS'] = 2
        hdr['NAXIS1'] = 1000
        hdr['NAXIS2'] = 1000
        hdr['BUNIT'] = '10**-17 ergs/(cm**2*s*Angstrom)'
        stub = Stub([sim_hdu(hdr)], error=True)
        with self.assertRaises(ValueError) as e:
            i = stub.image_format(hdr)
        self.assertEqual(str(e.exception), erg_msg)
        stub = Stub([sim_hdu(hdr)], error=False)
        i = stub.image_format(hdr)
        self.assertLog(log, 1, erg_msg)
        self.assertEqual(i, 'Data: FITS image [BITPIX=128, 1000x1000]')
        hdr = sim_header()
        hdr['SIMPLE'] = True
        hdr['BITPIX'] = 128
        hdr['NAXIS'] = 2
        hdr['NAXIS1'] = 1000
        hdr['NAXIS2'] = 1000
        hdr['BUNIT'] = '10**-17 erg/(cm**2*s*Angstrom)'
        stub = Stub([sim_hdu(hdr)], error=False)
        i = stub.image_format(hdr)
        self.assertLog(log, 4, "BUNIT   = '10**-17 erg/(cm**2*s*Angstrom)'")
        self.assertEqual(i, 'Data: FITS image [BITPIX=128, 1000x1000]')
        #
        # Check compressed HDU
        #
        hdr = sim_header()
        hdr['SIMPLE'] = True
        hdr['ZBITPIX'] = 16
        hdr['NAXIS'] = 2
        hdr['NAXIS1'] = 8
        hdr['NAXIS2'] = 10
        hdr['ZNAXIS'] = 2
        hdr['ZNAXIS1'] = 1000
        hdr['ZNAXIS2'] = 1000
        stub = Stub([sim_hdu(hdr)], error=False)
        i = stub.image_format(hdr)
        self.assertEqual(i, 'Data: FITS image [int16 (compressed), 1000x1000]')
        hdr = sim_header()
        hdr['SIMPLE'] = True
        hdr['ZBITPIX'] = 128
        hdr['NAXIS'] = 2
        hdr['NAXIS1'] = 8
        hdr['NAXIS2'] = 10
        hdr['ZNAXIS'] = 3
        hdr['ZNAXIS1'] = 1000
        hdr['ZNAXIS2'] = 1000
        hdr['ZNAXIS3'] = 1000
        stub = Stub([sim_hdu(hdr)], error=False)
        i = stub.image_format(hdr)
        self.assertEqual(i, 'Data: FITS image [BITPIX=128 (compressed), 1000x1000x1000]')
        #
        # Check compressed HDU in non-PRIMARY HDU
        #
        hdr0 = sim_header()
        hdr0['SIMPLE'] = True
        hdr0['BITPIX'] = 8
        hdr0['NAXIS'] = 0
        hdr0['EXTEND'] = True
        hdr1 = sim_header()
        hdr1['XTENSION'] = 'BINTABLE'
        hdr1['BITPIX'] = 8
        hdr1['NAXIS'] = 2
        hdr1['NAXIS1'] = 8
        hdr1['NAXIS2'] = 4194
        hdr1['PCOUNT'] = 22019244
        hdr1['GCOUNT'] = 1
        hdr1['TFIELDS'] = 1
        hdr1['TTYPE1'] = 'COMPRESSED_DATA'
        hdr1['TFORM1'] = '1PB(5975)'
        hdr1['ZIMAGE'] = True
        hdr1['ZSIMPLE'] = True
        hdr1['ZBITPIX'] = 16
        hdr1['ZNAXIS'] = 2
        hdr1['ZNAXIS1'] = 4256
        hdr1['ZNAXIS2'] = 4194
        hdr1['ZTILE1'] = 4256
        hdr1['ZTILE2'] = 1
        hdr1['ZCMPTYPE'] = 'RICE_1  '
        hdr1['ZNAME1'] = 'BLOCKSIZE'
        hdr1['ZVAL1'] =  32
        hdr1['ZNAME2'] = 'BYTEPIX '
        hdr1['ZVAL2'] =  2
        hdr1['BZERO'] = 32768
        hdr1['BSCALE'] = 1
        hdr1['EXTNAME'] = 'Z7      '
        hdr1['BUNIT'] = 'maggie'
        stub = Stub([sim_hdu(hdr0), sim_hdu(hdr1)], error=False)
        stub.filename = 'fits_file.fits.fz'
        i = stub.image_format(hdr1)
        self.assertEqual(i, 'Data: FITS image [int16 (compressed), 4256x4194]')
        self.assertLog(log, -1, "Non-standard (but acceptable) unit 'maggie' detected in fits_file.fits.fz.")

    def test_Stub_contents(self):
        """Test the table-of-contents functionality.
        """
        hdr0 = sim_header()
        hdr0['SIMPLE'] = True
        hdr0['BITPIX'] = 8
        hdr0['NAXIS'] = 0
        hdr0['EXTEND'] = True
        hdr1 = sim_header()
        hdr1['XTENSION'] = 'BINTABLE'
        hdr1['BITPIX'] = 8
        hdr1['NAXIS'] = 2
        hdr1['NAXIS1'] = 8
        hdr1['NAXIS2'] = 4194
        hdr1['PCOUNT'] = 22019244
        hdr1['GCOUNT'] = 1
        hdr1['TFIELDS'] = 1
        hdr1['TTYPE1'] = 'COMPRESSED_DATA'
        hdr1['TFORM1'] = '1PB(5975)'
        hdr1['ZIMAGE'] = True
        hdr1['ZSIMPLE'] = True
        hdr1['ZBITPIX'] = 16
        hdr1['ZNAXIS'] = 2
        hdr1['ZNAXIS1'] = 4256
        hdr1['ZNAXIS2'] = 4194
        hdr1['ZTILE1'] = 4256
        hdr1['ZTILE2'] = 1
        hdr1['ZCMPTYPE'] = 'RICE_1  '
        hdr1['ZNAME1'] = 'BLOCKSIZE'
        hdr1['ZVAL1'] =  32
        hdr1['ZNAME2'] = 'BYTEPIX '
        hdr1['ZVAL2'] =  2
        hdr1['BZERO'] = 32768
        hdr1['BSCALE'] = 1
        hdr1['EXTNAME'] = 'Z7      '
        hdr1['BUNIT'] = 'maggie'
        stub = Stub([sim_hdu(hdr0), sim_hdu(hdr1)], error=False)
        stub.filename = 'fits_file.fits.fz'
        self.assertEqual(stub.contents[2], ('HDU1_', 'Z7', 'BINTABLE', '*Brief Description*'))
        del hdr1['EXTNAME']
        stub = Stub([sim_hdu(hdr0), sim_hdu(hdr1)], error=False)
        stub.filename = 'fits_file.fits.fz'
        self.assertEqual(stub.contents[2], ('HDU1_', '', 'BINTABLE', '*Brief Description*'))
        self.assertLog(log, -1, 'HDU1 has no EXTNAME set!')

    def test_extrakey(self):
        """Test the identification of non-boring keys.
        """
        extrakey_tests = {'TTYPE01': False,
                          'TFORM12': False,
                          'TUNIT00': False,
                          'TCOMM33': False,
                          'TDIM11': False,
                          'BITPIX': False,
                          'DEPNAM33': False,
                          'DEPVER33': False,
                          'ZTENSION': False,
                          'ZBITPIX': False,
                          'FOOBAR': True}
        for k in extrakey_tests:
            if extrakey_tests[k]:
                self.assertTrue(extrakey(k))
            else:
                self.assertFalse(extrakey(k))

    @patch('os.path.getsize')
    def test_file_size(self, mock_size):
        """Test the determination and formatting of file size.
        """
        sizes = {5: '5 bytes',
                 2048: '2 KB',
                 3145728: '3 MB',
                 6442450944: '6 GB',
                 7696581394432: '7.0 TB'}
        for s in sizes:
            mock_size.return_value = s
            self.assertEqual(file_size(s), sizes[s])

    def test_fits_column_format(self):
        """Test the translation of FITS column format strings.
        """
        formats = {
            '1PB(5)': '8-bit stream',
            '1PI(10)': '16-bit stream',
            '1QJ(15)': '32-bit stream',
            'A': 'char[1]',
            'B': 'binary',
            'L': 'logical',
            'E': 'float32',
            'D': 'float64',
            'I': 'int16',
            'J': 'int32',
            'K': 'int64',
            '10D': 'float64[10]',
            '20J': 'int32[20]'}
        for f in formats:
            ff = fits_column_format(f)
            self.assertEqual(ff, formats[f])

    def test_extract_keywords(self):
        """Test the parsing of a full FITS HDU.
        """
        hdr = sim_header()
        hdr['SIMPLE'] = True
        hdr['BITPIX'] = 8
        hdr['NAXIS'] = 0
        hdr['EXTEND'] = True
        lines = extract_keywords(hdr)
        self.assertEqual(len(lines), 0)
        hdr['BOOLEAN'] = True
        hdr['VERSION'] = '0.1.2'
        hdr['INTEGER'] = 12345
        hdr['FLOAT'] = 3.14159
        hdr['UNDR_'] = 'underscore_'
        lines = extract_keywords(hdr)
        expected_lines = [('BOOLEAN', 'T', 'bool',
                           'This is the comment on BOOLEAN.'),
                          ('VERSION', '0.1.2', 'str',
                           'This is the comment on VERSION.'),
                          ('INTEGER', '12345', 'int',
                           'This is the comment on INTEGER.'),
                          ('FLOAT', '3.14159', 'float',
                           'This is the comment on FLOAT.'),
                          ('UNDR\\_', 'underscore\\_', 'str',
                           'This is the comment on UNDR\\_.')]
        for k in range(len(lines)):
            self.assertEqual(lines[k], expected_lines[k])
        hdr = sim_header()
        hdr['SIMPLE'] = True
        hdr['BITPIX'] = 8
        hdr['NAXIS'] = 0
        hdr['EXTEND'] = True
        # Artificial example, but needed to trigger an exception
        hdr['FOOBAR'] = (3.14159, 2.71828)
        lines = extract_keywords(hdr)
        expected_lines = [('FOOBAR', (3.14159, 2.71828),
                           'Unknown', 'This is the comment on FOOBAR.')]
        self.assertLog(log, 0, "Raised AttributeError on FOOBAR = (3.14159, 2.71828).")
        for k in range(len(lines)):
            self.assertEqual(lines[k], expected_lines[k])

    def test_process_file(self):
        """Full test of parsing a FITS file.
        """
        filename = resource_filename('desidatamodel.test', 't/fits_file.fits')
        modelfile = resource_filename('desidatamodel.test', 't/fits_file.rst')
        with open(modelfile) as m:
            modeldata = m.read()
        stub = Stub(filename)
        data = str(stub)
        self.assertEqual(stub.modelname, 'fits_file')
        modellines = modeldata.split('\n')
        for i, l in enumerate(data.split('\n')):
            self.assertEqual(l, modellines[i])


def test_suite():
    """Allows testing of only this module with the command::

        python setup.py test -m <modulename>
    """
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
