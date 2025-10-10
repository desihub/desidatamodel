==============================
Tile locations in MOCK Randoms
==============================

:Summary: For each random given in the directory, the list of unique TARGETIDs with number of appearances as reachable according to fiber assigment and details on those appearances.
:Naming Convention: ``rancomb_{RANN}{OBSCON}_Alltilelocinfo.fits``, where ``{OBSCON}`` denotes the observing program, either ``dark`` or ``bright`` and ``{RANN}`` is the random number (18 of them).
:Regex: ``rancomb_[0-9]{1,2}{dark|bright}_Alltilelocinfo.fits``
:File Type: FITS, 3 GB

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

Empty HDU.

HDU1
----

EXTNAME = LSS

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
    DESIDR dr1           str  DESI Data Release
    ====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

========== ========= ===== ========================================================================
Name       Type      Units Description
========== ========= ===== ========================================================================
TARGETID   int64           Unique DESI target ID
NTILE      int64           Number of tiles target was available on
TILES      char[36]        TILEIDs of those tile, in string form separated by -
TILELOCIDS char[111]       TILELOCIDs that the target was available for, separated by -
========== ========= ===== ========================================================================

