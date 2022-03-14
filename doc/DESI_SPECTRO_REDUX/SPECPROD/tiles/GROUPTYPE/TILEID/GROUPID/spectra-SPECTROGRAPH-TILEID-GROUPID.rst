========================================
spectra-SPECTROGRAPH-TILEID-GROUPID.fits
========================================

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``spectra-SPECTROGRAPH-TILEID-GROUPID.fits``, where
    ``SPECTROGRAPH`` is the spectrograph ID, ``TILEID`` is the tile number and
    ``GROUPID`` depends on the ``GROUPTYPE`` of the tile coadd.
:Regex: ``spectra-[0-9]-[0-9]+-([14]xsubset[1-6]|lowspeedsubset[1-6]|exp[0-9]{8}|thru[0-9]{8}|[0-9]{8})\.fits``
:File Type: FITS, 198 MB

Contents
========

====== ============ ======== ===================
Number EXTNAME      Type     Contents
====== ============ ======== ===================
HDU00_              IMAGE    *Brief Description*
HDU01_ FIBERMAP     BINTABLE *Brief Description*
HDU02_ SCORES       BINTABLE *Brief Description*
HDU03_ B_WAVELENGTH IMAGE    *Brief Description*
HDU04_ B_FLUX       IMAGE    *Brief Description*
HDU05_ B_IVAR       IMAGE    *Brief Description*
HDU06_ B_MASK       BINTABLE *Brief Description*
HDU07_ B_RESOLUTION IMAGE    *Brief Description*
HDU08_ R_WAVELENGTH IMAGE    *Brief Description*
HDU09_ R_FLUX       IMAGE    *Brief Description*
HDU10_ R_IVAR       IMAGE    *Brief Description*
HDU11_ R_MASK       BINTABLE *Brief Description*
HDU12_ R_RESOLUTION IMAGE    *Brief Description*
HDU13_ Z_WAVELENGTH IMAGE    *Brief Description*
HDU14_ Z_FLUX       IMAGE    *Brief Description*
HDU15_ Z_IVAR       IMAGE    *Brief Description*
HDU16_ Z_MASK       BINTABLE *Brief Description*
HDU17_ Z_RESOLUTION IMAGE    *Brief Description*
====== ============ ======== ===================


FITS Header Units
=================

HDU00
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
CHECKSUM cXXRdWUQcWUQcWUQ str  HDU checksum updated 2021-07-15T00:33:13
DATASUM  0                str  data unit checksum updated 2021-07-15T00:33:13
======== ================ ==== ==============================================

Empty HDU.

HDU01
-----

EXTNAME = FIBERMAP

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   413              int  length of dimension 1
NAXIS2   500              int  length of dimension 2
CHECKSUM TcPqUbPoTbPoTbPo str  HDU checksum updated 2021-07-15T00:33:13
DATASUM  1051947488       str  data unit checksum updated 2021-07-15T00:33:13
======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

===================== ======= ===== ===========
Name                  Type    Units Description
===================== ======= ===== ===========
TARGETID              int64
PETAL_LOC             int16
DEVICE_LOC            int32
LOCATION              int64
FIBER                 int32
FIBERSTATUS           int32
TARGET_RA             float64
TARGET_DEC            float64
PMRA                  float32
PMDEC                 float32
REF_EPOCH             float32
LAMBDA_REF            float32
FA_TARGET             int64
FA_TYPE               binary
OBJTYPE               char[3]
FIBERASSIGN_X         float32
FIBERASSIGN_Y         float32
PRIORITY              int32
SUBPRIORITY           float64
OBSCONDITIONS         int32
RELEASE               int16
BRICKID               int32
BRICK_OBJID           int32
MORPHTYPE             char[4]
FLUX_G                float32
FLUX_R                float32
FLUX_Z                float32
FLUX_IVAR_G           float32
FLUX_IVAR_R           float32
FLUX_IVAR_Z           float32
MASKBITS              int16
REF_ID                int64
REF_CAT               char[2]
GAIA_PHOT_G_MEAN_MAG  float32
GAIA_PHOT_BP_MEAN_MAG float32
GAIA_PHOT_RP_MEAN_MAG float32
PARALLAX              float32
BRICKNAME             char[8]
EBV                   float32
FLUX_W1               float32
FLUX_W2               float32
FLUX_IVAR_W1          float32
FLUX_IVAR_W2          float32
FIBERFLUX_G           float32
FIBERFLUX_R           float32
FIBERFLUX_Z           float32
FIBERTOTFLUX_G        float32
FIBERTOTFLUX_R        float32
FIBERTOTFLUX_Z        float32
SERSIC                float32
SHAPE_R               float32
SHAPE_E1              float32
SHAPE_E2              float32
PHOTSYS               char[1]
PRIORITY_INIT         int64
NUMOBS_INIT           int64
SV3_DESI_TARGET       int64
SV3_BGS_TARGET        int64
SV3_MWS_TARGET        int64
SV3_SCND_TARGET       int64
DESI_TARGET           int64
BGS_TARGET            int64
MWS_TARGET            int64
PLATE_RA              float64
PLATE_DEC             float64
NUM_ITER              int64
FIBER_X               float64
FIBER_Y               float64
DELTA_X               float64
DELTA_Y               float64
FIBER_RA              float64
FIBER_DEC             float64
EXPTIME               float64
PSF_TO_FIBER_SPECFLUX float64
NIGHT                 int32
EXPID                 int32
MJD                   float64
TILEID                int32
===================== ======= ===== ===========

HDU02
-----

EXTNAME = SCORES

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =======================
KEY    Example Value Type Comment
====== ============= ==== =======================
NAXIS1 488           int  width of table in bytes
NAXIS2 500           int  number of rows in table
====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

===================== ======= ===== ===================
Name                  Type    Units Description
===================== ======= ===== ===================
TARGETID              int64         label for field   1
SUM_RAW_COUNT_B       float64       label for field   2
MEDIAN_RAW_COUNT_B    float64       label for field   3
MEDIAN_RAW_SNR_B      float64       label for field   4
SUM_FFLAT_COUNT_B     float64       label for field   5
MEDIAN_FFLAT_COUNT_B  float64       label for field   6
MEDIAN_FFLAT_SNR_B    float64       label for field   7
SUM_SKYSUB_COUNT_B    float64       label for field   8
MEDIAN_SKYSUB_COUNT_B float64       label for field   9
MEDIAN_SKYSUB_SNR_B   float64       label for field  10
SUM_CALIB_COUNT_B     float64       label for field  11
MEDIAN_CALIB_COUNT_B  float64       label for field  12
MEDIAN_CALIB_SNR_B    float64       label for field  13
TSNR2_GPBDARK_B       float64       label for field  14
TSNR2_ELG_B           float64       label for field  15
TSNR2_GPBBRIGHT_B     float64       label for field  16
TSNR2_LYA_B           float64       label for field  17
TSNR2_BGS_B           float64       label for field  18
TSNR2_GPBBACKUP_B     float64       label for field  19
TSNR2_QSO_B           float64       label for field  20
TSNR2_LRG_B           float64       label for field  21
SUM_RAW_COUNT_R       float64       label for field  22
MEDIAN_RAW_COUNT_R    float64       label for field  23
MEDIAN_RAW_SNR_R      float64       label for field  24
SUM_FFLAT_COUNT_R     float64       label for field  25
MEDIAN_FFLAT_COUNT_R  float64       label for field  26
MEDIAN_FFLAT_SNR_R    float64       label for field  27
SUM_SKYSUB_COUNT_R    float64       label for field  28
MEDIAN_SKYSUB_COUNT_R float64       label for field  29
MEDIAN_SKYSUB_SNR_R   float64       label for field  30
SUM_CALIB_COUNT_R     float64       label for field  31
MEDIAN_CALIB_COUNT_R  float64       label for field  32
MEDIAN_CALIB_SNR_R    float64       label for field  33
TSNR2_GPBDARK_R       float64       label for field  34
TSNR2_ELG_R           float64       label for field  35
TSNR2_GPBBRIGHT_R     float64       label for field  36
TSNR2_LYA_R           float64       label for field  37
TSNR2_BGS_R           float64       label for field  38
TSNR2_GPBBACKUP_R     float64       label for field  39
TSNR2_QSO_R           float64       label for field  40
TSNR2_LRG_R           float64       label for field  41
SUM_RAW_COUNT_Z       float64       label for field  42
MEDIAN_RAW_COUNT_Z    float64       label for field  43
MEDIAN_RAW_SNR_Z      float64       label for field  44
SUM_FFLAT_COUNT_Z     float64       label for field  45
MEDIAN_FFLAT_COUNT_Z  float64       label for field  46
MEDIAN_FFLAT_SNR_Z    float64       label for field  47
SUM_SKYSUB_COUNT_Z    float64       label for field  48
MEDIAN_SKYSUB_COUNT_Z float64       label for field  49
MEDIAN_SKYSUB_SNR_Z   float64       label for field  50
SUM_CALIB_COUNT_Z     float64       label for field  51
MEDIAN_CALIB_COUNT_Z  float64       label for field  52
MEDIAN_CALIB_SNR_Z    float64       label for field  53
TSNR2_GPBDARK_Z       float64       label for field  54
TSNR2_ELG_Z           float64       label for field  55
TSNR2_GPBBRIGHT_Z     float64       label for field  56
TSNR2_LYA_Z           float64       label for field  57
TSNR2_BGS_Z           float64       label for field  58
TSNR2_GPBBACKUP_Z     float64       label for field  59
TSNR2_QSO_Z           float64       label for field  60
TSNR2_LRG_Z           float64       label for field  61
===================== ======= ===== ===================

HDU03
-----

EXTNAME = B_WAVELENGTH

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =====================
KEY    Example Value Type Comment
====== ============= ==== =====================
NAXIS1 2751          int  length of data axis 1
BUNIT  Angstrom      str
====== ============= ==== =====================

Data: FITS image [float64, 2751]

HDU04
-----

EXTNAME = B_FLUX

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============================ ==== =====================
KEY    Example Value                Type Comment
====== ============================ ==== =====================
NAXIS1 2751                         int  length of data axis 1
NAXIS2 500                          int  length of data axis 2
BUNIT  10**-17 erg/(s cm2 Angstrom) str
====== ============================ ==== =====================

Data: FITS image [float32, 2751x500]

HDU05
-----

EXTNAME = B_IVAR

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ================================= ==== =====================
KEY    Example Value                     Type Comment
====== ================================= ==== =====================
NAXIS1 2751                              int  length of data axis 1
NAXIS2 500                               int  length of data axis 2
BUNIT  10**+34 (s2 cm4 Angstrom2) / erg2 str
====== ================================= ==== =====================

Data: FITS image [float32, 2751x500]

HDU06
-----

EXTNAME = B_MASK

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== ==========================================
KEY    Example Value Type Comment
====== ============= ==== ==========================================
NAXIS1 8             int  width of table in bytes
NAXIS2 500           int  number of rows in table
BZERO  2147483648    int  offset data range to that of unsigned long
BSCALE 1             int  default scaling factor
====== ============= ==== ==========================================

Data: FITS image [int32 (compressed), 2751x500]

HDU07
-----

EXTNAME = B_RESOLUTION

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =====================
KEY    Example Value Type Comment
====== ============= ==== =====================
NAXIS1 2751          int  length of data axis 1
NAXIS2 11            int  length of data axis 2
NAXIS3 500           int  length of data axis 3
====== ============= ==== =====================

Data: FITS image [float32, 2751x11x500]

HDU08
-----

EXTNAME = R_WAVELENGTH

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =====================
KEY    Example Value Type Comment
====== ============= ==== =====================
NAXIS1 2326          int  length of data axis 1
BUNIT  Angstrom      str
====== ============= ==== =====================

Data: FITS image [float64, 2326]

HDU09
-----

EXTNAME = R_FLUX

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============================ ==== =====================
KEY    Example Value                Type Comment
====== ============================ ==== =====================
NAXIS1 2326                         int  length of data axis 1
NAXIS2 500                          int  length of data axis 2
BUNIT  10**-17 erg/(s cm2 Angstrom) str
====== ============================ ==== =====================

Data: FITS image [float32, 2326x500]

HDU10
-----

EXTNAME = R_IVAR

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ================================= ==== =====================
KEY    Example Value                     Type Comment
====== ================================= ==== =====================
NAXIS1 2326                              int  length of data axis 1
NAXIS2 500                               int  length of data axis 2
BUNIT  10**+34 (s2 cm4 Angstrom2) / erg2 str
====== ================================= ==== =====================

Data: FITS image [float32, 2326x500]

HDU11
-----

EXTNAME = R_MASK

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== ==========================================
KEY    Example Value Type Comment
====== ============= ==== ==========================================
NAXIS1 8             int  width of table in bytes
NAXIS2 500           int  number of rows in table
BZERO  2147483648    int  offset data range to that of unsigned long
BSCALE 1             int  default scaling factor
====== ============= ==== ==========================================

Data: FITS image [int32 (compressed), 2326x500]

HDU12
-----

EXTNAME = R_RESOLUTION

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =====================
KEY    Example Value Type Comment
====== ============= ==== =====================
NAXIS1 2326          int  length of data axis 1
NAXIS2 11            int  length of data axis 2
NAXIS3 500           int  length of data axis 3
====== ============= ==== =====================

Data: FITS image [float32, 2326x11x500]

HDU13
-----

EXTNAME = Z_WAVELENGTH

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =====================
KEY    Example Value Type Comment
====== ============= ==== =====================
NAXIS1 2881          int  length of data axis 1
BUNIT  Angstrom      str
====== ============= ==== =====================

Data: FITS image [float64, 2881]

HDU14
-----

EXTNAME = Z_FLUX

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============================ ==== =====================
KEY    Example Value                Type Comment
====== ============================ ==== =====================
NAXIS1 2881                         int  length of data axis 1
NAXIS2 500                          int  length of data axis 2
BUNIT  10**-17 erg/(s cm2 Angstrom) str
====== ============================ ==== =====================

Data: FITS image [float32, 2881x500]

HDU15
-----

EXTNAME = Z_IVAR

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ================================= ==== =====================
KEY    Example Value                     Type Comment
====== ================================= ==== =====================
NAXIS1 2881                              int  length of data axis 1
NAXIS2 500                               int  length of data axis 2
BUNIT  10**+34 (s2 cm4 Angstrom2) / erg2 str
====== ================================= ==== =====================

Data: FITS image [float32, 2881x500]

HDU16
-----

EXTNAME = Z_MASK

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== ==========================================
KEY    Example Value Type Comment
====== ============= ==== ==========================================
NAXIS1 8             int  width of table in bytes
NAXIS2 500           int  number of rows in table
BZERO  2147483648    int  offset data range to that of unsigned long
BSCALE 1             int  default scaling factor
====== ============= ==== ==========================================

Data: FITS image [int32 (compressed), 2881x500]

HDU17
-----

EXTNAME = Z_RESOLUTION

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =====================
KEY    Example Value Type Comment
====== ============= ==== =====================
NAXIS1 2881          int  length of data axis 1
NAXIS2 11            int  length of data axis 2
NAXIS3 500           int  length of data axis 3
====== ============= ==== =====================

Data: FITS image [float32, 2881x11x500]


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
