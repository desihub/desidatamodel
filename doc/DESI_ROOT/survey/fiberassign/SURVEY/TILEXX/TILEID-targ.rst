================
TILEID-targ.fits
================

:Summary: This file contains the primary science targets covered by the tile disk-footprint.
:Naming Convention: ``{TILEID}-targ.fits``, where ``{TILEID}`` is the zero-padded,
    6-digit TILED.
:Regex: ``[0-9]{6}-targ\.fits``
:File Type: FITS, 11 MB

Contents
========

====== ======= ======== ===========================================================
Number EXTNAME Type     Contents
====== ======= ======== ===========================================================
HDU0_          IMAGE    Empty HDU
HDU1_  TARGETS BINTABLE Primary science targets covered by the tile disk-footprint.
====== ======= ======== ===========================================================


FITS Header Units
=================

HDU0
----

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = TARGETS

Primary science targets covered by the tile disk-footprint: those are read
from the MTL ledgers and desitarget catalogs and provided as input to fiberassign.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ============= ======= =======================
    KEY      Example Value Type    Comment
    ======== ============= ======= =======================
    NAXIS1   382           int     width of table in bytes
    NAXIS2   30866         int     number of rows in table
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

===================== ======== ============ =======================================================================================================================================
Name                  Type     Units        Description
===================== ======== ============ =======================================================================================================================================
RELEASE               int16                 Imaging surveys release ID
BRICKID               int32                 Brick ID from tractor input
BRICKNAME             char[8]               Brick name from tractor input
BRICK_OBJID           int32                 Imaging Surveys OBJID on that brick
MORPHTYPE             char[4]               Imaging Surveys morphological type from Tractor
EBV                   float32  mag          Galactic extinction E(B-V) reddening from SFD98
FLUX_G                float32  nanomaggy    Flux in the Legacy Survey g-band (AB)
FLUX_R                float32  nanomaggy    Flux in the Legacy Survey r-band (AB)
FLUX_Z                float32  nanomaggy    Flux in the Legacy Survey z-band (AB)
FLUX_IVAR_G           float32  nanomaggy^-2 Inverse variance of FLUX_G (AB)
FLUX_IVAR_R           float32  nanomaggy^-2 Inverse variance of FLUX_R (AB)
FLUX_IVAR_Z           float32  nanomaggy^-2 Inverse variance of FLUX_Z (AB)
FLUX_W1               float32  nanomaggy    WISE flux in W1 (AB)
FLUX_W2               float32  nanomaggy    WISE flux in W2 (AB)
FLUX_IVAR_W1          float32  nanomaggy^-2 Inverse variance of FLUX_W1 (AB)
FLUX_IVAR_W2          float32  nanomaggy^-2 Inverse variance of FLUX_W2 (AB)
FIBERFLUX_G           float32  nanomaggy    Predicted g-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERFLUX_R           float32  nanomaggy    Predicted r-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERFLUX_Z           float32  nanomaggy    Predicted z-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERTOTFLUX_G        float32  nanomaggy    Predicted g-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
FIBERTOTFLUX_R        float32  nanomaggy    Predicted r-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
FIBERTOTFLUX_Z        float32  nanomaggy    Predicted z-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
MASKBITS              int16                 Bitwise mask from the imaging indicating potential issue or blending
SHAPE_R               float32  arcsec       Half-light radius of galaxy model (&gt;0)
SHAPE_E1              float32               Ellipticity component 1 of galaxy model for galaxy type MORPHTYPE
SHAPE_E2              float32               Ellipticity component 2 of galaxy model for galaxy type MORPHTYPE
SERSIC                float32               Power-law index for the Sersic profile model (MORPHTYPE=&#x27;SER&#x27;)
REF_ID                int64                 Tyc1*1,000,000+Tyc2*10+Tyc3 for Tycho-2; ``sourceid`` for Gaia DR2
REF_CAT               char[2]               Reference catalog source for star: &#x27;T2&#x27; for Tycho-2, &#x27;G2&#x27; for Gaia DR2, &#x27;L2&#x27; for the SGA, empty otherwise
GAIA_PHOT_G_MEAN_MAG  float32  mag          Gaia G band magnitude
GAIA_PHOT_BP_MEAN_MAG float32  mag          Gaia BP band magnitude
GAIA_PHOT_RP_MEAN_MAG float32  mag          Gaia RP band magnitude
PHOTSYS               char[1]               &#x27;N&#x27; for the MzLS/BASS photometric system, &#x27;S&#x27; for DECaLS
TARGETID              int64                 Unique DESI target ID
RA                    float64  deg          Barycentric Right Ascension in ICRS
DEC                   float64  deg          Barycentric declination in ICRS
REF_EPOCH             float32  yr           Reference epoch for Gaia/Tycho astrometry. Typically 2015.5 for Gaia
PARALLAX              float32  mas          Reference catalog parallax
PMRA                  float32  mas / yr     proper motion in the +RA direction (already including cos(dec))
PMDEC                 float32  mas / yr     Proper motion in the +Dec direction
DESI_TARGET           int64                 DESI (dark time program) target selection bitmask
BGS_TARGET            int64                 BGS (Bright Galaxy Survey) target selection bitmask
MWS_TARGET            int64                 Milky Way Survey targeting bits
SUBPRIORITY           float64               Random subpriority [0-1) to break assignment ties
OBSCONDITIONS         int32                 Bitmask of allowed observing conditions
PRIORITY_INIT         int64                 Target initial priority from target selection bitmasks and OBSCONDITIONS
NUMOBS_INIT           int64                 Initial number of observations for target calculated across target selection bitmasks and OBSCONDITIONS
SCND_TARGET           int64                 Target selection bitmask for secondary programs
NUMOBS_MORE           int64                 Number of additional observations needed
NUMOBS                int64                 Number of spectroscopic observations (on this specific, single tile)
Z                     float64               Redshift measured by Redrock
ZWARN                 int64                 Redshift warning bitmask from Redrock
ZTILEID               int32                 ID of tile that most recently updated target&#x27;s state
Z_QN                  float64               Redshift measured by QuasarNET using line with highest confidence
IS_QSO_QN             int16                 Spectroscopic classification from QuasarNET (1 for a quasar)
DELTACHI2             float64               chi2 difference between first- and second-best redrock template fits
TARGET_STATE          char[30]              Combination of target class and its current observational state
TIMESTAMP             char[25] s            UTC/ISO time at which the target state was updated
VERSION               char[14]              Tag of desitarget used to create the target catalog
PRIORITY              int64                 Target current priority
PLATE_RA              float64  deg          Barycentric Right Ascension in ICRS to be used by PlateMaker
PLATE_DEC             float64  deg          Barycentric Declination in ICRS to be used by PlateMaker
PLATE_REF_EPOCH       float32  yr           Copy of REF_EPOCH to be used by PlateMaker
===================== ======== ============ =======================================================================================================================================


Notes and Examples
==================

For the SURVEY=cmx m33 tile (TILEID=80615) tile and all the SURVEY=sv1 tiles (except TILEID=80971-80976, the dc3r2 ones), proper-motion correction was applied at the :doc:`fiberassign </DESI_TARGET/fiberassign/tiles/TILES_VERSION/TILEXX/fiberassign-TILEID>` design step; thus the following columns can have different values than in the :doc:`desitarget products </DESI_TARGET/TARG_DIR/DR/VERSION/targets/PHASE/RESOLVE/OBSCON/PHASEtargets-OBSCON-RESOLVE-hp-HP>`: ``TARGET_RA``, ``TARGET_DEC``, ``REF_EPOCH``, ``PLATE_RA``, ``PLATE_DEC``, and ``PLATE_REF_EPOCH``.

Some units in this file do not conform to the FITS standard:

* nanomaggy^-2 is incorrectly recorded as 1/nanomaggy^2

Such issues can typically be fixed by parsing the unit through astropy after reading in a Table, e.g.:

.. code-block:: python

    import astropy.units as u
    from astropy.table import Table
    objs = Table.read(filename, 1)
    u.Unit(str(objs["FLUX_IVAR_Z"].unit))
