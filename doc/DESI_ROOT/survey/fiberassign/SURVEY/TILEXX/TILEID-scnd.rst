================
TILEID-scnd.fits
================

:Summary: This file contains the secondary targets covered by the tile disk-footprint.
:Naming Convention: ``{TILEID}-scnd.fits``, where ``{TILEID}`` is the zero-padded,
    6-digit TILED.
:Regex: ``[0-9]{6}-scnd\.fits``
:File Type: FITS, 1 MB

Contents
========

====== ======= ======== =====================================================
Number EXTNAME Type     Contents
====== ======= ======== =====================================================
HDU0_          IMAGE    Empty HDU
HDU1_  TARGETS BINTABLE Secondary targets covered by the tile disk-footprint.
====== ======= ======== =====================================================


FITS Header Units
=================

HDU0
----

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = TARGETS

Secondary targets covered by the tile disk-footprint:
those are read from the MTL ledgers and desitarget catalogs and provided as
input to fiberassign.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ============= ======= =======================
    KEY      Example Value Type    Comment
    ======== ============= ======= =======================
    NAXIS1   275           int     width of table in bytes
    NAXIS2   4751          int     number of rows in table
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

===================== ======== ========= =======================================================================================================
Name                  Type     Units     Description
===================== ======== ========= =======================================================================================================
FLUX_G                float32  nanomaggy Flux in the Legacy Survey g-band (AB)
FLUX_R                float32  nanomaggy Flux in the Legacy Survey r-band (AB)
FLUX_Z                float32  nanomaggy Flux in the Legacy Survey z-band (AB)
GAIA_PHOT_G_MEAN_MAG  float32  mag       Gaia G band magnitude
GAIA_PHOT_BP_MEAN_MAG float32  mag       Gaia BP band magnitude
GAIA_PHOT_RP_MEAN_MAG float32  mag       Gaia RP band magnitude
TARGETID              int64              Unique DESI target ID
RA                    float64  deg       Barycentric Right Ascension in ICRS
DEC                   float64  deg       Barycentric declination in ICRS
PMRA                  float32  mas / yr  proper motion in the +RA direction (already including cos(dec))
PMDEC                 float32  mas / yr  Proper motion in the +Dec direction
REF_EPOCH             float32  yr        Reference epoch for Gaia/Tycho astrometry. Typically 2015.5 for Gaia
PARALLAX              float32  mas       Reference catalog parallax
DESI_TARGET           int64              DESI (dark time program) target selection bitmask
SCND_TARGET           int64              Target selection bitmask for secondary programs
SUBPRIORITY           float64            Random subpriority [0-1) to break assignment ties
OBSCONDITIONS         int32              Bitmask of allowed observing conditions
PRIORITY_INIT         int64              Target initial priority from target selection bitmasks and OBSCONDITIONS
NUMOBS_INIT           int64              Initial number of observations for target calculated across target selection bitmasks and OBSCONDITIONS
BGS_TARGET            int64              BGS (Bright Galaxy Survey) target selection bitmask
MWS_TARGET            int64              Milky Way Survey targeting bits
NUMOBS_MORE           int64              Number of additional observations needed
NUMOBS                int64              Number of spectroscopic observations (on this specific, single tile)
Z                     float64            Redshift measured by Redrock
ZWARN                 int64              Redshift warning bitmask from Redrock
ZTILEID               int32              ID of tile that most recently updated target's state
Z_QN                  float64            Redshift measured by QuasarNET using line with highest confidence
IS_QSO_QN             int16              Spectroscopic classification from QuasarNET (1 for a quasar)
DELTACHI2             float64            chi2 difference between first- and second-best redrock template fits
TARGET_STATE          char[30]           Combination of target class and its current observational state
TIMESTAMP             char[25] s         UTC/ISO time at which the target state was updated
VERSION               char[14]           Tag of desitarget used to create the target catalog
PRIORITY              int64              Target current priority
PLATE_RA              float64  deg       Barycentric Right Ascension in ICRS to be used by PlateMaker
PLATE_DEC             float64  deg       Barycentric Declination in ICRS to be used by PlateMaker
PLATE_REF_EPOCH       float32  yr        Copy of REF_EPOCH to be used by PlateMaker
===================== ======== ========= =======================================================================================================


Notes and Examples
==================

For the SURVEY=cmx m33 tile (TILEID=80615) tile and all the SURVEY=sv1 tiles (except TILEID=80971-80976, the dc3r2 ones), proper-motion correction was applied at the :doc:`fiberassign </DESI_TARGET/fiberassign/tiles/TILES_VERSION/TILEXX/fiberassign-TILEID>` design step; thus the following columns can have different values than in the :doc:`desitarget products </DESI_TARGET/TARG_DIR/DR/VERSION/targets/PHASE/RESOLVE/OBSCON/PHASEtargets-OBSCON-RESOLVE-hp-HP>`: ``TARGET_RA``, ``TARGET_DEC``, ``REF_EPOCH``, ``PLATE_RA``, ``PLATE_DEC``, and ``PLATE_REF_EPOCH``.
