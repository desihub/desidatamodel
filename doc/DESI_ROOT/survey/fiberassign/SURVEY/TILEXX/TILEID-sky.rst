===============
TILEID-sky.fits
===============

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``{TILEID}-sky.fits``, where ``{TILEID}`` is the zero-padded,
    6-digit TILED.
:Regex: ``[0-9]{6}-sky\.fits``
:File Type: FITS, 23 MB

Contents
========

====== =========== ======== ===================
Number EXTNAME     Type     Contents
====== =========== ======== ===================
HDU0_              IMAGE    Empty HDU
HDU1_  SKY_TARGETS BINTABLE *Brief Description*
====== =========== ======== ===================


FITS Header Units
=================

HDU0
----

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = SKY_TARGETS

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =======================
    KEY    Example Value Type Comment
    ====== ============= ==== =======================
    NAXIS1 152           int  width of table in bytes
    NAXIS2 163775        int  number of rows in table
    SUPP   F             bool
    DR     9             int
    ====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

================ ======= ============ ========================================================================================================
Name             Type    Units        Description
================ ======= ============ ========================================================================================================
RELEASE          int32                Imaging surveys release ID
BRICKID          int32                Brick ID from tractor input
BRICKNAME        char[8]              Brick name from tractor input
BRICK_OBJID      int32                Imaging Surveys OBJID on that brick
RA               float64 deg          Barycentric Right Ascension in ICRS
DEC              float64 deg          Barycentric declination in ICRS
BLOBDIST         float32 pix          label for field   7
FIBERFLUX_G      float32 nanomaggy    Predicted g-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERFLUX_R      float32 nanomaggy    Predicted r-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERFLUX_Z      float32 nanomaggy    Predicted z-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERFLUX_IVAR_G float32 nanomaggy^-2 label for field  11
FIBERFLUX_IVAR_R float32 nanomaggy^-2 label for field  12
FIBERFLUX_IVAR_Z float32 nanomaggy^-2 label for field  13
TARGETID         int64                Unique DESI target ID
DESI_TARGET      int64                DESI (dark time program) target selection bitmask
BGS_TARGET       int64                BGS (Bright Galaxy Survey) target selection bitmask
MWS_TARGET       int64                Milky Way Survey targeting bits
SUBPRIORITY      float64              Random subpriority [0-1) to break assignment ties
OBSCONDITIONS    int64                Bitmask of allowed observing conditions
PRIORITY_INIT    int64                Target initial priority from target selection bitmasks and OBSCONDITIONS
NUMOBS_INIT      int64                Initial number of observations for target calculated across target selection bitmasks and OBSCONDITIONS
HPXPIXEL         int64                HEALPixel containing this location at NSIDE=64 in the NESTED scheme
PLATE_RA         float64 deg          Barycentric Right Ascension in ICRS to be used by PlateMaker
PLATE_DEC        float64 deg          Barycentric Declination in ICRS to be used by PlateMaker
================ ======= ============ ========================================================================================================


Notes and Examples
==================

Some units in this file do not conform to the FITS standard:

* nanomaggy^-2 is incorrectly recorded as 1/nanomaggy^2

Such issues can typically be fixed by parsing the unit through astropy after reading in a Table, e.g.:

.. code-block:: python

    import astropy.units as u
    from astropy.table import Table
    objs = Table.read(filename, 1)
    u.Unit(str(objs["FIBERFLUX_IVAR_G"].unit))
