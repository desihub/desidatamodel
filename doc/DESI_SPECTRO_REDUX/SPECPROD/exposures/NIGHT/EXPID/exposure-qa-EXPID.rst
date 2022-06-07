======================
exposure-qa-EXPID.fits
======================

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``exposure-qa-{expid}``, where ``{expid}``
    is the 8-digit exposure ID.
:Regex: ``exposure-qa-[0-9]{8}\.fits``
:File Type: FITS, 441 KB

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

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    CHECKSUM C4gFE4Z9C4fCC4Z9 str  HDU checksum updated 2021-07-16T14:31:54
    DATASUM  0                str  data unit checksum updated 2021-07-16T14:31:54
    ======== ================ ==== ==============================================

Empty HDU.

HDU1
----

EXTNAME = FIBERQA

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ============= =================== ===== ==============================================
    KEY           Example Value       Type  Comment
    ============= =================== ===== ==============================================
    NAXIS1        86                  int   length of dimension 1
    NAXIS2        5000                int   length of dimension 2
    NIGHT         20210514            int
    EXPID         88364               int
    NGOODFIB      4611                int
    NGOODPET      10                  int
    WORSTRDN      5.072375888924774   float
    FPRMS2D       0.01157238915902728 float
    PMINEXPF      0.8370916420971888  float
    PMAXEXPF      1.27911264193688    float
    EFFTIME       217.9705047607422   float
    TILEID        21181               int
    EXPTIME       589.277             float
    MJD-OBS       59349.20075297      float
    TARGTRA       199.993521          float
    TARGTDEC      32.447031           float
    MOUNTEL       84.320435           float
    MOUNTHA       -6.689017           float
    AIRMASS       1.004188            float
    TILERA        199.992             float
    TILEDEC       32.447              float
    GOALTIME [1]_ 180.0               float
    GOALTYPE [1]_ BRIGHT              str
    FAPRGRM [1]_  bright              str
    SURVEY [1]_   main                str
    EBVFAC [1]_   1.02512649227135    float
    MINTFRAC [1]_ 0.85                float
    CHECKSUM      YP2AYM16YM1AYM13    str   HDU checksum updated 2021-07-16T14:31:54
    DATASUM       2084006317          str   data unit checksum updated 2021-07-16T14:31:54
    ============= =================== ===== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

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
FIBER_X       float64
FIBER_Y       float64
DELTA_X       float64
DELTA_Y       float64
EBV           float32
QAFIBERSTATUS int32
EFFTIME_SPEC  float32
============= ======= ===== ===========

HDU2
----

EXTNAME = PETALQA

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   62               int  length of dimension 1
    NAXIS2   10               int  length of dimension 2
    CHECKSUM 8aaf9WRc8aXc8WXc str  HDU checksum updated 2021-07-16T14:31:54
    DATASUM  666368269        str  data unit checksum updated 2021-07-16T14:31:54
    ======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

============== ======= ===== ===========
Name           Type    Units Description
============== ======= ===== ===========
PETAL_LOC      int16
WORSTREADNOISE float32
NGOODPOS       int16
NGOODFIB       int16
NSTDSTAR       int16
STARRMS        float32
TSNR2FRA       float32
EFFTIME_SPEC   float32
NCFRAME        int16
BSKYTHRURMS    float32
BSKYCHI2PDF    float32
RSKYTHRURMS    float32
RSKYCHI2PDF    float32
ZSKYTHRURMS    float32
ZSKYCHI2PDF    float32
BTHRUFRAC      float32
RTHRUFRAC      float32
ZTHRUFRAC      float32
============== ======= ===== ===========

.. [1] Optional

Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
