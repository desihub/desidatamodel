====
gfas
====

:Summary: DESI GFA files contain a single binary table covering the
    entire footprint.  They contain objects derived from matches between
    Gaia and the Legacy Surveys and the associated variables used by fiber
    assignment to select sources for guiding and focus.
:Naming Convention: ``DRX/VERSION/gfas-DRX-VERSION.fits``, where ``DRX`` is the
    imaging surveys data release name (e.g. dr7.1) and ``VERSION`` is the
    desitarget code version defining the cuts (e.g. 0.22.0).
:Regex: ``gfas-dr[0.9]+\.[0-9]+-v?[0-9]+\.[0-9]+(\.[0-9]+|)\.fits``
:File Type: FITS, 3 GB

Contents
========

====== =========== ======== ===================
Number EXTNAME     Type     Contents
====== =========== ======== ===================
HDU0_  PRIMARY     IMAGE    Empty
HDU1_  GFA_TARGETS BINTABLE Table of GFAs
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

EXTNAME = GFA_TARGETS

Table of GFAs

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============= ==== =======================
KEY      Example Value Type Comment
======== ============= ==== =======================
NAXIS1   112           int  width of table in bytes
NAXIS2   30270306      int  number of rows in table
HPXNSIDE 64            int  HEALPix nside
HPXNEST  T             bool HEALPix nested (not ring) ordering
======== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

================================ ======= ===== ===================
Name                             Type    Units Description
================================ ======= ===== ===================
TARGETID                         int64         ID (unique to file and the whole survey)
BRICKID                          int32         Brick ID from tractor input
BRICK_OBJID                      int32          OBJID (unique to brick, but not to file)
RA                               float64       Right ascension [degrees]
DEC                              float64       Declination [degrees]
RA_IVAR                          float32       Inverse Variance of RA [degrees]
DEC_IVAR                         float32       Inverse Variance of DEC [degrees]
TYPE                             char[4]       `Morphological Model`_ type
FLUX_G                           float32       `LS`_ flux from tractor input (g)
FLUX_R                           float32       `LS`_ flux from tractor input (r)
FLUX_Z                           float32       `LS`_ flux from tractor input (z)
FLUX_IVAR_G                      float32       Inverse Variance of FLUX_G
FLUX_IVAR_R                      float32       Inverse Variance of FLUX_R
FLUX_IVAR_Z                      float32       Inverse Variance of FLUX_Z
REF_ID                           int64         Tyc1*1,000,000+Tyc2*10+Tyc3 for `Tycho-2`_; "sourceid" for `Gaia`_ DR2
PMRA                             float32       Reference catalog proper motion in the RA direction
PMDEC                            float32       Reference catalog proper motion in the Dec direction
PMRA_IVAR                        float32       Inverse variance of PMRA
PMDEC_IVAR                       float32       Inverse variance of PMDEC
GAIA_PHOT_G_MEAN_MAG             float32       `Gaia`_ G band magnitude
GAIA_PHOT_G_MEAN_FLUX_OVER_ERROR float32       `Gaia`_ G band signal-to-noise
GAIA_ASTROMETRIC_EXCESS_NOISE    float32       `Gaia`_ astrometric excess noise
HPXPIXEL                         int64         HEALPixel containing GFA target
================================ ======= ===== ===================


Notes and Examples
==================

.. _`LS`: http://legacysurvey.org/dr7/catalogs/
.. _`Morphological Model`: http://legacysurvey.org/dr7/catalogs/
.. _`Gaia`: https://gea.esac.esa.int/archive/documentation//GDR2/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html
