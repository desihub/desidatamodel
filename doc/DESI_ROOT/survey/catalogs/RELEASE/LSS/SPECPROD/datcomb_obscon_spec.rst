==============================
datcomb_obscon_spec_zdone.fits
==============================

:Summary: Compilation of spectroscopic reduction
:Naming Convention: ``datcomb_{obscon}_spec_zdone.fits``, where obscon can be either dark or bright
:Regex: ``datcomb_(bright|dark)_spec_zdone\.fits``
:File Type: FITS, 4 GB

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

Selected columns from the cumulative tiles-based redshift catalogs (CROSS-REF) for the dark/bright program, selecting the data from fiber positioners available to science targets, and joining with the zmtl information (CROSS-REF) for each tile, which is used downstream to select observations that used "good hardware".

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ============= ============= ==== =====================
    KEY           Example Value Type Comment
    ============= ============= ==== =====================
    NAXIS1        372           int  length of dimension 1
    NAXIS2        11632889      int  length of dimension 2
    LONGSTRN [1]_ OGIP 1.0      str
    SPGRP [1]_    cumulative    str
    SURVEY [1]_   main          str
    PROGRAM [1]_  dark          str
    ZCATVER [1]_  v0            str
    DESIDR        dr1           str  DESI Data Release
    ============= ============= ==== =====================

.. [1] Optional

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

========================== =========== ===== ===============================================================================================================================
Name                       Type        Units Description
========================== =========== ===== ===============================================================================================================================
TARGETID                   int64             Unique DESI target ID
LASTNIGHT                  int32             Final night of observation included in a series of coadds
Z                          float64           Redshift measured by Redrock
ZERR                       float64           Redshift error from redrock
ZWARN                      int64             Redshift warning bitmask from Redrock
CHI2                       float64           Best fit chi squared
COEFF                      float64[10]       Redrock template coefficients
NPIXELS                    int64             Number of unmasked pixels contributing to the Redrock fit
SPECTYPE                   char[6]           Spectral type of Redrock best fit template (e.g. GALAXY, QSO, STAR)
SUBTYPE                    char[20]          Spectral subtype
NCOEFF                     int64             Number of Redrock template coefficients
DELTACHI2                  float64           chi2 difference between first- and second-best redrock template fits
LOCATION                   int64             Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBER                      int32             Fiber ID on the CCDs [0-4999]
COADD_FIBERSTATUS          int32             bitwise-AND of input FIBERSTATUS
TARGET_RA                  float64     deg   Barycentric right ascension in ICRS
TARGET_DEC                 float64     deg   Barycentric declination in ICRS
FIBERASSIGN_X              float32     mm    Fiberassign expected CS5 X location on focal plane
FIBERASSIGN_Y              float32     mm    Fiberassign expected CS5 Y location on focal plane
PRIORITY                   int32             Target current priority
DESI_TARGET                int64             DESI (dark time program) target selection bitmask
BGS_TARGET                 int64             BGS (Bright Galaxy Survey) target selection bitmask
TILEID                     int32             Unique DESI tile ID
COADD_NUMEXP               int16             Number of exposures in coadd
COADD_EXPTIME              float32     s     Summed exposure time for coadd
COADD_NUMNIGHT             int16             Number of nights in coadd
MEAN_DELTA_X               float32     mm    Mean (over exposures) fiber difference requested - actual CS5 X location on focal plane
RMS_DELTA_X                float32     mm    RMS (over exposures) of the fiber difference between measured and requested CS5 X location on focal plane
MEAN_DELTA_Y               float32     mm    Mean (over exposures) fiber difference requested - actual CS5 Y location on focal plane
RMS_DELTA_Y                float32     mm    RMS (over exposures) of the fiber difference between measured and requested CS5 Y location on focal plane
MEAN_PSF_TO_FIBER_SPECFLUX float32           Mean of input exposures fraction of light from point-like source captured by 1.5 arcsec diameter fiber given atmospheric seeing
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
Z_QN                       float64           Redshift measured by QuasarNET using line with highest confidence
Z_QN_CONF                  float64           Redshift confidence from QuasarNET
IS_QSO_QN                  int16             Spectroscopic classification from QuasarNET (1 for a quasar)
========================== =========== ===== ===============================================================================================================================


Notes and Examples
==================


