============
fiberpos-all
============

:Summary: A mapping of positioner number to fiber number, including
    positions from DESI-0530.
    An ECSV_ version of this file might also be present.
:Naming Convention: ``fiberpos-all.fits``
:Regex: ``fiberpos-all\.fits``
:File Type: FITS, 472 KB

.. _ECSV: https://github.com/astropy/astropy-APEs/blob/master/APE6.rst

Contents
========

====== ======== ======== ==============================
Number EXTNAME  Type     Contents
====== ======== ======== ==============================
HDU0_  PRIMARY  IMAGE    Empty
HDU1_  FIBERPOS BINTABLE Fiber positions on focal plane
====== ======== ======== ==============================


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

Fiber positions on focal plane

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ============= ==== =====================
    KEY      Example Value Type Comment
    ======== ============= ==== =====================
    NAXIS1   87            int  length of dimension 1
    NAXIS2   5430          int  length of dimension 2
    ======== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

=========== ======= ===== ==========================
Name        Type    Units Description
=========== ======= ===== ==========================
PETAL       int32         TODO: description needed
DEVICE      int32         TODO: description needed
DEVICE_TYPE char[3]       TODO: description needed
LOCATION    int64         TODO: description needed
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
