========================================
spectra-SPECTROGRAPH-TILEID-GROUPID.fits
========================================

:Summary: Collection of non-coadded spectra across exposures and cameras
    for a given TILEID on a given SPECTROGRAPH [0-9].
:Naming Convention: ``spectra-SPECTROGRAPH-TILEID-GROUPID.fits``, where
    ``SPECTROGRAPH`` is the spectrograph ID (0-9),
    ``TILEID`` is the tile number and
    ``GROUPID`` depends on the ``GROUPTYPE`` of the tile coadd.
:Regex: ``spectra-[0-9]-[0-9]+-([14]xsubset[1-6]|lowspeedsubset[1-6]|exp[0-9]{8}|thru[0-9]{8}|[0-9]{8})\.fits``
:File Type: FITS, 198 MB

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

Please see :doc:`coadd files <coadd-SPECTROGRAPH-TILEID-GROUPID>` for a coadded
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

Details are given below, with examples for reading and interpreting the
spectra files at the end.

Note: the table below is the order in which these HDUs appear in DESI spectroscopic
pipeline output, but the order is arbitrary and they should be read by
name not by number.

Contents
========

====== ============ ======== ===================
Number EXTNAME      Type     Contents
====== ============ ======== ===================
HDU00_              IMAGE    Keywords only
HDU01_ FIBERMAP     BINTABLE Target photometry, metadata, and what fibers they are assigned to
HDU02_ SCORES       BINTABLE QA metrics calculated from the data
HDU03_ B_WAVELENGTH IMAGE    Wavelength grid from the B-cameras
HDU04_ B_FLUX       IMAGE    Spectral Flux, 10^{-17} erg/s/cm2/Angstrom
HDU05_ B_IVAR       IMAGE    Inverse variance of B_FLUX
HDU06_ B_MASK       BINTABLE Mask, 0=good
HDU07_ B_RESOLUTION IMAGE    Resolution Matrix diagonals
HDU08_ R_WAVELENGTH IMAGE    Wavelength grid from the R-cameras
HDU09_ R_FLUX       IMAGE    Spectral Flux, 10^{-17} erg/s/cm2/Angstrom
HDU10_ R_IVAR       IMAGE    Inverse variance of R_FLUX
HDU11_ R_MASK       BINTABLE Mask, 0=good
HDU12_ R_RESOLUTION IMAGE    Resolution Matrix diagonals
HDU13_ Z_WAVELENGTH IMAGE    Wavelength grid from the Z-cameras
HDU14_ Z_FLUX       IMAGE    Spectral Flux, 10^{-17} erg/s/cm2/Angstrom
HDU15_ Z_IVAR       IMAGE    Inverse variance of Z_FLUX
HDU16_ Z_MASK       BINTABLE Mask, 0=good
HDU17_ Z_RESOLUTION IMAGE    Resolution Matrix diagonals
====== ============ ======== ===================

FITS Header Units
=================

HDU00
-----

Keywords only

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ========== ================ ==== ==============================================
    KEY        Example Value    Type Comment
    ========== ================ ==== ==============================================
    SPGRP      pernight         str  :doc:`GROUPTYPE <../../../index>` how these spectra are grouped
    SPGRPVAL   20201215         int  :doc:`GROUPID <../../../index>` value
    TILEID     80605            int  Integer tile ID
    SPECTRO    6                int  Spectrograph number (same as PETAL)
    PETAL      6                int  Focal plane petal number (same as SPECTRO)
    CHECKSUM   cXXRdWUQcWUQcWUQ str  HDU checksum updated 2021-07-15T00:33:13
    DATASUM    0                str  data unit checksum updated 2021-07-15T00:33:13
    ========== ================ ==== ==============================================

    Depending upon the SPGRP=GROUPTYPE, there may be additional keywords with more
    human-friendly names for the SPGRPVAL, e.g.

    .. rst-class:: keywords

    =============== ==============
    SPGRP=GROUPTYPE Extra keywords
    =============== ==============
    cumulative      NIGHT: all data through this YEARMMDD
    pernight        NIGHT: only data on this YEARMMDD
    perexp          NIGHT, EXPID: only data from this YEARMMDD and exposure ID
    =============== ==============

HDU 0 does not contain any data.

HDU01
-----

EXTNAME = FIBERMAP

Fibermap information combining the targeting photometry and metadata,
fiberassign requested positions, and actual as-observed fiber locations.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   413              int  Width of table in bytes
    NAXIS2   500              int  Number of unique targets (table rows)
    CHECKSUM TcPqUbPoTbPoTbPo str  HDU checksum
    DATASUM  1051947488       str  data unit checksum
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
PHOTSYS               char[1]              &#x27;N&#x27; for the MzLS/BASS photometric system, &#x27;S&#x27; for DECaLS
PRIORITY_INIT         int64                Target initial priority from target selection bitmasks and OBSCONDITIONS
NUMOBS_INIT           int64                Initial number of observations for target calculated across target selection bitmasks and OBSCONDITIONS
SV1_DESI_TARGET [1]_  int64                DESI (dark time program) target selection bitmask for SV1
SV1_BGS_TARGET [1]_   int64                BGS (bright time program) target selection bitmask for SV1
SV1_MWS_TARGET [1]_   int64                MWS (bright time program) target selection bitmask for SV1
SV1_SCND_TARGET [1]_  int64                Secondary target selection bitmask for SV1
SV3_DESI_TARGET [1]_  int64                DESI (dark time program) target selection bitmask for SV3
SV3_BGS_TARGET [1]_   int64                BGS (bright time program) target selection bitmask for SV3
SV3_MWS_TARGET [1]_   int64                MWS (bright time program) target selection bitmask for SV3
SV3_SCND_TARGET [1]_  int64                Secondary target selection bitmask for SV3
DESI_TARGET           int64                DESI (dark time program) target selection bitmask
BGS_TARGET            int64                BGS (Bright Galaxy Survey) target selection bitmask
MWS_TARGET            int64                Milky Way Survey targeting bits
SCND_TARGET [1]_      int64                Target selection bitmask for secondary programs
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
    NAXIS2 500           int  ``nspec`` number of rows in table
    ====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

See the :doc:`cframe SCORES HDU </DESI_SPECTRO_REDUX/SPECPROD/exposures/NIGHT/EXPID/cframe-CAMERA-EXPID>`
documentation for details about the columns.

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
    NAXIS1 2751          int  number of wavelengths
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
    NAXIS2 500                          int  ``nspec`` number of spectra
    BUNIT  10**-17 erg/(s cm2 Angstrom) str
    ====== ============================ ==== =====================

Data: FITS image [float32, 2751x500]

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
    NAXIS2 500                               int  ``nspec`` number of spectra
    BUNIT  10**+34 (s2 cm4 Angstrom2) / erg2 str
    ====== ================================= ==== =====================

Data: FITS image [float32, 2751x500]

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
    NAXIS2 500           int  ``nspec`` number of spectra
    BZERO  2147483648    int  offset data range to that of unsigned long
    BSCALE 1             int  default scaling factor
    ====== ============= ==== ==========================================

Data: FITS image [int32 (compressed), 2751x500]

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
    NAXIS3 500           int  ``nspec`` number of spectra
    ====== ============= ==== =====================

Data: FITS image [float32, 2751x11x500]

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
    NAXIS2 500                          int  ``nspec`` number of spectra
    BUNIT  10**-17 erg/(s cm2 Angstrom) str
    ====== ============================ ==== =====================

Data: FITS image [float32, 2326x500]

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
    NAXIS2 500                               int  ``nspec`` number of spectra
    BUNIT  10**+34 (s2 cm4 Angstrom2) / erg2 str
    ====== ================================= ==== =====================

Data: FITS image [float32, 2326x500]

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
    NAXIS2 500           int  ``nspec`` number of spectra
    BZERO  2147483648    int  offset data range to that of unsigned long
    BSCALE 1             int  default scaling factor
    ====== ============= ==== ==========================================

Data: FITS image [int32 (compressed), 2326x500]

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
    NAXIS1 2326          int  ``nwave`` number of wavelengths
    NAXIS2 11            int  ``ndiag`` number of diagonals
    NAXIS3 500           int  ``nspec`` number of spectra
    ====== ============= ==== =====================

Data: FITS image [float32, 2326x11x500]

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
    NAXIS2 500                          int  ``nspec`` number of spectra
    BUNIT  10**-17 erg/(s cm2 Angstrom) str
    ====== ============================ ==== =====================

Data: FITS image [float32, 2881x500]

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
    NAXIS2 500                               int  ``nspec`` number of spectra
    BUNIT  10**+34 (s2 cm4 Angstrom2) / erg2 str
    ====== ================================= ==== =====================

Data: FITS image [float32, 2881x500]

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
    NAXIS2 500           int  ``nspec`` number of spectra
    BZERO  2147483648    int  offset data range to that of unsigned long
    BSCALE 1             int  default scaling factor
    ====== ============= ==== ==========================================

Data: FITS image [int32 (compressed), 2881x500]

HDU17
-----

EXTNAME = Z_RESOLUTION

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
    NAXIS3 500           int  ``nspec`` number of spectra
    ====== ============= ==== =====================

Data: FITS image [float32, 2881x11x500]


Notes and Examples
==================

Spectra can be read and plotted with Python code like::

    from astropy.io import fits

    wave = dict()
    flux = dict()
    with fits.open('spectra-0-100-thru20210505.fits.gz') as hdus:
        for camera in ['B', 'R', 'Z']:
            wave[camera] = hdus[f'{camera}_WAVELENGTH'].data
            flux[camera] = hdus[f'{camera}_FLUX'].data

    import matplotlib.pyplot as plt
    plt.figure(figsize=(6,3))
    ispec = 217
    for camera in wave.keys():
        plt.plot(wave[camera], flux[camera][ispec])

    plt.xlabel('Wavelength [Angstrom]')
    plt.ylabel('Flux [1e-17 erg/s/cm2/Angstrom]')
    plt.tight_layout()
    plt.show()

.. image:: example_spectrum.png

The `desispec <https://github.com/desihub/desispec>`_ package provides
utility functions and classes for reading, slicing, combining, and writing
spectra.  e.g. the same plot can be made with::

    from desispec.io import read_spectra
    sp = read_spectra('spectra-0-100-thru20210505.fits.gz')

    import matplotlib.pyplot as plt
    plt.figure(figsize=(6,3))
    ispec = 217
    for camera in sp.bands:
        plt.plot(sp.wave[camera], sp.flux[camera][ispec])

    plt.xlabel('Wavelength [Angstrom]')
    plt.ylabel('Flux [1e-17 erg/s/cm2/Angstrom]')
    plt.tight_layout()
    plt.show()

or multiple spectra files can be read, sub-selected, combined, and re-written with::

    from desispec.io import read_spectra, write_spectra
    from desispec.spectra import stack
    spectra = list()
    for petal in range (10):
        sp = read_spectra(f'spectra-{petal}-100-thru20210505.fits')
        keep = sp.fibermap['FLUX_R'] > 10**((22.5-17)/2.5)   # mag_r > 17
        spectra.append(sp[keep])

    combined_spectra = stack(spectra)
    write_spectra('bright_spectra.fits', combined_spectra)


The format supports arbitrary channel (camera) names as long as for each channel {X}
there is a set of HDUs named {X}_WAVELENGTH, {X}_FLUX, {X}_IVAR, {X}_MASK,
{X}_RESOLUTION.

The contents of the spectra files are a reformatting of the data in multiple
input :doc:`cframe files </DESI_SPECTRO_REDUX/SPECPROD/exposures/NIGHT/EXPID/cframe-CAMERA-EXPID>` files.
Spectra files do not contain any additional information or calculations beyond
what is already in the cframe files, but they provide an analysis convenience
to get all the data for a given tile petal or healpix in a single file without
having to find and read multiple cframe files across multiple nights,
exposures, and cameras.

The FIBERMAP and SCORES tables are concatenated from the input cframe files,
with one row per target per exposure.  The WAVELENGTH, FLUX, IVAR, MASK,
and RESOLUTION HDUs of the input cframes are combined and stored here
with a \[BRZ\]\_ prefix, e.g. B_FLUX for the stack of all FLUX HDUs from
the input B-camera cframes.

