========
fiberpos
========

:Summary: A random mapping of positioner number to fiber number.
:Naming Convention: ``fiberpos.fits``
:Regex: ``fiberpos\.fits``
:File Type: FITS, 241 KB

Contents
========

====== ======== ======== ===================
Number EXTNAME  Type     Contents
====== ======== ======== ===================
HDU0_           IMAGE    Empty
HDU1_  FIBERPOS BINTABLE Map of positioner to fiber.
====== ======== ======== ===================


FITS Header Units
=================

HDU0
----

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = FIBERPOS

Map of positioner to fiber.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ============= ==== ===================================
KEY     Example Value Type Comment
======= ============= ==== ===================================
NAXIS1  48            int  width of table in bytes
NAXIS2  5000          int  number of rows in table
EXTNAME FIBERPOS      str  name of this binary table extension
======= ============= ==== ===================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

============ ======= ===== ==========================
Name         Type    Units Description
============ ======= ===== ==========================
fiber        int64         fiber number [0-4999]
positioner   int64         positioner number [0-4999]
spectrograph int64         spectrograph number [0-9]
x            float64       positioner x center [mm]
y            float64       positioner y center [mm]
z            float64       positioner z location [mm]
============ ======= ===== ==========================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
