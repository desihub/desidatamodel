=======================
fiberassign-TILEID.fits
=======================

:Summary: The fiberassign file contains the fiber positioner configuration information for
    each exposure: what fiber is placed where, what target that is, etc.
    The uncompressed version contains extra HDUs relative to the compressed version.
:Naming Convention: ``fiberassign-TILEID.fits``, where TILEID is the zero-padded
    6-digit tile ID.
:Regex: ``fiberassign-[0-9]{6}\.fits``
:File Type: FITS, 42 MB

Contents
========

====== ===================== ======== ===================
Number EXTNAME               Type     Contents
====== ===================== ======== ===================
HDU0_  PRIMARY               IMAGE    Keywords only
HDU1_  FIBERASSIGN           BINTABLE Target assignments for each fiber
HDU2_  SKY_MONITOR           BINTABLE Sky location for the 20 sky monitor fibers used by the ETC
HDU3_  GFA_TARGETS           BINTABLE Selected star for the ETC / GUIDE / FOCUS
HDU4_  TARGETS               BINTABLE List of targets that are reachable by a positioner
HDU5_  POTENTIAL_ASSIGNMENTS BINTABLE All possible (TARGETID, FIBER, LOCATION) assignments
HDU6_  FASSIGN               BINTABLE Short version of FIBERASSIGN
HDU7_  FTARGETS              BINTABLE Short version of TARGETS
HDU8_  FAVAIL                BINTABLE Equivalent to POTENTIAL_ASSIGNMENTS
====== ===================== ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

No data, but some useful header keywords.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ======================= ===== =======
    KEY      Example Value           Type  Comment
    ======== ======================= ===== =======
    FA_VER   1.2.1.dev2478           str   Fiberassign code version
    FIELDNUM 0                       int   Not used, always zero
    TILEDEC  28.12                   float [deg] Tile Declination
    FA_SURV  main                    str   Survey of origin of the targets
    TILEID   59096                   int   Tile ID
    FA_HA    0.0                     float [deg] Design Hour Angle
    FIELDROT 0.0                     float [deg] Field rotation
    REQRA    348.12                  float [deg] Tile Right Ascension
    REQDEC   28.12                   float [deg] Tile Declination
    FA_DATE  2022-07-01T00:00:00.000 str   [UTC] Plan field rotations for this date
    TILERA   348.12                  float [deg] Tile Right Ascension
    ======== ======================= ===== =======

Empty HDU.

HDU1
----

EXTNAME = FIBERASSIGN

The target assignments for each fiber of this tile.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ======================= ===== =======================
    KEY      Example Value           Type  Comment
    ======== ======================= ===== =======================
    NAXIS1   204                     int   width of table in bytes
    NAXIS2   5000                    int   number of rows in table
    FA_VER   1.2.1.dev2478           str   Fiberassign code version
    FIELDNUM 0                       int   Not used, always zero
    TILEDEC  28.12                   float [deg] Tile Declination
    FA_SURV  main                    str   Survey of origin of the targets
    TILEID   59096                   int   Tile ID
    FA_HA    0.0                     float [deg] Design Hour Angle
    FIELDROT 0.0                     float [deg] Field rotation
    REQRA    348.12                  float [deg] Tile Right Ascension
    REQDEC   28.12                   float [deg] Tile Declination
    FA_DATE  2022-07-01T00:00:00.000 str   [UTC] Plan field rotations for this date
    TILERA   348.12                  float [deg] Tile Right Ascension
    ======== ======================= ===== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

================ ======= ============ ========================================================================================================
Name             Type    Units        Description
================ ======= ============ ========================================================================================================
TARGETID         int64                Unique DESI target ID
PETAL_LOC        int16                Petal location [0-9]
DEVICE_LOC       int32                Device location on focal plane [0-523]
LOCATION         int32                Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBER            int32                Fiber ID on the CCDs [0-4999]
FIBERSTATUS      int32                Fiber status mask. 0=good
TARGET_RA        float64 deg          Barycentric right ascension in ICRS
TARGET_DEC       float64 deg          Barycentric declination in ICRS
PMRA             float32 mas yr^-1    proper motion in the +RA direction (already including cos(dec))
PMDEC            float32 mas yr^-1    Proper motion in the +Dec direction
PMRA_IVAR        float32 yr^2 mas^-2  Inverse variance of PMRA
PMDEC_IVAR       float32 yr^2 mas^-2  Inverse variance of PMDEC
REF_EPOCH        float32 yr           Reference epoch for Gaia/Tycho astrometry. Typically 2015.5 for Gaia
LAMBDA_REF       float32 Angstrom     Requested wavelength at which targets should be centered on fibers
FA_TARGET        int64                Targeting bit internally used by fiberassign (linked with FA_TYPE)
FA_TYPE          binary               Fiberassign internal target type (science, standard, sky, safe, suppsky)
OBJTYPE          char[3]              Object type: TGT, SKY, NON, BAD
FIBERASSIGN_X    float32 mm           Fiberassign expected CS5 X location on focal plane
FIBERASSIGN_Y    float32 mm           Fiberassign expected CS5 Y location on focal plane
NUMTARGET        int16                Total number of targets that this positioner covered
PRIORITY         int32                Target current priority
SUBPRIORITY      float64              Random subpriority [0-1) to break assignment ties
OBSCONDITIONS    int32                Bitmask of allowed observing conditions
NUMOBS_MORE      int32                Number of additional observations needed
RELEASE          int32                Imaging surveys release ID
BRICKID          int32                Brick ID from tractor input
BRICKNAME        char[8]              Brick name from tractor input
BRICK_OBJID      int32                Imaging Surveys OBJID on that brick
BLOBDIST         float32 pix          Maximum distance from a detected Legacy Surveys source
FIBERFLUX_G      float32 nanomaggy    Predicted g-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERFLUX_R      float32 nanomaggy    Predicted r-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERFLUX_Z      float32 nanomaggy    Predicted z-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERFLUX_IVAR_G float32 nanomaggy^-2 Inverse variance of ``FIBERFLUX_G``
FIBERFLUX_IVAR_R float32 nanomaggy^-2 Inverse variance of ``FIBERFLUX_R``
FIBERFLUX_IVAR_Z float32 nanomaggy^-2 Inverse variance of ``FIBERFLUX_Z``
DESI_TARGET      int64                DESI (dark time program) target selection bitmask
BGS_TARGET       int64                BGS (Bright Galaxy Survey) target selection bitmask
MWS_TARGET       int64                Milky Way Survey targeting bits
PRIORITY_INIT    int64                Target initial priority from target selection bitmasks and OBSCONDITIONS
NUMOBS_INIT      int64                Initial number of observations for target calculated across target selection bitmasks and OBSCONDITIONS
HPXPIXEL         int64                HEALPixel containing this location at NSIDE=64 in the NESTED scheme
================ ======= ============ ========================================================================================================

HDU2
----

EXTNAME = SKY_MONITOR

Blank sky assignments for sky monitor positioners.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ======================= ===== =======================
    KEY      Example Value           Type  Comment
    ======== ======================= ===== =======================
    NAXIS1   113                     int   width of table in bytes
    NAXIS2   20                      int   number of rows in table
    FA_VER   1.2.1.dev2478           str   Fiberassign code version
    FIELDNUM 0                       int   Not used, always zero
    TILEDEC  28.12                   float [deg] Tile Declination
    FA_SURV  main                    str   Survey of origin of the targets
    TILEID   59096                   int   Tile ID
    FA_HA    0.0                     float [deg] Design Hour Angle
    FIELDROT 0.0                     float [deg] Field rotation
    REQRA    348.12                  float [deg] Tile Right Ascension
    REQDEC   28.12                   float [deg] Tile Declination
    FA_DATE  2022-07-01T00:00:00.000 str   [UTC] Plan field rotations for this date
    TILERA   348.12                  float [deg] Tile Right Ascension
    ======== ======================= ===== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

================ ======= ============ ========================================================================================================
Name             Type    Units        Description
================ ======= ============ ========================================================================================================
FIBER            int32                Fiber ID on the CCDs [0-4999]
LOCATION         int32                Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
NUMTARGET        int16                Total number of targets that this positioner covered
TARGETID         int64                Unique DESI target ID
BRICKID          int32                Brick ID from tractor input
BRICK_OBJID      int32                Imaging Surveys OBJID on that brick
FA_TARGET        int64                Targeting bit internally used by fiberassign (linked with FA_TYPE)
FA_TYPE          binary               Fiberassign internal target type (science, standard, sky, safe, suppsky)
TARGET_RA        float64 deg          Barycentric right ascension in ICRS
TARGET_DEC       float64 deg          Barycentric declination in ICRS
FIBERASSIGN_X    float32 mm           Fiberassign expected CS5 X location on focal plane
FIBERASSIGN_Y    float32 mm           Fiberassign expected CS5 Y location on focal plane
BRICKNAME        char[8]              Brick name from tractor input
FIBERSTATUS      int32                Fiber status mask. 0=good
PETAL_LOC        int16                Petal location [0-9]
DEVICE_LOC       int32                Device location on focal plane [0-523]
PRIORITY         int32                Target current priority
SUBPRIORITY      float64              Random subpriority [0-1) to break assignment ties
FIBERFLUX_G      float32 nanomaggy    Predicted g-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERFLUX_R      float32 nanomaggy    Predicted r-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERFLUX_Z      float32 nanomaggy    Predicted z-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERFLUX_IVAR_G float32 nanomaggy^-2 Inverse variance of ``FIBERFLUX_G``
FIBERFLUX_IVAR_R float32 nanomaggy^-2 Inverse variance of ``FIBERFLUX_R``
FIBERFLUX_IVAR_Z float32 nanomaggy^-2 Inverse variance of ``FIBERFLUX_Z``
================ ======= ============ ========================================================================================================

HDU3
----

EXTNAME = GFA_TARGETS

GFA stars to be used by the ETC / GUIDE / FOCUS

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ======================= ===== =======================
    KEY      Example Value           Type  Comment
    ======== ======================= ===== =======================
    NAXIS1   166                     int   width of table in bytes
    NAXIS2   1873                    int   number of rows in table
    FA_VER   1.2.1.dev2478           str   Fiberassign code version
    FIELDNUM 0                       int   Not used, always zero
    TILEDEC  28.12                   float [deg] Tile Declination
    FA_SURV  main                    str   Survey of origin of the targets
    TILEID   59096                   int   Tile ID
    FA_HA    0.0                     float [deg] Design Hour Angle
    FIELDROT 0.0                     float [deg] Field rotation
    REQRA    348.12                  float [deg] Tile Right Ascension
    REQDEC   28.12                   float [deg] Tile Declination
    FA_DATE  2022-07-01T00:00:00.000 str   [UTC] Plan field rotations for this date
    TILERA   348.12                  float [deg] Tile Right Ascension
    ======== ======================= ===== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

================================= ======= ============ =======================================================================================================================================
Name                              Type    Units        Description
================================= ======= ============ =======================================================================================================================================
RELEASE                           int32                Imaging surveys release ID
TARGETID                          int64                Unique DESI target ID
BRICKID                           int32                Brick ID from tractor input
BRICK_OBJID                       int32                Imaging Surveys OBJID on that brick
TARGET_RA                         float64 deg          Barycentric right ascension in ICRS
TARGET_DEC                        float64 deg          Barycentric declination in ICRS
TARGET_RA_IVAR                    float32              label for field   7
TARGET_DEC_IVAR                   float32              label for field   8
MORPHTYPE                         char[4]              Imaging Surveys morphological type from Tractor
FLUX_G                            float32 nanomaggy    Flux in the Legacy Survey g-band (AB)
FLUX_R                            float32 nanomaggy    Flux in the Legacy Survey r-band (AB)
FLUX_Z                            float32 nanomaggy    Flux in the Legacy Survey z-band (AB)
FLUX_IVAR_G                       float32 nanomaggy^-2 Inverse variance of FLUX_G (AB)
FLUX_IVAR_R                       float32 nanomaggy^-2 Inverse variance of FLUX_R (AB)
FLUX_IVAR_Z                       float32 nanomaggy^-2 Inverse variance of FLUX_Z (AB)
REF_ID                            int64                Tyc1*1,000,000+Tyc2*10+Tyc3 for Tycho-2; ``sourceid`` for Gaia DR2
REF_CAT                           char[2]              Reference catalog source for star: &#x27;T2&#x27; for Tycho-2, &#x27;G2&#x27; for Gaia DR2, &#x27;L2&#x27; for the SGA, empty otherwise
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
GFA_LOC                           int16                label for field  35
ETC_FLAG                          int16                label for field  36
GUIDE_FLAG                        int16                label for field  37
FOCUS_FLAG                        int16                label for field  38
================================= ======= ============ =======================================================================================================================================

HDU4
----

EXTNAME = TARGETS

Unique list of targets reachable by a positioner.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ======================= ===== =======================
    KEY      Example Value           Type  Comment
    ======== ======================= ===== =======================
    NAXIS1   204                     int   width of table in bytes
    NAXIS2   145163                  int   number of rows in table
    FA_VER   1.2.1.dev2478           str   Fiberassign code version
    FIELDNUM 0                       int   Not used, always zero
    TILEDEC  28.12                   float [deg] Tile Declination
    FA_SURV  main                    str   Survey of origin of the targets
    TILEID   59096                   int   Tile ID
    FA_HA    0.0                     float [deg] Design Hour Angle
    FIELDROT 0.0                     float [deg] Field rotation
    REQRA    348.12                  float [deg] Tile Right Ascension
    REQDEC   28.12                   float [deg] Tile Declination
    FA_DATE  2022-07-01T00:00:00.000 str   [UTC] Plan field rotations for this date
    TILERA   348.12                  float [deg] Tile Right Ascension
    ======== ======================= ===== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

============= ======= ============ =======================================================================================================
Name          Type    Units        Description
============= ======= ============ =======================================================================================================
TARGETID      int64                Unique DESI target ID
PETAL_LOC     int16                Petal location [0-9]
DEVICE_LOC    int32                Device location on focal plane [0-523]
LOCATION      int32                Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBER         int32                Fiber ID on the CCDs [0-4999]
FIBERSTATUS   int32                Fiber status mask. 0=good
RA            float64 deg          Barycentric Right Ascension in ICRS
DEC           float64 deg          Barycentric declination in ICRS
PMRA          float32 mas yr^-1    proper motion in the +RA direction (already including cos(dec))
PMDEC         float32 mas yr^-1    Proper motion in the +Dec direction
PMRA_IVAR     float32 yr^2 mas^-2  Inverse variance of PMRA
PMDEC_IVAR    float32 yr^2 mas^-2  Inverse variance of PMDEC
REF_EPOCH     float32 yr           Reference epoch for Gaia/Tycho astrometry. Typically 2015.5 for Gaia
LAMBDA_REF    float32 Angstrom     Requested wavelength at which targets should be centered on fibers
FA_TARGET     int64                Targeting bit internally used by fiberassign (linked with FA_TYPE)
FA_TYPE       binary               Fiberassign internal target type (science, standard, sky, safe, suppsky)
OBJTYPE       char[3]              Object type: TGT, SKY, NON, BAD
FIBERASSIGN_X float32 mm           Fiberassign expected CS5 X location on focal plane
FIBERASSIGN_Y float32 mm           Fiberassign expected CS5 Y location on focal plane
NUMTARGET     int16                Total number of targets that this positioner covered
PRIORITY      int32                Target current priority
SUBPRIORITY   float64              Random subpriority [0-1) to break assignment ties
OBSCONDITIONS int32                Bitmask of allowed observing conditions
NUMOBS_MORE   int32                Number of additional observations needed
RELEASE       int32                Imaging surveys release ID
BRICKID       int32                Brick ID from tractor input
BRICKNAME     char[8]              Brick name from tractor input
BRICK_OBJID   int32                Imaging Surveys OBJID on that brick
BLOBDIST      float32 pix          Maximum distance from a detected Legacy Surveys source
APFLUX_G      float32 nanomaggy    Total flux in nanomaggies extracted in a 0.75 arcsec radius in the g band at this location
APFLUX_R      float32 nanomaggy    Total flux in nanomaggies extracted in a 0.75 arcsec radius in the r band at this location
APFLUX_Z      float32 nanomaggy    Total flux in nanomaggies extracted in a 0.75 arcsec radius in the z band at this location
APFLUX_IVAR_G float32 nanomaggy^-2 Inverse variance of APFLUX_G
APFLUX_IVAR_R float32 nanomaggy^-2 Inverse variance of APFLUX_R
APFLUX_IVAR_Z float32 nanomaggy^-2 Inverse variance of APFLUX_Z
DESI_TARGET   int64                DESI (dark time program) target selection bitmask
BGS_TARGET    int64                BGS (Bright Galaxy Survey) target selection bitmask
MWS_TARGET    int64                Milky Way Survey targeting bits
PRIORITY_INIT int64                Target initial priority from target selection bitmasks and OBSCONDITIONS
NUMOBS_INIT   int64                Initial number of observations for target calculated across target selection bitmasks and OBSCONDITIONS
HPXPIXEL      int64                HEALPixel containing this location at NSIDE=64 in the NESTED scheme
============= ======= ============ =======================================================================================================

HDU5
----

EXTNAME = POTENTIAL_ASSIGNMENTS

A list of targets that could have been assigned to each fiber.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ======================= ===== =======================
    KEY      Example Value           Type  Comment
    ======== ======================= ===== =======================
    NAXIS1   16                      int   width of table in bytes
    NAXIS2   163503                  int   number of rows in table
    FA_VER   1.2.1.dev2478           str   Fiberassign code version
    FIELDNUM 0                       int   Not used, always zero
    TILEDEC  28.12                   float [deg] Tile Declination
    FA_SURV  main                    str   Survey of origin of the targets
    TILEID   59096                   int   Tile ID
    FA_HA    0.0                     float [deg] Design Hour Angle
    FIELDROT 0.0                     float [deg] Field rotation
    REQRA    348.12                  float [deg] Tile Right Ascension
    REQDEC   28.12                   float [deg] Tile Declination
    FA_DATE  2022-07-01T00:00:00.000 str   [UTC] Plan field rotations for this date
    TILERA   348.12                  float [deg] Tile Right Ascension
    ======== ======================= ===== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

======== ===== ===== =======================================================
Name     Type  Units Description
======== ===== ===== =======================================================
TARGETID int64       Unique DESI target ID
FIBER    int32       Fiber ID on the CCDs [0-4999]
LOCATION int32       Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
======== ===== ===== =======================================================

HDU6
----

EXTNAME = FASSIGN

Short version of FIBERASSIGN.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ======================= ===== =======================
    KEY      Example Value           Type  Comment
    ======== ======================= ===== =======================
    NAXIS1   66                      int   width of table in bytes
    NAXIS2   5020                    int   number of rows in table
    FA_VER   1.2.1.dev2478           str   Fiberassign code version
    FIELDNUM 0                       int   Not used, always zero
    TILEDEC  28.12                   float [deg] Tile Declination
    FA_SURV  main                    str   Survey of origin of the targets
    TILEID   59096                   int   Tile ID
    FA_HA    0.0                     float [deg] Design Hour Angle
    FIELDROT 0.0                     float [deg] Field rotation
    REQRA    348.12                  float [deg] Tile Right Ascension
    REQDEC   28.12                   float [deg] Tile Declination
    FA_DATE  2022-07-01T00:00:00.000 str   [UTC] Plan field rotations for this date
    TILERA   348.12                  float [deg] Tile Right Ascension
    ======== ======================= ===== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

============= ======= ======== ========================================================================
Name          Type    Units    Description
============= ======= ======== ========================================================================
FIBER         int32            Fiber ID on the CCDs [0-4999]
TARGETID      int64            Unique DESI target ID
LOCATION      int32            Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBERSTATUS   int32            Fiber status mask. 0=good
LAMBDA_REF    float32 Angstrom Requested wavelength at which targets should be centered on fibers
PETAL_LOC     int16            Petal location [0-9]
DEVICE_LOC    int32            Device location on focal plane [0-523]
DEVICE_TYPE   char[3]          Device type
TARGET_RA     float64 deg      Barycentric right ascension in ICRS
TARGET_DEC    float64 deg      Barycentric declination in ICRS
FA_TARGET     int64            Targeting bit internally used by fiberassign (linked with FA_TYPE)
FA_TYPE       binary           Fiberassign internal target type (science, standard, sky, safe, suppsky)
FIBERASSIGN_X float32 mm       Fiberassign expected CS5 X location on focal plane
FIBERASSIGN_Y float32 mm       Fiberassign expected CS5 Y location on focal plane
============= ======= ======== ========================================================================

HDU7
----

EXTNAME = FTARGETS

Short version of TARGETS.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ======================= ===== =======================
    KEY      Example Value           Type  Comment
    ======== ======================= ===== =======================
    NAXIS1   53                      int   width of table in bytes
    NAXIS2   145163                  int   number of rows in table
    FA_VER   1.2.1.dev2478           str   Fiberassign code version
    FIELDNUM 0                       int   Not used, always zero
    TILEDEC  28.12                   float [deg] Tile Declination
    FA_SURV  main                    str   Survey of origin of the targets
    TILEID   59096                   int   Tile ID
    FA_HA    0.0                     float [deg] Design Hour Angle
    FIELDROT 0.0                     float [deg] Field rotation
    REQRA    348.12                  float [deg] Tile Right Ascension
    REQDEC   28.12                   float [deg] Tile Declination
    FA_DATE  2022-07-01T00:00:00.000 str   [UTC] Plan field rotations for this date
    TILERA   348.12                  float [deg] Tile Right Ascension
    ======== ======================= ===== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

============= ======= ===== ========================================================================
Name          Type    Units Description
============= ======= ===== ========================================================================
TARGETID      int64         Unique DESI target ID
TARGET_RA     float64 deg   Barycentric right ascension in ICRS
TARGET_DEC    float64 deg   Barycentric declination in ICRS
FA_TARGET     int64         Targeting bit internally used by fiberassign (linked with FA_TYPE)
FA_TYPE       binary        Fiberassign internal target type (science, standard, sky, safe, suppsky)
PRIORITY      int32         Target current priority
SUBPRIORITY   float64       Random subpriority [0-1) to break assignment ties
OBSCONDITIONS int32         Bitmask of allowed observing conditions
NUMOBS_MORE   int32         Number of additional observations needed
============= ======= ===== ========================================================================

HDU8
----

EXTNAME = FAVAIL

Equivalent to POTENTIAL_ASSIGNMENTS.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ======================= ===== =======================
    KEY      Example Value           Type  Comment
    ======== ======================= ===== =======================
    NAXIS1   16                      int   width of table in bytes
    NAXIS2   163503                  int   number of rows in table
    FA_VER   1.2.1.dev2478           str   Fiberassign code version
    FIELDNUM 0                       int   Not used, always zero
    TILEDEC  28.12                   float [deg] Tile Declination
    FA_SURV  main                    str   Survey of origin of the targets
    TILEID   59096                   int   Tile ID
    FA_HA    0.0                     float [deg] Design Hour Angle
    FIELDROT 0.0                     float [deg] Field rotation
    REQRA    348.12                  float [deg] Tile Right Ascension
    REQDEC   28.12                   float [deg] Tile Declination
    FA_DATE  2022-07-01T00:00:00.000 str   [UTC] Plan field rotations for this date
    TILERA   348.12                  float [deg] Tile Right Ascension
    ======== ======================= ===== =======================

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
