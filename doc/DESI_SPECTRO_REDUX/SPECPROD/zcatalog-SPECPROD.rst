=================
zcatalog-SPECPROD
=================

:Summary: This file concatenates all
    :doc:`zbest <./spectra-NSIDE/PIXGROUP/PIXNUM/zbest-NSIDE-PIXNUM>` files
    and then cross matches them with the input target catalog.
:Naming Convention: ``zcatalog-{SPECPROD}.fits``, where ``{SPECPROD}`` is the
    :envvar:`SPECPROD` name of the reduction run.
:Regex: ``zcatalog-[a-z0-9_-]+\.fits``
:File Type: FITS, 14 MB

Contents
========

====== ======== ======== ===========================================
Number EXTNAME  Type     Contents
====== ======== ======== ===========================================
HDU0_  PRIMARY  IMAGE    Empty
HDU1_  ZCATALOG BINTABLE Redshift catalog joined with target catalog
====== ======== ======== ===========================================


FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = ZCATALOG

The concatenated redshift data for all
:doc:`zbest <./spectra-NSIDE/PIXGROUP/PIXNUM/zbest-NSIDE-PIXNUM>` files,
cross matched with the original input target catalog.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =================================
KEY    Example Value Type Comment
====== ============= ==== =================================
NAXIS1 332           int  width of table in bytes
NAXIS2 44215         int  number of targets (rows) in table
====== ============= ==== =================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

================== =========== ===== ===================
Name               Type        Units Description
================== =========== ===== ===================
TARGETID           int64             label for field   1
CHI2               float64           label for field   2
COEFF              float64[10]       label for field   3
Z                  float64           label for field   4
ZERR               float64           label for field   5
ZWARN              int64             label for field   6
NPIXELS            int64             label for field   7
SPECTYPE           char[6]           label for field   8
SUBTYPE            char[6]           label for field   9
NCOEFF             int64             label for field  10
DELTACHI2          float64           label for field  11
BRICKNAME          char[8]           label for field  12
NUMEXP             int32             label for field  13
NUMTILE            int32             label for field  14
BRICKID            int32             label for field  15
BRICK_OBJID        int32             label for field  16
RA                 float64           label for field  17
DEC                float64           label for field  18
FLUX_G             float32           label for field  19
FLUX_R             float32           label for field  20
FLUX_Z             float32           label for field  21
FLUX_W1            float32           label for field  22
FLUX_W2            float32           label for field  23
MW_TRANSMISSION_G  float32           label for field  24
MW_TRANSMISSION_R  float32           label for field  25
MW_TRANSMISSION_Z  float32           label for field  26
MW_TRANSMISSION_W1 float32           label for field  27
MW_TRANSMISSION_W2 float32           label for field  28
PSFDEPTH_G         float32           label for field  29
PSFDEPTH_R         float32           label for field  30
PSFDEPTH_Z         float32           label for field  31
GALDEPTH_G         float32           label for field  32
GALDEPTH_R         float32           label for field  33
GALDEPTH_Z         float32           label for field  34
PSFDEPTH_W1        float32           label for field  35
PSFDEPTH_W2        float32           label for field  36
SHAPEDEV_R         float32           label for field  37
SHAPEDEV_E1        float32           label for field  38
SHAPEDEV_E2        float32           label for field  39
SHAPEEXP_R         float32           label for field  40
SHAPEEXP_E1        float32           label for field  41
SHAPEEXP_E2        float32           label for field  42
SUBPRIORITY        float64           label for field  43
DESI_TARGET        int64             label for field  44
BGS_TARGET         int64             label for field  45
MWS_TARGET         int64             label for field  46
HPXPIXEL           int64             label for field  47
================== =========== ===== ===================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
