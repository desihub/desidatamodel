===========================
fiberflat-CAMERA-EXPID.fits
===========================

:Summary: This file contains the fiberflat such that newflux = rawflux/fiberflat.
:Naming Convention: ``fiberflat-{CAMERA}-{EXPID}.fits``, where ``{camera}`` is the camera
    name (*e.g.* b0, r1, z9) and ``{EXPID}`` is the zero padded 8-digit exposure ID.
:Regex: ``fiberflat-[brz][0-9]-[0-9]{8}\.fits``
:File Type: FITS, 45 MB

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

TODO: Current pipeline (as of 2016-06-16) writes HDU0 with EXTNAME=FLUX, having
inherited that from the input frame.  That should be changed to FIBERFLAT
(as described above) or no HDU 0 EXTNAME (formal FITS standard).

astropy currently writes this as FITS file which it can read but cfitsio
cannot.  It is unknown which library is at fault.

FITS Header Units
=================

HDU0
----

EXTNAME = FIBERFLAT

Mean fiberflat.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

Header keywords are inherited from the input Frame file.

======== ====================================================================================================== ===== ==============================================
KEY      Example Value                                                                                          Type  Comment
======== ====================================================================================================== ===== ==============================================
NAXIS1   2975                                                                                                   int
NAXIS2   500                                                                                                    int
EXPID    0                                                                                                      int   DESI exposure ID
NIGHT    20160726                                                                                               str   Night of observation YEARMMDD
FLAVOR   flat                                                                                                   str   Flavor [arc, flat, science, ...]
DOSVER   SIM                                                                                                    str
DATE-OBS 2016-07-26T22:00:00                                                                                    str   Start of exposure
EXPTIME  10                                                                                                     float Exposure time [sec]
FEEVER   SIM                                                                                                    str
AIRORVAC vac                                                                                                    str
CAMERA   z0                                                                                                     str
FIBERMIN 0                                                                                                      int
CHECKSUM a6Zgc4Zga4Zga4Zg                                                                                       str   HDU checksum updated 2016-06-10T22:02:54
DATASUM  4180184824                                                                                             str   data unit checksum updated 2016-06-10T22:02:54
CHI2PDF  1.054664427586549                                                                                      float
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
NAXIS1   8                int  length of original image axis
NAXIS2   500              int  length of original image axis
BSCALE   1                int
BZERO    2147483648       int
CHECKSUM FcV3FZT2FbT2FZT2 str  HDU checksum updated 2016-06-10T22:02:54
DATASUM  743774           str  data unit checksum updated 2016-06-10T22:02:54
======== ================ ==== ==============================================

Data: FITS image [int32 (compressed), 2975x500]

HDU3
----

EXTNAME = MEANSPEC

Average flat lamp spectrum of fibers in this frame.  Fiberflat is relative
to this mean spectrum.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2975             int
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
BUNIT    Angstrom
CHECKSUM 9mXPJkUO9kUOGkUO str  HDU checksum updated 2016-06-10T22:02:54
DATASUM  3037649504       str  data unit checksum updated 2016-06-10T22:02:54
======== ================ ==== ==============================================

Data: FITS image [float32, 2975]
