# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""Test desidatamodel.check functions
"""
#
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
#
import os
import unittest
import warnings
import tempfile
import shutil
from pkg_resources import resource_filename
from ..check import (DataModel, collect_files, files_to_regexp, scan_model,
                     validate_prototypes)
from .. import PY3, DataModelWarning

DM = 'DESIDATAMODEL'


class TestCheck(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data_dir = tempfile.mkdtemp()
        if DM in os.environ:
            cls.old_env = os.environ[DM]
        else:
            cls.old_env = None
        os.environ[DM] = os.path.dirname(  # root/
                                         os.path.dirname(  # py/
                                                         os.path.dirname(  # desidatamodel/
                                                                         os.path.dirname(__file__))))  # test/
        if PY3:
            cls.assertRegexpMatches = cls.assertRegex

    @classmethod
    def tearDownClass(cls):
        if cls.old_env is None:
            del os.environ[DM]
        else:
            os.environ[DM] = cls.old_env
        shutil.rmtree(cls.data_dir)

    def setUp(self):
        warnings.resetwarnings()

    def tearDown(self):
        pass

    def test_scan_model(self):
        """Test identification of data model files.
        """
        root = os.path.join(os.environ[DM], 'doc', 'examples')
        files = scan_model(root)
        expected = set([os.path.join(root, f) for f in ('badModel.rst',
                                                        'sdR.rst',
                                                        'spPlate.rst')])
        found = set([p.filename for p in files])
        self.assertEqual(expected, found)

    def test_files_to_regexp(self):
        """Test compilation of regular expressions.
        """
        root = os.path.join(os.environ[DM], 'doc', 'DESI_SPECTRO_DATA')
        files = scan_model(root)
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            files_to_regexp('/desi/spectro/data', files)
        regexps = ['/desi/spectro/data/20160703/desi-12345678.fits.fz',
                   '/desi/spectro/data/20160703/gfa-12345678.fits',
                   '/desi/spectro/data/20160703/fibermap-12345678.fits']
        expected = [os.path.join(root, 'NIGHT', f) for f in ('desi-EXPID.rst',
                                                             'gfa-EXPID.rst',
                                                             'fibermap-EXPID.rst')]
        expected_f2r = dict(zip(expected, regexps))
        for f in files:
            self.assertRegexpMatches(expected_f2r[f.filename], f.regexp,
                                     ("{0} does not match " +
                                      "{1}").format(f.regexp.pattern,
                                                    expected_f2r[f.filename]))

    def test_collect_files(self):
        """Test finding files that correspond to data model files.
        """
        test_files = (os.path.join(self.data_dir, 'sdR-12345678.fits'),
                      os.path.join(self.data_dir, 'sdR-01234567.fits'),
                      os.path.join(self.data_dir, 'spPlate-1234-54321.fits'))
        for f in test_files:
            open(f, 'a').close()
        root = os.path.join(os.environ[DM], 'doc', 'examples')
        files = scan_model(root)
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            files_to_regexp(self.data_dir, files)
        self.assertEqual(len(w), 1)
        self.assertIsInstance(w[0].message, DataModelWarning)
        self.assertEqual(str(w[0].message),
                         ("{0}/doc/examples/badModel.rst has no file " +
                          "regexp!").format(os.environ[DM]))
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            collect_files(self.data_dir, files)
        self.assertEqual(len(w), 1)
        for f in files:
            self.assertIsNotNone(f.regexp)
            self.assertIsNotNone(f.prototype)
        for f in test_files:
            os.remove(f)

    def test_collect_files_missing(self):
        """Test finding files when some are missing.
        """
        test_files = (os.path.join(self.data_dir, 'sdR-12345678.fits'),
                      os.path.join(self.data_dir, 'sdR-01234567.fits'))
        for f in test_files:
            open(f, 'a').close()
        root = os.path.join(os.environ[DM], 'doc', 'examples')
        files = scan_model(root)
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            files_to_regexp(self.data_dir, files, error=True)
        self.assertEqual(len(w), 1)
        self.assertIsInstance(w[0].message, DataModelWarning)
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            collect_files(self.data_dir, files)
        self.assertEqual(len(w), 2)
        self.assertEqual(str(w[-1].message),
                         ('No files found matching {0}/doc/examples/' +
                          'spPlate.rst!').format(os.environ[DM]))
        # self.assertFalse(w and str(w[-1]))
        for f in test_files:
            os.remove(f)

    def test_extract_metadata(self):
        """Test reading metadata from data model files.
        """
        ex_meta = [{'title': 'HDU0',
                    'extension': 'IMAGE',
                    'extname': 'PRIMARY',
                    'format': 'Data: FITS image [int16, 100x100]',
                    'keywords': [('NAXIS1', '100', 'int', ''),
                                 ('NAXIS2', '100', 'int', ''),
                                 ('BSCALE', '1', 'int', ''),
                                 ('BZERO', '32768', 'int',
                                  'Data are really unsigned 16-bit int.'),
                                 ('EXTNAME', 'PRIMARY', 'str', '')]},
                   {'title': 'HDU1',
                    'extension': 'BINTABLE',
                    'extname': 'Galaxies',
                    'format': [('target', 'char[20]', '', ''),
                               ('V_mag', 'float32', 'mag', ''),
                               ('vdisp',  'float64',  'km/s', '')],
                    'keywords': [('NAXIS1', '32', 'int',
                                  'length of dimension 1'),
                                 ('NAXIS2', '3', 'int',
                                  'length of dimension 2')]}]
        modelfile = resource_filename('desidatamodel.test', 't/fits_file.rst')
        model = DataModel(modelfile, os.path.dirname(modelfile))
        meta = model.extract_metadata()
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
        modelfile = resource_filename('desidatamodel.test', 't/fits_file.rst')
        f = DataModel(modelfile, os.path.dirname(modelfile))
        f.get_regexp(os.path.dirname(modelfile))
        collect_files(os.path.dirname(modelfile), [f])
        # prototypes = {resource_filename('desidatamodel.test',
        #                                 't/fits_file.rst'):
        #               resource_filename('desidatamodel.test',
        #                                 't/fits_file.fits')}
        # w = validate_prototypes(prototypes)
        w = validate_prototypes([f])
        # self.assertEqual(len(w), 2)
        if len(w) > 0:
            print(w[0].message)
            print(w[1].message)

    def test_extract_columns(self):
        """Test extraction of columns from a row of data.
        """
        modelfile = resource_filename('desidatamodel.test', 't/fits_file.rst')
        f = DataModel(modelfile, os.path.dirname(modelfile))
        foo = '======= ============= ==== ====================='
        columns = list(map(len, foo.split()))
        row = 'NAXIS1  32            int  length of dimension 1'
        exc = ('NAXIS1', '32', 'int', 'length of dimension 1')
        c = f._extract_columns(row, columns)
        self.assertEqual(c, exc)

    def test_cross_reference(self):
        modelfile = resource_filename('desidatamodel.test', 't/fits_file.rst')
        f = DataModel(modelfile, os.path.dirname(modelfile))
        line = "See :doc:`Other file <fits_file>`"
        ref = f._cross_reference(line)
        self.assertEqual(ref, resource_filename('desidatamodel.test',
                                                't/fits_file.rst'))


def test_suite():
    """Allows testing of only this module with the command::

        python setup.py test -m <modulename>
    """
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
