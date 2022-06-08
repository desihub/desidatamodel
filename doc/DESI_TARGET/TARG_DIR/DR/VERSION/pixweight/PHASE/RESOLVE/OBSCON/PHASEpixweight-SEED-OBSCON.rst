=========
pixweight
=========

:Summary: DESI HEALPixel weight files contain a single binary table covering the 
    entire Legacy Surveys footprint. They contain meta information (the number of
    observations, the depth, etc.) derived from pixels in Legacy Surveys CCDs,
    together with target densities, conveniently stored as HEALPixel maps. They are 
    derived from corresponding DESI random catalogs and target files, which are
    listed in the README file in the parent `pixweight` directory.
:Naming Convention: ``PHASEpixweight-SEED-obscon.fits``,
          where ``PHASE`` is a specific DESI observational phase (*e.g.* svX with X=1,2,3
	  for iterations of Survey Validation) ``OBSCON`` is the observing condition
	  (or "layer") for the targets (*e.g.* dark), and ``SEED`` is the random seed used
	  to generate the associated random catalog. ``PHASE`` is omitted for Main Survey
	  catalogs.
:Regex: ``.*?pixweight-[0-9]+-[a-zA-Z]+\.fits``
:File Type: FITS, 100 MB

Contents
========

====== ========== ======== ===================
Number EXTNAME    Type     Contents
====== ========== ======== ===================
HDU0_  PRIMARY    IMAGE    Empty
HDU1_  PIXWEIGHTS BINTABLE pixweight catalog table
====== ========== ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = PIXWEIGHTS

Random catalog table

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============= ===== ========================================
KEY      Example Value Type  Comment
======== ============= ===== ========================================
NAXIS1   132           int   Width of table in bytes
NAXIS2   786432        int   Number of rows in table
FILENSID 2             int   HEALPix nside covered by file
FILENEST T             bool  HEALPix nested (not ring) ordering
FILEHPX  "11,5,4"      str   HEALPix pixel(s) covered by file
DR       9             int   `Legacy Surveys`_ (LS) Data Release used to generate randoms
DENSITY  45000         int   Number of random points generated per sq. deg.
APRAD    0.75          float Aperture radius used to calculate flux-related quantities (arcsec)
SEED     1             int   Seed used to generate random catalog
ADDMTL   F             bool  ``True`` if MTL-related columns were added to the parent catalog used to build this catalog
HPXNSIDE 64            int   HEALPix nside
HPXNEST  T             bool  HEALPix nested (not ring) ordering
SUPP     F             bool  ``True`` if randoms were generated without using `LS`_ pixels
RESOLVE  T             bool  ``True`` if from unique imaging
RESEED   626           int   Seed used to re-shuffle combined random catalogs to ensure randomness
MTLSPLIT T             bool  ``True`` if MTL-related columns were added to this random catalog
GAIALOC  "/global/"    str   Location of file used to generate stellar density
SURVEY   "main"        str   svX for SV, main for Main Survey
======== ============= ===== ========================================

Possible Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

============== ======== ============= ===================
Name           Type     Units         Description
============== ======== ============= ===================
HPXPIXEL       int32                  HEALPixel in pixweight map at HPXNSIDE
FRACAREA       float32                Fraction of HEALPixel with at least one observation in any band of the `Legacy Surveys`_
STARDENS       float32  1/deg^2       The stellar density in the HEALPixel from Gaia
EBV            float32                E(B-V) in HEALPixel from the `SFD98`_ dust map, from the median ``EBV`` in the associated random catalog
PSFDEPTH_G     float32                PSF depth in `LS`_ g in the HEALPixel, from the median ``PSFDEPTH_G`` in the associated random catalog
PSFDEPTH_R     float32                PSF depth in `LS`_ r in the HEALPixel, from the median ``PSFDEPTH_R`` in the associated random catalog
PSFDEPTH_Z     float32                PSF depth in `LS`_ z in the HEALPixel, from the median ``PSFDEPTH_Z`` in the associated random catalog
GALDEPTH_G     float32                Galaxy depth in `LS`_ g in the HEALPixel, from the median ``GALDEPTH_G`` in the associated random catalog
GALDEPTH_R     float32                Galaxy depth in `LS`_ r in the HEALPixel, from the median ``GALDEPTH_R`` in the associated random catalog
GALDEPTH_Z     float32                Galaxy depth in `LS`_ z in the HEALPixel, from the median ``GALDEPTH_Z`` in the associated random catalog
PSFDEPTH_W1    float32                (AB) PSF depth in WISE W1 in the HEALPixel, from the median ``PSFDEPTH_W1`` in the associated random catalog
PSFDEPTH_W2    float32                (AB) PSF depth in WISE W2 in the HEALPixel, from the median ``PSFDEPTH_W2`` in the associated random catalog
PSFSIZE_G      float32  arcsec        Weighted average PSF FWHM in `LS`_ g in the HEALPixel, from the median ``PSFSIZE_G`` in the associated random catalog
PSFSIZE_R      float32  arcsec        Weighted average PSF FWHM in `LS`_ r in the HEALPixel, from the median ``PSFSIZE_R`` in the associated random catalog
PSFSIZE_Z      float32  arcsec        Weighted average PSF FWHM in `LS`_ z in the HEALPixel, from the median ``PSFSIZE_Z`` in the associated random catalog
FRACAREA_12290 float32                Fraction of HEALPixel with at least one observation in any band with `LS MASKBITS`_ = X (bitwise OR, so, e.g. if X=7 then fraction for 2^0 | 2^1 | 2^2)
FRACAREA_8194  float32                Fraction of HEALPixel with at least one observation in any band with `LS MASKBITS`_ = X (bitwise OR, so, e.g. if X=7 then fraction for 2^0 | 2^1 | 2^2)
ELG            float32  1/deg^2       Density of ELG targets in HEALPixel
LRG            float32	1/deg^2       Density of LRG targets in HEALPixel
QSO            float32	1/deg^2       Density of QSO targets in HEALPixel
BGS_ANY        float32	1/deg^2       Density of BGS_ANY targets in HEALPixel
MWS_ANY        float32	1/deg^2       Density of MWS_ANY targets in HEALPixel
ALL            float32	1/deg^2       Density of `all` targets in HEALPixel
STD_FAINT      float32	1/deg^2       Density of STD_FAINT targets in HEALPixel
STD_BRIGHT     float32	1/deg^2       Density of STD_BRIGHT targets in HEALPixel
BGS_FAINT      float32	1/deg^2       Density of BGS_FAINT targets in HEALPixel
BGS_BRIGHT     float32	1/deg^2       Density of BGS_BRIGHT targets in HEALPixel
BGS_WISE       float32	1/deg^2       Density of BGS_WISE targets in HEALPixel
MWS_BROAD      float32	1/deg^2       Density of MWS_BROAD targets in HEALPixel
MWS_MAIN_RED   float32	1/deg^2       Density of MWS_MAIN_RED targets in HEALPixel
MWS_MAIN_BLUE  float32	1/deg^2       Density of MWS_MAIN_BLUE targets in HEALPixel
MWS_WD         float32	1/deg^2       Density of MWS_WD targets in HEALPixel
MWS_NEARBY     float32	1/deg^2       Density of MWS_NEARBY targets in HEALPixel
============== ======== ============= ===================


Notes and Examples
==================

See http://legacysurvey.org for more details about the corresponding columns for sources extracted by 
the Tractor in the Legacy Surveys, e.g. the units of the depth quantities.

.. _`SFD98`: http://adsabs.harvard.edu/abs/1998ApJ...500..525S
.. _`Legacy Surveys`: http://legacysurvey.org
.. _`LS`: http://legacysurvey.org/dr9/catalogs/
.. _`LS MASKBITS`: https://www.legacysurvey.org/dr9/bitmasks/
.. _`desitarget data model`: https://desidatamodel.readthedocs.io/en/latest/DESI_TARGET/index.html
.. _`DESI fiberassign code`: https://github.com/desihub/fiberassign
