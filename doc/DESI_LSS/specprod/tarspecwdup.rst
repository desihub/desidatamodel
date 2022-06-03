==============================
tarspecwdup
==============================

:Summary: Match of targets (with duplicates after FA) with spectroscopic data from the
         specprod (fuji/guadalupe for SV3/DA02)
:Naming Convention: ``datcomb_{program}_tarspecwdup_{tag}.fits``, where ``{program}``
                    is dark or bright, ``{tag}`` is a string identifier
:Regex: ``datcomb_[a-z]_tarspecwdup_[a-z]\.fits``
:File Type: FITS, 3 GB

Contents
========

====== ======= ======== =================================
Number EXTNAME Type     Contents
====== ======= ======== =================================
HDU0_  PRIMARY IMAGE    *PrimaryHDU with array data type*
HDU1_          BINTABLE *Match spec with targets FA*
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

*Match catalog between spectroscopic information and duplicate targets 
after running fiber assigments*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =======================
KEY    Example Value Type Comment
====== ============= ==== =======================
NAXIS1 463           int  width of table in bytes
NAXIS2 7528042       int  number of rows in table
====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

========================== =========== ===== ==================
Name                       Type        Units Description
========================== =========== ===== ==================
RA                         float64     deg   Taken from ledger of targets at timestamp of fiberassign file; see ledger description (link)
DEC                        float64     deg   ""
TARGETID                   int64             ""
DESI_TARGET                int64             ""
BGS_TARGET                 int64             ""
MWS_TARGET                 int64             ""
SUBPRIORITY                float64           ""
PRIORITY_INIT              int64             ""
TARGET_STATE               char[30]          ""
TIMESTAMP                  char[25]          ""
PRIORITY                   int64             ""
FIBER                      int32             Taken from redrock catalog; see description there (link)
LOCATION                   int64             ""
TILEID                     int64             ""
TILELOCID                  int64             10000*TILEID+LOCATION
CHI2                       float64           Taken from redrock catalog; see description there (link)
COEFF                      float64[10]       ""
Z                          float64           ""
ZERR                       float64           ""
ZWARN                      int64             ""
NPIXELS                    int64             ""
SPECTYPE                   char[6]           ""
SUBTYPE                    char[20]          ""
NCOEFF                     int64             ""
DELTACHI2                  float64           ""
COADD_FIBERSTATUS          int32             ""
FIBERASSIGN_X              float32           ""
FIBERASSIGN_Y              float32           ""
COADD_NUMEXP               int16             ""
COADD_EXPTIME              float32           ""
COADD_NUMNIGHT             int16             ""
MEAN_DELTA_X               float32           ""
RMS_DELTA_X                float32           ""
MEAN_DELTA_Y               float32           ""
RMS_DELTA_Y                float32           ""
MEAN_PSF_TO_FIBER_SPECFLUX float32           ""
TSNR2_ELG_B                float32           ""
TSNR2_LYA_B                float32           ""
TSNR2_BGS_B                float32           ""
TSNR2_QSO_B                float32           ""
TSNR2_LRG_B                float32           ""
TSNR2_ELG_R                float32           ""
TSNR2_LYA_R                float32           ""
TSNR2_BGS_R                float32           ""
TSNR2_QSO_R                float32           ""
TSNR2_LRG_R                float32           ""
TSNR2_ELG_Z                float32           ""
TSNR2_LYA_Z                float32           ""
TSNR2_BGS_Z                float32           ""
TSNR2_QSO_Z                float32           ""
TSNR2_LRG_Z                float32           ""
TSNR2_ELG                  float32           ""
TSNR2_LYA                  float32           ""
TSNR2_BGS                  float32           ""
TSNR2_QSO                  float32           ""
TSNR2_LRG                  float32           ""
ZWARN_MTL                  int64             ZWARN flag from ledger of targets at timestamp of fiberassign file; see ledger description (link)
Z_QN                       float64           column shouldn't be in this file Z if QUASAR
Z_QN_CONF                  float64           column shouldn't be in this file Confidence of QSO
IS_QSO_QN                  int16             column shouldn't be in this file If it is QSO
========================== =========== ===== ==================


Notes and Examples
==================

