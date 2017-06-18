==============================
tilemeasure_{tileid}_{visitid}
==============================

General Description
===================

FITS file with fiber assignments for a given DESI tile.

Naming Convention
-----------------

TBD.  We should group under subdirectories of
$DESI_TARGET/fiberassign/, but the naming for the subdirectories and for the
files themselves is TBD.

regex: ``tilemeasure-[0-9]{8}-[xx]\.fits``

Contents
========

====== ===================== ======== ===================
Number EXTNAME               Type     Contents
====== ===================== ======== ===================
HDU0_                        IMAGE    Blank
HDU1_  FIBER_ASSIGNMENTS     BINTABLE Target assignment for each fiber
HDU2_  POTENTIAL_ASSIGNMENTS BINTABLE All targets that could have been assigned
====== ===================== ======== ===================


FITS Header Units
=================

HDU0
----

Empty header.

HDU1
----

Fiber assignments.

The target assignments for each fiber of this tile.

Header Keywords
~~~~~~~~~~~~~~~

============= ======== ========= ============================
Name          Type       Units    Description
============= ======== ========= ============================
TILEID        int                Tile ID
TILERA        float64   degrees  Tile center right ascention
TILEDEC       float64   degrees  Tile center declination
============= ======== ========= ============================


Data Table Columns
~~~~~~~~~~~~~~~~~~

============= ======= ======== ===================
Name          Type    Units    Description
============= ======= ======== ===================
fiber         int32            Fiber id on the CCDs [0-4999]
location      int32            Positioner id on the focal plane [0-4999]
targetid      int64            Selected target ID
ra            float64 deg      Right ascension of target
dec           float64 deg      Declination of target
ra_fiber      float64 deg      Right ascension of fiber center measured by FVC
dec_fiber     float64 deg      Declination of fiber center measured by FVC
xfocal_design float32 mm       Designed X location on focal plane
yfocal_design float32 mm       Designed Y location on focal plane
xfocal_fiber  float32 mm       Measured X location on focal plane
yfocal_fiber  float32 mm       Measured Y location on focal plane
xfvc_design   float32 pix      Designed X location on FVC CCD
yfvc_design   float32 pix      Designed Y location on FVC CCD
xfvc_fiber    float32 pix      Measured X location on FVC CCD
yfvc_fiber    float32 pix      Measured Y location on FVC CCD
desi_target0  int64            TARGETFLAG for that target
numtarget     int32            number of targets that this fiber covers
t_priority    int32            target priority [deprecated?]
BRICKNAME     char[8]          Brick name from tractor input
============= ======= ======== ===================

HDU2
----

To do...
