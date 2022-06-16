================
TILEID-targ.fits
================

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``{TILEID}-targ.fits``, where ``{TILEID}`` is the zero-padded,
    6-digit TILED.
:Regex: ``[0-9]{6}-targ\.fits``
:File Type: FITS, 11 MB

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
    NAXIS1   382           int     width of table in bytes
    NAXIS2   30866         int     number of rows in table
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

===================== ======== ============= ===================
Name                  Type     Units         Description
===================== ======== ============= ===================
RELEASE               int16                  label for field   1
BRICKID               int32                  label for field   2
BRICKNAME             char[8]                label for field   3
BRICK_OBJID           int32                  label for field   4
MORPHTYPE             char[4]                label for field   5
EBV                   float32  mag           label for field   6
FLUX_G                float32  nanomaggy     label for field   7
FLUX_R                float32  nanomaggy     label for field   8
FLUX_Z                float32  nanomaggy     label for field   9
FLUX_IVAR_G           float32  nanomaggy^-2  label for field  10
FLUX_IVAR_R           float32  nanomaggy^-2  label for field  11
FLUX_IVAR_Z           float32  nanomaggy^-2  label for field  12
FLUX_W1               float32  nanomaggy     label for field  13
FLUX_W2               float32  nanomaggy     label for field  14
FLUX_IVAR_W1          float32  nanomaggy^-2  label for field  15
FLUX_IVAR_W2          float32  nanomaggy^-2  label for field  16
FIBERFLUX_G           float32  nanomaggy     label for field  17
FIBERFLUX_R           float32  nanomaggy     label for field  18
FIBERFLUX_Z           float32  nanomaggy     label for field  19
FIBERTOTFLUX_G        float32  nanomaggy     label for field  20
FIBERTOTFLUX_R        float32  nanomaggy     label for field  21
FIBERTOTFLUX_Z        float32  nanomaggy     label for field  22
MASKBITS              int16                  label for field  23
SHAPE_R               float32                label for field  24
SHAPE_E1              float32                label for field  25
SHAPE_E2              float32                label for field  26
SERSIC                float32                label for field  27
REF_ID                int64                  label for field  28
REF_CAT               char[2]                label for field  29
GAIA_PHOT_G_MEAN_MAG  float32  mag           label for field  30
GAIA_PHOT_BP_MEAN_MAG float32  mag           label for field  31
GAIA_PHOT_RP_MEAN_MAG float32  mag           label for field  32
PHOTSYS               char[1]                label for field  33
TARGETID              int64                  label for field  34
RA                    float64  deg           label for field  35
DEC                   float64  deg           label for field  36
REF_EPOCH             float32  yr            label for field  37
PARALLAX              float32  mas           label for field  38
PMRA                  float32  mas / yr      label for field  39
PMDEC                 float32  mas / yr      label for field  40
DESI_TARGET           int64                  label for field  41
BGS_TARGET            int64                  label for field  42
MWS_TARGET            int64                  label for field  43
SUBPRIORITY           float64                label for field  44
OBSCONDITIONS         int32                  label for field  45
PRIORITY_INIT         int64                  label for field  46
NUMOBS_INIT           int64                  label for field  47
SCND_TARGET           int64                  label for field  48
NUMOBS_MORE           int64                  label for field  49
NUMOBS                int64                  label for field  50
Z                     float64                label for field  51
ZWARN                 int64                  label for field  52
ZTILEID               int32                  label for field  53
Z_QN                  float64                label for field  54
IS_QSO_QN             int16                  label for field  55
DELTACHI2             float64                label for field  56
TARGET_STATE          char[30]               label for field  57
TIMESTAMP             char[25] s             label for field  58
VERSION               char[14]               label for field  59
PRIORITY              int64                  label for field  60
PLATE_RA              float64                label for field  61
PLATE_DEC             float64                label for field  62
PLATE_REF_EPOCH       float32                label for field  63
===================== ======== ============= ===================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
