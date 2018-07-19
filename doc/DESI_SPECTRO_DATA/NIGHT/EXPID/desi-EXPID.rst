==========
desi-EXPID
==========

:Summary: Raw data from the DESI spectrographs, with one fpack-compressed
    HDU per spectrograph camera
:Naming Convention: ``desi-EXPID.fits.fz``, where EXPID is the zero-padded
    8-digit exposure ID.
:Regex: ``desi-[0-9]{8}\.fits.fz``
:File Type: FITS, 500 MB

Contents
========

There is one HDU per spectrograph camera with EXTNAMEs like
B0, B1, ... R0, R1, ... Z8, Z9.  The structure of each of these is
the same; only one is explicitly documented below.

====== ======= ===== ===================
Number EXTNAME Type  Contents
====== ======= ===== ===================
HDU0_  PRIMARY IMAGE Blank except for header keywords
HDU1_  B0      IMAGE Raw data from the b0 spectrograph
====== ======= ===== ===================

FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

Blank except for header keywords

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== =================== ===== ================================
KEY      Example Value       Type  Comment
======== =================== ===== ================================
TELRA    335.03              float Telescope pointing RA [degrees]
TELDEC   19.88               float Telescope pointing dec [degrees]
FLAVOR   dark                str   Flavor [arc, flat, science, ...]
EXPTIME  1000                int   Exposure time [sec]
NIGHT    20170327            str   Night of observation YEARMMDD
EXPID    2                   int   DESI exposure ID
DATE-OBS 2017-03-27T22:00:00 str   Start of exposure in UTC
AIRMASS  1.0                 float Airmass at middle of exposure
TILEID   4                   int   DESI tile ID
DOSVER   SIM                 str
FEEVER   SIM                 str
DETECTOR SIM                 str
DEPNAM00 python              str
DEPVER00 3.5.2               str
DEPNAM01 numpy               str
DEPVER01 1.11.2              str
DEPNAM02 scipy               str
DEPVER02 0.18.1              str
DEPNAM03 astropy             str
DEPVER03 1.2.1               str
DEPNAM04 yaml                str
DEPVER04 3.12                str
DEPNAM05 desiutil            str
DEPVER05 1.9.3.dev402        str
DEPNAM06 desispec            str
DEPVER06 0.13.1.dev1288      str
DEPNAM07 desitarget          str
DEPVER07 0.9.0.dev754        str
DEPNAM08 desimodel           str
DEPVER08 0.6.0.dev178        str
DEPNAM09 desisim             str
DEPVER09 0.18.1.dev825       str
DEPNAM10 specter             str
DEPVER10 0.7.0dev1           str
DEPNAM11 speclite            str
DEPVER11 0.5                 str
======== =================== ===== ================================

Empty HDU.

TODO:

  * Synchronize with ICS for keywords (e.g. FLAVOR -> PROGRAM)

HDU1
----

EXTNAME = B0

Unprocessed spectrograph raw data, including overscans, from camera B0.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ===================== ===== =========================================================
KEY      Example Value         Type  Comment
======== ===================== ===== =========================================================
NAXIS1   4204                  int   width of table in bytes
NAXIS2   4096                  int   number of rows in table
EXTNAME  B0                    str   name of this binary table extension
TELDEC   19.88                 float Telescope pointing dec [degrees]
FLAVOR   dark                  str   Flavor [arc, flat, science, ...]
EXPTIME  1000                  int   Exposure time [sec]
NIGHT    20170327              str   Night of observation YEARMMDD
EXPID    2                     int   DESI exposure ID
TELRA    335.03                float Telescope pointing RA [degrees]
DATE-OBS 2017-03-27T22:00:00   str   Start of exposure
AIRMASS  1.0                   float Airmass at middle of exposure
TILEID   4                     int   DESI tile ID
DOSVER   SIM                   str
CAMERA   b0                    str
FEEVER   SIM                   str
DETECTOR SIM                   str
GAIN1    1.0                   float Gains from ICS
GAIN2    1.0                   float
GAIN3    1.0                   float
GAIN4    1.0                   float
RDNOISE1 3.0                   float Expected readnoise from ICS, not measured from these data
RDNOISE2 3.0                   float
RDNOISE3 3.0                   float
RDNOISE4 3.0                   float
PRESEC1  [1:4,1:2048]          str
DATASEC1 [5:2052,1:2048]       str
BIASSEC1 [2053:2102,1:2048]    str
CCDSEC1  [1:2048,1:2048]       str
PRESEC2  [4201:4204,1:2048]    str
DATASEC2 [2153:4200,1:2048]    str
BIASSEC2 [2103:2152,1:2048]    str
CCDSEC2  [2049:4096,1:2048]    str
PRESEC3  [1:4,2049:4096]       str
DATASEC3 [5:2052,2049:4096]    str
BIASSEC3 [2053:2102,2049:4096] str
CCDSEC3  [1:2048,2049:4096]    str
PRESEC4  [4201:4204,2049:4096] str
DATASEC4 [2153:4200,2049:4096] str
BIASSEC4 [2103:2152,2049:4096] str
CCDSEC4  [2049:4096,2049:4096] str
INHERIT  T                     bool
======== ===================== ===== =========================================================

Data: int32 FITS image [ny, nx]

Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*

Expected Changes
================

* Coordinate with ICS for header keywords
* Add telemetry HDU with contents TBD
