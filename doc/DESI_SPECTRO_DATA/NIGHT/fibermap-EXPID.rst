===================
fibermap-EXPID.fits
===================

:Summary: The fibermap contains the fiber positioner configuration information for
    each exposure: what fiber is placed where, what target that is, etc.
:Naming Convention: ``fibermap-{EXPID}.fits``, where {EXPID} is the 8-digit exposure ID.
:Regex: ``fibermap-[0-9]{8}\.fits``
:File Type: FITS, 1 MB

This table is also propagated forward to the
:doc:`frame <../../DESI_SPECTRO_REDUX/SPECPROD/exposures/NIGHT/EXPID/frame-CAMERA-EXPID>`,
:doc:`cframe <../../DESI_SPECTRO_REDUX/SPECPROD/exposures/NIGHT/EXPID/cframe-CAMERA-EXPID>`, and
:doc:`spectra <../../DESI_SPECTRO_REDUX/SPECPROD/spectra-NSIDE/PIXGROUP/PIXNUM/spectra-NSIDE-PIXNUM>`
files.

Contents
========

====== ======== ======== ===================
Number EXTNAME  Type     Contents
====== ======== ======== ===================
HDU0_  PRIMARY  IMAGE    Blank
HDU1_  FIBERMAP BINTABLE Fiber map table
====== ======== ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

Empty HDU.

This HDU has no non-standard required keywords.

HDU1
----

EXTNAME = FIBERMAP

The fiber map table of which targets where placed on which fibers
at which locations.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================= ===== =======================================
KEY      Example Value           Type  Comment
======== ======================= ===== =======================================
NAXIS1   378                     int   length of dimension 1
NAXIS2   5000                    int   length of dimension 2
NIGHT    20170327                str   YEARMMDD of sunset for this night
EXPID    2                       int   unique DESI exposure ID
TILEID   4                       int   DESI tile ID
FLAVOR   dark                    str   Flavor [arc, flat, science, zero, ...]
TELRA    335.03                  float Telescope pointing RA in J2000 degrees
TELDEC   19.88                   float Telescope pointing dec in J2000 degrees
AIRMASS  1.17754                 float Airmass at middle of exposure
EXPTIME  629.827                 float Exposure time [sec]
SEEING   0.7769                  float Seeing FWHM [arcsec]
MOONFRAC 0.4083                  float Moon illumination fraction 0-1; 1=full
MOONALT  -72.8225                float Moon altitude [degrees]
MOONSEP  131.1832                float Moon:tile separation angle [degrees]
DATE-OBS 2020-03-17T03:35:05.835 str   Start of exposure
======== ======================= ===== =======================================

TODO: standardize keywords with ICS, *e.g.* ``FLAVOR -> PROGRAM``.

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
X_TARGET    float32          X on focal plane derived from (RA,DEC)_TARGET
Y_TARGET    float32          Y on focal plane derived from (RA,DEC)_TARGET
X_FVCOBS    float32          X location observed by Fiber View Cam [mm]
Y_FVCOBS    float32          Y location observed by Fiber View Cam [mm]
Y_FVCERR    float32          Y location uncertainty from Fiber View Cam [mm]
X_FVCERR    float32          X location uncertainty from Fiber View Cam [mm]
=========== ========== ===== ===============================================

Expected Changes
================

This format is out of sync with the
`Imaging Legacy Surveys datamodel <http://legacysurvey.org/dr4/files/>`_,
and will be updated to have consistent names and formats for values that are
propagated from the tractor / sweep files.
*e.g.* ``MAG[5] -> FLUX_G, FLUX_R, FLUX_Z, FLUX_W1, FLUX_W2``.

This format is out of sync with the
:doc:`tile <../../DESI_TARGET/fiberassign/tile>` datamodel, and will be updated to
be consistent for values that are propagated forward from fiber assignment.
*e.g.* ``POSITIONER -> LOCATION``.
