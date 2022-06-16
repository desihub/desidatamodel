=================
fiberassign-EXPID
=================

:Summary: The fiberassign file contains the fiber positioner configuration information for
    each exposure: what fiber is placed where, what target that is, etc.
:Naming Convention: ``fiberassign-TILEID.fits.gz``, where TILEID is the zero-padded
    6-digit tile ID.
:Regex: ``fiberassign-[0-9]{6}\.fits\.gz``
:File Type: FITS, 5 MB

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
====== ===================== ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

No data, but some useful header keywords.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================= ===== =======
KEY      Example Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           Type  Comment
======== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================= ===== =======
TILEID   4403                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    int   Tile ID
TILERA   170.239                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 float [deg] Tile Right Ascension
TILEDEC  -7.093                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  float [deg] Tile Declination
FIELDROT 0.0210480650645507                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      float [deg] Field rotation
FA_PLAN  2022-07-01T00:00:00.000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 str   [UTC] Plan field rotations for this date
FA_HA    -6.72                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   float [deg] Design Hour Angle
FA_RUN   2022-01-03T17:00:31+00:00                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               str   [UTC] Date of the loaded Focal Plane state
FA_M_GFA 0.4                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     float [mm] Margin around GFA keep-out polygons
FA_M_PET 0.4                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     float [mm] Margin around petal-boundary keep-out polygons
FA_M_POS 0.05                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    float [mm] Margin around positioner keep-out polygons
REQRA    170.239                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 float [deg] Tile Right Ascension
REQDEC   -7.093                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  float [deg] Tile Declination
FIELDNUM 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       int   Not used, always zero
FA_VER   5.4.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   str   Fiberassign code version
FA_SURV  main                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    str   Survey of origin of the targets
FAFLAVOR maindark                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                str   String composed of the SURVEY and the PROGRAM
DESIROOT /data/datasystems                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       str   DESI_ROOT environment variable path
GFA      DESIROOT/target/catalogs/dr9/1.1.1/gfas                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 str   Path to the input GFA targets
MTL      DESIROOT/survey/ops/surveyops/trunk/mtl/main/dark                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       str   Path to the primary targets ledgers
SCND     DESIROOT/target/catalogs/dr9/1.1.1/targets/main/secondary/dark/targets-dark-secondary.fits                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              str   Path to the secondary targets static catalogs
SCND2    DESIROOT/target/catalogs/dr9/1.1.1/targets/main2/secondary/dark/main2targets-dark-secondary.fits                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        str   Path to the secondary targets static catalogs
SCNDMTL  DESIROOT/survey/ops/surveyops/trunk/mtl/main/secondary/dark                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             str   Path to the secondary targets ledgers
SKY      DESIROOT/target/catalogs/dr9/1.1.1/skies                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                str   Path to the sky targets
SKYSUPP  DESIROOT/target/catalogs/gaiadr2/1.1.1/skies-supp                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       str   Path to the supp-sky targets
TARG     DESIROOT/target/catalogs/dr9/1.1.1/targets/main/resolve/dark                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            str   Path to the primary targets static catalogs
TOO      DESIROOT/survey/ops/surveyops/trunk/mtl/main/ToO/ToO.ecsv                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               str   Path to the Target-of-Opportunity catalog
FAARGS   --doclean n --dr dr9 --dtver 1.1.1 --gaiadr gaiadr2 --goaltime 1000.0 --ha -6.72 --hdr_faprgrm dark --hdr_survey main --log_stdout False --lookup_sky_source ls --margin_gfa 0.4 --margin_petal 0.4 --margin_pos 0.05 --mintfrac 0.85 --mtltime 2022-01-13T18:13:09+00:00 --nosteps qa --pmcorr n --pmtime_utc_str 2022-01-14T10:13:28+00:00 --program DARK --rundate 2022-01-03T17:00:31+00:00 --sbprof ELG --sky_per_petal 40 --sky_per_slitblock 1 --standards_per_petal 10 --steps tiles,sky,gfa,targ,scnd,too,fa,zip,move,qa --survey main --svntiledir /data/tiles/SVN_tiles --tiledec -7.093 --tileid 4403 --tilera 170.239 --worldreadable True str   fba_launch command arguments
OUTDIR   /data/datasystems/target/fiberassign/holding_pen/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       str   Folder where the fba_launch outputs are written
SURVEY   main                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    str   Survey of origin of the targets
NOWTIME  2022-01-14T10:13:28+00:00                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               str   [UTC] Date of the fba_launch call
RUNDATE  2022-01-03T17:00:31+00:00                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               str   [UTC] Date of the loaded Focal Plane state
PMCORR   n                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       str   Is proper-motion correction applied for stars?
PMTIME   2022-01-14T10:13:28+00:00                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               str   [UTC] Used current time, if proper-motion correction is applied
FAPRGRM  dark                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    str   Program to which this tile belongs
MTLTIME  2022-01-13T18:13:09+00:00                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               str   [UTC] Date used to read the ledgers
OBSCON   DARK|GRAY|BRIGHT|BACKUP                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 str   Allowed observing conditions for this tile
GOALTIME 1000.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  float [s] Aimed EFFTIME_SPEC
GOALTYPE DARK                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    str   Sky conditions used for some noise estimation
EBVFAC   1.08401875659818                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        float 10.0 ** (2.165 * median(EBV) / 2.5))
SBPROF   ELG                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     str   Source profile used for some noise estimation
MINTFRAC 0.85                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    float Fraction of GOALTIME to be reached by EFFTIME_SPEC to consider the tile has completed
FASCRIPT /software/datasystems/desiconda/20200924/code/fiberassign/5.4.0/bin/fba_launch                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          str   Path to the fba_launch used script
SVNDM    138481                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  str   DESIMODEL/data svn revision number
SVNMTL   1083                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    str   DESI_SURVEYOPS/mtl svn revision number
LKSKYSRC ls                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      str   Photometric survey used for the sky look-up table for the stuck fibers
======== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================= ===== =======

Empty HDU.

HDU1
----

EXTNAME = FIBERASSIGN

The target assignments for each fiber of this tile.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== =======================
KEY      Example Value             Type  Comment
======== ========================= ===== =======================
NAXIS1   293                       int   width of table in bytes
NAXIS2   5000                      int   number of rows in table
TILEID   4403                      int   Tile ID
TILERA   170.239                   float [deg] Tile Right Ascension
TILEDEC  -7.093                    float [deg] Tile Declination
FIELDROT 0.0210480650645507        float [deg] Field rotation
FA_PLAN  2022-07-01T00:00:00.000   str   [UTC] Plan field rotations for this date
FA_HA    -6.72                     float [deg] Design Hour Angle
FA_RUN   2022-01-03T17:00:31+00:00 str   [UTC] Date of the loaded Focal Plane state
FA_M_GFA 0.4                       float [mm] Margin around GFA keep-out polygons
FA_M_PET 0.4                       float [mm] Margin around petal-boundary keep-out polygons
FA_M_POS 0.05                      float [mm] Margin around positioner keep-out polygons
REQRA    170.239                   float [deg] Tile Right Ascension
REQDEC   -7.093                    float [deg] Tile Declination
FIELDNUM 0                         int   Not used, always zero
FA_VER   5.4.0                     str   Fiberassign code version
FA_SURV  main                      str   Survey of origin of the targets
======== ========================= ===== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

===================== ======= ============== ===================
Name                  Type    Units          Description
===================== ======= ============== ===================
TARGETID              int64                  Unique target ID
PETAL_LOC             int16                  Petal location [0-9]
DEVICE_LOC            int32                  Device location on focal plane [0-523]
LOCATION              int32                  Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBER                 int32                  Fiber ID on the CCDs [0-4999]
FIBERSTATUS           int32                  Fiber status mask; 0=good
TARGET_RA             float64 deg            Target Right Ascension
TARGET_DEC            float64 deg            Target Declination
PMRA                  float32 mas/yr         Proper motion in the RA direction (already including cosDEC term)
PMDEC                 float32 mas/yr         Proper motion in the DEC direction
REF_EPOCH             float32 yr             Reference catalog reference epoch (eg, 2015.5 for Gaia DR2)
LAMBDA_REF            float32 Angstrom       Wavelength at which targets should be centered on fibers
FA_TARGET             int64                  Targeting bit internally used by fiberassign (linked with FA_TYPE)
FA_TYPE               binary                 Target type (science, standard, sky, safe, suppsky)
OBJTYPE               char[3]                TGT, SKY, BAD, empty
FIBERASSIGN_X         float32 mm             Expected CS5 X location on focal plane
FIBERASSIGN_Y         float32 mm             Expected CS5 Y location on focal plane
PRIORITY              int32                  Assignment priority; larger = higher priority
SUBPRIORITY           float64                Assignment subpriority [0-1]
OBSCONDITIONS         int32                  Bit-coded of allowed observing conditions
RELEASE               int16                  Imaging release number
BRICKNAME             char[8]                Imaging Surveys brick name
BRICKID               int32                  Imaging Surveys brick ID
BRICK_OBJID           int32                  Imaging surveys OBJID on that brick
MORPHTYPE             char[4]                Imaging surveys morphological type
EBV                   float32 mag            Galactic extinction E(B-V) reddening
FLUX_G                float32 nanomaggy      Flux in g-band
FLUX_R                float32 nanomaggy      Flux in r-band
FLUX_Z                float32 nanomaggy      Flux in z-band
FLUX_W1               float32 nanomaggy      Flux in WISE W1-band
FLUX_W2               float32 nanomaggy      Flux in WISE W2-band
FLUX_IVAR_G           float32 nanomaggy^-2   Inverse variance of FLUX_G
FLUX_IVAR_R           float32 nanomaggy^-2   Inverse variance of FLUX_R
FLUX_IVAR_Z           float32 nanomaggy^-2   Inverse variance of FLUX_Z
FLUX_IVAR_W1          float32 nanomaggy^-2   Inverse variance of FLUX_W1
FLUX_IVAR_W2          float32 nanomaggy^-2   Inverse variance of FLUX_W2
FIBERFLUX_G           float32 nanomaggy      g-band object model flux for 1 arcsec seeing and 1.5 arcsec diameter fiber
FIBERFLUX_R           float32 nanomaggy      r-band object model flux for 1 arcsec seeing and 1.5 arcsec diameter fiber
FIBERFLUX_Z           float32 nanomaggy      z-band object model flux for 1 arcsec seeing and 1.5 arcsec diameter fiber
FIBERTOTFLUX_G        float32 nanomaggy      like FIBERFLUX_G but including all objects overlapping this location
FIBERTOTFLUX_R        float32 nanomaggy      like FIBERFLUX_R but including all objects overlapping this location
FIBERTOTFLUX_Z        float32 nanomaggy      like FIBERFLUX_Z but including all objects overlapping this location
MASKBITS              int16                  Bitwise mask from the imaging indicating potential issue or blending
SERSIC                float32                Power-law index for the Sersic profile model
SHAPE_R               float32 arcsec         Half-light radius of galaxy model for galaxy type
SHAPE_E1              float32                Ellipticity component 1 of galaxy model for galaxy type
SHAPE_E2              float32                Ellipticity component 2 of galaxy model for galaxy type
REF_ID                int64                  Astrometric catalog reference ID (SOURCE_ID from Gaia and SGA; built from TYC1, TYC2, TYC3 for Tycho2)
REF_CAT               char[2]                Reference catalog source for this star
GAIA_PHOT_G_MEAN_MAG  float32 mag            Gaia G band mag
GAIA_PHOT_BP_MEAN_MAG float32 mag            Gaia BP mag
GAIA_PHOT_RP_MEAN_MAG float32 mag            Gaia RP mag
PARALLAX              float32 mas            Reference catalog parallax
PHOTSYS               char[1]                'N' for the MzLS/BASS photometric system, 'S' for DECaLS, 'G' for Gaia, '' for stuck/broken fibers
PRIORITY_INIT         int64                  Initial priority for target calculated across target selection bitmasks and OBSCONDITIONS
NUMOBS_INIT           int64                  Initial number of observations for target calculated across target selection bitmasks and OBSCONDITIONS
DESI_TARGET           int64                  Dark survey + calibration bitmask
BGS_TARGET            int64                  Bright Galaxy Survey bitmask
MWS_TARGET            int64                  Milky Way Survey bitmask
SCND_TARGET           int64                  Secondary programs bitmask
PLATE_RA              float64 deg            Right Ascension to be used by PlateMaker
PLATE_DEC             float64 deg            Declination to be used by PlateMaker
===================== ======= ============== ===================

HDU2
----

EXTNAME = SKY_MONITOR

Blank sky assignments for sky monitor positioners.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== =======================
KEY      Example Value             Type  Comment
======== ========================= ===== =======================
NAXIS1   99                        int   width of table in bytes
NAXIS2   20                        int   number of rows in table
TILEID   4403                      int   Tile ID
TILERA   170.239                   float [deg] Tile Right Ascension
TILEDEC  -7.093                    float [deg] Tile Declination
FIELDROT 0.0210480650645507        float [deg] Field rotation
FA_PLAN  2022-07-01T00:00:00.000   str   [UTC] Plan field rotations for this date
FA_HA    -6.72                     float [deg] Design Hour Angle
FA_RUN   2022-01-03T17:00:31+00:00 str   [UTC] Date of the loaded Focal Plane state
FA_M_GFA 0.4                       float [mm] Margin around GFA keep-out polygons
FA_M_PET 0.4                       float [mm] Margin around petal-boundary keep-out polygons
FA_M_POS 0.05                      float [mm] Margin around positioner keep-out polygons
REQRA    170.239                   float [deg] Tile Right Ascension
REQDEC   -7.093                    float [deg] Tile Declination
FIELDNUM 0                         int   Not used, always zero
FA_VER   5.4.0                     str   Fiberassign code version
FA_SURV  main                      str   Survey of origin of the targets
======== ========================= ===== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

============= ======= =========== ===================
Name          Type    Units       Description
============= ======= =========== ===================
FIBER         int32               Fiber ID on the CCDs [0-4999]
LOCATION      int32               Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
TARGETID      int64               Unique target ID
BRICKID       int32               Imaging Surveys brick ID
BRICK_OBJID   int32               Imaging surveys OBJID on that brick
FA_TARGET     int64               Targeting bit internally used by fiberassign (linked with FA_TYPE)
FA_TYPE       binary              Target type (science, standard, sky, safe, suppsky)
TARGET_RA     float64 deg         Target Right Ascension
TARGET_DEC    float64 deg         Target Declination
FIBERASSIGN_X float32 mm          Expected CS5 X location on focal plane
FIBERASSIGN_Y float32 mm          Expected CS5 Y location on focal plane
BRICKNAME     char[8]             Imaging Surveys brick name
FIBERSTATUS   int32               Fiber status mask; 0=good
PETAL_LOC     int16               Petal location [0-9]
DEVICE_LOC    int32               Device location on focal plane [0-523]
PRIORITY      int32               Assignment priority; larger = higher priority
SUBPRIORITY   float64             Assignment subpriority [0-1]
FIBERFLUX_G   float32 nanomaggy   Flux in g-band
FIBERFLUX_R   float32 nanomaggy   Flux in r-band
FIBERFLUX_Z   float32 nanomaggy   Flux in z-band
============= ======= =========== ===================

HDU3
----

EXTNAME = GFA_TARGETS

GFA stars to be used by the ETC / GUIDE / FOCUS

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== =======================
KEY      Example Value             Type  Comment
======== ========================= ===== =======================
NAXIS1   172                       int   width of table in bytes
NAXIS2   988                       int   number of rows in table
TILEID   4403                      int   Tile ID
TILERA   170.239                   float [deg] Tile Right Ascension
TILEDEC  -7.093                    float [deg] Tile Declination
FIELDROT 0.0210480650645507        float [deg] Field rotation
FA_PLAN  2022-07-01T00:00:00.000   str   [UTC] Plan field rotations for this date
FA_HA    -6.72                     float [deg] Design Hour Angle
FA_RUN   2022-01-03T17:00:31+00:00 str   [UTC] Date of the loaded Focal Plane state
FA_M_GFA 0.4                       float [mm] Margin around GFA keep-out polygons
FA_M_PET 0.4                       float [mm] Margin around petal-boundary keep-out polygons
FA_M_POS 0.05                      float [mm] Margin around positioner keep-out polygons
REQRA    170.239                   float [deg] Tile Right Ascension
REQDEC   -7.093                    float [deg] Tile Declination
FIELDNUM 0                         int   Not used, always zero
FA_VER   5.4.0                     str   Fiberassign code version
FA_SURV  main                      str   Survey of origin of the targets
======== ========================= ===== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

================================= ======= ============== ===================
Name                              Type    Units          Description
================================= ======= ============== ===================
RELEASE                           int32                  Imaging release number
TARGETID                          int64                  Unique target ID
BRICKID                           int32                  Imaging Surveys brick ID
BRICK_OBJID                       int32                  Imaging surveys OBJID on that brick
TARGET_RA                         float64 deg            Target Right Ascension
TARGET_DEC                        float64 deg            Target Declination
TARGET_RA_IVAR                    float32 deg^-2         Inverse variance of TARGET_RA
TARGET_DEC_IVAR                   float32 deg^-2         Inverse variance of TARGET_DEC
MORPHTYPE                         char[4]                Imaging surveys morphological type
MASKBITS                          int16                  Bitwise mask from the imaging indicating potential issue or blending
FLUX_G                            float32 nanomaggy      Flux in g-band
FLUX_R                            float32 nanomaggy      Flux in r-band
FLUX_Z                            float32 nanomaggy      Flux in z-band
FLUX_IVAR_G                       float32 nanomaggy^-2   Inverse variance of FLUX_G
FLUX_IVAR_R                       float32 nanomaggy^-2   Inverse variance of FLUX_R
FLUX_IVAR_Z                       float32 nanomaggy^-2   Inverse variance of FLUX_Z
REF_ID                            int64                  Astrometric catalog reference ID (SOURCE_ID from Gaia and SGA; built from TYC1, TYC2, TYC3 for Tycho2)
REF_CAT                           char[2]                Reference catalog source for this star
REF_EPOCH                         float32 yr             Reference catalog reference epoch
PARALLAX                          float32 mas            Reference catalog parallax
PARALLAX_IVAR                     float32 mas^-2         Inverse variance of PARALLAX
PMRA                              float32 mas/yr         Proper motion in the RA direction (already including cosDEC term)
PMDEC                             float32 mas/yr         Proper motion in the DEC direction
PMRA_IVAR                         float32 yr^2/mas^2     Inverse variance of PMRA
PMDEC_IVAR                        float32 yr^2/mas^2     Inverse variance of PMDEC
GAIA_PHOT_G_MEAN_MAG              float32 mag            Gaia G band mag
GAIA_PHOT_G_MEAN_FLUX_OVER_ERROR  float32                Gaia G band signal-to-noise
GAIA_PHOT_BP_MEAN_MAG             float32 mag            Gaia BP band mag
GAIA_PHOT_BP_MEAN_FLUX_OVER_ERROR float32                Gaia BP signal-to-noise
GAIA_PHOT_RP_MEAN_MAG             float32 mag            Gaia RP band mag
GAIA_PHOT_RP_MEAN_FLUX_OVER_ERROR float32                Gaia RP signal-to-noise
GAIA_ASTROMETRIC_EXCESS_NOISE     float32                Gaia astrometric excess noise
URAT_ID                           int64                  URAT ID
URAT_SEP                          float32 arcsec         Distance separation to the URAT coordinates
GAIA_PHOT_G_N_OBS                 int32                  Gaia G band number of observations
HPXPIXEL                          int64                  HEALPixel containing GFA target
GFA_LOC                           int16                  Covered GFA identifier
GUIDE_FLAG                        int16                  GUIDING bitmask
FOCUS_FLAG                        int16                  FOCUS bitmask
ETC_FLAG                          int16                  ETC bitmask
================================= ======= ============== ===================

HDU4
----

EXTNAME = TARGETS

Unique list of targets reachable by a positioner.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== =======================
KEY      Example Value             Type  Comment
======== ========================= ===== =======================
NAXIS1   81                        int   width of table in bytes
NAXIS2   152687                    int   number of rows in table
TILEID   4403                      int   Tile ID
TILERA   170.239                   float [deg] Tile Right Ascension
TILEDEC  -7.093                    float [deg] Tile Declination
FIELDROT 0.0210480650645507        float [deg] Field rotation
FA_PLAN  2022-07-01T00:00:00.000   str   [UTC] Plan field rotations for this date
FA_HA    -6.72                     float [deg] Design Hour Angle
FA_RUN   2022-01-03T17:00:31+00:00 str   [UTC] Date of the loaded Focal Plane state
FA_M_GFA 0.4                       float [mm] Margin around GFA keep-out polygons
FA_M_PET 0.4                       float [mm] Margin around petal-boundary keep-out polygons
FA_M_POS 0.05                      float [mm] Margin around positioner keep-out polygons
REQRA    170.239                   float [deg] Tile Right Ascension
REQDEC   -7.093                    float [deg] Tile Declination
FIELDNUM 0                         int   Not used, always zero
FA_VER   5.4.0                     str   Fiberassign code version
FA_SURV  main                      str   Survey of origin of the targets
======== ========================= ===== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

============= ======= ===== ===================
Name          Type    Units Description
============= ======= ===== ===================
TARGETID      int64         Unique target ID
RA            float64 deg   Target Right Ascension
DEC           float64 deg   Target Declination
FA_TARGET     int64         Targeting bit internally used by fiberassign (linked with FA_TYPE)
FA_TYPE       binary        Target type (science, standard, sky, safe, suppsky)
PRIORITY      int32         Assignment priority; larger = higher priority
SUBPRIORITY   float64       Assignment subpriority [0-1]
OBSCONDITIONS int32         Bit-coded of allowed observing conditions
DESI_TARGET   int64         Dark survey + calibration bitmask 
BGS_TARGET    int64         Bright Galaxy Survey bitmask
MWS_TARGET    int64         Milky Way Survey bitmask
SCND_TARGET   int64         Secondary programs bitmask
============= ======= ===== ===================

HDU5
----

EXTNAME = POTENTIAL_ASSIGNMENTS

A list of targets that could have been assigned to each fiber.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== =======================
KEY      Example Value             Type  Comment
======== ========================= ===== =======================
NAXIS1   16                        int   width of table in bytes
NAXIS2   169775                    int   number of rows in table
TILEID   4403                      int   Tile ID
TILERA   170.239                   float [deg] Tile Right Ascension
TILEDEC  -7.093                    float [deg] Tile Declination
FIELDROT 0.0210480650645507        float [deg] Field rotation
FA_PLAN  2022-07-01T00:00:00.000   str   [UTC] Plan field rotations for this date
FA_HA    -6.72                     float [deg] Design Hour Angle
FA_RUN   2022-01-03T17:00:31+00:00 str   [UTC] Date of the loaded Focal Plane state
FA_M_GFA 0.4                       float [mm] Margin around GFA keep-out polygons
FA_M_PET 0.4                       float [mm] Margin around petal-boundary keep-out polygons
FA_M_POS 0.05                      float [mm] Margin around positioner keep-out polygons
REQRA    170.239                   float [deg] Tile Right Ascension
REQDEC   -7.093                    float [deg] Tile Declination
FIELDNUM 0                         int   Not used, always zero
FA_VER   5.4.0                     str   Fiberassign code version
FA_SURV  main                      str   Survey of origin of the targets
======== ========================= ===== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

======== ===== ===== ===================
Name     Type  Units Description
======== ===== ===== ===================
TARGETID int64       Unique target ID
FIBER    int32       Fiber ID on the CCDs [0-4999]
LOCATION int32       Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
======== ===== ===== ===================


Notes and Examples
==================

* HDU0: early tiles may have some missing keywords from the listed ones.
* HDU1: this table defines the *requested* fiber assignments; see :doc:`fibermap-EXPID <../../../../../DESI_SPECTRO_DATA/NIGHT/EXPID/fibermap-EXPID>` for the actual observed assignments.
* HDU1: ``LAMBDA_REF`` : 5400 so far, not used for fiber positioning.
* HDU1, HDU4, HDU5: files built from CMX, SV1, SV2, or SV3 targets will have a slightly different column content for the targetings bit columns (e.g., ``CMX_TARGET``, ``SV1_DESI_TARGET``).
* HDU2: ``BRICKID``, ``BRICK_OBJID``, ``FA_TARGET``, ``BRICKNAME``, ``PRIORITY``, ``SUBPRIORITY``, ``FIBERFLUX_G``, ``FIBERFLUX_R``, ``FIBERFLUX_Z`` mostly are a zero value (and an empty string for ``BRICKNAME``).
* HDU3: for objects that do not have a match in URAT, the ``URAT_ID`` and ``URAT_SEP`` columns are -1.
* HDU5: the same target can appear more than once if it is reachable by more than one fiber.
