=============
tile_{tileid}
=============

General Description
===================

FITS file with fiber assignments for a given DESI tile.

Naming Convention
-----------------

TBD.  We should group under subdirectories of
$DESI_TARGET/fiberassign/, but the naming for the subdirectories and for the
files themselves is TBD.

regex: ``tile-[0-9]{8}\.fits``

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
MJD           int64            Modified Julian Days
TAI           float64  sec     Time determined at Kitt Peak using GPS-based NTP servers
fiber         int32            Fiber id on the CCDs [0-4999]
positioner    int32            Positioner id on the focal plane [0-4999]
targetid      int64            Selected target ID
ra            float64 deg      Right ascension of target
dec           float64 deg      Declination of target
xfocal_design float32 mm       Designed X location on focal plane
yfocal_design float32 mm       Designed Y location on focal plane
Q_design      float32 mm       Designed Q location on petal
S_design      float32 mm       Designed S location on petal
xfvc_design   float32 pix      Designed X location on FVC CCD
yfvc_design   float32 pix      Designed Y location on FVC CCD
ha            float32 deg      Expected Hour Angle at the middle of each exposure
airtemp       float32 C        Air Temperature
trustemp      float32 C        Temperature of telescope
desi_target0  int64            TARGETFLAG for that target
numtarget     int32            number of targets that this fiber covers
t_priority    int32            target priority [deprecated?]
BRICKNAME     char[8]          Brick name from tractor input
============= ======= ======== ===================

Notes:

  * we will probably change these to UPPERCASE and adjust some names (e.g. t_priority to PRIORITY)
  * x/yfocal_design are where fiber assignment thought the targets would
    be; this is non-authoritative and more detailed downstream code may have a
    refined answer

HDU2
----

Potential assignments.

A list of targets that could have been assigned to each fiber.
See DESI-1049 (https://desi.lbl.gov/DocDB/cgi-bin/private/ShowDocument?docid=1049) for
how to interpret this HDU.

Data Table Columns
~~~~~~~~~~~~~~~~~~

================= ===== ===== ===================
Name              Type  Units Description
================= ===== ===== ===================
potentialtargetid int64       label for field   1
================= ===== ===== ===================

Notes and Examples
==================

To do...
