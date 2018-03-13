# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""Test data model files for validity.
"""
#
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
#
import os
import unittest
import warnings
from ..check import scan_model, files_to_regexp
from .. import PY3, DataModelError, DataModelWarning

DM = 'DESIDATAMODEL'


class TestModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        if DM in os.environ:
            cls.old_env = os.environ[DM]
        else:
            cls.old_env = None
        os.environ[DM] = os.path.dirname(  # root/
                                         os.path.dirname(  # py/
                                                         os.path.dirname(  # desidatamodel/
                                                                         os.path.dirname(__file__))))  # test/
        cls.doc_dir = os.path.join(os.environ[DM], 'doc')

    @classmethod
    def tearDownClass(cls):
        if cls.old_env is None:
            del os.environ[DM]
        else:
            os.environ[DM] = cls.old_env

    def test_model(self):
        """Validate all data model files.
        """
        roots = [os.path.join(self.doc_dir, d) for d in os.listdir(self.doc_dir)
                 if os.path.isdir(os.path.join(self.doc_dir, d))]
        for root in roots:
            files = scan_model(root)
            #
            # Python has a warnings registry and will not re-issue warnings
            # in some cases.
            #
            # with warnings.catch_warnings(record=True) as w:
            #     warnings.simplefilter('always')
            #     f2r = files_to_regexp(root, '/desi/spectro/data', files)
            #     if len(w) > 0:
            #         m = str(w[0].message)
            #         if 'badModel.rst' not in m:
            #             raise DataModelError(str(w[0].message))
            if os.path.basename(root) == 'examples':
                with self.assertRaises(DataModelError):
                    files_to_regexp('/desi/spectro/data', files,
                                    error=True)
            else:
                files_to_regexp('/desi/spectro/data', files,
                                error=True)
            for f in files:
                meta = f.extract_metadata(error=True)


def test_suite():
    """Allows testing of only this module with the command::

        python setup.py test -m <modulename>
    """
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
