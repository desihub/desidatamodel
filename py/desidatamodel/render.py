# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""
====================
desidatamodel.render
====================

Render the column descriptions file.
"""
import csv
import importlib.resources as ir
import jinja2


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
    separator_data = list()
    with open(columns, newline='') as cf:
        reader = csv.reader(cf)
        for row in reader:
            for k, col in enumerate(row):
                try:
                    if len(col) > separator_data[k]:
                        separator_data[k] = len(col)
                except IndexError:
                    separator_data.append(len(col))
        cf.seek(0)
        format_string = " ".join(["{{{0}:{1}}}".format(k, c) for k, c in enumerate(separator_data)])
        # print(format_string)
        separator = ' '.join(['='*k for k in separator_data])
        print(template.render(reader=reader, format_string=format_string, separator=separator))
    return 0


if __name__ == '__main__':
    main()
