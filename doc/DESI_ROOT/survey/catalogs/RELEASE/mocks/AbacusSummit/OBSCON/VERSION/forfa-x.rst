======
forFA
======

:Summary: This is the parent tracer catalog before entering any DESI processing. It has the basic imaging mask applied and tracers have been selected in the DR1 footprint already.
:Naming Convention: ``forFA{MOCKREA}.fits``, where ``{MOCKREA}`` is the mock realization (25 of them)
:Regex: ``forFA[0-9]{2}.fits`` 
:File Type: FITS, 2 GB  

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    
HDU1_  TARGETS BINTABLE Main Table
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----


This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = TARGETS

Catalog containing tracers in the approximate DR1 footprint

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =====================
    KEY    Example Value Type Comment
    ====== ============= ==== =====================
    NAXIS1 170           int  length of dimension 1
    NAXIS2 13551475      int  length of dimension 2
    DESIDR dr1           str  DESI Data Release
    ====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

============== ======= ===== =======================================================================================================
Name           Type    Units Description
============== ======= ===== =======================================================================================================
R_MAG_APP [1]_ float32       Apparent magnitude in R band in mocks
R_MAG_ABS [1]_ float32       Absolute magnitude in R band in mocks
DEC            float64 deg   Barycentric declination in ICRS
RA             float64 deg   Barycentric Right Ascension in ICRS
TRUEZ          float32       True redshift in a galaxy mock catalog
RSDZ           float32       Redshift in mocks that includes RSD effects
DESI_TARGET    int64         DESI (dark time program) target selection bitmask
PRIORITY_INIT  int64         Target initial priority from target selection bitmasks and OBSCONDITIONS
PRIORITY       int64         Target current priority
NUMOBS_MORE    int64         Number of additional observations needed
NUMOBS_INIT    int64         Initial number of observations for target calculated across target selection bitmasks and OBSCONDITIONS
BGS_TARGET     int64         BGS (Bright Galaxy Survey) target selection bitmask
TARGETID       int64         Unique DESI target ID
BRICKID        int64         Brick ID from tractor input
NOBS_G         int64         Number of images for central pixel in g-band
NOBS_R         int64         Number of images for central pixel in r-band
NOBS_Z         int64         Number of images for central pixel in z-band
MASKBITS       int16         Bitwise mask from the imaging indicating potential issue or blending
MWS_TARGET     int64         Milky Way Survey targeting bits
SUBPRIORITY    float64       Random subpriority [0-1) to break assignment ties
BRICKNAME      char[8]       Brick name from tractor input
OBSCONDITIONS  int64         Bitmask of allowed observing conditions
SCND_TARGET    int64         Target selection bitmask for secondary programs
ZWARN          int64         Redshift warning bitmask from Redrock
============== ======= ===== =======================================================================================================

.. [1] Optional, present only on the BRIGHT TRACERS (BGS)

