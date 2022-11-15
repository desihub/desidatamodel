========================
Alltiles_tilelocs
========================

:Summary: Information on the tiles and locations each target appears on 
:Naming Convention: ``Alltiles_{PROGRAM}_tilelocs.dat.fits``, where ``{PROGRAM}`` denotes the observing program, either dark or bright
:Regex: For bright time ``Alltiles_bright_tilelocs.dat.fits`` 
:File Type: FITS, 544 MB  *This section gives the type of the file
    and its approximate size.*

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    Empty
HDU1_  TLINFO  BINTABLE Catalog data
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

Empty

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = TLINFO

Information on the tiles and locations each target appears on 

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =====================
    KEY    Example Value Type Comment
    ====== ============= ==== =====================
    NAXIS1 66            int  length of dimension 1
    NAXIS2 8645218       int  length of dimension 2
    ====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

========== ======== ===== ========================================================================
Name       Type     Units Description
========== ======== ===== ========================================================================
TARGETID   int64          Unique DESI target ID
NTILE      int64          Number of tiles target was available on
TILES      char[11]       TILEIDs of those tile, in string form separated by -;
TILELOCIDS char[39]       TILELOCIDs that the target was available for, separated by -
========== ======== ===== ========================================================================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
