===============
fba-TILEID.fits
===============

:Summary: This type of file is intended to be an "almost complete", but still intermediate,
    version of the final :doc:`fiberassign files <../../../../../DESI_TARGET/fiberassign/TILES_VERSION/TILEXX/fiberassign-TILEID>`.
:Naming Convention: ``fba-{TILEID}.fits``, where ``{TILEID}`` is the zero-padded,
    6-digit TILED.
:Regex: ``fba-[0-9]{6}\.fits``
:File Type: FITS, 9 MB

Contents
========

====== =========== ======== ===================
Number EXTNAME     Type     Contents
====== =========== ======== ===================
HDU0_  PRIMARY     IMAGE    Empty HDU.
HDU1_  FASSIGN     BINTABLE *Brief Description*
HDU2_  FTARGETS    BINTABLE *Brief Description*
HDU3_  FAVAIL      BINTABLE *Brief Description*
HDU4_  GFA_TARGETS BINTABLE Selected star for the ETC / GUIDE / FOCUS
====== =========== ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

This HDU contains header keywords only.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ============= ========================= ===== =======
    KEY           Example Value             Type  Comment
    ============= ========================= ===== =======
    TILEID        1774                      int
    TILERA        222.786                   float
    TILEDEC       41.722                    float
    FIELDROT      -0.113900362856195        float
    FA_PLAN       2022-07-01T00:00:00.000   str
    FA_HA         10.15                     float
    FA_RUN        2021-05-18T21:57:00+00:00 str
    FA_M_GFA [1]_ 0.4                       float
    FA_M_PET [1]_ 0.4                       float
    FA_M_POS [1]_ 0.05                      float
    REQRA         222.786                   float
    REQDEC        41.722                    float
    FIELDNUM      0                         int
    FA_VER        4.0.0                     str
    FA_SURV       main                      str
    ============= ========================= ===== =======

.. [1] Optional

Empty HDU.

HDU1
----

EXTNAME = FASSIGN

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ============= ========================= ===== =======================
    KEY           Example Value             Type  Comment
    ============= ========================= ===== =======================
    NAXIS1        66                        int   width of table in bytes
    NAXIS2        5020                      int   number of rows in table
    TILEID        1774                      int
    TILERA        222.786                   float
    TILEDEC       41.722                    float
    FIELDROT      -0.113900362856195        float
    FA_PLAN       2022-07-01T00:00:00.000   str
    FA_HA         10.15                     float
    FA_RUN        2021-05-18T21:57:00+00:00 str
    FA_M_GFA [1]_ 0.4                       float
    FA_M_PET [1]_ 0.4                       float
    FA_M_POS [1]_ 0.05                      float
    REQRA         222.786                   float
    REQDEC        41.722                    float
    FIELDNUM      0                         int
    FA_VER        4.0.0                     str
    FA_SURV       main                      str
    ============= ========================= ===== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

============== ======= ======== ========================================================================
Name           Type    Units    Description
============== ======= ======== ========================================================================
FIBER          int32            Fiber ID on the CCDs [0-4999]
TARGETID       int64            Unique DESI target ID
LOCATION       int32            Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBERSTATUS    int32            Fiber status mask. 0=good
LAMBDA_REF     float32 Angstrom Requested wavelength at which targets should be centered on fibers
PETAL_LOC      int16            Petal location [0-9]
DEVICE_LOC     int32            Device location on focal plane [0-523]
DEVICE_TYPE    char[3]          Device type
TARGET_RA      float64 deg      Barycentric right ascension in ICRS
TARGET_DEC     float64 deg      Barycentric declination in ICRS
FA_TARGET      int64            Targeting bit internally used by fiberassign (linked with FA_TYPE)
FA_TYPE        binary           Fiberassign internal target type (science, standard, sky, safe, suppsky)
FIBERASSIGN_X  float32 mm       Fiberassign expected CS5 X location on focal plane
FIBERASSIGN_Y  float32 mm       Fiberassign expected CS5 Y location on focal plane
PLATE_RA [1]_  float64 deg      Barycentric Right Ascension in ICRS to be used by PlateMaker
PLATE_DEC [1]_ float64 deg      Barycentric Declination in ICRS to be used by PlateMaker
============== ======= ======== ========================================================================

HDU2
----

EXTNAME = FTARGETS

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ============= ========================= ===== =======================
    KEY           Example Value             Type  Comment
    ============= ========================= ===== =======================
    NAXIS1        49                        int   width of table in bytes
    NAXIS2        146897                    int   number of rows in table
    TILEID        1774                      int
    TILERA        222.786                   float
    TILEDEC       41.722                    float
    FIELDROT      -0.113900362856195        float
    FA_PLAN       2022-07-01T00:00:00.000   str
    FA_HA         10.15                     float
    FA_RUN        2021-05-18T21:57:00+00:00 str
    FA_M_GFA [1]_ 0.4                       float
    FA_M_PET [1]_ 0.4                       float
    FA_M_POS [1]_ 0.05                      float
    REQRA         222.786                   float
    REQDEC        41.722                    float
    FIELDNUM      0                         int
    FA_VER        4.0.0                     str
    FA_SURV       main                      str
    ============= ========================= ===== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

============== ======= ===== ========================================================================
Name           Type    Units Description
============== ======= ===== ========================================================================
TARGETID       int64         Unique DESI target ID
TARGET_RA      float64 deg   Barycentric right ascension in ICRS
TARGET_DEC     float64 deg   Barycentric declination in ICRS
FA_TARGET      int64         Targeting bit internally used by fiberassign (linked with FA_TYPE)
FA_TYPE        binary        Fiberassign internal target type (science, standard, sky, safe, suppsky)
PRIORITY       int32         Target current priority
SUBPRIORITY    float64       Random subpriority [0-1) to break assignment ties
OBSCONDITIONS  int32         Bitmask of allowed observing conditions
PLATE_RA [1]_  float64 deg   Barycentric Right Ascension in ICRS to be used by PlateMaker
PLATE_DEC [1]_ float64 deg   Barycentric Declination in ICRS to be used by PlateMaker
============== ======= ===== ========================================================================

HDU3
----

EXTNAME = FAVAIL

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ========================= ===== =======================
    KEY      Example Value             Type  Comment
    ======== ========================= ===== =======================
    NAXIS1   16                        int   width of table in bytes
    NAXIS2   163517                    int   number of rows in table
    TILEID   1774                      int
    TILERA   222.786                   float
    TILEDEC  41.722                    float
    FIELDROT -0.113900362856195        float
    FA_PLAN  2022-07-01T00:00:00.000   str
    FA_HA    10.15                     float
    FA_RUN   2021-05-18T21:57:00+00:00 str
    REQRA    222.786                   float
    REQDEC   41.722                    float
    FIELDNUM 0                         int
    FA_VER   4.0.0                     str
    FA_SURV  main                      str
    ======== ========================= ===== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

======== ===== ===== =======================================================
Name     Type  Units Description
======== ===== ===== =======================================================
LOCATION int32       Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBER    int32       Fiber ID on the CCDs [0-4999]
TARGETID int64       Unique DESI target ID
======== ===== ===== =======================================================

HDU4
----

EXTNAME = GFA_TARGETS

GFA stars to be used by the ETC / GUIDE / FOCUS

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =======================
    KEY    Example Value Type Comment
    ====== ============= ==== =======================
    NAXIS1 168           int  width of table in bytes
    NAXIS2 820           int  number of rows in table
    ====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

================================= ======= ============ =====================================================================================================
Name                              Type    Units        Description
================================= ======= ============ =====================================================================================================
RELEASE                           int32                Imaging surveys release ID
TARGETID                          int64                Unique DESI target ID
BRICKID                           int32                Brick ID from tractor input
BRICK_OBJID                       int32                Imaging Surveys OBJID on that brick
TARGET_RA                         float64 deg          Barycentric right ascension in ICRS
TARGET_DEC                        float64 deg          Barycentric declination in ICRS
TARGET_RA_IVAR                    float32              label for field   7
TARGET_DEC_IVAR                   float32              label for field   8
MORPHTYPE                         char[4]              Imaging Surveys morphological type from Tractor
MASKBITS                          int16                Bitwise mask from the imaging indicating potential issue or blending
FLUX_G                            float32 nanomaggy    Flux in the Legacy Survey g-band (AB)
FLUX_R                            float32 nanomaggy    Flux in the Legacy Survey r-band (AB)
FLUX_Z                            float32 nanomaggy    Flux in the Legacy Survey z-band (AB)
FLUX_IVAR_G                       float32 nanomaggy^-2 Inverse variance of FLUX_G (AB)
FLUX_IVAR_R                       float32 nanomaggy^-2 Inverse variance of FLUX_R (AB)
FLUX_IVAR_Z                       float32 nanomaggy^-2 Inverse variance of FLUX_Z (AB)
REF_ID                            int64                Tyc1*1,000,000+Tyc2*10+Tyc3 for Tycho-2; ``sourceid`` for Gaia DR2
REF_CAT                           char[2]              Reference catalog source for star: T2 for Tycho-2, G2 for Gaia DR2, L2 for the SGA, empty otherwise
REF_EPOCH                         float32 yr           Reference epoch for Gaia/Tycho astrometry. Typically 2015.5 for Gaia
PARALLAX                          float32 mas          Reference catalog parallax
PARALLAX_IVAR                     float32 mas^-2       Inverse variance of PARALLAX
PMRA                              float32 mas yr^-1    proper motion in the +RA direction (already including cos(dec))
PMDEC                             float32 mas yr^-1    Proper motion in the +Dec direction
PMRA_IVAR                         float32 yr^2 mas^-2  Inverse variance of PMRA
PMDEC_IVAR                        float32 yr^2 mas^-2  Inverse variance of PMDEC
GAIA_PHOT_G_MEAN_MAG              float32 mag          Gaia G band magnitude
GAIA_PHOT_G_MEAN_FLUX_OVER_ERROR  float32              Gaia G band signal-to-noise
GAIA_PHOT_BP_MEAN_MAG             float32 mag          Gaia BP band magnitude
GAIA_PHOT_BP_MEAN_FLUX_OVER_ERROR float32              Gaia BP band signal-to-noise
GAIA_PHOT_RP_MEAN_MAG             float32 mag          Gaia RP band magnitude
GAIA_PHOT_RP_MEAN_FLUX_OVER_ERROR float32              Gaia RP band signal-to-noise
GAIA_ASTROMETRIC_EXCESS_NOISE     float32              Gaia astrometric excess noise
URAT_ID                           int64                ID in the URAT catalog for sources where URAT supplemented missing Gaia astrometric information
URAT_SEP                          float32 arcsec       Separation between URAT and Gaia sources where URAT supplemented missing Gaia astrometric information
HPXPIXEL                          int64                HEALPixel containing this location at NSIDE=64 in the NESTED scheme
GFA_LOC                           int16                label for field  36
ETC_FLAG                          int16                label for field  37
GUIDE_FLAG                        int16                label for field  38
FOCUS_FLAG                        int16                label for field  39
================================= ======= ============ =====================================================================================================


Notes and Examples
==================

This type of file contains only what is strictly needed or generated by fiber
assignment itself, while the final :doc:`fiberassign-TILEID.fits.gz files <../../../../../DESI_TARGET/fiberassign/TILES_VERSION/TILEXX/fiberassign-TILEID>`
also have merged in targeting information, and some bookkeeping changes such as
splitting the 20 sky monitor fibers separate from the 5000 science fibers,
and renaming/reordering HDUs.
