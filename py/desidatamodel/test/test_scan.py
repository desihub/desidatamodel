# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""Test desidatamodel.scan functions
"""
import os
import unittest
from unittest.mock import patch, call
from pkg_resources import resource_filename
from astropy.io import fits
from astropy.io.fits.card import Undefined
from collections import OrderedDict

from .datamodeltestcase import DataModelTestCase, DM
from .. import DataModelError
from ..check import DataModel
from ..stub import Stub
from ..scan import _options, collect_files, union_metadata, UnionStub, log


class TestScan(DataModelTestCase):

    def test_UnionStub(self):
        """Test initialization of UnionStub.
        """

        model = DataModel(self.test_files / 'fits_file_optional_columns.rst',
                          os.path.join(os.environ[DM], 'doc', 'examples'))
        foo = model.get_regexp('/desi/spectro/data')
        union = UnionStub(model, 10, error=False)
        self.assertEqual(union.nhdr, 2)
        self.assertEqual(union.count, 10)
        self.assertListEqual(union.contents, [union.contents_header,
                                              ('HDU0_', 'PRIMARY', 'IMAGE', '*Brief Description*'),
                                              ('HDU1_', 'Galaxies', 'BINTABLE', '*Brief Description*')])

    def test_UnionStub_mark_optional(self):
        """Test final output of UnionStub.
        """
        model = DataModel(self.test_files / 'fits_file_optional_columns.rst',
                          os.path.join(os.environ[DM], 'doc', 'examples'))
        foo = model.get_regexp('/desi/spectro/data')
        union = UnionStub(model, 10, error=False)
        union.counter[0]['keywords']['NAXIS1'] = 10
        union.counter[0]['keywords']['NAXIS2'] = 10
        union.counter[0]['keywords']['BSCALE'] = 10
        union.counter[0]['keywords']['BZERO'] = 10
        union.counter[0]['keywords']['OPTKEY1'] = 5
        union.counter[0]['keywords']['OPTKEY2'] = 0
        union.counter[1]['keywords']['NAXIS1'] = 10
        union.counter[1]['keywords']['NAXIS2'] = 10
        union.counter[1]['format']['target'] = 10
        union.counter[1]['format']['OPT1'] = 5
        union.counter[1]['format']['V_mag'] = 10
        union.counter[1]['format']['vdisp'] = 10
        union.counter[1]['format']['OPT2'] = 0
        union.mark_optional()
        self.assertLog(log, -2, "vdisp is a required column in HDU1.")
        self.assertLog(log, -1, "OPT2 is an unused column in HDU1.")

    def test_UnionStub_update(self):
        """Test updates to the union model.
        """
        stubs = [Stub(self.test_files / 'fits_file.fits'),
                 Stub(self.test_files / 'fits_file.fits'),
                 Stub(self.test_files / 'fits_file.fits')]
        stubs[0].hdumeta[0]['keywords'][2] = ('BSCALE', '1', 'int', 'No scaling.')
        stubs[0].hdumeta[1]['format'].append(('OPT1', 'int32', '', 'Comment'))
        stubs[0].hdumeta[1]['format'].append(('OPT2', 'float64', 'yr', 'Comment'))
        stubs[1].hdumeta[0]['keywords'][2] = ('BSCALE', '1', 'int', 'No scaling.')
        stubs[1].hdumeta[0]['keywords'].append(('KEYTEST', 'example', 'str', 'Comment'))
        stubs[1].hdumeta[0]['keywords'][2] = ('BSCALE', '1', 'int', 'No scaling.')
        stubs[1].hdumeta[1]['format'].append(('OPT2', 'float64', 'yr', 'Comment'))
        stubs[2].hdumeta[0]['keywords'].append(('KEYTEST', 'example', 'str', 'Comment'))
        model = DataModel(self.test_files / 'fits_file_optional_columns.rst',
                          os.path.join(os.environ[DM], 'doc', 'examples'))
        foo = model.get_regexp('/desi/spectro/data')
        modelmeta = model.extract_metadata()
        union = UnionStub(model, len(stubs))
        union.hdumeta[0]['keywords'][3] = ('BZERO', '', 'str', 'Data are really unsigned 16-bit int.')
        union.hdumeta[0]['keywords'].append(('UNUSED', 'example', 'str', 'Comment'))
        union.hdumeta[1]['format'][1] = ('target', 'char[30]', '', 'Comment')
        union.hdumeta[1]['format'][4] = ('vdisp', 'float64', 'm/s', 'Comment')
        union.hdumeta[1]['format'].append(('UNUSED', 'int16', '', 'Comment'))
        union.update(0, stubs[0].hdumeta[0]['keywords'])
        union.update(1, stubs[0].hdumeta[1]['keywords'])
        union.update(1, stubs[0].hdumeta[1]['format'], columns=True)
        union.update(0, stubs[1].hdumeta[0]['keywords'])
        union.update(1, stubs[1].hdumeta[1]['keywords'])
        union.update(1, stubs[1].hdumeta[1]['format'][1:], columns=True)
        union.update(0, stubs[2].hdumeta[0]['keywords'])
        union.update(1, stubs[2].hdumeta[1]['keywords'])
        union.update(1, stubs[2].hdumeta[1]['format'], columns=True)
        # self.assertLog(log, -2, "These keywords in HDU0 missing from data: {'OPTKEY2', 'OPTKEY1'}")
        # self.assertLog(log, -1, "These columns in HDU1 missing from data: {'OPT2', 'OPT1'}")
        self.assertEqual(union.counter[0]['keywords']['KEYTEST'], 2)
        self.assertEqual(union.counter[0]['keywords']['UNUSED'], 0)
        self.assertEqual(union.counter[0]['keywords']['BZERO'], 3)
        self.assertEqual(union.counter[1]['format']['UNUSED'], 0)
        self.assertEqual(union.counter[1]['format']['target'], 3)
        self.assertEqual(union.counter[1]['format']['OPT1'], 1)
        self.assertEqual(union.counter[1]['format']['OPT2'], 2)

    def test_collect_files(self):
        """Test finding files that correspond to data model files.
        """
        test_files = (os.path.join(self.data_dir, 'sdR-12345678.fits'),
                      os.path.join(self.data_dir, 'sdR-01234567.fits'),
                      os.path.join(self.data_dir, 'spPlate-1234-54321.fits'),
                      os.path.join(self.data_dir, 'extraneous.fits'))
        for f in test_files:
            open(f, 'a').close()
        model = DataModel(os.path.join(os.environ[DM], 'doc', 'examples', 'sdR.rst'),
                          os.path.join(os.environ[DM], 'doc', 'examples'))
        model.get_regexp(self.data_dir)
        all_files = collect_files(self.data_dir, model)
        self.assertIn(os.path.join(self.data_dir, 'sdR-12345678.fits'), all_files)
        self.assertIn(os.path.join(self.data_dir, 'sdR-01234567.fits'), all_files)

    @patch.object(UnionStub, 'mark_optional')
    @patch.object(UnionStub, 'update')
    def test_union_metadata(self, mock_update, mock_mark):
        """Test collection of stub data.
        """
        stubs = [Stub(self.test_files / 'fits_file.fits'),
                 Stub(self.test_files / 'fits_file.fits'),
                 Stub(self.test_files / 'fits_file.fits')]
        stubs[0].hdumeta[0]['extname'] = 'primary'
        stubs[1].hdumeta[1]['extname'] = ''
        stubs[2].nhdr = 1
        model = DataModel(self.test_files / 'fits_file_optional_columns.rst',
                          os.path.join(os.environ[DM], 'doc', 'examples'))
        foo = model.get_regexp('/desi/spectro/data')
        union_metadata(model, stubs)
        mock_mark.assert_called_once()
        mock_update.assert_has_calls([call(0, [('NAXIS1', '100', 'int', ''), ('NAXIS2', '100', 'int', ''), ('BSCALE', '1', 'int', ''), ('BZERO', '32768', 'int', 'Data are really unsigned 16-bit int.')]),
                                      call(1, [('NAXIS1', '32', 'int', 'length of dimension 1'), ('NAXIS2', '3', 'int', 'length of dimension 2')]),
                                      call(1, [('Name', 'Type', 'Units', 'Description'), ('target', 'char[20]', '', ''), ('V_mag', 'float32', 'mag', ''), ('vdisp', 'float64', 'km/s', '')], columns=True),
                                      call(0, [('NAXIS1', '100', 'int', ''), ('NAXIS2', '100', 'int', ''), ('BSCALE', '1', 'int', ''), ('BZERO', '32768', 'int', 'Data are really unsigned 16-bit int.')]),
                                      call(1, [('NAXIS1', '32', 'int', 'length of dimension 1'), ('NAXIS2', '3', 'int', 'length of dimension 2')]),
                                      call(1, [('Name', 'Type', 'Units', 'Description'), ('target', 'char[20]', '', ''), ('V_mag', 'float32', 'mag', ''), ('vdisp', 'float64', 'km/s', '')], columns=True),
                                      call(0, [('NAXIS1', '100', 'int', ''), ('NAXIS2', '100', 'int', ''), ('BSCALE', '1', 'int', ''), ('BZERO', '32768', 'int', 'Data are really unsigned 16-bit int.')])])

    @patch('sys.argv', ['deep_scan_metadata', '--verbose', '--number', '1000', 'DESI_SPECTRO_DATA/NIGHT/EXPID/desi-EXPID.rst', '/desi/spectro/data'])
    def test_options(self):
        """Test parse of command-line options.
        """
        options = _options()
        self.assertTrue(options.verbose)
        self.assertEqual(options.number, 1000)
        self.assertEqual(options.model, 'DESI_SPECTRO_DATA/NIGHT/EXPID/desi-EXPID.rst')
        self.assertListEqual(options.directory, ['/desi/spectro/data'])
