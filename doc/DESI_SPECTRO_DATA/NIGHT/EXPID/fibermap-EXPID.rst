===================
fibermap-EXPID.fits
===================

:Summary: The fibermap contains the fiber positioner configuration information for
    each exposure: what fiber is placed where, what target that is, etc.
:Naming Convention: ``fibermap-{EXPID}.fits``, where {EXPID} is the 8-digit exposure ID.
:Regex: ``fibermap-[0-9]{8}\.fits``
:File Type: FITS, 2 MB

This table is also propagated forward to the
:doc:`frame <../../../DESI_SPECTRO_REDUX/SPECPROD/exposures/NIGHT/EXPID/frame-CAMERA-EXPID>`,
:doc:`cframe <../../../DESI_SPECTRO_REDUX/SPECPROD/exposures/NIGHT/EXPID/cframe-CAMERA-EXPID>`, and
:doc:`spectra <../../../DESI_SPECTRO_REDUX/SPECPROD/healpix/SURVEY/PROGRAM/PIXGROUP/PIXNUM/spectra-SURVEY-PROGRAM-PIXNUM>`
files.

Contents
========

====== ======== ======== ===================
Number EXTNAME  Type     Contents
====== ======== ======== ===================
HDU0_  PRIMARY  IMAGE    Blank
HDU1_  FIBERMAP BINTABLE Fiber map table of what targets are on what fibers
HDU2_  TARGETS  BINTABLE Row matched target catalog for those assignments
====== ======== ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

Empty HDU.

This HDU has no non-standard required keywords.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================= ===== ========================================
KEY      Example Value     Type  Comment
======== ================= ===== ========================================
NAXIS1   0                 int
TILEID   1165              int
REQRA    150.69            float
REQDEC   33.86             float
TILERA   150.69            float
TILEDEC  33.86             float
REFEPOCH 2015.5            str
NIGHT    20201010          int
EXPID    123456            int
FLAVOR   science           str
FIELDNUM 0                 int   Field configuration number for this tile
TELRA    150.6899871709776 float
TELDEC   150.6899913445232 float
======== ================= ===== ========================================

Data: FITS image [float64, 0]

HDU1
----

EXTNAME = FIBERMAP

The fiber map table of which targets where placed on which fibers
at which locations.  This is a superset of the requested fiberassignments,
augmented with columns describing where the fibers actually ended up.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================= ===== =======================================
KEY      Example Value           Type  Comment
======== ======================= ===== =======================================
NAXIS1   378                     int   length of dimension 1
NAXIS2   5000                    int   length of dimension 2
NIGHT    20170327                str   YEARMMDD of sunset for this night
EXPID    2                       int   unique DESI exposure ID
TILEID   4                       int   DESI tile ID
PROGRAM  DARK                    str   program [dark, bright, gray, calib, ...]
FLAVOR   science                 str   Flavor [arc, flat, science, zero, ...]
REQRA    335.03                  float Requested telescope RA [degrees]
REQDEC   19.88                   float Requested telescope dec [degrees]
REQRA    335.03                  float Requested telescope RA [degrees]
REQDEC   19.88                   float Requested telescope dec [degrees]
TELRA    335.03                  float Actual telescope pointing RA [degrees]
TELDEC   19.88                   float Actual telescope pointing dec [degrees]
AIRMASS  1.17754                 float Airmass at middle of exposure
EXPTIME  629.827                 float Exposure time [sec]
SEEING   0.7769                  float Seeing FWHM [arcsec]
MOONFRAC 0.4083                  float Moon illumination fraction 0-1; 1=full
MOONALT  -72.8225                float Moon altitude [degrees]
MOONSEP  131.1832                float Moon:tile separation angle [degrees]
DATE-OBS 2020-03-17T03:35:05.835 str   Start of exposure
======== ======================= ===== =======================================

TODO: standardize keywords with ICS, *e.g.* ``FLAVOR -> PROGRAM``.

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
TARGET_RA        float64 deg          Target Right Ascension [degrees]
TARGET_DEC       float64 deg          Target declination [degrees]
TARGET_RA_IVAR   float32 deg^-2       Inverse variance of TARGET_RA
TARGET_DEC_IVAR  float32 deg^-2       Inverse variance of TARGET_DEC
LAMBDA_REF       float32 Angstrom     Wavelength at which targets should be centered on fibers
DESIGN_X         float32 mm           Expected CS5 X location on focal plane
DESIGN_Y         float32 mm           Expected CS5 Y location on focal plane
DESIGN_Q         float32 deg          CS5 Q azimuthal coordinate
DESIGN_S         float32 mm           CS5 S radial distance along curved focal surface
BRICKID          int64                Imaging Surveys brick ID
BRICK_OBJID      int64                Imaging surveys OBJID on that brick
TYPE             char[4]              Imaging surveys morphological type
PRIORITY         int32                Assignment priority; larger = higher priority
SUBPRIORITY      float64              Assignment subpriority [0-1]
NUMTARGET        int16                Total number of targets that this positioner covered
REF_ID           int64                Astrometric catalog reference ID (SOURCE_ID from GAIA)
PMRA             float32 mas/yr       Proper motion in the RA direction (already including cosDec term)
PMDEC            float32 mas/yr       Proper motion in the dec direction
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
FIBER_RA         float64 deg          RA of actual fiber position
FIBER_DEC        float64 deg          DEC of actual fiber position
FIBER_RA_IVAR    float32 deg^-2       Inverse variance of FIBER_RA [not meaningful yet]
FIBER_DEC_IVAR   float32 deg^-2       Inverse variance of FIBER_DEC [not meaningful yet]
DELTA_X          float32 mm           CS5 x difference between requested and actual position
DELTA_Y          float32 mm           CS5 y difference between requested and actual position
DELTA_X_IVAR     float32 mm^-2        Inverse variance of DELTA_X [not meaningful yet]
DELTA_Y_IVAR     float32 mm^-2        Inverse variance of DELTA_Y [not meaningful yet]
NUM_ITER         int16                Number of positioner iterations
SPECTROID        int16                Hardware ID of spectrograph
================ ======= ============ ===========

HDU2
----

EXTNAME = TARGETS

Target catalog row-matched to the FIBERASSIGN table entries.  Unassigned
fibers will have TARGETID=-1 here.

Note: Software release 18.11 (desispec/0.26.0 desisim/0.31.0) does not include
this HDU.  In the future it will either be included or deprecated and removed.

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

Notes and Examples
==================

To do...
