==================
MOCK full catalogs
==================

:Summary: mock catalogs containing information on all targets identified as reachable by DESI fiberassign, with one entry for each. The files are split by target type and whether of not vetos for angular positions and healpix maps have been applied
:Naming Convention: ``{TARGET}_full{VETO}.dat.fits``, where ``{TARGET}`` is the target type: ``QSO``, ``ELG_LOPnotqso``, ``LRG``, for dark or ``BGS_ANY``, ``BGS_BRIGHT`` or ``BGS_BRIGHT-21.5`` for bright. ``{VETO}`` is ``_noveto`` if vetos have not been applied, blank if vetos have been applied and ``_HPmapcut`` if both vetos and healpix map cuts have been applied.
:Regex: ``[A-Za-z0-9._+-]+_full(|_HPmapcut|_noveto)\.dat\.fits``
:File Type: FITS, 1 GB

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    Empty
HDU1_  LSS     BINTABLE Catalog data
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

Empty HDU.

HDU1
----

EXTNAME = LSS

Catalog data for the given target type; one entry per unique TARGETID

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =====================
    KEY    Example Value Type Comment
    ====== ============= ==== =====================
    NAXIS1 838           int  length of dimension 1
    NAXIS2 15327895      int  length of dimension 2
    DESIDR dr1           str  DESI Data Release
    ====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

================== ========= ===== =======================================================================================================================================
Name               Type      Units Description
================== ========= ===== =======================================================================================================================================
LOCATION           int32           Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBER              int32           Fiber ID on the CCDs [0-4999]
TARGETID           int64           Unique DESI target ID
TILEID             int64           Unique DESI tile ID
RA                 float32   deg   Barycentric Right Ascension in ICRS
DEC                float32   deg   Barycentric declination in ICRS
PRIORITY_INIT      int64           Target initial priority from target selection bitmasks and OBSCONDITIONS
DESI_TARGET        int64           DESI (dark time program) target selection bitmask
TILELOCID          int64           Is 10000*TILEID+LOCATION
PRIORITY           int32           Target current priority
SUBPRIORITY        float64         Random subpriority [0-1) to break assignment ties
TRUEZ              float32         True redshift in a galaxy mock catalog
Z                  float32         Redshift measured by Redrock
ZWARN              int64           Redshift warning bitmask from Redrock
ZWARN_MTL          int64           The ZWARN from the zmtl file (contains extra bits)
PRIORITY_ASSIGNED  int32           (only for data) PRIORITY of the target that was assigned to the given FIBER and TILEID (redundant with PRIORITY in the random catalogs)
GOODPRI            logical         True/False whether the priority of what was assigned to the location was less or equals to the base priority of the given target class
GOODHARDLOC        logical         True/False whether the fiber had good hardware
LOCATION_ASSIGNED  logical         True/False for assigned/unassigned for the target in question
TILELOCID_ASSIGNED logical         0/1 for unassigned/assigned for TILELOCID in question (it could have been assigned to a different target)
NTILE              int64           Number of tiles target was available on
TILES              char[*]         TILEIDs of those tile, in string form separated by -
TILELOCIDS         char[*]         TILELOCIDs that the target was available for separated by -
COMP_TILE          float64         Assignment completeness for all targets of this type with the same value for TILES
FRACZ_TILELOCID    float64         The fraction of targets of this type at this TILELOCID that received an observation (after forcing each target to a unique TILELOCID)
PHOTSYS            char[1]         N for the MzLS/BASS photometric system, S for DECaLS
lrg_mask [1]_      binary          lrg imaging mask
NOBS_G             int64           Number of images for central pixel in g-band
NOBS_R             int64           Number of images for central pixel in r-band
NOBS_Z             int64           Number of images for central pixel in z-band
MASKBITS           int16           Bitwise mask from the imaging indicating potential issue or blending
BGS_TARGET [1]_    int64           BGS (Bright Galaxy Survey) target selection bitmask
R_MAG_ABS [1]_     float32         Absolute magnitude in R band in mocks
================== ========= ===== =======================================================================================================================================

.. [1] Optional

Notes and Examples
==================

Optional columns:

* ``BGS_TARGET`` and ``R_MAG_ABS`` only present in BGS samples.
* ``lrg_mask`` only present in LRG samples.
