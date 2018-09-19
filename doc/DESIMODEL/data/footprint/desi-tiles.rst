==========
desi-tiles
==========

:Summary: The DESI footprint, described in terms of tiles.  ECSV_
          versions of this file might also be present, lacking
          vector-valued columns (BRIGHT*).
:Naming Convention: ``desi-tiles.fits``
:Regex: ``desi-tiles\.fits``
:File Type: FITS, 2 MB

.. _ECSV: https://github.com/astropy/astropy-APEs/blob/master/APE6.rst
.. _PAR: http://www.sdss.org/dr13/software/par/

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_  PRIMARY IMAGE    Empty Header
HDU1_  TILES   BINTABLE Tile data
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = TILES

Pre-defined DESI tile locations on the sky (i.e. telescope pointings)

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =====================
KEY    Example Value Type Comment
====== ============= ==== =====================
NAXIS1 114           int  length of dimension 1
NAXIS2 57620         int  length of dimension 2
====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

============= ========== ======= ===========
Name          Type       Units   Description
============= ========== ======= ===========
tileid        int32              Unique tile ID
ra            float64    deg     Right ascension
dec           float64    deg     Declination
pass          int16              DESI layer
in_desi       int16              1=within DESI footprint; 0=outside'
ebv_med       float32    mag     Median Galactic E(B-V) extinction in tile
airmass       float32            Airmass if observed at hour angle 15 deg
star_density  float32    deg^-2  Median number density of Gaia stars brighter than 19.5 mag in tile
exposefac     float32            Multiplicative exposure time factor from airmass and E(B-V)
program       char[6]            DARK, GRAY, BRIGHT, or EXTRA
obsconditions int32              1 for DARK, 2 for GRAY, 4 for BRIGHT, 0 for EXTRA
brightra      float64[3] deg     RAs of 3 brightest Tycho-2 stars in tile
brightdec     float64[3] deg     Decs of 3 brightest Tycho-2 stars in tile
brightvtmag   float32[3] mag     V_T magnitudes of 3 brightest Tycho-2 stars in tile
centerid      int32              Unique tile ID of pass 0 tile corresponding to this tile
============= ========== ======= ===========


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
