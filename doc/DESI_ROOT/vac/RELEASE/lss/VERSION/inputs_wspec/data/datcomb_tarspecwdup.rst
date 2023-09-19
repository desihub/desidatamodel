===================================
datcomb_tarspecwdup_Alltiles
===================================

:Summary: Match of targets (with duplicates after FA) with spectroscopic data from the specprod (fuji/guadalupe for SV3/DA02).
:Naming Convention: ``datcomb_{PROGRAM}_tarspecwdup_Alltiles.fits``, where ``{PROGRAM}`` denotes the observing program, either ``dark`` or ``bright``.
:Regex: ``datcomb_[a-z]{4,6}_tarspecwdup_Alltiles.fits``
:File Type: FITS, 2 GB

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

*Match catalog between spectroscopic information and duplicate targets after running fiber assigments*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ============= ==== =======================
    KEY      Example Value Type Comment
    ======== ============= ==== =======================
    NAXIS1   499           int  width of table in bytes
    NAXIS2   4461559       int  number of rows in table
    DESIDR   edr           str  DESI Data Release
    ======== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

========================== =========== ========= ===============================================================================================================================
Name                       Type        Units     Description
========================== =========== ========= ===============================================================================================================================
RA                         float64     deg       Target Right Ascension
DEC                        float64     deg       Target declination
REF_EPOCH [1]_             float32     yr        Reference epoch for Gaia/Tycho astrometry. Typically 2015.5 for Gaia
PARALLAX [1]_              float32     mas       Reference catalog parallax
PMRA [1]_                  float32     mas yr^-1 proper motion in the +RA direction (already including cos(dec))
PMDEC [1]_                 float32     mas yr^-1 Proper motion in the +Dec direction
TARGETID                   int64                 Unique DESI target ID
OBSCONDITIONS [1]_         int32                 Bitmask of allowed observing conditions
PRIORITY_INIT              int64                 Target initial priority from target selection bitmasks and OBSCONDITIONS
NUMOBS_INIT [1]_           int64                 Initial number of observations for target calculated across target selection bitmasks and OBSCONDITIONS
NUMOBS_MORE [1]_           int64                 Number of additional observations needed
NUMOBS [1]_                int64                 Number of spectroscopic observations (on this specific, single tile)
ZWARN_MTL                  int64                 The ZWARN from the zmtl file (contains extra bits)
ZTILEID [1]_               int32                 ID of tile that most recently updated target's state
TARGET_STATE               char[30]              Combination of target class and its current observational state
TIMESTAMP                  char[25]    s         UTC/ISO time at which the target state was updated
VERSION [1]_               char[14]              Tag of desitarget used to create the target catalog
PRIORITY                   int64                 Target current priority
LOCATION                   int64                 Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
TILEID                     int64                 Unique DESI tile ID
TILELOCID                  int64                 Is 10000*TILEID+LOCATION
Z                          float64               Redshift measured by Redrock
ZERR                       float64               Redshift error from redrock
ZWARN                      int64                 Redshift warning bitmask from Redrock
CHI2                       float64               Best fit chi squared
COEFF                      float64[10]           Redrock template coefficients
NPIXELS                    int64                 Number of unmasked pixels contributing to the Redrock fit
SPECTYPE                   char[6]               Spectral type of Redrock best fit template (e.g. GALAXY, QSO, STAR)
SUBTYPE                    char[20]              Spectral subtype
NCOEFF                     int64                 Number of Redrock template coefficients
DELTACHI2                  float64               chi2 difference between first- and second-best redrock template fits
FIBER                      int32                 Fiber ID on the CCDs [0-4999]
COADD_FIBERSTATUS          int32                 bitwise-AND of input FIBERSTATUS
FIBERASSIGN_X              float32     mm        Fiberassign expected CS5 X location on focal plane
FIBERASSIGN_Y              float32     mm        Fiberassign expected CS5 Y location on focal plane
COADD_NUMEXP               int16                 Number of exposures in coadd
COADD_EXPTIME              float32     s         Summed exposure time for coadd
COADD_NUMNIGHT             int16                 Number of nights in coadd
MEAN_DELTA_X               float32     mm        Mean (over exposures) fiber difference requested - actual CS5 X location on focal plane
RMS_DELTA_X                float32     mm        RMS (over exposures) of the fiber difference between measured and requested CS5 X location on focal plane
MEAN_DELTA_Y               float32     mm        Mean (over exposures) fiber difference requested - actual CS5 Y location on focal plane
RMS_DELTA_Y                float32     mm        RMS (over exposures) of the fiber difference between measured and requested CS5 Y location on focal plane
MEAN_PSF_TO_FIBER_SPECFLUX float32               Mean of input exposures fraction of light from point-like source captured by 1.5 arcsec diameter fiber given atmospheric seeing
TSNR2_ELG_B                float32               ELG B template (S/N)^2
TSNR2_LYA_B                float32               LYA B template (S/N)^2
TSNR2_BGS_B                float32               BGS B template (S/N)^2
TSNR2_QSO_B                float32               QSO B template (S/N)^2
TSNR2_LRG_B                float32               LRG B template (S/N)^2
TSNR2_ELG_R                float32               ELG R template (S/N)^2
TSNR2_LYA_R                float32               LYA R template (S/N)^2
TSNR2_BGS_R                float32               BGS R template (S/N)^2
TSNR2_QSO_R                float32               QSO R template (S/N)^2
TSNR2_LRG_R                float32               LRG R template (S/N)^2
TSNR2_ELG_Z                float32               ELG Z template (S/N)^2
TSNR2_LYA_Z                float32               LYA Z template (S/N)^2
TSNR2_BGS_Z                float32               BGS Z template (S/N)^2
TSNR2_QSO_Z                float32               QSO Z template (S/N)^2
TSNR2_LRG_Z                float32               LRG Z template (S/N)^2
TSNR2_ELG                  float32               ELG template (S/N)^2 summed over B,R,Z
TSNR2_LYA                  float32               LYA template (S/N)^2 summed over B,R,Z
TSNR2_BGS                  float32               BGS template (S/N)^2 summed over B,R,Z
TSNR2_QSO                  float32               QSO template (S/N)^2 summed over B,R,Z
TSNR2_LRG                  float32               LRG template (S/N)^2 summed over B,R,Z
SV3_DESI_TARGET            int64                 DESI (dark time program) target selection bitmask for SV3
SV3_BGS_TARGET             int64                 BGS (bright time program) target selection bitmask for SV3
SV3_MWS_TARGET             int64                 MWS (bright time program) target selection bitmask for SV3
========================== =========== ========= ===============================================================================================================================

.. [1] Optional
