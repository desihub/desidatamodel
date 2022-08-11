===================
tiles-SPECPROD.fits
===================

:Summary: Table containing cumulative observational metadata as well as derived quantities
    estimating the observational "depth" for each target class, quoted
    in seconds of effective, idealized observing time.
:Naming Convention: ``tiles-{SPECPROD}.fits``, where ``{SPECPROD}`` is the
    official name of the full reduction, *e.g.* ``everest``.
:Regex: ``tiles-[a-z0-9_-]+.fits``
:File Type: FITS, 165 KB

Contents
========

====== ================= ======== ===================
Number EXTNAME           Type     Contents
====== ================= ======== ===================
HDU0_                    IMAGE    Empty
HDU1_  TILE_COMPLETENESS BINTABLE Per-tile metadata
====== ================= ======== ===================


FITS Header Units
=================

HDU0
----

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = TILE_COMPLETENESS

Binary table containing metadata about individual DESI tiles. This
includes cumulative observational information as well as derived quantities
estimating the observational "depth" for each target class, quoted
in seconds of effective, idealized observing time.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =====================
    KEY    Example Value Type Comment
    ====== ============= ==== =====================
    NAXIS1 218           int  length of dimension 1
    NAXIS2 732           int  length of dimension 2
    ====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

================== ======== ===== ===========
Name               Type     Units Description
================== ======== ===== ===========
TILEID             int32          Unique DESI tile ID
SURVEY             char[20]       Survey name
PROGRAM            char[6]        Program name
FAPRGRM            char[20]       PROGRAM in fiberassign file
FAFLAVOR           char[20]       FLAVOR in fiberassign file
NEXP               int64          Number of exposures used in EFFTIME estimates
EXPTIME            float64   s    Actual exposure time
TILERA             float64   deg  RA of tile given in fiberassign file
TILEDEC            float64   deg  DEC of tile given in fiberassign file
EFFTIME_ETC        float64   s    Effective exposure time for nominal conditions derived from exposure ETC data
EFFTIME_SPEC       float64   s    Effective exposure time for nominal conditions derived from the TSNR2 fits to the spectroscopy
EFFTIME_GFA        float64   s    Effective exposure time for nominal conditions derived from exposure GFA data
GOALTIME           float64   s    Goal for total effective exposure time for the tile
OBSSTATUS          char[20]       Observing conditions bitmask
LRG_EFFTIME_DARK   float64   s    Effective exposure time for nominal dark conditions inferred for LRG targets
ELG_EFFTIME_DARK   float64   s    Effective exposure time for nominal dark conditions inferred for ELG targets
BGS_EFFTIME_BRIGHT float64   s    Effective exposure time for nominal bright conditions inferred for BGS targets
LYA_EFFTIME_DARK   float64   s    Effective exposure time for nominal dark conditions inferred for LYA targets
GOALTYPE           char[20]       The intended observing conditions for the tile
MINTFRAC           float64        Minimum fraction of GOALTIME acceptable for considering a tile complete
LASTNIGHT          int32          Most recent night with a good exposure
================== ======== ===== ===========

Notes and Examples
==================

For the definition of OBSCONDITIONS please see the :doc:`bitmask documentation </bitmasks>`
page for the definition of the bits.
