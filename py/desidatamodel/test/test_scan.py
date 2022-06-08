# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""Test desidatamodel.scan functions
"""
import os
import unittest
from unittest.mock import patch
from pkg_resources import resource_filename
from astropy.io import fits
from astropy.io.fits.card import Undefined
from collections import OrderedDict

from .datamodeltestcase import DataModelTestCase, DM
from .. import DataModelError
from ..check import DataModel
from ..scan import _options, collect_files, union_metadata, UnionStub


class TestScan(DataModelTestCase):

    def test_UnionStub(self):
        """Test initialization of UnionStub.
        """
        model = DataModel(os.path.join(os.environ[DM], 'doc', 'examples', 'sdR.rst'),
                          os.path.join(os.environ[DM], 'doc', 'examples'))
        union = UnionStub(model, error=False)
        self.assertEqual(union.nhdr, 1)
        self.assertListEqual(union.contents, [union.contents_header,
                                              ('HDU0_', 'FLUX', 'IMAGE', '*Brief Description*')])

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

    @patch('sys.argv', ['deep_scan_metadata', '--verbose', '--number', '1000', 'DESI_SPECTRO_DATA/NIGHT/EXPID/desi-EXPID.rst', '/desi/spectro/data'])
    def test_options(self):
        """Test parse of command-line options.
        """
        options = _options()
        self.assertTrue(options.verbose)
        self.assertEqual(options.number, 1000)
        self.assertEqual(options.section, 'DESI_SPECTRO_DATA/NIGHT/EXPID/desi-EXPID.rst')
        self.assertEqual(options.directory, '/desi/spectro/data')


def test_suite():
    """Allows testing of only this module with the command::

        python setup.py test -m <modulename>
    """
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
