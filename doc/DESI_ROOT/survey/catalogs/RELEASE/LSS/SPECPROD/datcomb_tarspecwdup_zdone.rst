====================================
datcomb TARGET zdone wdup
====================================

:Summary: Match of targets (with duplicates after FA) with spectroscopic data from the specprod.
:Naming Convention: ``datcomb_{TARGET}_tarspecwdup_zdone.fits``, where {TARGET} is the target type, like BGS_ANY or BGS_BRIGHT in bright program and like ELG_LOPnotqso, LRG or QSO in dark program
:Regex: ``datcomb_[a-z]_tarspecwdup_zdone.fits`` 
:File Type: FITS, 6 GB 

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

Match catalog between spectroscopic information and duplicate targets after running fiber assigments

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ============= ==== =====================
    KEY      Example Value Type Comment
    ======== ============= ==== =====================
    NAXIS1   463           int  length of dimension 1
    NAXIS2   13947971      int  length of dimension 2
    DESIDR   dr1           str  DESI Data Release
    ======== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

========================== =========== ===== ===============================================================================================================================
Name                       Type        Units Description
========================== =========== ===== ===============================================================================================================================
RA                         float64     deg   Barycentric Right Ascension in ICRS
DEC                        float64     deg   Barycentric declination in ICRS
TARGETID                   int64             Unique DESI target ID
DESI_TARGET                int64             DESI (dark time program) target selection bitmask
BGS_TARGET                 int64             BGS (Bright Galaxy Survey) target selection bitmask
MWS_TARGET                 int64             Milky Way Survey targeting bits
SUBPRIORITY                float64           Random subpriority [0-1) to break assignment ties
PRIORITY_INIT              int64             Target initial priority from target selection bitmasks and OBSCONDITIONS
TARGET_STATE               char[30]          Combination of target class and its current observational state
TIMESTAMP                  char[25]    s     UTC/ISO time at which the target state was updated
LOCATION                   int64             Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
TILEID                     int64             Unique DESI tile ID
TILELOCID                  int64             Is 10000*TILEID+LOCATION
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
FIBER                      int32             Fiber ID on the CCDs [0-4999]
COADD_FIBERSTATUS          int32             bitwise-AND of input FIBERSTATUS
FIBERASSIGN_X              float32     mm    Fiberassign expected CS5 X location on focal plane
FIBERASSIGN_Y              float32     mm    Fiberassign expected CS5 Y location on focal plane
PRIORITY                   int32             Target current priority
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

