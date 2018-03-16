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
HDU5_  FIBERMAP   BINTABLE Fibermap details propagated from :doc:`fibermap-EXPID.fits <../../../../../DESI_SPECTRO_DATA/NIGHT/fibermap-EXPID>`
HDU6_  SCORES     BINTABLE *Brief Description*
====== ========== ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = FLUX

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================= ===== ==============================================
KEY      Example Value           Type  Comment
======== ======================= ===== ==============================================
NAXIS1   2999                    int
NAXIS2   500                     int
NIGHT    20200316                str   Night of observation YEARMMDD
EXPID    20                      int   DESI exposure ID
TILEID   11108                   int   DESI tile ID
PROGRAM  DARK                    str   program [dark, bright, ...]
FLAVOR   science                 str   Flavor [arc, flat, science, zero, ...]
TELRA    150.87                  float Telescope pointing RA [degrees]
TELDEC   31.23                   float Telescope pointing dec [degrees]
AIRMASS  1.307154717878038       float Airmass at middle of exposure
EXPTIME  1142.541228573218       float Exposure time [sec]
SEEING   0.7572662830352783      float Seeing FWHM [arcsec]
MOONFRAC 0.4083473802955095      float Moon illumination fraction 0-1; 1=full
MOONALT  -79.39563600071901      float Moon altitude [degrees]
MOONSEP  131.2947533254612       float Moon:tile separation angle [degrees]
DATE-OBS 2020-03-17T02:42:47.160 str   Start of exposure
DEPNAM00 python                  str
DEPVER00 3.6.4                   str
DEPNAM01 numpy                   str
DEPVER01 1.13.3                  str
DEPNAM02 scipy                   str
DEPVER02 1.0.0                   str
DEPNAM03 astropy                 str
DEPVER03 1.3.3                   str
DEPNAM04 yaml                    str
DEPVER04 3.12                    str
DEPNAM05 matplotlib              str
DEPVER05 2.1.2                   str
DEPNAM06 fitsio                  str
DEPVER06 0.9.11                  str
DEPNAM07 healpy                  str
DEPVER07 1.11.0                  str
DEPNAM08 desiutil                str
DEPVER08 1.9.9                   str
DEPNAM09 desispec                str
DEPVER09 0.19.0                  str
DEPNAM10 desitarget              str
DEPVER10 0.19.1                  str
DEPNAM11 desimodel               str
DEPVER11 0.9.2                   str
DEPNAM12 desisim                 str
DEPVER12 0.26.0                  str
DEPNAM13 speclite                str
DEPVER13 0.7                     str
DEPNAM14 specsim                 str
DEPVER14 0.11                    str
PASS     1                       int
RA       150.87                  float
DEC      31.23                   float
EBMV     0.0189034678041935      float
MJD      58925.11304582807       float
TRANSPAR 0.7192993760108948      float
DOSVER   SIM                     str
FEEVER   SIM                     str
BUNIT    1e-17 erg/(s cm2 A)     str
AIRORVAC vac                     str   Vacuum wavelengths
CAMERA   z7                      str
FIBERMIN 3500                    int
CHECKSUM 9GKaD9HU9EHZC9HZ        str   HDU checksum updated 2018-03-01T15:08:14
DATASUM  1412099935              str   data unit checksum updated 2018-03-01T15:08:14
DEPNAM15 mpi4py                  str
DEPVER15 2.0.0                   str
DEPNAM16 specter                 str
DEPVER16 0.8.3                   str
DEPNAM17 redrock                 str
DEPVER17 0.9.0                   str
======== ======================= ===== ==============================================

Data: FITS image [float32, 2999x500]

HDU1
----

EXTNAME = IVAR

*Summarize the contents of this HDU.*

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

*Summarize the contents of this HDU.*

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

*Summarize the contents of this HDU.*

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

*Summarize the contents of this HDU.*

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

*Summarize the contents of this HDU.*

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

=========== ========== ===== ===========
Name        Type       Units Description
=========== ========== ===== ===========
OBJTYPE     char[10]
TARGETCAT   char[20]
BRICKNAME   char[8]
TARGETID    int64
DESI_TARGET int64
BGS_TARGET  int64
MWS_TARGET  int64
MAG         float32[5]
FILTER      char[200]
SPECTROID   int64
POSITIONER  int32
LOCATION    int32
DEVICE_LOC  int32
PETAL_LOC   int32
FIBER       int32
LAMBDAREF   float32
RA_TARGET   float64
DEC_TARGET  float64
RA_OBS      float64
DEC_OBS     float64
X_TARGET    float32
Y_TARGET    float32
X_FVCOBS    float32
Y_FVCOBS    float32
Y_FVCERR    float32
X_FVCERR    float32
=========== ========== ===== ===========

HDU6
----

EXTNAME = SCORES

*Summarize the contents of this HDU.*

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

===================== ======= ===== ============================================
Name                  Type    Units Description
===================== ======= ===== ============================================
SUM_RAW_COUNT_Z       float64       sum counts in wave. range 7600,9800A
MEDIAN_RAW_COUNT_Z    float64       median counts/A in wave. range 7600,9800A
MEDIAN_RAW_SNR_Z      float64       median SNR/sqrt(A) in wave. range 7600,9800A
SUM_FFLAT_COUNT_Z     float64       sum counts in wave. range 7600,9800A
MEDIAN_FFLAT_COUNT_Z  float64       median counts/A in wave. range 7600,9800A
MEDIAN_FFLAT_SNR_Z    float64       median SNR/sqrt(A) in wave. range 7600,9800A
SUM_SKYSUB_COUNT_Z    float64       sum counts in wave. range 7600,9800A
MEDIAN_SKYSUB_COUNT_Z float64       median counts/A in wave. range 7600,9800A
MEDIAN_SKYSUB_SNR_Z   float64       median SNR/sqrt(A) in wave. range 7600,9800A
SUM_CALIB_COUNT_Z     float64       sum counts in wave. range 7600,9800A
MEDIAN_CALIB_COUNT_Z  float64       median counts/A in wave. range 7600,9800A
MEDIAN_CALIB_SNR_Z    float64       median SNR/sqrt(A) in wave. range 7600,9800A
===================== ======= ===== ============================================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
