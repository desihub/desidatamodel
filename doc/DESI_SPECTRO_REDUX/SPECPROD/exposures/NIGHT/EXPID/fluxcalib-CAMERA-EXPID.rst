=======================
calib-CAMERA-EXPID.fits
=======================

:Summary: This holds the flux calibration model for a given camera and exposure.
:Naming Convention: ``calib-{CAMERA}-{EXPID}.fits``, where ``{CAMERA}`` is
    one of the spectrograph cameras (*e.g.* ``z1``) and ``{EXPID}``
    is the 8-digit exposure ID.
:Regex: ``fluxcalib-[brz][0-9]-[0-9]{8}\.fits``
:File Type: FITS, 10 MB

Contents
========

====== ========== ===== ===================
Number EXTNAME    Type  Contents
====== ========== ===== ===================
HDU0_  FLUXCALIB  IMAGE Flux calibration model
HDU1_  IVAR       IMAGE Inverse variance of flux
HDU2_  MASK       IMAGE Mask (0 = good)
HDU3_  WAVELENGTH IMAGE wavelength in Angstrom
====== ========== ===== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = FLUXCALIB

Flux calibration model such that calibrated flux = uncalibrated photons / model.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================== ===== ==============================================
KEY      Example Value              Type  Comment
======== ========================== ===== ==============================================
NAXIS1   2645                       int
NAXIS2   500                        int
NIGHT    20200316                   str   Night of observation YEARMMDD
EXPID    20                         int   DESI exposure ID
TILEID   11108                      int   DESI tile ID
PROGRAM  DARK                       str   program [dark, bright, ...]
FLAVOR   science                    str   Flavor [arc, flat, science, zero, ...]
TELRA    150.87                     float Telescope pointing RA [degrees]
TELDEC   31.23                      float Telescope pointing dec [degrees]
AIRMASS  1.307154717878038          float Airmass at middle of exposure
EXPTIME  1142.541228573218          float Exposure time [sec]
SEEING   0.7572662830352783         float Seeing FWHM [arcsec]
MOONFRAC 0.4083473802955095         float Moon illumination fraction 0-1; 1=full
MOONALT  -79.39563600071901         float Moon altitude [degrees]
MOONSEP  131.2947533254612          float Moon:tile separation angle [degrees]
DATE-OBS 2020-03-17T02:42:47.160    str   Start of exposure
MJD      58924.37858796309          float
SNR2FRAC 0.501188337802887          float
TRANSP   0.9980747699737549         float
SKY      1.0                        float
RA       150.73                     float
DEC      30.52                      float
PASS     1                          int
DOSVER   SIM                        str
FEEVER   SIM                        str
BUNIT    10**+17 cm2 count s / erg  str   *i.e.* (elec/A) / (1e-17 erg/s/cm2/A)
AIRORVAC vac                        str   Vacuum wavelengths
CAMERA   z1                         str
FIBERMIN 500                        int
CHECKSUM 1HdW1GZU1GbU1GZU           str   HDU checksum updated 2018-03-01T15:04:16
DATASUM  4250999040                 str   data unit checksum updated 2018-03-01T15:04:16
======== ========================== ===== ==============================================

Data: FITS image [float32, 2645x500]

HDU1
----

EXTNAME = IVAR

Inverse variance of flux calibration model.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2645             int
NAXIS2   500              int
CHECKSUM 6MLF7LID6LID6LID str  HDU checksum updated 2018-03-01T15:08:08
DATASUM  3645106355       str  data unit checksum updated 2018-03-01T15:08:08
======== ================ ==== ==============================================

Data: FITS image [float32, 2645x500]

HDU2
----

EXTNAME = MASK

Mask of flux calibration model; 0=good.

Prior to desispec/0.24.0 and software release 18.9, the MASK HDU was compressed.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2645             int  length of original image axis
NAXIS2   500              int  length of original image axis
BSCALE   1                int
BZERO    2147483648       int
CHECKSUM YeVDcZTCZbTCaZTC str  HDU checksum updated 2018-03-01T15:08:08
DATASUM  661250           str  data unit checksum updated 2018-03-01T15:08:08
======== ================ ==== ==============================================

Data: FITS image [int32, 2645x500]

HDU3
----

EXTNAME = WAVELENGTH

Wavelengths at which the flux calibration model is evaluated.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2645             int
BUNIT    Angstrom         str
CHECKSUM 5A83A5535A53A553 str  HDU checksum updated 2018-03-01T15:08:08
DATASUM  1455388369       str  data unit checksum updated 2018-03-01T15:08:08
======== ================ ==== ==============================================

Data: FITS image [float32, 2645]


Notes and Examples
==================

We may add an additional HDU with ``EXTNAME=METADATA`` containing a
binary table with one row per standard star giving
the details of which model was used, etc.
This is not yet implemented and details TBD.
