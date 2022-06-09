===========
targets-dr6
===========

:Summary: DESI target selection files contain a single binary table covering the
    entire footprint.  They contain the variables used by target selection
    (*e.g.* fluxes), variables needed by fiber assignment (*e.g.* RA, DEC),
    and variables needed for traceability (*e.g.* TARGETFLAG, TARGETID).
:Naming Convention: ``targets-DRX-VERSION.fits``, where ``DRX`` is the
    imaging surveys data release name (e.g. dr4) and ``VERSION`` is the
    desitarget code version defining the cuts.
:Regex: ``targets-dr[0-9]+-v?[0-9]+\.[0-9]+(\.[0-9]+|)\.fits``
:File Type: FITS, 3 GB

**Note**: this documents the target catalog format starting with DR4 /
desitarget 0.14.0 .  The previous format is documented in :doc:`targets-dr3`.

Contents
========

====== ======= ======== ============
Number EXTNAME Type     Contents
====== ======= ======== ============
HDU0_  PRIMARY IMAGE    Empty
HDU1_  TARGETS BINTABLE Target table
====== ======= ======== ============


FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

This HDU has no non-standard required keywords.

Empty HDU.


HDU1
----

EXTNAME = TARGETS

Target selection table

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================== ==== ===================================
KEY      Example Value        Type Comment
======== ==================== ==== ===================================
NAXIS1   176                  int  width of table in bytes
NAXIS2   15050911             int  number of rows in table
ENCODING ascii                str
SEED     1028862084           int  initial random seed
HPXNSIDE 64                   int  HEALPix nside
HPXNEST  T                    bool HEALPix nested (not ring) ordering
======== ==================== ==== ===================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

================== ======= ===== ===================
Name               Type    Units Description
================== ======= ===== ===================
BRICKID            int32         Brick ID from tractor input
BRICKNAME          char[8]       Brick name from tractor input
BRICK_OBJID        int32         OBJID (unique to brick, but not to file)
RA                 float64       Right ascension [degrees]
DEC                float64       Declination [degrees]
FLUX_G             float32       DECaLS flux from tractor input (g)
FLUX_R             float32       DECaLS flux from tractor input (r)
FLUX_Z             float32       DECaLS flux from tractor input (z)
FLUX_W1            float32       WISE flux in W1
FLUX_W2            float32       WISE flux in W2
MW_TRANSMISSION_G  float32       Milky Way dust transmission in DECaLS g
MW_TRANSMISSION_R  float32       Milky Way dust transmission in DECaLS r
MW_TRANSMISSION_Z  float32       Milky Way dust transmission in DECaLS z
MW_TRANSMISSION_W1 float32       Milky Way transmission in WISE W1
MW_TRANSMISSION_W2 float32       Milky Way transmission in WISE W2
PSFDEPTH_G         float32       PSF-based depth in DECaLS g
PSFDEPTH_R         float32       PSF-based depth in DECaLS r
PSFDEPTH_Z         float32       PSF-based depth in DECaLS z
GALDEPTH_G         float32       Model-based depth in DECaLS g
GALDEPTH_R         float32       Model-based depth in DECaLS r
GALDEPTH_Z         float32       Model-based depth in DECaLS z
PSFDEPTH_W1        float32       PSF-based depth in WISE W1
PSFDEPTH_W2        float32       PSF-based depth in WISE W2
SHAPEDEV_R         float32       Half-light radius of deVaucouleurs model (>0)
SHAPEDEV_E1        float32       Ellipticity parameter e1 of deVaucouleurs model
SHAPEDEV_E2        float32       Ellipticity parameter e2 of deVaucouleurs model
SHAPEEXP_R         float32       Half-light radius of exponential model (>0)
SHAPEEXP_E1        float32       Ellipticity parameter e1 of exponential model
SHAPEEXP_E2        float32       Ellipticity parameter e1 of exponential model
SUBPRIORITY        float64       Random subpriority [0-1] to break assignment ties
TARGETID           int64         Unique targeting ID
DESI_TARGET        int64         DESI (dark time program) target selection bitmask
BGS_TARGET         int64         BGS (bright time program) target selection bitmask
MWS_TARGET         int64         MWS (bright time program) target selection bitmask
HPXPIXEL           int64         HEALPixel containing target.
================== ======= ===== ===================

Notes and Examples
==================

In general, the above format contains:

* Columns that were used by target selection (e.g. FLUX_G/R/Z)
* Columns needed by fiber assignment (e.g. RA, DEC)
* Columns needed for traceability (e.g. BRICKNAME, TARGETID, DESI_TARGET, BGS_TARGET, MWS_TARGET)

TARGETID, HPXPIXEL, PHOTSYS, DESI_TARGET, BGS_TARGET and MWS_TARGET are created by target selection; the rest are passed through from the original input tractor files

See http://legacysurvey.org for more details about the columns from input tractor files
