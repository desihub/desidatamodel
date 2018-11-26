=======
planner
=======

:Summary: Cached state of the survey afternoon planner.
:Naming Convention: ``planner_YEAR-MM-DD.fits``, where ``YEAR-MM-DD`` is the
    date of the afternoon when the planner was run.
:Regex: ``planner_[0-9]{4}-[0-9]{2}-[0-9]{2}\.fits``
:File Type: FITS, 10 KB

Contents
========

====== ======= ======== =======================
Number EXTNAME Type     Contents
====== ======= ======== =======================
HDU0_          IMAGE    Keywords but blank data
HDU1_          BINTABLE Survey planner state
====== ======= ======== =======================

*TODO*: Add an EXTNAME for HDU 1.

FITS Header Units
=================

HDU0
----

*Summarize the contents of this HDU.*

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ============= ==== =====================
KEY     Example Value Type Comment
======= ============= ==== =====================
NAXIS1  25            int  length of dimension 1
NAXIS2  10            int  length of dimension 2
CADENCE daily         str
FIRST   2020-03-15    str
LAST    2020-03-15    str
======= ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

========= ======= ===== ===========
Name      Type    Units Description
========= ======= ===== ===========
COVERED   int64
COUNTDOWN int64
AVAILABLE logical
PRIORITY  float64
========= ======= ===== ===========


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
