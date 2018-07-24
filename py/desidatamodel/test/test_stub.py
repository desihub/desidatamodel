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
                    extract_keywords, image_format, log)


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
        with fits.open(resource_filename('desidatamodel.test',
                                         't/fits_file.fits')) as hdulist:
            stub = Stub(hdulist)
            self.assertEqual(stub.nhdr, 2)
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
        self.assertLog(log, 0, 'HDU0 has no EXTNAME set!')
        self.assertLog(log, 1, 'Unknown extension type: TABLE.')
        self.assertEqual(meta[1]['format'],
                         'Data: FITS image [float32, 10x10]')
        self.assertEqual(meta[2]['format'],
                         'Unknown extension type: TABLE.')
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

    def test_image_format(self):
        """Test format string for image HDUs.
        """
        hdr = sim_header()
        hdr['SIMPLE'] = True
        hdr['BITPIX'] = 8
        hdr['NAXIS'] = 0
        hdr['EXTEND'] = True
        i = image_format(hdr)
        self.assertEqual(i, 'Empty HDU.')
        hdr = sim_header()
        hdr['SIMPLE'] = True
        hdr['BITPIX'] = 8
        hdr['NAXIS'] = 1
        hdr['NAXIS1'] = 1000
        i = image_format(hdr)
        self.assertEqual(i, 'Data: FITS image [char, 1000]')
        hdr = sim_header()
        hdr['SIMPLE'] = True
        hdr['BITPIX'] = 16
        hdr['NAXIS'] = 2
        hdr['NAXIS1'] = 1000
        hdr['NAXIS2'] = 1000
        i = image_format(hdr)
        self.assertEqual(i, 'Data: FITS image [int16, 1000x1000]')
        hdr = sim_header()
        hdr['SIMPLE'] = True
        hdr['BITPIX'] = 128
        hdr['NAXIS'] = 2
        hdr['NAXIS1'] = 1000
        hdr['NAXIS2'] = 1000
        i = image_format(hdr)
        self.assertEqual(i, 'Data: FITS image [BITPIX=128, 1000x1000]')
        hdr = sim_header()
        hdr['SIMPLE'] = True
        hdr['BITPIX'] = 128
        hdr['NAXIS'] = 2
        hdr['NAXIS1'] = 1000
        hdr['NAXIS2'] = 1000
        hdr['BUNIT'] = '10**-17 ergs/(cm**2*s*Angstrom)'
        with self.assertRaises(DataModelError) as e:
            i = image_format(hdr, True)
        self.assertEqual(str(e.exception), "'10**-17 ergs/(cm**2*s*Angstrom)' did not parse as fits unit: At col 8, Unit 'ergs' not supported by the FITS standard. Did you mean erg?")
        i = image_format(hdr, False)
        self.assertLog(log, 0, "'10**-17 ergs/(cm**2*s*Angstrom)' did not parse as fits unit: At col 8, Unit 'ergs' not supported by the FITS standard. Did you mean erg?")
        self.assertEqual(i, 'Data: FITS image [BITPIX=128, 1000x1000]')
        hdr = sim_header()
        hdr['SIMPLE'] = True
        hdr['BITPIX'] = 128
        hdr['NAXIS'] = 2
        hdr['NAXIS1'] = 1000
        hdr['NAXIS2'] = 1000
        hdr['BUNIT'] = '10**-17 erg/(cm**2*s*Angstrom)'
        i = image_format(hdr, False)
        self.assertLog(log, 1, "BUNIT   = '1e-17 erg / (Angstrom cm2 s)'")
        self.assertEqual(i, 'Data: FITS image [BITPIX=128, 1000x1000]')
        #
        # Check compressed HDU
        #
        hdr = sim_header()
        hdr['SIMPLE'] = True
        hdr['ZBITPIX'] = 16
        hdr['NAXIS'] = 2
        hdr['NAXIS1'] = 1000
        hdr['NAXIS2'] = 1000
        i = image_format(hdr)
        self.assertEqual(i, 'Data: FITS image [int16 (compressed), 1000x1000]')
        hdr = sim_header()
        hdr['SIMPLE'] = True
        hdr['ZBITPIX'] = 128
        hdr['NAXIS'] = 2
        hdr['NAXIS1'] = 1000
        hdr['NAXIS2'] = 1000
        i = image_format(hdr)
        self.assertEqual(i, 'Data: FITS image [BITPIX=128 (compressed), 1000x1000]')


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
            '1PB': '8-bit stream',
            '1PI': '16-bit stream',
            '1PJ': '32-bit stream',
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
