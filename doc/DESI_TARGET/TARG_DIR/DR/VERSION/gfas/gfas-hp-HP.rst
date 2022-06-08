====
gfas
====

:Summary: DESI guide/focus/alignment (GFA) files contain a single binary table covering the
    entire footprint.  They contain objects derived from matches between
    Gaia and the Legacy Surveys and the associated variables used by fiber
    assignment to select sources for guiding and focus.
:Naming Convention: ``gfas-hp-HP.fits``,
    where ``HP`` is the HEALPixel covered
    at the (nested) HEALPixel nside included in the file header as ``FILENSID``
    (*e.g.* 11).
:Regex: ``gfas-hp-?[0-9]+\.fits``
:File Type: FITS, 20 MB - 8.5 GB

Contents
========

====== =========== ======== ============
Number EXTNAME     Type     Contents
====== =========== ======== ============
HDU0_  PRIMARY     IMAGE    Empty
HDU1_  GFA_TARGETS BINTABLE Target table
====== =========== ======== ============

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

Target selection table

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============= ===== ==================================
KEY      Example Value Type  Comment
======== ============= ===== ==================================
NAXIS1   164           int   width of table in bytes
NAXIS2   142824        int   number of rows in table
DR       9             int   Legacy Surveys Data Release used to find targets
MAGLIM   21.0          float magnitude limit on GFA targets in Gaia G-band
MINDEC   -90.0         float minimum declination for GFAs that are not selected from the Legacy Surveys
MINGALB  0.0           float closest latitude to Galactic Plane for GFAs that are not selected from the Legacy Surveys
NOURAT   F             bool  ``True`` if the URAT catalog was not used to supplement missing proper motions
GAIADR   "edr3"        str   Gaia Data Release used to select GFAs
HPXNSIDE 64            int   HEALPix nside for column `HPXPIXEL`
HPXNEST  T             bool  HEALPix nested (not ring) ordering
FILENSID 2             int   HEALPix nside covered by file
FILENEST T             bool  HEALPix nested (not ring) ordering
FILEHPX  11            int   HEALPix pixel(s) covered by file
======== ============= ===== ==================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

================================= =========== ================== ===================
Name                              Type        Units              Description
================================= =========== ================== ===================
RELEASE                           int16                          Legacy Surveys (`LS`_) `Release`_
TARGETID                          int64                          ID (unique to file and the whole survey)
BRICKID                           int32                          Brick ID from tractor input
BRICK_OBJID                       int32                          OBJID (unique to brick, but not to file)
RA                                float64     deg                Right ascension
DEC                               float64     deg                Declination
RA_IVAR                           float32     deg**-2            Right ascension inverse variance
DEC_IVAR                          float32     deg**-2            Declination inverse variance
MORPHTYPE                         char[4]                        `Morphological Model`_ type
MASKBITS                          int16                          Bitmask for ``coadd/*/*/*maskbits*`` maps, as on the `LS DR9 bitmasks page`_
FLUX_G                            float32     nanomaggies        `LS`_ flux from tractor input (g)
FLUX_R                            float32     nanomaggies        `LS`_ flux from tractor input (r)
FLUX_Z                            float32     nanomaggies        `LS`_ flux from tractor input (z)
FLUX_IVAR_G                       float32     nanomaggies**-2    Inverse Variance of FLUX_G
FLUX_IVAR_R                       float32     nanomaggies**-2    Inverse Variance of FLUX_R
FLUX_IVAR_Z                       float32     nanomaggies**-2    Inverse Variance of FLUX_Z
REF_ID                            int64                          Tyc1*1,000,000+Tyc2*10+Tyc3 for `Tycho-2`_; "sourceid" for `Gaia`_ DR2
REF_CAT                           char[2]                        Reference catalog source for star: "T2" for `Tycho-2`_, "G2" for `Gaia`_ DR2, "L2" for the `SGA`_, empty otherwise
REF_EPOCH                         float32     yr                 Reference epoch for Gaia/Tycho astrometry. Typically 2015.5 for Gaia.
PARALLAX                          float32     mas                Reference catalog parallax
PARALLAX_IVAR                     float32     mas**-2            Inverse variance of parallax
PMRA                              float32     mas/yr             Reference catalog proper motion in the RA direction
PMDEC                             float32     mas/yr             Reference catalog proper motion in the Dec direction
PMRA_IVAR                         float32     mas/yr**-2         Inverse variance of PMRA
PMDEC_IVAR                        float32     mas/yr**-2         Inverse variance of PMDEC
GAIA_PHOT_G_MEAN_MAG              float32     mag                `Gaia`_ G band magnitude
GAIA_PHOT_G_MEAN_FLUX_OVER_ERROR  float32                        `Gaia`_ G band signal-to-noise
GAIA_PHOT_BP_MEAN_MAG             float32     mag                `Gaia`_ BP band magnitude
GAIA_PHOT_BP_MEAN_FLUX_OVER_ERROR float32                        `Gaia`_ BP band signal-to-noise
GAIA_PHOT_RP_MEAN_MAG             float32     mag                `Gaia`_ RP band magnitude
GAIA_PHOT_RP_MEAN_FLUX_OVER_ERROR float32                        `Gaia`_ RP band signal-to-noise
GAIA_ASTROMETRIC_EXCESS_NOISE     float32                        `Gaia`_ astrometric excess noise
URAT_ID                           int64                          ID in the URAT catalog for sources where URAT supplemented missing Gaia astrometric information
URAT_SEP                          float32     arcsec             Separation between URAT and Gaia sources where URAT supplemented missing Gaia astrometric information
GAIA_PHOT_G_N_OBS                 int32                          Number of observations in Gaia G band
HPXPIXEL                          int64                          HEALPixel containing target at HPXNSIDE
================================= =========== ================== ===================

.. _`LS`: https://www.legacysurvey.org/dr8/catalogs/
.. _`ellipticity component`: https://www.legacysurvey.org/dr8/catalogs/
.. _`Release`: https://www.legacysurvey.org/release/
.. _`Morphological Model`: https://www.legacysurvey.org/dr8/catalogs/
.. _`Tycho-2`: https://heasarc.nasa.gov/W3Browse/all/tycho2.html
.. _`Gaia`: https://gea.esac.esa.int/archive/documentation//GDR2/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html
.. _`SFD98`: http://ui.adsabs.harvard.edu/abs/1998ApJ...500..525S
.. _`LS DR9 bitmasks page`: https://www.legacysurvey.org/dr9/bitmasks/
.. _`SGA`: https://github.com/moustakas/SGA

Notes
=====

See https://www.legacysurvey.org for more details about columns in the data model.
