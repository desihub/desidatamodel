===========
tile_TILEID
===========

:Summary: FITS file with fiber assignments for a given DESI tile.
:Naming Convention: TBD.  We should group under subdirectories of
    $DESI_TARGET/fiberassign/, but the naming for the subdirectories and for the
    files themselves is TBD.  The filename may also change to be more descriptive.
:Regex: ``tile_[0-9]{8}\.fits``
:File Type: FITS, 800 kB

Contents
========

====== ===================== ======== ===================
Number EXTNAME               Type     Contents
====== ===================== ======== ===================
HDU0_  PRIMARY               IMAGE    Blank
HDU1_  FIBER_ASSIGNMENTS     BINTABLE Target assignment for each fiber
HDU2_  POTENTIAL_ASSIGNMENTS BINTABLE All targets that could have been assigned
====== ===================== ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = FIBER_ASSIGNMENTS

The target assignments for each fiber of this tile.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============= ===== ============================
KEY      Example Value Type  Comment
======== ============= ===== ============================
NAXIS1   78            int   width of table in bytes
NAXIS2   5000          int   number of rows in table
TILEID   11108         int   Tile ID number
TILERA   150.87        float Tile RA [deg]
TILEDEC  31.23         float Tile DEC [deg]
======== ============= ===== ============================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

============= ======= ======== ===================
Name          Type    Units    Description
============= ======= ======== ===================
FIBER         int32            Fiber ID on the CCDs [0-4999]
LOCATION      int32            Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
NUMTARGET     int16            number of targets that this fiber covers
PRIORITY      int32            priority that was used while placing this target
TARGETID      int64            Selected target ID
DESI_TARGET   int64            Dark survey + calibration targeting bits
BGS_TARGET    int64            Bright Galaxy Survey targeting bits
MWS_TARGET    int64            Milky Way Survey targeting bits
RA            float64 deg      Right ascension of target
DEC           float64 deg      Declination of target
XFOCAL_DESIGN float32 mm       Designed X location on focal plane
YFOCAL_DESIGN float32 mm       Designed Y location on focal plane
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

EXTNAME = POTENTIAL_ASSIGNMENTS

A list of targets that could have been assigned to each fiber.
See `DESI-1049 <https://desi.lbl.gov/DocDB/cgi-bin/private/ShowDocument?docid=1049>`_ for
how to interpret this HDU.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============= ==== ============================
KEY      Example Value Type Comment
======== ============= ==== ============================
NAXIS1   8             int  width of table in bytes
NAXIS2   53370         int  number of rows in table
======== ============= ==== ============================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

================= ===== ===== ===================
Name              Type  Units Description
================= ===== ===== ===================
POTENTIALTARGETID int64       label for field   1
================= ===== ===== ===================

Notes and Examples
==================

To do...
