============
fiberpos-all
============

:Summary: A mapping of positioner number to fiber number. An ECSV_
          version of this file might also be present.
:Naming Convention: ``fiberpos-all.fits``
:Regex: ``fiberpos-all\.fits``
:File Type: FITS, 472 KB

.. _ECSV: https://github.com/astropy/astropy-APEs/blob/master/APE6.rst

Contents
========

====== ======== ======== ===================
Number EXTNAME  Type     Contents
====== ======== ======== ===================
HDU0_  PRIMARY  IMAGE    *Brief Description*
HDU1_  FIBERPOS BINTABLE *Brief Description*
====== ======== ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

*Summarize the contents of this HDU.*

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = FIBERPOS

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============= ==== =====================
KEY      Example Value Type Comment
======== ============= ==== =====================
NAXIS1   87            int  length of dimension 1
NAXIS2   5430          int  length of dimension 2
======== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=========== ======= ===== ===========
Name        Type    Units Description
=========== ======= ===== ===========
PETAL       int32
DEVICE      int32
DEVICE_TYPE char[3]
LOCATION    int64
FIBER       int32
X           float64 mm
Y           float64 mm
Z           float64 mm
Q           float64 deg
S           float64 mm
SPECTRO     int32
SLIT        int32
SLITBLOCK   int64
BLOCKFIBER  int64
=========== ======= ===== ===========


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
