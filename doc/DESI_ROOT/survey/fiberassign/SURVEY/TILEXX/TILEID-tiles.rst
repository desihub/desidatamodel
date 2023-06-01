=================
TILEID-tiles.fits
=================

:Summary: This file contains the designed properties of the observed tile.
:Naming Convention: ``{TILEID}-tiles.fits``, where ``{TILEID}`` is the zero-padded,
    6-digit TILED.
:Regex: ``[0-9]{6}-tiles\.fits``
:File Type: FITS, 8 KB

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    Empty HDU
HDU1_  TILES   BINTABLE Tile designed properties.
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = TILES

Tile designed properties.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =======================
    KEY    Example Value Type Comment
    ====== ============= ==== =======================
    NAXIS1 32            int  width of table in bytes
    NAXIS2 1             int  number of rows in table
    ====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

============= ======= ===== ===============================================
Name          Type    Units Description
============= ======= ===== ===============================================
TILEID        int32         Unique DESI tile ID
RA            float64 deg   Barycentric Right Ascension in ICRS
DEC           float64 deg   Barycentric declination in ICRS
OBSCONDITIONS int32         Bitmask of allowed observing conditions
IN_DESI       int16         Used by fiberassign to make a tile in the DESI footprint; always set to 1
PROGRAM       char[6]       DESI program type - BRIGHT, DARK, BACKUP, OTHER
============= ======= ===== ===============================================
