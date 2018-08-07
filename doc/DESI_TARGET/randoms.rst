=======
randoms
=======

:Summary: DESI random catalogs contain a single binary table covering the entire
    Legacy Surveys footprint. They contain meta-information (the number of
    observations, the depth, etc.) derived from pixels in Legacy Surveys CCDs at
    random RA/Dec coordinates.
:Naming Convention: ```DRX/VERSION/randoms-DRX-VERSION.fits``, where ``DRX`` is the
    imaging surveys data release name (e.g. dr7.1) and ``VERSION`` is the
    desitarget code version defining the cuts. Sometimes split into smaller
    subsets of random points named ``randoms-DRX-VERSION-N.fits`` where
    ``N`` is an integer.
:Regex: ``randoms-dr[0.9]+\.[0-9]+-v?[0-9]+\.[0-9]+(\.[0-9]+|)\.fits`` or
    :Regex: ``targets-dr[0.9]+\.[0-9]+-v?[0-9]+\.[0-9]+(\.[0-9]+|)\+-[0-9].fits``
:File Type: FITS, 70 GB

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_  PRIMARY IMAGE    Empty
HDU1_  RANDOMS BINTABLE Random catalog table
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = RANDOMS

Random catalog table

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============= ==== ========================================
KEY      Example Value Type Comment
======== ============= ==== ========================================
NAXIS1   68            int  width of table in bytes
NAXIS2   1124357626    int  number of rows in table
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
DENSITY  100000        int  Number of random points generated per sq. deg.
======== ============= ==== ========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

========== ======= ===== ===================
Name       Type    Units Description
========== ======= ===== ===================
RA         float64       Right ascension at pixel location [degrees]
DEC        float64       Declination at pixel location [degrees]
BRICKNAME  char[8]       Name of brick in the `Legacy Surveys`_ (LS) schema
NOBS_G     int16         Number of images at pixel location in `LS`_ g
NOBS_R     int16         Number of images at pixel location in `LS`_ r
NOBS_Z     int16         Number of images at pixel location in `LS`_ z
PSFDEPTH_G float32       PSF-based depth at pixel location in `LS`_ g
PSFDEPTH_R float32       PSF-based depth at pixel location in `LS`_ r
PSFDEPTH_Z float32       PSF-based depth at pixel location in `LS`_ z
GALDEPTH_G float32       Galaxy model-based depth at pixel location in `LS`_ g
GALDEPTH_R float32       Galaxy model-based depth at pixel location in `LS`_ r
GALDEPTH_Z float32       Galaxy model-based depth at pixel location in `LS`_ z
MASKBITS   int16         Bit mask of possible problems with pixel (see header)
EBV        float32       Galactic extinction E(B-V) reddening at pixel from `SFD98`_
HPXPIXEL   int64         HEALPixel containing location
========== ======= ===== ===================


Notes and Examples
==================

See http://legacysurvey.org for more details about the corresponding columns for sources extracted by 
the Tractor in the Legacy Surveys

.. _`SFD98`: http://adsabs.harvard.edu/abs/1998ApJ...500..525S
.. _`Legacy Surveys`: http://legacysurvey.org
.. _`LS`: http://legacysurvey.org/dr7/catalogs/
