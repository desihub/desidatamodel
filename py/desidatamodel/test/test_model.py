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
import warnings
from ..check import scan_model, files_to_regex, extract_metadata
from .. import PY3, DataModelError, DataModelWarning

DM = 'DESIDATAMODEL'


class TestModel(unittest.TestCase):

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
        cls.doc_dir = join(environ[DM], 'doc')

    @classmethod
    def tearDownClass(cls):
        if cls.old_env is None:
            del environ[DM]
        else:
            environ[DM] = cls.old_env

    def test_model(self):
        """Validate all data model files.
        """
        roots = [join(self.doc_dir, d) for d in listdir(self.doc_dir)
                 if join(self.doc_dir, d)]
        for root in roots:
            files = scan_model(root)
            #
            # Python has a warnings registry and will not re-issue warnings
            # in some cases.
            #
            # with warnings.catch_warnings(record=True) as w:
            #     warnings.simplefilter('always')
            #     f2r = files_to_regex(root, '/desi/spectro/data', files)
            #     if len(w) > 0:
            #         m = str(w[0].message)
            #         if 'badModel.rst' not in m:
            #             raise DataModelError(str(w[0].message))
            for f in files:
                meta = extract_metadata(f)
