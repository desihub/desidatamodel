================
TILEID-scnd.fits
================

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``{TILEID}-scnd.fits``, where ``{TILEID}`` is the zero-padded,
    6-digit TILED.
:Regex: ``[0-9]{6}-scnd\.fits``
:File Type: FITS, 1 MB

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
    NAXIS1   275           int     width of table in bytes
    NAXIS2   4751          int     number of rows in table
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

===================== ======== ========= ===================
Name                  Type     Units     Description
===================== ======== ========= ===================
FLUX_G                float32  nanomaggy label for field   1
FLUX_R                float32  nanomaggy label for field   2
FLUX_Z                float32  nanomaggy label for field   3
GAIA_PHOT_G_MEAN_MAG  float32  mag       label for field   4
GAIA_PHOT_BP_MEAN_MAG float32  mag       label for field   5
GAIA_PHOT_RP_MEAN_MAG float32  mag       label for field   6
TARGETID              int64              label for field   7
RA                    float64  deg       label for field   8
DEC                   float64  deg       label for field   9
PMRA                  float32  mas / yr  label for field  10
PMDEC                 float32  mas / yr  label for field  11
REF_EPOCH             float32  yr        label for field  12
PARALLAX              float32  mas       label for field  13
DESI_TARGET           int64              label for field  14
SCND_TARGET           int64              label for field  15
SUBPRIORITY           float64            label for field  16
OBSCONDITIONS         int32              label for field  17
PRIORITY_INIT         int64              label for field  18
NUMOBS_INIT           int64              label for field  19
BGS_TARGET            int64              label for field  20
MWS_TARGET            int64              label for field  21
NUMOBS_MORE           int64              label for field  22
NUMOBS                int64              label for field  23
Z                     float64            label for field  24
ZWARN                 int64              label for field  25
ZTILEID               int32              label for field  26
Z_QN                  float64            label for field  27
IS_QSO_QN             int16              label for field  28
DELTACHI2             float64            label for field  29
TARGET_STATE          char[30]           label for field  30
TIMESTAMP             char[25] s         label for field  31
VERSION               char[14]           label for field  32
PRIORITY              int64              label for field  33
PLATE_RA              float64            label for field  34
PLATE_DEC             float64            label for field  35
PLATE_REF_EPOCH       float32            label for field  36
===================== ======== ========= ===================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
