# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""Test desidatamodel.stub functions
"""
#
from __future__ import absolute_import, division, print_function, unicode_literals
#
import unittest
from ..stub import extrakey
#
class TestStub(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_extrakey(self):
        """Test the identification of non-boring keys.
        """
        extrakey_tests = {'TTYPE01':False,
            'TFORM12':False,
            'TUNIT00':False,
            'TCOMM33':False,
            'TDIM11':False,
            'BITPIX':False,
            'FOOBAR':True}
        for k in extrakey_tests:
            if extrakey_tests[k]:
                self.assertTrue(extrakey(k))
            else:
                self.assertFalse(extrakey(k))

if __name__ == '__main__':
    unittest.main()
