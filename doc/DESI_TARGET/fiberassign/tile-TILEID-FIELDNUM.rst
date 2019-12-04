====================
tile-TILEID-FIELDNUM
====================

:Summary: FITS file with fiber assignments for a given DESI tile.
:Naming Convention: tile-TILEID-FIELDNUM.fits where TILEID is a 6-digit
    pre-defined tile ID or 999999 for pointings without a pre-defined ID;
    and FIELDNUM is the 4-digit field number for this tile
    (typically 0, see notes below).

:Regex: ``tile-[0-9]{6}-[0-9]{4}\.fits``
:File Type: FITS, 2 MB

For standard DESI tiles, FIELDNUM=0.  Test tiles might have different
positioner configurations for the same tile and FIELDNUM encodes which
configuration it is.

Note: as of software release 18.11 (fiberassign 0.10.3) the files are
named tile_TILEID.fits instead of tile-TILEID-FIELDNUM.fits.  This will
change in the future.

Contents
========

====== ===================== ======== ===================
Number EXTNAME               Type     Contents
====== ===================== ======== ===================
HDU0_  PRIMARY               IMAGE    Blank
HDU1_  FIBERASSIGN           BINTABLE Target assignments for each fiber
HDU2_  SKY_MONITOR           BINTABLE *Description needed*
HDU3_  TARGETS               BINTABLE Target catalog row-matched to FIBERASSIGN table
HDU4_  POTENTIAL_ASSIGNMENTS BINTABLE All targets that could have been assigned
HDU5_  FASSIGN               BINTABLE *Description needed*
HDU6_  FTARGETS              BINTABLE *Description needed*
HDU7_  FAVAIL                BINTABLE *Description needed*
====== ===================== ======== ===================

NOTE: this file describes what the 19.9 fiberassign output files currently are,
which are somewhat different from what we eventually intend them to be.
Key upcoming differences for consistency with ICS:

  * filenames tile_TILEID.fits -> tile-TILEID-FIELDNUM.fits (TBD)
  * reordering HDUs?

FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

No data, but some useful header keywords.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== ========================================
KEY      Example Value             Type  Comment
======== ========================= ===== ========================================
TILEID   1165                      int   *Description needed*
TILERA   150.69                    float *Description needed*
TILEDEC  33.86                     float *Description needed*
FIELDROT 0.07075034296             float *Description needed*
FA_DATE  '2022-07-01T00:00:00.000' str   *Description needed*
FA_HA    0.                        float *Description needed*
REQRA    150.69                    float *Description needed*
REQDEC   33.86                     float *Description needed*
FIELDNUM 0                         int   Field configuration number for this tile
FA_VER   1.2.0                     str   Why are we not using DEPNAM/DEPVER?
FA_SURV  main                      str   *Description needed*
======== ========================= ===== ========================================

Empty HDU.

HDU1
----

EXTNAME = FIBERASSIGN

The target assignments for each fiber of this tile.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== ========================================
KEY      Example Value             Type  Comment
======== ========================= ===== ========================================
NAXIS1   576                       int   Width of table in bytes
NAXIS2   5000                      int   Number of fibers
TILEID   1165                      int   *Description needed*
TILERA   150.69                    float *Description needed*
TILEDEC  33.86                     float *Description needed*
FIELDROT 0.07075034296             float *Description needed*
FA_DATE  '2022-07-01T00:00:00.000' str   *Description needed*
FA_HA    0.                        float *Description needed*
REQRA    150.69                    float *Description needed*
REQDEC   33.86                     float *Description needed*
FIELDNUM 0                         int   Field configuration number for this tile
FA_VER   1.2.0                     str   Why are we not using DEPNAM/DEPVER?
FA_SURV  main                      str   *Description needed*
======== ========================= ===== ========================================

Note: None of these non-standard keywords are included yet in
fiberassign/0.10.3 in the 18.11 reference run.

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

================================= =========== ============ ===========
Name                              Type        Units        Description
================================= =========== ============ ===========
TARGETID                          int64                    Unique target ID
PETAL_LOC                         int16                    Petal location [0-9]
DEVICE_LOC                        int32                    Device location on focal plane [0-523]
LOCATION                          int32                    Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBER                             int32                    Fiber ID on the CCDs [0-4999]
FIBERSTATUS                       int32                    Fiber status mask; 0=good
TARGET_RA                         float64     deg          Target Right Ascension [degrees]
TARGET_DEC                        float64     deg          Target declination [degrees]
PMRA                              float32     mas/yr       Proper motion in the RA direction (already including cosDec term)
PMDEC                             float32     mas/yr       Proper motion in the dec direction
PMRA_IVAR                         float32                  Inverse variance of PMRA
PMDEC_IVAR                        float32                  Inverse variance of PMDEC
REF_EPOCH                         float32                  *Description needed*
LAMBDA_REF                        float32     Angstrom     Wavelength at which targets should be centered on fibers
FA_TARGET                         int64                    *Description needed*
FA_TYPE                           byte                     *Description needed*
OBJTYPE                           char[3]                  SKY, OBJ, NON
FIBERASSIGN_X                     float32     mm           Expected CS5 X location on focal plane
FIBERASSIGN_Y                     float32     mm           Expected CS5 Y location on focal plane
NUMTARGET                         int16                    Total number of targets that this positioner covered
PRIORITY                          int32                    Assignment priority; larger = higher priority
SUBPRIORITY                       float64                  Assignment subpriority [0-1]
OBSCONDITIONS                     int32                    *Description needed*
NUMOBS_MORE                       int32                    *Description needed*
RELEASE                           int16                    Imaging release number
BRICKID                           int32                    Imaging Surveys brick ID
BRICKNAME                         char[8]                  Imaging Surveys brick name
BRICK_OBJID                       int32                    Imaging surveys OBJID on that brick
MORPHTYPE                         char[4]                  Imaging surveys morphological type
TARGET_RA_IVAR                    float32     deg^-2       Inverse variance of TARGET_RA
TARGET_DEC_IVAR                   float32     deg^-2       Inverse variance of TARGET_DEC
DCHISQ                            float32[5]               *Description needed*
FLUX_G                            float32     nanomaggies  Flux in g-band
FLUX_R                            float32     nanomaggies  Flux in r-band
FLUX_Z                            float32     nanomaggies  Flux in z-band
FLUX_W1                           float32     nanomaggies  Flux in WISE W1-band
FLUX_W2                           float32     nanomaggies  Flux in WISE W2-band
FLUX_W3                           float32     nanomaggies  Flux in WISE W3-band
FLUX_W4                           float32     nanomaggies  Flux in WISE W4-band
FLUX_IVAR_G                       float32                  Inverse variance of FLUX_G
FLUX_IVAR_R                       float32                  Inverse variance of FLUX_R
FLUX_IVAR_Z                       float32                  Inverse variance of FLUX_Z
FLUX_IVAR_W1                      float32                  Inverse variance of FLUX_W1
FLUX_IVAR_W2                      float32                  Inverse variance of FLUX_W2
FLUX_IVAR_W3                      float32                  Inverse variance of FLUX_W3
FLUX_IVAR_W4                      float32                  Inverse variance of FLUX_W4
MW_TRANSMISSION_R                 float32                  *Description needed*
MW_TRANSMISSION_G                 float32                  *Description needed*
MW_TRANSMISSION_Z                 float32                  *Description needed*
MW_TRANSMISSION_W1                float32                  *Description needed*
MW_TRANSMISSION_W2                float32                  *Description needed*
MW_TRANSMISSION_W3                float32                  *Description needed*
MW_TRANSMISSION_W4                float32                  *Description needed*
NOBS_G                            int16                    *Description needed*
NOBS_R                            int16                    *Description needed*
NOBS_Z                            int16                    *Description needed*
FRACFLUX_G                        float32                  *Description needed*
FRACFLUX_R                        float32                  *Description needed*
FRACFLUX_Z                        float32                  *Description needed*
FRACMASKED_G                      float32                  *Description needed*
FRACMASKED_R                      float32                  *Description needed*
FRACMASKED_Z                      float32                  *Description needed*
FRACIN_G                          float32                  *Description needed*
FRACIN_R                          float32                  *Description needed*
FRACIN_Z                          float32                  *Description needed*
ALLMASK_G                         float32                  *Description needed*
ALLMASK_R                         float32                  *Description needed*
ALLMASK_Z                         float32                  *Description needed*
WISEMASK_W1                       byte                     *Description needed*
WISEMASK_W2                       byte                     *Description needed*
PSFDEPTH_G                        float32                  *Description needed*
PSFDEPTH_R                        float32                  *Description needed*
PSFDEPTH_Z                        float32                  *Description needed*
GALDEPTH_G                        float32                  *Description needed*
GALDEPTH_R                        float32                  *Description needed*
GALDEPTH_Z                        float32                  *Description needed*
FRACDEV                           float32                  *Description needed*
FRACDEV_IVAR                      float32                  *Description needed*
SHAPEDEV_R                        float32                  *Description needed*
SHAPEDEV_R_IVAR                   float32                  *Description needed*
SHAPEDEV_E1                       float32                  *Description needed*
SHAPEDEV_E1_IVAR                  float32                  *Description needed*
SHAPEDEV_E2                       float32                  *Description needed*
SHAPEDEV_E2_IVAR                  float32                  *Description needed*
SHAPEEXP_R                        float32                  *Description needed*
SHAPEEXP_R_IVAR                   float32                  *Description needed*
SHAPEEXP_E1                       float32                  *Description needed*
SHAPEEXP_E1_IVAR                  float32                  *Description needed*
SHAPEEXP_E2                       float32                  *Description needed*
SHAPEEXP_E2_IVAR                  float32                  *Description needed*
FIBERFLUX_G                       float32     nanomaggies  g-band object model flux for 1 arcsec seeing and 1.5 arcsec diameter fiber
FIBERFLUX_R                       float32     nanomaggies  r-band object model flux for 1 arcsec seeing and 1.5 arcsec diameter fiber
FIBERFLUX_Z                       float32     nanomaggies  z-band object model flux for 1 arcsec seeing and 1.5 arcsec diameter fiber
FIBERTOTFLUX_G                    float32     nanomaggies  like FIBERFLUX_G but including all objects overlapping this location
FIBERTOTFLUX_R                    float32     nanomaggies  like FIBERFLUX_R but including all objects overlapping this location
FIBERTOTFLUX_Z                    float32     nanomaggies  like FIBERFLUX_Z but including all objects overlapping this location
REF_CAT                           char[2]                  *Description needed*
REF_ID                            int64                    Astrometric catalog reference ID (SOURCE_ID from GAIA)
GAIA_PHOT_G_MEAN_MAG              float32                  *Description needed*
GAIA_PHOT_G_MEAN_FLUX_OVER_ERROR  float32                  *Description needed*
GAIA_PHOT_BP_MEAN_MAG             float32                  *Description needed*
GAIA_PHOT_BP_MEAN_FLUX_OVER_ERROR float32                  *Description needed*
GAIA_PHOT_RP_MEAN_MAG             float32                  *Description needed*
GAIA_PHOT_RP_MEAN_FLUX_OVER_ERROR float32                  *Description needed*
GAIA_PHOT_BP_RP_EXCESS_FACTOR     float32                  *Description needed*
GAIA_ASTROMETRIC_SIGMA5D_MAX      float32                  *Description needed*
GAIA_ASTROMETRIC_PARAMS_SOLVED    int64                    *Description needed*
GAIA_ASTROMETRIC_EXCESS_NOISE     float32                  `Gaia`_ astrometric excess noise
GAIA_DUPLICATED_SOURCE            bool                     `Gaia`_ duplicated source flag
PARALLAX                          float32                  *Description needed*
PARALLAX_IVAR                     float32                  *Description needed*
MASKBITS                          int16                    *Description needed*
EBV                               float32                  Median (average?) Milky Way dust E(B-V) extinction
PHOTSYS                           char[1]                  *Description needed*
DESI_TARGET                       int64                    Dark survey + calibration targeting bits
BGS_TARGET                        int64                    Bright Galaxy Survey targeting bits
MWS_TARGET                        int64                    Milky Way Survey targeting bits
PRIORITY_INIT                     int64                    *Description needed*
NUMOBS_INIT                       int64                    *Description needed*
HPXPIXEL                          int64                    HEALPixel containing target.
PRIORITY_INIT_DARK                int64                    *Description needed*
NUMOBS_INIT_DARK                  int64                    *Description needed*
PRIORITY_INIT_BRIGHT              int64                    *Description needed*
NUMOBS_INIT_BRIGHT                int64                    *Description needed*
FIBERFLUX_IVAR_G                  float64                  Why are these ``double``?
FIBERFLUX_IVAR_R                  float64                  Why are these ``double``?
FIBERFLUX_IVAR_Z                  float64                  Why are these ``double``?
================================= =========== ============ ===========

.. _`Gaia`: https://gea.esac.esa.int/archive/documentation//GDR2/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html

Notes:

* This table defines the *requested* fiber assignments.  See
  :doc:`fiberassign <../../DESI_SPECTRO_DATA/NIGHT/EXPID/fibermap-EXPID>` for the
  actual observed assignments.


HDU2
----

EXTNAME = SKY_MONITOR

Blank sky assignments for sky monitor positioners.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================= ===== =======================
KEY      Example Value           Type  Comment
======== ======================= ===== =======================
NAXIS1   113                     int   width of table in bytes
NAXIS2   20                      int   number of rows in table
TILEID   11108                   int
TILERA   150.87                  float
TILEDEC  31.23                   float
FIELDROT 0.0707542268034296      float
FA_DATE  2022-07-01T00:00:00.000 str
FA_HA    0.0                     float
REQRA    150.87                  float
REQDEC   31.23                   float
FIELDNUM 0                       int
FA_VER   1.2.0                   str
FA_SURV  main                    str
======== ======================= ===== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

See the FIBERASSIGN table for a description of these columns

================ ======= ===== ===================
Name             Type    Units Description
================ ======= ===== ===================
FIBER            int32
LOCATION         int32
NUMTARGET        int16
TARGETID         int64
BRICKID          int32
BRICK_OBJID      int32
FA_TARGET        int64
FA_TYPE          binary
TARGET_RA        float64
TARGET_DEC       float64
FIBERASSIGN_X    float32
FIBERASSIGN_Y    float32
BRICKNAME        char[8]
FIBERSTATUS      int32
PETAL_LOC        int16
DEVICE_LOC       int32
PRIORITY         int32
SUBPRIORITY      float64
FIBERFLUX_G      float32
FIBERFLUX_R      float32
FIBERFLUX_Z      float32
FIBERFLUX_IVAR_G float32
FIBERFLUX_IVAR_R float32
FIBERFLUX_IVAR_Z float32
================ ======= ===== ===================

Notes:

* This may be expanded to include aperture fluxes like ``FIBERTOTFLUX_[GRZ]``.

HDU3
----

EXTNAME = TARGETS

Target catalog row-matched to the FIBERASSIGN table entries.  Unassigned
fibers will have TARGETID=-1 here.

Note: we are considering deprecating this HDU and merging all additional
columns into the FIBERASSIGN HDU.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================= ===== =======================
KEY      Example Value           Type  Comment
======== ======================= ===== =======================
NAXIS1   576                     int   width of table in bytes
NAXIS2   5014                    int   number of rows in table
TILEID   11108                   int
TILERA   150.87                  float
TILEDEC  31.23                   float
FIELDROT 0.0707542268034296      float
FA_DATE  2022-07-01T00:00:00.000 str
FA_HA    0.0                     float
REQRA    150.87                  float
REQDEC   31.23                   float
FIELDNUM 0                       int
FA_VER   1.2.0                   str
FA_SURV  main                    str
======== ======================= ===== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

================================= ========== ===== ===================
Name                              Type       Units Description
================================= ========== ===== ===================
TARGETID                          int64
PETAL_LOC                         int16
DEVICE_LOC                        int32
LOCATION                          int32
FIBER                             int32
FIBERSTATUS                       int32
RA                                float64
DEC                               float64
PMRA                              float32
PMDEC                             float32
PMRA_IVAR                         float32
PMDEC_IVAR                        float32
REF_EPOCH                         float32
LAMBDA_REF                        float32
FA_TARGET                         int64
FA_TYPE                           binary
OBJTYPE                           char[3]
FIBERASSIGN_X                     float32
FIBERASSIGN_Y                     float32
NUMTARGET                         int16
PRIORITY                          int32
SUBPRIORITY                       float64
OBSCONDITIONS                     int32
NUMOBS_MORE                       int32
RELEASE                           int16
BRICKID                           int32
BRICKNAME                         char[8]
BRICK_OBJID                       int32
MORPHTYPE                         char[4]
RA_IVAR                           float32
DEC_IVAR                          float32
DCHISQ                            float32[5]
FLUX_G                            float32
FLUX_R                            float32
FLUX_Z                            float32
FLUX_W1                           float32
FLUX_W2                           float32
FLUX_W3                           float32
FLUX_W4                           float32
FLUX_IVAR_G                       float32
FLUX_IVAR_R                       float32
FLUX_IVAR_Z                       float32
FLUX_IVAR_W1                      float32
FLUX_IVAR_W2                      float32
FLUX_IVAR_W3                      float32
FLUX_IVAR_W4                      float32
MW_TRANSMISSION_G                 float32
MW_TRANSMISSION_R                 float32
MW_TRANSMISSION_Z                 float32
MW_TRANSMISSION_W1                float32
MW_TRANSMISSION_W2                float32
MW_TRANSMISSION_W3                float32
MW_TRANSMISSION_W4                float32
NOBS_G                            int16
NOBS_R                            int16
NOBS_Z                            int16
FRACFLUX_G                        float32
FRACFLUX_R                        float32
FRACFLUX_Z                        float32
FRACMASKED_G                      float32
FRACMASKED_R                      float32
FRACMASKED_Z                      float32
FRACIN_G                          float32
FRACIN_R                          float32
FRACIN_Z                          float32
ALLMASK_G                         float32
ALLMASK_R                         float32
ALLMASK_Z                         float32
WISEMASK_W1                       binary
WISEMASK_W2                       binary
PSFDEPTH_G                        float32
PSFDEPTH_R                        float32
PSFDEPTH_Z                        float32
GALDEPTH_G                        float32
GALDEPTH_R                        float32
GALDEPTH_Z                        float32
FRACDEV                           float32
FRACDEV_IVAR                      float32
SHAPEDEV_R                        float32
SHAPEDEV_R_IVAR                   float32
SHAPEDEV_E1                       float32
SHAPEDEV_E1_IVAR                  float32
SHAPEDEV_E2                       float32
SHAPEDEV_E2_IVAR                  float32
SHAPEEXP_R                        float32
SHAPEEXP_R_IVAR                   float32
SHAPEEXP_E1                       float32
SHAPEEXP_E1_IVAR                  float32
SHAPEEXP_E2                       float32
SHAPEEXP_E2_IVAR                  float32
APFLUX_G                          float32
APFLUX_R                          float32
APFLUX_Z                          float32
FIBERTOTFLUX_G                    float32
FIBERTOTFLUX_R                    float32
FIBERTOTFLUX_Z                    float32
REF_CAT                           char[2]
REF_ID                            int64
GAIA_PHOT_G_MEAN_MAG              float32
GAIA_PHOT_G_MEAN_FLUX_OVER_ERROR  float32
GAIA_PHOT_BP_MEAN_MAG             float32
GAIA_PHOT_BP_MEAN_FLUX_OVER_ERROR float32
GAIA_PHOT_RP_MEAN_MAG             float32
GAIA_PHOT_RP_MEAN_FLUX_OVER_ERROR float32
GAIA_PHOT_BP_RP_EXCESS_FACTOR     float32
GAIA_ASTROMETRIC_SIGMA5D_MAX      float32
GAIA_ASTROMETRIC_PARAMS_SOLVED    int64
GAIA_ASTROMETRIC_EXCESS_NOISE     float32
GAIA_DUPLICATED_SOURCE            logical
PARALLAX                          float32
PARALLAX_IVAR                     float32
MASKBITS                          int16
EBV                               float32
PHOTSYS                           char[1]
DESI_TARGET                       int64
BGS_TARGET                        int64
MWS_TARGET                        int64
PRIORITY_INIT                     int64
NUMOBS_INIT                       int64
HPXPIXEL                          int64
PRIORITY_INIT_DARK                int64
NUMOBS_INIT_DARK                  int64
PRIORITY_INIT_BRIGHT              int64
NUMOBS_INIT_BRIGHT                int64
APFLUX_IVAR_G                     float64
APFLUX_IVAR_R                     float64
APFLUX_IVAR_Z                     float64
================================= ========== ===== ===================


HDU4
----

EXTNAME = POTENTIAL_ASSIGNMENTS

A list of targets that could have been assigned to each fiber.
Note that the same target could appear more than once if it is covered
by more than one fiber


Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================= ===== =======================
KEY      Example Value           Type  Comment
======== ======================= ===== =======================
NAXIS1   16                      int   width of table in bytes
NAXIS2   50645                   int   number of rows in table
TILEID   11108                   int
TILERA   150.87                  float
TILEDEC  31.23                   float
FIELDROT 0.0707542268034296      float
FA_DATE  2022-07-01T00:00:00.000 str
FA_HA    0.0                     float
REQRA    150.87                  float
REQDEC   31.23                   float
FIELDNUM 0                       int
FA_VER   1.2.0                   str
FA_SURV  main                    str
======== ======================= ===== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

======== ===== ===== ===========
Name     Type  Units Description
======== ===== ===== ===========
TARGETID int64       Unique Target ID
FIBER    int32       Fiber number on the spectrographs [0-4999]
LOCATION int32       1000*PETAL_LOC + DEVICE_LOC location on focal plane
======== ===== ===== ===========

HDU5
----

EXTNAME = FASSIGN

*Description needed.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================= ===== =======================
KEY      Example Value           Type  Comment
======== ======================= ===== =======================
NAXIS1   66                      int   width of table in bytes
NAXIS2   5020                    int   number of rows in table
TILEID   11108                   int
TILERA   150.87                  float
TILEDEC  31.23                   float
FIELDROT 0.0707542268034296      float
FA_DATE  2022-07-01T00:00:00.000 str
FA_HA    0.0                     float
REQRA    150.87                  float
REQDEC   31.23                   float
FIELDNUM 0                       int
FA_VER   1.2.0                   str
FA_SURV  main                    str
======== ======================= ===== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

============= ======= ===== ===================
Name          Type    Units Description
============= ======= ===== ===================
FIBER         int32         *Description needed*
TARGETID      int64         *Description needed*
LOCATION      int32         *Description needed*
FIBERSTATUS   int32         *Description needed*
LAMBDA_REF    float32       *Description needed*
PETAL_LOC     int16         *Description needed*
DEVICE_LOC    int32         *Description needed*
DEVICE_TYPE   char[3]       *Description needed*
TARGET_RA     float64       *Description needed*
TARGET_DEC    float64       *Description needed*
FA_TARGET     int64         *Description needed*
FA_TYPE       binary        *Description needed*
FIBERASSIGN_X float32       *Description needed*
FIBERASSIGN_Y float32       *Description needed*
============= ======= ===== ===================

HDU6
----

EXTNAME = FTARGETS

*Description needed.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================= ===== =======================
KEY      Example Value           Type  Comment
======== ======================= ===== =======================
NAXIS1   53                      int   width of table in bytes
NAXIS2   5014                    int   number of rows in table
TILEID   11108                   int
TILERA   150.87                  float
TILEDEC  31.23                   float
FIELDROT 0.0707542268034296      float
FA_DATE  2022-07-01T00:00:00.000 str
FA_HA    0.0                     float
REQRA    150.87                  float
REQDEC   31.23                   float
FIELDNUM 0                       int
FA_VER   1.2.0                   str
FA_SURV  main                    str
======== ======================= ===== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

============= ======= ===== ===================
Name          Type    Units Description
============= ======= ===== ===================
TARGETID      int64         *Description needed*
TARGET_RA     float64       *Description needed*
TARGET_DEC    float64       *Description needed*
FA_TARGET     int64         *Description needed*
FA_TYPE       binary        *Description needed*
PRIORITY      int32         *Description needed*
SUBPRIORITY   float64       *Description needed*
OBSCONDITIONS int32         *Description needed*
NUMOBS_MORE   int32         *Description needed*
============= ======= ===== ===================

HDU7
----

EXTNAME = FAVAIL

*Description needed.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================= ===== =======================
KEY      Example Value           Type  Comment
======== ======================= ===== =======================
NAXIS1   16                      int   width of table in bytes
NAXIS2   50645                   int   number of rows in table
TILEID   11108                   int
TILERA   150.87                  float
TILEDEC  31.23                   float
FIELDROT 0.0707542268034296      float
FA_DATE  2022-07-01T00:00:00.000 str
FA_HA    0.0                     float
REQRA    150.87                  float
REQDEC   31.23                   float
FIELDNUM 0                       int
FA_VER   1.2.0                   str
FA_SURV  main                    str
======== ======================= ===== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

======== ===== ===== ===================
Name     Type  Units Description
======== ===== ===== ===================
LOCATION int32       *Description needed*
FIBER    int32       *Description needed*
TARGETID int64       *Description needed*
======== ===== ===== ===================

Notes and Examples
==================

To do...
