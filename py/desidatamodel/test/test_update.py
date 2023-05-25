# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""Test desidatamodel.update functions
"""
import unittest
import csv
from pkg_resources import resource_filename

from ..update import update


class TestUpdate(unittest.TestCase):

    def test_column_descriptions(self):
        """Ensure that every column described in the CSV file at least
        has a non-empty type and description.
        """
        coldef_file = resource_filename('desidatamodel', 'data/column_descriptions.csv')
        with open(coldef_file, newline='') as csv_columns:
            reader = csv.reader(csv_columns)
            self.assertTrue(all([row[1] for row in reader]))
            foo = csv_columns.seek(0)
            self.assertTrue(all([row[3] for row in reader]))

    def test_update(self):
        input_lines = """
blat
====

This is some example rst text.  Don't trip on this table.

==== === === ===
BLAT FOO BAR BIZ
==== === === ===
A    1   x   10
B    2   y   20
C    3   z   30
==== === === ===

But do update this one:

=============== ======= ===== ==============================
Name            Type    Units Description
=============== ======= ===== ==============================
TARGETID        int64         blah
PETAL_LOC       int16         blah with commas, and stuff.
DEVICE_LOC      int32   s     Note: units are incorrect anyway
TARGET_RA       float64
TARGET_DEC [1]_ float64
FLUX_R          float32
=============== ======= ===== ==============================

.. [1] A footnote to ignore

Final text
""".split('\n')

        # -----
        # updating with out force should only update blank entries
        output_lines = update(input_lines)

        # non-table lines unchanged:
        self.assertEqual(len(input_lines), len(output_lines))
        for i in range(16):
            self.assertEqual(input_lines[i], output_lines[i])

        # But data table appropriately grew for wider units column
        self.assertEqual(output_lines[16],
                         '=============== ======= ========= =====================================')
        self.assertEqual(output_lines[17],
                         'Name            Type    Units     Description')
        self.assertEqual(output_lines[18],
                         '=============== ======= ========= =====================================')

        # non-blank entries remain unchanges (except for Units column width)
        self.assertEqual(output_lines[20], 'PETAL_LOC       int16             blah with commas, and stuff.')

        # check some lines that should have changed
        for line in output_lines[22:]:
            # gained units and descriptions
            if line.startswith('TARGET_RA'):
                self.assertEqual(line, 'TARGET_RA       float64 deg       Barycentric right ascension in ICRS')

            # Footnote was preserved while adding units and description
            if line.startswith('TARGET_DEC'):
                self.assertEqual(line, 'TARGET_DEC [1]_ float64 deg       Barycentric declination in ICRS')

            if line.startswith('FLUX_R'):
                self.assertEqual(line, 'FLUX_R          float32 nanomaggy Flux in the Legacy Survey r-band (AB)')

        # -----
        # Repeat with force=True to update all descriptions
        output_lines = update(input_lines, force=True)

        self.assertEqual(output_lines[20], 'PETAL_LOC       int16             Petal location [0-9]')
