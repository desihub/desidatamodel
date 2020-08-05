===============
targets-\*.fits
===============

:Summary: DESI target selection files contain a single binary table covering the
    entire footprint.  They contain the variables used by target selection
    (*e.g.* fluxes), variables needed by fiber assignment (*e.g.* RA, DEC),
    and variables needed for traceability (*e.g.* TARGETFLAG, TARGETID).
:Naming Convention: TBD, let's try ``targets-{source}-{version}.fits`` where ``source`` is where the
    input data came from (*e.g.* 'dr1', 'dr2') and ``version`` is the code version
    that wrote this, preferably a git tag of desitargets.
:Regex: ``targets-dr[0-9]+-v?[0-9]+\.[0-9]+(\.[0-9]+|)\.fits``

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_  PRIMARY IMAGE    Blank
HDU1_  TARGETS BINTABLE Target selection table
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

Empty HDU.

HDU1
----

EXTNAME = TARGETS

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================================================== ==== ===================================
KEY      Example Value                                            Type Comment
======== ======================================================== ==== ===================================
EXTNAME  TARGETS                                                  str  name of this binary table extension
DEPNAM00 desitarget                                               str
DEPVER00 0.1.0                                                    str  desitarget.__version__
DEPNAM01 desitarget-git                                           str
DEPVAL01 0.1.0                                                    str  git revision
DEPNAM02 tractor-files                                            str
DEPVER02 /project/projectdirs/cosmo/data/legacysurvey/dr1/tractor str  input directory
======== ======================================================== ==== ===================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

===================== ========== ===== ===================
Name                  Type       Units Description
===================== ========== ===== ===================
BRICKID               int32            Brick ID from tractor input
BRICKNAME             char[8]          Brick name from tractor input
BRICK_OBJID           int32            OBJID (unique to brick, but not to file)
BRICK_PRIMARY         logical          should always be True
TYPE                  char[4]          tractor object type
RA                    float64          Right ascension [degrees]
RA_IVAR               float32          Inverse variance of RA
DEC                   float64          Declination [degrees]
DEC_IVAR              float32          Inverse variance of DEC
DECAM_FLUX            float32[6]       DECam flux from tractor input (ugrizY)
DECAM_MW_TRANSMISSION float32[6]       Milky Way dust transmission ([0-1] ugrizY)
WISE_FLUX             float32[4]       WISE flux (W1, W2, W3, W4)
WISE_MW_TRANSMISSION  float32[4]       Milky Way transmission
SHAPEEXP_R            float32          Half-light radius of exponential model (>0)
SHAPEDEV_R            float32          Half-light radius of deVaucouleurs model (>0)
TARGETID              int64            ID (unique to file and the whole survey)
DESI_TARGET           int64            DESI (dark time program) target selection bitmask
BGS_TARGET            int64            BGS (bright time program) target selection bitmask
MWS_TARGET            int64            MWS (bright time program) target selection bitmask
===================== ========== ===== ===================


Notes and Examples
==================

In general, the above format contains:

* Columns that were used by target selection (e.g. DECAM_FLUX)
* Columns needed by fiber assignment (e.g. RA, DEC)
* Columns needed for traceability (e.g. BRICKNAME, TARGETID, DESI_TARGET, BGS_TARGET, MWS_TARGET)

TARGETID, DESI_TARGET, BGS_TARGET and MWS_TARGET are created by target selection; the rest are passed through from the original input tractor files

See http://legacysurvey.org for more details about the columns from input tractor files
