# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""Test desidatamodel.columns functions
"""
import unittest

from ..columns import format_columns


class TestColumns(unittest.TestCase):

    def test_format_columns(self):
        """Test column formatting operations.
        """
        data = [('one', 'two', 'three'),
                ('four', 'five', 'six'),
                ('seven', 'eight', 'nine'),
                ('ten', 'eleven', 'twelve')]
        format_string, separator = format_columns(data)
        self.assertEqual(format_string, "{0:5} {1:6} {2:6}")
        self.assertEqual(separator, '===== ====== ======')
