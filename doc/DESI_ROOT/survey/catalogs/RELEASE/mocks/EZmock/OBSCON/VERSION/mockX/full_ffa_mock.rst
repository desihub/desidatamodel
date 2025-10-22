=============
mock FFA full
=============

:Summary: LSS catalogs containing information on all targets identified as reachable by DESI fiberassign for the FFA flavour, with one entry for each. The files are split by target type
:Naming Convention: ``ffa_full_{TARGET}.fits``, where ``{TARGET}`` is the target type: ``QSO``, ``ELG_LOP``, ``LRG`` or ``LRG+ELG_LOP`` for dark or ``BGS`` for bright.
:Regex: ``ffa_full_[A-Za-z_]+\.fits``
:File Type: FITS, 11 GB

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

================ ======== ========== =====================================================================================================================
Name             Type     Units      Description
================ ======== ========== =====================================================================================================================
LOCATION         int64               Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBER            int64               Fiber ID on the CCDs [0-4999]
TARGETID         int64               Unique DESI target ID
RA               float32  deg        Barycentric Right Ascension in ICRS
DEC              float32  deg        Barycentric declination in ICRS
RSDZ             float32             Redshift in mocks that includes RSD effects
TRUEZ            float32             True redshift in a galaxy mock catalog
RAN_NUM_0_1 [1]_ float32             Random number between 0 and 1
STATUS           binary              Bit column present in mocks to select according to nz or footprint
MASKBITS         int16               Bitwise mask from the imaging indicating potential issue or blending
NOBS_G           int16               Number of images for central pixel in g-band
NOBS_R           int16               Number of images for central pixel in r-band
NOBS_Z           int16               Number of images for central pixel in z-band
NZ [1]_          float64  h^3 Mpc^-3 The comoving number density of the tracer at the given redshift, assuming complete sample
GALCAP [1]_      char[1]             Galactic cap N or S
DESI_TARGET      int64               DESI (dark time program) target selection bitmask
PRIORITY_INIT    int64               Target initial priority from target selection bitmasks and OBSCONDITIONS
PRIORITY         int64               Target current priority
NUMOBS_MORE      int64               Number of additional observations needed
NUMOBS_INIT      int64               Initial number of observations for target calculated across target selection bitmasks and OBSCONDITIONS
BRICKID          int64               Brick ID from tractor input
BGS_TARGET       int64               BGS (Bright Galaxy Survey) target selection bitmask
MWS_TARGET       int64               Milky Way Survey targeting bits
SUBPRIORITY      float64             Random subpriority [0-1) to break assignment ties
BRICKNAME        char[8]             Brick name from tractor input
OBSCONDITIONS    int64               Bitmask of allowed observing conditions
SCND_TARGET      int64               Target selection bitmask for secondary programs
ZWARN            int64               Redshift warning bitmask from Redrock
COLLISION        logical             Boolean for whether given potential assignment had a fiber collision with any keep-out zone
TILEID           int64               Unique DESI tile ID
TSNR2_ELG        float32             ELG template (S/N)^2 summed over B,R,Z
TSNR2_LYA        float32             LYA template (S/N)^2 summed over B,R,Z
TSNR2_BGS        float32             BGS template (S/N)^2 summed over B,R,Z
TSNR2_QSO        float32             QSO template (S/N)^2 summed over B,R,Z
TSNR2_LRG        float32             LRG template (S/N)^2 summed over B,R,Z
TILELOCID        int64               Is 10000*TILEID+LOCATION
NTILE            int64               Number of tiles target was available on
TILES            char[*]             TILEIDs of those tile, in string form separated by -
TILELOCIDS       char[*]             TILELOCIDs that the target was available for separated by -
WEIGHT_IIP       float32             Weight coming from the probability of assignment in alt histories
BITWEIGHTS       int64[4]            A size of two 64 bit masks that encodes which of the alternative assignment histories that the target was assigned in
PHOTSYS          char[1]             N for the MzLS/BASS photometric system, S for DECaLS
================ ======== ========== =====================================================================================================================

.. [1] Optional, present only on the BRIGHT TRACERS (BGS)

