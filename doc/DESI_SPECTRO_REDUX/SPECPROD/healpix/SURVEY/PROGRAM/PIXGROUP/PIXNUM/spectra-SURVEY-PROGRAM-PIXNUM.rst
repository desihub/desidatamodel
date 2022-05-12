==================================
spectra-SURVEY-PROGRAM-PIXNUM.fits
==================================

:Summary: DESI spectra grouped by nested healpix number
:Naming Convention: ``spectra-SURVEY-PROGRAM-PIXNUM.fits``, where ``SURVEY`` is
    *e.g.* ``main`` or ``sv1``, ``PROGRAM`` is *e.g.* ``bright or ``dark``
    and ``PIXNUM`` is the HEALPixel number.
:Regex: ``spectra-(cmx|main|special|sv1|sv2|sv3)-(backup|bright|dark|other)-[0-9]+\.fits``
:File Type: FITS, 408 MB

Contents
========

====== ============ ======== ===================
Number EXTNAME      Type     Contents
====== ============ ======== ===================
HDU00_              IMAGE    Empty
HDU01_ FIBERMAP     BINTABLE fibermap table
HDU02_ SCORES       BINTABLE scores table
HDU03_ B_WAVELENGTH IMAGE    Wavelength array of b-channel spectra
HDU04_ B_FLUX       IMAGE    Flux of b-channel spectra
HDU05_ B_IVAR       IMAGE    Inverse variance of b-channel spectra
HDU06_ B_MASK       BINTABLE Mask of b-channel spectra
HDU07_ B_RESOLUTION IMAGE    Resolution matrices of b-channel spectra
HDU08_ R_WAVELENGTH IMAGE    Wavelength array of r-channel spectra
HDU09_ R_FLUX       IMAGE    Flux of r-channel spectra
HDU10_ R_IVAR       IMAGE    Inverse variance of r-channel spectra
HDU11_ R_MASK       BINTABLE Mask of r-channel spectra
HDU12_ R_RESOLUTION IMAGE    Resolution matrices of r-channel spectra
HDU13_ Z_WAVELENGTH IMAGE    Wavelength array of z-channel spectra
HDU14_ Z_FLUX       IMAGE    Flux of z-channel spectra
HDU15_ Z_IVAR       IMAGE    Inverse variance of z-channel spectra
HDU16_ Z_MASK       BINTABLE Mask of z-channel spectra
HDU17_ Z_RESOLUTION IMAGE    Resolution matrices of z-channel spectra
====== ============ ======== ===================


FITS Header Units
=================

HDU00
-----

HEALPixel keywords.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
HPXNSIDE 64               int
HPXPIXEL 12081            int
HPXNEST  T                bool
CHECKSUM 8DPU9BMR8BMR8BMR str  HDU checksum updated 2021-07-19T17:59:29
DATASUM  0                str  data unit checksum updated 2021-07-19T17:59:29
======== ================ ==== ==============================================

Empty HDU.

HDU01
-----

EXTNAME = FIBERMAP

fibermap table with two additional columns NIGHT and EXPID.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   413              int  length of dimension 1
NAXIS2   1031             int  length of dimension 2
CHECKSUM U9Fia89iV8Cia89i str  HDU checksum updated 2021-07-19T17:59:29
DATASUM  3589169610       str  data unit checksum updated 2021-07-19T17:59:29
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
SV1_DESI_TARGET       int64
SV1_BGS_TARGET        int64
SV1_MWS_TARGET        int64
SV1_SCND_TARGET       int64
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
NAXIS2 1031          int  number of rows in table
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

Wavelength[nwave] array in Angstroms of b-channel spectra

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

Flux[nspec,nwave] array in 1e-17 erg/(s cm2 Angstrom) of b-channel spectra

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============================ ==== =====================
KEY    Example Value                Type Comment
====== ============================ ==== =====================
NAXIS1 2751                         int  length of data axis 1
NAXIS2 1031                         int  length of data axis 2
BUNIT  10**-17 erg/(s cm2 Angstrom) str
====== ============================ ==== =====================

Data: FITS image [float32, 2751x1031]

HDU05
-----

EXTNAME = B_IVAR

Inverse variance of b-channel flux array

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ================================= ==== =====================
KEY    Example Value                     Type Comment
====== ================================= ==== =====================
NAXIS1 2751                              int  length of data axis 1
NAXIS2 1031                              int  length of data axis 2
BUNIT  10**+34 (s2 cm4 Angstrom2) / erg2 str
====== ================================= ==== =====================

Data: FITS image [float32, 2751x1031]

HDU06
-----

EXTNAME = B_MASK

Mask[nspec,nwave] of b-channel flux array.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== ==========================================
KEY    Example Value Type Comment
====== ============= ==== ==========================================
NAXIS1 8             int  width of table in bytes
NAXIS2 1031          int  number of rows in table
BZERO  2147483648    int  offset data range to that of unsigned long
BSCALE 1             int  default scaling factor
====== ============= ==== ==========================================

Data: FITS image [int32 (compressed), 2751x1031]

HDU07
-----

EXTNAME = B_RESOLUTION

Diagonals of b-channel resolution matrix

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =====================
KEY    Example Value Type Comment
====== ============= ==== =====================
NAXIS1 2751          int  length of data axis 1
NAXIS2 11            int  length of data axis 2
NAXIS3 1031          int  length of data axis 3
====== ============= ==== =====================

Data: FITS image [float32, 2751x11x1031]

A sparse resolution matrix may be created for spectrum ``i`` with::

    from desispec.resolution import Resolution
    R = Resolution(data[i])

Or using lower-level scipy.sparse matrices::

    import scipy.sparse
    import numpy as np
    nspec, ndiag, nwave = data.shape
    offsets = ndiag//2 - np.arange(ndiag, dtype=int)
    R = scipy.sparse.dia_matrix((data[i], offsets), shape=(nwave, nwave))

HDU08
-----

EXTNAME = R_WAVELENGTH

Wavelength[nwave] array in Angstroms of r-channel spectra

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

Flux[nspec,nwave] array in 1e-17 erg/(s cm2 Angstrom) of r-channel spectra

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============================ ==== =====================
KEY    Example Value                Type Comment
====== ============================ ==== =====================
NAXIS1 2326                         int  length of data axis 1
NAXIS2 1031                         int  length of data axis 2
BUNIT  10**-17 erg/(s cm2 Angstrom) str
====== ============================ ==== =====================

Data: FITS image [float32, 2326x1031]

HDU10
-----

EXTNAME = R_IVAR

Inverse variance of r-channel flux array

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ================================= ==== =====================
KEY    Example Value                     Type Comment
====== ================================= ==== =====================
NAXIS1 2326                              int  length of data axis 1
NAXIS2 1031                              int  length of data axis 2
BUNIT  10**+34 (s2 cm4 Angstrom2) / erg2 str
====== ================================= ==== =====================

Data: FITS image [float32, 2326x1031]

HDU11
-----

EXTNAME = R_MASK

Mask[nspec,nwave] of r-channel flux array.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== ==========================================
KEY    Example Value Type Comment
====== ============= ==== ==========================================
NAXIS1 8             int  width of table in bytes
NAXIS2 1031          int  number of rows in table
BZERO  2147483648    int  offset data range to that of unsigned long
BSCALE 1             int  default scaling factor
====== ============= ==== ==========================================

Data: FITS image [int32 (compressed), 2326x1031]

HDU12
-----

EXTNAME = R_RESOLUTION

Diagonals of r-channel resolution matrix.

See B_RESOLUTION HDU for description of the format.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =====================
KEY    Example Value Type Comment
====== ============= ==== =====================
NAXIS1 2326          int  length of data axis 1
NAXIS2 11            int  length of data axis 2
NAXIS3 1031          int  length of data axis 3
====== ============= ==== =====================

Data: FITS image [float32, 2326x11x1031]

HDU13
-----

EXTNAME = Z_WAVELENGTH

Wavelength[nwave] array in Angstroms of z-channel spectra

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

Flux[nspec,nwave] array in 1e-17 erg/(s cm2 Angstrom) of z-channel spectra

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============================ ==== =====================
KEY    Example Value                Type Comment
====== ============================ ==== =====================
NAXIS1 2881                         int  length of data axis 1
NAXIS2 1031                         int  length of data axis 2
BUNIT  10**-17 erg/(s cm2 Angstrom) str
====== ============================ ==== =====================

Data: FITS image [float32, 2881x1031]

HDU15
-----

EXTNAME = Z_IVAR

Inverse variance of z-channel flux array

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ================================= ==== =====================
KEY    Example Value                     Type Comment
====== ================================= ==== =====================
NAXIS1 2881                              int  length of data axis 1
NAXIS2 1031                              int  length of data axis 2
BUNIT  10**+34 (s2 cm4 Angstrom2) / erg2 str
====== ================================= ==== =====================

Data: FITS image [float32, 2881x1031]

HDU16
-----

EXTNAME = Z_MASK

Mask[nspec,nwave] of z-channel flux array.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== ==========================================
KEY    Example Value Type Comment
====== ============= ==== ==========================================
NAXIS1 8             int  width of table in bytes
NAXIS2 1031          int  number of rows in table
BZERO  2147483648    int  offset data range to that of unsigned long
BSCALE 1             int  default scaling factor
====== ============= ==== ==========================================

Data: FITS image [int32 (compressed), 2881x1031]

HDU17
-----

EXTNAME = Z_RESOLUTION

Diagonals of z-channel resolution matrix.

See B_RESOLUTION HDU for description of the format.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =====================
KEY    Example Value Type Comment
====== ============= ==== =====================
NAXIS1 2881          int  length of data axis 1
NAXIS2 11            int  length of data axis 2
NAXIS3 1031          int  length of data axis 3
====== ============= ==== =====================

Data: FITS image [float32, 2881x11x1031]


Notes and Examples
==================

The format supports arbitrary channel names as long as for each channel {X}
there is a set of HDUs named {X}_WAVELENGTH, {X}_FLUX, {X}_IVAR, {X}_MASK,
{X}_RESOLUTION.

Upcoming changes
================

The following changes are not yet in the spectra files, but will be added in
the future:

* signal-to-noise per band
