==========
surveyinit
==========

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``surveyinit.fits``, where ... *Give a human readable
    description of the filename, e.g. ``blat-{EXPID}`` where ``{EXPID}``
    is the 8-digit exposure ID.*
:Regex: ``surveyinit.fits`` *Give a regular expression for this filename.
    For example, a six-digit number would correspond to ``[0-9]{6}``.*
:File Type: FITS, 36 KB  *This section gives the type of the file
    and its approximate size.*

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    *Brief Description*
HDU1_  DARK    BINTABLE *Brief Description*
HDU2_  GRAY    BINTABLE *Brief Description*
HDU3_  BRIGHT  BINTABLE *Brief Description*
HDU4_  DESIGN  BINTABLE *Brief Description*
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ====================================================== ==== ==============
KEY      Example Value                                          Type Comment
======== ====================================================== ==== ==============
NAXIS1   31                                                     int
FIRST    2020-03-15                                             str
YEARS    2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017 str
START    2020-03-15                                             str
STOP     2020-04-15                                             str
TWILIGHT F                                                      bool
EXTNAME  WEATHER                                                str  extension name
======== ====================================================== ==== ==============

Data: FITS image [float64, 31]

HDU1
----

EXTNAME = DARK

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ============= ===== =====================
KEY     Example Value Type  Comment
======= ============= ===== =====================
NAXIS1  24            int   length of dimension 1
NAXIS2  192           int   length of dimension 2
ORIGIN  -60.0         float
EXTNAME DARK          str   extension name
======= ============= ===== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

===== ======= ===== ===========
Name  Type    Units Description
===== ======= ===== ===========
AVAIL float64
INIT  float64
PLAN  float64
===== ======= ===== ===========

HDU2
----

EXTNAME = GRAY

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ============= ===== =====================
KEY     Example Value Type  Comment
======= ============= ===== =====================
NAXIS1  24            int   length of dimension 1
NAXIS2  192           int   length of dimension 2
ORIGIN  -60.0         float
EXTNAME GRAY          str   extension name
======= ============= ===== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

===== ======= ===== ===========
Name  Type    Units Description
===== ======= ===== ===========
AVAIL float64
INIT  float64
PLAN  float64
===== ======= ===== ===========

HDU3
----

EXTNAME = BRIGHT

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ============= ===== =====================
KEY     Example Value Type  Comment
======= ============= ===== =====================
NAXIS1  24            int   length of dimension 1
NAXIS2  192           int   length of dimension 2
ORIGIN  -60.0         float
EXTNAME BRIGHT        str   extension name
======= ============= ===== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

===== ======= ===== ===========
Name  Type    Units Description
===== ======= ===== ===========
AVAIL float64
INIT  float64
PLAN  float64
===== ======= ===== ===========

HDU4
----

EXTNAME = DESIGN

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ============= ==== =====================
KEY     Example Value Type Comment
======= ============= ==== =====================
NAXIS1  24            int  length of dimension 1
NAXIS2  10            int  length of dimension 2
EXTNAME DESIGN        str  extension name
======= ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

==== ======= ===== ===========
Name Type    Units Description
==== ======= ===== ===========
INIT float64
HA   float64
TEXP float64
==== ======= ===== ===========


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
