============================
datcomb_bright_tarwdup_zdone
============================

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``datcomb_bright_tarwdup_zdone.fits``, where ... *Give a human readable
    description of the filename, e.g. ``blat-{EXPID}`` where ``{EXPID}``
    is the 8-digit exposure ID.*
:Regex: ``datcomb_bright_tarwdup_zdone.fits`` *Give a regular expression for this filename.
    For example, a six-digit number would correspond to ``[0-9]{6}``.*
:File Type: FITS, 1 GB  *This section gives the type of the file
    and its approximate size.*

Contents
========

====== ===================== ======== ===================
Number EXTNAME               Type     Contents
====== ===================== ======== ===================
HDU0_                        IMAGE    *Brief Description*
HDU1_  POTENTIAL_ASSIGNMENTS BINTABLE *Brief Description*
====== ===================== ======== ===================


FITS Header Units
=================

HDU0
----

*Summarize the contents of this HDU.*

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = POTENTIAL_ASSIGNMENTS

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ========================= ===== =====================
    KEY      Example Value             Type  Comment
    ======== ========================= ===== =====================
    NAXIS1   151                       int   length of dimension 1
    NAXIS2   10117500                  int   length of dimension 2
    TILEID   22465                     int
    TILERA   269.625                   float
    TILEDEC  29.534                    float
    FIELDROT -0.143659054471033        float
    FA_PLAN  2022-07-01T00:00:00.000   str
    FA_HA    16.53                     float
    FA_RUN   2021-06-26T04:16:33+00:00 str
    REQRA    269.625                   float
    REQDEC   29.534                    float
    FIELDNUM 0                         int
    FA_VER   5.0.0                     str
    FA_SURV  main                      str
    FA_M_GFA 0.4                       float
    FA_M_PET 0.4                       float
    FA_M_POS 0.05                      float
    ======== ========================= ===== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

============= ======== ===== ========================================================================
Name          Type     Units Description
============= ======== ===== ========================================================================
RA            float64        Right Ascension
DEC           float64        Declination
TARGETID      int64          Unique DESI target ID
DESI_TARGET   int64          Dark survey + calibration targeting bits
BGS_TARGET    int64          Bright Galaxy Survey targeting bits
MWS_TARGET    int64          Milky Way Survey targeting bits
SUBPRIORITY   float64        Random subpriority [0-1] to break assignment ties
PRIORITY_INIT int64          Target initial priority from target selection bitmasks and OBSCONDITIONS
TARGET_STATE  char[30]       Combination of target class and its current observational state
TIMESTAMP     char[25]       UTC/ISO time at which the target state was updated
ZWARN_MTL     int64          The ZWARN from the zmtl file (contains extra bits)
PRIORITY      int64          Target current priority
FIBER         int32          Fiber ID on the CCDs [0-4999]
LOCATION      int32          Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
TILEID        int64          Unique DESI tile ID
============= ======== ===== ========================================================================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
