=================
FVC-measure-EXPID
=================

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``FVC-measure-EXPID.fits``, where EXPID is the zero-padded
    8-digit exposure ID.
:Regex: ``FVC-measure-[0-9]{8}\.fits``
:File Type: FITS, 531 KB

Contents
========

====== ======== ======== ===================
Number EXTNAME  Type     Contents
====== ======== ======== ===================
HDU0_  PM       IMAGE    *Brief Description*
HDU1_  FVCCNTRD BINTABLE *Brief Description*
HDU2_  FVCCNTER BINTABLE *Brief Description*
====== ======== ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = PM

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ========================== ===== ==============================================
    KEY      Example Value              Type  Comment
    ======== ========================== ===== ==============================================
    NAXIS1   1                          int   length of data axis 1
    EXPID    51435                      int
    MODULE   FVCMEASURE                 str
    SEQUENCE FVC                        str
    MJD-OBS  58900.47012345             float
    NIGHT    20200220                   int
    DATE-OBS 2020-02-21T11:16:58.665928 str
    ST       13:53:58.630               str
    CHECKSUM 8B6A99338A3A8733           str   HDU checksum updated 2020-02-21T11:16:58
    DATASUM  1072693248                 str   data unit checksum updated 2020-02-21T11:16:58
    ======== ========================== ===== ==============================================

Data: FITS image [float64, 1]

HDU1
----

EXTNAME = FVCCNTRD

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   48               int  width of table in bytes
    NAXIS2   5406             int  number of rows in table
    EXPID    51435            int
    MODULE   FVCCENTROIDS     str
    CHECKSUM EiMfHgMZEgMdEgMZ str  HDU checksum updated 2020-02-21T11:16:58
    DATASUM  3879177035       str  data unit checksum updated 2020-02-21T11:16:58
    ======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

====== ======= ===== ===================
Name   Type    Units Description
====== ======= ===== ===================
mag    float64       label for field   1
serial int64         label for field   2
x      float64       label for field   3
fwhm   float64       label for field   4
flags  int64         label for field   5
y      float64       label for field   6
====== ======= ===== ===================

HDU2
----

EXTNAME = FVCCNTER

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   53               int  width of table in bytes
    NAXIS2   5088             int  number of rows in table
    EXPID    51435            int
    MODULE   FVCCENTERS       str
    CHECKSUM 380QA80Q480QA80Q str  HDU checksum updated 2020-02-21T11:16:58
    DATASUM  812294905        str  data unit checksum updated 2020-02-21T11:16:58
    ======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

======= ======= ===== ===================
Name    Type    Units Description
======= ======= ===== ===================
mag     float64       label for field   1
serial  int64         label for field   2
comment char[5]       label for field   3
x       float64       label for field   4
fwhm    float64       label for field   5
flags   int64         label for field   6
y       float64       label for field   7
======= ======= ===== ===================
