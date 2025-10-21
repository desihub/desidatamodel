=========================================
mock FFA and COMPLETE clustering catalogs
=========================================

:Summary: For each target type, LSS catalogs for the data, ready to be used for clustering measurements, are provided.
:Naming Convention: ``{TARGET}_{GALCAP}_clustering.dat.fits``, where ``{TARGET}`` is the target: ``QSO``, ``ELG_LOP``, ``LRG``, 
                    for dark or ``BGS_BRIGHT-21.5`` for bright. ``{GALCAP}`` is the Galactic hemisphere region ``NGC`` or ``SGC``.
:Regex: ``[A-Za-z0-9._+-]+_(NGC|SGC)_clustering\.dat\.fits``
:File Type: FITS, 237 MB

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

LSS catalogs for clustering measurements

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =======================
    KEY    Example Value Type Comment
    ====== ============= ==== =======================
    NAXIS1 137           int  width of table in bytes
    NAXIS2 1821322       int  number of rows in table
    DESIDR dr1           str  DESI Data Release
    ====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

============== ======= ===== ====================================================================================================
Name           Type    Units Description
============== ======= ===== ====================================================================================================
LOCATION       int64         Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBER          int64         Fiber ID on the CCDs [0-4999]
TARGETID       int64         Unique DESI target ID
RA             float32 deg   Barycentric Right Ascension in ICRS
DEC            float32 deg   Barycentric declination in ICRS
Z              float32       Redshift measured by Redrock
PRIORITY_INIT  int64         Target initial priority from target selection bitmasks and OBSCONDITIONS
PRIORITY       int64         Target current priority
DESI_TARGET    int64         DESI (dark time program) target selection bitmask
BRICKID        int64         Brick ID from tractor input
NOBS_G         int64         Number of images for central pixel in g-band
NOBS_R         int64         Number of images for central pixel in r-band
NOBS_Z         int64         Number of images for central pixel in z-band
MASKBITS       int16         Bitwise mask from the imaging indicating potential issue or blending
ZWARN          int64         Redshift warning bitmask from Redrock
COLLISION      logical       Boolean for whether given potential assignment had a fiber collision with any keep-out zone
TILEID         int64         Unique DESI tile ID
R_MAG_ABS [1]_ float32       Absolute magnitude in R band in mocks
lrg_mask [1]_  binary        label for field  18
PHOTSYS        char[1]       N for the MzLS/BASS photometric system, S for DECaLS
WEIGHT_SYS     float64       Correction for fluctuations in projected density with imaging conditions, from random forrest method
WEIGHT_COMP    float64       Completeness weight accounting for the local chance of being assigned a fiber
WEIGHT_ZFAIL   float64       Should be all 1 at this point for main survey
WEIGHT         float64       The combination of all weights to use
NTILE          int64         Number of tiles target was available on
NX             float64       Estimated mean number density given the redshift and number of overlapping tiles (NTILE)
WEIGHT_FKP     float64       1/(1+NZ*P0), with P0 different for each tracer
============== ======= ===== ====================================================================================================


.. [1] Optional

Notes and Examples
==================

* ``lrg_mask`` only present in LRG catalogs 
* ``R_MAG_ABS`` only present in BGS catalogs 
