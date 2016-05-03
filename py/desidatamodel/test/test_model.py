# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""Test data model files for validity.
"""
#
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
#
from os import environ, listdir, remove
from os.path import dirname, isdir, join
import unittest
# import warnings
from ..check import scan_model, extract_metadata
from .. import PY3, DataModelWarning

class TestModel(unittest.TestCase):

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
        cls.doc_dir = join(environ['DESIDATAMODEL'], 'doc')

    @classmethod
    def tearDownClass(cls):
        if cls.old_env is None:
            del environ['DESIDATAMODEL']
        else:
            environ['DESIDATAMODEL'] = cls.old_env

    def test_model(self):
        """Validate all data model files.
        """
        roots = [join(self.doc_dir, d) for d in listdir(self.doc_dir)
                 if join(self.doc_dir, d)]
        for root in roots:
            files = scan_model(root)
            for f in files:
                meta = extract_metadata(f)
