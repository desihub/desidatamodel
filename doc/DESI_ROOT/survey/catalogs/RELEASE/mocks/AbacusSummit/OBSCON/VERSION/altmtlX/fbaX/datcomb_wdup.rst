=========================
datcomb OBSCON wdup files
=========================

:Summary: Match of targets (with duplicate TARGETID corresponding to each potential assignment) with mock data. Both for potential assigments and actual assigments.
:Naming Convention: ``datcomb_{OBSCON}{assign}wdup.fits``, where ``{OBSCON}`` is either dark or bright and ``{assign}`` is optional, depending if it is potential assigments or actual observed assigments.
:Regex: ``datcomb_(dark|bright)(assign|)wdup\.fits``
:File Type: FITS, 2 GB



Contents
========

====== ======== ======== ===================
Number EXTNAME  Type     Contents
====== ======== ======== ===================
HDU0_           IMAGE    Empty
HDU1_  LSS      BINTABLE Catalog data
====== ======== ======== ===================


FITS Header Units
=================

HDU0
----

Empty HDU.

HDU1
----

EXTNAME = LSS

Match of targets (with duplicate TARGETID corresponding to each potential assignment or actual observed assigment) with mock data from the forFA files.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ============= ==== =====================
    KEY      Example Value Type Comment
    ======== ============= ==== =====================
    NAXIS1   463           int  length of dimension 1
    NAXIS2   13947971      int  length of dimension 2
    DESIDR   dr1           str  DESI Data Release
    ======== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

================== ======= ===== ===============================================================================================================================
Name               Type    Units Description
================== ======= ===== ===============================================================================================================================
TARGETID           int64         Unique DESI target ID
LOCATION           int32         Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
TILEID             int64         Unique DESI tile ID
PRIORITY [1]_      int32         Target current priority
SUBPRIORITY [1]_   float64       Random subpriority [0-1) to break assignment ties
TRUEZ [1]_         float32       True redshift in a galaxy mock catalog
RSDZ [1]_          float32       Redshift in mocks that includes RSD effects
ZWARN [1]_         int64         Redshift warning bitmask from Redrock
FIBER [1]_         int32         Fiber ID on the CCDs [0-4999]
RA [1]_            float64 deg   Barycentric Right Ascension in ICRS. Note that RA for dark tracer is type = float32
DEC [1]_           float64 deg   Barycentric declination in ICRS. Note that DEC for dark tracer is type = float32
PRIORITY_INIT [1]_ int64         Target initial priority from target selection bitmasks and OBSCONDITIONS
DESI_TARGET [1]_   int64         DESI (dark time program) target selection bitmask
R_MAG_ABS [1]_     float32       Absolute magnitude in R band in mocks
BGS_TARGET [1]_    int64         BGS (Bright Galaxy Survey) target selection bitmask
================== ======= ===== ===============================================================================================================================

.. [1] Optional

Notes and Examples
==================

Optional columns:

* ``PRIORITY``, ``SUBPRIORITY``, ``TRUEZ``, ``RSDZ``, ``ZWARN`` : Present in assign file
* ``FIBER``, ``RA``, ``DEC``, ``PRIORITY_INIT``, ``DESI_TARGET`` : Present in wdup potential file, both for dark and bright
* ``BGS_TARGET``, ``R_MAG_ABS`` : Only present in bright wdup potential file

.. warning::

        For OBSCON = dark, dtypes of RA,DEC is float32, instead of float64
