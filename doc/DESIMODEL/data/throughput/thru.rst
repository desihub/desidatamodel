====
thru
====

:Summary: Throughput data file.
:Naming Convention: ``thru-{ARM}.fits``, where ``{ARM}`` is 'b', 'r', 'z'.
:Regex: ``thru-[brz]\.fits``
:File Type: FITS, 1 MB

Contents
========

====== ========== ======== ===================
Number EXTNAME    Type     Contents
====== ========== ======== ===================
HDU0_  PRIMARY    IMAGE    *Brief Description*
HDU1_  THROUGHPUT BINTABLE *Brief Description*
HDU2_  FIBERINPUT BINTABLE *Brief Description*
====== ========== ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

*Summarize the contents of this HDU.*

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = THROUGHPUT

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================= ===== =======================================
KEY      Example Value     Type  Comment
======== ================= ===== =======================================
NAXIS1   32                int   length of dimension 1
NAXIS2   24651             int   length of dimension 2
EXPTIME  1000.0            float default exposure time [sec]
GEOMAREA 86787.09421000001 float geometric area of mirror - obscurations
FIBERDIA 1.52              float average fiber diameter [arcsec]
WAVEMIN  3533              int   Minimum wavelength [Angstroms]
WAVEMAX  5998              int   Maximum wavelength [Angstroms]
EXTNAME  THROUGHPUT        str   extension name
======== ================= ===== =======================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

========== ======= ===== ===========
Name       Type    Units Description
========== ======= ===== ===========
wavelength float64
throughput float64
extinction float64
fiberinput float64
========== ======= ===== ===========

HDU2
----

EXTNAME = FIBERINPUT

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ============= ==== =====================
KEY     Example Value Type Comment
======= ============= ==== =====================
NAXIS1  40            int  length of dimension 1
NAXIS2  24651         int  length of dimension 2
EXTNAME FIBERINPUT    str  extension name
======= ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

========== ======= ===== ===========
Name       Type    Units Description
========== ======= ===== ===========
wavelength float64
elg        float64
lrg        float64
star       float64
sky        float64
========== ======= ===== ===========


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
