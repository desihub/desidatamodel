============================
mock FFA clustering catalogs
============================

:Summary: For each target type, LSS catalogs for the data, ready to be used for clustering measurements, are provided.
:Naming Convention: ``{TARGET}_{GALCAP}_clustering.dat.fits``, where ``{TARGET}`` is the target: ``QSO``, ``ELG_LOP``, ``LRG``, ``LRG+ELG_LOP``
                    for dark or ``BGS`` for bright. ``{GALCAP}`` is the Galactic hemisphere region ``NGC`` or ``SGC``.
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

================ ========= ========== =====================================================================================================================
Name             Type      Units      Description
================ ========= ========== =====================================================================================================================
LOCATION         int64                Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBER            int64                Fiber ID on the CCDs [0-4999]
TARGETID         int64                Unique DESI target ID
RA               float32   deg        Barycentric Right Ascension in ICRS
DEC              float32   deg        Barycentric declination in ICRS
Z                float32              Redshift measured by Redrock
TRUEZ            float32              True redshift in a galaxy mock catalog
STATUS           binary               Bit column present in mocks to select according to nz or footprint
MASKBITS         int16                Bitwise mask from the imaging indicating potential issue or blending
NOBS_G           int64                Number of images for central pixel in g-band. Note that NOBS_G for dark tracer is type = int16
NOBS_R           int64                Number of images for central pixel in r-band. Note that NOBS_R for dark tracer is type = int16
NOBS_Z           int64                Number of images for central pixel in z-band. Note that NOBS_Z for dark tracer is type = int16
PRIORITY_INIT    int64                Target initial priority from target selection bitmasks and OBSCONDITIONS
PRIORITY         int64                Target current priority
DESI_TARGET      int64                DESI (dark time program) target selection bitmask
NUMOBS_MORE      int64                Number of additional observations needed
NUMOBS_INIT      int64                Initial number of observations for target calculated across target selection bitmasks and OBSCONDITIONS
BGS_TARGET       int64                BGS (Bright Galaxy Survey) target selection bitmask
MWS_TARGET       int64                Milky Way Survey targeting bits
SUBPRIORITY      float64              Random subpriority [0-1) to break assignment ties
BRICKNAME        char[8]              Brick name from tractor input
OBSCONDITIONS    int64                Bitmask of allowed observing conditions
SCND_TARGET      int64                Target selection bitmask for secondary programs
ZWARN            int64                Redshift warning bitmask from Redrock
COLLISION        logical              Boolean for whether given potential assignment had a fiber collision with any keep-out zone
TILEID           int64                Unique DESI tile ID
TSNR2_ELG        float32              ELG template (S/N)^2 summed over B,R,Z
TSNR2_LYA        float32              LYA template (S/N)^2 summed over B,R,Z
TSNR2_BGS        float32              BGS template (S/N)^2 summed over B,R,Z
TSNR2_QSO        float32              QSO template (S/N)^2 summed over B,R,Z
TSNR2_LRG        float32              LRG template (S/N)^2 summed over B,R,Z
TILELOCID        int64                Is 10000*TILEID+LOCATION
NTILE            int64                Number of tiles target was available on
TILES            char[*]              TILEIDs of those tile, in string form separated by -
TILELOCIDS       char[*]              TILELOCIDs that the target was available for separated by -
WEIGHT_IIP       float32              Weight coming from the probability of assignment in alt histories
BITWEIGHTS       int64[4]             A size of two 64 bit masks that encodes which of the alternative assignment histories that the target was assigned in
PHOTSYS          char[1]              N for the MzLS/BASS photometric system, S for DECaLS
WEIGHT_COMP      float32              Completeness weight accounting for the local chance of being assigned a fiber
lrg_mask [1]_    binary               Imaging mask bits relevant to LRG targets
R_MAG_ABS [1]_   float32              Absolute magnitude in R band in mocks
WEIGHT_SYS       float64              Correction for fluctuations in projected density with imaging conditions, from random forrest method
WEIGHT_ZFAIL     float64              Should be all 1 at this point for main survey
WEIGHT           float64              The combination of all weights to use
NX               float64              Estimated mean number density given the redshift and number of overlapping tiles (NTILE)
WEIGHT_FKP       float64              1/(1+NZ*P0), with P0 different for each tracer
RAN_NUM_0_1 [1]_ float32              Random number between 0 and 1
NZ [1]_          float64   h^3 Mpc^-3 The comoving number density of the tracer at the given redshift, assuming complete sample
GALCAP [1]_      char[1]              Galactic cap N or S
BRICKID [1]_     int64                Brick ID from tractor input
================ ========= ========== =====================================================================================================================

.. [1] Optional

Notes and Examples
==================

* ``lrg_mask`` only present in LRG catalogs 
* ``R_MAG_ABS``, ``NZ``, ``RAN_NUM_0_1``, ``GALCAP``, ``BRICKID`` only present in BGS catalogs 

.. warning::

        For OBSCON = dark, dtypes of NOBS_G, NOBS_R, NOBS_Z is int16, instead of int64

