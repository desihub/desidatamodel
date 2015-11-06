# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""
==================
desidatamodel.stub
==================

Generate data model files from FITS files.
"""
from __future__ import absolute_import, division, print_function, unicode_literals
# The line above will help with 2to3 support.
#
# This is a template.
#
rst = """{titlehighlight}
{title}
{titlehighlight}

General Description
===================

Summary
-------

*This section should be filled in with a high-level description of this file.
In general, you should remove or replace the emphasized text (\*this text
is emphasized\*) in this document.*

Naming Convention
-----------------

``{filename}``, where ...
*Give a human readable description of the filename, e.g.
``blat-{{EXPID}}`` where ``{{EXPID}}`` is the 8-digit exposure ID.*

regex: ``{filename}``
*Give a regular expression for this filename.
For example, a six-digit number would correspond to ``[0-9]{{6}}``.*

File Type
---------

{filetype}, {filesize}  *This section gives the type of the file and its approximate size.*

Contents
========

{contents_table}

FITS Header Units
=================

{hdu_sections}

Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*

"""
#
#
#
def binary_table_format(hdr):
    """Print format of binary table

    Parameters
    ----------
    hdr : astropy.io.fits.Header
        The header to parse.

    Returns
    -------
    binary_table_format : list
        A list of strings that can be appended to the main document.
    """
    from cgi import escape
    section = list()
    section.append('Required Data Table Columns')
    section.append('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    section.append('')
    columns_table =  [('Name','Type','Units','Description')]
    jformat = '{0:d}'
    for j in range(hdr['TFIELDS']):
        jj = jformat.format(j+1)
        name = hdr['TTYPE'+jj].strip()
        ttype = fits_column_format(hdr['TFORM'+jj].strip())
        tunit = 'TUNIT'+jj
        if tunit in hdr:
            units = hdr[tunit].strip()
        else:
            units = ''
        #- Check TCOMMnn keyword, otherwise use TTYPE comment for description
        commkey = 'TCOMM'+jj
        if commkey in hdr:
            description = escape(hdr[commkey].strip())
        else:
            description = escape(hdr.comments['TTYPE'+jj])
        columns_table.append((name,ttype,units,description))
    colsizes = [max(map(len,col)) for col in zip(*columns_table)]
    highlight = ' '.join(['='*k for k in colsizes])
    colformat = ' '.join(['{{{0:d}:{1:d}}}'.format(i,s) for i,s in enumerate(colsizes)])
    section.append(highlight)
    for k in range(len(columns_table)):
        section.append(colformat.format(*columns_table[k]).rstrip())
        if k == 0:
            section.append(highlight)
    section.append(highlight)
    section.append('')
    return section
#
#
#
def data_format(hdr):
    """Decide which kind of header this is, and print its data format

    Parameters
    ----------
    hdr : astropy.io.fits.Header
        The header to parse.

    Returns
    -------
    data_format : list
        A list of strings that can be appended to the main document.
    """
    section = list()
    if 'XTENSION' in hdr:
        if hdr['XTENSION'].strip() == 'BINTABLE':
            section += binary_table_format(hdr)
        elif hdr['XTENSION'].strip() == 'IMAGE':
            datatype = ''
            if 'BITPIX' in hdr:
                bitmap = {8:'char',16:'int16',32:'int32',64:'int64',-32:'float32',-64:'float64'}
                try:
                    datatype = bitmap[hdr['BITPIX']]
                except KeyError:
                    datatype = 'BITPIX={}'.format(hdr['BITPIX'])
            section.append('Data: FITS image [{0}]'.format(datatype))
            section.append('')
        else:
            section.append("Unknown extension type {0}".format(hdr['XTENSION']))
            section.append('')
    return section
#
#
#
def extrakey(key):
    """Return True if key is not a boring standard FITS keyword.

    To make the data model more human readable, we don't overwhelm the output
    with required keywords which are required by the FITS standard anyway.
    This list isn't exhaustive.

    Parameters
    ----------
    key : str
        A FITS keyword.

    Returns
    -------
    extrakey : bool
        ``True`` if the keyword is not boring.

    Examples
    --------
    >>> extrakey('SIMPLE')
    False
    >>> extrakey('BZERO')
    True
    """
    from re import match
    if match(r'TTYPE\d+', key) is not None:
        return False
    if match(r'TFORM\d+', key) is not None:
        return False
    if match(r'TUNIT\d+', key) is not None:
        return False
    if match(r'TCOMM\d+', key) is not None:
        return False
    if match(r'TDIM\d+', key) is not None:
        return False
    #- don't drop NAXIS1 and NAXIS2 since we want to document which is which
    if key in ('BITPIX', 'NAXIS', 'PCOUNT', 'GCOUNT',
        'TFIELDS', 'XTENSION', 'SIMPLE', 'EXTEND', 'COMMENT', 'HISTORY'):
        return False
    return True
#
#- Adapted from stackoverflow answers for human readable size formatting
#
def file_size(filename):
    """Determine file size and return string with human readable size format.

    Parameters
    ----------
    filename : str
        A string containing a filename.

    Returns
    -------
    file_size : str
        A human-readable file size.

    Examples
    --------
    >>> file_size('one-gb-file.dat')
    '1 GB'
    """
    from os.path import getsize
    n = getsize(filename)
    for unit in ['bytes','KB','MB','GB']:
        if n < 1024:
            return "{0:d} {1}".format(int(n), unit)
        else:
            n /= 1024.0
    return "{0:3.1f} {1}".format(n, 'TB')
#
#
#
def fits_column_format(format):
    """Convert a FITS column format to a human-readable form.

    Parameters
    ----------
    format : str
        A FITS-style format string.

    Returns
    -------
    fits_column_format : str
        A human-readable version of the format string.

    Examples
    --------
    >>> fits_column_format('A')
    'char[1]'
    >>> fits_column_format('J')
    'int32'
    >>> fits_column_format('12E')
    'float32[12]'
    """
    if format.startswith('1P'):
        cmap = {'B':'8-bit stream','I':'16-bit stream','J':'32-bit stream'}
        return cmap[format[2]]
    fitstype=format[-1]
    if fitstype == 'A' and len(format) == 1:
        return 'char[1]'
    fmap = {'A':'char','I':'int16','J':'int32','K':'int64',
            'E':'float32','D':'float64', 'B':'binary', 'L':'logical'}
    if len(format) > 1:
        return fmap[fitstype] + '[' + format[0:len(format)-1] + ']'
    else:
        return fmap[fitstype]
#
#
#
def parse_header(hdr):
    """Create a table of header keywords, omitting those required by FITS anyway.

    Parameters
    ----------
    hdr : astropy.io.fits.Header
        The header to parse.

    Returns
    -------
    parse_header : list
        A list of strings that can be appended to the main document.
    """
    from sys import version_info
    from cgi import escape
    section = list()
    keywords = list()
    if version_info.major == 3:
        str_types = (str,)
    else:
        str_types = (str,unicode)
    for key in hdr:
        if extrakey(key):
            #- Escape &, <, >, in strings, but don't choke on int/float
            value = hdr[key]
            if isinstance(value, bool):
                ktype = 'bool'
                value = ('F','T')[int(value)]
            if isinstance(value, str_types):
                value = escape(value)
                if value == 'T' or value == 'F':
                    ktype = 'bool'
                else:
                    ktype = 'str'
            if isinstance(value, int):
                value = str(value)
                ktype = 'int'
            if isinstance(value, float):
                value = str(value)
                ktype = 'float'
            if key.endswith('_'):
                key = key[0:len(key)-1] + '\\_'
            if value.endswith('_'):
                value = value[0:len(value)-1] + '\\_'
            keywords.append(dict(KEY=key, Value=value, Type=ktype,
                Comment=escape(hdr.comments[key])) )
    if len(keywords) == 0:
        section.append('This HDU has no non-standard required keywords.')
        section.append('')
    else:
        section.append('Required Header Keywords')
        section.append('~~~~~~~~~~~~~~~~~~~~~~~~')
        section.append('')
        keywords_table =  [('KEY','Example Value','Type','Comment')]
        for kw in keywords:
            keywords_table.append((kw['KEY'],kw['Value'],kw['Type'],kw['Comment']))
        colsizes = [max(map(len,col)) for col in zip(*keywords_table)]
        highlight = ' '.join(['='*k for k in colsizes])
        colformat = ' '.join(['{{{0:d}:{1:d}}}'.format(i,s) for i,s in enumerate(colsizes)])
        section.append(highlight)
        for k in range(len(keywords_table)):
            section.append(colformat.format(*keywords_table[k]).rstrip())
            if k == 0:
                section.append(highlight)
        section.append(highlight)
        section.append('')
    #
    # Analyze any tables that might be present.
    #
    section += data_format(hdr)
    return section
#
#
#
def process_file(filename):
    """Process a single FITS file.

    Parameters
    ----------
    filename : str
        Name of a FITS file.

    Returns
    -------
    process_file : tuple
        A tuple containing the name of the model file and the data to write to it.
    """
    import re
    from astropy.io import fits
    from os.path import basename
    rstkeywords = dict()
    #
    # Create a title
    #
    basef = basename(filename)
    try:
        modelname = basef[0:basef.index('-')]
    except ValueError:
        modelname = basef[0:basef.index('.')]
    rstkeywords['title'] = modelname
    rstkeywords['titlehighlight'] = '='*len(rstkeywords['title'])
    rstkeywords['filename'] = basef
    rstkeywords['filetype'] = 'FITS'
    rstkeywords['filesize'] = file_size(filename)
    #
    #- Read the file and parse the headers
    #
    with fits.open(filename) as fx:
        nhdr = len(fx)
        if nhdr > 99:
            hduname = 'HDU{0:03d}'
        elif nhdr > 9:
            hduname = 'HDU{0:02d}'
        else:
            hduname = 'HDU{0:1d}'
        contents_table = [('Number','EXTNAME','Type','Contents')]
        headers = list()
        hdu_sections = list()
        for k in range(nhdr):
            headers.append(fx[k].header)
            if k > 0 and 'EXTNAME' in headers[k]:
                extname = headers[k]['EXTNAME'].strip()
            else:
                extname = ''
            if k > 0:
                exttype = headers[k]['XTENSION'].strip()
            else:
                exttype = 'IMAGE'
            contents_table.append((hduname.format(k)+'_',extname,exttype,'*Brief Description*'))
            sec_title = hduname.format(k)
            hdu_sections.append(sec_title)
            hdu_sections.append('-'*len(sec_title))
            hdu_sections.append('')
            if extname != '':
                hdu_sections.append('EXTNAME = '+extname)
                hdu_sections.append('')
            hdu_sections.append('*Summarize the contents of this HDU.*')
            hdu_sections.append('')
            hdu_sections += parse_header(headers[k])
    #
    # Construct the contents table.
    #
    colsizes = [max(map(len,col)) for col in zip(*contents_table)]
    highlight = ' '.join(['='*k for k in colsizes])+"\n"
    colformat = ' '.join(['{{{0:d}:{1:d}}}'.format(i,s) for i,s in enumerate(colsizes)])+"\n"
    rstkeywords['contents_table'] = highlight
    for k in range(nhdr+1):
        rstkeywords['contents_table'] += colformat.format(*contents_table[k])
        if k == 0:
            rstkeywords['contents_table'] += highlight
    rstkeywords['contents_table'] += highlight
    rstkeywords['hdu_sections'] = '\n'.join(hdu_sections)
    return (modelname, rst.format(**rstkeywords))
#
#
#
#
def main():
    """Entry point for the generate_model script.

    Parameters
    ----------
    None

    Returns
    -------
    main : int
        An integer suitable for passing to ``sys.exit()``.
    """
    from os.path import basename
    from sys import argv, stderr
    from argparse import ArgumentParser
    try:
        from astropy.io import fits
    except ImportError:
        print("This script requires astropy.io.fits, available in your favourite Python distribution.",file=stderr)
        return 1
    desc = """Generate an DESI data model stub for a given FITS file.

    You will still need to hand edit the file to add descriptions, etc., but
    it gives you a good starting point in the correct format.
    """
    parser = ArgumentParser(description=desc,prog=basename(argv[0]))
    parser.add_argument('filename',help='A FITS file.',metavar='FILE',nargs='+')
    options = parser.parse_args()
    for f in options.filename:
        modelname, data = process_file(f)
        #
        # Write the file
        #
        with open("{0}.rst".format(modelname),'w') as m:
            m.write(data)
    return 0
