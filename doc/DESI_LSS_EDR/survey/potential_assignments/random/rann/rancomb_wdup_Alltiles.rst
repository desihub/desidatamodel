===========================
rancomb_wdup_Alltiles
===========================

:Summary: It is a file with information about all random targets after match with potential assigment in fiber assigment.
:Naming Convention: ``rancomb_{PROGRAM}wdup_Alltiles.fits``, where ``{PROGRAM}`` is either ``dark`` or ``bright``.
:Regex: ``rancomb_[a-z]{4,6}wdup_Alltiles.fits``
:File Type: FITS, 145 MB

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    Empty
HDU1_  FAVAIL  BINTABLE Catalog data
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = FAVAIL

*Merge between potential assigments from fiber assigment and random targets*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ========================= ===== =====================
    KEY      Example Value             Type  Comment
    ======== ========================= ===== =====================
    NAXIS1   40                        int   length of dimension 1
    NAXIS2   3825185                   int   length of dimension 2
    TILEID   49                        int
    TILERA   179.691                   float
    TILEDEC  -0.078                    float
    FIELDROT 0.000359628494740581      float
    FA_PLAN  2022-07-01T00:00:00.000   str
    FA_HA    0.0                       float
    FA_RUN   2021-05-03T20:56:22+00:00 str
    REQRA    179.691                   float
    REQDEC   -0.078                    float
    FIELDNUM 0                         int
    FA_VER   2.3.0                     str
    FA_SURV  sv3                       str
    ======== ========================= ===== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

======== ======= ===== =======================================================
Name     Type    Units Description
======== ======= ===== =======================================================
LOCATION int32         Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBER    int32         Fiber ID on the CCDs [0-4999]
TARGETID int64         Unique DESI target ID
RA       float64 deg   Target Right Ascension
DEC      float64 deg   Target declination
TILEID   int64         Unique DESI tile ID
======== ======= ===== =======================================================

