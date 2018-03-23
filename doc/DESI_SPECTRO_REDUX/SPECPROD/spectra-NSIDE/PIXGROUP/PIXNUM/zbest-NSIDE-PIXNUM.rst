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

Empty HDU.

This HDU has no non-standard required keywords.

TODO: this HDU should have code versions used but it doesn't yet.

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

=========== ========== ===== ===============================================
Name        Type       Units Description
=========== ========== ===== ===============================================
OBJTYPE     char[10]         Target type [ELG, LRG, QSO, STD, STAR, SKY]
TARGETCAT   char[20]         Name/version of the target catalog
BRICKNAME   char[8]          Brickname from target imaging
TARGETID    int64            Unique target ID
DESI_TARGET int64            DESI dark+calib targeting bit mask
BGS_TARGET  int64            DESI Bright Galaxy Survey targeting bit mask
MWS_TARGET  int64            DESI Milky Way Survey targeting bit mask
MAG         float32[5]       magnitudes in each of the filters
FILTER      char[200]        SDSS_R, DECAM_Z, WISE1, etc.
SPECTROID   int64            Spectrograph ID [0-9]
POSITIONER  int32            Positioner Location ID [0-9542]
LOCATION    int32
DEVICE_LOC  int32
PETAL_LOC   int32
FIBER       int32            Fiber ID [0-4999]
LAMBDAREF   float32          Reference wavelength at which to align fiber
RA_TARGET   float64          Target right ascension [degrees]
DEC_TARGET  float64          Target declination [degrees]
RA_OBS      float64          RA of obs from (X,Y)_FVCOBS and optics [deg]
DEC_OBS     float64          dec of obs from (X,Y)_FVCOBS and optics [deg]
X_TARGET    float64          X on focal plane derived from (RA,DEC)_TARGET
Y_TARGET    float64          Y on focal plane derived from (RA,DEC)_TARGET
X_FVCOBS    float64          X location observed by Fiber View Cam [mm]
Y_FVCOBS    float64          Y location observed by Fiber View Cam [mm]
Y_FVCERR    float32          Y location uncertainty from Fiber View Cam [mm]
X_FVCERR    float32          X location uncertainty from Fiber View Cam [mm]
NIGHT       int32
EXPID       int32
TILEID      int32
=========== ========== ===== ===============================================


Upcoming Changes
================

The following changes are not yet in the zbest files, but will be added in
the future:

* Code versions in HDU 0
* Coadded signal-to-noise per band
