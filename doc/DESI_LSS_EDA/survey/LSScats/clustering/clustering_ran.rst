==================================================
Clustering LSS catalogs for randoms
==================================================

:Summary: For each target type, LSS catalogs for the randoms, ready to be used for clustering measurements, are provided.
:Naming Convention: ``{TARGET}_{PHOTSYS}_{RANN}_clustering.ran.fits``, where ``{TARGET}`` is the target type, ``{PHOTSYS}`` is the photometric region, and {RANN} is the number for the random file (18 total, numbered 0 through 17). Each are random with respect to eachother.
:Regex: For example, ``BGS_BRIGHT_N_0_clustering.ran.fits`` is the randoms for BGS_BRIGHT in the Northern portion of the imaging (BASS/MzLS) for random file 0.
:File Type: FITS, 193 MB  *This section gives the type of the file
    and its approximate size.*

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    *Brief Description*
HDU1_  LSS     BINTABLE *Brief Description*
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

*Summarize the contents of this HDU.*

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = LSS

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =======================
    KEY    Example Value Type Comment
    ====== ============= ==== =======================
    NAXIS1 115           int  width of table in bytes
    NAXIS2 1763774       int  number of rows in table
    ====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

============= ======== ===== ===================================================================================================================================================
Name          Type     Units Description
============= ======== ===== ===================================================================================================================================================
TARGETID      int64          Unique DESI target ID
RA            float64        Right Ascension
DEC           float64        Declination
NTILE         int64          Number of tiles target was available on
TILES         char[11]       TILEIDs of those tile, in string form separated by -
Z             float64        Redshift measured by Redrock
WEIGHT        float64        The combination of all weights to use
WEIGHT_SYS    float64        A weight correcting for fluctuations in projected density with imaging conditions, using the random forest method of regressis by Edmond Chaussidon
WEIGHT_COMP   float64        1/FRACZ_TILELOCID
WEIGHT_ZFAIL  float32        Should be all 1 at this point for main survey
flux_g_dered  float32        Flux in the g-band after correcting for Galactic extinction (AB system) Only BGS
flux_r_dered  float32        Flux in the r-band after correcting for Galactic extinction (AB system) Only BGS
flux_z_dered  float32        Flux in the z-band after correcting for Galactic extinction (AB system) Only BGS
flux_w1_dered float32        Flux in the WISE W1-band after correcting for Galactic extinction (AB system) Only BGS
flux_w2_dered float32        Flux in the WISE W2-band after correcting for Galactic extinction (AB system) Only BGS
NZ            float64        The comoving number density of the tracer at the given redshift, in units (h/Mpc)^3, assuming complete sample
WEIGHT_FKP    float64        1/(1+NZ*P0), with P0 different for each tracer
============= ======== ===== ===================================================================================================================================================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
