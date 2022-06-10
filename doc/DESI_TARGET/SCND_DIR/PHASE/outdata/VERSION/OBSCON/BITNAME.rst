========================
output secondary targets
========================

:Summary: DESI secondary target output files include a binary fits table. This table
	  contains the targets provided with a given secondary proposal, with the
	  added targeting information (`i.e.` IDs and bits) needed by the DESI pipeline.
:Naming Convention: ``BITNAME.fits``,
   where ``BITNAME`` matches the name of the secondary targeting bit used by the desitarget
   pipeline for a given survey phase (see the desitarget GitHub repository for, `e.g.`
   the `sv1`_ or `main`_ secondary target bitmasks).
:Regex: ``[a-zA-Z]+\.fits``
:File Type: FITS, 20 KB - 284 MB

Contents (FITS version; see notes, below, for text version)
===========================================================

====== ======= ======== ============
Number EXTNAME Type     Contents
====== ======= ======== ============
HDU0_  PRIMARY IMAGE    Empty
HDU1_  TARGETS BINTABLE Output secondary targets
====== ======= ======== ============

FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = TARGETS

Output secondary targets

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============= ===== ==================================
KEY      Example Value Type  Comment
======== ============= ===== ==================================
NAXIS1   89            int   width of table in bytes
NAXIS2   4838          int   number of rows in table
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

================================= =========== ================ ===================
Name                              Type        Units            Description
================================= =========== ================ ===================
RA                                float64     deg              Right ascension
DEC                               float64     deg              Declination
PMRA                              float32     mas / yr         Proper motion in the RA direction
PMDEC                             float32     mas / yr         Proper motion in the Dec direction
REF_EPOCH                         float32     yr               Astrometric reference epoch. Defaults to 2015.5.
OVERRIDE                          bool                         If ``True`` do not match to and accept an existing primary target. Instead, always generate a new ``TARGETID``.
FLUX_G                            float32     nanomaggies      `LS`_ flux from tractor input (g)
FLUX_R                            float32     nanomaggies      `LS`_ flux from tractor input (r)
FLUX_Z                            float32     nanomaggies      `LS`_ flux from tractor input (z)
PARALLAX                          float32     mas              Reference catalog parallax
GAIA_PHOT_G_MEAN_MAG              float32     mag              `Gaia`_ G band magnitude
GAIA_PHOT_BP_MEAN_MAG             float32     mag              `Gaia`_ BP band magnitude
GAIA_PHOT_RP_MEAN_MAG             float32     mag              `Gaia`_ RP band magnitude
GAIA_ASTROMETRIC_EXCESS_NOISE     float32                      `Gaia`_ astrometric excess noise
TARGETID                          int64                        Unique targeting ID
DESI_TARGET                       int64                        DESI (dark time program) target selection bitmask
SCND_TARGET                       int64                        SCND (secondary program) target selection bitmask
SCND_ORDER                        int32                        Row in which this target appeared in the input secondary target file
================================= =========== ================ ===================

.. _`LS`: https://www.legacysurvey.org/dr9/catalogs/
.. _`ellipticity component`: https://www.legacysurvey.org/dr9/catalogs/
.. _`Release`: https://www.legacysurvey.org/release/
.. _`Morphological Model`: https://www.legacysurvey.org/dr9/catalogs/
.. _`Tycho-2`: https://heasarc.nasa.gov/W3Browse/all/tycho2.html
.. _`Gaia`: https://gea.esac.esa.int/archive/documentation//GDR2/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html
.. _`SFD98`: http://ui.adsabs.harvard.edu/abs/1998ApJ...500..525S
.. _`LS DR9 bitmasks page`: https://www.legacysurvey.org/dr9/bitmasks/
.. _`SGA`: https://github.com/moustakas/SGA
.. _`sv1`: https://github.com/desihub/desitarget/blob/2.5.0/py/desitarget/sv1/data/sv1_targetmask.yaml#L155-L226
.. _`main`: https://github.com/desihub/desitarget/blob/2.5.0/py/desitarget/data/targetmask.yaml#L131-L182

