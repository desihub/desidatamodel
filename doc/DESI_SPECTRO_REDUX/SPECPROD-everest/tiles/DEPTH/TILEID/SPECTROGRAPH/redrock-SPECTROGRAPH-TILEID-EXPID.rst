=======
redrock
=======

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``redrock-7-80610-1xsubset1.fits``, where ... *Give a human readable
    description of the filename, e.g. ``blat-{EXPID}`` where ``{EXPID}``
    is the 8-digit exposure ID.*
:Regex: ``redrock-7-80610-1xsubset1.fits`` *Give a regular expression for this filename.
    For example, a six-digit number would correspond to ``[0-9]{6}``.*
:File Type: FITS, 542 KB  *This section gives the type of the file
    and its approximate size.*

Contents
========

====== ============ ======== ===================
Number EXTNAME      Type     Contents
====== ============ ======== ===================
HDU0_               IMAGE    *Brief Description*
HDU1_  REDSHIFTS    BINTABLE *Brief Description*
HDU2_  FIBERMAP     BINTABLE *Brief Description*
HDU3_  EXP_FIBERMAP BINTABLE *Brief Description*
HDU4_  TSNR2        BINTABLE *Brief Description*
====== ============ ======== ===================


FITS Header Units
=================

HDU0
----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============= ==== ===============
KEY      Example Value Type Comment
======== ============= ==== ===============
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
======== ============= ==== ===============

Empty HDU.

HDU1
----

EXTNAME = REDSHIFTS

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =====================
KEY    Example Value Type Comment
====== ============= ==== =====================
NAXIS1 170           int  length of dimension 1
NAXIS2 500           int  length of dimension 2
====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

========= =========== ===== ===========
Name      Type        Units Description
========= =========== ===== ===========
TARGETID  int64
CHI2      float64
COEFF     float64[10]
Z         float64
ZERR      float64
ZWARN     int64
NPIXELS   int64
SPECTYPE  char[6]
SUBTYPE   char[20]
NCOEFF    int64
DELTACHI2 float64
========= =========== ===== ===========

HDU2
----

EXTNAME = FIBERMAP

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =====================
KEY    Example Value Type Comment
====== ============= ==== =====================
NAXIS1 399           int  length of dimension 1
NAXIS2 500           int  length of dimension 2
====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

========================== ======= ===== ===========
Name                       Type    Units Description
========================== ======= ===== ===========
TARGETID                   int64
PETAL_LOC                  int16
DEVICE_LOC                 int32
LOCATION                   int64
FIBER                      int32
COADD_FIBERSTATUS          int32
TARGET_RA                  float64
TARGET_DEC                 float64
PMRA                       float32
PMDEC                      float32
REF_EPOCH                  float32
LAMBDA_REF                 float32
FA_TARGET                  int64
FA_TYPE                    binary
OBJTYPE                    char[3]
FIBERASSIGN_X              float32
FIBERASSIGN_Y              float32
NUMTARGET                  int16
PRIORITY                   int32
SUBPRIORITY                float64
OBSCONDITIONS              int32
MORPHTYPE                  char[4]
FLUX_G                     float32
FLUX_R                     float32
FLUX_Z                     float32
FLUX_IVAR_G                float32
FLUX_IVAR_R                float32
FLUX_IVAR_Z                float32
REF_ID                     int64
REF_CAT                    char[2]
GAIA_PHOT_G_MEAN_MAG       float32
GAIA_PHOT_BP_MEAN_MAG      float32
GAIA_PHOT_RP_MEAN_MAG      float32
PARALLAX                   float32
EBV                        float32
FLUX_W1                    float32
FLUX_W2                    float32
FIBERFLUX_G                float32
FIBERFLUX_R                float32
FIBERFLUX_Z                float32
FIBERTOTFLUX_G             float32
FIBERTOTFLUX_R             float32
FIBERTOTFLUX_Z             float32
MASKBITS                   int16
SERSIC                     float32
SHAPE_R                    float32
SHAPE_E1                   float32
SHAPE_E2                   float32
PHOTSYS                    char[1]
SV1_DESI_TARGET            int64
SV1_BGS_TARGET             int64
SV1_MWS_TARGET             int64
PRIORITY_INIT              int64
NUMOBS_INIT                int64
RELEASE                    int32
BRICKID                    int32
BRICKNAME                  char[8]
BRICK_OBJID                int32
BLOBDIST                   float32
FIBERFLUX_IVAR_G           float32
FIBERFLUX_IVAR_R           float32
FIBERFLUX_IVAR_Z           float32
DESI_TARGET                int64
BGS_TARGET                 int64
MWS_TARGET                 int64
HPXPIXEL                   int64
PLATE_RA                   float64
PLATE_DEC                  float64
TILEID                     int32
COADD_NUMEXP               int16
COADD_EXPTIME              float32
COADD_NUMNIGHT             int16
COADD_NUMTILE              int16
MEAN_DELTA_X               float32
RMS_DELTA_X                float32
MEAN_DELTA_Y               float32
RMS_DELTA_Y                float32
MEAN_FIBER_RA              float64
STD_FIBER_RA               float32
MEAN_FIBER_DEC             float64
STD_FIBER_DEC              float32
MEAN_PSF_TO_FIBER_SPECFLUX float32
MEAN_FIBER_X               float32
MEAN_FIBER_Y               float32
========================== ======= ===== ===========

HDU3
----

EXTNAME = EXP_FIBERMAP

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =====================
KEY    Example Value Type Comment
====== ============= ==== =====================
NAXIS1 162           int  length of dimension 1
NAXIS2 1000          int  length of dimension 2
====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

===================== ======= ===== ===========
Name                  Type    Units Description
===================== ======= ===== ===========
TARGETID              int64
PRIORITY              int32
SUBPRIORITY           float64
NIGHT                 int32
EXPID                 int32
MJD                   float64
TILEID                int32
EXPTIME               float64
PETAL_LOC             int16
DEVICE_LOC            int32
LOCATION              int64
FIBER                 int32
FIBERSTATUS           int32
FIBERASSIGN_X         float32
FIBERASSIGN_Y         float32
LAMBDA_REF            float32
PLATE_RA              float64
PLATE_DEC             float64
NUM_ITER              int64
FIBER_X               float64
FIBER_Y               float64
DELTA_X               float64
DELTA_Y               float64
FIBER_RA              float64
FIBER_DEC             float64
PSF_TO_FIBER_SPECFLUX float64
===================== ======= ===== ===========

HDU4
----

EXTNAME = TSNR2

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =====================
KEY    Example Value Type Comment
====== ============= ==== =====================
NAXIS1 136           int  length of dimension 1
NAXIS2 500           int  length of dimension 2
====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

================= ======= ===== ===========
Name              Type    Units Description
================= ======= ===== ===========
TARGETID          int64
TSNR2_GPBDARK_B   float32
TSNR2_ELG_B       float32
TSNR2_GPBBRIGHT_B float32
TSNR2_LYA_B       float32
TSNR2_BGS_B       float32
TSNR2_GPBBACKUP_B float32
TSNR2_QSO_B       float32
TSNR2_LRG_B       float32
TSNR2_GPBDARK_R   float32
TSNR2_ELG_R       float32
TSNR2_GPBBRIGHT_R float32
TSNR2_LYA_R       float32
TSNR2_BGS_R       float32
TSNR2_GPBBACKUP_R float32
TSNR2_QSO_R       float32
TSNR2_LRG_R       float32
TSNR2_GPBDARK_Z   float32
TSNR2_ELG_Z       float32
TSNR2_GPBBRIGHT_Z float32
TSNR2_LYA_Z       float32
TSNR2_BGS_Z       float32
TSNR2_GPBBACKUP_Z float32
TSNR2_QSO_Z       float32
TSNR2_LRG_Z       float32
TSNR2_GPBDARK     float32
TSNR2_ELG         float32
TSNR2_GPBBRIGHT   float32
TSNR2_LYA         float32
TSNR2_BGS         float32
TSNR2_GPBBACKUP   float32
TSNR2_QSO         float32
TSNR2_LRG         float32
================= ======= ===== ===========


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
