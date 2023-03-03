# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""
==================
desidatamodel.stub
==================

Generate data model files from FITS files.
"""
import os
import re
from html import escape
from astropy.io import fits
from astropy.io.fits.card import Undefined

from desiutil.log import log, DEBUG

from . import DataModelError
from .unit import DataModelUnit
#
# This is a template.
#
rst = """{titlehighlight}
{title}
{titlehighlight}

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\\*this text is emphasized\\*) in this document.*
:Naming Convention: ``{filename}``, where ... *Give a human readable
    description of the filename, e.g. ``blat-{{EXPID}}`` where ``{{EXPID}}``
    is the 8-digit exposure ID.*
:Regex: ``{filename}`` *Give a regular expression for this filename.
    For example, a six-digit number would correspond to ``[0-9]{{6}}``.*
:File Type: {filetype}, {filesize}  *This section gives the type of the file
    and its approximate size.*

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


class Stub(DataModelUnit):
    """This object contains metadata about a file and methods to print that
    metadata.

    Parameters
    ----------
    filename : file path, file-like object or :class:`~astropy.io.fits.HDUList`
        Data file to convert to a data model file.
    error : :class:`bool`, optional
        If ``True``, failure to extract certain required metadata raises an
        exception.

    Attributes
    ----------
    columns_header : :func:`tuple`
        The header of a table summarizing the columns of a BINTABLE HDU.
    contents_header : :func:`tuple`
        The header of a table summarizing the HDUs.
    filename : :class:`str`
        Name of the file.
    headers : :class:`list`
        The HDUs read from the file.
    keywords_header : :func:`tuple`
        The header of a table listing interesting FITS keywords.
    nhdr : :class:`int`
        Number of HDUs.
    """
    contents_header = ('Number', 'EXTNAME', 'Type', 'Contents')
    keywords_header = ('KEY', 'Example Value', 'Type', 'Comment')
    columns_header = ('Name', 'Type', 'Units', 'Description')

    def __init__(self, filename, description_file=None, error=False):
        self.filename = None
        self.error = error
        self.headers = list()
        self.description_file = description_file
        if isinstance(filename, (list, fits.HDUList)):
            self.nhdr = len(filename)
            for k in range(self.nhdr):
                self.headers.append(filename[k].header)
        else:
            with fits.open(filename, disable_image_compression=True) as fx:
                self.nhdr = len(fx)
                for k in range(self.nhdr):
                    self.headers.append(fx[k].header)
            if isinstance(filename, (str,)):
                self.filename = filename
        self._basef = None
        self._modelname = None
        self._filesize = None
        self._filetype = None
        self._hdumeta = None
        self._hduname = None
        self._contents = None
        return

    @property
    def basef(self):
        """Base name of the file.
        """
        if self._basef is None:
            self._basef = os.path.basename(self.filename)
        return self._basef

    @property
    def modelname(self):
        """Name to use for the data model file.
        """
        if self._modelname is None:
            try:
                self._modelname = self.basef[0:self.basef.index('-')]
            except ValueError:
                self._modelname = self.basef[0:self.basef.index('.')]
        return self._modelname

    @property
    def filetype(self):
        """Type of file. Assumes FITS (for now) unless overridden in a subclass.
        """
        if self._filetype is None:
            self._filetype = 'FITS'
        return self._filetype

    @property
    def filesize(self):
        """Size of the file in human-readable format.
        """
        if self._filesize is None:
            self._filesize = file_size(self.filename)
        return self._filesize

    @property
    def hdumeta(self):
        """Metadata associated with each HDU.
        """
        if self._hdumeta is None:
            self._hdumeta = list()
            for k in range(self.nhdr):
                meta = dict()
                meta['title'] = self.hduname.format(k)
                meta['extname'] = self.contents[k+1][1]
                meta['keywords'] = extract_keywords(self.headers[k])
                if 'XTENSION' in self.headers[k]:
                    meta['extension'] = self.headers[k]['XTENSION'].strip()
                    if meta['extension'] == 'IMAGE':
                        meta['format'] = self.image_format(self.headers[k])
                    elif meta['extension'] == 'BINTABLE':
                        try:
                            meta['format'] = self.columns(k, self.error)
                        except DataModelError:
                            meta['format'] = self.image_format(self.headers[k])
                            try:
                                meta['extension'] = self.headers[k]['ZTENSION'].strip()
                            except KeyError:
                                try:
                                    i = self.headers[k]['ZIMAGE']
                                    if i:
                                        meta['extension'] = 'IMAGE'
                                except KeyError:
                                    log.warning("Possible malformed compressed data in HDU %d of %s.",
                                                k, self.filename)
                    else:
                        w = ("Unknown extension type: " +
                             "{extension}.").format(**meta)
                        meta['format'] = w
                        log.warning(w)
                else:
                    meta['extension'] = 'IMAGE'
                    meta['format'] = self.image_format(self.headers[k])
                self._hdumeta.append(meta)
        return self._hdumeta

    @property
    def hduname(self):
        """Format of HDU names.
        """
        if self._hduname is None:
            if self.nhdr > 99:
                self._hduname = 'HDU{0:03d}'
            elif self.nhdr > 9:
                self._hduname = 'HDU{0:02d}'
            else:
                self._hduname = 'HDU{0:1d}'
        return self._hduname

    @property
    def contents(self):
        """A table summarizing the HDUs.
        """
        if self._contents is None:
            self._contents = list()
            self._contents.append(self.contents_header)
            for k in range(self.nhdr):
                if 'EXTNAME' in self.headers[k]:
                    extname = self.headers[k]['EXTNAME'].strip()
                else:
                    extname = ''
                    #
                    # Don't complain about missing EXTNAME on primary, empty HDUs.
                    # See https://github.com/desihub/desidatamodel/issues/69
                    #
                    if k > 0:
                        log.warning("HDU%d has no EXTNAME set!", k)
                if k > 0:
                    if 'ZTENSION' in self.headers[k]:
                        exttype = self.headers[k]['ZTENSION'].strip()
                    else:
                        exttype = self.headers[k]['XTENSION'].strip()
                else:
                    exttype = 'IMAGE'
                self._contents.append((self.hduname.format(k)+'_',
                                       extname, exttype,
                                       '*Brief Description*'))
        return self._contents

    def columns(self, hdu, error=False):
        """Describe the columns of a BINTABLE HDU.

        Parameters
        ----------
        hdu : :class:`int`
            The HDU number (zero-indexed).
        error : :class:`bool`, optional
            If ``True``, failure to extract certain required metadata raises an
            exception.

        Returns
        -------
        :class:`list`
            The rows of the table.

        Raises
        ------
        :exc:`~desidatamodel.DataModelError`
            If the BINTABLE is actually a compressed image.
        :exc:`ValueError`
            If `error` and a ``TUNIT`` value does not have FITS-standard
            units.
        """
        hdr = self.headers[hdu]
        if 'ZBITPIX' in hdr:
            raise DataModelError("HDU{0:d} is actually a compressed image!".format(hdu))
        ncol = hdr['TFIELDS']
        c = list()
        c.append(self.columns_header)
        if self.description_file is not None:
            print('You add a file with column descriptions and units, reading column description and units from here', self.description_file)
            desc_data = fits.open(self.description_file)[1].data

        for j in range(ncol):

            if self.description_file is not None:
                
                units = desc_data[(desc_data['NAME'] == name)]['UNIT'][0].strip()
                bad_unit = self.check_unit(units, error=error)
                    if bad_unit:
                        log.debug("Non-standard (but acceptable) unit %s detected for column %s in column description file",
                              bad_unit, self.filename)

            else:
                jj = '{0:d}'.format(j+1)
                name = hdr['TTYPE'+jj].strip()
                ttype = fits_column_format(hdr['TFORM'+jj].strip())
                tunit = 'TUNIT'+jj
                if tunit in hdr:
                    units = hdr[tunit].strip()
                    bad_unit = self.check_unit(units, error=error)
                    if bad_unit:
                        log.debug("Non-standard (but acceptable) unit %s detected for column %s in HDU %d of %s.",
                              bad_unit, j, hdu, self.filename)
                else:
                    units = ''

            if self.description_file is not None:
                description = escape(desc_data[(desc_data['NAME'] == name)]['DESC'][0])
            else:
                # Check TCOMMnn keyword, otherwise use TTYPE comment
                # for description.
                commkey = 'TCOMM'+jj
                if commkey in hdr:
                    description = escape(hdr[commkey].strip())
                else:
                    description = escape(hdr.comments['TTYPE'+jj])
            c.append((name, ttype, units, description))
        return c

    def keywords(self, hdu):
        """A table summarizing the interesting keywords in a particular HDU.

        Parameters
        ----------
        hdu : :class:`int`
            The HDU number (zero-indexed).

        Returns
        -------
        :class:`list`
            The rows of the table.
        """
        return [self.keywords_header] + self.hdumeta[hdu]['keywords']

    def colsizes(self, table):
        """Compute the size (number of characters) of each column in a table.

        Parameters
        ----------
        table : :class:`list`
            A list representing a table.

        Returns
        -------
        :class:`list`
            The size of each column in the table.
        """
        return [max(map(len, col)) for col in zip(*table)]

    def highlight(self, sizes):
        """Return reStructuredText-compatible table highlights.

        Parameters
        ----------
        sizes : :class:`list`
            The width of each column.

        Returns
        -------
        :class:`str`
            A highlight string.
        """
        return ' '.join(['='*k for k in sizes])

    def colformat(self, sizes):
        """Return a string ready to be formatted.

        Parameters
        ----------
        sizes : :class:`list`
            The width of each column.

        Returns
        -------
        :class:`str`
            A string with format characters.
        """
        return ' '.join(['{{{0:d}:{1:d}}}'.format(i, s)
                         for i, s in enumerate(sizes)])

    def format_table(self, table, indent=False):
        """Convert tabular data into reStructuredText-compatible string.

        This function assumes that `table` already has a header as the
        first row.

        Parameters
        ----------
        table : :class:`list`
            A data table.
        indent : :class:`bool`
            If ``True``, indent the table for compatibility with
            collapsible tables.

        Returns
        -------
        :class:`list`
            A list of strings that can be joined.
        """
        spaces = ''
        if indent:
            spaces = '    '
        sizes = self.colsizes(table)
        highlight = spaces + self.highlight(sizes)
        colformat = spaces + self.colformat(sizes)
        t = [highlight]
        for k in range(len(table)):
            t.append(colformat.format(*table[k]).rstrip())
            if k == 0:
                t.append(highlight)
        t.append(highlight)
        return t

    def section(self, hdu):
        """A string describing an HDU.

        Parameters
        ----------
        hdu : :class:`int`
            The HDU number (zero-indexed).

        Returns
        -------
        :class:`list`
            A list of strings that can be joined.
        """
        s = list()
        #
        # Section title & summary.
        #
        s.append(self.hdumeta[hdu]['title'])
        s.append('-'*len(self.hdumeta[hdu]['title']))
        s.append('')
        if self.hdumeta[hdu]['extname']:
            s.append('EXTNAME = {extname}'.format(**self.hdumeta[hdu]))
            s.append('')
        s.append('*Summarize the contents of this HDU.*')
        s.append('')
        #
        # Interesting keywords.
        #
        if len(self.hdumeta[hdu]['keywords']) > 0:
            s.append('Required Header Keywords')
            s.append('~~~~~~~~~~~~~~~~~~~~~~~~')
            s.append('')
            s.append('.. collapse:: Required Header Keywords Table')
            s.append('')
            s.append('    .. rst-class:: keywords')
            s.append('')
            s += self.format_table(self.keywords(hdu), indent=True)
        else:
            s.append('This HDU has no non-standard required keywords.')
        s.append('')
        #
        # Data payload
        #
        if self.hdumeta[hdu]['extension'] == 'BINTABLE':
            s.append('Required Data Table Columns')
            s.append('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            s.append('')
            s.append('.. rst-class:: columns')
            s.append('')
            s += self.format_table(self.hdumeta[hdu]['format'])
        else:
            s.append(self.hdumeta[hdu]['format'])
        s.append('')
        return s

    def __str__(self):
        kw = dict()
        kw['title'] = self.modelname
        kw['titlehighlight'] = '='*len(kw['title'])
        kw['filename'] = self.basef
        kw['filetype'] = self.filetype
        kw['filesize'] = self.filesize
        kw['contents_table'] = ("\n".join(self.format_table(self.contents)) +
                                "\n")
        hdu_sections = list()
        for k in range(self.nhdr):
            hdu_sections += self.section(k)
        kw['hdu_sections'] = "\n".join(hdu_sections)
        return rst.format(**kw)

    def image_format(self, hdr):
        """Obtain format of an image HDU.

        Parameters
        ----------
        hdr : :class:`~astropy.io.fits.Header`
            The header to parse.

        Returns
        -------
        :class:`str`
            A string describing the image format.

        Raises
        ------
        :exc:`~desidatamodel.DataModelError`
            If ``self.error`` is set a `BUNIT` header with units that do not
            follow the FITS standard is detected.
        """
        n = hdr['NAXIS']
        if n == 0:
            return 'Empty HDU.'
        bitmap = {8: 'char', 16: 'int16', 32: 'int32', 64: 'int64',
                  -32: 'float32', -64: 'float64'}
        if 'ZBITPIX' in hdr:
            n = hdr['ZNAXIS']
            dims = [str(hdr['ZNAXIS{0:d}'.format(k+1)]) for k in range(n)]
            try:
                datatype = bitmap[hdr['ZBITPIX']] + ' (compressed)'
            except KeyError:
                datatype = 'BITPIX={0} (compressed)'.format(hdr['ZBITPIX'])
        else:
            dims = [str(hdr['NAXIS{0:d}'.format(k+1)]) for k in range(n)]
            try:
                datatype = bitmap[hdr['BITPIX']]
            except KeyError:
                datatype = 'BITPIX={}'.format(hdr['BITPIX'])
        if 'BUNIT' in hdr:
            log.debug("BUNIT   = '%s'", hdr['BUNIT'])
            bad_unit = self.check_unit(hdr['BUNIT'], error=self.error)
            if bad_unit:
                log.debug("Non-standard (but acceptable) unit %s detected in %s.",
                          bad_unit, self.filename)
        return 'Data: FITS image [{0}, {1}]'.format(datatype, 'x'.join(dims))


def extrakey(key):
    """Return True if key is not a boring standard FITS keyword.

    To make the data model more human readable, we don't overwhelm the output
    with required keywords which are required by the FITS standard anyway, or
    cases where the number of headers might change over time.

    This list isn't exhaustive.

    Parameters
    ----------
    key : :class:`str`
        A FITS keyword.

    Returns
    -------
    :class:`bool`
        ``True`` if the keyword is not boring.

    Examples
    --------
    >>> extrakey('SIMPLE')
    False
    >>> extrakey('DEPNAM01')
    False
    >>> extrakey('BZERO')
    True
    """
    from re import match
    # don't drop NAXIS1 and NAXIS2 since we want to document which is which
    if key in ('BITPIX', 'NAXIS', 'PCOUNT', 'GCOUNT', 'TFIELDS', 'XTENSION',
               'SIMPLE', 'EXTEND', 'COMMENT', 'HISTORY', 'EXTNAME', ''):
        return False
    # Table-specific keywords
    if match(r'T(TYPE|FORM|UNIT|COMM|DIM|NULL)\d+', key) is not None:
        return False
    # Compression-specific keywords
    if match(r'Z(SIMPLE|IMAGE|TENSION|BITPIX|NAXIS|NAXIS1|NAXIS2|PCOUNT|GCOUNT|TILE1|TILE2|CMPTYPE|NAME1|VAL1|NAME2|VAL2|HECKSUM|DATASUM)', key) is not None:
        return False
    # Dependency list
    if match(r'DEP(NAM|VER)\d+', key) is not None:
        return False
    return True


def file_size(filename):
    """Determine file size and return string with human readable size format.

    Adapted from stackoverflow answers for human readable size formatting.

    Parameters
    ----------
    filename : :class:`str`
        A string containing a filename.

    Returns
    -------
    :class:`str`
        A human-readable file size.

    Examples
    --------
    >>> file_size('one-gb-file.dat')
    '1 GB'
    """
    n = os.path.getsize(filename)
    for unit in ['bytes', 'KB', 'MB', 'GB']:
        if n < 1024:
            return "{0:d} {1}".format(int(n), unit)
        else:
            n /= 1024.0
    return "{0:3.1f} {1}".format(n, 'TB')


def fits_column_format(format):
    """Convert a FITS column format to a human-readable form.

    Parameters
    ----------
    format : :class:`str`
        A FITS-style format string.

    Returns
    -------
    :class:`str`
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
    m = re.match(r'(0|1|)[PQ]([A-Z])\([0-9]+\)', format)
    if m is not None:
        t = m.groups()
        cmap = {'A': 'char stream',
                'B': '8-bit stream',
                'I': '16-bit stream',
                'J': '32-bit stream',
                'K': '64-bit stream'}
        return cmap[t[1]]
    fitstype = format[-1]
    if fitstype == 'A' and len(format) == 1:
        return 'char[1]'
    fmap = {'A': 'char', 'I': 'int16', 'J': 'int32', 'K': 'int64',
            'E': 'float32', 'D': 'float64', 'B': 'binary', 'L': 'logical'}
    if len(format) > 1:
        return fmap[fitstype] + '[' + format[0:len(format)-1] + ']'
    else:
        return fmap[fitstype]


def extract_keywords(hdr):
    """Extract interesting keywords from a FITS header.

    Parameters
    ----------
    hdr : :class:`~astropy.io.fits.Header`
        The header to parse.

    Returns
    -------
    :class:`list`
        A list of tuples containing the metadata of interesting keywords.
    """
    keywords = list()
    for key in hdr:
        if extrakey(key):
            # Escape &, <, >, in strings, but don't choke on int/float
            value = hdr[key]
            if isinstance(value, bool):
                ktype = 'bool'
                value = ('F', 'T')[int(value)]
            if isinstance(value, (str,)):
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
            if isinstance(value, (Undefined, type(None))):
                log.error("Empty header keyword %s detected! This violates the FITS standard!", key)
                value = 'None'
                ktype = 'Unknown'
            if key.endswith('_'):
                key = key[0:len(key)-1] + '\\_'
            try:
                if value.endswith('_'):
                    value = value[0:len(value)-1] + '\\_'
            except AttributeError:
                ktype = 'Unknown'
                log.warning("Raised AttributeError on %s = %s.", key, value)
            keywords.append((key, value, ktype, escape(hdr.comments[key])))
    return keywords


def main():
    """Entry point for the generate_model script.

    Returns
    -------
    :class:`int`
        An integer suitable for passing to :func:`sys.exit`.
    """
    from sys import argv
    from argparse import ArgumentParser
    try:
        from astropy.io import fits
    except ImportError:
        log.critical("This script requires astropy.io.fits, " +
                     "available in your " +
                     "favourite Python distribution.")
        return 1
    desc = """Generate an DESI data model stub for a given FITS file.

    You will still need to hand edit the file to add descriptions, etc., but
    it gives you a good starting point in the correct format.
    """
    parser = ArgumentParser(description=desc, prog=os.path.basename(argv[0]))
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true',
                        help='Set log level to DEBUG.')
    parser.add_argument('filename', help='A FITS file.', metavar='FILE',
                        nargs='+')
    parser.add_argument("--desc", help="A file with columns description. So far only fits files available. Must have at least columns name and desc", default=None)

    options = parser.parse_args()
    if options.verbose:
        log.setLevel(DEBUG)
    for f in options.filename:
        stub = Stub(f)
        data = str(stub)
        #
        # Write the file
        #
        with open("{0}.rst".format(stub.modelname), 'w') as m:
            m.write(data)
    return 0
