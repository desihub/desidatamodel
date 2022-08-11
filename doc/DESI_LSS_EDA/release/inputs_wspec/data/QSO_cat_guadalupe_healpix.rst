=========================
QSO_cat_guadalupe_healpix
=========================

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``QSO_cat_guadalupe_healpix.fits``, where ... *Give a human readable
    description of the filename, e.g. ``blat-{EXPID}`` where ``{EXPID}``
    is the 8-digit exposure ID.*
:Regex: ``QSO_cat_guadalupe_healpix.fits`` *Give a regular expression for this filename.
    For example, a six-digit number would correspond to ``[0-9]{6}``.*
:File Type: FITS, 106 MB  *This section gives the type of the file
    and its approximate size.*

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    *Brief Description*
HDU1_  QSO_CAT BINTABLE *Brief Description*
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

*Summarize the contents of this HDU.*

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = QSO_CAT

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =======================
    KEY    Example Value Type Comment
    ====== ============= ==== =======================
    NAXIS1 360           int  width of table in bytes
    NAXIS2 297881        int  number of rows in table
    ====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

================== =========== ===== ====================================================================
Name               Type        Units Description
================== =========== ===== ====================================================================
TARGETID           int64             Unique DESI target ID
Z                  float64           Redshift measured by Redrock
ZERR               float64           Redshift error from redrock
ZWARN              int64             Redshift warning bitmask measured by Redrock
SPECTYPE           char stream       Spectype from redrock file
COADD_FIBERSTATUS  int32
TARGET_RA          float64           Target right ascension
TARGET_DEC         float64           Target declination
MORPHTYPE          char stream       Imaging Surveys morphological type
EBV                float32           Galactic extinction E(B-V) reddening from SFD98
FLUX_G             float32           Flux in the Legacy Survey g-band (AB)
FLUX_R             float32           Flux in the Legacy Survey r-band (AB)
FLUX_Z             float32           Flux in the Legacy Survey z-band (AB)
FLUX_W1            float32           WISE flux in W1 (AB)
FLUX_W2            float32           WISE flux in W2 (AB)
FLUX_IVAR_G        float32           Inverse variance of FLUX_G (AB)
FLUX_IVAR_R        float32           Inverse variance of FLUX_R (AB)
FLUX_IVAR_Z        float32           Inverse variance of FLUX_Z (AB)
FLUX_IVAR_W1       float32           Inverse variance of FLUX_W1 (AB)
FLUX_IVAR_W2       float32           Inverse variance of FLUX_W2 (AB)
MW_TRANSMISSION_G  float64           Milky Way dust transmission in g-band
MW_TRANSMISSION_R  float64           Milky Way dust transmission in r-band
MW_TRANSMISSION_Z  float64           Milky Way dust transmission in z-band
MW_TRANSMISSION_W1 float64           Milky Way dust transmission in WISE W1
MW_TRANSMISSION_W2 float64           Milky Way dust transmission in WISE W2
PROBA_RF           float64
MASKBITS           int16             Bitwise mask from the imaging indicating potential issue or blending
DESI_TARGET        int64             Dark survey + calibration targeting bits
SCND_TARGET        int64             Target selection bitmask for secondary programs
COADD_NUMEXP       int16
COADD_EXPTIME      float32
CMX_TARGET         int64             Target selection bitmask for commissioning
SV1_DESI_TARGET    int64             DESI (dark time program) target selection bitmask for SV1
SV2_DESI_TARGET    int64             DESI (dark time program) target selection bitmask for SV2
SV3_DESI_TARGET    int64             DESI (dark time program) target selection bitmask for SV3
SV1_SCND_TARGET    int64             Secondary target selection bitmask for SV1
SV2_SCND_TARGET    int64             Secondary target selection bitmask for SV2
SV3_SCND_TARGET    int64             Secondary target selection bitmask for SV3
TSNR2_LYA          float32           LYA template (S/N)^2 summed over B,R,Z
TSNR2_QSO          float32           QSO template (S/N)^2 summed over B,R,Z
DELTA_CHI2_MGII    float32
A_MGII             float32
SIGMA_MGII         float32
B_MGII             float32
VAR_A_MGII         float32
VAR_SIGMA_MGII     float32
VAR_B_MGII         float32
Z_RR               float32           Redshift collected from redrock file
Z_QN               float32           Redshift measured by QuasarNET
C_LYA              float32           Confidence line for LYA (*i.e.*) ~ probability to be a QSO
C_CIV              float32           Confidence line for CIV
C_CIII             float32           Confidence line for CIII
C_MgII             float32           Confidence line for MgII
C_Hbeta            float32           Confidence line for Hbeta
C_Halpha           float32           Confidence line for Halpha
Z_LYA              float32           Redshift estimated by QuasarNET with LYA line
Z_CIV              float32           Redshift estimated by QuasarNET with CIV line
Z_CIII             float32           Redshift estimated by QuasarNET with CIII line
Z_MgII             float32           Redshift estimated by QuasarNET with MgII line
Z_Hbeta            float32           Redshift estimated by QuasarNET with Hbeta line
Z_Halpha           float32           Redshift estimated by QuasarNET with Halpha line
QSO_MASKBITS       int32
HPXPIXEL           int64             HEALPixel containing this location at NSIDE=64 in the NESTED scheme
SURVEY             char stream       Survey name
PROGRAM            char stream       DESI program type - BRIGHT, DARK or BACKUP
================== =========== ===== ====================================================================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
