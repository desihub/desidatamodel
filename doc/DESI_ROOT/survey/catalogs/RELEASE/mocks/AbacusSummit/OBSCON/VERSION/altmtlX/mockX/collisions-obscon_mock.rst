=================
collisions OBSCON
=================

:Summary: Compilation of all potential assignments with collisions with fiber assignment keep out zones given FIBER and LOCATION for the given TILEID
:Naming Convention: ``collisions-{OBSCON}_mock{MOCKREA}.fits``, where ``{OBSCON}`` can be bright or dark and ``{MOCKREA}`` is the mock realization (25 of them)
:Regex: ``collision_(bright|dark)_mock[0-9]+\.fits``
:File Type: FITS, 334 MB

Contents
========

====== ========= ======== ===================
Number EXTNAME   Type     Contents
====== ========= ======== ===================
HDU0_            IMAGE    Empty
HDU1_  COLLISION BINTABLE Catalog data
====== ========= ======== ===================


FITS Header Units
=================

HDU0
----

Empty HDU.

HDU1
----

EXTNAME = COLLISION

Main collision catalog for the given program bright or dark

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =======================
    KEY    Example Value Type Comment
    ====== ============= ==== =======================
    NAXIS1 24            int  width of table in bytes
    NAXIS2 1775487       int  number of rows in table
    DESIDR dr1           str  DESI Data Release
    ====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

=============== ======= ===== =======================================================================================================
Name            Type    Units Description
=============== ======= ===== =======================================================================================================
LOCATION        int64         Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBER           int64         Fiber ID on the CCDs [0-4999]
TARGETID        int64         Unique DESI target ID
RA              float32 deg   Barycentric Right Ascension in ICRS
DEC             float32 deg   Barycentric declination in ICRS
TRUEZ           float32       True redshift in a galaxy mock catalog
STATUS          int32         Bit column present in Mocks to select according to nz or footprint
RSDZ            float32       Redshift in mocks that includes RSD effects
PRIORITY_INIT   int64         Target initial priority from target selection bitmasks and OBSCONDITIONS
PRIORITY        int64         Target current priority
DESI_TARGET     int64         DESI (dark time program) target selection bitmask
NUMOBS_MORE     int64         Number of additional observations needed
NUMOBS_INIT     int64         Initial number of observations for target calculated across target selection bitmasks and OBSCONDITIONS
BRICKID         int64         Brick ID from tractor input
NOBS_G          int64         Number of images for central pixel in g-band
NOBS_R          int64         Number of images for central pixel in r-band
NOBS_Z          int64         Number of images for central pixel in z-band
MASKBITS        int16         Bitwise mask from the imaging indicating potential issue or blending
BGS_TARGET      int64         BGS (Bright Galaxy Survey) target selection bitmask
MWS_TARGET      int64         Milky Way Survey targeting bits
SUBPRIORITY     float64       Random subpriority [0-1) to break assignment ties
BRICKNAME       char[8]       Brick name from tractor input
OBSCONDITIONS   int64         Bitmask of allowed observing conditions
SCND_TARGET     int64         Target selection bitmask for secondary programs
ZWARN           int64         Redshift warning bitmask from Redrock
COLLISION       logical       Boolean for whether given potential assignment had a fiber collision with any keep-out zone
TILEID          int64         Unique DESI tile ID
R_MAG_APP [1]_  float32       Apparent magnitude in R band in mocks
R_MAG_ABS [1]_  float32       Absolute magnitude in R band in mocks
=============== ======= ===== =======================================================================================================

.. [1] Optional, present in the bright samples only

