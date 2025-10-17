=====================================
COMBINED MOCK DATA AFTER REDSHIFT
=====================================

:Summary: Match of targets (with duplicate TARGETID corresponding to each potential assignment) with mock redshift data.
:Naming Convention: ``datcomb_{OBSCON}_tarspecwdup_zdone.fits``, where ``{OBSCON}`` is dark or bright
:Regex: ``datcomb_(dark|bright)_tarspecwdup_zdone\.fits``
:File Type: FITS, 6 GB

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

Match of targets (with duplicate TARGETID corresponding to each potential assignment) with spectroscopic data compiled with datcomb_obscon_spec. Unobserved potential assignments have the corresponding spectroscopic information set to null values.

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

=============== ======= ===== ========================================================================
Name            Type    Units Description
=============== ======= ===== ========================================================================
LOCATION        int32         Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBER           int32         Fiber ID on the CCDs [0-4999]
TARGETID        int64         Unique DESI target ID
TILEID          int64         Unique DESI tile ID
R_MAG_ABS [1]_  float32       Absolute magnitude in R band in mocks
DEC             float64 deg   Barycentric declination in ICRS
RA              float64 deg   Barycentric Right Ascension in ICRS
DESI_TARGET     int64         DESI (dark time program) target selection bitmask
PRIORITY_INIT   int64         Target initial priority from target selection bitmasks and OBSCONDITIONS
BGS_TARGET [1]_ int64         BGS (Bright Galaxy Survey) target selection bitmask
TILELOCID       int64         Is 10000*TILEID+LOCATION
PRIORITY        int32         Target current priority
SUBPRIORITY     float64       Random subpriority [0-1) to break assignment ties
TRUEZ           float32       True redshift in a galaxy mock catalog
RSDZ            float32       Redshift in mocks that includes RSD effects
ZWARN           int64         Redshift warning bitmask from Redrock
ZWARN_MTL       int64         The ZWARN from the zmtl file (contains extra bits)
=============== ======= ===== ========================================================================

.. [1] Optional, only present on bright samples

