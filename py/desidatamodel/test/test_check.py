# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""Test desidatamodel.check functions
"""
#
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
#
from os import environ, remove
from os.path import dirname, isdir, join
import unittest
import warnings
from ..check import (collect_files, files_to_regex, scan_model,
                     extract_metadata, validate_prototypes,
                     extract_columns)
from .. import PY3, DataModelWarning

DM = 'DESIDATAMODEL'


class TestCheck(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data_dir = join(dirname(__file__), 't')
        if DM in environ:
            cls.old_env = environ[DM]
        else:
            cls.old_env = None
        environ[DM] = dirname(  # root/
                              dirname(  # py/
                                      dirname(  # desidatamodel/
                                              dirname(__file__))))  # test/
        if PY3:
            cls.assertRegexpMatches = cls.assertRegex

    @classmethod
    def tearDownClass(cls):
        if cls.old_env is None:
            del environ[DM]
        else:
            environ[DM] = cls.old_env

    def test_scan_model(self):
        """Test identification of data model files.
        """
        root = join(environ[DM], 'doc', 'examples')
        files = scan_model(root)
        expected = set([join(root, f) for f in ('badModel.rst',
                                                'sdR.rst', 'spPlate.rst')])
        self.assertEqual(set(files), expected)

    def test_files_to_regex(self):
        """Test compilation of regular expressions.
        """
        root = join(environ[DM], 'doc', 'DESI_SPECTRO_DATA')
        files = scan_model(root)
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            f2r = files_to_regex(root, '/desi/spectro/data', files)
        regexes = ['/desi/spectro/data/20160703/desi-12345678.fits',
                   '/desi/spectro/data/20160703/fibermap-12345678.fits']
        expected = [join(root, 'NIGHT', f) for f in ('desi-EXPID.rst',
                                                     'fibermap-EXPID.rst')]
        expected_f2r = dict(zip(expected, regexes))
        for k in f2r:
            self.assertRegexpMatches(expected_f2r[k], f2r[k],
                                     ("{0} does not match " +
                                      "{1}").format(f2r[k].pattern,
                                                    expected_f2r[k]))

    def test_collect_files(self):
        """Test finding files that correspond to data model files.
        """
        test_files = (join(self.data_dir, 'sdR-12345678.fits'),
                      join(self.data_dir, 'sdR-01234567.fits'),
                      join(self.data_dir, 'spPlate-1234-54321.fits'))
        for f in test_files:
            open(f, 'a').close()
        root = join(environ[DM], 'doc', 'examples')
        files = scan_model(root)
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            f2r = files_to_regex(root, self.data_dir, files)
        self.assertEqual(len(w), 1)
        self.assertIsInstance(w[0].message, DataModelWarning)
        self.assertEqual(str(w[0].message),
                         ("{0}/doc/examples/badModel.rst has no file " +
                          "regex!").format(environ[DM]))
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            p = collect_files(self.data_dir, f2r)
        self.assertEqual(len(w), 5)
        for r in f2r:
            if f2r[r] is not None:
                self.assertIn(r, p)
        for f in test_files:
            remove(f)

    def test_collect_files_missing(self):
        """Test finding files when some are missing.
        """
        test_files = (join(self.data_dir, 'sdR-12345678.fits'),
                      join(self.data_dir, 'sdR-01234567.fits'))
        for f in test_files:
            open(f, 'a').close()
        root = join(environ[DM], 'doc', 'examples')
        files = scan_model(root)
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            f2r = files_to_regex(root, self.data_dir, files)
        self.assertEqual(len(w), 1)
        self.assertIsInstance(w[0].message, DataModelWarning)
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            p = collect_files(self.data_dir, f2r)
        self.assertEqual(len(w), 6)
        self.assertEqual(str(w[-1].message),
                         ('No files found matching {0}/doc/examples/' +
                          'spPlate.rst!').format(environ[DM]))
        # self.assertFalse(w and str(w[-1]))
        for f in test_files:
            remove(f)

    def test_extract_metadata(self):
        """Test reading metadata from data model files.
        """
        ex_meta = [{'title': 'HDU0',
                    'extension': 'IMAGE',
                    'extname': '',
                    'format': 'Data: FITS image [int16, 100x100]',
                    'keywords': [('NAXIS1', '100', 'int', ''),
                                 ('NAXIS2', '100', 'int', ''),
                                 ('BSCALE', '1', 'int', ''),
                                 ('BZERO', '32768', 'int',
                                  'Data are really unsigned 16-bit int.')]},
                   {'title': 'HDU1',
                    'extension': 'BINTABLE',
                    'extname': 'Galaxies',
                    'format': [('target', 'char[20]', '', ''),
                               ('V_mag', 'float32', 'mag', ''),
                               ('vdisp',  'float64',  'km/s', '')],
                    'keywords': [('NAXIS1', '32', 'int',
                                  'length of dimension 1'),
                                 ('NAXIS2', '3', 'int',
                                  'length of dimension 2'),
                                 ('EXTNAME', 'Galaxies', 'str',
                                  'Name of this HDU.')]}]
        modelfile = join(self.data_dir, 'fits_file.rst')
        meta = extract_metadata(modelfile)
        self.assertEqual(len(meta), 2)
        for i, m in enumerate(meta):
            self.assertEqual(m['title'], ex_meta[i]['title'])
            self.assertEqual(m['extension'], ex_meta[i]['extension'])
            self.assertEqual(m['extname'], ex_meta[i]['extname'])
            for k in range(len(m['keywords'])):
                self.assertEqual(m['keywords'][k], ex_meta[i]['keywords'][k])
            if m['extension'] == "IMAGE":
                self.assertEqual(m['format'], ex_meta[i]['format'])
            else:
                for k in range(len(m['format'])):
                    self.assertEqual(m['format'][k], ex_meta[i]['format'][k])

    def test_validate_prototypes(self):
        """Test the data model validation function.
        """
        prototypes = {join(self.data_dir, 'fits_file.rst'):
                      join(self.data_dir, 'fits_file.fits')}
        w = validate_prototypes(prototypes)
        self.assertEqual(len(w), 0)

    def test_extract_columns(self):
        """Test extraction of columns from a row of data.
        """
        foo = '======= ============= ==== ====================='
        columns = list(map(len, foo.split()))
        row = 'NAXIS1  32            int  length of dimension 1'
        exc = ('NAXIS1', '32', 'int', 'length of dimension 1')
        c = extract_columns(row, columns)
        self.assertEqual(c, exc)
