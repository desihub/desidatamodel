===============
TILEID-gfa.fits
===============

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``{TILEID}-gfa.fits``, where ``{TILEID}`` is the zero-padded,
    6-digit TILED.
:Regex: ``[0-9]{6}-gfa\.fits``
:File Type: FITS, 6 MB

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    *Brief Description*
HDU1_  TARGETS BINTABLE *Brief Description*
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

*Summarize the contents of this HDU.*

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = TARGETS

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ============= ==== =======================
    KEY      Example Value Type Comment
    ======== ============= ==== =======================
    NAXIS1   164           int  width of table in bytes
    NAXIS2   43904         int  number of rows in table
    SURVEY   main          str
    RESOLVE  T             bool
    MASKBITS T             bool
    BACKUP   F             bool
    NOSEC    F             bool
    DR       9             int
    ======== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

================================= ======= ============= ===================
Name                              Type    Units         Description
================================= ======= ============= ===================
RELEASE                           int32                 label for field   1
TARGETID                          int64                 label for field   2
BRICKID                           int32                 label for field   3
BRICK_OBJID                       int32                 label for field   4
RA                                float64 deg           label for field   5
DEC                               float64 deg           label for field   6
RA_IVAR                           float32 deg^-2        label for field   7
DEC_IVAR                          float32 deg^-2        label for field   8
MORPHTYPE                         char[4]               label for field   9
MASKBITS                          int16                 label for field  10
FLUX_G                            float32 nanomaggy     label for field  11
FLUX_R                            float32 nanomaggy     label for field  12
FLUX_Z                            float32 nanomaggy     label for field  13
FLUX_IVAR_G                       float32 nanomaggy^-2  label for field  14
FLUX_IVAR_R                       float32 nanomaggy^-2  label for field  15
FLUX_IVAR_Z                       float32 nanomaggy^-2  label for field  16
REF_ID                            int64                 label for field  17
REF_CAT                           char[2]               label for field  18
REF_EPOCH                         float32 yr            label for field  19
PARALLAX                          float32 mas           label for field  20
PARALLAX_IVAR                     float32 mas^-2        label for field  21
PMRA                              float32 mas / yr      label for field  22
PMDEC                             float32 mas / yr      label for field  23
PMRA_IVAR                         float32 yr^2 / mas^2  label for field  24
PMDEC_IVAR                        float32 yr^2 / mas^2  label for field  25
GAIA_PHOT_G_MEAN_MAG              float32 mag           label for field  26
GAIA_PHOT_G_MEAN_FLUX_OVER_ERROR  float32               label for field  27
GAIA_PHOT_BP_MEAN_MAG             float32 mag           label for field  28
GAIA_PHOT_BP_MEAN_FLUX_OVER_ERROR float32               label for field  29
GAIA_PHOT_RP_MEAN_MAG             float32 mag           label for field  30
GAIA_PHOT_RP_MEAN_FLUX_OVER_ERROR float32               label for field  31
GAIA_ASTROMETRIC_EXCESS_NOISE     float32               label for field  32
URAT_ID                           int64                 label for field  33
URAT_SEP                          float32 arcsec        label for field  34
GAIA_PHOT_G_N_OBS                 int32                 label for field  35
HPXPIXEL                          int64                 label for field  36
================================= ======= ============= ===================


Notes and Examples
==================

Some units in this file do not conform to the FITS standard:

* deg^-2 is incorrectly recorded as 1/deg^2
* nanomaggy^-2 is incorrectly recorded as 1/nanomaggy^2
* mas^-2 is incorrectly recorded as 1/mas^2

Such issues can typically be fixed by parsing the unit through astropy after reading in a Table, e.g.:

.. code-block:: python

    import astropy.units as u
    from astropy.table import Table
    objs = Table.read(filename, 1)
    u.Unit(str(objs["RA_IVAR"].unit))
