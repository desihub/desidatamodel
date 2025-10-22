=========================
Potential assigment files
=========================

:Summary: This file includes all reachable sky coordinates, as determined by the DESI fiberassign software, matching the footprint of DESI target samples as well as information about collisions
:Naming Convention: ``pota-{OBSCON}.fits`` or ``pota-{OBSCON}_{TAG}_{TRACER}.fits``, where ``{OBSCON}`` can be ``DARK`` or ``BRIGHT`` and ``{TAG}`` can be ``joined_unreduced`` or ``withntile`` (optional, only for dark tracers) and ``{TRACER}`` can be ``LRG``, ``QSO``, ``ELG_LOP`` for DARK or ``BGS`` for BRIGHT.
:Regex: ``pota-(BRIGHT|DARK)(?:_(joined_unreduced|withntile)_(LRG|BGS|QSO|ELG))?\.fits``
:File Type: FITS, 2 GB

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    Empty
HDU1_  LSS     BINTABLE Catalog data
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = LSS

All reachable randoms for the given realization in the directory (18 randoms) for the given OBSCON (DARK or BRIGHT)

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =======================
    KEY    Example Value Type Comment
    ====== ============= ==== =======================
    NAXIS1 49            int  width of table in bytes
    NAXIS2 49152819      int  number of rows in table
    DESIDR dr1           str  DESI Data Release
    ====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

=============== ========= ===== ===========================================================================================
Name            Type      Units Description
=============== ========= ===== ===========================================================================================
LOCATION [1]_   int64           Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBER [1]_      int64           Fiber ID on the CCDs [0-4999]
TARGETID        int64           Unique DESI target ID
RA              float64   deg   Barycentric Right Ascension in ICRS
DEC             float64   deg   Barycentric declination in ICRS
TILEID [1]_     int64           Unique DESI tile ID
COLLISION [1]_  logical         Boolean for whether given potential assignment had a fiber collision with any keep-out zone
NTILE [1]_      int64           Number of tiles target was available on
TILES [1]_      char[*]         TILEIDs of those tile, in string form separated by -
TILELOCIDS [1]_ char[*]         TILELOCIDs that the target was available for separated by -
=============== ========= ===== ===========================================================================================

.. [1] Optional
 

Notes and Examples
==================

* ``LOCATION``, ``FIBER``, ``TILEID``, ``COLLISION`` present for pota-OBSCON only
* ``NTILE``, ``TILES``, ``TILELOCIDS`` present for TAG = withntile
