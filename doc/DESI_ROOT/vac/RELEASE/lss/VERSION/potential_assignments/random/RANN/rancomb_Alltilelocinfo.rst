===========================
rancomb_Alltilelocinfo
===========================

:Summary: For random associated with ``RANN`` given in the directory, the list of unique TARGETIDs with number of appearances as reachable according to fiber assigment and details on those appearances.
:Naming Convention: ``rancomb_{PROGRAM}_Alltilelocinfo.fits``, where ``{PROGRAM}`` denotes the observing program, either ``dark`` or ``bright``.
:Regex: ``rancomb_[a-z]{4,6}_Alltilelocinfo.fits``
:File Type: FITS, 100 MB

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    Empty
HDU1_  TILELOC BINTABLE Catalog data
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = TILELOC

*Table for randoms with RANN, given by the directory with unique TARGETIDS (randoms) associated with tiles where it has potentially being observed after fiber assigment*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =======================
    KEY    Example Value Type Comment
    ====== ============= ==== =======================
    NAXIS1 226           int  width of table in bytes
    NAXIS2 465355        int  number of rows in table
    DESIDR edr           str  DESI Data Release
    ====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

========== ========= ===== ========================================================================
Name       Type      Units Description
========== ========= ===== ========================================================================
TARGETID   int64           Unique DESI target ID
NTILE      int64           Number of tiles target was available on
TILES      char[51]        TILEIDs of those tile, in string form separated by -
TILELOCIDS char[159]       TILELOCIDs that the target was available for, separated by -
========== ========= ===== ========================================================================

