=====
stats
=====

:Summary: Nightly summary statistics, recorded by pass, from a surveysim run.
:Naming Convention: ``stats_surveysim.fits``
:Regex: ``stats_surveysim\.fits``
:File Type: FITS, 810 KB

*Note*: currently this is an output of surveysim, but in the future may become
an output of real operations survey QA.

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    Blank.
HDU1_  STATS   BINTABLE Nighly summary statistics by pass.
====== ======= ======== ===================

FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

Empty HDU.

HDU1
----

EXTNAME = STATS

Survey summary statistics by pass.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ================= ==== =====================
KEY     Example Value     Type Comment
======= ================= ==== =====================
NAXIS1  1826              int  length of dimension 1
NAXIS2  13                int  length of dimension 2
TILES   desi-tiles.fits   str  Name of the tiles file specified in desisurvey config.
START   2020-03-15        str  YEAR-MM-YY of the first night of the survey.
STOP    2020-04-15        str  YEAR-MM-YY of the most recent night with statistics recorded.
======= ================= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

============ ========== ===== ===========
Name         Type       Units Description
============ ========== ===== ===========
MJD          float64          MJD of local noon before this night.
tsched       float64    d     Total scheduled time for all programs during this night.
topen        float64[3] d     Actual time dome was open during this night, per program.
tdead        float64[3] d     Deadtime during this night (dome open, but idling), per program.
tscience     float64[8] d     Time spent with the shutter open for science exposures, per pass.
tsetup       float64[8] d     Time spent setting up to observe a new field, per pass.
tsplit       float64[8] d     Time spent setting up to reobserve the previous field, per pass.
completed    int32[8]   d     Number of tiles completed this night, per pass.
nexp         int32[8]   d     Number of exposures recorded this night, per pass.
nsetup       int32[8]   d     Number of setups to observe a new field, per pass.
nsplit       int32[8]   d     Number of setups to re-observe a previous field, per pass.
nsetup_abort int32[8]   d     Number of times a new field setup was aborted, per pass.
nsplit_abort int32[8]   d     Number of times a repeat field setup was aborted, per pass.
============ ========== ===== ===========

The table contains one row per night, with row ``N`` corresponding to ``N`` nights after the header ``START`` date.

All timing statistics are in units of days.

The ``topen`` and ``tdead`` arrays are indexed by the number of programs, which are defined in the `tiles module
<https://desisurvey.readthedocs.io/en/latest/api.html#desisurvey.tiles.Tiles.PROGRAMS>`__. There will always be
space for all three programs (DARK, GRAY, BRIGHT), even when using a custom tiles file with fewer programs
actually used.

The remaining arrays are indexed by the number of passes, which depends on the actual tiles file being used.
In general, a tiles file uses arbitrary pass numbering, which might not be dense or consecutive for each program.
The `Tiles object <https://desisurvey.readthedocs.io/en/latest/api.html#desisurvey.tiles.Tiles>`__
defines data structures to map the indices used here to the pass numbers and programs used in the tiles file.

Notes and Examples
==================

A `SurveyStatistics
<https://surveysim.readthedocs.io/en/latest/api.html#surveysim.stats.SurveyStatistics>`__
object tracks survey statistics during simulation::

    import surveysim.stats
    stats = surveysim.stats.SurveyStatistics()

Its internal state after a simulation (or each night) can be saved using, for example::

    stats.save('stats.fits', comment='Baseline (seed=1)')

This state can then later be restored using::

    stats = surveysim.stats.SurveyStatistics(restore='stats.fits')
