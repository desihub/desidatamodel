=================
fiberassign-EXPID
=================

:Summary: The fiberassign file contains the fiber positioner configuration information for
    each exposure: what fiber is placed where, what target that is, etc.
:Naming Convention: ``fiberassign-EXPID.fits.gz``, where EXPID is the zero-padded
    8-digit exposure ID.
:Regex: ``fiberassign-[0-9]{8}\.fits\.gz``
:File Type: FITS, 5 MB

Contents
========

====== ===================== ======== ===================
Number EXTNAME               Type     Contents
====== ===================== ======== ===================
HDU0_  PRIMARY               IMAGE    *Brief Description*
HDU1_  FIBERASSIGN           BINTABLE *Brief Description*
HDU2_  SKY_MONITOR           BINTABLE *Brief Description*
HDU3_  GFA_TARGETS           BINTABLE *Brief Description*
HDU4_  TARGETS               BINTABLE *Brief Description*
HDU5_  POTENTIAL_ASSIGNMENTS BINTABLE *Brief Description*
====== ===================== ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================= ===== =======
KEY      Example Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           Type  Comment
======== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================= ===== =======
TILEID   4403                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    int
TILERA   170.239                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 float
TILEDEC  -7.093                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  float
FIELDROT 0.0210480650645507                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      float
FA_PLAN  2022-07-01T00:00:00.000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 str
FA_HA    -6.72                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   float
FA_RUN   2022-01-03T17:00:31+00:00                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               str
FA_M_GFA 0.4                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     float
FA_M_PET 0.4                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     float
FA_M_POS 0.05                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    float
REQRA    170.239                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 float
REQDEC   -7.093                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  float
FIELDNUM 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       int
FA_VER   5.4.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   str
FA_SURV  main                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    str
FAFLAVOR maindark                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                str
DESIROOT /data/datasystems                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       str
GFA      DESIROOT/target/catalogs/dr9/1.1.1/gfas                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 str
MTL      DESIROOT/survey/ops/surveyops/trunk/mtl/main/dark                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       str
SCND     DESIROOT/target/catalogs/dr9/1.1.1/targets/main/secondary/dark/targets-dark-secondary.fits                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              str
SCND2    DESIROOT/target/catalogs/dr9/1.1.1/targets/main2/secondary/dark/main2targets-dark-secondary.fits                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        str
SCNDMTL  DESIROOT/survey/ops/surveyops/trunk/mtl/main/secondary/dark                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             str
SKY      DESIROOT/target/catalogs/dr9/1.1.1/skies                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                str
SKYSUPP  DESIROOT/target/catalogs/gaiadr2/1.1.1/skies-supp                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       str
TARG     DESIROOT/target/catalogs/dr9/1.1.1/targets/main/resolve/dark                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            str
TOO      DESIROOT/survey/ops/surveyops/trunk/mtl/main/ToO/ToO.ecsv                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               str
FAARGS   --doclean n --dr dr9 --dtver 1.1.1 --gaiadr gaiadr2 --goaltime 1000.0 --ha -6.72 --hdr_faprgrm dark --hdr_survey main --log_stdout False --lookup_sky_source ls --margin_gfa 0.4 --margin_petal 0.4 --margin_pos 0.05 --mintfrac 0.85 --mtltime 2022-01-13T18:13:09+00:00 --nosteps qa --pmcorr n --pmtime_utc_str 2022-01-14T10:13:28+00:00 --program DARK --rundate 2022-01-03T17:00:31+00:00 --sbprof ELG --sky_per_petal 40 --sky_per_slitblock 1 --standards_per_petal 10 --steps tiles,sky,gfa,targ,scnd,too,fa,zip,move,qa --survey main --svntiledir /data/tiles/SVN_tiles --tiledec -7.093 --tileid 4403 --tilera 170.239 --worldreadable True str
OUTDIR   /data/datasystems/target/fiberassign/holding_pen/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       str
SURVEY   main                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    str
NOWTIME  2022-01-14T10:13:28+00:00                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               str
RUNDATE  2022-01-03T17:00:31+00:00                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               str
PMCORR   n                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       str
PMTIME   2022-01-14T10:13:28+00:00                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               str
FAPRGRM  dark                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    str
MTLTIME  2022-01-13T18:13:09+00:00                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               str
OBSCON   DARK|GRAY|BRIGHT|BACKUP                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 str
GOALTIME 1000.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  float
GOALTYPE DARK                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    str
EBVFAC   1.08401875659818                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        float
SBPROF   ELG                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     str
MINTFRAC 0.85                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    float
FASCRIPT /software/datasystems/desiconda/20200924/code/fiberassign/5.4.0/bin/fba_launch                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          str
SVNDM    138481                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  str
SVNMTL   1083                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    str
LKSKYSRC ls                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      str
======== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================= ===== =======

Empty HDU.

HDU1
----

EXTNAME = FIBERASSIGN

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== =======================
KEY      Example Value             Type  Comment
======== ========================= ===== =======================
NAXIS1   293                       int   width of table in bytes
NAXIS2   5000                      int   number of rows in table
TILEID   4403                      int
TILERA   170.239                   float
TILEDEC  -7.093                    float
FIELDROT 0.0210480650645507        float
FA_PLAN  2022-07-01T00:00:00.000   str
FA_HA    -6.72                     float
FA_RUN   2022-01-03T17:00:31+00:00 str
FA_M_GFA 0.4                       float
FA_M_PET 0.4                       float
FA_M_POS 0.05                      float
REQRA    170.239                   float
REQDEC   -7.093                    float
FIELDNUM 0                         int
FA_VER   5.4.0                     str
FA_SURV  main                      str
======== ========================= ===== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

===================== ======= ===== ===================
Name                  Type    Units Description
===================== ======= ===== ===================
TARGETID              int64         label for field   1
PETAL_LOC             int16         label for field   2
DEVICE_LOC            int32         label for field   3
LOCATION              int32         label for field   4
FIBER                 int32         label for field   5
FIBERSTATUS           int32         label for field   6
TARGET_RA             float64       label for field   7
TARGET_DEC            float64       label for field   8
PMRA                  float32       label for field   9
PMDEC                 float32       label for field  10
REF_EPOCH             float32       label for field  11
LAMBDA_REF            float32       label for field  12
FA_TARGET             int64         label for field  13
FA_TYPE               binary        label for field  14
OBJTYPE               char[3]       label for field  15
FIBERASSIGN_X         float32       label for field  16
FIBERASSIGN_Y         float32       label for field  17
PRIORITY              int32         label for field  18
SUBPRIORITY           float64       label for field  19
OBSCONDITIONS         int32         label for field  20
RELEASE               int16         label for field  21
BRICKNAME             char[8]       label for field  22
BRICKID               int32         label for field  23
BRICK_OBJID           int32         label for field  24
MORPHTYPE             char[4]       label for field  25
EBV                   float32       label for field  26
FLUX_G                float32       label for field  27
FLUX_R                float32       label for field  28
FLUX_Z                float32       label for field  29
FLUX_W1               float32       label for field  30
FLUX_W2               float32       label for field  31
FLUX_IVAR_G           float32       label for field  32
FLUX_IVAR_R           float32       label for field  33
FLUX_IVAR_Z           float32       label for field  34
FLUX_IVAR_W1          float32       label for field  35
FLUX_IVAR_W2          float32       label for field  36
FIBERFLUX_G           float32       label for field  37
FIBERFLUX_R           float32       label for field  38
FIBERFLUX_Z           float32       label for field  39
FIBERTOTFLUX_G        float32       label for field  40
FIBERTOTFLUX_R        float32       label for field  41
FIBERTOTFLUX_Z        float32       label for field  42
MASKBITS              int16         label for field  43
SERSIC                float32       label for field  44
SHAPE_R               float32       label for field  45
SHAPE_E1              float32       label for field  46
SHAPE_E2              float32       label for field  47
REF_ID                int64         label for field  48
REF_CAT               char[2]       label for field  49
GAIA_PHOT_G_MEAN_MAG  float32       label for field  50
GAIA_PHOT_BP_MEAN_MAG float32       label for field  51
GAIA_PHOT_RP_MEAN_MAG float32       label for field  52
PARALLAX              float32       label for field  53
PHOTSYS               char[1]       label for field  54
PRIORITY_INIT         int64         label for field  55
NUMOBS_INIT           int64         label for field  56
DESI_TARGET           int64         label for field  57
BGS_TARGET            int64         label for field  58
MWS_TARGET            int64         label for field  59
SCND_TARGET           int64         label for field  60
PLATE_RA              float64       label for field  61
PLATE_DEC             float64       label for field  62
===================== ======= ===== ===================

HDU2
----

EXTNAME = SKY_MONITOR

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== =======================
KEY      Example Value             Type  Comment
======== ========================= ===== =======================
NAXIS1   99                        int   width of table in bytes
NAXIS2   20                        int   number of rows in table
TILEID   4403                      int
TILERA   170.239                   float
TILEDEC  -7.093                    float
FIELDROT 0.0210480650645507        float
FA_PLAN  2022-07-01T00:00:00.000   str
FA_HA    -6.72                     float
FA_RUN   2022-01-03T17:00:31+00:00 str
FA_M_GFA 0.4                       float
FA_M_PET 0.4                       float
FA_M_POS 0.05                      float
REQRA    170.239                   float
REQDEC   -7.093                    float
FIELDNUM 0                         int
FA_VER   5.4.0                     str
FA_SURV  main                      str
======== ========================= ===== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

============= ======= ===== ===================
Name          Type    Units Description
============= ======= ===== ===================
FIBER         int32         label for field   1
LOCATION      int32         label for field   2
TARGETID      int64         label for field   3
BRICKID       int32         label for field   4
BRICK_OBJID   int32         label for field   5
FA_TARGET     int64         label for field   6
FA_TYPE       binary        label for field   7
TARGET_RA     float64       label for field   8
TARGET_DEC    float64       label for field   9
FIBERASSIGN_X float32       label for field  10
FIBERASSIGN_Y float32       label for field  11
BRICKNAME     char[8]       label for field  12
FIBERSTATUS   int32         label for field  13
PETAL_LOC     int16         label for field  14
DEVICE_LOC    int32         label for field  15
PRIORITY      int32         label for field  16
SUBPRIORITY   float64       label for field  17
FIBERFLUX_G   float32       label for field  18
FIBERFLUX_R   float32       label for field  19
FIBERFLUX_Z   float32       label for field  20
============= ======= ===== ===================

HDU3
----

EXTNAME = GFA_TARGETS

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== =======================
KEY      Example Value             Type  Comment
======== ========================= ===== =======================
NAXIS1   172                       int   width of table in bytes
NAXIS2   988                       int   number of rows in table
TILEID   4403                      int
TILERA   170.239                   float
TILEDEC  -7.093                    float
FIELDROT 0.0210480650645507        float
FA_PLAN  2022-07-01T00:00:00.000   str
FA_HA    -6.72                     float
FA_RUN   2022-01-03T17:00:31+00:00 str
FA_M_GFA 0.4                       float
FA_M_PET 0.4                       float
FA_M_POS 0.05                      float
REQRA    170.239                   float
REQDEC   -7.093                    float
FIELDNUM 0                         int
FA_VER   5.4.0                     str
FA_SURV  main                      str
======== ========================= ===== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

================================= ======= ===== ===================
Name                              Type    Units Description
================================= ======= ===== ===================
RELEASE                           int32         label for field   1
TARGETID                          int64         label for field   2
BRICKID                           int32         label for field   3
BRICK_OBJID                       int32         label for field   4
TARGET_RA                         float64       label for field   5
TARGET_DEC                        float64       label for field   6
TARGET_RA_IVAR                    float32       label for field   7
TARGET_DEC_IVAR                   float32       label for field   8
MORPHTYPE                         char[4]       label for field   9
MASKBITS                          int16         label for field  10
FLUX_G                            float32       label for field  11
FLUX_R                            float32       label for field  12
FLUX_Z                            float32       label for field  13
FLUX_IVAR_G                       float32       label for field  14
FLUX_IVAR_R                       float32       label for field  15
FLUX_IVAR_Z                       float32       label for field  16
REF_ID                            int64         label for field  17
REF_CAT                           char[2]       label for field  18
REF_EPOCH                         float32       label for field  19
PARALLAX                          float32       label for field  20
PARALLAX_IVAR                     float32       label for field  21
PMRA                              float32       label for field  22
PMDEC                             float32       label for field  23
PMRA_IVAR                         float32       label for field  24
PMDEC_IVAR                        float32       label for field  25
GAIA_PHOT_G_MEAN_MAG              float32       label for field  26
GAIA_PHOT_G_MEAN_FLUX_OVER_ERROR  float32       label for field  27
GAIA_PHOT_BP_MEAN_MAG             float32       label for field  28
GAIA_PHOT_BP_MEAN_FLUX_OVER_ERROR float32       label for field  29
GAIA_PHOT_RP_MEAN_MAG             float32       label for field  30
GAIA_PHOT_RP_MEAN_FLUX_OVER_ERROR float32       label for field  31
GAIA_ASTROMETRIC_EXCESS_NOISE     float32       label for field  32
URAT_ID                           int64         label for field  33
URAT_SEP                          float32       label for field  34
GAIA_PHOT_G_N_OBS                 int32         label for field  35
HPXPIXEL                          int64         label for field  36
GFA_LOC                           int16         label for field  37
GUIDE_FLAG                        int16         label for field  38
FOCUS_FLAG                        int16         label for field  39
ETC_FLAG                          int16         label for field  40
================================= ======= ===== ===================

HDU4
----

EXTNAME = TARGETS

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== =======================
KEY      Example Value             Type  Comment
======== ========================= ===== =======================
NAXIS1   81                        int   width of table in bytes
NAXIS2   152687                    int   number of rows in table
TILEID   4403                      int
TILERA   170.239                   float
TILEDEC  -7.093                    float
FIELDROT 0.0210480650645507        float
FA_PLAN  2022-07-01T00:00:00.000   str
FA_HA    -6.72                     float
FA_RUN   2022-01-03T17:00:31+00:00 str
FA_M_GFA 0.4                       float
FA_M_PET 0.4                       float
FA_M_POS 0.05                      float
REQRA    170.239                   float
REQDEC   -7.093                    float
FIELDNUM 0                         int
FA_VER   5.4.0                     str
FA_SURV  main                      str
======== ========================= ===== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

============= ======= ===== ===================
Name          Type    Units Description
============= ======= ===== ===================
TARGETID      int64         label for field   1
RA            float64       label for field   2
DEC           float64       label for field   3
FA_TARGET     int64         label for field   4
FA_TYPE       binary        label for field   5
PRIORITY      int32         label for field   6
SUBPRIORITY   float64       label for field   7
OBSCONDITIONS int32         label for field   8
DESI_TARGET   int64         label for field   9
BGS_TARGET    int64         label for field  10
MWS_TARGET    int64         label for field  11
SCND_TARGET   int64         label for field  12
============= ======= ===== ===================

HDU5
----

EXTNAME = POTENTIAL_ASSIGNMENTS

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== =======================
KEY      Example Value             Type  Comment
======== ========================= ===== =======================
NAXIS1   16                        int   width of table in bytes
NAXIS2   169775                    int   number of rows in table
TILEID   4403                      int
TILERA   170.239                   float
TILEDEC  -7.093                    float
FIELDROT 0.0210480650645507        float
FA_PLAN  2022-07-01T00:00:00.000   str
FA_HA    -6.72                     float
FA_RUN   2022-01-03T17:00:31+00:00 str
FA_M_GFA 0.4                       float
FA_M_PET 0.4                       float
FA_M_POS 0.05                      float
REQRA    170.239                   float
REQDEC   -7.093                    float
FIELDNUM 0                         int
FA_VER   5.4.0                     str
FA_SURV  main                      str
======== ========================= ===== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

======== ===== ===== ===================
Name     Type  Units Description
======== ===== ===== ===================
TARGETID int64       label for field   1
FIBER    int32       label for field   2
LOCATION int32       label for field   3
======== ===== ===== ===================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
