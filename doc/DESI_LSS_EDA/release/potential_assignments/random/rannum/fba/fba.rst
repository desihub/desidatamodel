===
fba
===

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``fba-020548.fits``, where ... *Give a human readable
    description of the filename, e.g. ``blat-{EXPID}`` where ``{EXPID}``
    is the 8-digit exposure ID.*
:Regex: ``fba-020548.fits`` *Give a regular expression for this filename.
    For example, a six-digit number would correspond to ``[0-9]{6}``.*
:File Type: FITS, 1 MB  *This section gives the type of the file
    and its approximate size.*

Contents
========

====== ======== ======== ===================
Number EXTNAME  Type     Contents
====== ======== ======== ===================
HDU0_  PRIMARY  IMAGE    *Brief Description*
HDU1_  FASSIGN  BINTABLE *Brief Description*
HDU2_  FTARGETS BINTABLE *Brief Description*
HDU3_  FAVAIL   BINTABLE *Brief Description*
====== ======== ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ========================= ===== =======
    KEY      Example Value             Type  Comment
    ======== ========================= ===== =======
    TILEID   20548                     int
    TILERA   342.402                   float
    TILEDEC  -0.459                    float
    FIELDROT -0.0374910713166181       float
    FA_PLAN  2022-07-01T00:00:00.000   str
    FA_HA    0.0                       float
    FA_RUN   2021-06-28T20:50:21+00:00 str
    REQRA    342.402                   float
    REQDEC   -0.459                    float
    FIELDNUM 0                         int
    FA_VER   5.0.0                     str
    FA_SURV  main                      str
    ======== ========================= ===== =======

Empty HDU.

HDU1
----

EXTNAME = FASSIGN

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ========================= ===== =======================
    KEY      Example Value             Type  Comment
    ======== ========================= ===== =======================
    NAXIS1   82                        int   width of table in bytes
    NAXIS2   5020                      int   number of rows in table
    TILEID   20548                     int
    TILERA   342.402                   float
    TILEDEC  -0.459                    float
    FIELDROT -0.0374910713166181       float
    FA_PLAN  2022-07-01T00:00:00.000   str
    FA_HA    0.0                       float
    FA_RUN   2021-06-28T20:50:21+00:00 str
    REQRA    342.402                   float
    REQDEC   -0.459                    float
    FIELDNUM 0                         int
    FA_VER   5.0.0                     str
    FA_SURV  main                      str
    ======== ========================= ===== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

============= ======= ===== ==================================================================
Name          Type    Units Description
============= ======= ===== ==================================================================
FIBER         int32         Fiber ID on the CCDs [0-4999]
TARGETID      int64         Unique DESI target ID
LOCATION      int32         Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBERSTATUS   int32         Fiber status mask. 0=good
LAMBDA_REF    float32       Wavelength at which targets should be centered on fibers
PETAL_LOC     int16         Petal location [0-9]
DEVICE_LOC    int32         Device location on focal plane [0-523]
DEVICE_TYPE   char[3]       Devide type
TARGET_RA     float64       Target right ascension
TARGET_DEC    float64       Target declination
FA_TARGET     int64         Targeting bit internally used by fiberassign (linked with FA_TYPE)
FA_TYPE       binary        Target type (science, standard, sky, safe, suppsky)
FIBERASSIGN_X float32       Expected CS5 X location on focal plane
FIBERASSIGN_Y float32       Expected CS5 Y location on focal plane
PLATE_RA      float64       Right Ascension to be used by PlateMaker
PLATE_DEC     float64       Declination to be used by PlateMaker
============= ======= ===== ==================================================================

HDU2
----

EXTNAME = FTARGETS

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ========================= ===== =======================
    KEY      Example Value             Type  Comment
    ======== ========================= ===== =======================
    NAXIS1   65                        int   width of table in bytes
    NAXIS2   16264                     int   number of rows in table
    TILEID   20548                     int
    TILERA   342.402                   float
    TILEDEC  -0.459                    float
    FIELDROT -0.0374910713166181       float
    FA_PLAN  2022-07-01T00:00:00.000   str
    FA_HA    0.0                       float
    FA_RUN   2021-06-28T20:50:21+00:00 str
    REQRA    342.402                   float
    REQDEC   -0.459                    float
    FIELDNUM 0                         int
    FA_VER   5.0.0                     str
    FA_SURV  main                      str
    ======== ========================= ===== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

============= ======= ===== ==================================================================
Name          Type    Units Description
============= ======= ===== ==================================================================
TARGETID      int64         Unique DESI target ID
TARGET_RA     float64       Target right ascension
TARGET_DEC    float64       Target declination
FA_TARGET     int64         Targeting bit internally used by fiberassign (linked with FA_TYPE)
FA_TYPE       binary        Target type (science, standard, sky, safe, suppsky)
PRIORITY      int32         Target current priority
SUBPRIORITY   float64       Random subpriority [0-1] to break assignment ties
OBSCONDITIONS int32         Bit-coded of allowed observing conditions
PLATE_RA      float64       Right Ascension to be used by PlateMaker
PLATE_DEC     float64       Declination to be used by PlateMaker
============= ======= ===== ==================================================================

HDU3
----

EXTNAME = FAVAIL

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ========================= ===== =======================
    KEY      Example Value             Type  Comment
    ======== ========================= ===== =======================
    NAXIS1   16                        int   width of table in bytes
    NAXIS2   18104                     int   number of rows in table
    TILEID   20548                     int
    TILERA   342.402                   float
    TILEDEC  -0.459                    float
    FIELDROT -0.0374910713166181       float
    FA_PLAN  2022-07-01T00:00:00.000   str
    FA_HA    0.0                       float
    FA_RUN   2021-06-28T20:50:21+00:00 str
    REQRA    342.402                   float
    REQDEC   -0.459                    float
    FIELDNUM 0                         int
    FA_VER   5.0.0                     str
    FA_SURV  main                      str
    ======== ========================= ===== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

======== ===== ===== =======================================================
Name     Type  Units Description
======== ===== ===== =======================================================
LOCATION int32       Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBER    int32       Fiber ID on the CCDs [0-4999]
TARGETID int64       Unique DESI target ID
======== ===== ===== =======================================================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
