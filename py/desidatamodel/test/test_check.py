# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""Test desidatamodel.check functions
"""
import os
import sys
from packaging import version
import unittest
from unittest.mock import patch

from .datamodeltestcase import DataModelTestCase, DM

from .. import DataModelError
from ..check import (DataModel, collect_files, files_to_regexp, scan_model,
                     validate_prototypes, log, _options)


class TestCheck(DataModelTestCase):

    def test_DataModel_init(self):
        """Test initialization of the DataModel object.
        """
        modelfile = self.test_files / 'fits_file.rst'
        model = DataModel(modelfile, self.test_files)
        self.assertEqual(model.filename, str(modelfile))
        self.assertEqual(model.section, str(self.test_files))

    def test_DataModel_init_bad_type(self):
        """Test initialization of the DataModel object.
        """
        modelfile = self.test_files / 'fits_file.rst'
        with self.assertRaises(ValueError):
            model = DataModel(None, self.test_files)
        with self.assertRaises(ValueError):
            model = DataModel(modelfile, None)

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
        files_to_regexp('/desi/spectro/data', files)
        regexps = ['/desi/spectro/data/20160703/12345678/centroids-12345678.json',
                   '/desi/spectro/data/20160703/12345678/coordinates-12345678.fits',
                   '/desi/spectro/data/20160703/12345678/desi-12345678.fits.fz',
                   '/desi/spectro/data/20160703/12345678/etc-12345678.json',
                   '/desi/spectro/data/20160703/12345678/fiberassign-123456.fits.gz',
                   '/desi/spectro/data/20160703/12345678/fibermap-12345678.fits',
                   '/desi/spectro/data/20160703/00000123/focus-00000123.fits.fz',
                   '/desi/spectro/data/20160703/00000123/fvc-00000123.fits.fz',
                   '/desi/spectro/data/20160703/00000123/FVC-measure-00000123.fits',
                   '/desi/spectro/data/20160703/00000123/fvc-primary-00000123.fits',
                   '/desi/spectro/data/20160703/00000123/gfa-00000123.fits.fz',
                   '/desi/spectro/data/20160703/00000123/guide-00000123.fits.fz',
                   '/desi/spectro/data/20160703/00000123/guide-rois-00000123.fits.fz',
                   '/desi/spectro/data/20160703/00000123/manifest_00000123.json',
                   '/desi/spectro/data/20160703/00000123/pm-00000123.fits',
                   '/desi/spectro/data/20160703/00000123/request-00000123.json',
                   '/desi/spectro/data/20160703/00000123/sky-00000123.fits.fz']
        expected = [os.path.join(root, 'NIGHT', 'EXPID', f) for f in (
            'centroids-EXPID.rst',
            'coordinates-EXPID.rst',
            'desi-EXPID.rst',
            'etc-EXPID.rst',
            'fiberassign-TILEID.rst',
            'fibermap-EXPID.rst',
            'focus-EXPID.rst',
            'fvc-EXPID.rst',
            'FVC-measure-EXPID.rst',
            'fvc-primary-EXPID.rst',
            'gfa-EXPID.rst',
            'guide-EXPID.rst',
            'guide-rois-EXPID.rst',
            'manifest_EXPID.rst',
            'pm-EXPID.rst',
            'request-EXPID.rst',
            'sky-EXPID.rst',)]
        expected_f2r = dict(zip(expected, regexps))
        for f in files:
            self.assertRegex(expected_f2r[f.filename], f.regexp,
                             ("{0} does not " +
                              "match {1}").format(f.regexp.pattern,
                                                  expected_f2r[f.filename]))

    @patch('desidatamodel.check.re')
    def test_files_to_regexp_with_error(self, mock_re):
        """Test compilation of regular expressions; raise exception.
        """
        mock_re.compile.return_value = None
        root = os.path.join(os.environ[DM], 'doc', 'DESI_SPECTRO_DATA')
        files = scan_model(root)
        with self.assertRaises(DataModelError) as e:
            files_to_regexp('/desi/spectro/data', files, error=True)
        self.assertEqual(str(e.exception), "%s has no file regexp!" % files[0].filename)

    @patch.object(DataModel, '_type_size')
    def test_files_to_regexp_with_missing_filetype(self, mock_type):
        """Test compilation of regular expressions; raise exception for missing file type.
        """
        mock_type.return_value = (None, None)
        root = os.path.join(os.environ[DM], 'doc', 'DESI_SPECTRO_DATA')
        files = scan_model(root)
        with self.assertRaises(DataModelError) as e:
            foo = files[0].get_regexp(root, error=True)
        self.assertEqual(str(e.exception), "%s has missing or invalid file type!" % files[0].filename)
        mock_type.assert_called_once()

    @patch.object(DataModel, '_expectedtypes', ('foo', 'bar'))
    def test_files_to_regexp_with_bad_filetype(self):
        """Test compilation of regular expressions; log unusual file type.
        """
        root = os.path.join(os.environ[DM], 'doc', 'DESI_SPECTRO_DATA')
        files = scan_model(root)
        foo = files[0].get_regexp(root)
        self.assertLog(log, -1, "Unusual file type, fits, detected for {0}!".format(files[0].filename))

    def test_get_regexp_filesize(self):
        """Test extraction of file size from data model documents.
        """
        modelfile = self.test_files / 'fits_file.rst'
        model = DataModel(modelfile, os.path.dirname(modelfile))
        foo = model.get_regexp('/desi/spectro/data')
        self.assertEqual(model.filetype, 'fits')
        self.assertEqual(model.filesize, '28 KB')

    def test_get_regexp_missing_filesize(self):
        """Test extraction of file size from data model documents, missing size.
        """
        modelfile = self.test_files / 'fits_file_no_size.rst'
        model = DataModel(modelfile, os.path.dirname(modelfile))
        foo = model.get_regexp('/desi/spectro/data')
        self.assertEqual(model.filetype, 'fits')
        self.assertEqual(model.filesize, 'Unknown')

    def test_collect_files(self):
        """Test finding files that correspond to data model files.
        """
        test_files = (os.path.join(self.data_dir, 'sdR-12345678.fits'),
                      os.path.join(self.data_dir, 'sdR-01234567.fits'),
                      os.path.join(self.data_dir, 'spPlate-1234-54321.fits'),
                      os.path.join(self.data_dir, 'extraneous.fits'))
        for f in test_files:
            open(f, 'a').close()
        root = os.path.join(os.environ[DM], 'doc', 'examples')
        files = scan_model(root)
        files_to_regexp(self.data_dir, files)

        self.assertInLog(log, ("{0}/doc/examples/badModel.rst has no file " +
                               "regexp!").format(os.environ[DM]))
        collect_files(self.data_dir, files)
        self.assertInLog(log, 'Extraneous file detected: {0}'.format(test_files[3]))
        for f in files:
            if os.path.basename(f.filename) == 'badModel.rst':
                self.assertIsNone(f.regexp)
                self.assertIsNone(f._prototypes)
            else:
                self.assertIsNotNone(f.regexp)
                self.assertIsNotNone(f._prototypes)
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
        files_to_regexp(self.data_dir, files)

        self.assertInLog(log, ("{0}/doc/examples/badModel.rst has no file " +
                               "regexp!").format(os.environ[DM]))
        collect_files(self.data_dir, files)
        self.assertInLog(log, ('No files found matching {0}/doc/examples/' +
                               'spPlate.rst!').format(os.environ[DM]))
        for f in test_files:
            os.remove(f)

    def test_extract_metadata(self):
        """Test reading metadata from data model files.
        """
        ex_meta = {'PRIMARY':
                   {'title': 'HDU0',
                    'number': 0,
                    'extension': 'IMAGE',
                    'extname': 'PRIMARY',
                    'format': 'Data: FITS image [int16, 100x100]',
                    'keywords': [('NAXIS1', '100', 'int', ''),
                                 ('NAXIS2', '100', 'int', ''),
                                 ('BSCALE', '1', 'int', ''),
                                 ('BZERO', '32768', 'int',
                                  'Data are really unsigned 16-bit int.'),
                                 ('EXTNAME', 'PRIMARY', 'str', '')]},
                   'Galaxies':
                   {'title': 'HDU1',
                    'number': 1,
                    'extension': 'BINTABLE',
                    'extname': 'Galaxies',
                    'format': [('target', 'char[20]', '', ''),
                               ('V_mag', 'float32', 'mag', ''),
                               ('vdisp',  'float64',  'km/s', '')],
                    'keywords': [('NAXIS1', '32', 'int',
                                  'length of dimension 1'),
                                 ('NAXIS2', '3', 'int',
                                  'length of dimension 2')]}}
        modelfile = self.test_files / 'fits_file.rst'
        model = DataModel(modelfile, os.path.dirname(modelfile))
        meta = model.extract_metadata()
        self.assertEqual(self.title, 'fits_file')
        self.assertEqual(len(meta.keys()), len(ex_meta.keys()))
        for key, m in meta.items():
            self.assertEqual(m['title'], ex_meta[key]['title'])
            self.assertEqual(m['number'], ex_meta[key]['number'])
            self.assertEqual(m['extension'], ex_meta[key]['extension'])
            self.assertEqual(m['extname'], ex_meta[key]['extname'])
            for k in range(len(m['keywords'])):
                self.assertEqual(m['keywords'][k], ex_meta[key]['keywords'][k])
            if m['extension'] == "IMAGE":
                self.assertEqual(m['format'], ex_meta[key]['format'])
            else:
                for k in range(len(m['format'])):
                    self.assertEqual(m['format'][k], ex_meta[key]['format'][k])

    def test_extract_metadata(self):
        """Test reading metadata from data model files, including a collapsed table.
        """
        ex_meta = {'PRIMARY':
                   {'title': 'HDU0',
                    'number': 0,
                    'extension': 'IMAGE',
                    'extname': 'PRIMARY',
                    'format': 'Data: FITS image [int16, 100x100]',
                    'keywords': [('NAXIS1', '100', 'int', ''),
                                 ('NAXIS2', '100', 'int', ''),
                                 ('BSCALE', '1', 'int', ''),
                                 ('BZERO', '32768', 'int',
                                  'Data are really unsigned 16-bit int.'),
                                 ('EXTNAME', 'PRIMARY', 'str', '')]},
                   'Galaxies':
                   {'title': 'HDU1',
                    'number': 1,
                    'extension': 'BINTABLE',
                    'extname': 'Galaxies',
                    'format': [('target', 'char[20]', '', ''),
                               ('V_mag', 'float32', 'mag', ''),
                               ('vdisp',  'float64',  'km/s', '')],
                    'keywords': [('NAXIS1', '32', 'int',
                                  'length of dimension 1'),
                                 ('NAXIS2', '3', 'int',
                                  'length of dimension 2')]}}
        modelfile = self.test_files / 'fits_file_collapse.rst'
        model = DataModel(modelfile, os.path.dirname(modelfile))
        meta = model.extract_metadata()
        self.assertEqual(len(meta.keys()), len(ex_meta.keys()))
        for key, m in meta.items():
            self.assertEqual(m['title'], ex_meta[key]['title'])
            self.assertEqual(m['number'], ex_meta[key]['number'])
            self.assertEqual(m['extension'], ex_meta[key]['extension'])
            self.assertEqual(m['extname'], ex_meta[key]['extname'])
            for k in range(len(m['keywords'])):
                self.assertEqual(m['keywords'][k], ex_meta[key]['keywords'][k])
            if m['extension'] == "IMAGE":
                self.assertEqual(m['format'], ex_meta[key]['format'])
            else:
                for k in range(len(m['format'])):
                    self.assertEqual(m['format'][k], ex_meta[key]['format'][k])

    def test_extract_metadata_missing_extname(self):
        """Test reading metadata with missing EXTNAME.
        """
        modelfile = self.test_files / 'fits_file.rst'
        model = DataModel(modelfile, os.path.dirname(modelfile))
        meta = model.extract_metadata()
        lines = model._metafile_data.split('\n')
        lines[57] = ''
        model._metafile_data = '\n'.join(lines) + '\n'
        model.hdumeta = None
        with self.assertRaises(DataModelError) as e:
            meta = model.extract_metadata(error=True)
        self.assertEqual(str(e.exception), "HDU 1 in {0} has no EXTNAME!".format(modelfile))
        model.hdumeta = None
        meta = model.extract_metadata(error=False)
        self.assertLog(log, -1, "HDU 1 in {0} has no EXTNAME!".format(modelfile))

    def test_extract_metadata_bad_keyword_unit(self):
        """Test reading metadata with bad FITS BUNIT values.
        """
        erg_msg = self.badUnitMessage('ergs')
        modelfile = self.test_files / 'fits_file.rst'
        model = DataModel(modelfile, os.path.dirname(modelfile))
        meta = model.extract_metadata()
        lines = model._metafile_data.split('\n')
        lines.insert(46, "BUNIT  ergs          str  This is a bad unit.")
        model._metafile_data = '\n'.join(lines) + '\n'
        model.hdumeta = None
        with self.assertRaises(ValueError) as e:
            meta = model.extract_metadata(error=True)
        self.assertEqual(str(e.exception), erg_msg)
        model.hdumeta = None
        meta = model.extract_metadata(error=False)
        self.assertLog(log, -1, "HDU 0 in {0} should have a more meaningful EXTNAME than 'PRIMARY'.".format(modelfile))
        self.assertLog(log, -2, erg_msg)

    def test_extract_metadata_missing_keyword_unit(self):
        """Test reading metadata with missing units for header keywords.
        """
        modelfile = self.test_files / 'fits_file.rst'
        model = DataModel(modelfile, os.path.dirname(modelfile))
        meta = model.extract_metadata()
        lines = model._metafile_data.split('\n')
        lines.insert(46, "BUNIT  erg                This is a bad unit.")
        model._metafile_data = '\n'.join(lines) + '\n'
        model.hdumeta = None
        with self.assertRaises(DataModelError) as e:
            meta = model.extract_metadata(error=True)
        self.assertEqual(str(e.exception), "Missing type for keyword BUNIT in HDU 0 of {0}!".format(modelfile))
        model.hdumeta = None
        meta = model.extract_metadata(error=False)
        self.assertLog(log, -1, "HDU 0 in {0} should have a more meaningful EXTNAME than 'PRIMARY'.".format(modelfile))
        self.assertLog(log, -2, "Missing type for keyword BUNIT in HDU 0 of {0}!".format(modelfile))

    def test_extract_metadata_bad_column_unit(self):
        """Test reading metadata with bad FITS column units.
        """
        erg_msg = self.badUnitMessage('ergs')
        modelfile = self.test_files / 'fits_file.rst'
        model = DataModel(modelfile, os.path.dirname(modelfile))
        meta = model.extract_metadata()
        lines = model._metafile_data.split('\n')
        lines[85] = 'vdisp  float64  ergs'
        model._metafile_data = '\n'.join(lines) + '\n'
        model.hdumeta = None
        with self.assertRaises(ValueError) as e:
            meta = model.extract_metadata(error=True)
        self.assertEqual(str(e.exception), erg_msg)
        model.hdumeta = None
        meta = model.extract_metadata(error=False)
        self.assertLog(log, -1, erg_msg)

    def test_extract_metadata_missing_column_type(self):
        """Test reading metadata with missing FITS column types.
        """
        modelfile = self.test_files / 'fits_file.rst'
        model = DataModel(modelfile, os.path.dirname(modelfile))
        meta = model.extract_metadata()
        lines = model._metafile_data.split('\n')
        lines[85] = 'vdisp'
        model._metafile_data = '\n'.join(lines) + '\n'
        model.hdumeta = None
        with self.assertRaises(DataModelError) as e:
            meta = model.extract_metadata(error=True)
        self.assertEqual(str(e.exception), "Missing type for column vdisp in HDU 1 of {0}!".format(modelfile))
        model.hdumeta = None
        meta = model.extract_metadata(error=False)
        self.assertLog(log, -1, "Missing type for column vdisp in HDU 1 of {0}!".format(modelfile))

    def test_extract_metadata_with_hdu_span(self):
        """Test reading metadata with a HDU span.
        """
        modelfile = self.test_files / 'fits_file_hduspan.rst'
        model = DataModel(modelfile, os.path.dirname(modelfile))
        meta = model.extract_metadata()
        self.assertEqual(meta['TWO']['number'], 2)

    def test_extract_metadata_with_hdu_span_no_spanext(self):
        """Test reading metadata with a HDU span, but with no reference HDU.
        """
        modelfile = self.test_files / 'fits_file_hduspan_no_spanext.rst'
        model = DataModel(modelfile, os.path.dirname(modelfile))
        with self.assertRaises(DataModelError) as e:
            meta = model.extract_metadata()
        self.assertEqual(str(e.exception),
                         "Cannot find EXTNAME = 'MISSING' which is supposed to define HDU 2 to HDU 5!")

    def test_extract_metadata_with_hdu_span_bad_extname(self):
        """Test reading metadata with a HDU span, but with bad EXTNAME specification.
        """
        modelfile = self.test_files / 'fits_file_hduspan_bad_extname.rst'
        model = DataModel(modelfile, os.path.dirname(modelfile))
        meta = model.extract_metadata()
        self.assertLog(log, -1, "Range specification from HDU 2 to HDU 5 does not have a matching EXTNAME specification!")

    def test_extract_metadata_bad_format(self):
        """Test reading metadata with a bad HDU format specification.
        """
        modelfile = self.test_files / 'fits_file_bad_format.rst'
        model = DataModel(modelfile, os.path.dirname(modelfile))
        with self.assertRaises(DataModelError) as e:
            meta = model.extract_metadata()
        self.assertEqual(str(e.exception),
                         "Unable to determine format for HDU 1 in %s!" % modelfile)

    def test_validate_prototypes(self):
        """Test the data model validation function.
        """
        modelfile = self.test_files / 'fits_file.rst'
        f = DataModel(modelfile, os.path.dirname(modelfile))
        f.get_regexp(os.path.dirname(modelfile))
        collect_files(os.path.dirname(modelfile), [f])
        validate_prototypes([f])

    def test_validate_prototype_no_prototype(self):
        """Test the data model validation method with no prototype.
        """
        modelfile = self.test_files / 'fits_file.rst'
        f = DataModel(modelfile, os.path.dirname(modelfile))
        f.get_regexp(os.path.dirname(modelfile))
        collect_files(os.path.dirname(modelfile), [f])
        f._prototypes = None
        f.validate_prototype(error=True)

    def test_validate_prototype_not_verifiable_prototype(self):
        """Test the data model validation method with prototypes that are not
        currently verifiable.
        """
        modelfile = self.test_files / 'fits_file.rst'
        f = DataModel(modelfile, os.path.dirname(modelfile))
        f.get_regexp(os.path.dirname(modelfile))
        collect_files(os.path.dirname(modelfile), [f])
        f._prototypes = ('a.txt', 'b.txt.gz', 'c.txt.fz', 'd.txt', 'e.txt')
        f.validate_prototype(error=True)
        self.assertLog(log, -1, "Prototypes for {0} cannot be validated with current software, skipping.".format(f.filename))

    def test_validate_prototype_oserror(self):
        """Test the data model validation method with a file that throws an error.
        """
        modelfile = self.test_files / 'fits_file.rst'
        f = DataModel(modelfile, os.path.dirname(modelfile))
        f.get_regexp(os.path.dirname(modelfile))
        collect_files(os.path.dirname(modelfile), [f])
        # self.assertListEqual(f._prototypes, [os.path.join(os.path.dirname(modelfile), 'fits_file.fits'), ''])
        f._prototypes = [os.path.join(os.path.dirname(modelfile), 'data_table.txt'),
                         os.path.join(os.path.dirname(modelfile), 'fits_file.fits')]
        f.validate_prototype(error=True)
        self.assertLog(log, -4, "Error opening {0}, skipping to next candidate.".format(f._prototypes[0]))
        if self.astropyVersion < version.parse('4.1'):
            empty = 'Empty or corrupt FITS file'
        elif self.astropyVersion < version.parse('5.0'):
            empty = 'No SIMPLE card found, this file does not appear to be a valid FITS file'
        else:
            empty = 'No SIMPLE card found, this file does not appear to be a valid FITS file. If this is really a FITS file, try with ignore_missing_simple=True'
        self.assertLog(log, -3, "Message was: '{0}'.".format(empty))
        self.assertLog(log, -2, "(s.nhdr = 2) == (len(modelmeta.keys()) = 2)")
        self.assertLog(log, -1, "Comparing {0} to {1}.".format(f._prototypes[1], modelfile))

    def test_validate_prototype_hdu_mismatch(self):
        """Test the data model validation method with wrong number of HDUs.
        """
        modelfile = self.test_files / 'fits_file.rst'
        f = DataModel(modelfile, os.path.dirname(modelfile))
        f.get_regexp(os.path.dirname(modelfile))
        collect_files(os.path.dirname(modelfile), [f])
        foo = f.extract_metadata()
        f.hdumeta['foobar'] = 'baz'
        f.validate_prototype(error=True)
        self.assertLog(log, -2, "{0} has the wrong number of sections (HDUs) according to {1}, skipping to next candidate.".format(str(modelfile).replace('.rst', '.fits'), modelfile))
        self.assertLog(log, -1, "No useful prototype files found for {0}!".format(modelfile))

    def test_validate_prototype_hdu_keyword_mismatch(self):
        """Test the data model validation method with wrong number of HDU keywords.
        """
        modelfile = self.test_files / 'fits_file.rst'
        f = DataModel(modelfile, os.path.dirname(modelfile))
        f.get_regexp(os.path.dirname(modelfile))
        collect_files(os.path.dirname(modelfile), [f])
        f.validate_prototype()
        f._stub_meta[0]['keywords'].append(('BUNIT', 'erg', 'str', 'This is a test.'))
        f.validate_prototype(error=True)
        self.assertLog(log, -1, "Prototype file {0} has these keywords in HDU0 missing from model: {{'BUNIT'}}".format(str(modelfile).replace('.rst', '.fits')))

    def test_validate_prototype_hdu_keyword_type_mismatch(self):
        """Test the data model validation method with a keyword type mismatch.
        """
        modelfile = self.test_files / 'fits_file.rst'
        f = DataModel(modelfile, os.path.dirname(modelfile))
        f.get_regexp(os.path.dirname(modelfile))
        collect_files(os.path.dirname(modelfile), [f])
        f.extract_metadata()
        f.hdumeta['PRIMARY']['keywords'][2] = ('BSCALE', '1.2', 'float', '')
        f.validate_prototype()
        self.assertLog(log, -1, "File %s HDU%d keyword %s has different keyword type according to %s (%s != %s)." % (f.prototype, 0, 'BSCALE', modelfile, 'int', 'float'))

    def test_validate_prototype_hdu_wrong_keyword(self):
        """Test the data model validation method with wrong HDU keyword names.
        """
        modelfile = self.test_files / 'fits_file.rst'
        f = DataModel(modelfile, os.path.dirname(modelfile))
        f.get_regexp(os.path.dirname(modelfile))
        collect_files(os.path.dirname(modelfile), [f])
        f.validate_prototype()
        f._stub_meta[0]['keywords'][-1] = ('BUNIT', 'erg', 'str', 'This is a test.')
        f.validate_prototype(error=True)
        self.assertLog(log, -2, "Prototype file {0} has these keywords in HDU0 missing from model: {{'BUNIT'}}".format(str(modelfile).replace('.rst', '.fits')))
        self.assertLog(log, -1, "Model file {0} has these keywords in HDU0 missing from data: {{'BZERO'}}".format(modelfile))

    def test_validate_prototype_hdu_extension_type(self):
        """Test the data model validation method with wrong HDU extension type.
        """
        modelfile = self.test_files / 'fits_file.rst'
        f = DataModel(modelfile, os.path.dirname(modelfile))
        f.get_regexp(os.path.dirname(modelfile))
        collect_files(os.path.dirname(modelfile), [f])
        f.validate_prototype()
        f._stub_meta[1]['extension'] = 'IMAGE'
        f.validate_prototype(error=True)
        self.assertLog(log, -1, "Prototype file {0} has an extension type mismatch in HDU1 (IMAGE != BINTABLE) according to {1}.".format(str(modelfile).replace('.rst', '.fits'), modelfile))
        # f._stub_meta[1]['extname'] = ''
        # f.validate_prototype(error=True)
        # self.assertLog(log, -1, "Prototype file {0} has no EXTNAME in HDU1.".format(str(modelfile).replace('.rst', '.fits')))

    def test_validate_prototype_hdu_extension_name(self):
        """Test the data model validation method with wrong HDU extension name.
        """
        modelfile = self.test_files / 'fits_file.rst'
        f = DataModel(modelfile, os.path.dirname(modelfile))
        f.get_regexp(os.path.dirname(modelfile))
        collect_files(os.path.dirname(modelfile), [f])
        f.validate_prototype()
        f._stub_meta[1]['extname'] = 'GALAXY'
        f.validate_prototype(error=True)
        self.assertLog(log, -1, "Prototype file {0} has an EXTNAME mismatch in HDU1 (GALAXY != Galaxies) according to {1}.".format(str(modelfile).replace('.rst', '.fits'), modelfile))
        f._stub_meta[1]['extname'] = ''
        f.validate_prototype(error=True)
        self.assertLog(log, -2, "Prototype file {0} has no EXTNAME in HDU1.".format(str(modelfile).replace('.rst', '.fits')))
        self.assertLog(log, -1, "Could not find EXTNAME = '' in {0}; trying by HDU number.".format(modelfile))

    def test_validate_prototype_hdu_bad_format(self):
        """Test the data model validation method with a bad HDU format in the model.
        """
        modelfile = self.test_files / 'fits_file.rst'
        f = DataModel(modelfile, os.path.dirname(modelfile))
        f.get_regexp(os.path.dirname(modelfile))
        collect_files(os.path.dirname(modelfile), [f])
        f.extract_metadata()
        del f.hdumeta['PRIMARY']['format']
        with self.assertRaises(KeyError):
            foo = f.hdumeta['PRIMARY']['format']
        f.validate_prototype()
        self.assertLog(log, -1, "Prototype file {0} has an extension format mismatch in HDU0 according to {1}.".format(f.prototype, modelfile))

    def test_validate_prototype_hdu_alternate_format(self):
        """Test the data model validation method with an alternate HDU format in the model.
        """
        modelfile = self.test_files / 'fits_file.rst'
        f = DataModel(modelfile, os.path.dirname(modelfile))
        f.get_regexp(os.path.dirname(modelfile))
        collect_files(os.path.dirname(modelfile), [f])
        f.extract_metadata()
        f.hdumeta['PRIMARY']['format'] = 'Data: FITS image [int16'
        f.validate_prototype()
        f._stub.hdumeta[0]['format'] = 'Data: FITS image [int16'
        f.validate_prototype()
        self.assertLog(log, -1, "Comparing {0} to {1}.".format(f.prototype, modelfile))

    def test_validate_prototype_hdu_bad_extension(self):
        """Test the data model validation method with a bad HDU extension in the model.
        """
        modelfile = self.test_files / 'fits_file.rst'
        f = DataModel(modelfile, os.path.dirname(modelfile))
        f.get_regexp(os.path.dirname(modelfile))
        collect_files(os.path.dirname(modelfile), [f])
        f.extract_metadata()
        del f.hdumeta['PRIMARY']['extension']
        with self.assertRaises(KeyError):
            foo = f.hdumeta['PRIMARY']['extension']
        f.validate_prototype()
        self.assertLog(log, -1, "Prototype file {0} has an extension type mismatch in HDU0 (IMAGE != Extension type not found) according to {1}.".format(f.prototype, modelfile))

    def test_validate_prototype_hdu_missing_column(self):
        """Test the data model validation method with missing column in the model.
        """
        modelfile = self.test_files / 'fits_file.rst'
        f = DataModel(modelfile, os.path.dirname(modelfile))
        f.get_regexp(os.path.dirname(modelfile))
        collect_files(os.path.dirname(modelfile), [f])
        f.extract_metadata()
        del f.hdumeta['Galaxies']['format'][2]
        f.validate_prototype()
        self.assertLog(log, -1, "Prototype file %s has these columns in HDU1 missing from model: %s" % (f.prototype, str(set(['vdisp']))))

    def test_validate_prototype_hdu_missing_data_column(self):
        """Test the data model validation method with missing column in the data.
        """
        modelfile = self.test_files / 'fits_file.rst'
        f = DataModel(modelfile, os.path.dirname(modelfile))
        f.get_regexp(os.path.dirname(modelfile))
        collect_files(os.path.dirname(modelfile), [f])
        f.extract_metadata()
        f.hdumeta['Galaxies']['format'].append(('extra', 'int16', '', ''))
        f.validate_prototype()
        self.assertLog(log, -1, "Model file %s has these columns in HDU1 missing from data: %s" % (modelfile, str(set(['extra']))))

    def test_validate_prototype_hdu_bad_column_type(self):
        """Test the data model validation method with a bad column type.
        """
        modelfile = self.test_files / 'fits_file.rst'
        f = DataModel(modelfile, os.path.dirname(modelfile))
        f.get_regexp(os.path.dirname(modelfile))
        collect_files(os.path.dirname(modelfile), [f])
        f.extract_metadata()
        f.hdumeta['Galaxies']['format'][1] = ('V_mag', 'float64', 'mag', '')
        f.validate_prototype()
        self.assertLog(log, -1, "File %s HDU%d column %s has different type according to %s (%s != %s)." % (f.prototype, 1, 'V_mag', modelfile, 'float32', 'float64'))

    def test_validate_prototype_hdu_bad_column_unit(self):
        """Test the data model validation method with a bad column unit.
        """
        modelfile = self.test_files / 'fits_file.rst'
        f = DataModel(modelfile, os.path.dirname(modelfile))
        f.get_regexp(os.path.dirname(modelfile))
        collect_files(os.path.dirname(modelfile), [f])
        f.extract_metadata()
        f.hdumeta['Galaxies']['format'][1] = ('V_mag', 'float32', 'counts', '')
        f.validate_prototype()
        self.assertLog(log, -1, "File %s HDU%d column %s has different units according to %s (%s != %s)." % (f.prototype, 1, 'V_mag', modelfile, 'mag', 'counts'))

    def test_validate_prototype_optional_keywords(self):
        """Test the data model validation method with optional keywords.
        """
        modelfile = self.test_files / 'fits_file_optional_columns.rst'
        f = DataModel(modelfile, os.path.dirname(modelfile))
        f.get_regexp(os.path.dirname(modelfile))
        collect_files(os.path.dirname(modelfile), [f])
        f.extract_metadata()
        self.assertEqual(f.hdumeta['PRIMARY']['keywords'][4][0], 'OPTKEY1 [1]_')
        self.assertEqual(f.hdumeta['PRIMARY']['keywords'][5][0], 'OPTKEY2 [1]_')
        f.validate_prototype()
        self.assertLog(log, -1, "Comparing %s to %s." % (f.prototype, modelfile))

    def test_validate_prototype_optional_columns(self):
        """Test the data model validation method with optional columns.
        """
        modelfile = self.test_files / 'fits_file_optional_columns.rst'
        f = DataModel(modelfile, os.path.dirname(modelfile))
        f.get_regexp(os.path.dirname(modelfile))
        collect_files(os.path.dirname(modelfile), [f])
        f.extract_metadata()
        self.assertEqual(f.hdumeta['Galaxies']['format'][1][0], 'OPT1 [1]_')
        f.validate_prototype()
        self.assertLog(log, -1, "Comparing %s to %s." % (f.prototype, modelfile))

    def test_validate_prototype_variable_columns(self):
        """Test the data model validation method with variable-size columns.
        """
        modelfile = self.test_files / 'fits_file_variable_columns.rst'
        f = DataModel(modelfile, os.path.dirname(modelfile))
        f.get_regexp(os.path.dirname(modelfile))
        collect_files(os.path.dirname(modelfile), [f])
        f.extract_metadata()
        self.assertEqual(f.hdumeta['Galaxies']['format'][0][1], 'char[*]')
        f.validate_prototype()
        self.assertLog(log, -1, "File %s HDU1 column target has an acceptable variable-length string according to %s." % (f.prototype, modelfile))

    def test_extract_columns(self):
        """Test extraction of columns from a row of data.
        """
        modelfile = self.test_files / 'fits_file.rst'
        f = DataModel(modelfile, os.path.dirname(modelfile))
        foo = '======= ============= ==== ============'
        columns = list(map(len, foo.split()))
        row = 'NAXIS1  32            int  length of dimension 1'
        exc = ('NAXIS1', '32', 'int', 'length of dimension 1')
        c = f._extract_columns(row, columns)
        self.assertEqual(c, exc)

    def test_cross_reference(self):
        """Test parsing of cross-references.
        """
        modelfile = self.test_files / 'fits_file.rst'
        f = DataModel(modelfile, os.path.dirname(modelfile))
        line = "See :doc:`Other file <fits_file>`"
        ref = f._cross_reference(line)
        self.assertEqual(ref, str(modelfile))

    @patch('sys.argv', ['check_model', '--verbose', '--compare-files', 'DESI_SPECTRO_DATA', '/desi/spectro/data/desi-00000000.fits.fz'])
    def test_options(self):
        """Test parse of command-line options.
        """
        options = _options()
        self.assertTrue(options.verbose)
        self.assertTrue(options.files)
        self.assertEqual(options.section, 'DESI_SPECTRO_DATA')
        self.assertEqual(options.directory, '/desi/spectro/data/desi-00000000.fits.fz')
