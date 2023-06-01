=================
FVC-measure-EXPID
=================

:Summary: This file type is found in early commissioning data, but should
    be considered obsolete.
:Naming Convention: ``FVC-measure-EXPID.fits``, where EXPID is the zero-padded
    8-digit exposure ID.
:Regex: ``FVC-measure-[0-9]{8}\.fits``
:File Type: FITS, 531 KB

Contents
========

====== ======== ======== ===================
Number EXTNAME  Type     Contents
====== ======== ======== ===================
HDU0_  PM       IMAGE    TODO: description needed
HDU1_  FVCCNTRD BINTABLE TODO: description needed
HDU2_  FVCCNTER BINTABLE TODO: description needed
====== ======== ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = PM

TODO: description needed

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

TODO: description needed

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
mag    float64       TODO: description needed
serial int64         TODO: description needed
x      float64       TODO: description needed
fwhm   float64       TODO: description needed
flags  int64         TODO: description needed
y      float64       TODO: description needed
====== ======= ===== ===================

HDU2
----

EXTNAME = FVCCNTER

TODO: description needed

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
mag     float64       TODO: description needed
serial  int64         TODO: description needed
comment char[5]       TODO: description needed
x       float64       TODO: description needed
fwhm    float64       TODO: description needed
flags   int64         TODO: description needed
y       float64       TODO: description needed
======= ======= ===== ===================
