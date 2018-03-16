=====================
sky-CAMERA-EXPID.fits
=====================

:Summary: This holds the sky model for a given camera and exposure.
:Naming Convention: ``sky-{CAMERA}-{EXPID}.fits``, where ``{CAMERA}`` is
    one of the spectrograph cameras (*e.g.* ``z1``) and ``{EXPID}``
    is the 8-digit exposure ID.
:Regex: ``sky-[brz][0-9]-[0-9]{8}\.fits``
:File Type: FITS, 17 MB

Contents
========

====== ========== ===== ===================
Number EXTNAME    Type  Contents
====== ========== ===== ===================
HDU0_  SKY        IMAGE sky model in photons/bin
HDU1_  IVAR       IMAGE inverse variance ``(photons/bin)^-2``
HDU2_  MASK       IMAGE sky mask (0 = good)
HDU3_  WAVELENGTH IMAGE wavelength in Angstrom
HDU4_  STATIVAR   IMAGE *Brief Description*
====== ========== ===== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = SKY

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
BUNIT    electron/Angstrom       str
AIRORVAC vac                     str   Vacuum wavelengths
CAMERA   z1                      str
FIBERMIN 500                     int
CHECKSUM 1HdW1GZU1GbU1GZU        str   HDU checksum updated 2018-03-01T15:04:16
DATASUM  4250999040              str   data unit checksum updated 2018-03-01T15:04:16
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
CHECKSUM 6WAh6U2e6U9e6U9e str  HDU checksum updated 2018-03-01T15:04:16
DATASUM  3062262200       str  data unit checksum updated 2018-03-01T15:04:16
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
CHECKSUM 0dTm2ZQl0bQl0ZQl str  HDU checksum updated 2018-03-01T15:04:16
DATASUM  749750           str  data unit checksum updated 2018-03-01T15:04:16
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
CHECKSUM 9HSaCFQZ9FQaCFQW str  HDU checksum updated 2018-03-01T15:04:16
DATASUM  1159831655       str  data unit checksum updated 2018-03-01T15:04:16
======== ================ ==== ==============================================

Data: FITS image [float32, 2999]

HDU4
----

EXTNAME = STATIVAR

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2999             int
NAXIS2   500              int
BUNIT    Angstrom         str
CHECKSUM DkSiGkPgDkPgDkPg str  HDU checksum updated 2018-03-01T15:04:16
DATASUM  507269785        str  data unit checksum updated 2018-03-01T15:04:16
======== ================ ==== ==============================================

Data: FITS image [float32, 2999x500]


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*