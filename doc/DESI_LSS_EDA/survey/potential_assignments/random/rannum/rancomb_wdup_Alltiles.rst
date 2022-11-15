===========================
rancomb_brightwdup_Alltiles
===========================

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``rancomb_brightwdup_Alltiles.fits``, where ... *Give a human readable
    description of the filename, e.g. ``blat-{EXPID}`` where ``{EXPID}``
    is the 8-digit exposure ID.*
:Regex: ``rancomb_brightwdup_Alltiles.fits`` *Give a regular expression for this filename.
    For example, a six-digit number would correspond to ``[0-9]{6}``.*
:File Type: FITS, 230 MB  *This section gives the type of the file
    and its approximate size.*

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    *Brief Description*
HDU1_  FAVAIL  BINTABLE *Brief Description*
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

*Summarize the contents of this HDU.*

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = FAVAIL

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ========================= ===== =====================
    KEY      Example Value             Type  Comment
    ======== ========================= ===== =====================
    NAXIS1   40                        int   length of dimension 1
    NAXIS2   6046896                   int   length of dimension 2
    TILEID   21166                     int
    TILERA   212.136                   float
    TILEDEC  46.298                    float
    FIELDROT -0.096432263112936        float
    FA_PLAN  2022-07-01T00:00:00.000   str
    FA_HA    0.0                       float
    FA_RUN   2021-05-18T22:12:52+00:00 str
    REQRA    212.136                   float
    REQDEC   46.298                    float
    FIELDNUM 0                         int
    FA_VER   4.0.0                     str
    FA_SURV  main                      str
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
RA       float64       Right Ascension
DEC      float64       Declination
TILEID   int64         Unique DESI tile ID
======== ======= ===== =======================================================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
