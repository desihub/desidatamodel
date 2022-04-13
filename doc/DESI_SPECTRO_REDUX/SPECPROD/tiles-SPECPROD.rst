=====
tiles
=====

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``tiles-fuji.fits``, where ... *Give a human readable
    description of the filename, e.g. ``blat-{EXPID}`` where ``{EXPID}``
    is the 8-digit exposure ID.*
:Regex: ``tiles-fuji.fits`` *Give a regular expression for this filename.
    For example, a six-digit number would correspond to ``[0-9]{6}``.*
:File Type: FITS, 165 KB  *This section gives the type of the file
    and its approximate size.*

Contents
========

====== ================= ======== ===================
Number EXTNAME           Type     Contents
====== ================= ======== ===================
HDU0_                    IMAGE    *Brief Description*
HDU1_  TILE_COMPLETENESS BINTABLE *Brief Description*
====== ================= ======== ===================


FITS Header Units
=================

HDU0
----

*Summarize the contents of this HDU.*

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = TILE_COMPLETENESS

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =====================
KEY    Example Value Type Comment
====== ============= ==== =====================
NAXIS1 218           int  length of dimension 1
NAXIS2 732           int  length of dimension 2
====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

================== ======== ===== ===========
Name               Type     Units Description
================== ======== ===== ===========
TILEID             int32
SURVEY             char[20]
PROGRAM            char[6]
FAPRGRM            char[20]
FAFLAVOR           char[20]
NEXP               int64
EXPTIME            float64
TILERA             float64
TILEDEC            float64
EFFTIME_ETC        float64
EFFTIME_SPEC       float64
EFFTIME_GFA        float64
GOALTIME           float64
OBSSTATUS          char[20]
LRG_EFFTIME_DARK   float64
ELG_EFFTIME_DARK   float64
BGS_EFFTIME_BRIGHT float64
LYA_EFFTIME_DARK   float64
GOALTYPE           char[20]
MINTFRAC           float64
LASTNIGHT          int32
================== ======== ===== ===========


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*