=================
collisions-OBSCON
=================

:Summary: Compilation of all potential assignments with collisions with fiber assignment keep out zones given FIBER and LOCATION for the given TILEID
:Naming Convention: ``collisions-{OBSCON}.fits``, where ``{OBSCON}`` can be BRIGHT or DARK
:Regex: ``collisions-[a-z]{4,6}\.fits`` 
:File Type: FITS, 40 MB  

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

Main collision catalog for the given program bright or dark 

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =======================
    KEY    Example Value Type Comment
    ====== ============= ==== =======================
    NAXIS1 24            int  width of table in bytes
    NAXIS2 1775487       int  number of rows in table
    DESIDR dr1           str
    ====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

======== ===== ===== =======================================================
Name     Type  Units Description
======== ===== ===== =======================================================
TARGETID int64       Unique DESI target ID
FIBER    int32       Fiber ID on the CCDs [0-4999]
LOCATION int32       Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
TILEID   int64       Unique DESI tile ID
======== ===== ===== =======================================================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
