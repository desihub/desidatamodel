# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""
====================
desidatamodel.update
====================

Tools to update column units and descriptions in a pre-existing datamodel file.
"""

import re
import sys
from html import escape
from pkg_resources import resource_filename
import argparse
import numpy as np
from astropy.table import Table
from astropy.io.ascii import RST

from desiutil.log import get_logger

from .stub import read_column_descriptions


def read_table_rows(lines, i):
    """
    Read an RST-format table from a set of lines

    Args:
        lines (list of str): lines from data model file
        i (int): start at line number i

    Return: None or list of dict(Name, Type, Units, Description)

    Looks for data table description of the form::

       ==== ==== ===== ===========
       Name Type Units Description
       ==== ==== ===== ===========
       blat int  s     biz bat bar
       foo  int        bing bang boom
       ==== ==== ===== ===========

    while allowing the columns to have arbitrary widths or possibly be blank.

    Returns None if table starting at line `i` doesn't match that form.
    """
    h1 = lines[i]    # expected header separator with 4 sets of "==="
    h2 = lines[i+1]  # expected column names
    h3 = lines[i+2]  # expected repeat of header separator

    # check this is the right kind of table, or not at start of table
    if h1 != h3 or h2.split() != ['Name', 'Type', 'Units', 'Description']:
        return None

    # column indices where each column starts
    itype = h2.index('Type')
    iunit = h2.index('Units')
    idesc = h2.index('Description')

    # Assemble the rows as a list of dict objects
    rows = list()
    for j in range(i+3, len(lines)):
        if lines[j] == h3:   # table footer === === === ===
            break

        line = lines[j]

        colname = line[0:itype].strip()
        coltype = line[itype:iunit].strip()
        colunit = line[iunit:idesc].strip()
        coldesc = line[idesc:].strip()
        rows.append(dict(Name=colname, Type=coltype, Units=colunit, Description=coldesc))

    return rows


def format_rst_table(table):
    """
    Format an astropy Table in left-aligned RST format

    Args:
        table (astropy.table.Table)

    Returns:
        list of strings to print/write for the RST-format table

    Note: this doesn't use astropy.io.ascii.rst because that generates
    right-aligned columns.
    """
    # determin columns widths as max of column name or column values
    colwidths = list()
    for name in table.colnames:
        width = max(len(name), max(list(map(len, table[name]))))
        colwidths.append(width)

    # separator line for table header and footer
    separator_line = ' '.join(['='*w for w in colwidths])

    # format code for 4 columns of the appropriate width
    rowformat = ' '.join(['{{:{:d}}}'.format(w) for w in colwidths])

    rows = list()
    rows.append(separator_line)
    rows.append(rowformat.format(*table.colnames).strip())
    rows.append(separator_line)
    for row in table:
        rows.append(rowformat.format(*row).strip())
    rows.append(separator_line)

    return rows


def update(lines, force=False):
    """Update units and descriptions for data tables in datamodel lines

    Args:
        lines (list of str): lines read from an input datamodel file

    Options:
        force (bool): if True, update non-blank input entries too

    Returns: list of str lines with updates units and descriptions

    This function is separated from `main` primarily to facilitate testing
    of updating input lines into output lines without having to actually
    read and write files every time.
    """
    log = get_logger()

    coldef_file = resource_filename('desidatamodel', 'data/column_descriptions.csv')
    coldefs = read_column_descriptions(coldef_file)

    output_lines = list()

    # Strip trailing whitespace (including newline)
    lines = [x.rstrip() for x in lines]

    # Iterate over input lines looking for data tables
    i = 0
    while i < len(lines):
        if re.match('(=+) (=+) (=+) (=+)', lines[i]):
            rows = read_table_rows(lines, i)

            # if it wasn't a Name Type Units Description table, continue
            if rows is None:
                output_lines.append(lines[i])
                i += 1
                continue

            # We have a table, update units and descriptions
            for j in range(len(rows)):
                # get just the first word of the Name column to avoid
                # possible footnotes marking them as optional
                name = rows[j]['Name'].split()[0]

                if name in coldefs:
                    # standard Units and Descriptions for this Name
                    units = escape(coldefs[name]['Units']).strip()
                    description = escape(coldefs[name]['Description']).strip()

                    # updating a blank entry = info
                    # changing a pre-existing entry = warning
                    current_units = rows[j]['Units']
                    if current_units != units:
                        if current_units == '' or force:
                            rows[j]['Units'] = units

                        if current_units == '':
                            log.info(f'Adding {name} Units "{units}"')
                        elif force:
                            log.warning(f'Updating {name} Units from "{current_units}" to "{units}"')
                        else:
                            log.warning(f'{name} Units differ but not updating; "{current_units}" vs. "{units}"')

                    current_desc = rows[j]['Description']
                    if current_desc != description:
                        if current_desc == '' or force:
                            rows[j]['Description'] = description

                        if current_desc == '':
                            log.info(f'Adding {name} Description "{description}"')
                        elif force:
                            log.warning(f'Updating {name} Description from "{current_desc}" to "{description}"')
                        else:
                            log.warning(f'{name} Descriptions differ but not updating; "{current_desc}" vs. "{description}"')

            # convert to table, then undo masking of blank strings
            table = Table(rows, names=['Name', 'Type', 'Units', 'Description'])
            for colname in table.colnames:
                try:
                    table[colname].mask = np.zeros(len(table), dtype=bool)
                except AttributeError:
                    pass  # column not masked

            for line in format_rst_table(table):
                output_lines.append(line)

            # skip forward by length of table
            # 3 header lines, 1 footer line, plus actual table length
            i += 4 + len(table)

        # end of processing a table block; just output whatever line this was
        else:
            output_lines.append(lines[i])
            i += 1

    return output_lines


def main():
    """Updates a datamodel file with standard units and descriptions

    Returns
    -------
    :class:`int`
        An integer suitable for passing to :func:`sys.exit`.
    """

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--infile', required=True,
                        help='Input model filename')
    parser.add_argument('-o', '--outfile',
                        help='Output model filename')
    parser.add_argument('--inplace', action='store_true',
                        help="Update input file inplace, equivalent to specifying "
                             "--outfile with same name as --infile")
    parser.add_argument('--force', action='store_true',
                        help="Update non-blank pre-existing entries that differ from "
                             "reference units and descriptions")
    args = parser.parse_args()

    log = get_logger()

    if args.inplace:
        if args.outfile is not None:
            raise ValueError("When using --inplace, don't specify --outfile")
        args.outfile = args.infile
    elif args.outfile is None:
        log.info('Neither --inplace nor --outfile specified; will print changes but not write output')

    # Read input data model file
    with open(args.infile) as fp:
        input_lines = fp.readlines()

    output_lines = update(input_lines, force=args.force)

    if args.outfile is not None:
        with open(args.outfile, 'w') as fp:
            for line in output_lines:
                fp.write(line+'\n')
    return 0
