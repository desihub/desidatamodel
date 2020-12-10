# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""Utility class used by other tests.
"""
import os
import tempfile
import unittest
import logging
import shutil
from packaging import version

from astropy import __version__ as astropyVersion

from desiutil.log import log
from desiutil.test.test_log import NullMemoryHandler

DM = 'DESIDATAMODEL'


class DataModelTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.astropyVersion = version.parse(astropyVersion)
        cls.maxDiff = None
        cls.data_dir = tempfile.mkdtemp()
        if DM in os.environ:
            cls.old_env = os.environ[DM]
        else:
            cls.old_env = None
        os.environ[DM] = os.path.dirname(  # root/
                                         os.path.dirname(  # py/
                                                         os.path.dirname(  # desidatamodel/
                                                                         os.path.dirname(__file__))))  # test/
        cls.doc_dir = os.path.join(os.environ[DM], 'doc')

    @classmethod
    def tearDownClass(cls):
        if cls.old_env is None:
            del os.environ[DM]
        else:
            os.environ[DM] = cls.old_env
        shutil.rmtree(cls.data_dir)

    def setUp(self):
        # Replace the log handler with something that writes to memory.
        self.cache_level = log.level
        root_logger = logging.getLogger(log.name.rsplit('.', 1)[0])
        while len(root_logger.handlers) > 0:
            h = root_logger.handlers[0]
            h.flush()
            self.cache_handler = h
            fmt = h.formatter
            root_logger.removeHandler(h)
        mh = NullMemoryHandler()
        mh.setFormatter(fmt)
        root_logger.addHandler(mh)
        log.setLevel(logging.DEBUG)

    def tearDown(self):
        root_logger = logging.getLogger(log.name.rsplit('.', 1)[0])
        while len(root_logger.handlers) > 0:
            h = root_logger.handlers[0]
            h.flush()
            root_logger.removeHandler(h)
        root_logger.addHandler(self.cache_handler)
        log.setLevel(self.cache_level)
        self.cache_level = None
        self.cache_handler = None

    def assertLog(self, logger, order=-1, message=''):
        """Asserts that the `message` is at line `order` in the log buffer.
        """
        root_logger = logging.getLogger(logger.name.rsplit('.', 1)[0])
        handler = root_logger.handlers[0]
        record = handler.buffer[order]
        self.assertEqual(record.getMessage(), message)

    def assertInLog(self, logger, message=''):
        """Asserts that the `message` is one of the lines in the log buffer.
        """
        root_logger = logging.getLogger(logger.name.rsplit('.', 1)[0])
        handler = root_logger.handlers[0]
        ok = False
        for record in handler.buffer:
            if record.getMessage() == message:
                ok = True
                break

        if not ok:
            self.assertTrue(ok, f'Not found in log messages: {message}')

    def badUnitMessage(self, unit):
        """Returns a string that can be used to match errors related to bad units.
        """
        m = "'{0}' did not parse as fits unit: At col {1:d}, Unit 'ergs' not supported by the FITS standard. Did you mean erg?".format(unit, unit.index('ergs'))
        if self.astropyVersion >= version.parse('4.0'):
            m += " If this is meant to be a custom unit, define it with 'u.def_unit'. To have it recognized inside a file reader or other code, enable it with 'u.add_enabled_units'. For details, see http://docs.astropy.org/en/latest/units/combining_and_defining.html"
        if self.astropyVersion >= version.parse('4.0.2'):
            m = m.replace('http', 'https')
        return m
