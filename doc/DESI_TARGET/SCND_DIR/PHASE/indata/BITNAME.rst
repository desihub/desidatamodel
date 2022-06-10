=======================
input secondary targets
=======================

:Summary: DESI secondary target input files contain the targets provided with a
   given secondary proposal. They can consist of either a binary fits table
   or a text file.
:Naming Convention: ``BITNAME.fits`` or ``BITNAME.txt``,
   where ``BITNAME`` matches the name of the secondary targeting bit used by the desitarget
   pipeline for a given survey phase (see the desitarget GitHub repository for, `e.g.`
   the `sv1`_ or `main`_ secondary target bitmasks).
:Regex: ``[a-zA-Z]+\.fits`` or ``[a-zA-Z]+\.txt``
:File Type: FITS or text, 10 KB - 900 MB

Contents (FITS version; see notes, below, for text version)
===========================================================

====== ======= ======== ============
Number EXTNAME Type     Contents
====== ======= ======== ============
HDU0_  PRIMARY IMAGE    Empty
HDU1_  NONE    BINTABLE Input secondary targets
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

EXTNAME = NONE

Input secondary targets

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~


.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ============= ==== ==================================
    KEY      Example Value Type Comment
    ======== ============= ==== ==================================
    NAXIS1   29            int  width of table in bytes
    NAXIS2   2772483       int  number of rows in table
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
REF_EPOCH                         float32     yr                    Astrometric reference epoch. Defaults to 2015.5.
OVERRIDE                          bool                              If ``True`` do not match to and accept an existing primary target. Instead, always generate a new ``TARGETID``.
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
.. _`sv1`: https://github.com/desihub/desitarget/blob/2.5.0/py/desitarget/sv1/data/sv1_targetmask.yaml#L155-L226
.. _`main`: https://github.com/desihub/desitarget/blob/2.5.0/py/desitarget/data/targetmask.yaml#L131-L182

Notes
=====

For .fits files, a subset of the columns must correspond to the
`Required Data Table Columns` listed above. Any other columns can exist
and can be populated with any values.

For .txt files the first 6 columns must correspond to the
`Required Data Table Columns` listed above. Subsequent columns
can contain any additional information. The # may be included as
a comment card. For objects with low proper motion, zero can
be passed for the proper motion columns. If zero is passed for
``REF_EPOCH``, it will be interpreted to be 2015.5.
