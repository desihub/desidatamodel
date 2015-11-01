# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""Test desidatamodel.stub functions
"""
#
from __future__ import absolute_import, division, print_function, unicode_literals
#
import os
import unittest
from collections import OrderedDict
from new import instancemethod
from ..stub import (data_format, extrakey, file_size,
    fits_column_format, parse_header, process_file)
#
#
#
class sim_header(OrderedDict):
    """Simulate a FITS header object.
    """
    def get_comment(self,key):
        """Simulate the get_comment method from FITS header objects.
        """
        return "This is the comment on {0}.".format(key)
#
#
#
class TestStub(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data_dir = os.path.join(os.path.dirname(__file__),'t')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_data_format(self):
        """Test identification of images and tables.
        """
        hdr = sim_header()
        lines = data_format(hdr)
        self.assertEqual(lines,[])
        hdr['XTENSION'] = 'FOOBAR'
        lines = data_format(hdr)
        self.assertEqual(lines,["Unknown extension type {0}".format(hdr['XTENSION']),''])
        hdr['XTENSION'] = 'IMAGE'
        bitpix = {8:'char',16:'int16',32:'int32',64:'int64',-32:'float32',-64:'float64',99:'BITPIX=99'}
        for k in bitpix:
            hdr['BITPIX'] = k
            self.assertEqual(data_format(hdr),['Data: FITS image [{0}]'.format(bitpix[k]),''])
        del hdr['BITPIX']
        hdr['XTENSION'] = 'BINTABLE'
        hdr['TFIELDS'] = 3
        hdr['TTYPE1'] = 'one'
        hdr['TTYPE2'] = 'two'
        hdr['TTYPE3'] = 'three'
        hdr['TFORM1'] = '1A'
        hdr['TFORM2'] = '2J'
        hdr['TFORM3'] = '3D'
        hdr['TUNIT3'] = 'km/s'
        hdr['TCOMM3'] = 'The units are km/s.'
        lines = data_format(hdr)
        with open(os.path.join(self.data_dir,'data_table.txt')) as dt:
            table = dt.read().split('\n')
        self.assertEqual(lines,table)

    def test_extrakey(self):
        """Test the identification of non-boring keys.
        """
        extrakey_tests = {'TTYPE01':False,
            'TFORM12':False,
            'TUNIT00':False,
            'TCOMM33':False,
            'TDIM11':False,
            'BITPIX':False,
            'FOOBAR':True}
        for k in extrakey_tests:
            if extrakey_tests[k]:
                self.assertTrue(extrakey(k))
            else:
                self.assertFalse(extrakey(k))

    def test_file_size(self):
        """Test the determination and formatting of file size.
        """
        filename = os.path.join(self.data_dir,'this-file-contains-five-bytes.txt')
        s = file_size(filename)
        self.assertEqual(s,'5 bytes')
        filename = os.path.join(self.data_dir,'this-file-contains-2048-bytes.txt')
        s = file_size(filename)
        self.assertEqual(s,'2 KB')

    def test_fits_column_format(self):
        """Test the translation of FITS column format strings.
        """
        formats = {
            '1PB':'8-bit stream',
            '1PI':'16-bit stream',
            '1PJ':'32-bit stream',
            'A':'char[1]',
            'B':'binary',
            'L':'logical',
            'E':'float32',
            'D':'float64',
            'I':'int16',
            'J':'int32',
            'K':'int64',
            '10D':'float64[10]',
            '20J':'int32[20]'}
        for f in formats:
            ff = fits_column_format(f)
            self.assertEqual(ff,formats[f])

    def test_parse_header(self):
        """Test the parsing of a full FITS HDU.
        """
        hdr = sim_header()
        hdr['SIMPLE'] = True
        hdr['BITPIX'] = 8
        hdr['NAXIS'] = 0
        hdr['EXTEND'] = True
        lines = parse_header(hdr)
        self.assertEqual(lines,['This HDU has no non-standard required keywords.',''])
        hdr['BOOLEAN'] = True
        hdr['VERSION'] = '0.1.2'
        hdr['INTEGER'] = 12345
        hdr['FLOAT'] = 3.14159
        hdr['UNDR_'] = 'underscore_'
        lines = parse_header(hdr)
        self.assertEqual(lines,[
            'Required Header Keywords',
            '~~~~~~~~~~~~~~~~~~~~~~~~',
            '',
            '======= ============= ===== ===============================',
            'KEY     Example Value Type  Comment',
            '======= ============= ===== ===============================',
            'BOOLEAN T             bool  This is the comment on BOOLEAN.',
            'VERSION 0.1.2         str   This is the comment on VERSION.',
            'INTEGER 12345         int   This is the comment on INTEGER.',
            'FLOAT   3.14159       float This is the comment on FLOAT.',
            'UNDR\\_  underscore\\_  str   This is the comment on UNDR\\_.',
            '======= ============= ===== ===============================',
            ''
            ])

    def test_process_file(self):
        """Full test of parsing a FITS file.
        """
        filename = os.path.join(self.data_dir,'fits_file.fits')
        modelfile = os.path.join(self.data_dir,'fits_file.rst')
        with open(modelfile) as m:
            modeldata = m.read()
        modelname, data = process_file(filename)
        self.assertEqual(modelname,'fits_file')
        self.assertEqual(data,modeldata)

if __name__ == '__main__':
    unittest.main()
