========================
cframe-CAMERA-EXPID.fits
========================

:Summary: This holds the calibrated spectra for a given camera and exposure.
    See the datamodel for :doc:`frame-CAMERA-EXPID <frame-CAMERA-EXPID>`
    files for details of the format.
:Naming Convention: ``cframe-{CAMERA}-{EXPID}.fits``, where ``{CAMERA}`` is
    one of the spectrograph cameras (*e.g.* ``z1``) and ``{EXPID}``
    is the 8-digit exposure ID.
:Regex: ``cframe-[brz][0-9]-[0-9]{8}\.fits``
:File Type: FITS, 86 MB

Contents
========

====== ========== ======== ===================
Number EXTNAME    Type     Contents
====== ========== ======== ===================
HDU0_  FLUX       IMAGE    Flux, erg/s/cm2/A
HDU1_  IVAR       IMAGE    Inverse variance, ``(erg/s/cm2/A)^-2``
HDU2_  MASK       IMAGE    Mask (0 = good)
HDU3_  WAVELENGTH IMAGE    wavelength in Angstrom
HDU4_  RESOLUTION IMAGE    Resolution Matrix
HDU5_  FIBERMAP   BINTABLE Fibermap
HDU6_  CHI2PIX    IMAGE    chi2 fit of PSF model to CCD image
HDU7_  SCORES     BINTABLE Quality Assurance scores
====== ========== ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = FLUX

Calibrated spectral flux in 1e-17 erg / (s cm2 Angstrom).

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============================ ===== ==============================================
KEY      Example Value                Type  Comment
======== ============================ ===== ==============================================
NAXIS1   2999                         int
NAXIS2   500                          int
NIGHT    20200316                     str   Night of observation YEARMMDD
EXPID    20                           int   DESI exposure ID
TILEID   11108                        int   DESI tile ID
PROGRAM  DARK                         str   program [dark, bright, ...]
FLAVOR   science                      str   Flavor [arc, flat, science, zero, ...]
TELRA    150.87                       float Telescope pointing RA [degrees]
TELDEC   31.23                        float Telescope pointing dec [degrees]
AIRMASS  1.307154717878038            float Airmass at middle of exposure
EXPTIME  1142.541228573218            float Exposure time [sec]
SEEING   0.7572662830352783           float Seeing FWHM [arcsec]
MOONFRAC 0.4083473802955095           float Moon illumination fraction 0-1; 1=full
MOONALT  -79.39563600071901           float Moon altitude [degrees]
MOONSEP  131.2947533254612            float Moon:tile separation angle [degrees]
DATE-OBS 2020-03-17T02:42:47.160      str   Start of exposure
MJD      58924.37858796309            float
SNR2FRAC 0.501188337802887            float
TRANSP   0.9980747699737549           float
SKY      1.0                          float
RA       150.73                       float
DEC      30.52                        float
PASS     1                            int
DOSVER   SIM                          str
FEEVER   SIM                          str
BUNIT    10**-17 erg/(s cm2 Angstrom) str
AIRORVAC vac                          str   Vacuum wavelengths
CAMERA   z1                           str
FIBERMIN 500                          int
CHECKSUM 1HdW1GZU1GbU1GZU             str   HDU checksum updated 2018-03-01T15:04:16
DATASUM  4250999040                   str   data unit checksum updated 2018-03-01T15:04:16
======== ============================ ===== ==============================================

Data: FITS image [float32, 2999x500]

HDU1
----

EXTNAME = IVAR

Inverse variance of flux (i.e. 1/error^2).

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2999             int
NAXIS2   500              int
CHECKSUM IY2iIX2iIX2iIX2i str  HDU checksum updated 2018-03-01T15:08:14
DATASUM  2728612709       str  data unit checksum updated 2018-03-01T15:08:14
======== ================ ==== ==============================================

Data: FITS image [float32, 2999x500]

HDU2
----

EXTNAME = MASK

Mask of spectra; 0=good.

Prior to desispec/0.24.0 and software release 18.9, the MASK HDU was compressed.

TODO: add documentation link to what bits mean what.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2999             int  length of original image axis
NAXIS2   500              int  length of original image axis
BSCALE   1                int
BZERO    2147483648       int
CHECKSUM odSnqZPlodPloZPl str  HDU checksum updated 2018-03-01T15:08:14
DATASUM  749750           str  data unit checksum updated 2018-03-01T15:08:14
======== ================ ==== ==============================================

Data: FITS image [int32, 2999x500]

HDU3
----

EXTNAME = WAVELENGTH

Wavelengths at which flux is measured.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2999             int
BUNIT    Angstrom         str
CHECKSUM iUcmiUajiUajiUaj str  HDU checksum updated 2018-03-01T15:08:14
DATASUM  4144667411       str  data unit checksum updated 2018-03-01T15:08:14
======== ================ ==== ==============================================

Data: FITS image [float64, 2999]

HDU4
----

EXTNAME = RESOLUTION

Diagonal elements of convolution matrix describing spectral resolution.

TODO: add code example for using this.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2999             int
NAXIS2   13               int
NAXIS3   500              int
CHECKSUM bALae7JXbAJab5JU str  HDU checksum updated 2018-03-01T15:08:15
DATASUM  1034366580       str  data unit checksum updated 2018-03-01T15:08:15
======== ================ ==== ==============================================

Data: FITS image [float32, 2999x13x500]

HDU5
----

EXTNAME = FIBERMAP

Fibermap of what targets were assigned to what fibers.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   378              int  length of dimension 1
NAXIS2   500              int  length of dimension 2
ENCODING ascii            str
CHECKSUM UUVAVUS8UUSAUUS5 str  HDU checksum updated 2018-03-01T15:08:15
DATASUM  4154192770       str  data unit checksum updated 2018-03-01T15:08:15
======== ================ ==== ==============================================

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
================================= ======= ===== ===========

HDU6
----

EXTNAME = CHI2PIX

chi2 of PSF fit to CCD data per flux bin.  Large values indicate poor fits,
e.g. due to unmasked cosmics or other CCD defects.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2751             int  Number of wavelengths
NAXIS2   500              int  Number of spectra
CHECKSUM jcVelZSejbSejZSe str  HDU checksum updated 2020-04-27T21:02:01
DATASUM  2095353275       str  data unit checksum updated 2020-04-27T21:02:01
======== ================ ==== ==============================================

Data: FITS image [float32, 2751x500]

HDU7
----

EXTNAME = SCORES

Scores / metrics measured from the spectra for use in QA and systematics
studies.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   96               int  length of dimension 1
NAXIS2   500              int  length of dimension 2
ENCODING ascii            str
CHECKSUM eQiCeOZ9eOfCeOZ9 str  HDU checksum updated 2018-03-01T15:08:15
DATASUM  2282282789       str  data unit checksum updated 2018-03-01T15:08:15
======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Note: the ``_C`` in the column names refers to the camera for this particular
frame, e.g. ``_B``, ``_R``, or ``_Z``.  These are designed such that the
SCORES tables from individual frames can be later combined into a summary
table for the exposure.

TODO: document wavelength ranges covered per camera.

===================== ======= ===== ============================================
Name                  Type    Units Description
===================== ======= ===== ============================================
SUM_RAW_COUNT_C       float64       sum counts
MEDIAN_RAW_COUNT_C    float64       median counts/A
MEDIAN_RAW_SNR_C      float64       median SNR/sqrt(A)
SUM_FFLAT_COUNT_C     float64       sum counts
MEDIAN_FFLAT_COUNT_C  float64       median counts/A
MEDIAN_FFLAT_SNR_C    float64       median SNR/sqrt(A)
SUM_SKYSUB_COUNT_C    float64       sum counts
MEDIAN_SKYSUB_COUNT_C float64       median counts/A
MEDIAN_SKYSUB_SNR_C   float64       median SNR/sqrt(A)
SUM_CALIB_COUNT_C     float64       sum counts
MEDIAN_CALIB_COUNT_C  float64       median counts/A
MEDIAN_CALIB_SNR_C    float64       median SNR/sqrt(A)
===================== ======= ===== ============================================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
