======================================
coadd-SPECTROGRAPH-TILEID-GROUPID.fits
======================================

:Summary: Coadded spectra.
:Naming Convention: ``coadd-SPECTROGRAPH-TILEID-GROUPID.fits``, where
    ``SPECTROGRAPH`` is the spectrograph ID, ``TILEID`` is the tile number and
    ``GROUPID`` depends on the ``GROUPTYPE`` of the tile coadd.
:Regex: ``coadd-[0-9]-[0-9]+-([14]xsubset[1-6]|lowspeedsubset[1-6]|exp[0-9]{8}|thru[0-9]{8}|[0-9]{8})\.fits``
:File Type: FITS, 213 MB

Coadd files contain spectra for multiple targets coadded across exposures
but not across spectrograph cameras.
This file follows nearly the same format as the
:doc:`spectra files <spectra-SPECTROGRAPH-TILEID-GROUPID>`, except there is
one entry per target instead of one entry per exposure per target, and
the FIBERMAP is split into two HDUs:

  * FIBERMAP: values such as fluxes and targeting bits that remain applicable
    for each target even after a coadd.
  * EXP_FIBERMAP: values like fiber offsets and atmospheric seeing that
    apply to the individual exposures contributing to the coadd.

The coadded FIBERMAP also gets some new summary columns,
*e.g.* ``COADD_NUMEXP`` and ``COADD_NUMTILE`` recording the number of
exposures and unique TILEIDs contributing to the coadd.

Contents
========

====== ============ ======== ===================
Number EXTNAME      Type     Contents
====== ============ ======== ===================
HDU00_              IMAGE    Keywords only
HDU01_ FIBERMAP     BINTABLE Coadded fibermap table
HDU02_ EXP_FIBERMAP BINTABLE Per-exposure entries from input fibermaps
HDU03_ B_WAVELENGTH IMAGE    Wavelength array of b-channel spectra
HDU04_ B_FLUX       IMAGE    Flux of b-channel spectra
HDU05_ B_IVAR       IMAGE    Inverse variance of b-channel spectra
HDU06_ B_MASK       IMAGE    Mask of b-channel spectra
HDU07_ B_RESOLUTION IMAGE    Resolution matrices of b-channel spectra
HDU08_ R_WAVELENGTH IMAGE    Wavelength array of r-channel spectra
HDU09_ R_FLUX       IMAGE    Flux of r-channel spectra
HDU10_ R_IVAR       IMAGE    Inverse variance of r-channel spectra
HDU11_ R_MASK       IMAGE    Mask of r-channel spectra
HDU12_ R_RESOLUTION IMAGE    Resolution matrices of r-channel spectra
HDU13_ Z_WAVELENGTH IMAGE    Wavelength array of z-channel spectra
HDU14_ Z_FLUX       IMAGE    Flux of z-channel spectra
HDU15_ Z_IVAR       IMAGE    Inverse variance of z-channel spectra
HDU16_ Z_MASK       IMAGE    Mask of z-channel spectra
HDU17_ Z_RESOLUTION IMAGE    Resolution matrices of z-channel spectra
HDU18_ SCORES       BINTABLE QA scores table
====== ============ ======== ===================

Note: the above is the order in which these HDUs appear in DESI spectroscopic
pipeline output, but the order is arbitrary and they should be read by
name not by number.

FITS Header Units
=================

HDU00
-----

Keywords only.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ========== =============================== ==== ==============================================
    KEY        Example Value                   Type Comment
    ========== =============================== ==== ==============================================
    SPGRP      cumulative                      str  Method of grouping spectra for coadd, e.g. PERNIGHT or CUMULATIVE
    SPGRPVAL   20210205                        int  Group value for this coadd, e.g.
    NIGHT [1]_ 20210708                        int  YEARMMDD night identifier for "pernight" and "cumulative" groups
    TILEID     80605                           int  DESI Tile ID
    SPECTRO    2                               int  Spectrograph number
    PETAL      2                               int  Focal plane petal number
    CHECKSUM   AfAMBZ1KAf8KAZ8K                str  HDU checksum updated 2021-07-16T14:01:46
    DATASUM    0                               str  data unit checksum updated 2021-07-16T14:01:46
    FIBERMIN   1000                            int  First fiber number included in this coadd
    INFIL000   spectra-2-545-thru20210510.fits str  Input file(s) contributing to this coadd
    LONGSTRN   OGIP 1.0                        str
    ========== =============================== ==== ==============================================

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
    NAXIS1   387              int
    NAXIS2   500              int  Number of targets
    ENCODING ascii            str
    LONGSTRN OGIP 1.0         str
    CHECKSUM H5Z5H5Z3H5Z3H5Z3 str  HDU checksum updated 2021-07-16T14:01:46
    DATASUM  4214162542       str  data unit checksum updated 2021-07-16T14:01:46
    ======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

========================== ======= ============ ===============================================================================================================================
Name                       Type    Units        Description
========================== ======= ============ ===============================================================================================================================
TARGETID                   int64                Unique DESI target ID
PETAL_LOC                  int16                Petal location [0-9]
DEVICE_LOC                 int32                Device location on focal plane [0-523]
LOCATION                   int64                Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBER                      int32                Fiber ID on the CCDs [0-4999]
COADD_FIBERSTATUS          int32                bitwise-AND of input FIBERSTATUS
TARGET_RA                  float64 deg          Barycentric right ascension in ICRS
TARGET_DEC                 float64 deg          Barycentric declination in ICRS
PMRA                       float32 mas yr^-1    proper motion in the +RA direction (already including cos(dec))
PMDEC                      float32 mas yr^-1    Proper motion in the +Dec direction
REF_EPOCH                  float32 yr           Reference epoch for Gaia/Tycho astrometry. Typically 2015.5 for Gaia
LAMBDA_REF                 float32 Angstrom     Requested wavelength at which targets should be centered on fibers
FA_TARGET                  int64                Targeting bit internally used by fiberassign (linked with FA_TYPE)
FA_TYPE                    binary               Fiberassign internal target type (science, standard, sky, safe, suppsky)
OBJTYPE                    char[3]              Object type: TGT, SKY, NON, BAD
FIBERASSIGN_X              float32 mm           Fiberassign expected CS5 X location on focal plane
FIBERASSIGN_Y              float32 mm           Fiberassign expected CS5 Y location on focal plane
PRIORITY                   int32                Target current priority
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
PHOTSYS                    char[1]              &#x27;N&#x27; for the MzLS/BASS photometric system, &#x27;S&#x27; for DECaLS
PRIORITY_INIT              int64                Target initial priority from target selection bitmasks and OBSCONDITIONS
NUMOBS_INIT                int64                Initial number of observations for target calculated across target selection bitmasks and OBSCONDITIONS
SV1_DESI_TARGET [1]_       int64                DESI (dark time program) target selection bitmask for SV1
SV1_BGS_TARGET [1]_        int64                BGS (bright time program) target selection bitmask for SV1
SV1_MWS_TARGET [1]_        int64                MWS (bright time program) target selection bitmask for SV1
SV1_SCND_TARGET [1]_       int64                Secondary target selection bitmask for SV1
SV3_DESI_TARGET [1]_       int64                DESI (dark time program) target selection bitmask for SV3
SV3_BGS_TARGET [1]_        int64                BGS (bright time program) target selection bitmask for SV3
SV3_MWS_TARGET [1]_        int64                MWS (bright time program) target selection bitmask for SV3
SV3_SCND_TARGET [1]_       int64                Secondary target selection bitmask for SV3
DESI_TARGET                int64                DESI (dark time program) target selection bitmask
BGS_TARGET                 int64                BGS (Bright Galaxy Survey) target selection bitmask
MWS_TARGET                 int64                Milky Way Survey targeting bits
SCND_TARGET [1]_           int64                Target selection bitmask for secondary programs
PLATE_RA                   float64 deg          Barycentric Right Ascension in ICRS to be used by PlateMaker
PLATE_DEC                  float64 deg          Barycentric Declination in ICRS to be used by PlateMaker
TILEID                     int32                Unique DESI tile ID
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
MEAN_FIBER_X               float32 mm           Mean (over exposures) fiber CS5 X location on focal plane
MEAN_FIBER_Y               float32 mm           Mean (over exposures) fiber CS5 Y location on focal plane
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
    NAXIS1   162              int
    NAXIS2   1000             int  Number of input target exposures
    ENCODING ascii            str
    CHECKSUM 3f5X4e3U3e3U3e3U str  HDU checksum updated 2021-07-16T14:01:46
    DATASUM  360255485        str  data unit checksum updated 2021-07-16T14:01:46
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

Wavelength grid of spectra from the B camera.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2751             int  Number of wavelength bins
    BUNIT    Angstrom         str
    CHECKSUM 7CGAA9F99AFAA9F9 str  HDU checksum updated 2021-07-16T14:01:46
    DATASUM  979185614        str  data unit checksum updated 2021-07-16T14:01:46
    ======== ================ ==== ==============================================

Data: FITS image [float64, 2751]

HDU04
-----

EXTNAME = B_FLUX

Extracted spectral flux from the B camera.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ============================ ==== ==============================================
    KEY      Example Value                Type Comment
    ======== ============================ ==== ==============================================
    NAXIS1   2751                         int  Number of wavelength bins
    NAXIS2   500                          int  Number of spectra
    BUNIT    10**-17 erg/(s cm2 Angstrom) str
    CHECKSUM lgKZngKZlgKZlgKZ             str  HDU checksum updated 2021-07-16T14:01:46
    DATASUM  1157856797                   str  data unit checksum updated 2021-07-16T14:01:46
    ======== ============================ ==== ==============================================

Data: FITS image [float32, 2751x500]

HDU05
-----

EXTNAME = B_IVAR

Inverse variance of the B_FLUX HDU.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================================= ==== ==============================================
    KEY      Example Value                     Type Comment
    ======== ================================= ==== ==============================================
    NAXIS1   2751                              int  Number of wavelength bins
    NAXIS2   500                               int  Number of spectra
    BUNIT    10**+34 (s2 cm4 Angstrom2) / erg2 str
    CHECKSUM JATXJASUJASUJASU                  str  HDU checksum updated 2021-07-16T14:01:47
    DATASUM  2428790047                        str  data unit checksum updated 2021-07-16T14:01:47
    ======== ================================= ==== ==============================================

Data: FITS image [float32, 2751x500]

HDU06
-----

EXTNAME = B_MASK

Mask for B-camera flux values.  0=good.
See the :doc:`bitmask documentation </bitmasks>` for definitions of
individual bits.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2751             int  Number of wavelength bins
    NAXIS2   500              int  Number of spectra
    BSCALE   1                int
    BZERO    2147483648       int
    CHECKSUM W4fLW4dLW4dLW4dL str  HDU checksum updated 2021-07-16T14:01:47
    DATASUM  688030           str  data unit checksum updated 2021-07-16T14:01:47
    ======== ================ ==== ==============================================

Data: FITS image [int32, 2751x500]

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
    NAXIS3   500              int  Number of spectra
    CHECKSUM 1l9M1i6K1i6K1i6K str  HDU checksum updated 2021-07-16T14:01:50
    DATASUM  1827421509       str  data unit checksum updated 2021-07-16T14:01:50
    ======== ================ ==== ==============================================

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

Wavelength grid of spectra from the R camera.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2326             int  Number of wavelength bins
    BUNIT    Angstrom         str
    CHECKSUM 7JPAAHO78HOAAHO7 str  HDU checksum updated 2021-07-16T14:01:51
    DATASUM  456732359        str  data unit checksum updated 2021-07-16T14:01:51
    ======== ================ ==== ==============================================

Data: FITS image [float64, 2326]

HDU09
-----

EXTNAME = R_FLUX

Extracted spectral flux from the R camera.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ============================ ==== ==============================================
    KEY      Example Value                Type Comment
    ======== ============================ ==== ==============================================
    NAXIS1   2326                         int  Number of wavelength bins
    NAXIS2   500                          int  Number of spectra
    BUNIT    10**-17 erg/(s cm2 Angstrom) str
    CHECKSUM M3ENO3BMM3BMM3BM             str  HDU checksum updated 2021-07-16T14:01:51
    DATASUM  640139918                    str  data unit checksum updated 2021-07-16T14:01:51
    ======== ============================ ==== ==============================================

Data: FITS image [float32, 2326x500]

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
    NAXIS1   2326                              int  Number of wavelength bins
    NAXIS2   500                               int  Number of spectra
    BUNIT    10**+34 (s2 cm4 Angstrom2) / erg2 str
    CHECKSUM VDCjYABhVABhVABh                  str  HDU checksum updated 2021-07-16T14:01:51
    DATASUM  2650218726                        str  data unit checksum updated 2021-07-16T14:01:51
    ======== ================================= ==== ==============================================

Data: FITS image [float32, 2326x500]

HDU11
-----

EXTNAME = R_MASK

Mask for R-camera flux values.  0=good.
See the :doc:`bitmask documentation </bitmasks>` for definitions of
individual bits.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2326             int  Number of wavelength bins
    NAXIS2   500              int  Number of spectra
    BSCALE   1                int
    BZERO    2147483648       int
    CHECKSUM m7e4n4e1m4e1m4e1 str  HDU checksum updated 2021-07-16T14:01:51
    DATASUM  582966           str  data unit checksum updated 2021-07-16T14:01:51
    ======== ================ ==== ==============================================

Data: FITS image [int32, 2326x500]

HDU12
-----

EXTNAME = R_RESOLUTION

Resolution matrix stored as diagonals of a 3D sparse matrix.
See the frame file :ref:`RESOLUTION documentation <frame-hdu4-resolution>`
for how thease are interpreted and used.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2326             int  Number of wavelength bins
    NAXIS2   11               int  Number of diagonals
    NAXIS3   500              int  Number of spectra
    CHECKSUM e3FYh09Xe0CXe09X str  HDU checksum updated 2021-07-16T14:01:54
    DATASUM  1488519775       str  data unit checksum updated 2021-07-16T14:01:54
    ======== ================ ==== ==============================================

Data: FITS image [float32, 2326x11x500]

HDU13
-----

EXTNAME = Z_WAVELENGTH

Wavelength grid of spectra from the Z camera.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2881             int  Number of wavelength bins
    BUNIT    Angstrom         str
    CHECKSUM gaVNgYSLgaSLgWSL str  HDU checksum updated 2021-07-16T14:01:54
    DATASUM  3106662670       str  data unit checksum updated 2021-07-16T14:01:54
    ======== ================ ==== ==============================================

Data: FITS image [float64, 2881]

HDU14
-----

EXTNAME = Z_FLUX

Extracted spectral flux from the Z camera.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ============================ ==== ==============================================
    KEY      Example Value                Type Comment
    ======== ============================ ==== ==============================================
    NAXIS1   2881                         int  Number of wavelength bins
    NAXIS2   500                          int  Number of spectra
    BUNIT    10**-17 erg/(s cm2 Angstrom) str
    CHECKSUM 9GPWGFMU9FMUGFMU             str  HDU checksum updated 2021-07-16T14:01:55
    DATASUM  3338246075                   str  data unit checksum updated 2021-07-16T14:01:55
    ======== ============================ ==== ==============================================

Data: FITS image [float32, 2881x500]

HDU15
-----

EXTNAME = Z_IVAR

Inverse variance of the Z_FLUX HDU.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================================= ==== ==============================================
    KEY      Example Value                     Type Comment
    ======== ================================= ==== ==============================================
    NAXIS1   2881                              int  Number of wavelength bins
    NAXIS2   500                               int  Number of spectra
    BUNIT    10**+34 (s2 cm4 Angstrom2) / erg2 str
    CHECKSUM 4Ala47iR4AiX47iX                  str  HDU checksum updated 2021-07-16T14:01:55
    DATASUM  2758170465                        str  data unit checksum updated 2021-07-16T14:01:55
    ======== ================================= ==== ==============================================

Data: FITS image [float32, 2881x500]

HDU16
-----

EXTNAME = Z_MASK

Mask for Z-camera flux values.  0=good.
See the :doc:`bitmask documentation </bitmasks>` for definitions of
individual bits.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2881             int  Number of wavelength bins
    NAXIS2   500              int  Number of spectra
    BSCALE   1                int
    BZERO    2147483648       int
    CHECKSUM 95fkD3fk93fkC3fk str  HDU checksum updated 2021-07-16T14:01:56
    DATASUM  720616           str  data unit checksum updated 2021-07-16T14:01:56
    ======== ================ ==== ==============================================

Data: FITS image [int32, 2881x500]

HDU17
-----

EXTNAME = Z_RESOLUTION

Resolution matrix stored as diagonals of a 3D sparse matrix.
See the frame file :ref:`RESOLUTION documentation <frame-hdu4-resolution>`
for how thease are interpreted and used.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2881             int  Number of wavelength bins
    NAXIS2   11               int  Number of diagonals
    NAXIS3   500              int  Number of spectra
    CHECKSUM DFFSG99QDECQD99Q str  HDU checksum updated 2021-07-16T14:01:59
    DATASUM  500309470        str  data unit checksum updated 2021-07-16T14:01:59
    ======== ================ ==== ==============================================

Data: FITS image [float32, 2881x11x500]

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
    NAXIS2   500              int  Number of spectra
    ENCODING ascii            str
    CHECKSUM EpXcGmWcEmWcEmWc str  HDU checksum updated 2021-07-16T14:01:59
    DATASUM  1286335698       str  data unit checksum updated 2021-07-16T14:01:59
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
:doc:`spectra files <spectra-SPECTROGRAPH-TILEID-GROUPID>` documentation.

The format supports arbitrary channel (camera) names as long as for each channel {X}
there is a set of HDUs named {X}_WAVELENGTH, {X}_FLUX, {X}_IVAR, {X}_MASK,
{X}_RESOLUTION.

For the SURVEY=cmx m33 tile (TILEID=80615) tile and all the SURVEY=sv1 tiles (except TILEID=80971-80976, the dc3r2 ones), proper-motion correction was applied at the :doc:`fiberassign </DESI_TARGET/fiberassign/tiles/TILES_VERSION/TILEXX/fiberassign-TILEID>` design step; thus the following columns can have different values than in the :doc:`desitarget products </DESI_TARGET/TARG_DIR/DR/VERSION/targets/PHASE/RESOLVE/OBSCON/PHASEtargets-OBSCON-RESOLVE-hp-HP>`: ``TARGET_RA``, ``TARGET_DEC``, ``REF_EPOCH``, ``PLATE_RA``, ``PLATE_DEC``, and ``PLATE_REF_EPOCH``.

For targets with a non-zero proper motion, ``FIBER_RA`` and ``FIBER_DEC`` refer to the position at the reference epoch (but note that the proper-motion correction has been applied at the time of the observation, it is just not recorded in ``FIBER_RA`` and ``FIBER_DEC``).
