=======
planner
=======

:Summary: Cached state of the survey afternoon planner.
:Naming Convention: ``planner_YEAR-MM-DD.fits``, where ``YEAR-MM-DD`` is the
    date of the afternoon when the planner was run.
:Regex: ``planner_[0-9]{4}-[0-9]{2}-[0-9]{2}\.fits``
:File Type: FITS, 400 KB

Contents
========

====== ======= ======== =======================
Number EXTNAME Type     Contents
====== ======= ======== =======================
HDU0_          IMAGE    Blank.
HDU1_  PLAN    BINTABLE Survey planner state.
====== ======= ======== =======================

FITS Header Units
=================

HDU0
----

EXTNAME = (None)

Empty HDU.

HDU1
----

EXTNAME = PLAN

Snapshot of the internal state of a `desisurvey.plan.Planner
<https://desisurvey.readthedocs.io/en/latest/api.html#desisurvey.plan.Planner>`__
object.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ============= ==== =====================
KEY     Example Value Type Comment
======= ============= ==== =====================
NAXIS1  29            int  length of dimension 1.
NAXIS2  16071         int  length of dimension 2.
CADENCE monthly       str  Fiber assignment cadence (monthly / daily).
FIRST   2019-12-01    str  First night that was planned.
LAST    2024-11-29    str  Last night that has been planned so far.
======= ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

========= ======= ===== ===========
Name      Type    Units Description
========= ======= ===== ===========
TILEID    int64         Tile ID from the tiles file.
COVERED   int64         Day number that tile was first covered relative to ``FIRST`` or -1.
COUNTDOWN int64         Countdown of remaining fiber assignment cycles until this tile will be assigned.
AVAILABLE logical       Does this tile have fibers already assigned?
PRIORITY  float64       Relative priority for scheduling this tile. Must be >= 0.
========= ======= ===== ===========

The meaning of "covered" is specified by the ``fiber_assignment_order`` configuration parameter,
which also specifies the starting ``COUNTDOWN`` value for each pass.

Each row of the table corresponds to one tile with indexing that matches `desisurvey.tiles.Tiles 
<https://desisurvey.readthedocs.io/en/latest/api.html#desisurvey.tiles.Tiles>`__.

Notes and Examples
==================

A `Planner object
<https://desisurvey.readthedocs.io/en/latest/api.html#desisurvey.plan.Planner>`__
manages updates during afternoon planning::

    import desisurvey.rules
    import desisurvey.plan
    rules = desisurvey.rules.Rules()
    planner = desisurvey.plan.Planner(rules)

Its internal state after each afternoon can be saved using, for example::

    planner.save('planner_snapshot.fits')

This state can then be later restored using::

    planner = desisurvey.plan.Planner(rules, restore='planner_snapshot.fits')
