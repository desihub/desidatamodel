=====
skies
=====

*Warning* this file might not be compatible with the data model, because it contains
two `:Regex:` sections.  This should be two separate files.

:Summary: DESI sky locations contain a single binary table covering the entire
    Legacy Surveys footprint. The imaging "blob maps" are bisected to achieve
    a requisite number of sky locations per sq. deg. Sky locations are placed
    within the bisected grid as far from blobs that contain sources as is
    possible. Flux is measured in an aperture at each sky location.
:Naming Convention: ``DRX/VERSION/skies-DRX-VERSION.fits``, where ``DRX`` is the
    imaging surveys data release name (e.g. dr7.1) and ``VERSION`` is the
    desitarget code version.
:Regex: ``randoms-dr[0.9]+\.[0-9]+-v?[0-9]+\.[0-9]+(\.[0-9]+|)\.fits`` or
    :Regex: ``targets-dr[0.9]+\.[0-9]+-v?[0-9]+\.[0-9]+(\.[0-9]+|)\+-[0-9].fits``
:File Type: FITS, 3 GB

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_  PRIMARY IMAGE    Empty
HDU1_  SKIES   BINTABLE Table of sky locations
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

EXTNAME = SKIES

Table of sky locations

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============= ===== =======================
KEY      Example Value Type  Comment
======== ============= ===== =======================
NAXIS1   136           int   width of table in bytes
NAXIS2   25936848      int   number of rows in table
AP0      0.75          float radius of aperture at sky location [arcsec]
AP1      1.0           float radius of aperture at sky location [arcsec]
BADFLUX0 1000.0        float amount of flux in AP0 to define a BAD sky location [nanomaggies]
BADFLUX1 1000.0        float amount of flux in AP1 to define a BAD sky location [nanomaggies]
HPXNSIDE 64            int   HEALPix nside
HPXNEST  T             bool  HEALPix nested (not ring) ordering
======== ============= ===== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

============= ========== ===== ===================
Name          Type       Units Description
============= ========== ===== ===================
RELEASE       int32            Legacy Surveys (`LS`_) `Release`_
BRICKID       int32            Brick ID from tractor input
BRICKNAME     char[8]          Brick name from tractor input
BRICK_OBJID   int32            OBJID (unique to brick, but not to file)
RA            float64          Right ascension [degrees]
DEC           float64          Declination [degrees]
APFLUX_G      float32[2]       `LS`_ flux in each aperture listed in the header in (g)
APFLUX_R      float32[2]       `LS`_ flux in each aperture listed in the header in (r)
APFLUX_Z      float32[2]       `LS`_ flux in each aperture listed in the header in (z)
APFLUX_IVAR_G float32[2]       Inverse variance of APFLUX_G
APFLUX_IVAR_R float32[2]       Inverse variance of APFLUX_R
APFLUX_IVAR_Z float32[2]       Inverse variance of APFLUX_Z
OBSCONDITIONS int32            Convenience for downstream fiber assign code (always 65535)
SUBPRIORITY   float64          Priority that is used to break ties during fiber assignment
TARGETID      int64            ID (unique to file and the whole survey)
DESI_TARGET   int64            DESI (dark time program) target selection bitmask
BGS_TARGET    int64            BGS (bright time program) target selection bitmask
MWS_TARGET    int64            MWS (bright time program) target selection bitmask
HPXPIXEL      int64            HEALPixel containing sky location
============= ========== ===== ===================


Notes and Examples
==================

.. _`LS`: http://legacysurvey.org/dr7/catalogs/
.. _`Release`: http://legacysurvey.org/release/
