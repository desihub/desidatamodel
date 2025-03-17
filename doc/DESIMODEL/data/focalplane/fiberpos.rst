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
HDU0_  PRIMARY  IMAGE    Empty
HDU1_  FIBERPOS BINTABLE Map of positioner to fiber.
====== ======== ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = FIBERPOS

Map of positioner to fiber.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords


    ======= ============= ==== ===================================
    KEY     Example Value Type Comment
    ======= ============= ==== ===================================
    NAXIS1  87            int  width of table in bytes
    NAXIS2  5000          int  number of rows in table
    EXTNAME FIBERPOS      str  name of this binary table extension
    ======= ============= ==== ===================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

=========== ======= ===== ==========================
Name        Type    Units Description
=========== ======= ===== ==========================
PETAL       int32         Petal location [0-9]
DEVICE      int32         Device location on focal plane [0-523]
DEVICE_TYPE char[3]       Device type
LOCATION    int64         Location on the focal plane PETAL*1000 + DEVICE
FIBER       int32         fiber number [0-4999]
X           float64 mm    positioner x center [mm]
Y           float64 mm    positioner y center [mm]
Z           float64 mm    positioner z location [mm]
Q           float64 deg   TODO: description needed
S           float64 mm    TODO: description needed
SPECTRO     int32         spectrograph number [0-9]
SLIT        int32         TODO: description needed
SLITBLOCK   int64         TODO: description needed
BLOCKFIBER  int64         TODO: description needed
=========== ======= ===== ==========================
