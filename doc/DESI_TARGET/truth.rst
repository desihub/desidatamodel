==========
truth.fits
==========

General Description
===================

:Summary: DESI Truth files contain binary tables describing the provenance
    of a target and its true properties. This file goes together with a
    mock target catalog.  Properties that apply to all targets (e.g. photometry)
    are in the `TRUTH` HDU, while template-specific truth values are in
    separate HDUs, e.g. `TRUTH_BGS`, `TRUTH_ELG`, `TRUTH_STAR`, etc.
:Naming Convention: TBD, let's try ``truth-{version}.fits`` where ``version``
    is the code version that wrote this, preferably a git tag of desitargets.
:Regex: ``truth-v?[0-9]+\.[0-9]+(\.[0-9]+|)\.fits``
:File Type: FITS, 28 MB

Contents
========

====== ========== ======== ============================
Number EXTNAME    Type     Contents
====== ========== ======== ============================
HDU0_  PRIMARY    IMAGE    Blank
HDU1_  TRUTH      BINTABLE Truth table
HDU2_  TRUTH_BGS  BINTABLE BGS-specific truth metadata
HDU3_  TRUTH_ELG  BINTABLE ELG-specific truth metadata
HDU4_  TRUTH_LRG  BINTABLE LRG-specific truth metadata
HDU5_  TRUTH_QSO  BINTABLE QSO-specific truth metadata
HDU6_  TRUTH_STAR BINTABLE STAR-specific truth metadata
HDU7_  TRUTH_WD   BINTABLE WD-specific truth metadata
====== ========== ======== ============================


FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

This HDU has no non-standard required keywords.

Empty HDU.


HDU1
----

EXTNAME = TRUTH

Target truth metadata for properties that apply to all targets.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============= ==== ===================================
KEY      Example Value Type Comment
======== ============= ==== ===================================
NAXIS1   118           int  width of table in bytes
NAXIS2   241273        int  number of rows in table
======== ============= ==== ===================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ======== ===== ===================
Name            Type     Units Description
=============== ======== ===== ===================
TARGETID        int64          ID (unique to file and the whole survey)
MOCKID          int64          Mock ID
CONTAM_TARGET   int64
TRUEZ           float64        True redshift in mock catalog (including peculiar velocity)
TRUESPECTYPE    char[10]       True object type in mock catalog
TEMPLATETYPE    char[10]
TEMPLATESUBTYPE char[10]
TEMPLATEID      int32
SEED            int64
MAG             float32
MAGFILTER       char[15]
FLUX_G          float32        DECaLS flux from tractor input (g)
FLUX_R          float32        DECaLS flux from tractor input (r)
FLUX_Z          float32        DECaLS flux from tractor input (z)
FLUX_W1         float32        WISE flux in W1
FLUX_W2         float32        WISE flux in W2
=============== ======== ===== ===================

HDU2
----

EXTNAME = TRUTH_BGS

Truth metadata for targets from BGS templates
(even if they were targeted as a different class).

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =======================
KEY    Example Value Type Comment
====== ============= ==== =======================
NAXIS1 56            int  width of table in bytes
NAXIS2 65748         int  number of rows in table
====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=========== ======= ===== ===================
Name        Type    Units Description
=========== ======= ===== ===================
TARGETID    int64         
OIIFLUX     float32       Flux in [OII] line
HBETAFLUX   float32       Flux in Hbeta line
EWOII       float32       
EWHBETA     float32       
D4000       float32       
VDISP       float32       Velocity dispersion
OIIDOUBLET  float32       
OIIIHBETA   float32       
OIIHBETA    float32       
NIIHBETA    float32       
SIIHBETA    float32       
TRUEZ_NORSD float32       
=========== ======= ===== ===================

HDU3
----

EXTNAME = TRUTH_ELG

Truth metadata for targets from ELG templates
(even if they were targeted as a different class).

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =======================
KEY    Example Value Type Comment
====== ============= ==== =======================
NAXIS1 56            int  width of table in bytes
NAXIS2 90286         int  number of rows in table
====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=========== ======= ===== ===================
Name        Type    Units Description
=========== ======= ===== ===================
TARGETID    int64         
OIIFLUX     float32       Flux in [OII] line
HBETAFLUX   float32       Flux in Hbeta line
EWOII       float32       
EWHBETA     float32       
D4000       float32       
VDISP       float32       Velocity dispersion
OIIDOUBLET  float32       
OIIIHBETA   float32       
OIIHBETA    float32       
NIIHBETA    float32       
SIIHBETA    float32       
TRUEZ_NORSD float32       
=========== ======= ===== ===================

HDU4
----

EXTNAME = TRUTH_LRG

Truth metadata for targets from LRG templates
(even if they were targeted as a different class).

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =======================
KEY    Example Value Type Comment
====== ============= ==== =======================
NAXIS1 56            int  width of table in bytes
NAXIS2 17444         int  number of rows in table
====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=========== ======= ===== ===================
Name        Type    Units Description
=========== ======= ===== ===================
TARGETID    int64         
OIIFLUX     float32       Flux in [OII] line
HBETAFLUX   float32       Flux in Hbeta line
EWOII       float32       
EWHBETA     float32       
D4000       float32       
VDISP       float32       
OIIDOUBLET  float32       
OIIIHBETA   float32       
OIIHBETA    float32       
NIIHBETA    float32       
SIIHBETA    float32       
TRUEZ_NORSD float32       
=========== ======= ===== ===================

HDU5
----

EXTNAME = TRUTH_QSO

Truth metadata for targets from QSO templates
(even if they were targeted as a different class).

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =======================
KEY    Example Value Type Comment
====== ============= ==== =======================
NAXIS1 782           int  width of table in bytes
NAXIS2 5391          int  number of rows in table
====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

============== ============ ===== ===================
Name           Type         Units Description
============== ============ ===== ===================
TARGETID       int64              
MABS_1450      float32            
SLOPES         float32[5]         
EMLINES        float32[186]       
BAL_TEMPLATEID int16              
TRUEZ_NORSD    float32            
============== ============ ===== ===================

HDU6
----

EXTNAME = TRUTH_STAR

Truth metadata for targets from stellar templates
(even if they were targeted as a different class).

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =======================
KEY    Example Value Type Comment
====== ============= ==== =======================
NAXIS1 20            int  width of table in bytes
NAXIS2 45222         int  number of rows in table
====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

======== ======= ===== ===================
Name     Type    Units Description
======== ======= ===== ===================
TARGETID int64         
TEFF     float32       Effective Temperature
LOGG     float32       Surface Gravity
FEH      float32       Metallicity
======== ======= ===== ===================

HDU7
----

EXTNAME = TRUTH_WD

Truth metadata for targets from White Dwarf (WD) templates
(even if they were targeted as a different class).

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =======================
KEY    Example Value Type Comment
====== ============= ==== =======================
NAXIS1 16            int  width of table in bytes
NAXIS2 175           int  number of rows in table
====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

======== ======= ===== ===================
Name     Type    Units Description
======== ======= ===== ===================
TARGETID int64         
TEFF     float32       Effective Temperature
LOGG     float32       Surface Gravity
======== ======= ===== ===================


Notes and Examples
==================

In general, the above tables contain:

* Columns needed for traceability (e.g. TARGETID, BRICKNAME)
* Columns needed by fiber assignment (e.g. RA, DEC)
* Columns mimicking results from the spectroscopic pipeline (e.g. TRUEZ, TRUETYPE)

This file is created by the targets.mock submodule.
