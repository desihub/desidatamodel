=========================
Potential assigment files
=========================

:Summary: This file includes all reachable sky coordinates, as determined by the DESI fiberassign software, matching the footprint of DESI target samples as well as information about collisions
:Naming Convention: ``pota-{OBSCON}.fits`` or ``pota-{OBSCON}_{TAG}_{TRACER}.fits``, where ``{OBSCON}`` can be ``DARK`` or ``BRIGHT`` and ``{TAG}`` can be ``joined_unreduced`` or ``withntile`` (optional, only for dark tracers) and ``{TRACER}`` can be ``LRG``, ``QSO``, ``ELG_LOP`` for DARK or ``BGS`` for BRIGHT.
:Regex: ``pota-(BRIGHT|DARK)(?:_(joined_unreduced|withntile)_(LRG|BGS|QSO|ELG))?\.fits``
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

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = LSS

All reachable randoms for the given realization in the directory (18 randoms) for the given OBSCON (DARK or BRIGHT)

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

=============== ======== ===== =======================================================================================================
Name            Type     Units Description
=============== ======== ===== =======================================================================================================
LOCATION        int64          Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBER           int64          Fiber ID on the CCDs [0-4999]
TARGETID        int64          Unique DESI target ID
R_MAG_APP [1]_  float32        Apparent magnitude in r band in mocks
R_MAG_ABS [1]_  float32        Absolute magnitude in r band in mocks
DEC             float64  deg   Barycentric declination in ICRS
RA              float64  deg   Barycentric Right Ascension in ICRS
TRUEZ           float32        True redshift in a galaxy mock catalog
RSDZ            float32        Redshift in mocks that includes RSD effects
DESI_TARGET     int64          DESI (dark time program) target selection bitmask
PRIORITY_INIT   int64          Target initial priority from target selection bitmasks and OBSCONDITIONS
PRIORITY        int64          Target current priority
NUMOBS_MORE     int64          Number of additional observations needed
NUMOBS_INIT     int64          Initial number of observations for target calculated across target selection bitmasks and OBSCONDITIONS
BRICKID         int64          Brick ID from tractor input
NOBS_G          int64          Number of images for central pixel in g-band
NOBS_R          int64          Number of images for central pixel in r-band
NOBS_Z          int64          Number of images for central pixel in z-band
MASKBITS        int16          Bitwise mask from the imaging indicating potential issue or blending
BGS_TARGET      int64          BGS (Bright Galaxy Survey) target selection bitmask
MWS_TARGET      int64          Milky Way Survey targeting bits
SUBPRIORITY     float64        Random subpriority [0-1) to break assignment ties
BRICKNAME       char[8]        Brick name from tractor input
OBSCONDITIONS   int64          Bitmask of allowed observing conditions
SCND_TARGET     int64          Target selection bitmask for secondary programs
ZWARN           int64          Redshift warning bitmask from Redrock
COLLISION       logical        Boolean for whether given potential assignment had a fiber collision with any keep-out zone
TILEID          int64          Unique DESI tile ID
TSNR2_ELG [1]_  float32        ELG template (S/N)^2 summed over B,R,Z
TSNR2_LYA [1]_  float32        LYA template (S/N)^2 summed over B,R,Z
TSNR2_BGS [1]_  float32        BGS template (S/N)^2 summed over B,R,Z
TSNR2_QSO [1]_  float32        QSO template (S/N)^2 summed over B,R,Z
TSNR2_LRG [1]_  float32        LRG template (S/N)^2 summed over B,R,Z
TILELOCID [1]_  int64          Is 10000*TILEID+LOCATION
NTILE [1]_      int64          Number of tiles target was available on
TILES [1]_      char[*]        TILEIDs of those tile, in string form separated by -
TILELOCIDS [1]_ char[*]        TILELOCIDs that the target was available for separated by -
STATUS [1]_     int32          Bit column present in mocks to select according to nz or footprint
=============== ======== ===== =======================================================================================================

.. [1] Optional
 

Notes and Examples
==================

* ``R_MAG_APP`` and ``R_MAG_ABS`` present in bright samples only
* ``TSNR2_ELG``, ``TSNR2_LYA``, ``TSNR2_BGS``, ``TSNR2_QSO``, ``TSNR2_LRG``, ``TILELOCID`` present for TAG = joined_unreduced only
* ``NTILE``, ``TILES``, ``TILELOCIDS`` present for TAG = joined_unreduced and TAG = withntile
* ``STATUS`` present in pota-DARK samples only
