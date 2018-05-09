=====================
desi-tiles-randomized
=====================

:Summary: A randomized version of the desi-tiles file. ECSV_
          and PAR_ versions of this file might also be present.
:Naming Convention: ``desi-tiles-randomized.fits``
:Regex: ``desi-tiles-randomized\.fits``
:File Type: FITS, 3 MB

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

Tile centers with randomized offsets to wash out large scale patterns from
regular overlaps.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =======================
KEY    Example Value Type Comment
====== ============= ==== =======================
NAXIS1 36            int  Number of bytes per row
NAXIS2 115240        int  Number of rows
====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

========= ======= ===== ===========
Name      Type    Units Description
========= ======= ===== ===========
TILEID    int32
RA        float64 deg
DEC       float64 deg
PASS      int16
IN_DESI   int16
EBV_MED   float32
AIRMASS   float32
EXPOSEFAC float32
========= ======= ===== ===========


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
