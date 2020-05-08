=======================
zbest-NSIDE-PIXNUM.fits
=======================

:Summary: Best fit redshifts for each targets in a spectra file.
:Naming Convention: ``zbest-NSIDE-PIXNUM.fits``, where NSIDE is the healpix
    Nside (typically 64) and PIXNUM is the nested scheme healpix number.
:Regex: ``zbest-[0-9]+-[0-9]+\.fits``
:File Type: FITS, 1 MB

Note: the corresponding spectra file in this directory has one entry per
exposure of each target, while this zbest file has one entry per target,
thus it can have a different number of entries and is not row-matched to
the spectra file.

Contents
========

====== ======== ======== =============================
Number EXTNAME  Type     Contents
====== ======== ======== =============================
HDU0_  PRIMARY  IMAGE    Blank HDU
HDU1_  ZBEST    BINTABLE Table with best fit redshifts
HDU2_  FIBERMAP BINTABLE Propagated fibermap file data.
====== ======== ======== =============================


FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============= ==== ===============
KEY      Example Value Type Comment
======== ============= ==== ===============
RRVER    0.13.2        str  Redrock version
TEMNAM00 GALAXY        str
TEMVER00 2.6           str
TEMNAM01 QSO           str
TEMVER01 unknown       str
TEMNAM02 STAR:::A      str
TEMVER02 unknown       str
TEMNAM03 STAR:::B      str
TEMVER03 unknown       str
TEMNAM04 STAR:::CV     str
TEMVER04 unknown       str
TEMNAM05 STAR:::F      str
TEMVER05 unknown       str
TEMNAM06 STAR:::G      str
TEMVER06 unknown       str
TEMNAM07 STAR:::K      str
TEMVER07 unknown       str
TEMNAM08 STAR:::M      str
TEMVER08 unknown       str
TEMNAM09 STAR:::WD     str
TEMVER09 unknown       str
======== ============= ==== ===============

Empty HDU.

HDU1
----

EXTNAME = ZBEST

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ============= ==== ===================================
KEY     Example Value Type Comment
======= ============= ==== ===================================
NAXIS1  143           int  width of table in bytes
NAXIS2  1165          int  number of rows in table
======= ============= ==== ===================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

========= =========== ===== =============================================
Name      Type        Units Description
========= =========== ===== =============================================
TARGETID  int64             Target ID for this row
CHI2      float64           Best fit chi2
COEFF     float64[10]       Redrock template coefficients
Z         float64           Best fit redshift
ZERR      float64           Uncertainty on best fit redshift
ZWARN     int64             Warning flags; 0 is good
NPIXELS   int64
SPECTYPE  char[6]           Spectral type
SUBTYPE   char[6]           Spectral subtype (maybe blank)
NCOEFF    int64
DELTACHI2 float64           Delta(chi2) to next best fit
NUMEXP    int32
NUMTILE   int32
========= =========== ===== =============================================

HDU2
----

EXTNAME = FIBERMAP

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ============= ==== ===================================
KEY     Example Value Type Comment
======= ============= ==== ===================================
NAXIS1  390           int  width of table in bytes
NAXIS2  3526          int  number of rows in table
======= ============= ==== ===================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

================================= ======= ===== ===========
Name                              Type    Units Description
================================= ======= ===== ===========
TARGETID                          int64         Unique target ID
PETAL_LOC                         int16         Focal plane petal location 0-9
DEVICE_LOC                        int32         Device location 0-5xx
LOCATION                          int64         1000*PETAL_LOC + DEVICE_LOC
FIBER                             int32         Fiber number 0-4999
FIBERSTATUS                       int32         Fiber status mask; 0=good
TARGET_RA                         float64
TARGET_DEC                        float64
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
TARGET_RA_IVAR                    float32
TARGET_DEC_IVAR                   float32
EBV                               float32
FLUX_G                            float32
FLUX_R                            float32
FLUX_Z                            float32
FLUX_IVAR_G                       float32
FLUX_IVAR_R                       float32
FLUX_IVAR_Z                       float32
MW_TRANSMISSION_G                 float32
MW_TRANSMISSION_R                 float32
MW_TRANSMISSION_Z                 float32
FRACFLUX_G                        float32
FRACFLUX_R                        float32
FRACFLUX_Z                        float32
FRACMASKED_G                      float32
FRACMASKED_R                      float32
FRACMASKED_Z                      float32
FRACIN_G                          float32
FRACIN_R                          float32
FRACIN_Z                          float32
NOBS_G                            int16
NOBS_R                            int16
NOBS_Z                            int16
PSFDEPTH_G                        float32
PSFDEPTH_R                        float32
PSFDEPTH_Z                        float32
GALDEPTH_G                        float32
GALDEPTH_R                        float32
GALDEPTH_Z                        float32
FLUX_W1                           float32
FLUX_W2                           float32
FLUX_W3                           float32
FLUX_W4                           float32
FLUX_IVAR_W1                      float32
FLUX_IVAR_W2                      float32
FLUX_IVAR_W3                      float32
FLUX_IVAR_W4                      float32
MW_TRANSMISSION_W1                float32
MW_TRANSMISSION_W2                float32
MW_TRANSMISSION_W3                float32
MW_TRANSMISSION_W4                float32
ALLMASK_G                         int16
ALLMASK_R                         int16
ALLMASK_Z                         int16
FIBERFLUX_G                       float32
FIBERFLUX_R                       float32
FIBERFLUX_Z                       float32
FIBERTOTFLUX_G                    float32
FIBERTOTFLUX_R                    float32
FIBERTOTFLUX_Z                    float32
WISEMASK_W1                       binary
WISEMASK_W2                       binary
MASKBITS                          int16
FRACDEV                           float32
FRACDEV_IVAR                      float32
SHAPEDEV_R                        float32
SHAPEDEV_E1                       float32
SHAPEDEV_E2                       float32
SHAPEDEV_R_IVAR                   float32
SHAPEDEV_E1_IVAR                  float32
SHAPEDEV_E2_IVAR                  float32
SHAPEEXP_R                        float32
SHAPEEXP_E1                       float32
SHAPEEXP_E2                       float32
SHAPEEXP_R_IVAR                   float32
SHAPEEXP_E1_IVAR                  float32
SHAPEEXP_E2_IVAR                  float32
REF_ID                            int64
REF_CAT                           char[2]
GAIA_PHOT_G_MEAN_MAG              float32
GAIA_PHOT_G_MEAN_FLUX_OVER_ERROR  float32
GAIA_PHOT_BP_MEAN_MAG             float32
GAIA_PHOT_BP_MEAN_FLUX_OVER_ERROR float32
GAIA_PHOT_RP_MEAN_MAG             float32
GAIA_PHOT_RP_MEAN_FLUX_OVER_ERROR float32
GAIA_PHOT_BP_RP_EXCESS_FACTOR     float32
GAIA_ASTROMETRIC_EXCESS_NOISE     float32
GAIA_DUPLICATED_SOURCE            logical
GAIA_ASTROMETRIC_SIGMA5D_MAX      float32
GAIA_ASTROMETRIC_PARAMS_SOLVED    logical
PARALLAX                          float32
PARALLAX_IVAR                     float32
PHOTSYS                           char[1]
CMX_TARGET                        int64
PRIORITY_INIT                     int64
NUMOBS_INIT                       int64
HPXPIXEL                          int64
BLOBDIST                          float32
FIBERFLUX_IVAR_G                  float32
FIBERFLUX_IVAR_R                  float32
FIBERFLUX_IVAR_Z                  float32
DESI_TARGET                       int64
BGS_TARGET                        int64
MWS_TARGET                        int64
NUM_ITER                          int64
FIBER_X                           float64
FIBER_Y                           float64
DELTA_X                           float64
DELTA_Y                           float64
FIBER_RA                          float64
FIBER_DEC                         float64
NIGHT                             int32         YEARMMDD of sunset
EXPID                             int32         exposure ID
MJD                               float64
TILEID                            int32         tile ID
================================= ======= ===== ===========


Upcoming Changes
================

The following changes are not yet in the zbest files, but will be added in
the future:

* Coadded signal-to-noise per band
