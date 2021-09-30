=====
ztile
=====

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``ztile-sv2-backup-cumulative.fits``, where ... *Give a human readable
    description of the filename, e.g. ``blat-{EXPID}`` where ``{EXPID}``
    is the 8-digit exposure ID.*
:Regex: ``ztile-sv2-backup-cumulative.fits`` *Give a regular expression for this filename.
    For example, a six-digit number would correspond to ``[0-9]{6}``.*
:File Type: FITS, 4 MB  *This section gives the type of the file
    and its approximate size.*

Contents
========

====== ============ ======== ===================
Number EXTNAME      Type     Contents
====== ============ ======== ===================
HDU0_               IMAGE    *Brief Description*
HDU1_  ZCATALOG     BINTABLE *Brief Description*
HDU2_  EXP_FIBERMAP BINTABLE *Brief Description*
====== ============ ======== ===================


FITS Header Units
=================

HDU0
----

*Summarize the contents of this HDU.*

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = ZCATALOG

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============= ==== =======================
KEY      Example Value Type Comment
======== ============= ==== =======================
NAXIS1   677           int  width of table in bytes
NAXIS2   5000          int  number of rows in table
RRVER    0.15.0        str  Redrock version
TEMNAM00 GALAXY        str
TEMVER00 2.6           str
TEMNAM01 QSO           str
TEMVER01 0.1           str
TEMNAM02 STAR:::A      str
TEMVER02 0.1           str
TEMNAM03 STAR:::B      str
TEMVER03 0.1           str
TEMNAM04 STAR:::CV     str
TEMVER04 0.1           str
TEMNAM05 STAR:::F      str
TEMVER05 0.1           str
TEMNAM06 STAR:::G      str
TEMVER06 0.1           str
TEMNAM07 STAR:::K      str
TEMVER07 0.1           str
TEMNAM08 STAR:::M      str
TEMVER08 0.1           str
TEMNAM09 STAR:::WD     str
TEMVER09 0.1           str
======== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

========================== =========== ===== ===================
Name                       Type        Units Description
========================== =========== ===== ===================
TARGETID                   int64             label for field   1
CHI2                       float64           label for field   2
COEFF                      float64[10]       label for field   3
Z                          float64           label for field   4
ZERR                       float64           label for field   5
ZWARN                      int64             label for field   6
NPIXELS                    int64             label for field   7
SPECTYPE                   char[6]           label for field   8
SUBTYPE                    char[20]          label for field   9
NCOEFF                     int64             label for field  10
DELTACHI2                  float64           label for field  11
PETAL_LOC                  int16             label for field  12
DEVICE_LOC                 int32             label for field  13
LOCATION                   int64             label for field  14
FIBER                      int32             label for field  15
COADD_FIBERSTATUS          int32             label for field  16
TARGET_RA                  float64           label for field  17
TARGET_DEC                 float64           label for field  18
PMRA                       float32           label for field  19
PMDEC                      float32           label for field  20
REF_EPOCH                  float32           label for field  21
LAMBDA_REF                 float32           label for field  22
FA_TARGET                  int64             label for field  23
FA_TYPE                    binary            label for field  24
OBJTYPE                    char[3]           label for field  25
FIBERASSIGN_X              float32           label for field  26
FIBERASSIGN_Y              float32           label for field  27
PRIORITY                   int32             label for field  28
SUBPRIORITY                float64           label for field  29
OBSCONDITIONS              int32             label for field  30
RELEASE                    int16             label for field  31
BRICKID                    int32             label for field  32
BRICK_OBJID                int32             label for field  33
MORPHTYPE                  char[4]           label for field  34
FLUX_G                     float32           label for field  35
FLUX_R                     float32           label for field  36
FLUX_Z                     float32           label for field  37
FLUX_IVAR_G                float32           label for field  38
FLUX_IVAR_R                float32           label for field  39
FLUX_IVAR_Z                float32           label for field  40
MASKBITS                   int16             label for field  41
REF_ID                     int64             label for field  42
REF_CAT                    char[2]           label for field  43
GAIA_PHOT_G_MEAN_MAG       float32           label for field  44
GAIA_PHOT_BP_MEAN_MAG      float32           label for field  45
GAIA_PHOT_RP_MEAN_MAG      float32           label for field  46
PARALLAX                   float32           label for field  47
BRICKNAME                  char[8]           label for field  48
EBV                        float32           label for field  49
FLUX_W1                    float32           label for field  50
FLUX_W2                    float32           label for field  51
FLUX_IVAR_W1               float32           label for field  52
FLUX_IVAR_W2               float32           label for field  53
FIBERFLUX_G                float32           label for field  54
FIBERFLUX_R                float32           label for field  55
FIBERFLUX_Z                float32           label for field  56
FIBERTOTFLUX_G             float32           label for field  57
FIBERTOTFLUX_R             float32           label for field  58
FIBERTOTFLUX_Z             float32           label for field  59
SERSIC                     float32           label for field  60
SHAPE_R                    float32           label for field  61
SHAPE_E1                   float32           label for field  62
SHAPE_E2                   float32           label for field  63
PHOTSYS                    char[1]           label for field  64
PRIORITY_INIT              int64             label for field  65
NUMOBS_INIT                int64             label for field  66
SV2_DESI_TARGET            int64             label for field  67
SV2_BGS_TARGET             int64             label for field  68
SV2_MWS_TARGET             int64             label for field  69
SV2_SCND_TARGET            int64             label for field  70
DESI_TARGET                int64             label for field  71
BGS_TARGET                 int64             label for field  72
MWS_TARGET                 int64             label for field  73
PLATE_RA                   float64           label for field  74
PLATE_DEC                  float64           label for field  75
TILEID                     int32             label for field  76
COADD_NUMEXP               int16             label for field  77
COADD_EXPTIME              float32           label for field  78
COADD_NUMNIGHT             int16             label for field  79
COADD_NUMTILE              int16             label for field  80
MEAN_DELTA_X               float32           label for field  81
RMS_DELTA_X                float32           label for field  82
MEAN_DELTA_Y               float32           label for field  83
RMS_DELTA_Y                float32           label for field  84
MEAN_FIBER_RA              float64           label for field  85
STD_FIBER_RA               float32           label for field  86
MEAN_FIBER_DEC             float64           label for field  87
STD_FIBER_DEC              float32           label for field  88
MEAN_PSF_TO_FIBER_SPECFLUX float32           label for field  89
MEAN_FIBER_X               float32           label for field  90
MEAN_FIBER_Y               float32           label for field  91
TSNR2_GPBDARK_B            float32           label for field  92
TSNR2_ELG_B                float32           label for field  93
TSNR2_GPBBRIGHT_B          float32           label for field  94
TSNR2_LYA_B                float32           label for field  95
TSNR2_BGS_B                float32           label for field  96
TSNR2_GPBBACKUP_B          float32           label for field  97
TSNR2_QSO_B                float32           label for field  98
TSNR2_LRG_B                float32           label for field  99
TSNR2_GPBDARK_R            float32           label for field 100
TSNR2_ELG_R                float32           label for field 101
TSNR2_GPBBRIGHT_R          float32           label for field 102
TSNR2_LYA_R                float32           label for field 103
TSNR2_BGS_R                float32           label for field 104
TSNR2_GPBBACKUP_R          float32           label for field 105
TSNR2_QSO_R                float32           label for field 106
TSNR2_LRG_R                float32           label for field 107
TSNR2_GPBDARK_Z            float32           label for field 108
TSNR2_ELG_Z                float32           label for field 109
TSNR2_GPBBRIGHT_Z          float32           label for field 110
TSNR2_LYA_Z                float32           label for field 111
TSNR2_BGS_Z                float32           label for field 112
TSNR2_GPBBACKUP_Z          float32           label for field 113
TSNR2_QSO_Z                float32           label for field 114
TSNR2_LRG_Z                float32           label for field 115
TSNR2_GPBDARK              float32           label for field 116
TSNR2_ELG                  float32           label for field 117
TSNR2_GPBBRIGHT            float32           label for field 118
TSNR2_LYA                  float32           label for field 119
TSNR2_BGS                  float32           label for field 120
TSNR2_GPBBACKUP            float32           label for field 121
TSNR2_QSO                  float32           label for field 122
TSNR2_LRG                  float32           label for field 123
========================== =========== ===== ===================

HDU2
----

EXTNAME = EXP_FIBERMAP

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =======================
KEY    Example Value Type Comment
====== ============= ==== =======================
NAXIS1 162           int  width of table in bytes
NAXIS2 5000          int  number of rows in table
====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

===================== ======= ===== ===================
Name                  Type    Units Description
===================== ======= ===== ===================
TARGETID              int64         label for field   1
PRIORITY              int32         label for field   2
SUBPRIORITY           float64       label for field   3
NIGHT                 int32         label for field   4
EXPID                 int32         label for field   5
MJD                   float64       label for field   6
TILEID                int32         label for field   7
EXPTIME               float64       label for field   8
PETAL_LOC             int16         label for field   9
DEVICE_LOC            int32         label for field  10
LOCATION              int64         label for field  11
FIBER                 int32         label for field  12
FIBERSTATUS           int32         label for field  13
FIBERASSIGN_X         float32       label for field  14
FIBERASSIGN_Y         float32       label for field  15
LAMBDA_REF            float32       label for field  16
PLATE_RA              float64       label for field  17
PLATE_DEC             float64       label for field  18
NUM_ITER              int64         label for field  19
FIBER_X               float64       label for field  20
FIBER_Y               float64       label for field  21
DELTA_X               float64       label for field  22
DELTA_Y               float64       label for field  23
FIBER_RA              float64       label for field  24
FIBER_DEC             float64       label for field  25
PSF_TO_FIBER_SPECFLUX float64       label for field  26
===================== ======= ===== ===================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
