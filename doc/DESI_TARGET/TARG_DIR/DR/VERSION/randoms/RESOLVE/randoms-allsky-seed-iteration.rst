==============
randoms-allsky
==============

:Summary: DESI allsky random catalogs contain a single binary table covering
    the entire sky. Inside the `Legacy Surveys`_ (LS) footprint they contain meta
    information (the number of observations, the depth, etc.) derived from
    pixels in Legacy Surveys CCDs at random RA/Dec coordinates. Outside the
    `LS`_ footprint they contain highly simplified columns. These files are a
    combination of the standard inside-the-footprint random catalogs and the
    simplified outside-the-footprint random catalogs.
:Naming Convention: ``randoms-allsky-seed-iteration.fits``, where ``seed`` represents
    the random seed used to generate the catalog and ``iteration`` lists the iteration
    number of the catalog (several iterations are typically conducted
    during a given run to generate random catalogs).
:Regex: ``randoms-allsky-[0-9]+-[0-9]+\.fits``
:File Type: FITS, 12 GB

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

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ============= ===== ========================================
    KEY      Example Value Type  Comment
    ======== ============= ===== ========================================
    NAXIS1   281           int   Width of table in bytes
    NAXIS2   1124357626    int   Number of rows in table
    FILENSID 2             int   HEALPix nside covered by file
    FILENEST T             bool  HEALPix nested (not ring) ordering
    FILEHPX  11,5,4        str   HEALPix pixel(s) covered by file
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
    ======== ============= ===== ========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

============= ======== ============== ===================
Name          Type     Units          Description
============= ======== ============== ===================
RA            float64  deg            Right ascension at pixel location
DEC           float64  deg            Declination at pixel location
BRICKNAME     char[8]                 Name of the brick
BRICKID       int32                   A unique Brick ID
NOBS_G        int16                   Number of images at pixel location in `LS`_ g
NOBS_R        int16                   Number of images at pixel location in `LS`_ r
NOBS_Z        int16                   Number of images at pixel location in `LS`_ z
PSFDEPTH_G    float32                 PSF-based depth at pixel location in `LS`_ g
PSFDEPTH_R    float32                 PSF-based depth at pixel location in `LS`_ r
PSFDEPTH_Z    float32                 PSF-based depth at pixel location in `LS`_ z
GALDEPTH_G    float32                 Galaxy model-based depth at pixel location in `LS`_ g
GALDEPTH_R    float32                 Galaxy model-based depth at pixel location in `LS`_ r
GALDEPTH_Z    float32                 Galaxy model-based depth at pixel location in `LS`_ z
PSFDEPTH_W1   float32                 PSF-based depth in WISE W1 (AB mag system)
PSFDEPTH_W2   float32                 PSF-based depth in WISE W2 (AB mag system)
PSFSIZE_G     float32  arcsec         Weighted average PSF FWHM in `LS`_ g
PSFSIZE_R     float32  arcsec         Weighted average PSF FWHM in `LS`_ r
PSFSIZE_Z     float32  arcsec         Weighted average PSF FWHM in `LS`_ z
APFLUX_G      float32  nanomaggy      Total flux extracted in a 0.75 arcsec radius in g
APFLUX_R      float32  nanomaggy      Total flux extracted in a 0.75 arcsec radius in r
APFLUX_Z      float32  nanomaggy      Total flux extracted in a 0.75 arcsec radius in z
APFLUX_IVAR_G float32  nanomaggy^-2   Inverse variance of APFLUX_G
APFLUX_IVAR_R float32  nanomaggy^-2   Inverse variance of APFLUX_R
APFLUX_IVAR_Z float32  nanomaggy^-2   Inverse variance of APFLUX_Z
MASKBITS      int16                   Bit mask of possible problems with pixel (see the LS `DR9 bitmasks page`_)
WISEMASK_W1   uint8                   Bitwise mask for WISE W1 data (see the LS `DR9 bitmasks page`_)
WISEMASK_W2   uint8                   Bitwise mask for WISE W2 data (see the LS `DR9 bitmasks page`_)
EBV           float32                 Galactic extinction E(B-V) reddening at pixel from `SFD98`_
PHOTSYS       char[1]                 'N' for an MzLS/BASS location, 'S' for a DECaLS location
HPXPIXEL      int64                   HEALPixel containing this location at NSIDE=64 in the NESTED scheme
============= ======== ============== ===================


Notes and Examples
==================

See http://legacysurvey.org for more details about the corresponding columns for sources extracted by
the Tractor in the Legacy Surveys, e.g. the units of the depth quantities.

.. _`SFD98`: http://adsabs.harvard.edu/abs/1998ApJ...500..525S
.. _`Legacy Surveys`: http://legacysurvey.org
.. _`LS`: http://legacysurvey.org/dr9/catalogs/
.. _`DR9 bitmasks page`: https://www.legacysurvey.org/dr9/bitmasks/
.. _`desitarget data model`: https://desidatamodel.readthedocs.io/en/latest/DESI_TARGET/index.html
.. _`DESI fiberassign code`: https://github.com/desihub/fiberassign
