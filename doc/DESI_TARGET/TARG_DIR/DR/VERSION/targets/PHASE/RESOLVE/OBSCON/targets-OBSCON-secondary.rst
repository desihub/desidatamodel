==============================
"standalone" secondary targets
==============================

:Summary: DESI "standalone" secondary targets are stored in single, monolithic binary
    tables. Here, "standalone" refers to the fact that either the proposer of the particular secondary
    target class requested that their targets should `not` be merged with matching primary targets, or
    that no match was found to a primary target.
:Naming Convention: ``PHASEtargets-OBSCON-secondary.fits``,
    where ``PHASE`` is a specific DESI observational phase (*e.g.* svX with X=1,2,3
    for iterations of Survey Validation), and ``OBSCON`` is the
    observing condition or "layer") for the targets (*e.g.* dark).
:Regex: ``(cmx|sv1|sv2|sv3|main2|)targets-(bright|dark)-secondary\.fits``
:File Type: FITS, 200-900 MB

Contents
========

====== ============ ======== ============
Number EXTNAME      Type     Contents
====== ============ ======== ============
HDU0_  PRIMARY      IMAGE    Empty
HDU1_  SCND_TARGETS BINTABLE Table of secondary targets
====== ============ ======== ============

FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = SCND_TARGETS

Table of secondary targets

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ============= ===== ==================================
    KEY      Example Value Type  Comment
    ======== ============= ===== ==================================
    NAXIS1   121           int   width of table in bytes
    NAXIS2   7125595       int   number of rows in table
    SURVEY   "main"        str   svX for SV, main for Main Survey
    PRIMDIR  "/global/"    str   location of directory of information about corresponding primary targets
    SEP      1.0           float matching radius that was used to find primary targets (arcsec)
    MASKED   T             bool  ``True`` if targets were masked to avoid bright sources
    MASKDIR  "masks/"      str   location of directory of masks used to avoid bright sources
    SCNDDIR  "/global/"    str   directory from which secondary targets were read
    OBSCON   "DARK"        str   observing layer for file
    SUBPSEED 717           int   random seed used to generate `SUBPRIORITY` values
    ======== ============= ===== ==================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

=============================== =========== ================ ===================
Name                            Type        Units            Description
=============================== =========== ================ ===================
RA                              float64     deg              Right ascension
DEC                             float64     deg              Declination
PMRA                            float32     mas/yr           Reference catalog proper motion in the RA direction
PMDEC                           float32     mas/yr           Reference catalog proper motion in the Dec direction
REF_EPOCH                       float32     yr               Reference epoch for Gaia/Tycho astrometry. Typically 2015.5 for Gaia.
OVERRIDE                        bool                         ``True`` if the secondary target class was not matched to primary targets
FLUX_G                          float32     nanomaggy        `LS`_ flux from tractor input (g)
FLUX_R                          float32     nanomaggy        `LS`_ flux from tractor input (r)
FLUX_Z                          float32     nanomaggy        `LS`_ flux from tractor input (z)
PARALLAX                        float32     mas              Reference catalog parallax
GAIA_PHOT_G_MEAN_MAG            float32     mag              `Gaia`_ G band magnitude
GAIA_PHOT_BP_MEAN_MAG           float32     mag              `Gaia`_ BP band magnitude
GAIA_PHOT_RP_MEAN_MAG           float32     mag              `Gaia`_ RP band magnitude
GAIA_ASTROMETRIC_EXCESS_NOISE   float32                      `Gaia`_ astrometric excess noise
TARGETID                        int64                        Unique targeting ID
DESI_TARGET                     int64                        DESI (dark time program) target selection bitmask
SCND_TARGET                     int64                        SCND (secondary program) target selection bitmask
SCND_ORDER                      int32                        Row in which this target appeared in the input secondary target file
SUBPRIORITY                     float64                      Random subpriority [0-1] to break assignment ties
OBSCONDITIONS                   int64                        Flag target to be observed in combinations of dark/bright observing layer
PRIORITY_INIT                   int64                        Initial priority for target calculated across target selection bitmasks and OBSCONDITIONS
NUMOBS_INIT                     int64                        Initial number of observations for target calculated across target selection bitmasks and OBSCONDITIONS
=============================== =========== ================ ===================

.. _`LS`: https://www.legacysurvey.org/dr9/catalogs/
.. _`ellipticity component`: https://www.legacysurvey.org/dr9/catalogs/
.. _`Release`: https://www.legacysurvey.org/release/
.. _`Morphological Model`: https://www.legacysurvey.org/dr9/catalogs/
.. _`Tycho-2`: https://heasarc.nasa.gov/W3Browse/all/tycho2.html
.. _`Gaia`: https://gea.esac.esa.int/archive/documentation//GDR2/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html
.. _`SFD98`: http://ui.adsabs.harvard.edu/abs/1998ApJ...500..525S
.. _`LS DR9 bitmasks page`: https://www.legacysurvey.org/dr9/bitmasks/
.. _`SGA`: https://github.com/moustakas/SGA
