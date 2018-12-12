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
HDU0_  --                    IMAGE    Blank
HDU1_  FIBERASSIGN           BINTABLE Target assignments for each fiber
HDU2_  POTENTIAL             BINTABLE All targets that could have been assigned
HDU3_  SKYETC                 BINTABLE Sky assignments for sky monitor positioners
HDU4_  TARGETS               BINTABLE Target catalog row-matched to FIBERASSIGN table
HDU5_  GFA_TARGETS           BINTABLE Targets on GFAs (OPTIONAL)
====== ===================== ======== ===================

NOTE: this file describes what the 18.11 fiberassign output files currently are,
which are somewhat different from what we eventually intend them to be.
Key upcoming differences for consistency with ICS:

  * filenames tile_TILEID.fits -> tile-TILEID-FIELDNUM.fits (TBD)
  * reordering HDUs
  * rename HDU SKYETC -> SKY_MONITOR
  * rename HDU POTENTIAL -> POTENTIAL_ASSIGNMENTS

FITS Header Units
=================

HDU0
----

EXTNAME = (None)

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

Data: Blank Image

Note: None of these non-standard keywords are included yet in
fiberassign/0.10.3 in the 18.11 reference run.

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

Note: None of these non-standard keywords are included yet in
fiberassign/0.10.3 in the 18.11 reference run.

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

================================= =========== ============ ===========
Name                              Type        Units        Description
================================= =========== ============ ===========
FIBER                             int32                    Fiber ID on the CCDs [0-4999]
LOCATION                          int32                    Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
NUMTARGET                         int16                    Total number of targets that this positioner covered
PRIORITY                          int32                    Assignment priority; larger = higher priority
TARGETID                          int64                    Unique target ID
DESI_TARGET                       int64                    Dark survey + calibration targeting bits
BGS_TARGET                        int64                    Bright Galaxy Survey targeting bits
MWS_TARGET                        int64                    Milky Way Survey targeting bits
TARGET_RA                         float64     deg          Target Right Ascension [degrees]
TARGET_DEC                        float64     deg          Target declination [degrees]
DESIGN_X                          float32     mm           Expected CS5 X location on focal plane
DESIGN_Y                          float32     mm           Expected CS5 Y location on focal plane
BRICKNAME                         char[8]                  Imaging Surveys brick name
FIBERSTATUS                       int32                    Fiber status mask; 0=good
DESIGN_Q                          float32     deg          CS5 Q azimuthal coordinate
DESIGN_S                          float32     mm           CS5 S radial distance along curved focal surface
LAMBDA_REF                        float32     Angstrom     Wavelength at which targets should be centered on fibers
OBJTYPE                           char[3]                  SKY, OBJ, NON
PETAL_LOC                         int16                    Petal location [0-9]
DEVICE_LOC                        int32                    Device location on focal plane [0-523]
RELEASE                           int32                    Imaging release number
BRICKID                           int32                    Imaging Surveys brick ID
BRICK_OBJID                       int64                    Imaging surveys OBJID on that brick
MORPHTYPE                         char[4]                  Imaging surveys morphological type
TARGET_RA_IVAR                    float32     deg^-2       Inverse variance of TARGET_RA
TARGET_DEC_IVAR                   float32     deg^-2       Inverse variance of TARGET_DEC
DCHISQ                            float32[5]
FLUX_G                            float32     nanomaggies  Flux in g-band
FLUX_R                            float32     nanomaggies  Flux in r-band
FLUX_Z                            float32     nanomaggies  Flux in z-band
FLUX_W1                           float32     nanomaggies  Flux in WISE W1-band
FLUX_W2                           float32     nanomaggies  Flux in WISE W2-band
FLUX_IVAR_G                       float32                  Inverse variance of FLUX_G
FLUX_IVAR_R                       float32                  Inverse variance of FLUX_R
FLUX_IVAR_Z                       float32                  Inverse variance of FLUX_Z
FLUX_IVAR_W1                      float32                  Inverse variance of FLUX_W1
FLUX_IVAR_W2                      float32                  Inverse variance of FLUX_W2
MW_TRANSMISSION_G                 float32
MW_TRANSMISSION_R                 float32
MW_TRANSMISSION_Z                 float32
MW_TRANSMISSION_W1                float32
MW_TRANSMISSION_W2                float32
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
FIBERFLUX_G                       float32     nanomaggies  g-band object model flux for 1 arcsec seeing and 1.5 arcsec diameter fiber
FIBERFLUX_R                       float32     nanomaggies  r-band object model flux for 1 arcsec seeing and 1.5 arcsec diameter fiber
FIBERFLUX_Z                       float32     nanomaggies  z-band object model flux for 1 arcsec seeing and 1.5 arcsec diameter fiber
FIBERTOTFLUX_G                    float32     nanomaggies  like FIBERFLUX_G but including all objects overlapping this location
FIBERTOTFLUX_R                    float32     nanomaggies  like FIBERFLUX_R but including all objects overlapping this location
FIBERTOTFLUX_Z                    float32     nanomaggies  like FIBERFLUX_Z but including all objects overlapping this location
REF_ID                            int64                    Astrometric catalog reference ID (SOURCE_ID from GAIA)
GAIA_PHOT_G_MEAN_MAG              float32
GAIA_PHOT_G_MEAN_FLUX_OVER_ERROR  float32
GAIA_PHOT_BP_MEAN_MAG             float32
GAIA_PHOT_BP_MEAN_FLUX_OVER_ERROR float32
GAIA_PHOT_RP_MEAN_MAG             float32
GAIA_PHOT_RP_MEAN_FLUX_OVER_ERROR float32
GAIA_ASTROMETRIC_EXCESS_NOISE     float32
GAIA_DUPLICATED_SOURCE            logical
PARALLAX                          float32
PARALLAX_IVAR                     float32
PMRA                              float32     mas/yr       Proper motion in the RA direction (already including cosDec term)
PMRA_IVAR                         float32                  Inverse variance of PMRA
PMDEC                             float32     mas/yr       Proper motion in the dec direction
PMDEC_IVAR                        float32                  Inverse variance of PMDEC
BRIGHTSTARINBLOB                  logical
EBV                               float32
PHOTSYS                           char[1]
SUBPRIORITY                       float64                  Assignment subpriority [0-1]
HPXPIXEL                          int64
NUMOBS_MORE                       int32
OBSCONDITIONS                     int32
================================= =========== ============ ===========

Notes:

* DESIGN_X/Y are where fiber assignment thought the targets would
  be; this is non-authoritative and more detailed downstream code will have
  a refined answer for each actual observation of this tile.
* This table defines the *requested* fiber assignments.  See
  :doc:`fiberassign <../../DESI_SPECTRO_DATA/NIGHT/EXPID/fibermap-EXPID>` for the
  actual observed assignments.

HDU2
----

EXTNAME = POTENTIAL

A list of targets that could have been assigned to each fiber.
Note that the same target could appear more than once if it is covered
by more than one fiber

Note: to be renamed "POTENTIAL_ASSIGNMENTS"

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

HDU3
----

EXTNAME = SKYETC

Blank sky assignments for sky monitor positioners.

Note: to be renamed "SKY_MONITOR"

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

============= ======= ===== ===================
Name          Type    Units Description
============= ======= ===== ===================
FIBER         int32         
LOCATION      int32         
NUMTARGET     int16         
PRIORITY      int32         
TARGETID      int64         
DESI_TARGET   int64         
BGS_TARGET    int64         
MWS_TARGET    int64         
RA            float64       
DEC           float64       
XFOCAL_DESIGN float32       
YFOCAL_DESIGN float32       
BRICKNAME     char[8]       
FIBERMASK     int32         
============= ======= ===== ===================

Notes:

  * This may be expanded to include aperture fluxes like
    `FIBERTOTFLUX_G/R/Z`.

HDU4
----

EXTNAME = TARGETS

Target catalog row-matched to the FIBERASSIGN table entries.  Unassigned
fibers will have TARGETID=-1 here.

Note: we are considering deprecating this HDU and merging all additional
columns into the FIBERASSIGN HDU.

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


================================= ========== ===== ===================
Name                              Type       Units Description
================================= ========== ===== ===================
TARGETID                          int64            
RELEASE                           int32            
BRICKID                           int32            
BRICKNAME                         char[8]          
BRICK_OBJID                       int32            
MORPHTYPE                         char[4]          
RA                                float64          
DEC                               float64          
RA_IVAR                           float32          
DEC_IVAR                          float32          
DCHISQ                            float32[5]       
FLUX_G                            float32          
FLUX_R                            float32          
FLUX_Z                            float32          
FLUX_W1                           float32          
FLUX_W2                           float32          
FLUX_IVAR_G                       float32          
FLUX_IVAR_R                       float32          
FLUX_IVAR_Z                       float32          
FLUX_IVAR_W1                      float32          
FLUX_IVAR_W2                      float32          
MW_TRANSMISSION_G                 float32          
MW_TRANSMISSION_R                 float32          
MW_TRANSMISSION_Z                 float32          
MW_TRANSMISSION_W1                float32          
MW_TRANSMISSION_W2                float32          
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
FIBERFLUX_G                       float32          
FIBERFLUX_R                       float32          
FIBERFLUX_Z                       float32          
FIBERTOTFLUX_G                    float32          
FIBERTOTFLUX_R                    float32          
FIBERTOTFLUX_Z                    float32          
REF_ID                            int64            
GAIA_PHOT_G_MEAN_MAG              float32          
GAIA_PHOT_G_MEAN_FLUX_OVER_ERROR  float32          
GAIA_PHOT_BP_MEAN_MAG             float32          
GAIA_PHOT_BP_MEAN_FLUX_OVER_ERROR float32          
GAIA_PHOT_RP_MEAN_MAG             float32          
GAIA_PHOT_RP_MEAN_FLUX_OVER_ERROR float32          
GAIA_ASTROMETRIC_EXCESS_NOISE     float32          
GAIA_DUPLICATED_SOURCE            logical          
PARALLAX                          float32          
PARALLAX_IVAR                     float32          
PMRA                              float32          
PMRA_IVAR                         float32          
PMDEC                             float32          
PMDEC_IVAR                        float32          
BRIGHTSTARINBLOB                  logical          
EBV                               float32          
PHOTSYS                           char[1]          
DESI_TARGET                       int64            
BGS_TARGET                        int64            
MWS_TARGET                        int64            
SUBPRIORITY                       float64          
HPXPIXEL                          int64            
NUMOBS_MORE                       int32            
PRIORITY                          int64            
OBSCONDITIONS                     int32            
================================= ========== ===== ===================

TODO: fill in units and descriptions

HDU5
----

EXTNAME = GFA_TARGETS

Table of objects that are on each GFA, including both point and extended sources.

Note: this HDU is optional for simulations and not included in the 18.11
reference run.

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


Notes and Examples
==================

To do...
