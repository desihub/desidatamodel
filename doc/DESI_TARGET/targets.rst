===================
targets-DRX-VERSION
===================

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
HDU0_          IMAGE    Empty
HDU1_  TARGETS BINTABLE Target table
====== ======= ======== ============


FITS Header Units
=================

HDU0
----

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
NAXIS1   243                  int  width of table in bytes
NAXIS2   15050911             int  number of rows in table
EXTNAME  TARGETS              str  name of this binary table extension
DEPNAM00 desitarget           str
DEPVER00 0.14.0               str
DEPNAM01 desitarget-git       str
DEPVER01 unknown              str
DEPNAM02 sandboxcuts          str
DEPVER02 F                    bool sandbox cuts were used or not (T/F)
DEPNAM03 photcat              str
DEPVER03 dr4                  str
DEPNAM04 tractor-files        str
DEPVER04 /data/dr4/sweep/4.0/ str  Full path to input catalogs
DEPNAM05 qso-selection        str
DEPVER05 randomforest         str  QSO selection algorithm
DEPNAM06 HPXNSIDE             str
DEPVER06 64                   int
DEPNAM07 HPXNEST              str
DEPVER07 T                    bool
======== ==================== ==== ===================================

TODO: HPXNSIDE and HPXNEST should be regular keywords, not DEP* keywords.

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

================== ========== =============== ==================================
Name               Type       Units           Description
================== ========== =============== ==================================
RELEASE            int32                      label for column  1
BRICKID            int32                      Integer brick ID
BRICKNAME          char[8]                    String brick name
BRICK_OBJID        int32                      ObjectID on that brick
TYPE               char[4]                    PSF, SIMP, DEV, EXP
RA                 float64    deg             Right Ascension      
DEC                float64    deg             Declination
RA_IVAR            float32    1/deg2          Inverse variance of RA     
DEC_IVAR           float32    1/deg2          Inverse variance of dec     
DCHISQ             float32[5]                 
FLUX_G             float32    nanomaggies     g-band flux
FLUX_R             float32    nanomaggies     r-band flux      
FLUX_Z             float32    nanomaggies     z-band flux
FLUX_W1            float32    nanomaggies     WISE W1-band flux
FLUX_W2            float32    nanomaggies     WISE W2-band flux
FLUX_W3            float32    nanomaggies     WISE W3-band flux
FLUX_W4            float32    nanomaggies     WISE W4-band flux
FLUX_IVAR_G        float32    1/nanomaggies2  inverse variance of FLUX_G
FLUX_IVAR_R        float32    1/nanomaggies2  inverse variance of FLUX_R
FLUX_IVAR_Z        float32    1/nanomaggies2  inverse variance of FLUX_Z
FLUX_IVAR_W1       float32    1/nanomaggies2  inverse variance of FLUX_W1
FLUX_IVAR_W2       float32    1/nanomaggies2  inverse variance of FLUX_W2
FLUX_IVAR_W3       float32    1/nanomaggies2  inverse variance of FLUX_W3
FLUX_IVAR_W4       float32    1/nanomaggies2  inverse variance of FLUX_W4
MW_TRANSMISSION_G  float32                    Milky Way transmission in g
MW_TRANSMISSION_R  float32          
MW_TRANSMISSION_Z  float32          
MW_TRANSMISSION_W1 float32          
MW_TRANSMISSION_W2 float32          
MW_TRANSMISSION_W3 float32          
MW_TRANSMISSION_W4 float32          
NOBS_G             int16                      Number of g-band obs     
NOBS_R             int16                      Number of r-band obs  
NOBS_Z             int16                      Number of z-band obs
FRACFLUX_G         float32          
FRACFLUX_R         float32          
FRACFLUX_Z         float32          
PSFDEPTH_G         float32          
PSFDEPTH_R         float32          
PSFDEPTH_Z         float32          
GALDEPTH_G         float32          
GALDEPTH_R         float32          
GALDEPTH_Z         float32          
SHAPEDEV_R         float32          
SHAPEEXP_R         float32          
TARGETID           int64                      Unique target ID
DESI_TARGET        int64                      Dark + calib target selection bits
BGS_TARGET         int64                      Bright Galaxy Survey TS bits
MWS_TARGET         int64                      Milky Way Survey TS bits
HPXPIXEL           int64                      Healpixel ID (NESTED)
PHOTSYS            char[1]                    N or S
================== ========== =============== ==================================


Notes and Examples
==================

In general, the above format contains:

* Columns that were used by target selection (e.g. FLUX_G/R/Z)
* Columns needed by fiber assignment (e.g. RA, DEC)
* Columns needed for traceability (e.g. BRICKNAME, TARGETID, DESI_TARGET, BGS_TARGET, MWS_TARGET)

TARGETID, HPXPIXEL, PHOTSYS, DESI_TARGET, BGS_TARGET and MWS_TARGET are created by target selection; the rest are pass through from the original input tractor files

See http://legacysurvey.org for more details about the columns from input tractor files
