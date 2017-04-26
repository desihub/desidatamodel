=========
fiberflat
=========

General Description
===================

Summary
-------

This file contains the fiberflat such that newflux = rawflux/fiberflat.

Naming Convention
-----------------

``fiberflat-{camera}-{expid}.fits``, where ``{camera}`` is the camera
name (e.g. b0, r1, z9) and ``{expid}`` is the zero padded 8-digit exposure ID.

regex: ``fiberflat-[brz][0-9]-[0-9]{8}\.fits``

File Type
---------

FITS, 45 MB

Contents
========

====== ========== ===== ===================
Number EXTNAME    Type  Contents
====== ========== ===== ===================
HDU0_  FIBERFLAT  IMAGE fiberflat[nspec, nwave]
HDU1_  IVAR       IMAGE inverse variance of fiberflat
HDU2_  MASK       IMAGE bitmask of fiberflat (0=good)
HDU3_  MEANSPEC   IMAGE average spectrum[nwave]
HDU4_  WAVELENGTH IMAGE wavelength grid[nwave] in Angstroms
====== ========== ===== ===================

Current pipeline (as of 2016-06-16) writes HDU0 with EXTNAME=FLUX, having
inherited that from the input frame.  That should be changed to FIBERFLAT
(as described above) or no HDU 0 EXTNAME (formal FITS standard).

astropy currently writes this as FITS file which it can read but cfitsio
cannot.  It is unknown which library is at fault.

FITS Header Units
=================

HDU0
----

Mean fiberflat.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

Header keywords are inherited from the input Frame file.

======== ====================================================================================================== ===== ==============================================
KEY      Example Value                                                                                          Type  Comment
======== ====================================================================================================== ===== ==============================================
NAXIS1   2975                                                                                                   int
NAXIS2   500                                                                                                    int
EXTNAME  FLUX                                                                                                   str   name of this binary table extension
TELRA    335.03                                                                                                 float Telescope pointing RA [degrees]
EXPID    0                                                                                                      int   DESI exposure ID
TILEID   4                                                                                                      int   DESI tile ID
TELDEC   19.88                                                                                                  float Telescope pointing dec [degrees]
DATE-OBS 2016-07-26T22:00:00                                                                                    str   Start of exposure
FLAVOR   flat                                                                                                   str   Flavor [arc, flat, science, ...]
NIGHT    20160726                                                                                               str   Night of observation YEARMMDD
AIRMASS  1.0                                                                                                    float Airmass at middle of exposure
EXPTIME  10                                                                                                     int   Exposure time [sec]
CAMERA   z0                                                                                                     str
GAIN1    1.0                                                                                                    float
GAIN2    1.0                                                                                                    float
GAIN3    1.0                                                                                                    float
GAIN4    1.0                                                                                                    float
RDNOISE1 2.9                                                                                                    float
RDNOISE2 2.9                                                                                                    float
RDNOISE3 2.9                                                                                                    float
RDNOISE4 2.9                                                                                                    float
PRESEC1  [1:7,1:2064]                                                                                           str
DATASEC1 [8:2064,1:2064]                                                                                        str
BIASSEC1 [2065:2114,1:2064]                                                                                     str
CCDSEC1  [1:2057,1:2064]                                                                                        str
PRESEC2  [4222:4228,1:2064]                                                                                     str
DATASEC2 [2165:4221,1:2064]                                                                                     str
BIASSEC2 [2115:2164,1:2064]                                                                                     str
CCDSEC2  [2058:4114,1:2064]                                                                                     str
PRESEC3  [1:7,2065:4128]                                                                                        str
DATASEC3 [8:2064,2065:4128]                                                                                     str
BIASSEC3 [2065:2114,2065:4128]                                                                                  str
CCDSEC3  [1:2057,2065:4128]                                                                                     str
PRESEC4  [4222:4228,2065:4128]                                                                                  str
DATASEC4 [2165:4221,2065:4128]                                                                                  str
BIASSEC4 [2115:2164,2065:4128]                                                                                  str
CCDSEC4  [2058:4114,2065:4128]                                                                                  str
OVERSCN1 186.790687984                                                                                          float
OBSRDN1  2.91374495497                                                                                          float
OVERSCN2 142.624612403                                                                                          float
OBSRDN2  2.91379123644                                                                                          float
OVERSCN3 150.976618217                                                                                          float
OBSRDN3  2.90516702412                                                                                          float
OVERSCN4 166.076046512                                                                                          float
OBSRDN4  2.92814520174                                                                                          float
INHERIT  T                                                                                                      bool
CHECKSUM a6Zgc4Zga4Zga4Zg                                                                                       str   HDU checksum updated 2016-06-10T22:02:54
DATASUM  4180184824                                                                                             str   data unit checksum updated 2016-06-10T22:02:54
NSPEC    5                                                                                                      int   Number of spectra
WAVEMIN  7445.0                                                                                                 float First wavelength [Angstroms]
WAVEMAX  9824.0                                                                                                 float Last wavelength [Angstroms]
WAVESTEP 0.8                                                                                                    float Wavelength step size [Angstroms]
SPECTER  0.5.0dev1                                                                                              str   https://github.com/desihub/specter
IN_PSF   ...st/calib2d/psf/20160726/psfnight-z0.fits                                                            str   Input spectral PSF
IN_IMG   .../dailytest/20160726/pix-z0-00000000.fits                                                            str   Input image
FIBERMIN 0                                                                                                      int
DEPNAM00 python                                                                                                 str
DEPVER00 2.7.11 \|Anaconda 2.0.1 (x86_64)\| (default, Dec  6 2015, 18:57:58) ...                                str
DEPNAM01 numpy                                                                                                  str
DEPVER01 1.10.4                                                                                                 str
DEPNAM02 scipy                                                                                                  str
DEPVER02 0.17.0                                                                                                 str
DEPNAM03 astropy                                                                                                str
DEPVER03 1.1.1                                                                                                  str
DEPNAM04 yaml                                                                                                   str
DEPVER04 3.11                                                                                                   str
DEPNAM05 matplotlib                                                                                             str
DEPVER05 1.5.0                                                                                                  str
DEPNAM06 desiutil                                                                                               str
DEPVER06 1.5.0.dev325                                                                                           str
DEPNAM07 desispec                                                                                               str
DEPVER07 0.5.0.dev858                                                                                           str
DEPNAM08 specter                                                                                                str
DEPVER08 0.5.0dev1                                                                                              str
DEPNAM09 speclite                                                                                               str
DEPVER09 0.3dev271.dev351                                                                                       str
======== ====================================================================================================== ===== ==============================================

Data: FITS image [float32, 2975x500]

HDU1
----

EXTNAME = IVAR

Inverse variance of the fiberflat.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2975             int
NAXIS2   500              int
EXTNAME  IVAR             str  extension name
CHECKSUM 9PBADOB69OBAAOB3 str  HDU checksum updated 2016-06-10T22:02:54
DATASUM  3462666130       str  data unit checksum updated 2016-06-10T22:02:54
======== ================ ==== ==============================================

Data: FITS image [float32, 2975x500]

HDU2
----

EXTNAME = MASK

Mask of the fiberflat; 0=good.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2975             int  length of original image axis
NAXIS2   500              int  length of original image axis
BSCALE   1                int
BZERO    2147483648       int
EXTNAME  MASK             str  name of this binary table extension
CHECKSUM FcV3FZT2FbT2FZT2 str  HDU checksum updated 2016-06-10T22:02:54
DATASUM  743774           str  data unit checksum updated 2016-06-10T22:02:54
======== ================ ==== ==============================================

Data: FITS image [int32, 2975x500]

HDU3
----

EXTNAME = MEANSPEC

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2975             int
EXTNAME  MEANSPEC         str  extension name
CHECKSUM cBAJf94GcAAGc93G str  HDU checksum updated 2016-06-10T22:02:54
DATASUM  2259023115       str  data unit checksum updated 2016-06-10T22:02:54
======== ================ ==== ==============================================

Data: FITS image [float32, 2975]

HDU4
----

EXTNAME = WAVELENGTH

Wavelength grid in Angstroms used by this fiberflat.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2975             int
EXTNAME  WAVELENGTH       str  extension name
CHECKSUM 9mXPJkUO9kUOGkUO str  HDU checksum updated 2016-06-10T22:02:54
DATASUM  3037649504       str  data unit checksum updated 2016-06-10T22:02:54
======== ================ ==== ==============================================

Data: FITS image [float32, 2975]
