========
priminfo
========

:Summary: priminfo files include a binary table containing matches between secondary
    targets and DESI primary targets in a (nested) HEALPixel.
:Naming Convention: ``PHASEtargets-no-obscon-hp-HP.fits``, where ``PHASE``
    is ``sv1`` or ``sv3`` for the corresponding survey, but empty for ``main`` and
    ``HP`` is the HEALPixel covered
    at the (nested) HEALPixel nside included in the file header as ``FILENSID``
    (*e.g.* 11).
:Regex: ``(sv1|sv3|)targets-no-obscon-hp-?[0-9]+\.fits``
:File Type: FITS, 12 KB - 9.8 MB

Contents
========

====== ======= ========= ============
Number EXTNAME Type      Contents
====== ======= ========= ============
HDU0_  PRIMARY IMAGE     Empty
HDU1_  TARGETS SCND_TARG Matches between primary and secondary targets
====== ======= ========= ============

FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = SCND_TARG

Matches between primary and secondary targets

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ============= ==== ==================================
    KEY      Example Value Type Comment
    ======== ============= ==== ==================================
    NAXIS1   130           int  width of table in bytes
    NAXIS2   30444         int  number of rows in table
    SURVEY   "main"        str  svX for SV, main for Main Survey
    ======== ============= ==== ==================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

================================= =========== ===================== ===================
Name                              Type        Units                 Description
================================= =========== ===================== ===================
RA                                float64     deg                   Right ascension
DEC                               float64     deg                   Declination
PMRA                              float32     mas / yr              Proper motion in the RA direction
PMDEC                             float32     mas / yr              Proper motion in the Dec direction
REF_EPOCH                         float32     yr                    Astrometric reference epoch. Typically 2015.5.
OVERRIDE                          logical                           If ``True`` do not match to and accept an existing primary target. Instead, always generate a new ``TARGETID``
FLUX_G                            float32     nanomaggy             `LS`_ flux from tractor input (g)
FLUX_R                            float32     nanomaggy             `LS`_ flux from tractor input (r)
FLUX_Z                            float32     nanomaggy             `LS`_ flux from tractor input (z)
PARALLAX                          float32     mas                   Reference catalog parallax
GAIA_PHOT_G_MEAN_MAG              float32     mag                   `Gaia`_ G band magnitude
GAIA_PHOT_BP_MEAN_MAG             float32     mag                   `Gaia`_ BP band magnitude
GAIA_PHOT_RP_MEAN_MAG             float32     mag                   `Gaia`_ RP band magnitude
GAIA_ASTROMETRIC_EXCESS_NOISE     float32                           `Gaia`_ astrometric excess noise
TARGETID                          int64                             Unique targeting ID
DESI_TARGET                       int64                             DESI (dark time program) target selection bitmask
SCND_TARGET                       int64                             SCND (secondary program) target selection bitmask
SCND_ORDER                        int32                             Row in which this target appeared in the input secondary target file
PRIORITY_INIT                     int64                             Initial priority for target calculated across target selection bitmasks and OBSCONDITIONS
SUBPRIORITY                       float64                           Random subpriority [0-1] to break assignment ties
NUMOBS_INIT                       int64                             Initial number of observations for target calculated across target selection bitmasks and OBSCONDITIONS
OBSCONDITIONS                     int64                             Flag target to be observed in combinations of dark/bright observing layer
SCND_TARGET_INIT                  int64                             Duplication of ``SCND_TARGET`` column (used for internal bookkeeping)
PRIM_MATCH                        logical                           ``True`` if a secondary target matches a primary target
================================= =========== ===================== ===================

.. _`LS`: https://www.legacysurvey.org/dr9/catalogs/
.. _`ellipticity component`: https://www.legacysurvey.org/dr9/catalogs/
.. _`Release`: https://www.legacysurvey.org/release/
.. _`Morphological Model`: https://www.legacysurvey.org/dr9/catalogs/
.. _`Tycho-2`: https://heasarc.nasa.gov/W3Browse/all/tycho2.html
.. _`Gaia`: https://gea.esac.esa.int/archive/documentation//GDR2/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html
.. _`SFD98`: http://ui.adsabs.harvard.edu/abs/1998ApJ...500..525S
.. _`LS DR9 bitmasks page`: https://www.legacysurvey.org/dr9/bitmasks/
.. _`SGA`: https://github.com/moustakas/SGA

Notes
=====

The general user will likely not find the ``priminfo`` files useful. They
are generated for internal bookkeeping to track whether a secondary target
is a "standalone" secondary target or is instead allowed to be merged with
a DESI primary target.
