===================
unpartitioned skies
===================

:Summary: Unpartitioned DESI sky locations contain a single binary table covering the entire
    `Legacy Surveys`_ footprint. They will `not` be a useful data product for
    most users. They exist because DESI sky locations are originally generated in
    Legacy Surveys `bricks` before being re-partitioned into HEALPixels.
    The unpartitioned sky files are assembled according to which `bricks` occupy each
    HEALPixel rather than by which `sky locations` occupy each HEALPixel. They are purely
    included for completeness, and are merely a rearrangement of the DESI skies files.
:Naming Convention: ``skies-hp-HP.fits-unpartitioned``,
    where ``HP`` is the HEALPixel covered
    at the (nested) HEALPixel nside included in the file header as ``FILENSID``
    (*e.g.* 11).
:Regex: ``skies-hp-?[0-9]+\.fits-unpartitioned``
:File Type: FITS, 2 MB - 140 MB

Contents
========

====== =========== ======== ===================
Number EXTNAME     Type     Contents
====== =========== ======== ===================
HDU0_  PRIMARY     IMAGE    Empty
HDU1_  SKY_TARGETS BINTABLE Table of sky locations
====== =========== ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = SKY_TARGETS

Table of sky locations

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============= ===== ==================================
KEY      Example Value Type  Comment
======== ============= ===== ==================================
NAXIS1   136           int   width of table in bytes
NAXIS2   1055419       int   number of rows in table
AP0      0.75          float aperture radius used to calculate flux-related quantities (arcsec)
SUPP     F             bool  ``True`` if sky location are `not` derived from the `Legacy Surveys`_
DR       9             int   Legacy Surveys Data Release used to find targets
NPERSDEG 18000.0       float density of sky locations generated per sq. deg.
HPXNSIDE 64            int   HEALPix nside for column `HPXPIXEL`
HPXNEST  T             bool  HEALPix nested (not ring) ordering
SUBPSEED 805           int   random seed used to generate `SUBPRIORITY` values
MASKED   T             bool  ``True`` if targets were masked to avoid bright sources
MASKDIR  "masks/"      str   location of directory of masks used to avoid bright sources
CMDLINE  "/global/"    str   command-line call used to generate target file
FILENSID 2             int   HEALPix nside covered by file
FILENEST T             bool  HEALPix nested (not ring) ordering
FILEHPX  11            int   HEALPix pixel(s) covered by file
======== ============= ===== ==================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

================================= ========== ======= ===================
Name                              Type       Units   Description
================================= ========== ======= ===================
RELEASE                           int32              Legacy Surveys (`LS`_) `Release`_
BRICKID                           int32              Brick ID from tractor input
BRICKNAME                         char[8]            Brick name from tractor input
BRICK_OBJID                       int32              OBJID (unique to brick, but not to file)
RA                                float64    deg     Right ascension
DEC                               float64    deg     Declination
BLOBDIST                          float32    pix     Maximum distance from a detected `Legacy Surveys`_ source
FIBERFLUX_G                       float32            g-band object model flux calculated in aperture of radius ``AP0``
FIBERFLUX_R                       float32            r-band object model flux calculated in aperture of	radius ``AP0``
FIBERFLUX_Z                       float32            z-band object model flux calculated in aperture of	radius ``AP0``
FIBERFLUX_IVAR_G                  float32            Inverse Variance of ``FIBERFLUX_G``
FIBERFLUX_IVAR_R                  float32            Inverse Variance of ``FIBERFLUX_R``
FIBERFLUX_IVAR_Z                  float32            Inverse Variance of ``FIBERFLUX_Z``
TARGETID                          int64              Unique targeting ID
DESI_TARGET                       int64              DESI (dark time program) target selection bitmask
BGS_TARGET                        int64              BGS (bright time program) target selection bitmask
MWS_TARGET                        int64              MWS (bright time program) target selection bitmask
SUBPRIORITY                       float64            Random subpriority [0-1] to break assignment ties
OBSCONDITIONS                     int64              Flag target to be observed in combinations of dark/bright observing layer
PRIORITY_INIT                     int64              Initial priority for target calculated across target selection bitmasks and OBSCONDITIONS
NUMOBS_INIT                       int64              Initial number of observations for target calculated across target selection bitmasks and OBSCONDITIONS
HPXPIXEL                          int64              HEALPixel containing sky location
================================= ========== ======= ===================

.. _`Legacy Surveys`: http://legacysurvey.org
.. _`LS`: http://legacysurvey.org/dr9/catalogs/
.. _`ellipticity component`: http://legacysurvey.org/dr9/catalogs/
.. _`Release`: http://legacysurvey.org/release/
.. _`Morphological Model`: http://legacysurvey.org/dr9/catalogs/
.. _`Tycho-2`: https://heasarc.nasa.gov/W3Browse/all/tycho2.html
.. _`Gaia`: https://gea.esac.esa.int/archive/documentation//GDR2/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html
