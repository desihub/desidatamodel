# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""Test desidatamodel.unit functions
"""
# import os
import unittest
# from pkg_resources import resource_filename
# from .. import DataModelError
from .datamodeltestcase import DataModelTestCase
from ..unit import DataModelUnit, log


class TestUnit(DataModelTestCase):
    """Test desidatamodel.unit functions
    """

    def test_check_model(self):
        """Test method to validate units.
        """
        erg_msg = self.badUnitMessage('ergs')
        u = DataModelUnit()
        c = u.check_unit('erg')
        self.assertIsNone(c)
        c = u.check_unit('ergs', error=False)
        self.assertIsNone(c)
        c = u.check_unit('nanomaggies', error=True)
        self.assertEqual(c, "'nanomaggies'")
        self.assertLog(log, -1, erg_msg)
        with self.assertRaises(ValueError) as e:
            c = u.check_unit('ergs', error=True)
        self.assertEqual(str(e.exception), erg_msg)
        self.assertLog(log, -1, erg_msg)


def test_suite():
    """Allows testing of only this module with the command::

        python setup.py test -m <modulename>
    """
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
