======================
rancomb_Alltilelocinfo
======================

:Summary: For a random associated with ``{RANN}``, the list of unique TARGETIDs with number of appearances as reachable according to fiber assigment and details on those appearances.
:Naming Convention: ``rancomb_{RANN}{PROGRAM}_Alltilelocinfo.fits``, where ``{RANN}`` is the number of the random file (0 through 17) and ``{PROGRAM}`` is the observing program, either ``dark`` or ``bright``.
:Regex: ``rancomb_[0-9]+(dark|bright)_Alltilelocinfo.fits``
:File Type: FITS, 327 MB

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

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = TLINFO

Information on the tiles and locations that a given random appears on.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =======================
    KEY    Example Value Type Comment
    ====== ============= ==== =======================
    NAXIS1 66            int  width of table in bytes
    NAXIS2 5196355       int  number of rows in table
    DESIDR edr           str  DESI Data Release
    ====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

========== ======== ===== ========================================================================
Name       Type     Units Description
========== ======== ===== ========================================================================
TARGETID   int64          Unique DESI target ID
NTILE      int64          Number of tiles target was available on
TILES      char[*]        TILEIDs of those tile, in string form separated by '-'
TILELOCIDS char[*]        TILELOCIDs that the target was available for, separated by '-'
========== ======== ===== ========================================================================

