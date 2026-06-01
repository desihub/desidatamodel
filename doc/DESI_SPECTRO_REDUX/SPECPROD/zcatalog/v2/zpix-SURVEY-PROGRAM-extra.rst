==============================
zpix-SURVEY-PROGRAM-extra.fits
==============================

:Summary: All remaining columns from the healpix-based redshift catalogs not
          included in the core or imaging files, one file per SURVEY and PROGRAM.
          Includes full Redrock output, TSNR2 scores, emission line fits,
          QuasarNET results, and per-tracer quality flags.
:Naming Convention: ``zpix-SURVEY-PROGRAM-extra.fits``, where ``SURVEY`` is
    *e.g.* ``main`` or ``sv1`` and ``PROGRAM`` is *e.g.* ``bright`` or ``dark``.
:Regex: ``zpix-(cmx|main|sv1|sv2|sv3|special)-(backup|bright|dark|other)-extra\.fits``
:File Type: FITS, ~500 MB

Contents
========

====== =============== ======== ============================================================
Number EXTNAME         Type     Contents
====== =============== ======== ============================================================
HDU0_  PRIMARY         IMAGE    Empty
HDU1_  ZCATALOG_EXTRA  BINTABLE All extra columns not in core or imaging files
====== =============== ======== ============================================================


FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ============ ================ ==== =======================
    KEY          Example Value    Type Comment
    ============ ================ ==== =======================
    CHECKSUM     9aaGCVYE9aaECUYE str  HDU checksum
    DATASUM      0                str  data unit checksum
    ZCATVER      v2               str  Version of zcatalog files
    ============ ================ ==== =======================

Empty HDU.

HDU1
----

EXTNAME = ZCATALOG_EXTRA

All columns not included in the core
:doc:`zpix-SURVEY-PROGRAM.fits <./zpix-SURVEY-PROGRAM>` or imaging
:doc:`zpix-SURVEY-PROGRAM-imaging.fits <./zpix-SURVEY-PROGRAM-imaging>` files.
Rows are in the same order and correspond 1-to-1 with the ZCATALOG HDU.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ============ ================ ==== =======================
    KEY          Example Value    Type Comment
    ============ ================ ==== =======================
    NAXIS1       870              int  width of table in bytes
    NAXIS2       139728           int  number of rows in table
    RRVER        0.15.0           str  Redrock version
    SURVEY [1]_  main             str  DESI sub-survey (e.g. sv1, sv3, main)
    PROGRAM [1]_ dark             str  DESI program (e.g. dark, bright)
    CHECKSUM     QA6lQ26iQ96iQ96i str  HDU checksum
    DATASUM      4284326946       str  data unit checksum
    ZCATVER      v2               str  Version of zcatalog files
    ============ ================ ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

========================== =========== ======== =====================================================================================================================================
Name                       Type        Units    Description
========================== =========== ======== =====================================================================================================================================
TARGETID                   int64                Unique DESI target ID
HEALPIX                    int32                HEALPixel containing this location at NSIDE=64 in the NESTED scheme
SPGRPVAL                   int32                Value by which spectra are grouped for a coadd (healpixel number for healpix coadds)
Z                          float64              Redshift measured by Redrock
ZERR                       float32              Redshift error from Redrock
ZWARN                      int32                Redshift warning bitmask from Redrock
CHI2                       float32              Best fit chi squared
COEFF                      float32[10]          Redrock template coefficients
NPIXELS                    int32                Number of unmasked pixels contributing to the Redrock fit
SPECTYPE                   char[6]              Spectral type of Redrock best fit template (e.g. GALAXY, QSO, STAR)
SUBTYPE                    char[3]              Spectral subtype
NCOEFF                     int16                Number of Redrock template coefficients
DELTACHI2                  float32              chi2 difference between first- and second-best redrock template fits
COEFF_BEST                 float32[10]          Redrock template coefficients for Z_BEST fit
SUBPRIORITY                float64              Random subpriority [0-1] to break assignment ties
FA_TARGET                  int64                Targeting bit internally used by fiberassign (linked with FA_TYPE)
FA_TYPE                    binary               Fiberassign internal target type (science, standard, sky, safe, suppsky)
OBSCONDITIONS              int16                Flag the target to be observed in graytime
PRIORITY_INIT              int64                Target initial priority from target selection bitmasks and OBSCONDITIONS
NUMOBS_INIT                int64                Initial number of observations for target calculated across target selection bitmasks and OBSCONDITIONS
PLATE_RA                   float64     deg      Barycentric Right Ascension in ICRS to be used by PlateMaker
PLATE_DEC                  float64     deg      Barycentric Declination in ICRS to be used by PlateMaker
LAMBDA_REF                 float32     Angstrom Requested wavelength at which targets should be centered on fibers
DEVICE_LOC                 int16                Device location on focal plane [0-523]
LOCATION                   int16                Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FITMETHOD                  char[4]              Redshift fitting method (e.g. PCA)
MEAN_DELTA_X               float32     mm       Mean (over exposures) fiber difference requested - actual CS5 X location on focal plane
RMS_DELTA_X                float32     mm       RMS (over exposures) of the fiber difference between measured and requested CS5 X location on focal plane
MEAN_DELTA_Y               float32     mm       Mean (over exposures) fiber difference requested - actual CS5 Y location on focal plane
RMS_DELTA_Y                float32     mm       RMS (over exposures) of the fiber difference between measured and requested CS5 Y location on focal plane
MEAN_PSF_TO_FIBER_SPECFLUX float32              Mean of input exposures fraction of light from point-like source captured by 1.5 arcsec diameter fiber given atmospheric seeing
MEAN_FIBER_RA              float64     deg      Mean (over exposures) RA of actual fiber position
STD_FIBER_RA               float32     arcsec   Standard deviation (over exposures) of RA of actual fiber position
MEAN_FIBER_DEC             float64     deg      Mean (over exposures) DEC of actual fiber position
STD_FIBER_DEC              float32     arcsec   Standard deviation (over exposures) of DEC of actual fiber position
MEAN_FIBER_X               float32     mm       Mean (over exposures) fiber CS5 X location on focal plane
MEAN_FIBER_Y               float32     mm       Mean (over exposures) fiber CS5 Y location on focal plane
TSNR2_GPBDARK_B            float32              template (S/N)^2 for dark targets in guider pass band on B
TSNR2_ELG_B                float32              ELG B template (S/N)^2
TSNR2_GPBBRIGHT_B          float32              template (S/N)^2 for bright targets in guider pass band on B
TSNR2_LYA_B                float32              LYA B template (S/N)^2
TSNR2_BGS_B                float32              BGS B template (S/N)^2
TSNR2_GPBBACKUP_B          float32              template (S/N)^2 for backup targets in guider pass band on B
TSNR2_QSO_B                float32              QSO B template (S/N)^2
TSNR2_LRG_B                float32              LRG B template (S/N)^2
TSNR2_GPBDARK_R            float32              template (S/N)^2 for dark targets in guider pass band on R
TSNR2_ELG_R                float32              ELG R template (S/N)^2
TSNR2_GPBBRIGHT_R          float32              template (S/N)^2 for bright targets in guider pass band on R
TSNR2_LYA_R                float32              LYA R template (S/N)^2
TSNR2_BGS_R                float32              BGS R template (S/N)^2
TSNR2_GPBBACKUP_R          float32              template (S/N)^2 for backup targets in guider pass band on R
TSNR2_QSO_R                float32              QSO R template (S/N)^2
TSNR2_LRG_R                float32              LRG R template (S/N)^2
TSNR2_GPBDARK_Z            float32              template (S/N)^2 for dark targets in guider pass band on Z
TSNR2_ELG_Z                float32              ELG Z template (S/N)^2
TSNR2_GPBBRIGHT_Z          float32              template (S/N)^2 for bright targets in guider pass band on Z
TSNR2_LYA_Z                float32              LYA Z template (S/N)^2
TSNR2_BGS_Z                float32              BGS Z template (S/N)^2
TSNR2_GPBBACKUP_Z          float32              template (S/N)^2 for backup targets in guider pass band on Z
TSNR2_QSO_Z                float32              QSO Z template (S/N)^2
TSNR2_LRG_Z                float32              LRG Z template (S/N)^2
TSNR2_GPBDARK              float32              template (S/N)^2 for dark targets in guider pass band
TSNR2_ELG                  float32              ELG template (S/N)^2 summed over B,R,Z
TSNR2_GPBBRIGHT            float32              template (S/N)^2 for bright targets in guider pass band
TSNR2_LYA                  float32              LYA template (S/N)^2 summed over B,R,Z
TSNR2_BGS                  float32              BGS template (S/N)^2 summed over B,R,Z
TSNR2_GPBBACKUP            float32              template (S/N)^2 for backup targets in guider pass band
TSNR2_QSO                  float32              QSO template (S/N)^2 summed over B,R,Z
TSNR2_LRG                  float32              LRG template (S/N)^2 summed over B,R,Z
OII_FLUX                   float32              [OII] doublet flux from emission line fit
OII_FLUX_IVAR              float32              Inverse variance of OII_FLUX
IS_QSO_MGII                logical              True if this object is classified as a QSO by the MgII afterburner
IS_QSO_QN_NEW_RR           logical              True if QuasarNET classification differs from Redrock and target is a QSO
C_LYA                      float32              QuasarNET confidence for Lyman-alpha line
C_CIV                      float32              QuasarNET confidence for CIV line
C_CIII                     float32              QuasarNET confidence for CIII line
C_MgII                     float32              QuasarNET confidence for MgII line
C_Hbeta                    float32              QuasarNET confidence for H-beta line
C_Halpha                   float32              QuasarNET confidence for H-alpha line
Z_NEW                      float64              QuasarNET redshift (when IS_QSO_QN_NEW_RR is True)
ZERR_NEW                   float64              QuasarNET redshift error
ZWARN_NEW                  int64                Redshift warning bitmask for QuasarNET redshift
SPECTYPE_NEW               char[6]              Spectral type from QuasarNET fit
SUBTYPE_NEW                char[20]             Spectral subtype from QuasarNET fit
CHI2_NEW                   float64              Chi squared for QuasarNET fit
DELTACHI2_NEW              float64              Delta chi2 for QuasarNET fit
COEFF_NEW                  float64[10]          Template coefficients for QuasarNET fit
GOOD_Z_BGS                 logical              True if BGS target with high-confidence redshift passing LSS quality cuts
GOOD_Z_LRG                 logical              True if LRG target with high-confidence redshift passing LSS quality cuts
GOOD_Z_ELG                 logical              True if ELG target with high-confidence redshift passing LSS quality cuts
GOOD_Z_QSO                 logical              True if QSO target with high-confidence redshift (Z_QSO) passing LSS quality cuts
Z_QSO                      float64              QuasarNET-corrected QSO redshift (used in GOOD_Z_QSO evaluation)
ZERR_QSO                   float32              Error on Z_QSO
========================== =========== ======== =====================================================================================================================================

.. [1] Optional
