=========================
RANDOM full MOCK catalogs
=========================

:Summary: LSS catalogs containing information on all of the random targets identified as reachable by DESI fiberassign, for one of the input randoms. The files are split by target type, random file number, and whether of not vetos for angular positions and healpix map cuts have been applied
:Naming Convention: ``{TARGET}_{RANN}_full{VETO}.ran.fits``, where ``{TARGET}`` is the target type: ``QSO``, ``ELG``, ``ELG_LOPnotqso``, ``LRG``, for dark or ``BGS_ANY``, ``BGS_BRIGHT`` for bright. ``{RANN}`` is the number between 0 and 17 designating the given random file, and ``{VETO}`` is _noveto if vetos have not been applied, blank if vetos have been applied and _HPmapcut if both vetos and healpix map cuts have been applied.
:Regex: ``[A-Za-z0-9._+-]+_[0-9]+_full(|_HPmapcut|_noveto)\.ran\.fits``
:File Type: FITS, 5 GB

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    Empty
HDU1_  LSS     BINTABLE Random data
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

Empty HDU.

HDU1
----

EXTNAME = LSS

Catalog of randoms

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =====================
    KEY    Example Value Type Comment
    ====== ============= ==== =====================
    NAXIS1 391           int  length of dimension 1
    NAXIS2 15297348      int  length of dimension 2
    DESIDR dr1           str  DESI Data Release
    ====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

=========== ======== ===== ======================================================================================================================================
Name        Type     Units Description
=========== ======== ===== ======================================================================================================================================
LOCATION    int64          Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBER       int64          Fiber ID on the CCDs [0-4999]
TARGETID    int64          Unique DESI target ID
RA          float64  deg   Barycentric Right Ascension in ICRS
DEC         float64  deg   Barycentric declination in ICRS
TILEID      int64          Unique DESI tile ID
PRIORITY    int32          Target current priority
TSNR2_ELG   float32        ELG template (S/N)^2 summed over B,R,Z
TSNR2_LYA   float32        LYA template (S/N)^2 summed over B,R,Z
TSNR2_BGS   float32        BGS template (S/N)^2 summed over B,R,Z
TSNR2_QSO   float32        QSO template (S/N)^2 summed over B,R,Z
TSNR2_LRG   float32        LRG template (S/N)^2 summed over B,R,Z
TILELOCID   int64          Is 10000*TILEID+LOCATION
ZPOSSLOC    logical        True/False whether the location could have been assigned to the given target class
GOODHARDLOC logical        True/False whether the fiber had good hardware
GOODPRI     logical        True/False whether the priority of what was assigned to the location was less or equals to the base priority of the given target class
GOODTSNR    logical        True/False whether the TSNR (class) value used was above the minimum threshold for the given target class
NTILE       int64          Number of tiles target was available on
TILES       char[*]        TILEIDs of those tile, in string form separated by -
TILELOCIDS  char[*]        TILELOCIDs that the target was available for separated by -
NOBS_G      int16          Number of images for central pixel in g-band
NOBS_R      int16          Number of images for central pixel in r-band
NOBS_Z      int16          Number of images for central pixel in z-band
MASKBITS    int16          Bitwise mask from the imaging indicating potential issue or blending
PHOTSYS     char[1]        N for the MzLS/BASS photometric system, S for DECaLS
=========== ======== ===== ======================================================================================================================================

