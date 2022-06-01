===============
full_random
===============

:Summary: Random merge catalog (with duplicates), clean after vetomasks. Parent catalog
          for clustering random catalog
:Naming Convention: ``{target}_{RANNUM}_full.ran.fits``, where ``{target}`` is
                    the target type (LRG, ELG...) and ``{RANNUM}`` is the random number
:Regex: ``[a-zA-Z]_[0-9]_full\.ran\.fits``
:File Type: FITS, 653 MB


Contents
========

====== ======== ======== ==========================================
Number EXTNAME  Type     Contents
====== ======== ======== ==========================================
HDU0_  PRIMARY  IMAGE    *PrimaryHDU with array data type*
HDU1_  LSS      BINTABLE *Random Full catalog prior to clustering*
====== ======== ======== ==========================================


FITS Header Units
=================

HDU0
----

*Primary HDU conforms to FITS standard*

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = LSS

*Full catalog of randoms (with duplicates) after vetomask*


Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =======================
KEY    Example Value Type Comment
====== ============= ==== =======================
NAXIS1 543           int  width of table in bytes
NAXIS2 417645        int  number of rows in table
====== ============= ==== =======================


Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

========================== ========= ===== ======================================
Name                       Type      Units Description
========================== ========= ===== ======================================
LOCATION                   int64           Fiber Location
FIBER                      int32           Fiber ID
TARGETID                   int64           Unique Target ID
RA                         float64   deg   Right Ascension
DEC                        float64   deg   Declination
TILEID                     int64           Unique TILE ID
ZWARN                      int64           Redshift warnings
COADD_FIBERSTATUS          int32           Fiber status
FIBERASSIGN_X              float32         Fiber position, x
FIBERASSIGN_Y              float32         Fiber position, y
PRIORITY                   int32           Priority on target
COADD_NUMEXP               int16           Number of exposures
COADD_EXPTIME              float32         Exposure time
COADD_NUMNIGHT             int16           Numnight ID
MEAN_DELTA_X               float32         Delta x target
RMS_DELTA_X                float32         RMS in Delta x
MEAN_DELTA_Y               float32         Delta y target
RMS_DELTA_Y                float32         RMS in Delta y
MEAN_PSF_TO_FIBER_SPECFLUX float32         Target info
TSNR2_ELG_B                float32         Template info
TSNR2_LYA_B                float32         Template info
TSNR2_BGS_B                float32         Template info
TSNR2_QSO_B                float32         Template info
TSNR2_LRG_B                float32         Template info
TSNR2_ELG_R                float32         Template info
TSNR2_LYA_R                float32         Template info
TSNR2_BGS_R                float32         Template info
TSNR2_QSO_R                float32         Template info
TSNR2_LRG_R                float32         Template info
TSNR2_ELG_Z                float32         Template info
TSNR2_LYA_Z                float32         Template info
TSNR2_BGS_Z                float32         Template info
TSNR2_QSO_Z                float32         Template info
TSNR2_LRG_Z                float32         Template info
TSNR2_ELG                  float32         Template info
TSNR2_LYA                  float32         Template info
TSNR2_BGS                  float32         Template info
TSNR2_QSO                  float32         Template info
TSNR2_LRG                  float32         Template info
TILELOCID                  int64           Unique TILE-Location ID
GOODHARDLOC                logical         If good Hardware
ZPOSSLOC                   logical         If good redshift
NTILE                      int64           Number of tiles
TILES                      char[]          List of tiles observed, separated by -
TILELOCIDS                 char[]          TILELOC IDs, separated by -
RELEASE                    int16           Release
BRICKID                    int32           Brick ID
BRICKNAME                  char[]          Brick Name
BRICK_OBJID                int32           Object ID at Brick
NOBS_G                     int16           Number obs in G
NOBS_R                     int16           Number obs in R
NOBS_Z                     int16           Number obs in Z
PSFDEPTH_G                 float32         Estimated PSF depth G
PSFDEPTH_R                 float32         Estimated PSF depth R
PSFDEPTH_Z                 float32         Estimated PSF depth Z
GALDEPTH_G                 float32         Estimated Model depth G
GALDEPTH_R                 float32         Estimated Model depth R
GALDEPTH_Z                 float32         Estimated Model depth Z
PSFDEPTH_W1                float32         Estimated PSF depth W1
PSFDEPTH_W2                float32         Estimated PSF depth W2
PSFSIZE_G                  float32         Size PSF G
PSFSIZE_R                  float32         Size PSF R
PSFSIZE_Z                  float32         Size PSF Z
APFLUX_G                   float32         Aperture Flux G
APFLUX_R                   float32         Aperture Flux R
APFLUX_Z                   float32         Aperture Flux Z
APFLUX_IVAR_G              float32         Error in Aperture Flux G
APFLUX_IVAR_R              float32         Error in Aperture Flux R
APFLUX_IVAR_Z              float32         Error in Aperture Flux Z
MASKBITS                   int16           DESI maskbits
WISEMASK_W1                binary          If in WISE W1 mask
WISEMASK_W2                binary          If in WISE W2 mask
EBV                        float32         Extinction E(B-V)
PHOTSYS                    char[1]         If North or South
HPXPIXEL                   int64           Healpix pixel ID
GOODPRI                    logical         If Good priority
sort                       float32         Array for sorting
rosette_number             int64           Rosette number
rosette_r                  float64         Distance to rosette center
COMP_TILE                  float64         Completeness in Tile
lrg_mask                   binary          If within LRG mask
========================== ========= ===== ======================================


Notes and Examples
==================

