=====================
clustering_random
=====================

:Summary: Final random clustering catalog for RANNUM
:Naming Convention: ``{target}_{reg}_{RANNUM}_clustering.ran.fits``, where ``{target}``
                    is the target type (LRG, ELG...), ``{reg}`` can be S,N or non-exist 
                    and ``{RANNUM}`` is the random number
:Regex: ``[a-zA-Z]_[A-Z]_[0-9]_clustering\.ran\.fits``
:File Type: FITS, 62 MB  


Contents
========

====== ======= ======== =================================
Number EXTNAME Type     Contents
====== ======= ======== =================================
HDU0_  PRIMARY IMAGE    *PrimaryHDU with array data type*
HDU1_  LSS     BINTABLE *Random clustering catalog*
====== ======= ======== =================================


FITS Header Units
=================

HDU0
----

*Primary HDU conforms to FITS standard*

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = LSS

*Random clustering catalog with weights and vetoed*


Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =======================
KEY    Example Value Type Comment
====== ============= ==== =======================
NAXIS1 151           int  width of table in bytes
NAXIS2 434685        int  number of rows in table
====== ============= ==== =======================


Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

============== ======== ===== ======================================
Name           Type     Units Description
============== ======== ===== ======================================
TARGETID       int64          Unique Target ID
RA             float64  deg   Right Ascension
DEC            float64  deg   Declination
NTILE          int64          Number of tiles
TILES          char[]         List of tiles observed, separated by -
rosette_number int64          Rosette number
rosette_r      float64        Distance to center of rosette
COMP_TILE      float64        Tile completeness
Z              float64        Redshift
WEIGHT         float64        Total weight
flux_g_dered   float32        Flux in band g, deredened
flux_r_dered   float32        Flux in band r, deredened
flux_z_dered   float32        Flux in band z, deredened
flux_w1_dered  float32        Flux in band W1, deredened
flux_w2_dered  float32        Flux in band W2, deredened
NZ             float64        N(z) contribution of source
WEIGHT_FKP     float64        FKP weight
============== ======== ===== ======================================


Notes and Examples
==================

