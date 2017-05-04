========
fiberpos
========

:Summary: A random mapping of positioner number to fiber number. ECSV_
          and plain text versions of this file might also be present.
:Naming Convention: ``fiberpos.fits``
:Regex: ``fiberpos\.fits``
:File Type: FITS, 440 KB

.. _ECSV: https://github.com/astropy/astropy-APEs/blob/master/APE6.rst

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
NAXIS1  87            int  width of table in bytes
NAXIS2  5000          int  number of rows in table
EXTNAME FIBERPOS      str  name of this binary table extension
======= ============= ==== ===================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=========== ======= ===== ==========================
Name        Type    Units Description
=========== ======= ===== ==========================
PETAL       int32
DEVICE      int32
DEVICE_TYPE char[3]
LOCATION    int64
FIBER       int32         fiber number [0-4999]
X           float64 mm    positioner x center [mm]
Y           float64 mm    positioner y center [mm]
Z           float64 mm    positioner z location [mm]
Q           float64 deg
S           float64 mm
SPECTRO     int32         spectrograph number [0-9]
SLIT        int32
SLITBLOCK   int64
BLOCKFIBER  int64
=========== ======= ===== ==========================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
