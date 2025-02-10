============
tiles-OBSCON
============

:Summary: List of tiles making the release for the given program dark or bright (OBSCON)
:Naming Convention: ``tiles-{OBSCON}.fits``, where ``{OBSCON}`` is DARK or BRIGHT
:Regex: ``tiles-[a-z]{4,6}.fits`` 
:File Type: FITS, 59 KB  

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    Empty
HDU1_  LSS     BINTABLE Tile list
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

The sky coordinates for each TILEID consider for the corresponding LSS catalogs

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =====================
    KEY    Example Value Type Comment
    ====== ============= ==== =====================
    NAXIS1 24            int  length of dimension 1
    NAXIS2 2275          int  length of dimension 2
    DESIDR dr1           str  DESI Data Release
    ====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

====== ======= ===== ===================================
Name   Type    Units Description
====== ======= ===== ===================================
TILEID int64         Unique DESI tile ID
RA     float64 deg   Barycentric Right Ascension in ICRS
DEC    float64 deg   Barycentric declination in ICRS
====== ======= ===== ===================================


Notes and Examples
==================

These can be used to, e.g., define the greater footprint, which can be useful, e.g., for producing mock samples.
