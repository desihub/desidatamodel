=============
full
=============

:Summary: Merge catalog (with duplicates), clean after vetomasks. Parent catalog
          for clustering catalog
:Naming Convention: ``{target}_full.dat.fits``, where ``{target}`` is
                    the target type (LRG, ELG...) 
:Regex: ``[a-zA-Z]_full\.dat\.fits``
:File Type: FITS, 114 MB  *This section gives the type of the file
    and its approximate size.*


Contents
========

====== ======= ======== =================================
Number EXTNAME Type     Contents
====== ======= ======== =================================
HDU0_  PRIMARY IMAGE    *PrimaryHDU with array data type*
HDU1_  LSS     BINTABLE *Complete catalog after veto*
====== ======= ======== =================================


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

*Full catalog of targets ID (with duplicates) after vetomask*


Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =======================
KEY    Example Value Type Comment
====== ============= ==== =======================
NAXIS1 905           int  width of table in bytes
NAXIS2 133200        int  number of rows in table
====== ============= ==== =======================


Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

========================== =========== ===== ======================================
Name                       Type        Units Description
========================== =========== ===== ======================================
RA                         float64     deg   Right Ascension
DEC                        float64     deg   Declination
TARGETID                   int64             Unique Target ID
SV3_DESI_TARGET            int64             Target Type
SV3_BGS_TARGET             int64             Target Type if BGS
SV3_MWS_TARGET             int64             Target Type if MW
PRIORITY_INIT              int64             Initial priority
TARGET_STATE               char[]            Target state
TIMESTAMP                  char[]            Process Timestamp
ZWARN_MTL                  int64             Z warnings in MTL
LOCATION                   int64             Fiber Location
TILEID                     int64             Unique TILE ID
TILELOCID                  int64             Unique TILE-Location ID
Z_not4clus                 float64           Redshift (do not use if blind)
ZERR                       float64           Error in Redshift
ZWARN                      int64             Redshift Warnings
CHI2                       float64           Chi2 of SED fitting
COEFF                      float64[10]       Coefficient
NPIXELS                    int64             N pixels
SPECTYPE                   char[]            Spectral type in fit
SUBTYPE                    char[]            Spec Sub-type
NCOEFF                     int64             N Coefficients
DELTACHI2                  float64           Delta Chi2
FIBER                      int32             Fiber ID
COADD_FIBERSTATUS          int32             Fiber status
FIBERASSIGN_X              float32           Fiber position, x
FIBERASSIGN_Y              float32           Fiber position, y
COADD_NUMEXP               int16             Number of exposures
COADD_EXPTIME              float32           Exposure time
COADD_NUMNIGHT             int16             Numnight ID
MEAN_DELTA_X               float32           Delta x target
RMS_DELTA_X                float32           RMS in Delta x
MEAN_DELTA_Y               float32           Delta y target
RMS_DELTA_Y                float32           RMS in Delta y
MEAN_PSF_TO_FIBER_SPECFLUX float32           Template info
TSNR2_ELG_B                float32           Template info
TSNR2_LYA_B                float32           Template info
TSNR2_BGS_B                float32           Template info
TSNR2_QSO_B                float32           Template info
TSNR2_LRG_B                float32           Template info
TSNR2_ELG_R                float32           Template info
TSNR2_LYA_R                float32           Template info
TSNR2_BGS_R                float32           Template info
TSNR2_QSO_R                float32           Template info
TSNR2_LRG_R                float32           Template info
TSNR2_ELG_Z                float32           Template info
TSNR2_LYA_Z                float32           Template info
TSNR2_BGS_Z                float32           Template info
TSNR2_QSO_Z                float32           Template info
TSNR2_LRG_Z                float32           Template info
TSNR2_ELG                  float32           Template info
TSNR2_LYA                  float32           Template info
TSNR2_BGS                  float32           Template info
TSNR2_QSO                  float32           Template info
TSNR2_LRG                  float32           Template info
GOODHARDLOC                logical           Hardware location status
RELEASE                    int16             Release
BRICKID                    int32             Brick ID
BRICKNAME                  char[]            Brick name
BRICK_OBJID                int32             ID Of object in Brick
MORPHTYPE                  char[]            Phot Morph type
EBV                        float32           Extinction E(B-V)
FLUX_G                     float32           Flux in G [AB]
FLUX_R                     float32           Flux in R [AB]
FLUX_Z                     float32           Flux in Z [AB]
FLUX_IVAR_G                float32           Variance in FLUX_G
FLUX_IVAR_R                float32           Variance in FLUX_R
FLUX_IVAR_Z                float32           Variance in FLUX_Z
MW_TRANSMISSION_G          float32           MW transmission in G
MW_TRANSMISSION_R          float32           MW transmission in R
MW_TRANSMISSION_Z          float32           MW transmission in Z
FRACFLUX_G                 float32           Fraction Flux G
FRACFLUX_R                 float32           Fraction Flux R
FRACFLUX_Z                 float32           Fraction Flux Z
FRACMASKED_G               float32           Masked fraction G
FRACMASKED_R               float32           Masked fraction R
FRACMASKED_Z               float32           Masked fraction Z
FRACIN_G                   float32           Fraction inside G
FRACIN_R                   float32           Fraction inside R
FRACIN_Z                   float32           Fraction inside Z
NOBS_G                     int16             Number obs in G
NOBS_R                     int16             Number obs in R
NOBS_Z                     int16             Number obs in Z
PSFDEPTH_G                 float32           Estimated PSF depth G
PSFDEPTH_R                 float32           Estimated PSF depth R
PSFDEPTH_Z                 float32           Estimated PSF depth Z
GALDEPTH_G                 float32           Estimated Model depth G
GALDEPTH_R                 float32           Estimated Model depth R
GALDEPTH_Z                 float32           Estimated Model depth Z
FLUX_W1                    float32           Flux in WISE-W1 [AB]
FLUX_W2                    float32           Flux in WISE-W2 [AB]
FLUX_IVAR_W1               float32           Variance in FLUX_W1
FLUX_IVAR_W2               float32           Variance in FLUX_W2
MW_TRANSMISSION_W1         float32           MW transmission in W1
MW_TRANSMISSION_W2         float32           MW transmission in W2
ALLMASK_G                  int16             All Mask G
ALLMASK_R                  int16             All Mask R
ALLMASK_Z                  int16             All Mask Z
FIBERFLUX_G                float32           Fiber Flux in G
FIBERFLUX_R                float32           Fiber Flux in R
FIBERFLUX_Z                float32           Fiber Flux in Z
FIBERTOTFLUX_G             float32           Fiber-to-flux G
FIBERTOTFLUX_R             float32           Fiber-to-flux R
FIBERTOTFLUX_Z             float32           Fiber-to-flux Z
WISEMASK_W1                binary            WISE MASK bit W1
WISEMASK_W2                binary            WISE MASK bit W2
MASKBITS                   int16             DESI maskbits
SHAPE_R                    float32           Shape parameter
PHOTSYS                    char[1]           If North or South
NTILE                      int64             Number of tiles
TILES                      char[]            List of tiles observed, separated by -
TILELOCIDS                 char[]            TILELOC IDs, separated by -
LOCATION_ASSIGNED          logical           Location assigned in FA
TILELOCID_ASSIGNED         int64             Tile Loc ID assigned in FA
sort                       float64           Sorted number
COMP_TILE                  float64           Completeness in Tile
rosette_number             float64           Rosette number
rosette_r                  float64           Distance to rosette center
FRACZ_TILELOCID            float64           Fraction Tile Loc IDs
BITWEIGHTS                 int64[2]          PIP Bitwise bits
PROB_OBS                   float64           Probability of being observed AltMTL
lrg_mask                   binary            If within LRG mask
========================== =========== ===== ======================================


Notes and Examples
==================

