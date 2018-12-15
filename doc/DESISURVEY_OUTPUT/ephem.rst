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
HDU1_  EPHEM   BINTABLE Ephemeris table
====== ======= ======== ===============

FITS Header Units
=================

HDU0
----

EXTNAME = (None)

Empty HDU.

HDU1
----

EXTNAME = EPHEM

Ephemeris table

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ================== ==== ===================================
KEY    Example Value      Type Comment
====== ================== ==== ===================================
NAXIS1 2920               int  length of dimension 1
NAXIS2 31                 int  length of dimension 2
NAME   Survey Ephemerides str
START  2020-03-15         str  Calculated ephemerides start on the evening of this date.
STOP   2020-04-15         str  Calculated ephemerides stop on the morning of this date.
====== ================== ==== ===================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

================= =========== ===== ===========
Name              Type        Units Description
================= =========== ===== ===========
noon              float64           MJD of local noon before night
dusk              float64           MJD of dark/gray sunset
dawn              float64           MJD of dark/gray sunrise
brightdusk        float64           MJD of bright sunset
brightdawn        float64           MJD of bright sunrise
brightdusk_LST    float64     deg   Apparent LST at brightdawn
brightdawn_LST    float64     deg   Apparent LST at brightdusk
moonrise          float64           MJD of moonrise before/during night
moonset           float64           MJD of moonset after/during night
moon_illum_frac   float64           Illuminated fraction of moon surface
nearest_full_moon float64           Nearest full moon - local midnight in days
programs          int16[4]          Program sequence between dusk and dawn (see notes)
changes           float64[3]        MJD of program changes between dusk and dawn
moon_ra           float64[25] deg   RA of moon tabulated during the night (see notes)
moon_dec          float64[25] deg   DEC of moon tabulated during the night (see notes)
venus_ra          float64[25] deg   RA of venus
venus_dec         float64[25] deg   DEC of venus
mars_ra           float64[25] deg   RA of mars
mars_dec          float64[25] deg   DEC of mars
jupiter_ra        float64[25] deg   RA of jupiter
jupiter_dec       float64[25] deg   DEC of jupiter
saturn_ra         float64[25] deg   RA of saturn
saturn_dec        float64[25] deg   DEC of saturn
neptune_ra        float64[25] deg   RA of neptune
neptune_dec       float64[25] deg   DEC of neptune
uranus_ra         float64[25] deg   RA of uranus
uranus_dec        float64[25] deg   DEC of uranus
================= =========== ===== ===========

Notes and Examples
==================

The default date range is chosen large enough to cover commissioning,
survey validation and the 5-year main survey, so should not normally need
to be changed.

The ``desisurvey`` package includes a `convenience wrapper <https://desisurvey.readthedocs.io/en/latest/api.html#desisurvey.ephem.get_ephem>`__
that should normally be used to access this file::

    import desisurvey.ephem
    ephem = desisurvey.ephem.get_ephem()

This wrapper implements memory and disk caching, for efficiency, and returns
an `Ephemerides <https://desisurvey.readthedocs.io/en/latest/api.html#desisurvey.ephem.Ephemerides>`__
with useful methods for working with the table data. If you need direct access to the
table use, for example::

    print(ephem.table[:10])

The integer codes used for the nightly program sequence are DARK=0, GRAY=1, BRIGHT=2.
Use program names where possible, instead of integer codes: the mapping between them
is defined in the ``desisurvey.tiles`` module::

    import desisurvey.tiles
    assert deisurvey.tiles.Tiles.PROGRAM_INDEX['GRAY'] == 1

RA, DEC coordinates for the moon and planets are tabulated on an hourly
grid spanning local noon - noon (inclusive, so 25 grid points) spanning each night.
You will normally want to interpolate these values using the `get_object_interpolator <https://desisurvey.readthedocs.io/en/latest/api.html#desisurvey.ephem.get_object_interpolator>`__
convenience method::

    night_ephem = ephem.get_night('2022-12-25')
    moon_altaz = desisurvey.ephem.get_object_interpolator(night_ephem, 'moon', altaz=True)
    alt, az = moon_altaz(mjd)

Note that you can either interpolate in (RA,DEC) or (Alt,Az).
