============================
DATA clustering catalogs
============================

:Summary: For each target type, LSS catalogs for the data, ready to be used for clustering measurements, are provided.
:Naming Convention: ``{TARGET}_{PHOTSYS}_clustering.dat.fits``, where ``{TARGET}`` is the target: ``QSO``, ``ELG``, ``ELG_LOPnotqso``, ``LRG``, ``LRG+ELG_LOPnotqso``,
                    for dark or ``BGS_ANY``, ``BGS_BRIGHT``, ``BGS_BRIGHT-21.5`` for bright. ``{PHOTSYS}`` is the photometric region ``NGC`` or ``SGC`` or the combination of both if not explicitly shown.
:Regex: ``[a-zA-Z_+]+[A-Z_]{0,4}_clustering.dat.fits`` 
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

This HDU has no non-standard required keywords.

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

==================== ======== ========= =====================================================================================================================
Name                 Type     Units     Description
==================== ======== ========= =====================================================================================================================
TARGETID             int64              Unique DESI target ID
Z                    float64            Redshift measured by Redrock
NTILE                int64              Number of tiles target was available on
RA                   float64  deg       Barycentric Right Ascension in ICRS
DEC                  float64  deg       Barycentric declination in ICRS
PHOTSYS              char[1]            N for the MzLS/BASS photometric system, S for DECaLS
FRAC_TLOBS_TILES     float64            Fraction of targets with the same TILES value that contribute to FRACZ_TILELOCID
WEIGHT_ZFAIL         float64            Should be all 1 at this point for main survey
WEIGHT_SN            float64            Imaging systematics weights derived with the sysnet NN regression method
WEIGHT_RF [1]_       float64            Imaging systematics weights derived with the regressis random forest regression method
WEIGHT_SN [1]_       float64            Imaging systematics weights derived with the sysnet NN regression method
WEIGHT_SYS           float64            Correction for fluctuations in projected density with imaging conditions, from random forrest method
WEIGHT               float64            The combination of all weights to use
WEIGHT_COMP          float64            Completeness weight accounting for the local chance of being assigned a fiber
NX                   float64            Estimated mean number density given the redshift and number of overlapping tiles (NTILE)
WEIGHT_FKP           float64            1/(1+NX*P0), with P0 different for each tracer
WEIGHT_RESCALED [1]_ float64            Rescaled weight when unifying different targets into a single frame              
EFFECTIVE_BIAS [1]_  float64            Effective bias used to weight the galaxy when unifying several tracers
flux_g_dered [1]_    float32  nanomaggy (lower or uppercase) Flux in the g-band after correcting for Galactic extinction (AB system) 
flux_r_dered [1]_    float32  nanomaggy (lower or uppercase) Flux in the r-band after correcting for Galactic extinction (AB system)
flux_z_dered [1]_    float32  nanomaggy (lower or uppercase) Flux in the z-band after correcting for Galactic extinction (AB system)
flux_w1_dered [1]_   float32  nanomaggy (lower or uppercase) Flux in the WISE W1-band after correcting for Galactic extinction (AB system)
flux_w2_dered [1]_   float32  nanomaggy (lower or uppercase) Flux in the WISE W2-band after correcting for Galactic extinction (AB system)
==================== ======== ========= =====================================================================================================================

.. [1] Optional columns. WEIGHT_RESCALED and EFFECTIVE_BIAS only when unifying targets into a single frame (e.g.: LRG+ELG_LOPnotqso)
                         flux_g_dered, flux_r_dered, flux_z_dered, flux_w1_dered, flux_w2_dered only present in BGS samples

Notes and Examples
==================

