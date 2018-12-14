==========
surveyinit
==========

:Summary: Design hour angles calculated during survey initialization.
:Naming Convention: ``surveyinit.fits``
:Regex: ``surveyinit.fits``
:File Type: FITS, 36 KB

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_  WEATHER IMAGE    Nightly dome-open fractions assumed to calculate available LST.
HDU1_  DARK    BINTABLE Summary of hour angle optimization for the DARK program.
HDU2_  GRAY    BINTABLE Summary of hour angle optimization for the GRAY program.
HDU3_  BRIGHT  BINTABLE Summary of hour angle optimization for the BRIGHT program.
HDU4_  DESIGN  BINTABLE Design hours angles for all programs.
====== ======= ======== ===================

FITS Header Units
=================

HDU0
----

EXTNAME = WEATHER

Nightly dome-open fractions due to weather that are are assumed when calculating
the available LST per program, as in input to the design hour-angle optimization.
These are obtained 

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ====================================================== ==== ==============
KEY      Example Value                                          Type Comment
======== ====================================================== ==== ==============
NAXIS1   2556                                                   int  Length of dimension 1.
FIRST    2019-01-01                                             str  Date of the first tabulated night.
YEARS    2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017 str  List of years averaged to calculate predicted dome-open fractions.
START    2019-12-01                                             str  Nominal survey start date used for hour-angle optimization.
STOP     2024-11-30                                             str  Nominal survey stop date used for hour-angle optimization.
TWILIGHT F                                                      bool Was twilight included in the BRIGHT program schedule for optimzation?
======== ====================================================== ==== ==============

Data: FITS image [float64, 2556]

The HDU data consists of a 1D array of dome-open fractions estimated by averaging historical weather data. The value at index ``K`` corresponds to the night of ``FIRST`` plus ``K`` days.  Note that dome-open fractions are tabulated for an extended date range
that covers the nominal survey dates but also commissioning and survey validation.

HDU1
----

EXTNAME = DARK

Summary of hour angle optimization for the DARK program.

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
