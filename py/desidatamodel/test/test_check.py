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
from ..check import collect_files, files_to_regex, scan_model
from .. import PY3

class TestCheck(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data_dir = join(dirname(__file__), 't')
        if 'DESIDATAMODEL' in environ:
            cls.old_env = environ['DESIDATAMODEL']
        else:
            cls.old_env = None
        environ['DESIDATAMODEL'] = dirname(  # root/
                                           dirname(  # py/
                                           dirname(  # desidatamodel/
                                           dirname(__file__)  # test/
                                           )))
        if PY3:
            cls.assertRegexpMatches = cls.assertRegex

    @classmethod
    def tearDownClass(cls):
        if cls.old_env is None:
            del environ['DESIDATAMODEL']
        else:
            environ['DESIDATAMODEL'] = cls.old_env

    def test_scan_model(self):
        """Test identification of data model files.
        """
        root = join(environ['DESIDATAMODEL'], 'doc', 'examples')
        files = scan_model(root)
        expected = set([join(root, f) for f in ('sdR.rst', 'spPlate.rst')])
        self.assertEqual(set(files), expected)

    def test_files_to_regex(self):
        """Test compilation of regular expressions.
        """
        root = join(environ['DESIDATAMODEL'], 'doc', 'DESI_SPECTRO_DATA')
        files = scan_model(root)
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
        root = join(environ['DESIDATAMODEL'], 'doc', 'examples')
        files = scan_model(root)
        f2r = files_to_regex(root, self.data_dir, files)
        p, e, m = collect_files(self.data_dir, f2r)
        for r in f2r:
            self.assertIn(r, p)
        self.assertEqual(len(e), 5)
        for f in test_files:
            remove(f)

    def test_collect_files_missing(self):
        """Test finding files when some are missing.
        """
        test_files = (join(self.data_dir, 'sdR-12345678.fits'),
                      join(self.data_dir, 'sdR-01234567.fits'))
        for f in test_files:
            open(f, 'a').close()
        root = join(environ['DESIDATAMODEL'], 'doc', 'examples')
        files = scan_model(root)
        f2r = files_to_regex(root, self.data_dir, files)
        p, e, m = collect_files(self.data_dir, f2r)
        self.assertEqual(len(m), 1)
        for f in test_files:
            remove(f)
