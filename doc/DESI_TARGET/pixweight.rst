=========
pixweight
=========

:Summary: DESI HEALPixel weight files contain a single binary table covering the 
    entire Legacy Surveys footprint. They contain meta information (the number of
    observations, the depth, etc.) derived from pixels in Legacy Surveys CCDs,
    together with target densities, conveniently stored as HEALPixel maps. They are 
    derived from the corresponding ``DRX/VERSION/randoms-DRX-VERSION.fits`` and
    ``DRX/VERSION/targets-DRX-VERSION.fits`` files.
:Naming Convention: ``DRX/VERSION/pixweight-DRX-VERSION.fits``, where ``DRX`` is the
    imaging surveys data release name (e.g. dr7.1) and ``VERSION`` is the desitarget 
    code version.
:Regex: ``pixweight-dr[0.9]+\.[0-9]+-v?[0-9]+\.[0-9]+(\.[0-9]+|)\.fits``
:File Type: FITS, 81 MB

Contents
========

====== ========== ======== ===================
Number EXTNAME    Type     Contents
====== ========== ======== ===================
HDU0_  PRIMARY    IMAGE    Empty
HDU1_  PIXWEIGHTS BINTABLE HEALPixel weight map table
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

Table of weights in HEALPixels

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============= ==== ========================================
KEY      Example Value Type Comment
======== ============= ==== ========================================
NAXIS1   108           int  width of table in bytes
NAXIS2   786432        int  number of rows in table
BITNM0   NPRIMARY      str  ``MASKBITS`` bit 0: not-brick-primary
BITNM1   BRIGHT        str  ``MASKBITS`` bit 1: bright star in blob
BITNM2   SATUR_G       str  ``MASKBITS`` bit 2: g saturated + margin
BITNM3   SATUR_R       str  ``MASKBITS`` bit 3: r saturated + margin
BITNM4   SATUR_Z       str  ``MASKBITS`` bit 4: z saturated + margin
BITNM5   ALLMASK_G     str  ``MASKBITS`` bit 5: any ALLMASK_G bit set
BITNM6   ALLMASK_R     str  ``MASKBITS`` bit 6: any ALLMASK_R bit set
BITNM7   ALLMASK_Z     str  ``MASKBITS`` bit 7: any ALLMASK_Z bit set
BITNM8   WISEM1        str  ``MASKBITS`` bit 8: WISE W1 bright star mask
BITNM9   WISEM2        str  ``MASKBITS`` bit 9: WISE W2 bright star mask
HPXNSIDE 64            int  HEALPix nside
HPXNEST  T             bool HEALPix nested (not ring) ordering
DENSITY  100000        int  DENSITY of points in corresponding random catalog
======== ============= ==== ========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

============= ======= ===== ===================
Name          Type    Units Description
============= ======= ===== ===================
HPXPIXEL      int32         HEALPixel integer (total number of HEALPixels corresponds to unique NSIDE)
FRACAREA      float32       Fraction of HEALPixel covered by at least one image
STARDENS      float32       Density of Gaia sources in HEALPixel
EBV           float32       E(B-V) from `SFD98`_ dust map (derived from median of random points in HEALPixel)
PSFDEPTH_G    float32       PSF-based depth in HEALPixel in `LS`_ g (derived from median of random points)
PSFDEPTH_R    float32       PSF-based depth in HEALPixel in `LS`_ r (derived from median of random points)
PSFDEPTH_Z    float32       PSF-based depth in HEALPixel in `LS`_ z (derived from median of random points)
GALDEPTH_G    float32       Galaxy model-based depth in HEALPixel in `LS`_ g (from median of randoms)
GALDEPTH_R    float32       Galaxy model-based depth in HEALPixel in `LS`_ r (from median of randoms)
GALDEPTH_Z    float32       Galaxy model-based depth in HEALPixel in `LS`_ z (from median of randoms)
ELG           float32       Density of ``ELG`` targets in HEALPixel [per sq. deg.]
LRG           float32       Density of ``LRG`` targets in HEALPixel [per sq. deg.]
QSO           float32       Density of ``QSO`` targets in HEALPixel [per sq. deg.]
BGS_ANY       float32       Density of all ``BGS`` targets in HEALPixel [per sq. deg.]
STD           float32       Density of ``STD`` targets in HEALPixel [per sq. deg.]
STD_BRIGHT    float32       Density of ``STD_BRIGHT`` targets in HEALPixel [per sq. deg.]
MWS_ANY       float32       Density of all ``MWS`` targets in HEALPixel [per sq. deg.]
ALL           float32       Density of all targets in HEALPixel [per sq. deg.]
LRG_1PASS     float32       Density of ``LRG_1PASS`` targets in HEALPixel [per sq. deg.]
LRG_2PASS     float32       Density of ``LRG_2PASS`` targets in HEALPixel [per sq. deg.]
BGS_FAINT     float32       Density of ``BGS_FAINT`` targets in HEALPixel [per sq. deg.]
BGS_BRIGHT    float32       Density of ``BGS_BRIGHT`` targets in HEALPixel [per sq. deg.]
MWS_MAIN      float32       Density of ``MWS_MAIN`` targets in HEALPixel [per sq. deg.]
MWS_MAIN_RED  float32       Density of ``MWS_MAIN_RED`` targets in HEALPixel [per sq. deg.]
MWS_MAIN_BLUE float32       Density of ``MWS_MAIN_BLUE`` targets in HEALPixel [per sq. deg.]
MWS_WD        float32       Density of ``MWS_WD`` targets in HEALPixel [per sq. deg.]
MWS_NEARBY    float32       Density of ``MWS_NEARBY`` targets in HEALPixel [per sq. deg.] 
============= ======= ===== ===================


Notes and Examples
==================

See http://legacysurvey.org for more details about the corresponding columns for sources extracted by 
the Tractor in the Legacy Surveys, e.g. the units of the depth quantities.

.. _`SFD98`: http://adsabs.harvard.edu/abs/1998ApJ...500..525S
.. _`LS`: http://legacysurvey.org/dr7/catalogs/

