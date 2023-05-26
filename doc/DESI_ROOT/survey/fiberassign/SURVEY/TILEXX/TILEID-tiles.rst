=================
TILEID-tiles.fits
=================

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
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
HDU1_  TILES   BINTABLE *Brief Description*
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

*Summarize the contents of this HDU.*

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

============= ======= ===== ===================
Name          Type    Units Description
============= ======= ===== ===================
TILEID        int32         label for field   1
RA            float64       label for field   2
DEC           float64       label for field   3
OBSCONDITIONS int32         label for field   4
IN_DESI       int16         label for field   5
PROGRAM       char[6]       label for field   6
============= ======= ===== ===================
