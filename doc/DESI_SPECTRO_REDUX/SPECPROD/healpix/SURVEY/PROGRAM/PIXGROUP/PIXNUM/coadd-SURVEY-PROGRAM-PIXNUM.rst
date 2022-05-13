================================
coadd-SURVEY-PROGRAM-PIXNUM.fits
================================

:Summary: This holds the calibrated coadded spectra organized by healpix location
    on the sky.
:Naming Convention: ``coadd-SURVEY-PROGRAM-PIXNUM.fits``, where ``SURVEY`` is
    *e.g.* ``main`` or ``sv1``, ``PROGRAM`` is *e.g.* ``bright or ``dark``
    and ``PIXNUM`` is the HEALPixel number.
:Regex: ``coadd-(cmx|main|special|sv1|sv2|sv3)-(backup|bright|dark|other)-[0-9]+\.fits``
:File Type: FITS, 219 MB

This file follows nearly the same format as the
:doc:`spectra files <spectra-SURVEY-PROGRAM-PIXNUM>`, except there is
one entry per target instead of one entry per exposure per target, and
the FIBERMAP replaces some exposure-specific columns with summary columns,
e.g. ``NIGHT`` becomes ``FIRST_NIGHT``, ``LAST_NIGHT``, and ``NUM_NIGHT``.

As-of software release 20.4 (desispec 0.34.4), the SCORES HDU is the last
HDU instead of HDU2.

Contents
========

====== ============ ======== ===================
Number EXTNAME      Type     Contents
====== ============ ======== ===================
HDU00_              IMAGE    Empty
HDU01_ FIBERMAP     BINTABLE fibermap table
HDU02_ EXP_FIBERMAP BINTABLE *Brief Description*
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
HDU18_ SCORES       BINTABLE scores table
====== ============ ======== ===================


FITS Header Units
=================

HDU00
-----

HEALPixel keywords.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== =========================== ==== ==============================================
    KEY      Example Value               Type Comment
    ======== =========================== ==== ==============================================
    HPXNSIDE 64                          int
    HPXPIXEL 38863                       int
    HPXNEST  T                           bool
    CHECKSUM 96ZDB6YB96YBA6YB            str  HDU checksum updated 2021-07-20T01:03:03
    DATASUM  0                           str  data unit checksum updated 2021-07-20T01:03:03
    FIBERMIN -513                        int
    INFIL000 spectra-sv1-dark-38863.fits str
    ======== =========================== ==== ==============================================

Empty HDU.

HDU01
-----

EXTNAME = FIBERMAP

fibermap table with two additional columns NIGHT and EXPID.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   341              int  length of dimension 1
    NAXIS2   514              int  length of dimension 2
    ENCODING ascii            str
    CHECKSUM 4aNU7WKR4aKR4UKR str  HDU checksum updated 2021-07-20T01:03:03
    DATASUM  4121667036       str  data unit checksum updated 2021-07-20T01:03:03
    ======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

========================== ======= ===== =====================================================
Name                       Type    Units Description
========================== ======= ===== =====================================================
TARGETID                   int64         Unique target ID
COADD_FIBERSTATUS          int32
TARGET_RA                  float64       Target Right Ascension [degrees]
TARGET_DEC                 float64       Target declination [degrees]
PMRA                       float32       PM in +RA dir (already incl cos(dec))
PMDEC                      float32       Proper motion in +dec direction
REF_EPOCH                  float32       proper motion reference epoch
FA_TARGET                  int64
FA_TYPE                    binary        Internal fiberassign target type
OBJTYPE                    char[3]       SKY, TGT, NON
SUBPRIORITY                float64       Assignment subpriority [0-1)
OBSCONDITIONS              int32         bitmask of allowable observing conditions
RELEASE                    int16         imaging surveys release ID
BRICKID                    int32         Imaging Surveys brick ID
BRICK_OBJID                int32         Imaging Surveys OBJID on that brick
MORPHTYPE                  char[4]       Imaging Surveys morphological type
FLUX_G                     float32       g-band flux
FLUX_R                     float32       r-band flux
FLUX_Z                     float32       z-band flux
FLUX_IVAR_G                float32       Inverse variance of FLUX_G
FLUX_IVAR_R                float32       Inverse variance of FLUX_R
FLUX_IVAR_Z                float32       Inverse variance of FLUX_Z
MASKBITS                   int16         Photometry mask bits
REF_ID                     int64         Astrometric cat refID (Gaia SOURCE_ID)
REF_CAT                    char[2]       astrometry reference catalog
GAIA_PHOT_G_MEAN_MAG       float32       Gaia G band mag
GAIA_PHOT_BP_MEAN_MAG      float32       Gaia BP band mag
GAIA_PHOT_RP_MEAN_MAG      float32       Gaia RP band mag
PARALLAX                   float32       Parallax
BRICKNAME                  char[8]       Imaging Surveys brick name
EBV                        float32       Galactic extinction E(B-V) reddening from SFD98
FLUX_W1                    float32       WISE W1-band flux
FLUX_W2                    float32       WISE W2-band flux
FLUX_IVAR_W1               float32       Inverse variance of FLUX_W1
FLUX_IVAR_W2               float32       Inverse variance of FLUX_W2
FIBERFLUX_G                float32       g-band model flux 1&quot; seeing, 1.5&quot; dia fiber
FIBERFLUX_R                float32       r-band model flux 1&quot; seeing, 1.5&quot; dia fiber
FIBERFLUX_Z                float32       z-band model flux 1&quot; seeing, 1.5&quot; dia fiber
FIBERTOTFLUX_G             float32       fiberflux model incl. all objs at this loc
FIBERTOTFLUX_R             float32       fiberflux model incl. all objs at this loc
FIBERTOTFLUX_Z             float32       fiberflux model incl. all objs at this loc
SERSIC                     float32       Power-law index for the Sersic profile model
SHAPE_R                    float32       Half-light radius of galaxy model
SHAPE_E1                   float32       Ellipticity component 1 for galaxy model
SHAPE_E2                   float32       Ellipticity component 2 for galaxy model
PHOTSYS                    char[1]       N for BASS/MzLS, S for DECam
PRIORITY_INIT              int64         initial priority
NUMOBS_INIT                int64         initial number of requested observations
SV1_DESI_TARGET            int64
SV1_BGS_TARGET             int64
SV1_MWS_TARGET             int64
SV1_SCND_TARGET            int64
DESI_TARGET                int64         Dark survey + calibration targeting bits
BGS_TARGET                 int64         Bright Galaxy Survey targeting bits
MWS_TARGET                 int64         Milky Way Survey targeting bits
PLATE_RA                   float64       Right Ascension for Platemaker to use [degrees]
PLATE_DEC                  float64       declination for Platemaker to use [degrees]
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
========================== ======= ===== =====================================================

HDU02
-----

EXTNAME = EXP_FIBERMAP

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   162              int  length of dimension 1
    NAXIS2   7112             int  length of dimension 2
    ENCODING ascii            str
    CHECKSUM g3Nmh2Nlg2Nlg2Nl str  HDU checksum updated 2021-07-20T01:03:03
    DATASUM  3607867694       str  data unit checksum updated 2021-07-20T01:03:03
    ======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

===================== ======= ===== ===============================================
Name                  Type    Units Description
===================== ======= ===== ===============================================
TARGETID              int64         Unique target ID
PRIORITY              int32         Assignment priority; larger=higher priority
SUBPRIORITY           float64       Assignment subpriority [0-1)
NIGHT                 int32
EXPID                 int32
MJD                   float64
TILEID                int32
EXPTIME               float64       Exposure time
PETAL_LOC             int16         Petal location [0-9]
DEVICE_LOC            int32         Device location on focal plane [0-523]
LOCATION              int64         FP location PETAL_LOC*1000 + DEVICE_LOC
FIBER                 int32         Fiber ID on the CCDs [0-4999]
FIBERSTATUS           int32         Fiber status; 0=good
FIBERASSIGN_X         float32       Expected CS5 X on focal plane
FIBERASSIGN_Y         float32       Expected CS5 Y on focal plane
LAMBDA_REF            float32       Wavelength at which fiber was centered
PLATE_RA              float64       Right Ascension for Platemaker to use [degrees]
PLATE_DEC             float64       declination for Platemaker to use [degrees]
NUM_ITER              int64         Number of positioner iterations
FIBER_X               float64       CS5 X location requested by PlateMaker
FIBER_Y               float64       CS5 Y location requested by PlateMaker
DELTA_X               float64       CS5 X diff requested and actual position
DELTA_Y               float64       CS5 Y diff requested and actual position
FIBER_RA              float64       RA of actual fiber position
FIBER_DEC             float64       DEC of actual fiber position
PSF_TO_FIBER_SPECFLUX float64
===================== ======= ===== ===============================================

HDU03
-----

EXTNAME = B_WAVELENGTH

Wavelength[nwave] array in Angstroms of b-channel spectra

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2751             int
    BUNIT    Angstrom         str
    CHECKSUM 9FJDF9H99CHCC9H9 str  HDU checksum updated 2021-07-20T01:03:03
    DATASUM  979185614        str  data unit checksum updated 2021-07-20T01:03:03
    ======== ================ ==== ==============================================

Data: FITS image [float64, 2751]

HDU04
-----

EXTNAME = B_FLUX

Flux[nspec,nwave] array in 1e-17 erg/(s cm2 Angstrom) of b-channel spectra

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ============================ ==== ==============================================
    KEY      Example Value                Type Comment
    ======== ============================ ==== ==============================================
    NAXIS1   2751                         int
    NAXIS2   514                          int
    BUNIT    10**-17 erg/(s cm2 Angstrom) str
    CHECKSUM KdcnKccnKccnKccn             str  HDU checksum updated 2021-07-20T01:03:03
    DATASUM  1454063034                   str  data unit checksum updated 2021-07-20T01:03:03
    ======== ============================ ==== ==============================================

Data: FITS image [float32, 2751x514]

HDU05
-----

EXTNAME = B_IVAR

Inverse variance of b-channel flux array

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================================= ==== ==============================================
    KEY      Example Value                     Type Comment
    ======== ================================= ==== ==============================================
    NAXIS1   2751                              int
    NAXIS2   514                               int
    BUNIT    10**+34 (s2 cm4 Angstrom2) / erg2 str
    CHECKSUM 1AE635E61AE613E6                  str  HDU checksum updated 2021-07-20T01:03:03
    DATASUM  2902189966                        str  data unit checksum updated 2021-07-20T01:03:03
    ======== ================================= ==== ==============================================

Data: FITS image [float32, 2751x514]

HDU06
-----

EXTNAME = B_MASK

Mask[nspec,nwave] of b-channel flux array.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2751             int
    NAXIS2   514              int
    BSCALE   1                int
    BZERO    2147483648       int
    CHECKSUM 78fA97f677fA77f3 str  HDU checksum updated 2021-07-20T01:03:03
    DATASUM  707110           str  data unit checksum updated 2021-07-20T01:03:03
    ======== ================ ==== ==============================================

Data: FITS image [int32, 2751x514]

HDU07
-----

EXTNAME = B_RESOLUTION

Diagonals of b-channel resolution matrix

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2751             int
    NAXIS2   11               int
    NAXIS3   514              int
    CHECKSUM 4q1B4o094o0A4o09 str  HDU checksum updated 2021-07-20T01:03:03
    DATASUM  1510900028       str  data unit checksum updated 2021-07-20T01:03:03
    ======== ================ ==== ==============================================

Data: FITS image [float32, 2751x11x514]

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

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2326             int
    BUNIT    Angstrom         str
    CHECKSUM 9JTAFHQ79HQACHQ7 str  HDU checksum updated 2021-07-20T01:03:03
    DATASUM  456732359        str  data unit checksum updated 2021-07-20T01:03:03
    ======== ================ ==== ==============================================

Data: FITS image [float64, 2326]

HDU09
-----

EXTNAME = R_FLUX

Flux[nspec,nwave] array in 1e-17 erg/(s cm2 Angstrom) of r-channel spectra

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ============================ ==== ==============================================
    KEY      Example Value                Type Comment
    ======== ============================ ==== ==============================================
    NAXIS1   2326                         int
    NAXIS2   514                          int
    BUNIT    10**-17 erg/(s cm2 Angstrom) str
    CHECKSUM PCCbR99bPACbP99b             str  HDU checksum updated 2021-07-20T01:03:03
    DATASUM  54356891                     str  data unit checksum updated 2021-07-20T01:03:03
    ======== ============================ ==== ==============================================

Data: FITS image [float32, 2326x514]

HDU10
-----

EXTNAME = R_IVAR

Mask[nspec,nwave] of r-channel flux array.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================================= ==== ==============================================
    KEY      Example Value                     Type Comment
    ======== ================================= ==== ==============================================
    NAXIS1   2326                              int
    NAXIS2   514                               int
    BUNIT    10**+34 (s2 cm4 Angstrom2) / erg2 str
    CHECKSUM GeBDGZ9DGbADGZ7D                  str  HDU checksum updated 2021-07-20T01:03:03
    DATASUM  789948970                         str  data unit checksum updated 2021-07-20T01:03:03
    ======== ================================= ==== ==============================================

Data: FITS image [float32, 2326x514]

HDU11
-----

EXTNAME = R_MASK

Mask[nspec,nwave] of r-channel flux array.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2326             int
    NAXIS2   514              int
    BSCALE   1                int
    BZERO    2147483648       int
    CHECKSUM T5gdV3dcT3dcT3dc str  HDU checksum updated 2021-07-20T01:03:03
    DATASUM  598689           str  data unit checksum updated 2021-07-20T01:03:03
    ======== ================ ==== ==============================================

Data: FITS image [int32, 2326x514]

HDU12
-----

EXTNAME = R_RESOLUTION

Diagonals of r-channel resolution matrix.

See B_RESOLUTION HDU for description of the format.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2326             int
    NAXIS2   11               int
    NAXIS3   514              int
    CHECKSUM DkAIDj3GDjAGDj3G str  HDU checksum updated 2021-07-20T01:03:04
    DATASUM  1927301622       str  data unit checksum updated 2021-07-20T01:03:04
    ======== ================ ==== ==============================================

Data: FITS image [float32, 2326x11x514]

HDU13
-----

EXTNAME = Z_WAVELENGTH

Wavelength[nwave] array in Angstroms of z-channel spectra

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2881             int
    BUNIT    Angstrom         str
    CHECKSUM iaWMkYVMiaVMiYVM str  HDU checksum updated 2021-07-20T01:03:04
    DATASUM  3106662670       str  data unit checksum updated 2021-07-20T01:03:04
    ======== ================ ==== ==============================================

Data: FITS image [float64, 2881]

HDU14
-----

EXTNAME = Z_FLUX

Flux[nspec,nwave] array in 1e-17 erg/(s cm2 Angstrom) of z-channel spectra

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ============================ ==== ==============================================
    KEY      Example Value                Type Comment
    ======== ============================ ==== ==============================================
    NAXIS1   2881                         int
    NAXIS2   514                          int
    BUNIT    10**-17 erg/(s cm2 Angstrom) str
    CHECKSUM 0aea1VdZ0Zda0ZdY             str  HDU checksum updated 2021-07-20T01:03:04
    DATASUM  1889497861                   str  data unit checksum updated 2021-07-20T01:03:04
    ======== ============================ ==== ==============================================

Data: FITS image [float32, 2881x514]

HDU15
-----

EXTNAME = Z_IVAR

Inverse variance of z-channel flux array

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================================= ==== ==============================================
    KEY      Example Value                     Type Comment
    ======== ================================= ==== ==============================================
    NAXIS1   2881                              int
    NAXIS2   514                               int
    BUNIT    10**+34 (s2 cm4 Angstrom2) / erg2 str
    CHECKSUM ni6Dpi3Cni3Cni3C                  str  HDU checksum updated 2021-07-20T01:03:04
    DATASUM  105099897                         str  data unit checksum updated 2021-07-20T01:03:04
    ======== ================================= ==== ==============================================

Data: FITS image [float32, 2881x514]

HDU16
-----

EXTNAME = Z_MASK

Mask[nspec,nwave] of z-channel flux array.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2881             int
    NAXIS2   514              int
    BSCALE   1                int
    BZERO    2147483648       int
    CHECKSUM X6iYY4gYX4gYX4gY str  HDU checksum updated 2021-07-20T01:03:04
    DATASUM  740483           str  data unit checksum updated 2021-07-20T01:03:04
    ======== ================ ==== ==============================================

Data: FITS image [int32, 2881x514]

HDU17
-----

EXTNAME = Z_RESOLUTION

Diagonals of z-channel resolution matrix.

See B_RESOLUTION HDU for description of the format.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2881             int
    NAXIS2   11               int
    NAXIS3   514              int
    CHECKSUM oocZpnbYonbYonbY str  HDU checksum updated 2021-07-20T01:03:04
    DATASUM  1564215354       str  data unit checksum updated 2021-07-20T01:03:04
    ======== ================ ==== ==============================================

Data: FITS image [float32, 2881x11x514]

HDU18
-----

EXTNAME = SCORES

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   172              int  length of dimension 1
    NAXIS2   514              int  length of dimension 2
    ENCODING ascii            str
    CHECKSUM XQAAZP89XPAAXP79 str  HDU checksum updated 2021-07-20T01:03:05
    DATASUM  3357773203       str  data unit checksum updated 2021-07-20T01:03:05
    ======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

=================== ======= ===== ============================================
Name                Type    Units Description
=================== ======= ===== ============================================
TARGETID            int64         DESI Unique Target ID
INTEG_COADD_FLUX_B  float32       integ. flux in wave. range 4000,5800A
MEDIAN_COADD_FLUX_B float32       median flux in wave. range 4000,5800A
MEDIAN_COADD_SNR_B  float32       median SNR/sqrt(A) in wave. range 4000,5800A
INTEG_COADD_FLUX_R  float32       integ. flux in wave. range 5800,7600A
MEDIAN_COADD_FLUX_R float32       median flux in wave. range 5800,7600A
MEDIAN_COADD_SNR_R  float32       median SNR/sqrt(A) in wave. range 5800,7600A
INTEG_COADD_FLUX_Z  float32       integ. flux in wave. range 7600,9800A
MEDIAN_COADD_FLUX_Z float32       median flux in wave. range 7600,9800A
MEDIAN_COADD_SNR_Z  float32       median SNR/sqrt(A) in wave. range 7600,9800A
TSNR2_GPBDARK_B     float32       GPBDARK B template (S/N)^2
TSNR2_ELG_B         float32       ELG B template (S/N)^2
TSNR2_GPBBRIGHT_B   float32       GPBBRIGHT B template (S/N)^2
TSNR2_LYA_B         float32       LYA B template (S/N)^2
TSNR2_BGS_B         float32       BGS B template (S/N)^2
TSNR2_GPBBACKUP_B   float32       GPBBACKUP B template (S/N)^2
TSNR2_QSO_B         float32       QSO B template (S/N)^2
TSNR2_LRG_B         float32       LRG B template (S/N)^2
TSNR2_GPBDARK_R     float32       GPBDARK R template (S/N)^2
TSNR2_ELG_R         float32       ELG R template (S/N)^2
TSNR2_GPBBRIGHT_R   float32       GPBBRIGHT R template (S/N)^2
TSNR2_LYA_R         float32       LYA R template (S/N)^2
TSNR2_BGS_R         float32       BGS R template (S/N)^2
TSNR2_GPBBACKUP_R   float32       GPBBACKUP R template (S/N)^2
TSNR2_QSO_R         float32       QSO R template (S/N)^2
TSNR2_LRG_R         float32       LRG R template (S/N)^2
TSNR2_GPBDARK_Z     float32       GPBDARK Z template (S/N)^2
TSNR2_ELG_Z         float32       ELG Z template (S/N)^2
TSNR2_GPBBRIGHT_Z   float32       GPBBRIGHT Z template (S/N)^2
TSNR2_LYA_Z         float32       LYA Z template (S/N)^2
TSNR2_BGS_Z         float32       BGS Z template (S/N)^2
TSNR2_GPBBACKUP_Z   float32       GPBBACKUP Z template (S/N)^2
TSNR2_QSO_Z         float32       QSO Z template (S/N)^2
TSNR2_LRG_Z         float32       LRG Z template (S/N)^2
TSNR2_GPBDARK       float32       GPBDARK template (S/N)^2 summed over B,R,Z
TSNR2_ELG           float32       ELG template (S/N)^2 summed over B,R,Z
TSNR2_GPBBRIGHT     float32       GPBBRIGHT template (S/N)^2 summed over B,R,Z
TSNR2_LYA           float32       LYA template (S/N)^2 summed over B,R,Z
TSNR2_BGS           float32       BGS template (S/N)^2 summed over B,R,Z
TSNR2_GPBBACKUP     float32       GPBBACKUP template (S/N)^2 summed over B,R,Z
TSNR2_QSO           float32       QSO template (S/N)^2 summed over B,R,Z
TSNR2_LRG           float32       LRG template (S/N)^2 summed over B,R,Z
=================== ======= ===== ============================================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
