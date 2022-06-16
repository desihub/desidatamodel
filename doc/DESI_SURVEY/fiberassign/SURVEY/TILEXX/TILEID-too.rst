===============
TILEID-too.fits
===============

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``{TILEID}-too.fits``, where ``{TILEID}`` is the zero-padded,
    6-digit TILED.
:Regex: ``[0-9]{6}-too\.fits``
:File Type: FITS, 19 KB

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    *Brief Description*
HDU1_  TARGETS BINTABLE *Brief Description*
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

EXTNAME = TARGETS

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ============= ======= =======================
    KEY      Example Value Type    Comment
    ======== ============= ======= =======================
    NAXIS1   223           int     width of table in bytes
    NAXIS2   1             int     number of rows in table
    SURVEY   main          str
    RESOLVE  T             bool
    MASKBITS T             bool
    BACKUP   F             bool
    NOSEC    F             bool
    DR       None          Unknown
    ======== ============= ======= =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

============================= ======== ========= ===================
Name                          Type     Units     Description
============================= ======== ========= ===================
RA                            float64  deg       label for field   1
DEC                           float64  deg       label for field   2
PMRA                          float64  mas / yr  label for field   3
PMDEC                         float64  mas / yr  label for field   4
REF_EPOCH                     float64  yr        label for field   5
FLUX_G                        float32  nanomaggy label for field   6
FLUX_R                        float32  nanomaggy label for field   7
FLUX_Z                        float32  nanomaggy label for field   8
PARALLAX                      float32  mas       label for field   9
GAIA_PHOT_G_MEAN_MAG          float32  mag       label for field  10
GAIA_PHOT_BP_MEAN_MAG         float32  mag       label for field  11
GAIA_PHOT_RP_MEAN_MAG         float32  mag       label for field  12
GAIA_ASTROMETRIC_EXCESS_NOISE float32            label for field  13
TARGETID                      int64              label for field  14
DESI_TARGET                   int64              label for field  15
SCND_TARGET                   int64              label for field  16
SCND_ORDER                    int32              label for field  17
PRIORITY_INIT                 int64              label for field  18
SUBPRIORITY                   float64            label for field  19
NUMOBS_INIT                   int64              label for field  20
OBSCONDITIONS                 int64              label for field  21
CHECKER                       char[5]            label for field  22
TOO_TYPE                      char[5]            label for field  23
TOO_PRIO                      char[2]            label for field  24
OCLAYER                       char[6]            label for field  25
MJD_BEGIN                     float64  d         label for field  26
MJD_END                       float64  d         label for field  27
TOOID                         int64              label for field  28
TIMESTAMP                     char[25] s         label for field  29
PLATE_RA                      float64            label for field  30
PLATE_DEC                     float64            label for field  31
PLATE_REF_EPOCH               float64            label for field  32
============================= ======== ========= ===================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
