# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""Test desidatamodel.unit functions
"""
# import os
import unittest
# from pkg_resources import resource_filename

from .datamodeltestcase import DataModelTestCase, DM

# from .. import DataModelError
# from ..check import (DataModel, collect_files, files_to_regexp, scan_model,
#                      validate_prototypes, log)
from ..unit import DataModelUnit

class TestUnit(DataModelTestCase):
    """Test desidatamodel.unit functions
    """

    def test_check_model(self):
        """Test method to validate units.
        """
        pass


def test_suite():
    """Allows testing of only this module with the command::

        python setup.py test -m <modulename>
    """
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
