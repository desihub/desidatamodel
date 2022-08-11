==============================
datcomb_dark_tarspecwdup_zdone
==============================

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``datcomb_dark_tarspecwdup_zdone.fits``, where ... *Give a human readable
    description of the filename, e.g. ``blat-{EXPID}`` where ``{EXPID}``
    is the 8-digit exposure ID.*
:Regex: ``datcomb_dark_tarspecwdup_zdone.fits`` *Give a regular expression for this filename.
    For example, a six-digit number would correspond to ``[0-9]{6}``.*
:File Type: FITS, 3 GB  *This section gives the type of the file
    and its approximate size.*

Contents
========

====== ======== ======== ===================
Number EXTNAME  Type     Contents
====== ======== ======== ===================
HDU0_           IMAGE    *Brief Description*
HDU1_  ZCATALOG BINTABLE *Brief Description*
====== ======== ======== ===================


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

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ========================= ===== =====================
    KEY      Example Value             Type  Comment
    ======== ========================= ===== =====================
    NAXIS1   463                       int   length of dimension 1
    NAXIS2   7528042                   int   length of dimension 2
    TILEID   1824                      int
    TILERA   327.055                   float
    TILEDEC  -1.253                    float
    FIELDROT -0.0677254831640627       float
    FA_PLAN  2022-07-01T00:00:00.000   str
    FA_HA    -1.65                     float
    FA_RUN   2021-05-30T15:35:53+00:00 str
    REQRA    327.055                   float
    REQDEC   -1.253                    float
    FIELDNUM 0                         int
    FA_VER   5.0.0                     str
    FA_SURV  main                      str
    FA_M_GFA 0.4                       float
    FA_M_PET 0.4                       float
    FA_M_POS 0.05                      float
    LONGSTRN OGIP 1.0                  str
    RRVER    0.15.2                    str
    TEMNAM00 GALAXY                    str
    TEMVER00 2.6                       str
    TEMNAM01 QSO                       str
    TEMVER01 0.1                       str
    TEMNAM02 STAR:::A                  str
    TEMVER02 0.1                       str
    TEMNAM03 STAR:::B                  str
    TEMVER03 0.1                       str
    TEMNAM04 STAR:::CV                 str
    TEMVER04 0.1                       str
    TEMNAM05 STAR:::F                  str
    TEMVER05 0.1                       str
    TEMNAM06 STAR:::G                  str
    TEMVER06 0.1                       str
    TEMNAM07 STAR:::K                  str
    TEMVER07 0.1                       str
    TEMNAM08 STAR:::M                  str
    TEMVER08 0.1                       str
    TEMNAM09 STAR:::WD                 str
    TEMVER09 0.1                       str
    SPGRP    cumulative                str
    SURVEY   main                      str
    PROGRAM  dark                      str
    ======== ========================= ===== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

========================== =========== ===== =========================================================================================================
Name                       Type        Units Description
========================== =========== ===== =========================================================================================================
RA                         float64           Right Ascension
DEC                        float64           Declination
TARGETID                   int64             Unique DESI target ID
DESI_TARGET                int64             Dark survey + calibration targeting bits
BGS_TARGET                 int64             Bright Galaxy Survey targeting bits
MWS_TARGET                 int64             Milky Way Survey targeting bits
SUBPRIORITY                float64           Random subpriority [0-1] to break assignment ties
PRIORITY_INIT              int64             Target initial priority from target selection bitmasks and OBSCONDITIONS
TARGET_STATE               char[30]          Combination of target class and its current observational state
TIMESTAMP                  char[25]          UTC/ISO time at which the target state was updated
PRIORITY                   int64             Target current priority
FIBER                      int32             Fiber ID on the CCDs [0-4999]
LOCATION                   int64             Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
TILEID                     int64             Unique DESI tile ID
TILELOCID                  int64             Is 10000*TILEID+LOCATION
Z                          float64           Redshift measured by Redrock
ZERR                       float64           Redshift error from redrock
ZWARN                      int64             Redshift warning bitmask measured by Redrock
CHI2                       float64           Best fit :math:`\chi^2`
COEFF                      float64[10]       Redrock template coefficients
NPIXELS                    int64
SPECTYPE                   char[6]           Spectype from redrock file
SUBTYPE                    char[20]          Spectral subtype
NCOEFF                     int64
DELTACHI2                  float64           Delta-chi-squared for template fit from Redrock
COADD_FIBERSTATUS          int32
FIBERASSIGN_X              float32           Expected CS5 X location on focal plane
FIBERASSIGN_Y              float32           Expected CS5 Y location on focal plane
COADD_NUMEXP               int16
COADD_EXPTIME              float32
COADD_NUMNIGHT             int16
MEAN_DELTA_X               float32           Mean (over exposures) fiber difference between measured and requested CS5 X location on focal plane
RMS_DELTA_X                float32           RMS (over exposures) of the fiber difference between measured and requested CS5 X location on focal plane
MEAN_DELTA_Y               float32           Mean (over exposures) fiber CS5 Y location on focal plane
RMS_DELTA_Y                float32           RMS (over exposures) of the fiber difference between measured and requested CS5 Y location on focal plane
MEAN_PSF_TO_FIBER_SPECFLUX float32
TSNR2_ELG_B                float32           ELG B template (S/N)^2
TSNR2_LYA_B                float32           LYA B template (S/N)^2
TSNR2_BGS_B                float32           BGS B template (S/N)^2
TSNR2_QSO_B                float32           QSO B template (S/N)^2
TSNR2_LRG_B                float32           LRG B template (S/N)^2
TSNR2_ELG_R                float32           ELG R template (S/N)^2
TSNR2_LYA_R                float32           LYA R template (S/N)^2
TSNR2_BGS_R                float32           BGS R template (S/N)^2
TSNR2_QSO_R                float32           QSO R template (S/N)^2
TSNR2_LRG_R                float32           LRG R template (S/N)^2
TSNR2_ELG_Z                float32           ELG Z template (S/N)^2
TSNR2_LYA_Z                float32           LYA Z template (S/N)^2
TSNR2_BGS_Z                float32           BGS Z template (S/N)^2
TSNR2_QSO_Z                float32           QSO Z template (S/N)^2
TSNR2_LRG_Z                float32           LRG Z template (S/N)^2
TSNR2_ELG                  float32           ELG template (S/N)^2 summed over B,R,Z
TSNR2_LYA                  float32           LYA template (S/N)^2 summed over B,R,Z
TSNR2_BGS                  float32           BGS template (S/N)^2 summed over B,R,Z
TSNR2_QSO                  float32           QSO template (S/N)^2 summed over B,R,Z
TSNR2_LRG                  float32           LRG template (S/N)^2 summed over B,R,Z
ZWARN_MTL                  int64             The ZWARN from the zmtl file (contains extra bits)
Z_QN                       float64           Redshift measured by QuasarNET
Z_QN_CONF                  float64           Redshift confidence from QuasarNET
IS_QSO_QN                  int16             Spectroscopic classification from QuasarNET (1 for a quasar)
========================== =========== ===== =========================================================================================================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
