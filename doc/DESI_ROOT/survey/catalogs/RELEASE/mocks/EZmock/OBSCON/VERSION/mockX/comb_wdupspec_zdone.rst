===============
COMB FILE ZDONE
===============

:Summary: Match of potential assignments with information from the mock parent sample given the TILEID and the LOCATION
:Naming Convention: ``comb{OBSCON}_wdupspec_zdone.fits``, , where ``{OBSCON}`` is the observing program, either ``dark`` or ``bright``.
:Regex: ``comb+(dark|bright)_wdupspec_zdone.fits`` 
:File Type: FITS, 3 GB  

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

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = LSS

Main data HDU. Merger of randoms to target info in given fibers

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =====================
    KEY    Example Value Type Comment
    ====== ============= ==== =====================
    NAXIS1 221           int  length of dimension 1
    NAXIS2 1624343       int  length of dimension 2
    DESIDR dr1           str  DESI Data Release
    ====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

============= ======= ========== =======================================================================================================
Name          Type    Units      Description
============= ======= ========== =======================================================================================================
LOCATION      int64              Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBER         int64              Fiber ID on the CCDs [0-4999]
TARGETID      int64              Unique DESI target ID
RA            float32 deg        Barycentric Right Ascension in ICRS
DEC           float32 deg        Barycentric declination in ICRS
RSDZ          float32            Redshift in mocks that includes RSD effects
TRUEZ         float32            True redshift in a galaxy mock catalog
RAN_NUM_0_1   float32            Random number between 0 and 1
STATUS        binary             Bit column present in Mocks to select according to nz or footprint
MASKBITS      int16              Bitwise mask from the imaging indicating potential issue or blending
NOBS_G        int64              Number of images for central pixel in g-band. Note that NOBS_G for dark tracer is type = int16
NOBS_R        int64              Number of images for central pixel in r-band. Note that NOBS_R for dark tracer is type = int16
NOBS_Z        int64              Number of images for central pixel in z-band. Note that NOBS_Z for dark tracer is type = int16
NZ            float64 h^3 Mpc^-3 The comoving number density of the tracer at the given redshift, assuming complete sample
GALCAP        char[1]            Galactic cap (N or S)
DESI_TARGET   int64              DESI (dark time program) target selection bitmask
PRIORITY_INIT int64              Target initial priority from target selection bitmasks and OBSCONDITIONS
PRIORITY      int64              Target current priority
NUMOBS_MORE   int64              Number of additional observations needed
NUMOBS_INIT   int64              Initial number of observations for target calculated across target selection bitmasks and OBSCONDITIONS
BRICKID       int64              Brick ID from tractor input
BGS_TARGET    int64              BGS (Bright Galaxy Survey) target selection bitmask
MWS_TARGET    int64              Milky Way Survey targeting bits
SUBPRIORITY   float64            Random subpriority [0-1) to break assignment ties
BRICKNAME     char[8]            Brick name from tractor input
OBSCONDITIONS int64              Bitmask of allowed observing conditions
SCND_TARGET   int64              Target selection bitmask for secondary programs
ZWARN         int64              Redshift warning bitmask from Redrock
COLLISION     logical            Boolean for whether given potential assignment had a fiber collision with any keep-out zone
TILEID        int64              Unique DESI tile ID
TSNR2_ELG     float32            ELG template (S/N)^2 summed over B,R,Z
TSNR2_LYA     float32            LYA template (S/N)^2 summed over B,R,Z
TSNR2_BGS     float32            BGS template (S/N)^2 summed over B,R,Z
TSNR2_QSO     float32            QSO template (S/N)^2 summed over B,R,Z
TSNR2_LRG     float32            LRG template (S/N)^2 summed over B,R,Z
TILELOCID     int64              Is 10000*TILEID+LOCATION
============= ======= ========== =======================================================================================================

.. warning::

        For OBSCON = dark, dtypes of NOBS_G, NOBS_R, NOBS_Z is int16, instead of int64

