==================================
spectra-SURVEY-PROGRAM-PIXNUM.fits
==================================

:Summary: DESI spectra grouped by nested healpix number
:Naming Convention: ``spectra-SURVEY-PROGRAM-PIXNUM.fits``, where ``SURVEY`` is
    *e.g.* ``main`` or ``sv1``, ``PROGRAM`` is *e.g.* ``bright`` or ``dark``
    and ``PIXNUM`` is the HEALPixel number.
:Regex: ``spectra-(cmx|main|special|sv1|sv2|sv3)-(backup|bright|dark|other)-[0-9]+\.fits``
:File Type: FITS, 408 MB

Spectra files contain non-coadded spectra for multiple targets observed on
multiple individual exposures and cameras.  The format can contain any
arbitrary set of targets, though the standard DESI spectroscopic pipeline
outputs are grouped either by a single petal of a given tile,
or all targets on a single healpix.

Tile-based spectra can be grouped in multiple ways across
exposures and nights;  see the top-level :doc:`SPECPROD/tiles/ <../../../index>`
description for an overview of the per-tile GROUPTYPE and GROUPID options.
Healpix-based spectra are grouped by SURVEY and PROGRAM.
Science analyses may release spectra in other groups, e.g. all the spectra
selected for a particular analysis.

Please see :doc:`coadd files <coadd-SURVEY-PROGRAM-PIXNUM>` for a coadded
version of the same spectra in a very similar format.

The FIBERMAP table contains metadata about each target, with one row per
target per exposure.  The corresponding SCORES table contains quantities
measured from the spectra, also with one row per target per exposure.

The spectra themselves are in a set of image HDUs for the FLUX,
IVAR (inverse variance), MASK, and spectral RESOLUTION, each prefixed
with a spectrograph camera name, e.g. B, R, or Z for DESI, though the format
in general could support other numbers and names of cameras for other
instruments.  A row of each image HDU correponds to the target from the
same row index of the FIBERMAP and SCORES HDUs.

See the end of :doc:`tile-based spectra </DESI_SPECTRO_REDUX/SPECPROD/tiles/GROUPTYPE/TILEID/GROUPID/spectra-SPECTROGRAPH-TILEID-GROUPID>`
for examples of reading this file format.

Note: the table below is the order in which these HDUs appear in DESI spectroscopic
pipeline output, but the order is arbitrary and they should be read by
name not by number.


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

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    SPGRP    healpix          str  Spectral grouping method
    SPGRPVAL 26371            int  Grouping value = healpixel number
    HPXPIXEL 26371            int  Nested nside=64 healpixel number
    HPXNSIDE 64               int  Healpix nside
    HPXNEST  True             str  Healpix nested? (vs. ring)
    SURVEY   main             str  DESI Survey (sv1, sv3, main...)
    PROGRAM  bright           str  DESI Program (dark, bright, ...)
    CHECKSUM 8DPU9BMR8BMR8BMR str  HDU checksum updated 2021-07-19T17:59:29
    DATASUM  0                str  data unit checksum updated 2021-07-19T17:59:29
    ======== ================ ==== ==============================================

Empty HDU.

HDU01
-----

EXTNAME = FIBERMAP

Fibermap table with per-target metdata.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   413              int  Width of table in bytes
    NAXIS2   1031             int  Number of rows in table
    CHECKSUM U9Fia89iV8Cia89i str  HDU checksum
    DATASUM  3589169610       str  data unit checksum
    ======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Propagated from the FIBERMAP HDU of the input :doc:`cframe files </DESI_SPECTRO_REDUX/SPECPROD/exposures/NIGHT/EXPID/cframe-CAMERA-EXPID>`.

.. rst-class:: columns

===================== ======= ============ =========================================================================================================================
Name                  Type    Units        Description
===================== ======= ============ =========================================================================================================================
TARGETID              int64                Unique DESI target ID
PETAL_LOC             int16                Petal location [0-9]
DEVICE_LOC            int32                Device location on focal plane [0-523]
LOCATION              int64                Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBER                 int32                Fiber ID on the CCDs [0-4999]
FIBERSTATUS           int32                Fiber status mask. 0=good
TARGET_RA             float64 deg          Barycentric right ascension in ICRS
TARGET_DEC            float64 deg          Barycentric declination in ICRS
PMRA                  float32 mas yr^-1    proper motion in the +RA direction (already including cos(dec))
PMDEC                 float32 mas yr^-1    Proper motion in the +Dec direction
REF_EPOCH             float32 yr           Reference epoch for Gaia/Tycho astrometry. Typically 2015.5 for Gaia
LAMBDA_REF            float32 Angstrom     Requested wavelength at which targets should be centered on fibers
FA_TARGET             int64                Targeting bit internally used by fiberassign (linked with FA_TYPE)
FA_TYPE               binary               Fiberassign internal target type (science, standard, sky, safe, suppsky)
OBJTYPE               char[3]              Object type: TGT, SKY, NON, BAD
FIBERASSIGN_X         float32 mm           Fiberassign expected CS5 X location on focal plane
FIBERASSIGN_Y         float32 mm           Fiberassign expected CS5 Y location on focal plane
PRIORITY              int32                Target current priority
SUBPRIORITY           float64              Random subpriority [0-1) to break assignment ties
OBSCONDITIONS         int32                Bitmask of allowed observing conditions
RELEASE               int16                Imaging surveys release ID
BRICKID               int32                Brick ID from tractor input
BRICK_OBJID           int32                Imaging Surveys OBJID on that brick
MORPHTYPE             char[4]              Imaging Surveys morphological type from Tractor
FLUX_G                float32 nanomaggy    Flux in the Legacy Survey g-band (AB)
FLUX_R                float32 nanomaggy    Flux in the Legacy Survey r-band (AB)
FLUX_Z                float32 nanomaggy    Flux in the Legacy Survey z-band (AB)
FLUX_IVAR_G           float32 nanomaggy^-2 Inverse variance of FLUX_G (AB)
FLUX_IVAR_R           float32 nanomaggy^-2 Inverse variance of FLUX_R (AB)
FLUX_IVAR_Z           float32 nanomaggy^-2 Inverse variance of FLUX_Z (AB)
MASKBITS              int16                Bitwise mask from the imaging indicating potential issue or blending
REF_ID                int64                Tyc1*1,000,000+Tyc2*10+Tyc3 for Tycho-2; “sourceid” for Gaia DR2
REF_CAT               char[2]              Reference catalog source for star: “T2” for Tycho-2, “G2” for Gaia DR2, “L2” for the SGA, empty otherwise
GAIA_PHOT_G_MEAN_MAG  float32 mag          Gaia G band magnitude
GAIA_PHOT_BP_MEAN_MAG float32 mag          Gaia BP band magnitude
GAIA_PHOT_RP_MEAN_MAG float32 mag          Gaia RP band magnitude
PARALLAX              float32 mas          Reference catalog parallax
BRICKNAME             char[8]              Brick name from tractor input
EBV                   float32 mag          Galactic extinction E(B-V) reddening from SFD98
FLUX_W1               float32 nanomaggy    WISE flux in W1 (AB)
FLUX_W2               float32 nanomaggy    WISE flux in W2 (AB)
FLUX_IVAR_W1          float32 nanomaggy^-2 Inverse variance of FLUX_W1 (AB)
FLUX_IVAR_W2          float32 nanomaggy^-2 Inverse variance of FLUX_W2 (AB)
FIBERFLUX_G           float32 nanomaggy    Predicted g-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERFLUX_R           float32 nanomaggy    Predicted r-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERFLUX_Z           float32 nanomaggy    Predicted z-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERTOTFLUX_G        float32 nanomaggy    Predicted g-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
FIBERTOTFLUX_R        float32 nanomaggy    Predicted r-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
FIBERTOTFLUX_Z        float32 nanomaggy    Predicted z-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
SERSIC                float32              Power-law index for the Sersic profile model (MORPHTYPE=”SER”)
SHAPE_R               float32 arcsec       Half-light radius of galaxy model (&gt;0)
SHAPE_E1              float32              Ellipticity component 1 of galaxy model for galaxy type MORPHTYPE
SHAPE_E2              float32              Ellipticity component 2 of galaxy model for galaxy type MORPHTYPE
PHOTSYS               char[1]              'N' for the MzLS/BASS photometric system, 'S' for DECaLS
PRIORITY_INIT         int64                Target initial priority from target selection bitmasks and OBSCONDITIONS
NUMOBS_INIT           int64                Initial number of observations for target calculated across target selection bitmasks and OBSCONDITIONS
SV1_DESI_TARGET [1]_  int64                DESI (dark time program) target selection bitmask for SV1
SV1_BGS_TARGET [1]_   int64                BGS (bright time program) target selection bitmask for SV1
SV1_MWS_TARGET [1]_   int64                MWS (bright time program) target selection bitmask for SV1
SV1_SCND_TARGET [1]_  int64                Secondary target selection bitmask for SV1
DESI_TARGET           int64                DESI (dark time program) target selection bitmask
BGS_TARGET            int64                BGS (Bright Galaxy Survey) target selection bitmask
MWS_TARGET            int64                Milky Way Survey targeting bits
SCND_TARGET           int64                Target selection bitmask for secondary programs
PLATE_RA              float64 deg          Barycentric Right Ascension in ICRS to be used by PlateMaker
PLATE_DEC             float64 deg          Barycentric Declination in ICRS to be used by PlateMaker
NUM_ITER              int64                Number of positioner iterations
FIBER_X               float64 mm           CS5 X location requested by PlateMaker
FIBER_Y               float64 mm           CS5 Y location requested by PlateMaker
DELTA_X               float64 mm           CS5 X requested minus actual position
DELTA_Y               float64 mm           CS5 Y requested minus actual position
FIBER_RA              float64 deg          RA of actual fiber position
FIBER_DEC             float64 deg          DEC of actual fiber position
EXPTIME               float64 s            Length of time shutter was open
PSF_TO_FIBER_SPECFLUX float64              fraction of light from point-like source captured by 1.5 arcsec diameter fiber given atmospheric seeing
NIGHT                 int32
EXPID                 int32                DESI Exposure ID number
MJD                   float64              Modified Julian Date when shutter was opened for this exposure
TILEID                int32                Unique DESI tile ID
===================== ======= ============ =========================================================================================================================

.. [1] Optional

HDU02
-----

EXTNAME = SCORES

Scores / metrics measured from the spectra for use in QA and systematics studies.
These are propagated from the input
:doc:`cframe SCORES HDU </DESI_SPECTRO_REDUX/SPECPROD/exposures/NIGHT/EXPID/cframe-CAMERA-EXPID>`.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =======================
    KEY    Example Value Type Comment
    ====== ============= ==== =======================
    NAXIS1 488           int  width of table in bytes
    NAXIS2 1031          int  number of rows in table
    ====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

===================== ======= ===== ============================================================
Name                  Type    Units Description
===================== ======= ===== ============================================================
TARGETID              int64         Unique DESI target ID
SUM_RAW_COUNT_B       float64       Sum of raw counts in B camera
MEDIAN_RAW_COUNT_B    float64       Median of raw counts in B camera
MEDIAN_RAW_SNR_B      float64       Median(raw signal/noise) in B camera
SUM_FFLAT_COUNT_B     float64       Sum of fiber-flatfielded counts B camera
MEDIAN_FFLAT_COUNT_B  float64       Median of fiber-flatfielded counts in B camera
MEDIAN_FFLAT_SNR_B    float64       Median(S/N) of fiberflatfielded counts in B camera
SUM_SKYSUB_COUNT_B    float64       Sum of sky-subtracted counts in B camera
MEDIAN_SKYSUB_COUNT_B float64       Median of sky-subtracted counts in B camera
MEDIAN_SKYSUB_SNR_B   float64       Median(S/N) of sky-subtracted counts in B camera
SUM_CALIB_COUNT_B     float64       Sum of calibrated flux in B camera
MEDIAN_CALIB_COUNT_B  float64       Median of calibrated flux in B camera
MEDIAN_CALIB_SNR_B    float64       Median(S/N) of calibrated flux in B camera
TSNR2_GPBDARK_B       float64       template (S/N)^2 for dark targets in guider pass band on B
TSNR2_ELG_B           float64       ELG B template (S/N)^2
TSNR2_GPBBRIGHT_B     float64       template (S/N)^2 for bright targets in guider pass band on B
TSNR2_LYA_B           float64       LYA B template (S/N)^2
TSNR2_BGS_B           float64       BGS B template (S/N)^2
TSNR2_GPBBACKUP_B     float64
TSNR2_QSO_B           float64       QSO B template (S/N)^2
TSNR2_LRG_B           float64       LRG B template (S/N)^2
SUM_RAW_COUNT_R       float64       Sum of raw counts in R camera
MEDIAN_RAW_COUNT_R    float64       Median of raw counts in R camera
MEDIAN_RAW_SNR_R      float64       Median(raw signal/noise) in R camera
SUM_FFLAT_COUNT_R     float64       Sum of fiber-flatfielded counts R camera
MEDIAN_FFLAT_COUNT_R  float64       Median of fiber-flatfielded counts in R camera
MEDIAN_FFLAT_SNR_R    float64       Median(S/N) of fiberflatfielded counts in R camera
SUM_SKYSUB_COUNT_R    float64       Sum of sky-subtracted counts in R camera
MEDIAN_SKYSUB_COUNT_R float64       Median of sky-subtracted counts in R camera
MEDIAN_SKYSUB_SNR_R   float64       Median(S/N) of sky-subtracted counts in R camera
SUM_CALIB_COUNT_R     float64       Sum of calibrated flux in R camera
MEDIAN_CALIB_COUNT_R  float64       Median of calibrated flux in R camera
MEDIAN_CALIB_SNR_R    float64       Median(S/N) of calibrated flux in R camera
TSNR2_GPBDARK_R       float64       template (S/N)^2 for dark targets in guider pass band on R
TSNR2_ELG_R           float64       ELG R template (S/N)^2
TSNR2_GPBBRIGHT_R     float64       template (S/N)^2 for bright targets in guider pass band on R
TSNR2_LYA_R           float64       LYA R template (S/N)^2
TSNR2_BGS_R           float64       BGS R template (S/N)^2
TSNR2_GPBBACKUP_R     float64
TSNR2_QSO_R           float64       QSO R template (S/N)^2
TSNR2_LRG_R           float64       LRG R template (S/N)^2
SUM_RAW_COUNT_Z       float64       Sum of raw counts in Z camera
MEDIAN_RAW_COUNT_Z    float64       Median of raw counts in Z camera
MEDIAN_RAW_SNR_Z      float64       Median(raw signal/noise) in Z camera
SUM_FFLAT_COUNT_Z     float64       Sum of fiber-flatfielded counts Z camera
MEDIAN_FFLAT_COUNT_Z  float64       Median of fiber-flatfielded counts in Z camera
MEDIAN_FFLAT_SNR_Z    float64       Median(S/N) of fiberflatfielded counts in Z camera
SUM_SKYSUB_COUNT_Z    float64       Sum of sky-subtracted counts in Z camera
MEDIAN_SKYSUB_COUNT_Z float64       Median of sky-subtracted counts in Z camera
MEDIAN_SKYSUB_SNR_Z   float64       Median(S/N) of sky-subtracted counts in Z camera
SUM_CALIB_COUNT_Z     float64       Sum of calibrated flux in Z camera
MEDIAN_CALIB_COUNT_Z  float64       Median of calibrated flux in Z camera
MEDIAN_CALIB_SNR_Z    float64       Median(S/N) of calibrated flux in Z camera
TSNR2_GPBDARK_Z       float64       template (S/N)^2 for dark targets in guider pass band on Z
TSNR2_ELG_Z           float64       ELG Z template (S/N)^2
TSNR2_GPBBRIGHT_Z     float64       template (S/N)^2 for bright targets in guider pass band on Z
TSNR2_LYA_Z           float64       LYA Z template (S/N)^2
TSNR2_BGS_Z           float64       BGS Z template (S/N)^2
TSNR2_GPBBACKUP_Z     float64
TSNR2_QSO_Z           float64       QSO Z template (S/N)^2
TSNR2_LRG_Z           float64       LRG Z template (S/N)^2
===================== ======= ===== ============================================================

HDU03
-----

EXTNAME = B_WAVELENGTH

1D array of B-camera wavelengths in Angstrom, in vacuum (not in air),
in the rest frame of the solar system barycenter.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =====================
    KEY    Example Value Type Comment
    ====== ============= ==== =====================
    NAXIS1 2751          int  Number of wavelengths
    BUNIT  Angstrom      str
    ====== ============= ==== =====================

Data: FITS image [float64, 2751]

HDU04
-----

EXTNAME = B_FLUX

2D array of calibrated spectral flux of dimension ``[nspec, nwave]``
in units of 1e-17 erg / (s cm2 Angstrom).
``nspec`` is the number of fibers per camera.
``nwave`` in the length of the wavelength array.
The spectra of all fibers share the same wavelength grid, given in HDU B_WAVELENGTH.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============================ ==== =====================
    KEY    Example Value                Type Comment
    ====== ============================ ==== =====================
    NAXIS1 2751                         int  ``nwave`` number of wavelengths
    NAXIS2 1031                         int  ``nspec`` number of spectra
    BUNIT  10**-17 erg/(s cm2 Angstrom) str
    ====== ============================ ==== =====================

Data: FITS image [float32, 2751x1031]

HDU05
-----

EXTNAME = B_IVAR

Inverse variance of flux (1/sigma^2) in units of (10^{-17} erg/s/cm2/A)^-2.
Uncertainties comprise statistical uncertainties from the error propagation
of the initial CCD pixel variance, the calibration uncertainties,
plus an additional term on bright sky lines to account for the
imperfect sky subtraction.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ================================= ==== =====================
    KEY    Example Value                     Type Comment
    ====== ================================= ==== =====================
    NAXIS1 2751                              int  ``nwave`` number of wavelengths
    NAXIS2 1031                              int  ``nspec`` number of spectra
    BUNIT  10**+34 (s2 cm4 Angstrom2) / erg2 str
    ====== ================================= ==== =====================

Data: FITS image [float32, 2751x1031]

HDU06
-----

EXTNAME = B_MASK

Mask of spectral data; 0=good.
See the :doc:`bitmask documentation </bitmasks>` page for the definition of the bits.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== ==========================================
    KEY    Example Value Type Comment
    ====== ============= ==== ==========================================
    NAXIS1 2751          int  ``nwave`` number of wavelengths
    NAXIS2 1031          int  ``nspec`` number of spectra
    BZERO  2147483648    int  offset data range to that of unsigned long
    BSCALE 1             int  default scaling factor
    ====== ============= ==== ==========================================

Data: FITS image [int32 (compressed), 2751x1031]

HDU07
-----

EXTNAME = B_RESOLUTION

Resolution matrix stored as a 3D sparse matrix, modeling the
per-fiber non-Gaussian effective line-spread-function resolution.
See the :doc:`frame RESOLUTION HDU </DESI_SPECTRO_REDUX/SPECPROD/exposures/NIGHT/EXPID/frame-CAMERA-EXPID>`
documentation for details about using this HDU.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =====================
    KEY    Example Value Type Comment
    ====== ============= ==== =====================
    NAXIS1 2751          int  ``nwave`` number of wavelengths
    NAXIS2 11            int  ``ndiag`` number of diagonals
    NAXIS3 1031          int  ``nspec`` number of spectra
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

1D array of R-camera wavelengths in Angstrom, in vacuum (not in air),
in the rest frame of the solar system barycenter.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =====================
    KEY    Example Value Type Comment
    ====== ============= ==== =====================
    NAXIS1 2326          int  number of wavelengths
    BUNIT  Angstrom      str
    ====== ============= ==== =====================

Data: FITS image [float64, 2326]

HDU09
-----

EXTNAME = R_FLUX

2D array of calibrated spectral flux of dimension ``[nspec, nwave]``
in units of 1e-17 erg / (s cm2 Angstrom).
``nspec`` is the number of fibers per camera.
``nwave`` in the length of the wavelength array.
The spectra of all fibers share the same wavelength grid, given in HDU R_WAVELENGTH.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============================ ==== =====================
    KEY    Example Value                Type Comment
    ====== ============================ ==== =====================
    NAXIS1 2326                         int  ``nwave`` number of wavelengths
    NAXIS2 1031                         int  ``nspec`` number of spectra
    BUNIT  10**-17 erg/(s cm2 Angstrom) str
    ====== ============================ ==== =====================

Data: FITS image [float32, 2326x1031]

HDU10
-----

EXTNAME = R_IVAR

Inverse variance of flux (1/sigma^2) in units of (10^{-17} erg/s/cm2/A)^-2.
Uncertainties comprise statistical uncertainties from the error propagation
of the initial CCD pixel variance, the calibration uncertainties,
plus an additional term on bright sky lines to account for the
imperfect sky subtraction.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ================================= ==== =====================
    KEY    Example Value                     Type Comment
    ====== ================================= ==== =====================
    NAXIS1 2326                              int  ``nwave`` number of wavelengths
    NAXIS2 1031                              int  ``nspec`` number of spectra
    BUNIT  10**+34 (s2 cm4 Angstrom2) / erg2 str
    ====== ================================= ==== =====================

Data: FITS image [float32, 2326x1031]

HDU11
-----

EXTNAME = R_MASK

Mask of spectral data; 0=good.
See the :doc:`bitmask documentation </bitmasks>` page for the definition of the bits.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== ==========================================
    KEY    Example Value Type Comment
    ====== ============= ==== ==========================================
    NAXIS1 2326          int  ``nwave`` number of wavelengths
    NAXIS2 1031          int  ``nspec`` number of spectra
    BZERO  2147483648    int  offset data range to that of unsigned long
    BSCALE 1             int  default scaling factor
    ====== ============= ==== ==========================================

Data: FITS image [int32 (compressed), 2326x1031]

HDU12
-----

EXTNAME = R_RESOLUTION

Resolution matrix stored as a 3D sparse matrix, modeling the
per-fiber non-Gaussian effective line-spread-function resolution.
See the :doc:`frame RESOLUTION HDU </DESI_SPECTRO_REDUX/SPECPROD/exposures/NIGHT/EXPID/frame-CAMERA-EXPID>`
documentation for details about using this HDU.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

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

1D array of Z-camera wavelengths in Angstrom, in vacuum (not in air),
in the rest frame of the solar system barycenter.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =====================
    KEY    Example Value Type Comment
    ====== ============= ==== =====================
    NAXIS1 2881          int  ``nwave`` number of wavelengths
    BUNIT  Angstrom      str
    ====== ============= ==== =====================

Data: FITS image [float64, 2881]

HDU14
-----

EXTNAME = Z_FLUX

2D array of calibrated spectral flux of dimension ``[nspec, nwave]``
in units of 1e-17 erg / (s cm2 Angstrom).
``nspec`` is the number of fibers per camera.
``nwave`` in the length of the wavelength array.
The spectra of all fibers share the same wavelength grid, given in HDU Z_WAVELENGTH.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============================ ==== =====================
    KEY    Example Value                Type Comment
    ====== ============================ ==== =====================
    NAXIS1 2881                         int  ``nwave`` number of wavelengths
    NAXIS2 1031                         int  ``nspec`` number of spectra
    BUNIT  10**-17 erg/(s cm2 Angstrom) str
    ====== ============================ ==== =====================

Data: FITS image [float32, 2881x1031]

HDU15
-----

EXTNAME = Z_IVAR

Inverse variance of flux (1/sigma^2) in units of (10^{-17} erg/s/cm2/A)^-2.
Uncertainties comprise statistical uncertainties from the error propagation
of the initial CCD pixel variance, the calibration uncertainties,
plus an additional term on bright sky lines to account for the
imperfect sky subtraction.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ================================= ==== =====================
    KEY    Example Value                     Type Comment
    ====== ================================= ==== =====================
    NAXIS1 2881                              int  ``nwave`` number of wavelengths
    NAXIS2 1031                              int  ``nspec`` number of spectra
    BUNIT  10**+34 (s2 cm4 Angstrom2) / erg2 str
    ====== ================================= ==== =====================

Data: FITS image [float32, 2881x1031]

HDU16
-----

EXTNAME = Z_MASK

Mask of spectral data; 0=good.
See the :doc:`bitmask documentation </bitmasks>` page for the definition of the bits.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== ==========================================
    KEY    Example Value Type Comment
    ====== ============= ==== ==========================================
    NAXIS1 2881          int  ``nwave`` number of wavelengths
    NAXIS2 1031          int  ``nspec`` number of spectra
    BZERO  2147483648    int  offset data range to that of unsigned long
    BSCALE 1             int  default scaling factor
    ====== ============= ==== ==========================================

Data: FITS image [int32 (compressed), 2881x1031]

HDU17
-----

EXTNAME = Z_RESOLUTION

Diagonals of z-channel resolution matrix.

Resolution matrix stored as a 3D sparse matrix, modeling the
per-fiber non-Gaussian effective line-spread-function resolution.
See the :doc:`frame RESOLUTION HDU </DESI_SPECTRO_REDUX/SPECPROD/exposures/NIGHT/EXPID/frame-CAMERA-EXPID>`
documentation for details about using this HDU.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =====================
    KEY    Example Value Type Comment
    ====== ============= ==== =====================
    NAXIS1 2881          int  ``nwave`` number of wavelengths
    NAXIS2 11            int  ``ndiag`` number of diagonals
    NAXIS3 1031          int  ``nspec`` number of spectra
    ====== ============= ==== =====================

Data: FITS image [float32, 2881x11x1031]


Notes and Examples
==================

The format supports arbitrary channel names as long as for each channel {X}
there is a set of HDUs named {X}_WAVELENGTH, {X}_FLUX, {X}_IVAR, {X}_MASK,
{X}_RESOLUTION.

For the SURVEY=cmx m33 tile (TILEID=80615) tile and all the SURVEY=sv1 tiles (except TILEID=80971-80976, the dc3r2 ones), proper-motion correction was applied at the :doc:`fiberassign </DESI_TARGET/fiberassign/tiles/TILES_VERSION/TILEXX/fiberassign-TILEID>` design step; thus the following columns can have different values than in the :doc:`desitarget products </DESI_TARGET/TARG_DIR/DR/VERSION/targets/PHASE/RESOLVE/OBSCON/PHASEtargets-OBSCON-RESOLVE-hp-HP>`: ``TARGET_RA``, ``TARGET_DEC``, ``REF_EPOCH``, ``PLATE_RA``, ``PLATE_DEC``, and ``PLATE_REF_EPOCH``.

For targets with a non-zero proper motion, ``FIBER_RA`` and ``FIBER_DEC`` refer to the position at the reference epoch (but note that the proper-motion correction has been applied at the time of the observation, it is just not recorded in ``FIBER_RA`` and ``FIBER_DEC``).
