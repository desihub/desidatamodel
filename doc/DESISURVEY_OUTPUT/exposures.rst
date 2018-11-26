===================
exposures_surveysim
===================

:Summary: List of exposures from surveysim.
:Naming Convention: ``exposures_surveysim.fits``
:Regex: ``exposures_surveysim\.fits``
:File Type: FITS, 15 KB  *This section gives the type of the file
    and its approximate size.*

*Note*: currently this is only an output from surveysim, but it may become an
output of survey operations, caching in a file the information that is also
contained in the operations database.

Contents
========

====== ========= ======== ===================
Number EXTNAME   Type     Contents
====== ========= ======== ===================
HDU0_            IMAGE    Blank
HDU1_  EXPOSURES BINTABLE Exposure metadata
HDU2_  TILEDATA  BINTABLE Tile metadata
====== ========= ======== ===================


FITS Header Units
=================

HDU0
----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ================= ==== =======
KEY     Example Value     Type Comment
======= ================= ==== =======
TILES   ./test-tiles.fits str
NEXP    21                int
INITIAL 2020-03-15        str
======= ================= ==== =======

Empty HDU.

HDU1
----

EXTNAME = EXPOSURES

Exposure metadata.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ============= ==== =====================
KEY     Example Value Type Comment
======= ============= ==== =====================
NAXIS1  36            int  length of dimension 1
NAXIS2  21            int  length of dimension 2
EXTNAME EXPOSURES     str  extension name
======= ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

======== ======= ===== ===========
Name     Type    Units Description
======== ======= ===== ===========
MJD      float64
EXPTIME  float32
TILEID   int32
SNR2FRAC float32
AIRMASS  float32
SEEING   float32
TRANSP   float32
SKY      float32
======== ======= ===== ===========

HDU2
----

EXTNAME = TILEDATA

Tile metadata.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ============= ==== =====================
KEY     Example Value Type Comment
======= ============= ==== =====================
NAXIS1  20            int  length of dimension 1
NAXIS2  10            int  length of dimension 2
EXTNAME TILEDATA      str  extension name
======= ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

======== ======= ===== ===========
Name     Type    Units Description
======== ======= ===== ===========
AVAIL    int32
PLANNED  int32
EXPTIME  float32
SNR2FRAC float32
NEXP     int32
======== ======= ===== ===========

*TODO*: please make it very clear whether AVAIL=available for fiber assignment
vs. available for observations or something else;
ditto for PLANNED=date on which fiber assignment was run after which it becomes
available for observing?  Or something else?  The two concepts I'm looking for:

  * the date on which all required overlaps are complete and the tile becomes
    eligible for fiber assignment (AVAIL? or is that tracked in the planner?)
  * the date on which fiber assignment was actually run and the tile becomes
    eligible for observations (PLANNED?)

Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
