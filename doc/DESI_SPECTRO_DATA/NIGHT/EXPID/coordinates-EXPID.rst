=================
coordinates-EXPID
=================

:Summary: Coordinates data
:Naming Convention: ``coordinates-EXPID.fits``, where EXPID is the zero-padded
    8-digit exposure ID.
:Regex: ``coordinates-[0-9]{8}\.fits``
:File Type: FITS, 1 MB

Contents
========

====== ========== ======== ===================
Number EXTNAME    Type     Contents
====== ========== ======== ===================
HDU0_  COORDS     IMAGE    *Brief Description*
HDU1_  DATA       BINTABLE *Brief Description*
HDU2_  STATIONARY BINTABLE *Brief Description*
====== ========== ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = COORDS

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ========================================= ======= =======
    KEY      Example Value                             Type    Comment
    ======== ========================================= ======= =======
    TILEID   4403                                      int
    TILERA   170.239                                   float
    TILEDEC  -7.093                                    float
    FIELDROT 0.0210480650645507                        float
    FA_PLAN  2022-07-01T00:00:00.000                   str
    FA_HA    -6.72                                     float
    FA_RUN   2022-01-03T17:00:31+00:00                 str
    FA_M_GFA 0.4                                       float
    FA_M_PET 0.4                                       float
    FA_M_POS 0.05                                      float
    REQRA    170.239                                   float
    REQDEC   -7.093                                    float
    FIELDNUM 0                                         int
    FA_VER   5.4.0                                     str
    FA_SURV  main                                      str
    EXPID    118526                                    int
    FLAVOR   science                                   str
    SEQUENCE _Split                                    str
    GUIDECAM GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8 str
    ACQCAM   GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8 str
    GUIDTIME 5.0                                       float
    ACQTIME  15.0                                      float
    FOCUSCAM FOCUS1,FOCUS4,FOCUS6,FOCUS9               str
    FOCSTIME 60.0                                      float
    SKYCAM   SKYCAM0,SKYCAM1                           str
    SKYTIME  60.0                                      float
    SPCGRPHS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9   str
    CCDSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9   str
    ILLSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9   str
    OBSTYPE  SCIENCE                                   str
    EXPTIME  None                                      Unknown
    ESTTIME  3705.79                                   float
    MAXTIME  5400.0                                    float
    MINTIME  300.0                                     float
    REQTIME  1860.0                                    float
    MIDTIME  915.0                                     float
    NIGHT    20220113                                  int
    SEQSTART 2022-01-14T11:03:08.447408                str
    POSRMS   None                                      Unknown
    TURBRMS  None                                      Unknown
    POSENABL None                                      Unknown
    POSDISAB None                                      Unknown
    POSONTGT None                                      Unknown
    POSONFRC None                                      Unknown
    POSCVFRC None                                      Unknown
    POSCYCLE None                                      Unknown
    POSCNVGD None                                      Unknown
    CONVERGD None                                      Unknown
    ======== ========================================= ======= =======

Empty HDU.

HDU1
----

EXTNAME = DATA

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =======================
    KEY    Example Value Type Comment
    ====== ============= ==== =======================
    NAXIS1 240           int  width of table in bytes
    NAXIS2 5133          int  number of rows in table
    ====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

============ ======= ===== ===================
Name         Type    Units Description
============ ======= ===== ===================
PETAL_LOC    int64         label for field   1
DEVICE_LOC   int64         label for field   2
POS_Q        float64       label for field   3
POS_S        float64       label for field   4
POS_FLAGS    float64       label for field   5
POS_X        float64       label for field   6
POS_Y        float64       label for field   7
TARGET_RA    float64       label for field   8
TARGET_DEC   float64       label for field   9
FA_X         float32       label for field  10
FA_Y         float32       label for field  11
FA_FIBER     float64       label for field  12
FOR_DX_1     float64       label for field  13
FOR_DY_1     float64       label for field  14
FOR_X_1      float64       label for field  15
FOR_Y_1      float64       label for field  16
FLAGS_FOR_1  int64         label for field  17
FOR_OFFSET_1 float64       label for field  18
EXP_Q_1      float64       label for field  19
EXP_S_1      float64       label for field  20
FLAGS_EXP_1  int64         label for field  21
EXP_X_1      float64       label for field  22
EXP_Y_1      float64       label for field  23
FVC_X_1      float64       label for field  24
FVC_Y_1      float64       label for field  25
FLAGS_FVC_1  int64         label for field  26
CNT_X_1      float64       label for field  27
CNT_Y_1      float64       label for field  28
FLAGS_CNT_1  int64         label for field  29
CNT_MAG_1    float64       label for field  30
CNT_ERR_1    float64       label for field  31
============ ======= ===== ===================

HDU2
----

EXTNAME = STATIONARY

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =======================
    KEY    Example Value Type Comment
    ====== ============= ==== =======================
    NAXIS1 358           int  width of table in bytes
    NAXIS2 796           int  number of rows in table
    ====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

========== ========= ===== ===================
Name       Type      Units Description
========== ========= ===== ===================
PETAL_LOC  int64           label for field   1
DEVICE_LOC int64           label for field   2
ZENITH_X   float64         label for field   3
ZENITH_Y   float64         label for field   4
MODEL_X    char[163]       label for field   5
MODEL_Y    char[163]       label for field   6
========== ========= ===== ===================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
