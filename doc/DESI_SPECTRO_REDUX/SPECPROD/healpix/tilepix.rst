============
tilepix.fits
============

:Summary: This file maps which DESI tiles overlap which HEALpix pixels (nested nside=64).
:Naming Convention: ``tilepix.fits``
:Regex: ``tilepix\.fits``
:File Type: FITS, 630 KB

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    Blank
HDU1_  TILEPIX BINTABLE table with healpix:tile mapping
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

Empty HDU.

HDU1
----

EXTNAME = TILEPIX

Table mapping tile petals to HEALPix pixels (nested nside=64).

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ============= ==== =====================
    KEY      Example Value Type Comment
    ======== ============= ==== =====================
    NAXIS1   9             int  length of dimension 1
    NAXIS2   70894         int  length of dimension 2
    HPXNSIDE 64            int
    HPXNEST  T             bool
    ======== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

========= ======= ===== ===========
Name      Type    Units Description
========= ======= ===== ===========
TILEID    int32         DESI Tile ID
SURVEY    char[7]       DESI survey (sv1, sv3, main...)
PROGRAM   char[6]       DESI program (dark, bright, ...)
PETAL_LOC int16         Petal location 0-9 = spectrograph number
HEALPIX   int32         Nested nside=64 healpix number
========= ======= ===== ===========


Notes and Examples
==================

Each DESI tile has 10 petals/spectrographs, each of which overlaps multiple
healpixels.  Similarly, each healpixel could be covered by multiple tile petals.
Since many DESI files are split by petal (spectrograph), this map gives the
individual petal coverage as well, not just that the tile overlaps the healpixel.

Example::

    import numpy as np
    from astropy.table import Table
    tilepix = Table.read('tilepix.fits')

    #- All healpix that cover tile 100 (20 healpix)
    np.unique(tilepix['HEALPIX'][tilepix['TILEID']==100])

    #- All tiles that cover healpix 11250 (28 tiles)
    np.unique(tilepix['TILEID'][tilepix['HEALPIX'] == 11250])

There is also a json version of this file with a dictionary structured as::

    tilepix[tileid][petal] -> list of healpix covered by that tile+petal

Due to limitations of the json format, the ``tileid`` and ``petal`` keys of the
dictionary are strings, not integers.
