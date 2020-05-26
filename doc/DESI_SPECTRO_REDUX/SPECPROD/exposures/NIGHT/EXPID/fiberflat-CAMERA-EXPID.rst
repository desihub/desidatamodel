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

====== ========== ======== ===================
Number EXTNAME    Type     Contents
====== ========== ======== ===================
HDU0_  FIBERFLAT  IMAGE    fiberflat[nspec, nwave]
HDU1_  IVAR       IMAGE    inverse variance of fiberflat
HDU2_  MASK       IMAGE    bitmask of fiberflat (0=good)
HDU3_  MEANSPEC   IMAGE    average spectrum[nwave]
HDU4_  WAVELENGTH IMAGE    wavelength grid[nwave] in Angstroms
HDU5_  FIBERMAP   BINTABLE fibermap
====== ========== ======== ===================

Note: the FIBERMAP HDU may be dropped from future versions

FITS Header Units
=================

HDU0
----

EXTNAME = FIBERFLAT

Mean fiberflat.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

Header keywords are inherited from the input Frame file.

======== =========================== ===== ==============================================
KEY      Example Value               Type  Comment
======== =========================== ===== ==============================================
NAXIS1   2975                        int
NAXIS2   500                         int
EXPID    0                           int   DESI exposure ID
NIGHT    20160726                    str   Night of observation YEARMMDD
FLAVOR   flat                        str   Flavor [arc, flat, science, ...]
DOSVER   SIM                         str
DATE-OBS 2016-07-26T22:00:00         str   Start of exposure
EXPTIME  10                          float Exposure time [sec]
FEEVER   SIM                         str
AIRORVAC vac                         str
CAMERA   z0                          str
FIBERMIN 0                           int
CHECKSUM a6Zgc4Zga4Zga4Zg            str   HDU checksum updated 2016-06-10T22:02:54
DATASUM  4180184824                  str   data unit checksum updated 2016-06-10T22:02:54
CHI2PDF  1.054664427586549           float
======== =========================== ===== ==============================================

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

Prior to desispec/0.24.0 and software release 18.9, the MASK HDU was compressed.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2975             int  Number of wavelengths
NAXIS2   500              int  Number of spectra
BSCALE   1                int
BZERO    2147483648       int
CHECKSUM FcV3FZT2FbT2FZT2 str  HDU checksum updated 2016-06-10T22:02:54
DATASUM  743774           str  data unit checksum updated 2016-06-10T22:02:54
======== ================ ==== ==============================================

Data: FITS image [int32, 2975x500]

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
NAXIS1   2975             int  Number of wavelengths
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
NAXIS1   2975             int  Number of wavelengths
BUNIT    Angstrom         str
CHECKSUM 9mXPJkUO9kUOGkUO str  HDU checksum updated 2016-06-10T22:02:54
DATASUM  3037649504       str  data unit checksum updated 2016-06-10T22:02:54
======== ================ ==== ==============================================

Data: FITS image [float32, 2975]

HDU5
----

EXTNAME = FIBERMAP

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   357              int  length of dimension 1
NAXIS2   500              int  length of dimension 2
ENCODING ascii            str
CHECKSUM GXdcHVbZGVbbGVbZ str  HDU checksum updated 2020-04-29T21:19:14
DATASUM  1416756853       str  data unit checksum updated 2020-04-29T21:19:14
======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

================= ======= ===== ===========
Name              Type    Units Description
================= ======= ===== ===========
TARGETID          int64
DESI_TARGET       int64
BGS_TARGET        int64
MWS_TARGET        int64
SECONDARY_TARGET  int64
TARGET_RA         float64
TARGET_DEC        float64
TARGET_RA_IVAR    float64
TARGET_DEC_IVAR   float64
BRICKID           int64
BRICK_OBJID       int64
MORPHTYPE         char[4]
PRIORITY          int32
SUBPRIORITY       float64
REF_ID            int64
PMRA              float32
PMDEC             float32
REF_EPOCH         float32
PMRA_IVAR         float32
PMDEC_IVAR        float32
RELEASE           int16
FLUX_G            float32
FLUX_R            float32
FLUX_Z            float32
FLUX_W1           float32
FLUX_W2           float32
FLUX_IVAR_G       float32
FLUX_IVAR_R       float32
FLUX_IVAR_Z       float32
FLUX_IVAR_W1      float32
FLUX_IVAR_W2      float32
FIBERFLUX_G       float32
FIBERFLUX_R       float32
FIBERFLUX_Z       float32
FIBERFLUX_W1      float32
FIBERFLUX_W2      float32
FIBERTOTFLUX_G    float32
FIBERTOTFLUX_R    float32
FIBERTOTFLUX_Z    float32
FIBERTOTFLUX_W1   float32
FIBERTOTFLUX_W2   float32
MW_TRANSMISSION_G float32
MW_TRANSMISSION_R float32
MW_TRANSMISSION_Z float32
EBV               float32
PHOTSYS           char[1]
OBSCONDITIONS     int32
NUMOBS_INIT       int64
PRIORITY_INIT     int64
NUMOBS_MORE       int32
HPXPIXEL          int64
FIBER             int32
PETAL_LOC         int32
DEVICE_LOC        int32
LOCATION          int32
FIBERSTATUS       int32
OBJTYPE           char[3]
LAMBDA_REF        float32
FIBERASSIGN_X     float32
FIBERASSIGN_Y     float32
FA_TARGET         int64
FA_TYPE           binary
NUMTARGET         int16
FIBER_RA          float64
FIBER_DEC         float64
FIBER_RA_IVAR     float32
FIBER_DEC_IVAR    float32
PLATEMAKER_X      float32
PLATEMAKER_Y      float32
PLATEMAKER_RA     float32
PLATEMAKER_DEC    float32
NUM_ITER          int32
SPECTROID         int32
================= ======= ===== ===========

