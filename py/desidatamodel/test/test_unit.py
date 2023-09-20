# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""Test desidatamodel.unit functions
"""
skip_unit_warning = False
try:
    from desiutil.annotate import FITSUnitWarning
except ImportError:
    skip_unit_warning = True
from .datamodeltestcase import DataModelTestCase
from ..unit import validate_unit, log


class TestUnit(DataModelTestCase):
    """Test desidatamodel.unit functions
    """

    def test_check_model(self):
        """Test method to validate units.
        """
        erg_msg = self.badUnitMessage('ergs')
        c = validate_unit('erg')
        self.assertIsNone(c)
        with self.assertWarns(FITSUnitWarning) as w:
            c = validate_unit('ergs', error=False)
        self.assertEqual(str(w.warning), erg_msg)
        self.assertIsNone(c)
        c = validate_unit('nanomaggies', error=True)
        self.assertEqual(c, "'nanomaggies'")
        with self.assertRaises(ValueError) as e:
            c = validate_unit('ergs', error=True)
        self.assertEqual(str(e.exception), erg_msg)
