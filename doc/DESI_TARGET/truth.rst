==========
truth.fits
==========

General Description
===================

:Summary: DESI Truth files contain a single binary table covering the entire footprint.
    They contain the variables that define the procedence of a target and its
    true properties. This file goes together with a mock target catalog.
:Naming Convention: TBD, let's try ``truth-{version}.fits`` where ``version`` is the code version
    that wrote this, preferably a git tag of desitargets.
:Regex: ``truth-v?[0-9]+\.[0-9]+(\.[0-9]+|)\.fits``
:File Type: FITS, 28 MB

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_  PRIMARY IMAGE    Blank
HDU1_  TRUTH   BINTABLE Truth table
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

EXTNAME = TRUTH

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============= ==== ===================================
KEY      Example Value Type Comment
======== ============= ==== ===================================
NAXIS1   118           int  width of table in bytes
NAXIS2   241273        int  number of rows in table
======== ============= ==== ===================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ======== ===== ===================
Name            Type     Units Description
=============== ======== ===== ===================
TARGETID        int64          ID (unique to file and the whole survey)
MOCKID          int64          Mock ID
CONTAM_TARGET   int64
TRUEZ           float64        True redshift in mock catalog (including peculiar velocity)
TRUESPECTYPE    char[10]       True object type in mock catalog
TEMPLATETYPE    char[10]
TEMPLATESUBTYPE char[10]
TEMPLATEID      int32
SEED            int64
MAG             float32
VDISP           float32        Velocity dispersion
FLUX_G          float32        DECaLS flux from tractor input (g)
FLUX_R          float32        DECaLS flux from tractor input (r)
FLUX_Z          float32        DECaLS flux from tractor input (z)
FLUX_W1         float32        WISE flux in W1
FLUX_W2         float32        WISE flux in W2
OIIFLUX         float32        Flux in OII line
HBETAFLUX       float32        Flux in Hbeta line
TEFF            float32        Effective Temperature
LOGG            float32        Surface Gravity
FEH             float32        Metallicity
=============== ======== ===== ===================


Notes and Examples
==================

In general, the above format contains:

* Columns needed for traceability (e.g. TARGETID, BRICKNAME)
* Columns needed by fiber assignment (e.g. RA, DEC)
* Columns mimicking results from the spectroscopic pipeline (e.g. TRUEZ, TRUETYPE)

This file is created by the targets.mock submodule.
