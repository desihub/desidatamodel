==========
desi-tiles
==========

:Summary: The DESI footprint, described in terms of tiles.  ECSV_
          and PAR_ versions of this file might also be present.
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
HDU0_          IMAGE    Empty Header
HDU1_          BINTABLE Tile data
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

*Summarize the contents of this HDU.*

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =====================
KEY    Example Value Type Comment
====== ============= ==== =====================
NAXIS1 50            int  length of dimension 1
NAXIS2 57620         int  length of dimension 2
====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

============= ======= ===== ===========
Name          Type    Units Description
============= ======= ===== ===========
TILEID        int32
RA            float64 deg
DEC           float64 deg
PASS          int16
IN_DESI       int16
EBV_MED       float32
AIRMASS       float32
STAR_DENSITY  float32
EXPOSEFAC     float32
PROGRAM       char[6]
OBSCONDITIONS int32
============= ======= ===== ===========


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
