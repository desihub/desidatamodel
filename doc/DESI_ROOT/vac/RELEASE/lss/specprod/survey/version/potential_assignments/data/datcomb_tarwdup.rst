===============
datcomb_tarwdup
===============

:Summary: File with information about all targets after match with potential assigment from FA.
:Naming Convention: ``datcomb_{PROGRAM}_tarwdup_alltiles.fits``, where ``{PROGRAM}`` refers to the observing program, either ``dark`` or ``bright``.
:Regex: ``datcomb_[a-z]{4,6}_tarwdup_alltiles.fits``
:File Type: FITS, 1 GB

Contents
========

====== ===================== ======== ===================
Number EXTNAME               Type     Contents
====== ===================== ======== ===================
HDU0_                        IMAGE    Empty
HDU1_  POTENTIAL_ASSIGNMENTS BINTABLE Catalog data
====== ===================== ======== ===================


FITS Header Units
=================

HDU0
----

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = POTENTIAL_ASSIGNMENTS

*Merge between potential assigments from fiber assigment and input targets*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ========================= ===== =======================
    KEY      Example Value             Type  Comment
    ======== ========================= ===== =======================
    NAXIS1   151                       int   width of table in bytes
    NAXIS2   10117500                  int   number of rows in table
    DESIDR   edr                       str   DESI Data Release
    ======== ========================= ===== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

============= ======== ========= =======================================================================================================
Name          Type     Units     Description
============= ======== ========= =======================================================================================================
RA            float64  deg       Target Right Ascension
DEC           float64  deg       Target declination
REF_EPOCH     float32  yr        Reference epoch for Gaia/Tycho astrometry. Typically 2015.5 for Gaia
PARALLAX      float32  mas       Reference catalog parallax
PMRA          float32  mas yr^-1 proper motion in the +RA direction (already including cos(dec))
PMDEC         float32  mas yr^-1 Proper motion in the +Dec direction
TARGETID      int64              Unique DESI target ID
SUBPRIORITY   float64            Random subpriority [0-1) to break assignment ties
OBSCONDITIONS int32              Bitmask of allowed observing conditions
PRIORITY_INIT int64              Target initial priority from target selection bitmasks and OBSCONDITIONS
NUMOBS_INIT   int64              Initial number of observations for target calculated across target selection bitmasks and OBSCONDITIONS
NUMOBS_MORE   int64              Number of additional observations needed
NUMOBS        int64              Number of spectroscopic observations (on this specific, single tile)
Z             float64            Redshift measured by Redrock
ZWARN_MTL     int64              The ZWARN from the zmtl file (contains extra bits)
ZTILEID       int32              ID of tile that most recently updated target&#x27;s state
TARGET_STATE  char[30]           Combination of target class and its current observational state
TIMESTAMP     char[25] s         UTC/ISO time at which the target state was updated
VERSION       char[14]           Tag of desitarget used to create the target catalog
PRIORITY      int64              Target current priority
FIBER         int32              Fiber ID on the CCDs [0-4999]
LOCATION      int32              Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
TILEID        int64              Unique DESI tile ID
============= ======== ========= =======================================================================================================

