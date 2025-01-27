===
fba
===

:Summary: The fiberassign file contains the fiber positioner configuration information for each exposure for the given randoms.
:Naming Convention: ``fba-{TILEID}.fits``, where `{TILEID}` is the 8-digit exposure ID.
:Regex: ``fba-[0-9]{6}.fits``
:File Type: FITS, 1 MB

Contents
========

====== ======== ======== ====================================================
Number EXTNAME  Type     Contents
====== ======== ======== ====================================================
HDU0_  PRIMARY  IMAGE    Headers
HDU1_  FASSIGN  BINTABLE Target assignments for each fiber
HDU2_  FTARGETS BINTABLE List of targets that are reachable by a positioner
HDU3_  FAVAIL   BINTABLE All possible (TARGETID, FIBER, LOCATION) assignments
====== ======== ======== ====================================================


FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

*No data, but some useful header keywords*

This HDU has no non-standard required keywords.

Empty HDU.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ========================= ===== =======
    KEY      Example Value             Type  Comment
    ======== ========================= ===== =======
    TILEID   30                        int
    TILERA   179.719                   float
    TILEDEC  -0.016                    float
    FIELDROT 0.000298543513740412      float
    FA_PLAN  2022-07-01T00:00:00.000   str
    FA_HA    0.0                       float
    FA_RUN   2021-04-10T21:28:37+00:00 str
    REQRA    179.719                   float
    REQDEC   -0.016                    float
    FIELDNUM 0                         int
    FA_VER   2.3.0                     str
    FA_SURV  sv3                       str
    ======== ========================= ===== =======

HDU1
----

EXTNAME = FASSIGN

*The target assignments for each fiber of this tile*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ========================= ===== =======================
    KEY      Example Value             Type  Comment
    ======== ========================= ===== =======================
    NAXIS1   66                        int   width of table in bytes
    NAXIS2   5020                      int   number of rows in table
    TILEID   30                        int
    TILERA   179.719                   float
    TILEDEC  -0.016                    float
    FIELDROT 0.000298543513740412      float
    FA_PLAN  2022-07-01T00:00:00.000   str
    FA_HA    0.0                       float
    FA_RUN   2021-04-10T21:28:37+00:00 str
    REQRA    179.719                   float
    REQDEC   -0.016                    float
    FIELDNUM 0                         int
    FA_VER   2.3.0                     str
    FA_SURV  sv3                       str
    DESIDR   edr                       str   DESI Data Release
    ======== ========================= ===== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

============= ======= ======== ========================================================================
Name          Type    Units    Description
============= ======= ======== ========================================================================
FIBER         int32            Fiber ID on the CCDs [0-4999]
TARGETID      int64            Unique DESI target ID
LOCATION      int32            Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBERSTATUS   int32            Fiber status mask. 0=good
LAMBDA_REF    float32 Angstrom Requested wavelength at which targets should be centered on fibers
PETAL_LOC     int16            Petal location [0-9]
DEVICE_LOC    int32            Device location on focal plane [0-523]
DEVICE_TYPE   char[3]          Device type
TARGET_RA     float64 deg      Target right ascension
TARGET_DEC    float64 deg      Target declination
FA_TARGET     int64            Targeting bit internally used by fiberassign (linked with FA_TYPE)
FA_TYPE       binary           Fiberassign internal target type (science, standard, sky, safe, suppsky)
FIBERASSIGN_X float32 mm       Fiberassign expected CS5 X location on focal plane
FIBERASSIGN_Y float32 mm       Fiberassign expected CS5 Y location on focal plane
============= ======= ======== ========================================================================

HDU2
----

EXTNAME = FTARGETS

*Unique list of targets reachable by a positioner*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ========================= ===== =======================
    KEY      Example Value             Type  Comment
    ======== ========================= ===== =======================
    NAXIS1   49                        int   width of table in bytes
    NAXIS2   16584                     int   number of rows in table
    TILEID   30                        int
    TILERA   179.719                   float
    TILEDEC  -0.016                    float
    FIELDROT 0.000298543513740412      float
    FA_PLAN  2022-07-01T00:00:00.000   str
    FA_HA    0.0                       float
    FA_RUN   2021-04-10T21:28:37+00:00 str
    REQRA    179.719                   float
    REQDEC   -0.016                    float
    FIELDNUM 0                         int
    FA_VER   2.3.0                     str
    FA_SURV  sv3                       str
    DESIDR   edr                       str   DESI Data Release
    ======== ========================= ===== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

============= ======= ===== ========================================================================
Name          Type    Units Description
============= ======= ===== ========================================================================
TARGETID      int64         Unique DESI target ID
TARGET_RA     float64 deg   Target right ascension
TARGET_DEC    float64 deg   Target declination
FA_TARGET     int64         Targeting bit internally used by fiberassign (linked with FA_TYPE)
FA_TYPE       binary        Fiberassign internal target type (science, standard, sky, safe, suppsky)
PRIORITY      int32         Target current priority
SUBPRIORITY   float64       Random subpriority [0-1) to break assignment ties
OBSCONDITIONS int32         Bitmask of allowed observing conditions
============= ======= ===== ========================================================================

HDU3
----

EXTNAME = FAVAIL

*A list of targets that could have been assigned to each fiber*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ========================= ===== =======================
    KEY      Example Value             Type  Comment
    ======== ========================= ===== =======================
    NAXIS1   16                        int   width of table in bytes
    NAXIS2   18420                     int   number of rows in table
    TILEID   30                        int
    TILERA   179.719                   float
    TILEDEC  -0.016                    float
    FIELDROT 0.000298543513740412      float
    FA_PLAN  2022-07-01T00:00:00.000   str
    FA_HA    0.0                       float
    FA_RUN   2021-04-10T21:28:37+00:00 str
    REQRA    179.719                   float
    REQDEC   -0.016                    float
    FIELDNUM 0                         int
    FA_VER   2.3.0                     str
    FA_SURV  sv3                       str
    DESIDR   edr                       str   DESI Data Release
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

