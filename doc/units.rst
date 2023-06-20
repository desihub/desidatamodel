===================
Units in Data Files
===================

In the DESI data model, wherever possible we describe the units carried by
values in the data files being described. In some cases the values are actually
dimensionless, or a simple quantity such as wavelength (``Angstrom``). In
other cases the units are more complex such as spectral flux density
(``10^-17 erg cm^-2 s^-1 Angstrom^-1``).

The majority of the files in the DESI data set are `FITS files`_.  The
FITS standard supports header keywords that describe the units of the
values stored in each HDU. A ``BUNIT`` keyword describes the units for an
image HDU, while ``TUNITn`` keywords describe the units of column ``n`` in
a table HDU.  In the DESI data model, we specify units that follow FITS
standards as closely as possible. See Section 4.3 of the
`FITS Standard (Version 4.0)`_ for more details.

However, even though units are described in this data model, it is not always
the case that units are specified in the FITS files themselves. In other words,
``BUNIT`` or ``TUNITn`` header keywords are not always present.
If you routinely read FITS files with QTable_, for example, the described units
might not appear automatically.


.. _`FITS files`: https://fits.gsfc.nasa.gov
.. _`FITS Standard (Version 4.0)`: https://fits.gsfc.nasa.gov/standard40/fits_standard40aa-le.pdf
.. _`QTable`: https://docs.astropy.org/en/stable/api/astropy.table.QTable.html#astropy.table.QTable
