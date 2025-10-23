=========================
Potential assigment files
=========================

:Summary: This file includes all reachable sky coordinates, as determined by the DESI fiberassign software, matching the footprint of DESI target samples as well as information about collisions.
:Naming Convention: ``pota-{OBSCON}.fits`` where ``{OBSCON}`` can be ``DARK`` or ``BRIGHT``.
:Regex: ``pota-(BRIGHT|DARK)\.fits``
:File Type: FITS, 2 GB

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

All reachable tracers for the given realization for the given OBSCON (DARK or BRIGHT)

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =======================
    KEY    Example Value Type Comment
    ====== ============= ==== =======================
    NAXIS1 49            int  width of table in bytes
    NAXIS2 49152819      int  number of rows in table
    DESIDR dr1           str  DESI Data Release
    ====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

================ ======= ========== =======================================================================================================
Name             Type    Units      Description
================ ======= ========== =======================================================================================================
LOCATION         int64              Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBER            int64              Fiber ID on the CCDs [0-4999]
TARGETID         int64              Unique DESI target ID
RA               float32 deg        Barycentric Right Ascension in ICRS
DEC              float32 deg        Barycentric declination in ICRS
RSDZ             float32            Redshift in mocks that includes RSD effects
TRUEZ            float32            True redshift in a galaxy mock catalog
STATUS           binary             Bit column present in mocks to select according to nz or footprint
MASKBITS         int16              Bitwise mask from the imaging indicating potential issue or blending
NOBS_G           int16              Number of images for central pixel in g-band
NOBS_R           int16              Number of images for central pixel in r-band
NOBS_Z           int16              Number of images for central pixel in z-band
PRIORITY_INIT    int64              Target initial priority from target selection bitmasks and OBSCONDITIONS
PRIORITY         int64              Target current priority
DESI_TARGET      int64              DESI (dark time program) target selection bitmask
NUMOBS_MORE      int64              Number of additional observations needed
NUMOBS_INIT      int64              Initial number of observations for target calculated across target selection bitmasks and OBSCONDITIONS
BGS_TARGET       int64              BGS (Bright Galaxy Survey) target selection bitmask
MWS_TARGET       int64              Milky Way Survey targeting bits
SUBPRIORITY      float64            Random subpriority [0-1) to break assignment ties
BRICKNAME        char[8]            Brick name from tractor input
OBSCONDITIONS    int64              Bitmask of allowed observing conditions
SCND_TARGET      int64              Target selection bitmask for secondary programs
ZWARN            int64              Redshift warning bitmask from Redrock
COLLISION        logical            Boolean for whether given potential assignment had a fiber collision with any keep-out zone
TILEID           int64              Unique DESI tile ID
RAN_NUM_0_1 [1]_ float32            Random number between 0 and 1
NZ [1]_          float64 h^3 Mpc^-3 The comoving number density of the tracer at the given redshift, assuming complete sample
BRICKID [1]_     int64              Brick ID from tractor input
GALCAP [1]_      char[1]            Galactic cap N or S
================ ======= ========== =======================================================================================================

.. [1] Optional, only present in BRIGHT sample

