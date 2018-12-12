===============
stats_surveysim
===============

:Summary: Survey statistics from a surveysim run.
:Naming Convention: ``stats_surveysim.fits``
:Regex: ``stats_surveysim.fits``
:File Type: FITS, 22 KB

*Note*: currently this is an output of surveysim, but in the future may become
an output of real operations survey QA.

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    *Brief Description*
HDU1_  STATS   BINTABLE *Brief Description*
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = (None)

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

===== ================= ==== =======
KEY   Example Value     Type Comment
===== ================= ==== =======
TILES ./test-tiles.fits str
START 2020-03-15        str
STOP  2020-04-15        str
===== ================= ==== =======

Empty HDU.

HDU1
----

EXTNAME = STATS

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ================= ==== =====================
KEY     Example Value     Type Comment
======= ================= ==== =====================
NAXIS1  448               int  length of dimension 1
NAXIS2  31                int  length of dimension 2
TILES   ./test-tiles.fits str
START   2020-03-15        str
STOP    2020-04-15        str
EXTNAME STATS             str  extension name
======= ================= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

============ ========== ===== ===========
Name         Type       Units Description
============ ========== ===== ===========
MJD          float64
tsched       float64
topen        float64[3]
tdead        float64[3]
tscience     float64[8]
tsetup       float64[8]
tsplit       float64[8]
completed    int32[8]
nexp         int32[8]
nsetup       int32[8]
nsplit       int32[8]
nsetup_abort int32[8]
nsplit_abort int32[8]
============ ========== ===== ===========


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
