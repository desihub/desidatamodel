===============
TILEID-too.fits
===============

:Summary: This file contains the Target-of-Opportunity targets covered by the tile disk-footprint.
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
HDU1_  TARGETS BINTABLE Target-of-Opportunity targets covered by the tile disk-footprint.
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

Target-of-Opportunity targets covered by the tile disk-footprint:
those are read from the MTL ledgers and desitarget catalogs and provided
as input to fiberassign.

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
SCND_ORDER                    int32              Number of row for target entry in secondary file (placeholder; needed by fiberassign)
PRIORITY_INIT                 int64              Target initial priority from target selection bitmasks and OBSCONDITIONS
SUBPRIORITY                   float64            Random subpriority [0-1) to break assignment ties
NUMOBS_INIT                   int64              Initial number of observations for target calculated across target selection bitmasks and OBSCONDITIONS
OBSCONDITIONS                 int64              Bitmask of allowed observing conditions
CHECKER                       char[5]            Initials of researcher who vetted the target
TOO_TYPE                      char[5]            Either "TILE" for a special tile or "FIBER" for a fiber-override ToO
TOO_PRIO                      char[2]            Either "HI" for a very-high-priority target or "LO" for a very-low-priority target
OCLAYER                       char[6]            Either "DARK" for dark-time or "BRIGHT" to observe in either bright- or dark-time
MJD_BEGIN                     float64  d         Start of the allowed observing window for this target (Modified Julian Date)
MJD_END                       float64  d         End of the allowed observing window for this target (Modified Julian Date)
TOOID                         int64              ID for this target assigned by the ``CHECKER``
TIMESTAMP                     char[25] s         UTC/ISO time at which the target state was updated
PLATE_RA                      float64  deg       Barycentric Right Ascension in ICRS to be used by PlateMaker
PLATE_DEC                     float64  deg       Barycentric Declination in ICRS to be used by PlateMaker
PLATE_REF_EPOCH               float64  yr        Copy of REF_EPOCH to be used by PlateMaker
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
