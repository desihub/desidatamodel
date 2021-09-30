====
tile
====

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``tile-qa-20096-thru20210608.fits``, where ... *Give a human readable
    description of the filename, e.g. ``blat-{EXPID}`` where ``{EXPID}``
    is the 8-digit exposure ID.*
:Regex: ``tile-qa-20096-thru20210608.fits`` *Give a regular expression for this filename.
    For example, a six-digit number would correspond to ``[0-9]{6}``.*
:File Type: FITS, 627 KB  *This section gives the type of the file
    and its approximate size.*

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    *Brief Description*
HDU1_  FIBERQA BINTABLE *Brief Description*
HDU2_  PETALQA BINTABLE *Brief Description*
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
CHECKSUM D5aEE4a9D4aED4a9 str  HDU checksum updated 2021-07-16T19:03:01
DATASUM  0                str  data unit checksum updated 2021-07-16T19:03:01
======== ================ ==== ==============================================

Empty HDU.

HDU1
----

EXTNAME = FIBERQA

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== =================== ===== ==============================================
KEY      Example Value       Type  Comment
======== =================== ===== ==============================================
NAXIS1   124                 int   length of dimension 1
NAXIS2   5000                int   length of dimension 2
TILEID   20096               int
LASTNITE 20210608            int
NGOODFIB 3992                int
NGOODPET 9                   int
EFFTIME  214.8598327636719   float
VALID    T                   bool
RMSDIST  0.01416921149939299 float
TILERA   229.546             float
TILEDEC  -0.056              float
GOALTIME 180.0               float
GOALTYPE BRIGHT              str
FAPRGRM  bright              str
SURVEY   main                str
EBVFAC   1.12631027332157    float
MINTFRAC 0.85                float
CHECKSUM 73CQ71BN71BN71BN    str   HDU checksum updated 2021-07-16T19:03:01
DATASUM  105714500           str   data unit checksum updated 2021-07-16T19:03:01
======== =================== ===== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

============= ======= ===== ===========
Name          Type    Units Description
============= ======= ===== ===========
TARGETID      int64
PETAL_LOC     int16
DEVICE_LOC    int32
LOCATION      int64
FIBER         int32
TARGET_RA     float64
TARGET_DEC    float64
MEAN_FIBER_X  float32
MEAN_FIBER_Y  float32
MEAN_DELTA_X  float32
MEAN_DELTA_Y  float32
RMS_DELTA_X   float32
RMS_DELTA_Y   float32
DESI_TARGET   int64
BGS_TARGET    int64
EBV           float32
TSNR2_LRG     float64
Z             float64
SPECTYPE      char[6]
DELTACHI2     float64
QAFIBERSTATUS int32
EFFTIME_SPEC  float32
============= ======= ===== ===========

HDU2
----

EXTNAME = PETALQA

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   66               int  length of dimension 1
NAXIS2   10               int  length of dimension 2
CHECKSUM 5m3P8l1M5l1M5l1M str  HDU checksum updated 2021-07-16T19:03:01
DATASUM  807618843        str  data unit checksum updated 2021-07-16T19:03:01
======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

============== ======= ===== ===========
Name           Type    Units Description
============== ======= ===== ===========
PETAL_LOC      int16
WORSTREADNOISE float32
NGOODPOS       float32
NSTDSTAR       float32
STARRMS        float32
TSNR2FRA       float32
NCFRAME        float32
BSKYTHRURMS    float32
BSKYCHI2PDF    float32
RSKYTHRURMS    float32
RSKYCHI2PDF    float32
ZSKYTHRURMS    float32
ZSKYCHI2PDF    float32
BTHRUFRAC      float32
RTHRUFRAC      float32
ZTHRUFRAC      float32
EFFTIME_SPEC   float32
============== ======= ===== ===========


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
