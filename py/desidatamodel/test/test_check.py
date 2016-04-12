# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""Test desidatamodel.check functions
"""
#
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
#
from os import environ
from os.path import dirname, isdir, join
import unittest
from ..check import scan_model


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
