# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""Utility class used by other tests.
"""
from __future__ import absolute_import

import os
import tempfile
import unittest
import logging
import shutil

from desiutil.log import log
from desiutil.test.test_log import TestHandler

from .. import PY3

DM = 'DESIDATAMODEL'


class DataModelTestCase(unittest.TestCase):

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
        mh = TestHandler()
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
        """Examine the log messages.
        """
        root_logger = logging.getLogger(logger.name.rsplit('.', 1)[0])
        handler = root_logger.handlers[0]
        record = handler.buffer[order]
        self.assertEqual(record.getMessage(), message)
