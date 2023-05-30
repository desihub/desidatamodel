===============
TILEID-sky.fits
===============

:Summary: This file contains the sky targets covered by the tile disk-footprint.
:Naming Convention: ``{TILEID}-sky.fits``, where ``{TILEID}`` is the zero-padded,
    6-digit TILED.
:Regex: ``[0-9]{6}-sky\.fits``
:File Type: FITS, 23 MB

Contents
========

====== =========== ======== ===============================================
Number EXTNAME     Type     Contents
====== =========== ======== ===============================================
HDU0_              IMAGE    Empty HDU
HDU1_  SKY_TARGETS BINTABLE Sky targets covered by the tile disk-footprint.
====== =========== ======== ===============================================


FITS Header Units
=================

HDU0
----

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = SKY_TARGETS

Sky targets covered by the tile disk-footprint: those are read from the
desitarget catalogs and provided as input to fiberassign.

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
BLOBDIST         float32 pix          Maximum distance from a detected Legacy Surveys source
FIBERFLUX_G      float32 nanomaggy    g-band flux measured in aperture of radius 0.75 arcsec, extracted from the Legacy Surveys `coadd stacks`_
FIBERFLUX_R      float32 nanomaggy    r-band flux measured in aperture of radius 0.75 arcsec, extracted from the Legacy Surveys `coadd stacks`_
FIBERFLUX_Z      float32 nanomaggy    z-band flux measured in aperture of radius 0.75 arcsec, extracted from the Legacy Surveys `coadd stacks`_
FIBERFLUX_IVAR_G float32 nanomaggy^-2 Inverse variance of ``FIBERFLUX_G``
FIBERFLUX_IVAR_R float32 nanomaggy^-2 Inverse variance of ``FIBERFLUX_R``
FIBERFLUX_IVAR_Z float32 nanomaggy^-2 Inverse variance of ``FIBERFLUX_Z``
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

.. _`coadd stacks`: https://www.legacysurvey.org/dr9/files/#image-stacks-region-coadd

Notes and Examples
==================

The ``FIBERFLUX`` quantities use a different definition ``FIBERFLUX`` as measured
in other files.  See also the :doc:`skies files <../../../../../DESI_TARGET/TARG_DIR/DR/VERSION/skies/skies-hp-HP>` files produced by desitarget_.

.. _desitarget: https://github.com/desihub/desitarget

Some units in this file do not conform to the FITS standard:

* nanomaggy^-2 is incorrectly recorded as 1/nanomaggy^2

Such issues can typically be fixed by parsing the unit through astropy after reading in a Table, e.g.:

.. code-block:: python

    import astropy.units as u
    from astropy.table import Table
    objs = Table.read(filename, 1)
    u.Unit(str(objs["FIBERFLUX_IVAR_G"].unit))
