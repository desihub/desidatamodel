=====
ephem
=====

:Summary: Cached ephemeris calculations for desisurvey.
:Naming Convention: ``ephem_YEAR-MM-DD_YEAR-MM-DD.fits``, where ``YEAR-MM-DD``
    are the first and last dates covered by this ephemeris cache.
:Regex: ``ephem_[0-9]{4}-[0-9]{2}-[0-9]{2}_[0-9]{4}-[0-9]{2}-[0-9]{2}\.fits``
:File Type: FITS, 100 KB

Contents
========

====== ======= ======== ===============
Number EXTNAME Type     Contents
====== ======= ======== ===============
HDU0_          IMAGE    Blank
HDU1_          BINTABLE Ephemeris table
====== ======= ======== ===============

*TODO*: Add an EXTNAME for HDU 1.

FITS Header Units
=================

HDU0
----

EXTNAME = (None)

Empty HDU.

HDU1
----

EXTNAME = (None)

Ephemeris table

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ================== ==== ===================================
KEY    Example Value      Type Comment
====== ================== ==== ===================================
NAXIS1 2920               int  length of dimension 1
NAXIS2 31                 int  length of dimension 2
NAME   Survey Ephemerides str
START  2020-03-15         str  First date of ephemeris calculation
STOP   2020-04-15         str  Last date of ephemeris calculations
====== ================== ==== ===================================

*TODO*: clarify if last day is inclusive

*TODO*: add an EXTNAME to the output

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

================= =========== ===== ===========
Name              Type        Units Description
================= =========== ===== ===========
noon              float64
dusk              float64
dawn              float64
brightdusk        float64
brightdawn        float64
brightdusk_LST    float64
brightdawn_LST    float64
moonrise          float64
moonset           float64
moon_illum_frac   float64
nearest_full_moon float64
programs          int16[4]
changes           float64[3]
moon_ra           float64[25] deg
moon_dec          float64[25] deg
venus_ra          float64[25] deg
venus_dec         float64[25] deg
mars_ra           float64[25] deg
mars_dec          float64[25] deg
jupiter_ra        float64[25] deg
jupiter_dec       float64[25] deg
saturn_ra         float64[25] deg
saturn_dec        float64[25] deg
neptune_ra        float64[25] deg
neptune_dec       float64[25] deg
uranus_ra         float64[25] deg
uranus_dec        float64[25] deg
================= =========== ===== ===========

*TODO*: what is the right unit for MJD days?  "day" isn't a valid FITS
standard unit.

*TODO*: clarify what MJD/date corresponds to the ra/dec values, e.g.
is that the RA/dec at noon, dusk, integer MJD, etc.

Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
