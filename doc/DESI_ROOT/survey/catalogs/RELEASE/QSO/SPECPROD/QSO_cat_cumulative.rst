==================
QSO_cat_cumulative
==================

:Summary: This contains the information on quasar automatically identified from DESI spectra coadded for all observations of the relevant tiles. Data appearing here is considered a successful quasar redshift by the LSS pipeline.
:Naming Convention: ``QSO_cat_{SPECPROD}_cumulative_{VERSION}.fits``.
:Regex: ``QSO_cat_[a-z]+_cumulative_v[0-9]\.fits``
:File Type: FITS, 778 MB

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    Empty
HDU1_  QSO_CAT BINTABLE Quasar Catalog
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = QSO_CAT

This HDU contains all of the information on the identified quasars. Further information could be obtained via a match to other files that contain the columns TARGETID and TILEID.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =======================
    KEY    Example Value Type Comment
    ====== ============= ==== =======================
    NAXIS1 384           int  width of table in bytes
    NAXIS2 2182309       int  number of rows in table
    DESIDR dr1           str  DESI Data Release
    ====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

================== ======= ============ =========================================================================================================
Name               Type    Units        Description
================== ======= ============ =========================================================================================================
TARGETID           int64                Unique DESI target ID
Z                  float64              Redshift measured by Redrock
ZERR               float64              Redshift error from redrock
ZWARN              int64                Redshift warning bitmask from Redrock
LOCATION           int64                Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
COADD_FIBERSTATUS  int32                bitwise-AND of input FIBERSTATUS
TARGET_RA          float64 deg          Barycentric right ascension in ICRS
TARGET_DEC         float64 deg          Barycentric declination in ICRS
EBV                float32 mag          Galactic extinction E(B-V) reddening from SFD98
FLUX_G             float32 nanomaggy    Flux in the Legacy Survey g-band (AB)
FLUX_R             float32 nanomaggy    Flux in the Legacy Survey r-band (AB)
FLUX_Z             float32 nanomaggy    Flux in the Legacy Survey z-band (AB)
FLUX_W1            float32 nanomaggy    WISE flux in W1 (AB)
FLUX_W2            float32 nanomaggy    WISE flux in W2 (AB)
FLUX_IVAR_G        float32 nanomaggy^-2 Inverse variance of FLUX_G (AB)
FLUX_IVAR_R        float32 nanomaggy^-2 Inverse variance of FLUX_R (AB)
FLUX_IVAR_Z        float32 nanomaggy^-2 Inverse variance of FLUX_Z (AB)
FLUX_IVAR_W1       float32 nanomaggy^-2 Inverse variance of FLUX_W1 (AB)
MW_TRANSMISSION_G  float64              Milky Way dust transmission in LS g-band
MW_TRANSMISSION_R  float64              Milky Way dust transmission in LS r-band
MW_TRANSMISSION_Z  float64              Milky Way dust transmission in LS z-band
MW_TRANSMISSION_W1 float64              Milky Way dust transmission in WISE W1
MW_TRANSMISSION_W2 float64              Milky Way dust transmission in WISE W2
PROBA_RF           float64              Probability of being a quasar generated by the quasar Random Forest targeting algorithm.
FLUX_IVAR_W2       float32 nanomaggy^-2 Inverse variance of FLUX_W2 (AB)
MASKBITS           int16                Bitwise mask from the imaging indicating potential issue or blending
CMX_TARGET         int64                Target selection bitmask for commissioning
DESI_TARGET        int64                DESI (dark time program) target selection bitmask
COADD_NUMEXP       int16                Number of exposures in coadd
COADD_EXPTIME      float32 s            Summed exposure time for coadd
SV1_DESI_TARGET    int64                DESI (dark time program) target selection bitmask for SV1
SV2_DESI_TARGET    int64                DESI (dark time program) target selection bitmask for SV2
SV3_DESI_TARGET    int64                DESI (dark time program) target selection bitmask for SV3
SV1_SCND_TARGET    int64                Secondary target selection bitmask for SV1
SV2_SCND_TARGET    int64                Secondary target selection bitmask for SV2
SV3_SCND_TARGET    int64                Secondary target selection bitmask for SV3
SCND_TARGET        int64                Target selection bitmask for secondary programs
TSNR2_LYA          float32              LYA template (S/N)^2 summed over B,R,Z
TSNR2_QSO          float32              QSO template (S/N)^2 summed over B,R,Z
DELTA_CHI2_MGII    float32              Difference of chi2 between redrock fit and MgII fitter over the lambda interval considered during the fit
A_MGII             float32              Fitted parameter A (amplitude) by MgII fitter
SIGMA_MGII         float32 Angstrom     Fitted parameter SIGMA (linewidth) by MgII fitter (in angstrom?)
B_MGII             float32              Fitted parameter B (constant) by MgII fitter
VAR_A_MGII         float32              Variance of MgII fit amplitude parameter A
VAR_SIGMA_MGII     float32              Variance of MgII fit width parameter sigma
VAR_B_MGII         float32              Variance of MgII fit offset parameter B
Z_RR               float32              Redshift collected from redrock file
Z_QN               float32              Redshift measured by QuasarNET using line with highest confidence
C_LYA              float32              Confidence for LyA line, i.e. ~probability to be a QSO
C_CIV              float32              Confidence for CIV line
C_CIII             float32              Confidence for CIII line
C_MgII             float32              Confidence for MgII line
C_Hbeta            float32              Confidence for Hbeta line
C_Halpha           float32              Confidence for Halpha line
Z_LYA              float32              Redshift estimated by QuasarNET with LyA line
Z_CIV              float32              Redshift estimated by QuasarNET with CIV line
Z_CIII             float32              Redshift estimated by QuasarNET with CIII line
Z_MgII             float32              Redshift estimated by QuasarNET with MgII line
Z_Hbeta            float32              Redshift estimated by QuasarNET with Hbeta line
Z_Halpha           float32              Redshift estimated by QuasarNET with Halpha line
QSO_MASKBITS       int32                 QSO Bitwise mask from the imaging indicating potential issue or blending
TILEID             int64                Unique DESI tile ID
LASTNIGHT          int64                Final night of observation included in a series of coadds
PETAL_LOC          int64                Petal location [0-9]
SURVEY             char[7]              Survey name: cmx, sv1, sv2, sv3, main
PROGRAM            char[6]              DESI program type - BRIGHT, DARK, BACKUP, OTHER
MORPHTYPE          char[3]              Imaging Surveys morphological type from Tractor
SPECTYPE           char[6]              Spectral type of Redrock best fit template (e.g. GALAXY, QSO, STAR)
================== ======= ============ =========================================================================================================


Notes and Examples
==================

As of DR1, the selection criteria are the same as described in Chaussidon et al. (2023)
