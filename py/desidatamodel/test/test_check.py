# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""Test desidatamodel.check functions
"""
#
from __future__ import absolute_import, division, print_function, unicode_literals
#
import os
import unittest


class TestCheck(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data_dir = os.path.join(os.path.dirname(__file__),'t')

    @classmethod
    def tearDownClass(cls):
        pass
