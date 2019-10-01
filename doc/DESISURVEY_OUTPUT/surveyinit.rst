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
the available LST per program, as an input to the design hour-angle optimization.

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

The HDU data consists of a 1D array of dome-open fractions estimated by averaging `historical weather data
<https://desimodel.readthedocs.io/en/latest/#desimodel.weather.dome_closed_fractions>`__.
The value at index ``K`` corresponds to the night of ``FIRST`` plus ``K`` days.  Note that dome-open fractions
are tabulated for an extended date range that covers the nominal survey dates but also commissioning and survey validation.

Use `load_weather <https://desisurvey.readthedocs.io/en/latest/api.html#desisurvey.plan.load_weather>`__
to read the dome-open fractions as a 1D array, optionally sliced to a specified range of dates.

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
ORIGIN  -60.0         float Low edge of first LST histogram bin in degrees.
======= ============= ===== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

===== ======= ===== ===========
Name  Type    Units Description
===== ======= ===== ===========
AVAIL float64       Histogram of available LST in the DARK program.
INIT  float64       Histogram of initial LST usage, before optimization.
PLAN  float64       Histogram of planned LST usage, after optimization.
===== ======= ===== ===========

Histograms are normalized to the (dimensionless) units of sidereal hours per LST bin integrated over the survey.

HDU2
----

EXTNAME = GRAY

Summary of hour angle optimization for the GRAY program.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ============= ===== =====================
KEY     Example Value Type  Comment
======= ============= ===== =====================
NAXIS1  24            int   length of dimension 1
NAXIS2  192           int   length of dimension 2
ORIGIN  -60.0         float Low edge of first LST histogram bin in degrees.
======= ============= ===== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

===== ======= ===== ===========
Name  Type    Units Description
===== ======= ===== ===========
AVAIL float64       Histogram of available LST in the GRAY program.
INIT  float64       Histogram of initial LST usage, before optimization.
PLAN  float64       Histogram of planned LST usage, after optimization.
===== ======= ===== ===========

Histograms are normalized to the (dimensionless) units of sidereal hours per LST bin integrated over the survey.

HDU3
----

EXTNAME = BRIGHT

Summary of hour angle optimization for the BRIGHT program.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ============= ===== =====================
KEY     Example Value Type  Comment
======= ============= ===== =====================
NAXIS1  24            int   length of dimension 1
NAXIS2  192           int   length of dimension 2
ORIGIN  -60.0         float Low edge of first LST histogram bin in degrees.
======= ============= ===== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

===== ======= ===== ===========
Name  Type    Units Description
===== ======= ===== ===========
AVAIL float64       Histogram of available LST in the BRIGHT program.
INIT  float64       Histogram of initial LST usage, before optimization.
PLAN  float64       Histogram of planned LST usage, after optimization.
===== ======= ===== ===========

Histograms are normalized to the (dimensionless) units of sidereal hours per LST bin integrated over the survey.

HDU4
----

EXTNAME = DESIGN

Optimized design hour angles for each tile in all programs.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ============= ==== =====================
KEY     Example Value Type Comment
======= ============= ==== =====================
NAXIS1  16071         int  length of dimension 1
NAXIS2  10            int  length of dimension 2
======= ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

==== ======= ===== ===========
Name Type    Units Description
==== ======= ===== ===========
INIT float64 deg   Initial hour angles before optimization.
HA   float64 deg   Final hour angles after optimization.
TEXP float64 s     Irreducible exposure time due to dust extinction and airmass at the design hour angle.
==== ======= ===== ===========

Each row of the table corresponds to one tile with indexing that matches ``desisurvey.tiles.Tiles``.

Use `load_design_hourangle
<https://desisurvey.readthedocs.io/en/latest/api.html#desisurvey.plan.load_weather>`__ to read
the ``HA`` column as a 1D array.

Notes and Examples
==================

The histograms of available LST in each program are calculated by `get_available_lst
<https://desisurvey.readthedocs.io/en/latest/api.html#desisurvey.ephem.Ephemerides.get_available_lst>`__.

Hour angle optimization is performed by `desisurvey.optimize.Optimizer
<https://desisurvey.readthedocs.io/en/latest/api.html#desisurvey.optimize.Optimizer>`__ and documented
in `DESI-3060 <https://desi.lbl.gov/DocDB/cgi-bin/private/ShowDocument?docid=3060>`__.
