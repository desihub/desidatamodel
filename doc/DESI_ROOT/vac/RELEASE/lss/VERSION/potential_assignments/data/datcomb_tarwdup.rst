===============
datcomb_tarwdup
===============

:Summary: File with information about all targets after match with potential assigment from FA.
:Naming Convention: ``datcomb_{PROGRAM}_tarwdup_Alltiles.fits``, where ``{PROGRAM}`` refers to the observing program, either ``dark`` or ``bright``.
:Regex: ``datcomb_(dark|bright)_tarwdup_Alltiles.fits``
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

==================== ======== ========= =======================================================================================================
Name                 Type     Units     Description
==================== ======== ========= =======================================================================================================
RA                   float64  deg       Target Right Ascension
DEC                  float64  deg       Target declination
TARGETID             int64              Unique DESI target ID
SUBPRIORITY          float64            Random subpriority [0-1) to break assignment ties
PRIORITY_INIT        int64              Target initial priority from target selection bitmasks and OBSCONDITIONS
ZWARN_MTL            int64              The ZWARN from the zmtl file (contains extra bits)
TARGET_STATE         char[30]           Combination of target class and its current observational state
TIMESTAMP            char[25] s         UTC/ISO time at which the target state was updated
PRIORITY             int64              Target current priority
FIBER                int32              Fiber ID on the CCDs [0-4999]
LOCATION             int32              Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
TILEID               int64              Unique DESI tile ID
SV3_DESI_TARGET [1]_ int64              DESI (dark time program) target selection bitmask for SV3
SV3_MWS_TARGET [1]_  int64              MWS (bright time program) target selection bitmask for SV3
SV3_BGS_TARGET [1]_  int64              BGS (bright time program) target selection bitmask for SV3
==================== ======== ========= =======================================================================================================

.. [1] Optional, only in dark sample. For the bright sample, they are recoverable from the target catalogs
