=======
targets
=======

General Description
===================

Summary
-------

DESI target selection files contain a single binary table covering the
entire footprint.  They contain the variables used by target selection
(e.g. fluxes), variables needed by fiber assignment (e.g. RA, DEC),
and variables needed for traceability (e.g. TARGETFLAG, TARGETID).

Naming Convention
-----------------

TBD, let's try `targets-{source}-{version}.fits` where `source` is where the
input data came from (e.g. 'dr1', 'dr2') and `version` is the code version
that wrote this, preferably a git tag of desitargets.

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents           
====== ======= ======== ===================
HDU0_          IMAGE    Blank
HDU1_  TARGETS BINTABLE Target selection table
====== ======= ======== ===================


FITS Header Units
=================

HDU0 (Blank)
------------

HDU1 / TARGETS
--------------

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

=lf-light radius of deVaucouleurs model (>0)
==================== ========== ===== ===================
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
TARGETID              int64            Unique target ID
TARGETFLAG            int64            Target selection bitmask
NUMOBS                int32            Number of observations requested
===================== ========== ===== ===================


Notes and Examples
==================

NUMOBS may be deprecated in future versions.

In general, the above format contains:
* Columns that were used by target selection (e.g. DECAM_FLUX)
* Columns needed by fiber assignment (e.g. RA, DEC)
* Columns needed for traceability (e.g. BRICKNAME, TARGETID, TARGETFLAG)


TARGETID, TARGETFLAG, and NUMOBS are created by target selection; the rest are pass through from the original input tractor files

See http://legacysurvey.org for more details about the columns from input tractor files
