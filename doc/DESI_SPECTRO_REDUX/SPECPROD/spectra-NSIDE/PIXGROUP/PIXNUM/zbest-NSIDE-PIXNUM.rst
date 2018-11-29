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
BRICKNAME char[8]           Imaging brickname where this target came from
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

================= ======= ===== ============================================
Name              Type    Units Description
================= ======= ===== ============================================
TARGETID          int64         Unique target ID
DESI_TARGET       int64         DESI dark+calib targeting bit mask
BGS_TARGET        int64         DESI Bright Galaxy Survey targeting bit mask
MWS_TARGET        int64         DESI Milky Way Survey targeting bit mask
SECONDARY_TARGET  int64
TARGET_RA         float64       Target right ascension [degrees]
TARGET_DEC        float64       Target declination [degrees]
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
PMRA_IVAR         float32
PMDEC_IVAR        float32
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
FIBER             int32         Fiber ID [0-4999]
PETAL_LOC         int32
DEVICE_LOC        int32
LOCATION          int32
FIBERSTATUS       int32
OBJTYPE           char[3]
LAMBDA_REF        float32
DESIGN_X          float32
DESIGN_Y          float32
DESIGN_Q          float32
DESIGN_S          float32
NUMTARGET         int16
FIBER_RA          float64
FIBER_DEC         float64
FIBER_RA_IVAR     float32
FIBER_DEC_IVAR    float32
DELTA_X           float32
DELTA_Y           float32
DELTA_X_IVAR      float32
DELTA_Y_IVAR      float32
NUM_ITER          int32
SPECTROID         int32
BRICKNAME         char[8]       Brickname from target imaging
LAMBDAREF         float64       Reference wavelength at which to align fiber
================= ======= ===== ============================================

Upcoming Changes
================

The following changes are not yet in the zbest files, but will be added in
the future:

* Code versions in HDU 0
* Coadded signal-to-noise per band
