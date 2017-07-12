========
fibermap
========

:Summary: The fibermap contains the fiber positioner configuration information for
    each exposure: what fiber is placed where, what target that is, etc.
:Naming Convention: ``fibermap-{EXPID}.fits``, where {EXPID} is the 8-digit exposure ID.
:Regex: ``fibermap-[0-9]{8}\.fits``
:File Type: FITS, 1 MB

This table is also propagated forward to the
:doc:`frame <../../DESI_SPECTRO_REDUX/SPECPROD/exposures/NIGHT/EXPID/frame-CAMERA-EXPID>`,
:doc:`cframe <../../DESI_SPECTRO_REDUX/SPECPROD/exposures/NIGHT/EXPID/cframe-CAMERA-EXPID>`, and
:doc:`spectra <../../DESI_SPECTRO_REDUX/SPECPROD/spectra/PIXGROUP/PIXNUM/spectra>`
files.

Contents
========

====== ======== ======== ===================
Number EXTNAME  Type     Contents
====== ======== ======== ===================
HDU0_           IMAGE    Blank
HDU1_  FIBERMAP BINTABLE Fiber map table
====== ======== ======== ===================


FITS Header Units
=================

HDU0
----

Blank; this HDU has no non-standard required keywords.

HDU1
----

EXTNAME = FIBERMAP

The fiber map table of which targets where placed on which fibers
at which locations.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ===== ==============================================
KEY      Example Value    Type  Comment
======== ================ ===== ==============================================
NAXIS1   228              int   length of dimension 1
NAXIS2   5                int   length of dimension 2
ENCODING ascii            str
EXTNAME  FIBERMAP         str
TELRA    335.03           float Telescope pointing RA in J2000 degrees
TELDEC   19.88            float Telescope pointing dec in J2000 degrees
FLAVOR   dark             str
NIGHT    20170327         str   YEARMMDD of sunset for this night
EXPID    2                int   unique DESI exposure ID
TILEID   4                int   DESI tile ID
DEPNAM00 python           str
DEPVER00 3.5.2            str
DEPNAM01 numpy            str
DEPVER01 1.11.2           str
DEPNAM02 scipy            str
DEPVER02 0.18.1           str
DEPNAM03 astropy          str
DEPVER03 1.2.1            str
DEPNAM04 yaml             str
DEPVER04 3.12             str
DEPNAM05 fitsio           str
DEPVER05 0.9.10           str
DEPNAM06 desiutil         str
DEPVER06 1.9.3.dev402     str
DEPNAM07 desispec         str
DEPVER07 0.13.1.dev1288   str
DEPNAM08 desitarget       str
DEPVER08 0.9.0.dev754     str
DEPNAM09 desimodel        str
DEPVER09 0.6.0.dev178     str
DEPNAM10 desisim          str
DEPVER10 0.18.1.dev825    str
DEPNAM11 specter          str
DEPVER11 0.7.0dev1        str
DEPNAM12 speclite         str
DEPVER12 0.5              str
CHECKSUM LO9JNN89LN8GLN89 str   HDU checksum updated 2017-03-27T16:11:38
DATASUM  4184538461       str   data unit checksum updated 2017-03-27T16:11:38
======== ================ ===== ==============================================

TODO: standardize keywords with ICS, e.g. FLAVOR -> PROGRAM.

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
FILTER      char[50]         SDSS_R, DECAM_Z, WISE1, etc.
SPECTROID   int32            Spectrograph ID [0-9]
POSITIONER  int32            Positioner Location ID [0-9542]
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
=========== ========== ===== ===============================================

Expected Changes
================

This format is out of sync with the
`Imaging Legacy Surveys datamodel <http://legacysurvey.org/dr4/files/>`_,
and will be updated to have consistent names and formats for values that are
propagated from the tractor / sweep files.
e.g. MAG[5] -> FLUX_G, FLUX_R, FLUX_Z, FLUX_W1, FLUX_W2.

This format is out of sync with the
:doc:`../../DESI_TARGET/fiberassign/tile` datamodel, and will be updated to
be consistent for values that are propagated forward from fiber assignment.
e.g. POSITIONER -> LOCATION.