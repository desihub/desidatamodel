# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""Test data model files for validity.
"""
import os

from .datamodeltestcase import DataModelTestCase

from ..check import scan_model, files_to_regexp
from .. import DataModelError


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
