================================================
mock FFA and COMPLETE RANDOM clustering catalogs
================================================

:Summary: For each target type, LSS catalogs for the randoms, ready to be used for clustering measurements, are provided.
:Naming Convention: ``{TARGET}_{GALCAP}_{RANN}_clustering.ran.fits``, where ``{TARGET}`` is the target: ``QSO``, ``ELG_LOP`` or ``LRG``
                    for dark or ``BGS_BRIGHT-21.5`` for bright. ``{GALCAP}`` is the Galactic hemisphere region ``NGC`` or ``SGC`` or the combination of both if not explicitly shown. And ``{RANN}`` is the number for the random file (18 total, numbered 0 through 17). Each are random with respect to each other.
:Regex: ``[A-Za-z0-9._+-]+_(NGC|SGC)_[0-9]+_clustering\.ran\.fits``
:File Type: FITS, 1 GB

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    Empty
HDU1_  LSS     BINTABLE Random data
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

Empty HDU.

HDU1
----

EXTNAME = LSS

Random catalog for clustering statistics

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =======================
    KEY    Example Value Type Comment
    ====== ============= ==== =======================
    NAXIS1 109           int  width of table in bytes
    NAXIS2 18677216      int  number of rows in table
    DESIDR dr1           str  DESI Data Release
    ====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

===================== ======= ===== ====================================================================
Name                  Type    Units Description
===================== ======= ===== ====================================================================
RA                    float64 deg   Barycentric Right Ascension in ICRS
DEC                   float64 deg   Barycentric declination in ICRS
Z                     float64       Redshift measured by Redrock
WEIGHT                float64       The combination of all weights to use
TARGETID_DATA         float64       For randoms and mocks: Unique DESI target ID of associated TILELOCID
WEIGHT_FKP            float64       1/(1+NZ*P0), with P0 different for each tracer
TARGETID [1]_         int64         Unique DESI target ID
NTILE [1]_            int64         Number of tiles target was available on
PHOTSYS [1]_          char[1]       N for the MzLS/BASS photometric system, S for DECaLS
WEIGHT_COMP [1]_      float64       Completeness weight accounting for the local chance of being assigned a fiber
WEIGHT_SYS [1]_       float64       Correction for fluctuations in projected density with imaging conditions, from random forrest method
WEIGHT_ZFAIL [1]_     float64       Should be all 1 at this point for main survey
FRAC_TLOBS_TILES [1]_ float64       Fraction of targets with the same TILES value that contribute to FRACZ_TILELOCID
===================== ======= ===== ====================================================================

.. [1] Optional
