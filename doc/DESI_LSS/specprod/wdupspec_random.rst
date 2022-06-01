===========================
wdupspec_random
===========================

:Summary: Match of randoms
         with information from the spectroscopic and target sample.

:Naming Convention: ``rancomb_{RANNUM}{program}wdupspec_{tag}.fits``, where ``{RANNUM}`` is
         the random number, ``{program}`` is dark or bright and 
         ``{tag}`` is a string identifier.

:Regex: ``rancomb_[0-9][a-z]wdupspec_[a-z]\.fits``

:File Type: FITS, 1 GB

Contents
========

====== ======= ======== =================================
Number EXTNAME Type     Contents
====== ======= ======== =================================
HDU0_  PRIMARY IMAGE    *PrimaryHDU with array data type*
HDU1_          BINTABLE *Main Table*
====== ======= ======== =================================


FITS Header Units
=================

HDU0
----

*Primary HDU conforms to FITS standard*

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

*Main data HDU. Merger of randoms to target info in given fibers*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =======================
KEY    Example Value Type Comment
====== ============= ==== =======================
NAXIS1 180           int  width of table in bytes
NAXIS2 7096864       int  number of rows in table
====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

========================== ======= ===== =================
Name                       Type    Units Description
========================== ======= ===== =================
LOCATION                   int64         Fiber location
FIBER                      int32         Fiber ID
TARGETID                   int64         Random target ID
RA                         float64 deg   Right Ascension
DEC                        float64 deg   Declination
TILEID                     int64         Tile ID
ZWARN                      int64         z warnings
COADD_FIBERSTATUS          int32         FA status
FIBERASSIGN_X              float32       FA position, x
FIBERASSIGN_Y              float32       FA position, y
COADD_NUMEXP               int16         Target num exp
COADD_EXPTIME              float32       Exposure time
COADD_NUMNIGHT             int16         numnight ID
MEAN_DELTA_X               float32       Delta x target
RMS_DELTA_X                float32       RMS Delta x
MEAN_DELTA_Y               float32       Delta y target
RMS_DELTA_Y                float32       RMS Delta y
MEAN_PSF_TO_FIBER_SPECFLUX float32       Target info
TSNR2_ELG_B                float32       Target info
TSNR2_LYA_B                float32       Target info
TSNR2_BGS_B                float32       Target info
TSNR2_QSO_B                float32       Target info
TSNR2_LRG_B                float32       Target info
TSNR2_ELG_R                float32       Target info
TSNR2_LYA_R                float32       Target info
TSNR2_BGS_R                float32       Target info
TSNR2_QSO_R                float32       Target info
TSNR2_LRG_R                float32       Target info
TSNR2_ELG_Z                float32       Target info
TSNR2_LYA_Z                float32       Target info
TSNR2_BGS_Z                float32       Target info
TSNR2_QSO_Z                float32       Target info
TSNR2_LRG_Z                float32       Target info
TSNR2_ELG                  float32       Target info
TSNR2_LYA                  float32       Target info
TSNR2_BGS                  float32       Target info
TSNR2_QSO                  float32       Target info
TSNR2_LRG                  float32       Target info
TILELOCID                  int64         Tile loc ID
========================== ======= ===== =================


Notes and Examples
==================

