# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""
=====================
desidatamodel.columns
=====================

Render the standard column descriptions file.
"""
import csv
import sys
import importlib.resources as ir
import jinja2


def format_columns(rows):
    """Does something.

    Parameters
    ----------
    rows : iterable
        An iterable containing rows with any number of columns.

    Returns
    -------
    :class:`tuple`
        A tuple containing a format string, and an RST-style table separator.
    """
    lengths = list()
    for row in rows:
        for k, col in enumerate(row):
            try:
                if len(col) > lengths[k]:
                    lengths[k] = len(col)
            except IndexError:
                lengths.append(len(col))
    format_string = " ".join(["{{{0}:{1}}}".format(k, c) for k, c in enumerate(lengths)])
    separator = ' '.join(['='*k for k in lengths])
    return (format_string, separator)


def main():
    """Entry point for command-line scripts.

    Returns
    -------
    :class:`int`
        An integer suitable for passing to :func:`sys.exit`.
    """
    env = jinja2.Environment(loader=jinja2.PackageLoader('desidatamodel', package_path='data'),
                             trim_blocks=True)
    template = env.get_template('column_descriptions.rst')
    columns = ir.files('desidatamodel') / 'data' / 'column_descriptions.csv'
    with open(columns, newline='') as cf:
        reader = csv.reader(cf)
        format_string, separator = format_columns(reader)
        cf.seek(0)
        print(template.render(reader=reader, format_string=format_string, separator=separator))
    return 0


if __name__ == '__main__':  # pragma: no cover
    sys.exit(main())
