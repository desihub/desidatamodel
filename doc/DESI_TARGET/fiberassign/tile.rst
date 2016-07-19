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

============= ======= ======== ===================
Name          Type    Units    Description
============= ======= ======== ===================
TILEID        int              Tile ID
TILERA        float   degrees  Tile right ascention
TILEDEC       float   degrees  Tile declination
============= ======= ======== ===================


Data Table Columns
~~~~~~~~~~~~~~~~~~

============= ======= ======== ===================
Name          Type    Units    Description
============= ======= ======== ===================
fiber         int32            Fiber id on the CCDs [0-4999]
positioner    int32            Positioner id on the focal plane [0-4999]
targetid      int64            Selected target ID
ra            float32 deg      Right ascension
dec           float32 deg      Declination
xfocal_design float32 mm       X location on focal plane
yfocal_design float32 mm       Y location on focal plane
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
