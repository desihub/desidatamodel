=========================================
mock FFA and COMPLETE clustering catalogs
=========================================

:Summary: For each target type, LSS catalogs for the data, ready to be used for clustering measurements, are provided.
:Naming Convention: ``{TARGET}_{FLAVOUR}_{GALCAP}_clustering.dat.fits``, where ``{TARGET}`` is the target: ``QSO``, ``ELG_LOP``, ``LRG``, 
                    for dark or ``BGS_BRIGHT-21.5`` for bright. ``{FLAVOUR}`` is ``ffa`` or ``complete`` and ``{GALCAP}`` is the Galactic hemisphere region ``NGC`` or ``SGC``.
:Regex: ``[A-Za-z0-9._+-]+_(ffa|complete)+_(NGC|SGC)_clustering\.dat\.fits``
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

================== ======== ===== =====================================================================================================================
Name               Type     Units Description
================== ======== ===== =====================================================================================================================
LOCATION           int64          Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBER              int64          Fiber ID on the CCDs [0-4999]
TARGETID           int64          Unique DESI target ID
R_MAG_ABS [1]_     float32        Absolute magnitude in r band in mocks
DEC                float64  deg   Barycentric declination in ICRS
RA                 float64  deg   Barycentric Right Ascension in ICRS
Z                  float32        Redshift measured by Redrock
DESI_TARGET        int64          DESI (dark time program) target selection bitmask
PRIORITY_INIT      int64          Target initial priority from target selection bitmasks and OBSCONDITIONS
PRIORITY           int64          Target current priority
BRICKID            int64          Brick ID from tractor input
NOBS_G             int64          Number of images for central pixel in g-band
NOBS_R             int64          Number of images for central pixel in r-band
NOBS_Z             int64          Number of images for central pixel in z-band
MASKBITS           int16          Bitwise mask from the imaging indicating potential issue or blending
ZWARN              int64          Redshift warning bitmask from Redrock
COLLISION          logical        Boolean for whether given potential assignment had a fiber collision with any keep-out zone
TILEID             int64          Unique DESI tile ID
PHOTSYS            char[1]        N for the MzLS/BASS photometric system, S for DECaLS
WEIGHT_SYS         float64        Correction for fluctuations in projected density with imaging conditions, from random forrest method
WEIGHT_COMP        float64        Completeness weight accounting for the local chance of being assigned a fiber
WEIGHT_ZFAIL       float64        Should be all 1 at this point for main survey
WEIGHT             float64        The combination of all weights to use
NTILE              int64          Number of tiles target was available on
NX                 float64        Estimated mean number density given the redshift and number of overlapping tiles (NTILE)
WEIGHT_FKP         float64        1/(1+NZ*P0), with P0 different for each tracer
lrg_mask [1]_      binary         (lower or upper case) Imaging mask bits relevant to LRG targets
R_MAG_APP [1]_     float32        Apparent magnitude in r band in mocks
NUMOBS_MORE [1]_   int64          Number of additional observations needed
NUMOBS_INIT [1]_   int64          Initial number of observations for target calculated across target selection bitmasks and OBSCONDITIONS
BGS_TARGET [1]_    int64          BGS (Bright Galaxy Survey) target selection bitmask
MWS_TARGET [1]_    int64          Milky Way Survey targeting bits
SUBPRIORITY [1]_   float64        Random subpriority [0-1) to break assignment ties
BRICKNAME [1]_     char[8]        Brick name from tractor input
OBSCONDITIONS [1]_ int64          Bitmask of allowed observing conditions
SCND_TARGET [1]_   int64          Target selection bitmask for secondary programs
TSNR2_ELG [1]_     float32        ELG template (S/N)^2 summed over B,R,Z
TSNR2_LYA [1]_     float32        LYA template (S/N)^2 summed over B,R,Z
TSNR2_BGS [1]_     float32        BGS template (S/N)^2 summed over B,R,Z
TSNR2_QSO [1]_     float32        QSO template (S/N)^2 summed over B,R,Z
TSNR2_LRG [1]_     float32        LRG template (S/N)^2 summed over B,R,Z
TILELOCID [1]_     int64          Is 10000*TILEID+LOCATION
TILES [1]_         char[*]        TILEIDs of those tile, in string form separated by -
TILELOCIDS [1]_    char[*]        TILELOCIDs that the target was available for separated by -
WEIGHT_IIP [1]_    float32        Weight coming from the probability of assignment in alt histories
BITWEIGHTS [1]_    int64[4]       A size of two 64 bit masks that encodes which of the alternative assignment histories that the target was assigned in
WEIGHT_IMLIN [1]_  float64        Imaging systematics weights derived with the eBOSS linear regression method
================== ======== ===== =====================================================================================================================

.. [1] Optional

Notes and Examples
==================

* ``lrg_mask`` only present in LRG catalogs 
* ``R_MAG_ABS`` only present in BGS catalogs 
* ``R_MAG_APP`` only present in BGS ffa catalogs
* ``NUMOBS_MORE``, ``NUMOBS_INIT``, ``BGS_TARGET``, ``MWS_TARGET``, ``SUBPRIORITY``, ``BRICKNAME``, ``OBSCONDITIONS``, ``SCND_TARGET``, ``TSNR2_ELG``, ``TSNR2_LYA``, ``TSNR2_BGS``, ``TSNR2_QSO``, ``TSNR2_LRG``, ``TILELOCID``, ``TILES``, ``TILELOCIDS``, ``WEIGHT_IIP``, ``BITWEIGHTS`` and ``WEIGHT_IMLIN`` only present in ffa catalogs
