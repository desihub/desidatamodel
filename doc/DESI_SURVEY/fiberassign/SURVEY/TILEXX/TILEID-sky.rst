===============
TILEID-sky.fits
===============

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``{TILEID}-sky.fits``, where ``{TILEID}`` is the zero-padded,
    6-digit TILED.
:Regex: ``[0-9]{6}-sky\.fits``
:File Type: FITS, 23 MB

Contents
========

====== =========== ======== ===================
Number EXTNAME     Type     Contents
====== =========== ======== ===================
HDU0_              IMAGE    *Brief Description*
HDU1_  SKY_TARGETS BINTABLE *Brief Description*
====== =========== ======== ===================


FITS Header Units
=================

HDU0
----

*Summarize the contents of this HDU.*

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = SKY_TARGETS

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =======================
    KEY    Example Value Type Comment
    ====== ============= ==== =======================
    NAXIS1 152           int  width of table in bytes
    NAXIS2 163775        int  number of rows in table
    SUPP   F             bool
    DR     9             int
    ====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

================ ======= ============= ===================
Name             Type    Units         Description
================ ======= ============= ===================
RELEASE          int32                 label for field   1
BRICKID          int32                 label for field   2
BRICKNAME        char[8]               label for field   3
BRICK_OBJID      int32                 label for field   4
RA               float64 deg           label for field   5
DEC              float64 deg           label for field   6
BLOBDIST         float32 pix           label for field   7
FIBERFLUX_G      float32 nanomaggy     label for field   8
FIBERFLUX_R      float32 nanomaggy     label for field   9
FIBERFLUX_Z      float32 nanomaggy     label for field  10
FIBERFLUX_IVAR_G float32 nanomaggy^-2  label for field  11
FIBERFLUX_IVAR_R float32 nanomaggy^-2  label for field  12
FIBERFLUX_IVAR_Z float32 nanomaggy^-2  label for field  13
TARGETID         int64                 label for field  14
DESI_TARGET      int64                 label for field  15
BGS_TARGET       int64                 label for field  16
MWS_TARGET       int64                 label for field  17
SUBPRIORITY      float64               label for field  18
OBSCONDITIONS    int64                 label for field  19
PRIORITY_INIT    int64                 label for field  20
NUMOBS_INIT      int64                 label for field  21
HPXPIXEL         int64                 label for field  22
PLATE_RA         float64               label for field  23
PLATE_DEC        float64               label for field  24
================ ======= ============= ===================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
