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

Contents
========

====== ===================== ======== ===================
Number EXTNAME               Type     Contents
====== ===================== ======== ===================
HDU0_  PRIMARY               IMAGE    Blank
HDU1_  FIBERASSIGN           BINTABLE Target assignments for each fiber
HDU2_  GFA_TARGETS           BINTABLE Targets on GFAs
HDU3_  SKY_MONITOR           BINTABLE Sky assignments for sky monitor positioners
HDU4_  TARGETS               BINTABLE Target catalog row-matched to FIBERASSIGN table
HDU5_  POTENTIAL_ASSIGNMENTS BINTABLE All targets that could have been assigned
====== ===================== ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

No data, but some useful header keywords

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============= ===== ========================================
KEY      Example Value Type  Comment
======== ============= ===== ========================================
NAXIS1   0             int
TILEID   1165          int
REQRA    150.69        float
REQDEC   33.86         float
TILERA   150.69        float
TILEDEC  33.86         float
REFEPOCH 2015.5        str
FIELDNUM 0             int   Field configuration number for this tile
======== ============= ===== ========================================

Data: FITS image [float64, 0]

HDU1
----

EXTNAME = FIBERASSIGN

The target assignments for each fiber of this tile.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============= ===== =====================
KEY      Example Value Type  Comment
======== ============= ===== =====================
NAXIS1   258           int   
NAXIS2   5000          int   Number of fibers
TILEID   1165          int   Unique Tile ID
REQRA    150.69        float Requested telescope RA [degees]
REQDEC   33.86         float Requested telescope dec [degrees]
TILERA   150.69        float Tile center RA [degrees]
TILEDEC  33.86         float Tile center DEC [degrees]
REFEPOCH 2015.5        str   Astrometry reference epoch
======== ============= ===== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

================ ======= ============ ===========
Name             Type    Units        Description
================ ======= ============ ===========
TARGETID         int64                Unique target ID
FIBER            int32                Fiber ID on the CCDs [0-4999]
PETAL_LOC        int16                Petal location [0-9]
DEVICE_LOC       int32                Device location on focal plane [0-523]
LOCATION         int32                Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBERSTATUS      int32                Fiber status mask; 0=good
OBJTYPE          char[3]              SKY, OBJ, NON
DESI_TARGET      int64                Dark survey + calibration targeting bits
BGS_TARGET       int64                Bright Galaxy Survey targeting bits
MWS_TARGET       int64                Milky Way Survey targeting bits
SECONDARY_TARGET int64                Secondary targets targeting bits
COMM_TARGET      int64                Commissioning targeting bits
SV1_DESI_TARGET  int64                Survey Validation targeting bits
SV1_BGS_TARGET   int64                Survey Validation targeting bits
SV1_MWS_TARGET   int64                Survey Validation targeting bits
TARGET_RA        float64 degrees      Target Right Ascension [degrees]
TARGET_DEC       float64 degrees      Target declination [degrees]
TARGET_RA_IVAR   float32 1/degrees^2  Inverse variance of TARGET_RA
TARGET_DEC_IVAR  float32 1/degrees^2  Inverse variance of TARGET_DEC
LAMBDA_REF       float32 Angstrom     Wavelength at which targets should be centered on fibers
DESIGN_X         float32 mm           Expected CS5 X location on focal plane
DESIGN_Y         float32 mm           Expected CS5 Y location on focal plane
DESIGN_Q         float32 degrees      CS5 Q azimuthal coordinate
DESIGN_S         float32 mm           CS5 S radial distance along curved focal surface
BRICKID          int64                Imaging Surveys brick ID
BRICK_OBJID      int64                Imaging surveys OBJID on that brick
TYPE             char[4]              Imaging surveys morphological type
PRIORITY         int32                Assignment priority; larger = higher priority
SUBPRIORITY      float64              Assignment subpriority [0-1]
NUMTARGET        int16                Total number of targets that this positioner covered
REF_ID           int64                Astrometric catalog reference ID (SOURCE_ID from GAIA)
PMRA             float32 marcsec/year Proper motion in the RA direction (already including cosDec term)
PMDEC            float32 marcsec/year Proper motion in the dec direction
PMRA_IVAR        float32              Inverse variance of PMRA
PMDEC_IVAR       float32              Inverse variance of PMDEC
FLUX_G           float32 nanomaggies  Flux in g-band
FLUX_R           float32 nanomaggies  Flux in r-band
FLUX_Z           float32 nanomaggies  Flux in z-band
FLUX_W1          float32 nanomaggies  Flux in WISE W1-band
FLUX_W2          float32 nanomaggies  Flux in WISE W2-band
FLUX_IVAR_G      float32              Inverse variance of FLUX_G
FLUX_IVAR_R      float32              Inverse variance of FLUX_R
FLUX_IVAR_Z      float32              Inverse variance of FLUX_Z
FLUX_IVAR_W1     float32              Inverse variance of FLUX_W1
FLUX_IVAR_W2     float32              Inverse variance of FLUX_W2
FIBERFLUX_G      float32 nanomaggies  g-band object model flux for 1 arcsec seeing and 1.5 arcsec diameter fiber
FIBERFLUX_R      float32 nanomaggies  r-band object model flux for 1 arcsec seeing and 1.5 arcsec diameter fiber
FIBERFLUX_Z      float32 nanomaggies  z-band object model flux for 1 arcsec seeing and 1.5 arcsec diameter fiber
FIBERTOTFLUX_G   float32 nanomaggies  like FIBERFLUX_G but including all objects overlapping this location
FIBERTOTFLUX_R   float32 nanomaggies  like FIBERFLUX_R but including all objects overlapping this location
FIBERTOTFLUX_Z   float32 nanomaggies  like FIBERFLUX_Z but including all objects overlapping this location
================ ======= ============ ===========

Missing columns to be added in the future:

  * PHOTSYS: N or S (maybe 0 or 1)
  * SV1_*_TARGET columns by be renamed

Notes:

* DESIGN_X/Y are where fiber assignment thought the targets would
  be; this is non-authoritative and more detailed downstream code will have
  a refined answer for each actual observation of this tile.
* This table defines the *requested* fiber assignments.  See
  :doc:`fiberassign <../../DESI_SPECTRO_DATA/NIGHT/EXPID/fibermap-EXPID>` for the
  actual observed assignments.

HDU2
----

EXTNAME = GFA_TARGETS

Table of objects that are on each GFA, including both point and extended sources.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============= ===== =====================
KEY      Example Value Type  Comment
======== ============= ===== =====================
NAXIS1   116           int   
NAXIS2   72            int   Number of targets
REQRA    150.69        float
REQDEC   33.86         float
REFEPOCH 2015.5        str
HPXNSIDE 64            int
HPXNEST  T             bool
======== ============= ===== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

See FIBERASSIGN table for column descriptions

================================ ======= ===== ===========
Name                             Type    Units Description
================================ ======= ===== ===========
TARGETID                         int64
BRICKID                          int32
BRICK_OBJID                      int32
TARGET_RA                        float64
TARGET_DEC                       float64
TARGET_RA_IVAR                   float32
TARGET_DEC_IVAR                  float32
TYPE                             char[4]
FLUX_G                           float32
FLUX_R                           float32
FLUX_Z                           float32
FLUX_IVAR_G                      float32
FLUX_IVAR_R                      float32
FLUX_IVAR_Z                      float32
REF_ID                           int64
PMRA                             float32
PMDEC                            float32
PMRA_IVAR                        float32
PMDEC_IVAR                       float32
GAIA_PHOT_G_MEAN_MAG             float32       Gaia G-band magnitude
GAIA_PHOT_G_MEAN_FLUX_OVER_ERROR float32       Gaia G-band signal-to-noise
ETC_FLAG                         int16         0=ok to use for exposure time calculator seeing and throughput
GUIDE_FLAG                       int16         0=ok to use for guiding
FOCUS_FLAG                       int16         0=ok to use for focus
HPXPIXEL                         int64         Healpixel number
GFA_LOC                          int16         GFA location [0-9] = PETAL_LOC
================================ ======= ===== ===========

HDU3
----

EXTNAME = SKY_MONITOR

Blank sky assignments for sky monitor positioners.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============= ==== =====================
KEY      Example Value Type Comment
======== ============= ==== =====================
NAXIS1   114           int  length of dimension 1
NAXIS2   20            int  length of dimension 2
ENCODING ascii         str
SEED     1028862084    int
HPXNSIDE 64            int
HPXNEST  T             bool
======== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

See the FIBERASSIGN table for a description of these columns

================ ======= ===== ===========
Name             Type    Units Description
================ ======= ===== ===========
BRICKID          int32
BRICK_OBJID      int32
TARGET_RA        float64
TARGET_DEC       float64
SUBPRIORITY      float64
TARGETID         int64
PETAL_LOC        int16
DEVICE_LOC       int32
LOCATION         int64
DESIGN_Q         float32
DESIGN_S         float32
DESIGN_X         float32
DESIGN_Y         float32
FIBERSTATUS      int32
APFLUX15_G       float32
APFLUX15_IVAR_G  float32
APFLUX15_R       float32
APFLUX15_IVAR_R  float32
APFLUX15_Z       float32
APFLUX15_IVAR_Z  float32
APFLUX15_W1      float32
APFLUX15_IVAR_W1 float32
APFLUX15_W2      float32
APFLUX15_IVAR_W2 float32
================ ======= ===== ===========

Notes:

  * APFLUX values may be dropped in a future version

HDU4
----

EXTNAME = TARGETS

Target catalog row-matched to the FIBERASSIGN table entries.  Unassigned
fibers will have TARGETID=-1 here.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============= ==== =====================
KEY      Example Value Type Comment
======== ============= ==== =====================
NAXIS1   184           int  length of dimension 1
NAXIS2   5000          int  length of dimension 2
TNULL1   999999        int
TNULL3   999999        int
TNULL31  999999        int
TNULL32  999999        int
TNULL33  999999        int
TNULL34  999999        int
TNULL35  999999        int
TNULL36  999999        int
ENCODING ascii         str
SEED     1028862084    int
HPXNSIDE 64            int
HPXNEST  T             bool
======== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

================== ======= ===== ===========
Name               Type    Units Description
================== ======= ===== ===========
BRICKID            int32
BRICKNAME          char[8]
BRICK_OBJID        int32
RA                 float64
DEC                float64
FLUX_G             float32
FLUX_R             float32
FLUX_Z             float32
FLUX_W1            float32
FLUX_W2            float32
MW_TRANSMISSION_G  float32
MW_TRANSMISSION_R  float32
MW_TRANSMISSION_Z  float32
MW_TRANSMISSION_W1 float32
MW_TRANSMISSION_W2 float32
PSFDEPTH_G         float32
PSFDEPTH_R         float32
PSFDEPTH_Z         float32
GALDEPTH_G         float32
GALDEPTH_R         float32
GALDEPTH_Z         float32
PSFDEPTH_W1        float32
PSFDEPTH_W2        float32
SHAPEDEV_R         float32
SHAPEDEV_E1        float32
SHAPEDEV_E2        float32
SHAPEEXP_R         float32
SHAPEEXP_E1        float32
SHAPEEXP_E2        float32
SUBPRIORITY        float64
TARGETID           int64
DESI_TARGET        int64
BGS_TARGET         int64
MWS_TARGET         int64
HPXPIXEL           int64
OBSCONDITIONS      int64
================== ======= ===== ===========

Notes:

  * Future versions will include IVAR columns

HDU5
----

EXTNAME = POTENTIAL_ASSIGNMENTS

A list of targets that could have been assigned to each fiber.
Note that the same target could appear more than once if it is covered
by more than one fiber

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =====================
KEY    Example Value Type Comment
====== ============= ==== =====================
NAXIS1 16            int  
NAXIS2 52351         int  Number of targets covered by this tile
====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

======== ===== ===== ===========
Name     Type  Units Description
======== ===== ===== ===========
TARGETID int64       Unique Target ID
FIBER    int32       Fiber number on the spectrographs [0-4999]
LOCATION int32       1000*PETAL_LOC + DEVICE_LOC location on focal plane
======== ===== ===== ===========


Notes and Examples
==================

To do...