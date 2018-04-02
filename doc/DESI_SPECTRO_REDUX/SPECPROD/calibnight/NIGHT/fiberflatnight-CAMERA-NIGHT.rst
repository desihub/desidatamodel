==============
fiberflatnight
==============

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``fiberflatnight-r6-20200318.fits``, where ... *Give a human readable
    description of the filename, e.g. ``blat-{EXPID}`` where ``{EXPID}``
    is the 8-digit exposure ID.*
:Regex: ``fiberflatnight-r6-20200318.fits`` *Give a regular expression for this filename.
    For example, a six-digit number would correspond to ``[0-9]{6}``.*
:File Type: FITS, 10 MB  *This section gives the type of the file
    and its approximate size.*

Contents
========

====== ========== ======== ===================
Number EXTNAME    Type     Contents
====== ========== ======== ===================
HDU0_  FIBERFLAT  IMAGE    *Brief Description*
HDU1_  IVAR       IMAGE    *Brief Description*
HDU2_  MASK       BINTABLE *Brief Description*
HDU3_  MEANSPEC   IMAGE    *Brief Description*
HDU4_  WAVELENGTH IMAGE    *Brief Description*
====== ========== ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = FIBERFLAT

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================= ===== ==============================================
KEY      Example Value           Type  Comment
======== ======================= ===== ==============================================
NAXIS1   2645                    int
NAXIS2   500                     int
EXPID    25                      int
NIGHT    20200318                str
FLAVOR   flat                    str
DOSVER   SIM                     str
DATE-OBS 2020-03-18T22:00:00.000 str
EXPTIME  10.0                    float
FEEVER   SIM                     str
AIRORVAC vac                     str   Vacuum wavelengths
CAMERA   r6                      str
FIBERMIN 3000                    int
CHECKSUM 3GDaAE9W6ECaAE9U        str   HDU checksum updated 2018-03-29T21:38:41
DATASUM  2868401259              str   data unit checksum updated 2018-03-29T21:38:41
CHI2PDF  1.052080036564363       float
======== ======================= ===== ==============================================

Data: FITS image [float32, 2645x500]

HDU1
----

EXTNAME = IVAR

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2645             int
NAXIS2   500              int
CHECKSUM QedlRcbkQcbkQcbk str  HDU checksum updated 2018-03-29T21:38:41
DATASUM  2161531188       str  data unit checksum updated 2018-03-29T21:38:41
======== ================ ==== ==============================================

Data: FITS image [float32, 2645x500]

HDU2
----

EXTNAME = MASK

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   8                int  width of table in bytes
NAXIS2   500              int  number of rows in table
BSCALE   1                int
BZERO    2147483648       int
CHECKSUM LmE7NjE7LjE7LjE7 str  HDU checksum updated 2018-03-29T21:38:41
DATASUM  7014250          str  data unit checksum updated 2018-03-29T21:38:41
======== ================ ==== ==============================================

Data: FITS image [int32 (compressed), 8x500]

HDU3
----

EXTNAME = MEANSPEC

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2645             int
CHECKSUM 9bCFEZAF9bAFEZAF str  HDU checksum updated 2018-03-29T21:38:41
DATASUM  360710800        str  data unit checksum updated 2018-03-29T21:38:41
======== ================ ==== ==============================================

Data: FITS image [float32, 2645]

HDU4
----

EXTNAME = WAVELENGTH

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2645             int
BUNIT    Angstrom         str
CHECKSUM 7A46A9240A247724 str  HDU checksum updated 2018-03-29T21:38:41
DATASUM  1455388369       str  data unit checksum updated 2018-03-29T21:38:41
======== ================ ==== ==============================================

Data: FITS image [float32, 2645]


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
