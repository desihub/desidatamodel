============
tilepix.fits
============

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``tilepix.fits``
:Regex: ``tilepix\.fits``
:File Type: FITS, 630 KB

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    *Brief Description*
HDU1_  TILEPIX BINTABLE *Brief Description*
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

*Summarize the contents of this HDU.*

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = TILEPIX

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============= ==== =====================
KEY      Example Value Type Comment
======== ============= ==== =====================
NAXIS1   9             int  length of dimension 1
NAXIS2   70894         int  length of dimension 2
HPXNSIDE 64            int
HPXNEST  T             bool
======== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

========= ======= ===== ===========
Name      Type    Units Description
========= ======= ===== ===========
TILEID    int32
PETAL_LOC logical
HEALPIX   int32
========= ======= ===== ===========


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
