================================
coadd-SURVEY-PROGRAM-PIXNUM.fits
================================

:Summary: This holds the calibrated coadded spectra organized by healpix location
    on the sky.
:Naming Convention: ``coadd-SURVEY-PROGRAM-PIXNUM.fits``, where ``SURVEY`` is
    *e.g.* ``main`` or ``sv1``, ``PROGRAM`` is *e.g.* ``bright`` or ``dark``
    and ``PIXNUM`` is the HEALPixel number.
:Regex: ``coadd-(cmx|main|special|sv1|sv2|sv3)-(backup|bright|dark|other)-[0-9]+\.fits``
:File Type: FITS, 219 MB

This file follows nearly the same format as the
:doc:`spectra files <spectra-SURVEY-PROGRAM-PIXNUM>`, except there is
one entry per target instead of one entry per exposure per target, and
the FIBERMAP replaces some exposure-specific columns with summary columns,
e.g. ``NIGHT`` becomes ``FIRST_NIGHT``, ``LAST_NIGHT``, and ``NUM_NIGHT``.

Contents
========

====== ============ ======== ===================
Number EXTNAME      Type     Contents
====== ============ ======== ===================
HDU00_              IMAGE    Keywords only
HDU01_ FIBERMAP     BINTABLE fibermap table
HDU02_ EXP_FIBERMAP BINTABLE Per-exposure entries from input fibermaps
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

Note: the above is the order in which these HDUs appear in DESI spectroscopic
pipeline output, but the order is arbitrary and they should be read by
name not by number.

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
    SPGRP    healpix                     str  Method of grouping spectra (always healpix for this file)
    SPGRPVAL 38863                       int  Healpix number
    HPXPIXEL 38863                       int  Healpix number
    HPXNSIDE 64                          int  Healpix nside
    HPXNEST  True                        str  Healpix nested? (vs. ring)
    SURVEY   sv3                         str  DESI survey (sv1, sv3, main...)
    PROGRAM  dark                        str  DESI program (dark, bright, ...)
    CHECKSUM 96ZDB6YB96YBA6YB            str  HDU checksum updated 2021-07-20T01:03:03
    DATASUM  0                           str  data unit checksum updated 2021-07-20T01:03:03
    FIBERMIN -513                        int
    INFIL000 spectra-sv1-dark-38863.fits str
    LONGSTRN OGIP 1.0                    str
    ======== =========================== ==== ==============================================

Empty HDU.

HDU01
-----

EXTNAME = FIBERMAP

Fibermap information combining the targeting photometry and metadata,
and fiberassign requested positions.  In the coadds, this HDU contains
only the information that remains applicable to coadded spectra, e.g.
the target flux values.  Values that are only meaningful per-exposure
(*e.g.* FIBER_X, FIBER_Y) are contained in the separate
`EXP_FIBERMAP <#hdu02>`_ HDU.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   341              int  Width of table in bytes
    NAXIS2   514              int  Number of targets
    ENCODING ascii            str
    LONGSTRN OGIP 1.0         str
    CHECKSUM 4aNU7WKR4aKR4UKR str  HDU checksum updated 2021-07-20T01:03:03
    DATASUM  4121667036       str  data unit checksum updated 2021-07-20T01:03:03
    ======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

========================== ======= ============ ===============================================================================================================================
Name                       Type    Units        Description
========================== ======= ============ ===============================================================================================================================
TARGETID                   int64                Unique DESI target ID
COADD_FIBERSTATUS          int32                bitwise-AND of input FIBERSTATUS
TARGET_RA                  float64 deg          Barycentric right ascension in ICRS
TARGET_DEC                 float64 deg          Barycentric declination in ICRS
PMRA                       float32 mas yr^-1    proper motion in the +RA direction (already including cos(dec))
PMDEC                      float32 mas yr^-1    Proper motion in the +Dec direction
REF_EPOCH                  float32 yr           Reference epoch for Gaia/Tycho astrometry. Typically 2015.5 for Gaia
FA_TARGET                  int64                Targeting bit internally used by fiberassign (linked with FA_TYPE)
FA_TYPE                    binary               Fiberassign internal target type (science, standard, sky, safe, suppsky)
OBJTYPE                    char[3]              Object type: TGT, SKY, NON, BAD
SUBPRIORITY                float64              Random subpriority [0-1) to break assignment ties
OBSCONDITIONS              int32                Bitmask of allowed observing conditions
RELEASE                    int16                Imaging surveys release ID
BRICKID                    int32                Brick ID from tractor input
BRICK_OBJID                int32                Imaging Surveys OBJID on that brick
MORPHTYPE                  char[4]              Imaging Surveys morphological type from Tractor
FLUX_G                     float32 nanomaggy    Flux in the Legacy Survey g-band (AB)
FLUX_R                     float32 nanomaggy    Flux in the Legacy Survey r-band (AB)
FLUX_Z                     float32 nanomaggy    Flux in the Legacy Survey z-band (AB)
FLUX_IVAR_G                float32 nanomaggy^-2 Inverse variance of FLUX_G (AB)
FLUX_IVAR_R                float32 nanomaggy^-2 Inverse variance of FLUX_R (AB)
FLUX_IVAR_Z                float32 nanomaggy^-2 Inverse variance of FLUX_Z (AB)
MASKBITS                   int16                Bitwise mask from the imaging indicating potential issue or blending
REF_ID                     int64                Tyc1*1,000,000+Tyc2*10+Tyc3 for Tycho-2; “sourceid” for Gaia DR2
REF_CAT                    char[2]              Reference catalog source for star: “T2” for Tycho-2, “G2” for Gaia DR2, “L2” for the SGA, empty otherwise
GAIA_PHOT_G_MEAN_MAG       float32 mag          Gaia G band magnitude
GAIA_PHOT_BP_MEAN_MAG      float32 mag          Gaia BP band magnitude
GAIA_PHOT_RP_MEAN_MAG      float32 mag          Gaia RP band magnitude
PARALLAX                   float32 mas          Reference catalog parallax
BRICKNAME                  char[8]              Brick name from tractor input
EBV                        float32 mag          Galactic extinction E(B-V) reddening from SFD98
FLUX_W1                    float32 nanomaggy    WISE flux in W1 (AB)
FLUX_W2                    float32 nanomaggy    WISE flux in W2 (AB)
FLUX_IVAR_W1               float32 nanomaggy^-2 Inverse variance of FLUX_W1 (AB)
FLUX_IVAR_W2               float32 nanomaggy^-2 Inverse variance of FLUX_W2 (AB)
FIBERFLUX_G                float32 nanomaggy    Predicted g-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERFLUX_R                float32 nanomaggy    Predicted r-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERFLUX_Z                float32 nanomaggy    Predicted z-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERTOTFLUX_G             float32 nanomaggy    Predicted g-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
FIBERTOTFLUX_R             float32 nanomaggy    Predicted r-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
FIBERTOTFLUX_Z             float32 nanomaggy    Predicted z-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
SERSIC                     float32              Power-law index for the Sersic profile model (MORPHTYPE=”SER”)
SHAPE_R                    float32 arcsec       Half-light radius of galaxy model (&gt;0)
SHAPE_E1                   float32              Ellipticity component 1 of galaxy model for galaxy type MORPHTYPE
SHAPE_E2                   float32              Ellipticity component 2 of galaxy model for galaxy type MORPHTYPE
PHOTSYS                    char[1]              'N' for the MzLS/BASS photometric system, 'S' for DECaLS
PRIORITY_INIT              int64                Target initial priority from target selection bitmasks and OBSCONDITIONS
NUMOBS_INIT                int64                Initial number of observations for target calculated across target selection bitmasks and OBSCONDITIONS
SV1_DESI_TARGET [1]_       int64                DESI (dark time program) target selection bitmask for SV1
SV1_BGS_TARGET [1]_        int64                BGS (bright time program) target selection bitmask for SV1
SV1_MWS_TARGET [1]_        int64                MWS (bright time program) target selection bitmask for SV1
SV1_SCND_TARGET [1]_       int64                Secondary target selection bitmask for SV1
DESI_TARGET                int64                DESI (dark time program) target selection bitmask
BGS_TARGET                 int64                BGS (Bright Galaxy Survey) target selection bitmask
MWS_TARGET                 int64                Milky Way Survey targeting bits
SCND_TARGET                int64                Target selection bitmask for secondary programs
PLATE_RA                   float64 deg          Barycentric Right Ascension in ICRS to be used by PlateMaker
PLATE_DEC                  float64 deg          Barycentric Declination in ICRS to be used by PlateMaker
COADD_NUMEXP               int16                Number of exposures in coadd
COADD_EXPTIME              float32 s            Summed exposure time for coadd
COADD_NUMNIGHT             int16                Number of nights in coadd
COADD_NUMTILE              int16                Number of tiles in coadd
MEAN_DELTA_X               float32 mm           Mean (over exposures) fiber difference requested - actual CS5 X location on focal plane
RMS_DELTA_X                float32 mm           RMS (over exposures) of the fiber difference between measured and requested CS5 X location on focal plane
MEAN_DELTA_Y               float32 mm           Mean (over exposures) fiber difference requested - actual CS5 Y location on focal plane
RMS_DELTA_Y                float32 mm           RMS (over exposures) of the fiber difference between measured and requested CS5 Y location on focal plane
MEAN_FIBER_RA              float64 deg          Mean (over exposures) RA of actual fiber position
STD_FIBER_RA               float32 arcsec       Standard deviation (over exposures) of RA of actual fiber position
MEAN_FIBER_DEC             float64 deg          Mean (over exposures) DEC of actual fiber position
STD_FIBER_DEC              float32 arcsec       Standard deviation (over exposures) of DEC of actual fiber position
MEAN_PSF_TO_FIBER_SPECFLUX float32              Mean of input exposures fraction of light from point-like source captured by 1.5 arcsec diameter fiber given atmospheric seeing
========================== ======= ============ ===============================================================================================================================

.. [1] Optional

HDU02
-----

EXTNAME = EXP_FIBERMAP

Fibermap entries that only apply to individual exposures, not to a coadd.
This table has one row per input target per exposure.
Also see the `FIBERMAP <#hdu01>`_ HDU for coadded fibermap quantities
with one row per target.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   162              int  Width of table in bytes
    NAXIS2   7112             int  Number of input target-exposures
    ENCODING ascii            str
    CHECKSUM g3Nmh2Nlg2Nlg2Nl str  HDU checksum updated 2021-07-20T01:03:03
    DATASUM  3607867694       str  data unit checksum updated 2021-07-20T01:03:03
    ======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

===================== ======= ======== =======================================================================================================
Name                  Type    Units    Description
===================== ======= ======== =======================================================================================================
TARGETID              int64            Unique DESI target ID
PRIORITY              int32            Target current priority
SUBPRIORITY           float64          Random subpriority [0-1) to break assignment ties
NIGHT                 int32
EXPID                 int32            DESI Exposure ID number
MJD                   float64          Modified Julian Date when shutter was opened for this exposure
TILEID                int32            Unique DESI tile ID
EXPTIME               float64 s        Length of time shutter was open
PETAL_LOC             int16            Petal location [0-9]
DEVICE_LOC            int32            Device location on focal plane [0-523]
LOCATION              int64            Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBER                 int32            Fiber ID on the CCDs [0-4999]
FIBERSTATUS           int32            Fiber status mask. 0=good
FIBERASSIGN_X         float32 mm       Fiberassign expected CS5 X location on focal plane
FIBERASSIGN_Y         float32 mm       Fiberassign expected CS5 Y location on focal plane
LAMBDA_REF            float32 Angstrom Requested wavelength at which targets should be centered on fibers
PLATE_RA              float64 deg      Barycentric Right Ascension in ICRS to be used by PlateMaker
PLATE_DEC             float64 deg      Barycentric Declination in ICRS to be used by PlateMaker
NUM_ITER              int64            Number of positioner iterations
FIBER_X               float64 mm       CS5 X location requested by PlateMaker
FIBER_Y               float64 mm       CS5 Y location requested by PlateMaker
DELTA_X               float64 mm       CS5 X requested minus actual position
DELTA_Y               float64 mm       CS5 Y requested minus actual position
FIBER_RA              float64 deg      RA of actual fiber position
FIBER_DEC             float64 deg      DEC of actual fiber position
PSF_TO_FIBER_SPECFLUX float64          fraction of light from point-like source captured by 1.5 arcsec diameter fiber given atmospheric seeing
===================== ======= ======== =======================================================================================================

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
    NAXIS1   2751             int  Number of wavelength bins
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
    NAXIS1   2751                         int  Number of wavelength bins
    NAXIS2   514                          int  Number of spectra
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
    NAXIS1   2751                              int  Number of wavelength bings
    NAXIS2   514                               int  Number of spectra
    BUNIT    10**+34 (s2 cm4 Angstrom2) / erg2 str
    CHECKSUM 1AE635E61AE613E6                  str  HDU checksum updated 2021-07-20T01:03:03
    DATASUM  2902189966                        str  data unit checksum updated 2021-07-20T01:03:03
    ======== ================================= ==== ==============================================

Data: FITS image [float32, 2751x514]

HDU06
-----

EXTNAME = B_MASK

Mask[nspec,nwave] of b-channel flux array; 0=good.
See the :doc:`bitmask documentation </bitmasks>` page for the definition of the bits.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2751             int  Number of wavelength bins
    NAXIS2   514              int  Number of spectra
    BSCALE   1                int
    BZERO    2147483648       int
    CHECKSUM 78fA97f677fA77f3 str  HDU checksum updated 2021-07-20T01:03:03
    DATASUM  707110           str  data unit checksum updated 2021-07-20T01:03:03
    ======== ================ ==== ==============================================

Data: FITS image [int32, 2751x514]

HDU07
-----

EXTNAME = B_RESOLUTION

Resolution matrix stored as diagonals of a 3D sparse matrix.
See the frame file :ref:`RESOLUTION documentation <frame-hdu4-resolution>`
for how these are interpreted and used.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2751             int  Number of wavelength bins
    NAXIS2   11               int  Number of diagonals
    NAXIS3   514              int  Number of spectra
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
    NAXIS1   2326             int  Number of wavelength bins
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
    NAXIS1   2326                         int  Number of wavelength bins
    NAXIS2   514                          int  Number of spectra
    BUNIT    10**-17 erg/(s cm2 Angstrom) str
    CHECKSUM PCCbR99bPACbP99b             str  HDU checksum updated 2021-07-20T01:03:03
    DATASUM  54356891                     str  data unit checksum updated 2021-07-20T01:03:03
    ======== ============================ ==== ==============================================

Data: FITS image [float32, 2326x514]

HDU10
-----

EXTNAME = R_IVAR

Inverse variance of the R_FLUX HDU.

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

Mask[nspec,nwave] of r-channel flux array.  0==good.
See the :doc:`bitmask documentation </bitmasks>` page for the definition of the bits.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2326             int  Number of wavelengths
    NAXIS2   514              int  Number of spectra
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
    NAXIS1   2326             int  Number of wavelengths
    NAXIS2   11               int  Number of diagonals
    NAXIS3   514              int  Number of spectra
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
    NAXIS1   2881             int  Number of wavelengths
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
    NAXIS1   2881                         int  Number of wavelengths
    NAXIS2   514                          int  Number of spectra
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
    NAXIS1   2881                              int  Number of wavelengths
    NAXIS2   514                               int  Number of spectra
    BUNIT    10**+34 (s2 cm4 Angstrom2) / erg2 str
    CHECKSUM ni6Dpi3Cni3Cni3C                  str  HDU checksum updated 2021-07-20T01:03:04
    DATASUM  105099897                         str  data unit checksum updated 2021-07-20T01:03:04
    ======== ================================= ==== ==============================================

Data: FITS image [float32, 2881x514]

HDU16
-----

EXTNAME = Z_MASK

Mask[nspec,nwave] of z-channel flux array.  0==good.
See the :doc:`bitmask documentation </bitmasks>` page for the definition of the bits.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2881             int  Number of wavelengths
    NAXIS2   514              int  Number of spectra
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
    NAXIS1   2881             int  Number of wavelengths
    NAXIS2   11               int  Number of diagonals
    NAXIS3   514              int  Number of spectra
    CHECKSUM oocZpnbYonbYonbY str  HDU checksum updated 2021-07-20T01:03:04
    DATASUM  1564215354       str  data unit checksum updated 2021-07-20T01:03:04
    ======== ================ ==== ==============================================

Data: FITS image [float32, 2881x11x514]

HDU18
-----

EXTNAME = SCORES

Scores / metrics measured from the spectra for use in QA and systematics studies.
These are coadded from the input
:doc:`cframe SCORES HDU </DESI_SPECTRO_REDUX/SPECPROD/exposures/NIGHT/EXPID/cframe-CAMERA-EXPID>`
files.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   172              int  Width of table in bytes
    NAXIS2   514              int  Number of spectra
    ENCODING ascii            str
    CHECKSUM XQAAZP89XPAAXP79 str  HDU checksum updated 2021-07-20T01:03:05
    DATASUM  3357773203       str  data unit checksum updated 2021-07-20T01:03:05
    ======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

=================== ======= ===== ============================================================
Name                Type    Units Description
=================== ======= ===== ============================================================
TARGETID            int64         Unique DESI target ID
INTEG_COADD_FLUX_B  float32       integ. flux in wave. range 4000,5800A
MEDIAN_COADD_FLUX_B float32       median flux in wave. range 4000,5800A
MEDIAN_COADD_SNR_B  float32       median SNR/sqrt(A) in wave. range 4000,5800A
INTEG_COADD_FLUX_R  float32       integ. flux in wave. range 5800,7600A
MEDIAN_COADD_FLUX_R float32       median flux in wave. range 5800,7600A
MEDIAN_COADD_SNR_R  float32       median SNR/sqrt(A) in wave. range 5800,7600A
INTEG_COADD_FLUX_Z  float32       integ. flux in wave. range 7600,9800A
MEDIAN_COADD_FLUX_Z float32       median flux in wave. range 7600,9800A
MEDIAN_COADD_SNR_Z  float32       median SNR/sqrt(A) in wave. range 7600,9800A
TSNR2_GPBDARK_B     float32       template (S/N)^2 for dark targets in guider pass band on B
TSNR2_ELG_B         float32       ELG B template (S/N)^2
TSNR2_GPBBRIGHT_B   float32       template (S/N)^2 for bright targets in guider pass band on B
TSNR2_LYA_B         float32       LYA B template (S/N)^2
TSNR2_BGS_B         float32       BGS B template (S/N)^2
TSNR2_GPBBACKUP_B   float32       GPBBACKUP B template (S/N)^2
TSNR2_QSO_B         float32       QSO B template (S/N)^2
TSNR2_LRG_B         float32       LRG B template (S/N)^2
TSNR2_GPBDARK_R     float32       template (S/N)^2 for dark targets in guider pass band on R
TSNR2_ELG_R         float32       ELG R template (S/N)^2
TSNR2_GPBBRIGHT_R   float32       template (S/N)^2 for bright targets in guider pass band on R
TSNR2_LYA_R         float32       LYA R template (S/N)^2
TSNR2_BGS_R         float32       BGS R template (S/N)^2
TSNR2_GPBBACKUP_R   float32       GPBBACKUP R template (S/N)^2
TSNR2_QSO_R         float32       QSO R template (S/N)^2
TSNR2_LRG_R         float32       LRG R template (S/N)^2
TSNR2_GPBDARK_Z     float32       template (S/N)^2 for dark targets in guider pass band on Z
TSNR2_ELG_Z         float32       ELG Z template (S/N)^2
TSNR2_GPBBRIGHT_Z   float32       template (S/N)^2 for bright targets in guider pass band on Z
TSNR2_LYA_Z         float32       LYA Z template (S/N)^2
TSNR2_BGS_Z         float32       BGS Z template (S/N)^2
TSNR2_GPBBACKUP_Z   float32       GPBBACKUP Z template (S/N)^2
TSNR2_QSO_Z         float32       QSO Z template (S/N)^2
TSNR2_LRG_Z         float32       LRG Z template (S/N)^2
TSNR2_GPBDARK       float32       template (S/N)^2 for dark targets in guider pass band
TSNR2_ELG           float32       ELG template (S/N)^2 summed over B,R,Z
TSNR2_GPBBRIGHT     float32       template (S/N)^2 for bright targets in guider pass band
TSNR2_LYA           float32       LYA template (S/N)^2 summed over B,R,Z
TSNR2_BGS           float32       BGS template (S/N)^2 summed over B,R,Z
TSNR2_GPBBACKUP     float32       GPBBACKUP template (S/N)^2 summed over B,R,Z
TSNR2_QSO           float32       QSO template (S/N)^2 summed over B,R,Z
TSNR2_LRG           float32       LRG template (S/N)^2 summed over B,R,Z
=================== ======= ===== ============================================================


Notes and Examples
==================

Coadd files can be read and interpreted using the same code examples
shown in the "Notes and Examples" section of the
:doc:`spectra files </DESI_SPECTRO_REDUX/SPECPROD/tiles/GROUPTYPE/TILEID/GROUPID/spectra-SPECTROGRAPH-TILEID-GROUPID>` documentation.

The format supports arbitrary channel (camera) names as long as for each channel {X}
there is a set of HDUs named {X}_WAVELENGTH, {X}_FLUX, {X}_IVAR, {X}_MASK,
{X}_RESOLUTION.

For the SURVEY=cmx m33 tile (TILEID=80615) tile and all the SURVEY=sv1 tiles (except TILEID=80971-80976, the dc3r2 ones), proper-motion correction was applied at the :doc:`fiberassign </DESI_TARGET/fiberassign/tiles/TILES_VERSION/TILEXX/fiberassign-TILEID>` design step; thus the following columns can have different values than in the :doc:`desitarget products </DESI_TARGET/TARG_DIR/DR/VERSION/targets/PHASE/RESOLVE/OBSCON/PHASEtargets-OBSCON-RESOLVE-hp-HP>`: ``TARGET_RA``, ``TARGET_DEC``, ``REF_EPOCH``, ``PLATE_RA``, ``PLATE_DEC``, and ``PLATE_REF_EPOCH``.

For targets with a non-zero proper motion, ``FIBER_RA`` and ``FIBER_DEC`` refer to the position at the reference epoch (but note that the proper-motion correction has been applied at the time of the observation, it is just not recorded in ``FIBER_RA`` and ``FIBER_DEC``).
