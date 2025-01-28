================
pota-OBSCON.fits
================

:Summary: This file includes all reachable, as determined by the DESI fiberassign software, sky coordinates of randoms matching the footprint of DESI target samples as well as information about collisions
:Naming Convention: ``pota-{OBSCON}.fits``, where {OBSCON} can be DARK or BRIGHT
:Regex: ``pota-[a-z].fits{4,6}``
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
    DESIDR dr1           str
    ====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

========= ======= ===== ===========================================================================================
Name      Type    Units Description
========= ======= ===== ===========================================================================================
LOCATION  int64         Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBER     int64         Fiber ID on the CCDs [0-4999]
TARGETID  int64         Unique DESI target ID
RA        float64 deg   Barycentric Right Ascension in ICRS
DEC       float64 deg   Barycentric declination in ICRS
TILEID    int64         Unique DESI tile ID
COLLISION logical       Boolean for whether given potential assignment had a fiber collision with any keep-out zone
========= ======= ===== ===========================================================================================


Notes and Examples
==================

