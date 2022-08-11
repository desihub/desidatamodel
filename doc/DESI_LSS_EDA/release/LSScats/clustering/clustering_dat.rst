==========
BGS_BRIGHT
==========

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``BGS_BRIGHT-21.5_S_clustering.dat.fits``, where ... *Give a human readable
    description of the filename, e.g. ``blat-{EXPID}`` where ``{EXPID}``
    is the 8-digit exposure ID.*
:Regex: ``BGS_BRIGHT-21.5_S_clustering.dat.fits`` *Give a regular expression for this filename.
    For example, a six-digit number would correspond to ``[0-9]{6}``.*
:File Type: FITS, 8 MB  *This section gives the type of the file
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
    NAXIS1 123           int  width of table in bytes
    NAXIS2 71051         int  number of rows in table
    ====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

============= ======== ===== ================================================================================================================================================================
Name          Type     Units Description
============= ======== ===== ================================================================================================================================================================
TARGETID      int64          Unique DESI target ID
Z             float64        Redshift measured by Redrock
NTILE         int64          Number of tiles target was available on
TILES         char[11]       TILEIDs of those tile, in string form separated by -
RA            float64        Right Ascension
DEC           float64        Declination
WEIGHT        float64        The combination of all weights to use
WEIGHT_ZFAIL  float32        Should be all 1 at this point for main survey
WEIGHT_COMP   float64        1/FRACZ_TILELOCID
WEIGHT_SYS    float64        A weight correcting for fluctuations in projected density with imaging conditions, using the random forest method of regressis by Edmond Chaussidon
flux_g_dered  float32        Flux in the g-band after correcting for Galactic extinction (AB system) Only BGS
flux_r_dered  float32        Flux in the r-band after correcting for Galactic extinction (AB system) Only BGS
flux_z_dered  float32        Flux in the z-band after correcting for Galactic extinction (AB system) Only BGS
flux_w1_dered float32        Flux in the WISE W1-band after correcting for Galactic extinction (AB system) Only BGS
flux_w2_dered float32        Flux in the WISE W2-band after correcting for Galactic extinction (AB system) Only BGS
WEIGHT_SYSEB  float64        A weight correcting for fluctuations in projected density with imaging conditions, using the linear regression method applied to eBOSS (might not exist for all)
NZ            float64        The comoving number density of the tracer at the given redshift, in units (h/Mpc)^3, assuming complete sample
WEIGHT_FKP    float64        1/(1+NZ*P0), with P0 different for each tracer
============= ======== ===== ================================================================================================================================================================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
