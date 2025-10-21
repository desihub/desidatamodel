===============================
AltMTL MOCK clustering catalogs
===============================

:Summary: For each target type, LSS catalogs for the data, ready to be used for clustering measurements.
:Naming Convention: ``{TARGET}_{GALCAP}_clustering.dat.fits``, where ``{TARGET}`` is the target: ``QSO``, ``ELG_LOPnotqso`` or ``LRG`` for dark or ``BGS_BRIGHT-21.5`` or ``BGS_BRIGHT`` for bright. ``{GALCAP}`` is the Galactic hemisphere region ``NGC`` or ``SGC``.
:Regex: ``[A-Za-z0-9._+-]+_(NGC|SGC)_clustering\.dat\.fits``
:File Type: FITS, 237 MB

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    Empty
HDU1_  LSS     BINTABLE Catalog data
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

Empty HDU.

HDU1
----

EXTNAME = LSS

LSS catalogs for clustering measurements

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =======================
    KEY    Example Value Type Comment
    ====== ============= ==== =======================
    NAXIS1 137           int  width of table in bytes
    NAXIS2 1821322       int  number of rows in table
    DESIDR dr1           str  DESI Data Release
    ====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

================ ======= ===== ====================================================================================================
Name             Type    Units Description
================ ======= ===== ====================================================================================================
TARGETID         int64         Unique DESI target ID
DEC              float64 deg   Barycentric declination in ICRS
RA               float64 deg   Barycentric Right Ascension in ICRS
Z                float32       Redshift measured by Redrock
NTILE            int64         Number of tiles target was available on
PHOTSYS          char[1]       N for the MzLS/BASS photometric system, S for DECaLS
FRAC_TLOBS_TILES float64       Fraction of targets with the same TILES value that contribute to FRACZ_TILELOCID
WEIGHT           float64       The combination of all weights to use
WEIGHT_ZFAIL     float64       Should be all 1 at this point for main survey
WEIGHT_COMP      float64       Completeness weight accounting for the local chance of being assigned a fiber
WEIGHT_SYS       float64       Correction for fluctuations in projected density with imaging conditions, from random forrest method
NX               float64       Estimated mean number density given the redshift and number of overlapping tiles (NTILE)
WEIGHT_FKP       float64       1/(1+NZ*P0), with P0 different for each tracer
WEIGHT_IMLIN     float64       Imaging systematics weights derived with the eBOSS linear regression method
================ ======= ===== ====================================================================================================

