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
LOCATION                   int64         From fiberassign fba FAVAIL HDU (link)
FIBER                      int32         ""
TARGETID                   int64         From target random (link)
RA                         float64 deg   ""
DEC                        float64 deg   ""
TILEID                     int64         From fiberassign file name
ZWARN                      int64         From redrock catalog, matched to TILEID,LOCATION (link)
COADD_FIBERSTATUS          int32         ""
FIBERASSIGN_X              float32       ""
FIBERASSIGN_Y              float32       ""
COADD_NUMEXP               int16         ""
COADD_EXPTIME              float32       ""
COADD_NUMNIGHT             int16         ""
MEAN_DELTA_X               float32       ""
RMS_DELTA_X                float32       ""
MEAN_DELTA_Y               float32       ""
RMS_DELTA_Y                float32       ""
MEAN_PSF_TO_FIBER_SPECFLUX float32       ""
TSNR2_ELG_B                float32       ""
TSNR2_LYA_B                float32       ""
TSNR2_BGS_B                float32       ""
TSNR2_QSO_B                float32       ""
TSNR2_LRG_B                float32       ""
TSNR2_ELG_R                float32       ""
TSNR2_LYA_R                float32       ""
TSNR2_BGS_R                float32       ""
TSNR2_QSO_R                float32       ""
TSNR2_LRG_R                float32       ""
TSNR2_ELG_Z                float32       ""
TSNR2_LYA_Z                float32       ""
TSNR2_BGS_Z                float32       ""
TSNR2_QSO_Z                float32       ""
TSNR2_LRG_Z                float32       ""
TSNR2_ELG                  float32       ""
TSNR2_LYA                  float32       ""
TSNR2_BGS                  float32       ""
TSNR2_QSO                  float32       ""
TSNR2_LRG                  float32       ""
TILELOCID                  int64         10000*TILEID+LOCATION
========================== ======= ===== =================


Notes and Examples
==================

