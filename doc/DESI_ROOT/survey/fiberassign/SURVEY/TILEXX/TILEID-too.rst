===============
TILEID-too.fits
===============

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``{TILEID}-too.fits``, where ``{TILEID}`` is the zero-padded,
    6-digit TILED.
:Regex: ``[0-9]{6}-too\.fits``
:File Type: FITS, 19 KB

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    Empty HDU
HDU1_  TARGETS BINTABLE *Brief Description*
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

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

    ======== ============= ======= =======================
    KEY      Example Value Type    Comment
    ======== ============= ======= =======================
    NAXIS1   223           int     width of table in bytes
    NAXIS2   1             int     number of rows in table
    SURVEY   main          str
    RESOLVE  T             bool
    MASKBITS T             bool
    BACKUP   F             bool
    NOSEC    F             bool
    DR       None          Unknown
    ======== ============= ======= =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

============================= ======== ========= =======================================================================================================
Name                          Type     Units     Description
============================= ======== ========= =======================================================================================================
RA                            float64  deg       Barycentric Right Ascension in ICRS
DEC                           float64  deg       Barycentric declination in ICRS
PMRA                          float64  mas / yr  proper motion in the +RA direction (already including cos(dec))
PMDEC                         float64  mas / yr  Proper motion in the +Dec direction
REF_EPOCH                     float64  yr        Reference epoch for Gaia/Tycho astrometry. Typically 2015.5 for Gaia
FLUX_G                        float32  nanomaggy Flux in the Legacy Survey g-band (AB)
FLUX_R                        float32  nanomaggy Flux in the Legacy Survey r-band (AB)
FLUX_Z                        float32  nanomaggy Flux in the Legacy Survey z-band (AB)
PARALLAX                      float32  mas       Reference catalog parallax
GAIA_PHOT_G_MEAN_MAG          float32  mag       Gaia G band magnitude
GAIA_PHOT_BP_MEAN_MAG         float32  mag       Gaia BP band magnitude
GAIA_PHOT_RP_MEAN_MAG         float32  mag       Gaia RP band magnitude
GAIA_ASTROMETRIC_EXCESS_NOISE float32            Gaia astrometric excess noise
TARGETID                      int64              Unique DESI target ID
DESI_TARGET                   int64              DESI (dark time program) target selection bitmask
SCND_TARGET                   int64              Target selection bitmask for secondary programs
SCND_ORDER                    int32              label for field  17
PRIORITY_INIT                 int64              Target initial priority from target selection bitmasks and OBSCONDITIONS
SUBPRIORITY                   float64            Random subpriority [0-1) to break assignment ties
NUMOBS_INIT                   int64              Initial number of observations for target calculated across target selection bitmasks and OBSCONDITIONS
OBSCONDITIONS                 int64              Bitmask of allowed observing conditions
CHECKER                       char[5]            label for field  22
TOO_TYPE                      char[5]            label for field  23
TOO_PRIO                      char[2]            label for field  24
OCLAYER                       char[6]            label for field  25
MJD_BEGIN                     float64  d         label for field  26
MJD_END                       float64  d         label for field  27
TOOID                         int64              label for field  28
TIMESTAMP                     char[25] s         UTC/ISO time at which the target state was updated
PLATE_RA                      float64  deg       Barycentric Right Ascension in ICRS to be used by PlateMaker
PLATE_DEC                     float64  deg       Barycentric Declination in ICRS to be used by PlateMaker
PLATE_REF_EPOCH               float64            label for field  32
============================= ======== ========= =======================================================================================================


Notes and Examples
==================

Some units in this file do not conform to the FITS standard:

* d is incorrectly recorded as day

Such issues can typically be fixed by parsing the unit through astropy after reading in a Table, e.g.:

.. code-block:: python

    import astropy.units as u
    from astropy.table import Table
    objs = Table.read(filename, 1)
    u.Unit(str(objs["MJD_END"].unit))
