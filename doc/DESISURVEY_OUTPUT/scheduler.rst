=========
scheduler
=========

:Summary: Cached state of the next tile selector.
:Naming Convention: ``scheduler_YEAR-MM-DD.fits``, where ``YEAR-MM-DD`` is
    the date of the sunset (i.e. night) when the scheduler was run.
:Regex: ``scheduler_[0-9]{4}-[0-9]{2}-[0-9]{2}\.fits``
:File Type: FITS, 130 KB

Contents
========

====== ======= ===== ===================
Number EXTNAME Type  Contents
====== ======= ===== ===================
HDU0_  SCHED   IMAGE *Brief Description*
====== ======= ===== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = SCHED

Snapshot of the internal state of a `Scheduler object
<https://desisurvey.readthedocs.io/en/latest/api.html#desisurvey.scheduler.Scheduler>`__.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =======
KEY    Example Value Type Comment
====== ============= ==== =======
NAXIS1 16071         int  Length of dimension 1.
NIGHT  2020-03-15    str  Last night the scheduler was initialized for.
NDONE  3             int  Total number of completed tiles.
====== ============= ==== =======

Data: FITS image [float64, 16071]

The data is a 1D array of the integrated squared signal-to-noise ratio (SNR) accumulated on each tile so far, relative to the target value.  Tile indexing matches `desisurvey.tiles.Tiles 
<https://desisurvey.readthedocs.io/en/latest/api.html#desisurvey.tiles.Tiles>`__.

Notes and Examples
==================

A `Scheduler object <https://desisurvey.readthedocs.io/en/latest/api.html#desisurvey.scheduler.Scheduler>`__
schedules observations during each night::

    import desisurvey.scheduler
    scheduler = desisurvey.scheduler.Scheduler()

Its internal state after each afternoon can be saved using, for example::

    scheduler.save('scheduler_snapshot.fits')
    
This state can then be later restored using::

    scheduler = desisurvey.scheduler.Scheduler(restore='scheduler_snapshot.fits')
