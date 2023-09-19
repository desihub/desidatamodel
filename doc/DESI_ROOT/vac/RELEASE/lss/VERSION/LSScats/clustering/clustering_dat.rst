========================================
Clustering LSS catalogs for data
========================================

:Summary: For each target type, LSS catalogs for the data, ready to be used for clustering measurements, are provided.
:Naming Convention: ``{TARGET}_{PHOTSYS}_clustering.dat.fits``, where ``{TARGET}`` is the target: ``QSO``, ``ELG``, ``ELGnotqso``, ``ELG_HIP``, ``ELG_HIPnotqso``, ``LRG``, ``LRG_main``,
                    for dark or ``BGS_ANY``, ``BGS_BRIGHT`` for bright. ``{PHOTSYS}`` is the photometric region ``N`` or ``S``.
:Regex: ``[a-zA-Z_]+_[NS]_clustering.dat.fits``
:File Type: FITS, 8 MB


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

*LSS catalogs for clustering measurements*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =======================
    KEY    Example Value Type Comment
    ====== ============= ==== =======================
    NAXIS1 123           int  width of table in bytes
    NAXIS2 71051         int  number of rows in table
    DESIDR edr           str  DESI Data Release
    ====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

================== ======== ========== =====================================================================================================================================
Name               Type     Units      Description
================== ======== ========== =====================================================================================================================================
RA                 float64  deg        Target Right Ascension
DEC                float64  deg        Target declination
TARGETID           int64               Unique DESI target ID
NTILE              int64               Number of tiles target was available on
TILES              char[*]             TILEIDs of those tile, in string form separated by '-'
Z                  float64             Redshift measured by Redrock
COMP_TILE          float64             Assignment completeness for all targets of this type with the same value for TILES
ROSETTE_NUMBER     int32               Rosette number ID [0-19]
ROSETTE_R          float64  deg        Radius from the center of the rosette to the target
FRACZ_TILELOCID    float64             The fraction of targets of this type at this TILELOCID that received an observation (after forcing each target to a unique TILELOCID)
BITWEIGHTS         int64[2]            A size of two 64 bit masks that encodes which of the alternative assignment histories that the target was assigned in
PROB_OBS           float64             The number alternative assignment histories that the target was assigned in divided by 128
WEIGHT_ZFAIL       float64             Should be all 1 at this point for main survey
WEIGHT             float64             The combination of all weights to use
FLUX_G_DERED [1]_  float32  nanomaggy  Flux in the g-band after correcting for Galactic extinction (AB system)
FLUX_R_DERED [1]_  float32  nanomaggy  Flux in the r-band after correcting for Galactic extinction (AB system)
FLUX_Z_DERED [1]_  float32  nanomaggy  Flux in the z-band after correcting for Galactic extinction (AB system)
FLUX_W1_DERED [1]_ float32  nanomaggy  Flux in the WISE W1-band after correcting for Galactic extinction (AB system)
FLUX_W2_DERED [1]_ float32  nanomaggy  Flux in the WISE W2-band after correcting for Galactic extinction (AB system)
REST_GMR_0P1 [1]_  float64             Rest-frame g-r colour at redshift=0.1
KCORR_R0P1 [1]_    float64             r-band k-correction at redshift=0.1
KCORR_G0P1 [1]_    float64             g-band k-correction at redshift=0.1
KCORR_R0P0 [1]_    float64             r-band k-correction at redshift=0.0
KCORR_G0P0 [1]_    float64             g-band k-correction at redshift=0.0
REST_GMR_0P0 [1]_  float64             Rest-frame g-r colour at redshift=0.0
EQ_ALL_0P0 [1]_    float64             e-correction at redshift=0.0
EQ_ALL_0P1 [1]_    float64             e-correction at redshift=0.1
ABSMAG_R [1]_      float64             Absolute magnitude in the r-band after k-correction
NZ                 float64  h^3 Mpc^-3 The comoving number density of the tracer at the given redshift, assuming complete sample
WEIGHT_FKP         float64             1/(1+NZ*P0), with P0 different for each tracer
================== ======== ========== =====================================================================================================================================

.. [1] Only present in BGS samples

