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
RA                         float64     deg   Right Ascension
DEC                        float64     deg   Declination
TARGETID                   int64             Unique ID
DESI_TARGET                int64             If in DESI
BGS_TARGET                 int64             If in BGS
MWS_TARGET                 int64             If in MWS
SUBPRIORITY                float64           Subpriority
PRIORITY_INIT              int64             Initial priority
TARGET_STATE               char[30]          Target state
TIMESTAMP                  char[25]          Time stamp
PRIORITY                   int64             Priority
FIBER                      int32             Fiber ID
LOCATION                   int64             Location fiber
TILEID                     int64             Tile ID
TILELOCID                  int64             Tile loc ID
CHI2                       float64           Chi2 SED
COEFF                      float64[10]       Coefficient
Z                          float64           Redshift
ZERR                       float64           Uncertainty in Z
ZWARN                      int64             Z warnings
NPIXELS                    int64             N pixels
SPECTYPE                   char[6]           Spec type
SUBTYPE                    char[20]          Spec Sub-type
NCOEFF                     int64             N coefficients
DELTACHI2                  float64           Delta chi2
COADD_FIBERSTATUS          int32             Fiber status
FIBERASSIGN_X              float32           Fiber position, x
FIBERASSIGN_Y              float32           Fiber position, y
COADD_NUMEXP               int16             Number exposures
COADD_EXPTIME              float32           Exposre time
COADD_NUMNIGHT             int16             Numnight ID
MEAN_DELTA_X               float32           Delta x target
RMS_DELTA_X                float32           RMS Delta x
MEAN_DELTA_Y               float32           Delta y target
RMS_DELTA_Y                float32           RMS Delta y
MEAN_PSF_TO_FIBER_SPECFLUX float32           Target info
TSNR2_ELG_B                float32           Target info
TSNR2_LYA_B                float32           Target info
TSNR2_BGS_B                float32           Target info
TSNR2_QSO_B                float32           Target info
TSNR2_LRG_B                float32           Target info
TSNR2_ELG_R                float32           Target info
TSNR2_LYA_R                float32           Target info
TSNR2_BGS_R                float32           Target info
TSNR2_QSO_R                float32           Target info
TSNR2_LRG_R                float32           Target info
TSNR2_ELG_Z                float32           Target info
TSNR2_LYA_Z                float32           Target info
TSNR2_BGS_Z                float32           Target info
TSNR2_QSO_Z                float32           Target info
TSNR2_LRG_Z                float32           Target info
TSNR2_ELG                  float32           Target info
TSNR2_LYA                  float32           Target info
TSNR2_BGS                  float32           Target info
TSNR2_QSO                  float32           Target info
TSNR2_LRG                  float32           Target info
ZWARN_MTL                  int64             Z warnings in MTL
Z_QN                       float64           Z if QUASAR
Z_QN_CONF                  float64           Confidence of QSO
IS_QSO_QN                  int16             If it is QSO
========================== =========== ===== ==================


Notes and Examples
==================

