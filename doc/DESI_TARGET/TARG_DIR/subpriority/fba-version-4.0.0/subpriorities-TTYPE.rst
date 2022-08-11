==================
supplemental skies
==================

:Summary: The subpriority files are single binary tables that include the fixed
    values of subpriority enforced for Main Survey targets. There is one file
    for each of dark-time and bright-time targets, and one for blank sky locations.
:Naming Convention: ``subpriorities-TTYPE.fits``,
    where ``TTYPE`` is one of ``dark``, ``bright`` or ``sky``.
:Regex: ``subpriorities-[a-zA-Z]+\.fits``
:File Type: FITS, 41 - 360 MB

Contents
========

====== =========== ======== ===================
Number EXTNAME     Type     Contents
====== =========== ======== ===================
HDU0_  PRIMARY     IMAGE    Empty
HDU1_  SUBPRIORITY BINTABLE Per-target SUBPRIORITY values
====== =========== ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = SUBPRIORITY

Per-target SUBPRIORITY values

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ============= ===== =================================
    KEY      Example Value Type  Comment
    ======== ============= ===== =================================
    NAXIS1   24            int   width of table in bytes
    NAXIS2   2026104       int   number of rows in table
    FAPRGRM  "bright"      str   one of "dark", "bright" or "sky"
    INFIL000 "$DESI_ROOT/" str   zeroth fiberassign file/tile for which fixed SUBPRIORITY values need to be enforced
    INFIL001 "$DESI_ROOT/" str   first fiberassign file/tile for which fixed SUBPRIORITY values need to be enforced
    INFILxxx "$DESI_ROOT/" str   etc.
    ======== ============= ===== =================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

============= ========== ======= ===================
Name          Type       Units   Description
============= ========== ======= ===================
TARGETID      int64              Unique targeting ID
SUBPRIORITY   float64            Random subpriority [0-1] to break assignment ties
DESI_TARGET   int64              DESI (dark time program) target selection bitmask
============= ========== ======= ===================
