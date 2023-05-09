================
rancomb_wdupspec
================

:Summary: Match of randoms with information from the spectroscopic and target sample. 
:Naming Convention: ``rancomb_{RANN}{PROGRAM}wdupspec_zdone.fits``, where ``{RANN}`` is the number of the random file (0 through 17) and ``{PROGRAM}`` is the observing program, either ``dark`` or ``bright``.
:Regex: ``rancomb_[0-17][a-z]{4,6}wdupspec_Alltiles.fits``
:File Type: FITS, 1 GB

Contents
========

====== ======== ======== ===================
Number EXTNAME  Type     Contents
====== ======== ======== ===================
HDU0_           IMAGE    Empty
HDU1_  ZCATALOG BINTABLE Catalog data
====== ======== ======== ===================


FITS Header Units
=================

HDU0
----

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = ZCATALOG

*Main data HDU. Merger of randoms to target info in given fibers*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ========================= ===== =======================
    KEY      Example Value             Type  Comment
    ======== ========================= ===== =======================
    NAXIS1   184                       int   width of table in bytes
    NAXIS2   6045226                   int   number of rows in table
    DESIDR   edr                       str   DESI Data Release
    ======== ========================= ===== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

========================== ======= ===== ===============================================================================================================================
Name                       Type    Units Description
========================== ======= ===== ===============================================================================================================================
LOCATION                   int64         Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBER                      int32         Fiber ID on the CCDs [0-4999]
TARGETID                   int64         Unique DESI target ID
RA                         float64 deg   Target Right Ascension
DEC                        float64 deg   Target declination
TILEID                     int64         Unique DESI tile ID
ZWARN                      int64         Redshift warning bitmask from Redrock
COADD_FIBERSTATUS          int32         bitwise-AND of input FIBERSTATUS
FIBERASSIGN_X              float32 mm    Fiberassign expected CS5 X location on focal plane
FIBERASSIGN_Y              float32 mm    Fiberassign expected CS5 Y location on focal plane
PRIORITY                   int32         Target current priority
COADD_NUMEXP               int16         Number of exposures in coadd
COADD_EXPTIME              float32 s     Summed exposure time for coadd
COADD_NUMNIGHT             int16         Number of nights in coadd
MEAN_DELTA_X               float32 mm    Mean (over exposures) fiber difference requested - actual CS5 X location on focal plane
RMS_DELTA_X                float32 mm    RMS (over exposures) of the fiber difference between measured and requested CS5 X location on focal plane
MEAN_DELTA_Y               float32 mm    Mean (over exposures) fiber difference requested - actual CS5 Y location on focal plane
RMS_DELTA_Y                float32 mm    RMS (over exposures) of the fiber difference between measured and requested CS5 Y location on focal plane
MEAN_PSF_TO_FIBER_SPECFLUX float32       Mean of input exposures fraction of light from point-like source captured by 1.5 arcsec diameter fiber given atmospheric seeing
TSNR2_ELG_B                float32       ELG B template (S/N)^2
TSNR2_LYA_B                float32       LYA B template (S/N)^2
TSNR2_BGS_B                float32       BGS B template (S/N)^2
TSNR2_QSO_B                float32       QSO B template (S/N)^2
TSNR2_LRG_B                float32       LRG B template (S/N)^2
TSNR2_ELG_R                float32       ELG R template (S/N)^2
TSNR2_LYA_R                float32       LYA R template (S/N)^2
TSNR2_BGS_R                float32       BGS R template (S/N)^2
TSNR2_QSO_R                float32       QSO R template (S/N)^2
TSNR2_LRG_R                float32       LRG R template (S/N)^2
TSNR2_ELG_Z                float32       ELG Z template (S/N)^2
TSNR2_LYA_Z                float32       LYA Z template (S/N)^2
TSNR2_BGS_Z                float32       BGS Z template (S/N)^2
TSNR2_QSO_Z                float32       QSO Z template (S/N)^2
TSNR2_LRG_Z                float32       LRG Z template (S/N)^2
TSNR2_ELG                  float32       ELG template (S/N)^2 summed over B,R,Z
TSNR2_LYA                  float32       LYA template (S/N)^2 summed over B,R,Z
TSNR2_BGS                  float32       BGS template (S/N)^2 summed over B,R,Z
TSNR2_QSO                  float32       QSO template (S/N)^2 summed over B,R,Z
TSNR2_LRG                  float32       LRG template (S/N)^2 summed over B,R,Z
TILELOCID                  int64         Is 10000*TILEID+LOCATION
========================== ======= ===== ===============================================================================================================================

