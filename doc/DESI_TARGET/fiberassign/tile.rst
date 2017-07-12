===========
tile_TILEID
===========

General Description
===================

FITS file with fiber assignments for a given DESI tile.

Naming Convention
-----------------

TBD.  We should group under subdirectories of
$DESI_TARGET/fiberassign/, but the naming for the subdirectories and for the
files themselves is TBD.  The filename may also change to be more descriptive.

regex: ``tile_[0-9]{8}\.fits``

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
FIBER         int32            Fiber ID on the CCDs [0-4999]
LOCATION      int32            Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
TARGETID      int64            Selected target ID
RA            float64 deg      Right ascension of target
DEC           float64 deg      Declination of target
XFOCAL_DESIGN float32 mm       Designed X location on focal plane
YFOCAL_DESIGN float32 mm       Designed Y location on focal plane
DESI_TARGET   int64            Dark survey + calibration targeting bits
BGS_TARGET    int64            Bright Galaxy Survey targeting bits
MWS_TARGET    int64            Milky Way Survey targeting bits
NUMTARGET     int32            number of targets that this fiber covers
PRIORITY      int32            priority that was used while placing this target
BRICKNAME     char[8]          Brick name from tractor input
============= ======= ======== ===================

Notes:

  * X/YFOCAL_DESIGN are where fiber assignment thought the targets would
    be; this is non-authoritative and more detailed downstream code will have
    a refined answer for each actual observation of this tile.
  * This table defines the *requested* fiber assignments.  See
    :doc:`fiberassign <../../DESI_SPECTRO_DATA/NIGHT/fibermap-EXPID>` for the
    actual observed assignments.

Expected changes:

  * Add columns Q_DESIGN, S_DESIGN; perhaps remove XFOCAL_DESIGN, YFOCAL_DESIGN.
    (radius S and angle Q are the preferred coordinates in the curved focal
    surface; X and Y are the projections to the tangent plane)
  * Add columns PETAL_LOC [0-10] and DEVICE_LOC [0-542]; See
    `DESI-0530 <https://desi.lbl.gov/DocDB/cgi-bin/private/ShowDocument?docid=530>`_.

HDU2
----

Potential assignments.

A list of targets that could have been assigned to each fiber.
See `DESI-1049 <https://desi.lbl.gov/DocDB/cgi-bin/private/ShowDocument?docid=1049>`_ for
how to interpret this HDU.

Data Table Columns
~~~~~~~~~~~~~~~~~~

================= ===== ===== ===================
Name              Type  Units Description
================= ===== ===== ===================
POTENTIALTARGETID int64       label for field   1
================= ===== ===== ===================

Notes and Examples
==================

To do...
