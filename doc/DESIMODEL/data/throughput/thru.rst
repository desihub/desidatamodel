====
thru
====

:Summary: Throughput data file.
:Naming Convention: ``thru-{ARM}.fits``, where ``{ARM}`` is 'b', 'r', 'z'.
:Regex: ``thru-[brz]\.fits``
:File Type: FITS, 1 MB

Contents
========

====== ========== ======== =============================
Number EXTNAME    Type     Contents
====== ========== ======== =============================
HDU0_  PRIMARY    IMAGE    Empty
HDU1_  THROUGHPUT BINTABLE Throughput model
HDU2_  FIBERINPUT BINTABLE Geometric loss at fiber input
====== ========== ======== =============================

FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = THROUGHPUT

Throughput model.

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

========== ======= ======== ===========
Name       Type    Units    Description
========== ======= ======== ===========
wavelength float64 Angstrom Wavelengths
throughput float64          Throughput losses not due to atmosphere or fiber inputs
extinction float64          Atmospheric extinction
fiberinput float64          DEPRECATED; fiber input losses (point-source?)
========== ======= ======== ===========

HDU2
----

EXTNAME = FIBERINPUT

Typical fiber input geometric throughput for various object types.
0 = no transmission; 1 = all light makes it into the fibers.

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

========== ======= ======== ===========
Name       Type    Units    Description
========== ======= ======== ===========
wavelength float64 Angstrom Wavelengths at which loss is modeled
elg        float64          throughput for typical ELG
lrg        float64          throughput for typical LRG
star       float64          throughput for typical point source
sky        float64          throughput for uniform source
========== ======= ======== ===========


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
