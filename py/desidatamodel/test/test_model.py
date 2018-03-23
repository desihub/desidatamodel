# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""Test data model files for validity.
"""
#
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
#
import os

from .datamodeltestcase import DataModelTestCase

from ..check import scan_model, files_to_regexp
from .. import PY3, DataModelError


class TestModel(DataModelTestCase):

    def test_model(self):
        """Validate all data model files.
        """
        roots = [os.path.join(self.doc_dir, d)
                 for d in os.listdir(self.doc_dir)
                 if os.path.isdir(os.path.join(self.doc_dir, d))]
        for root in roots:
            files = scan_model(root)
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
