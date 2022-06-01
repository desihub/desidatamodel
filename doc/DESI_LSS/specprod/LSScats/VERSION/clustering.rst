===================
clustering
===================

:Summary: Final clustering catalog that should be used for xi statistics, including
          completeness weights and vetomasks
:Naming Convention: ``{target}_{reg}_clustering.dat.fits``, where ``{target}``
                    is the target type (LRG, ELG...), and ``{reg}`` can be S,N or non-exist
:Regex: ``[a-zA-Z]_[A-Z]_clustering\.dat\.fits``
:File Type: FITS, 20 MB  

Contents
========

====== ======= ======== =================================
Number EXTNAME Type     Contents
====== ======= ======== =================================
HDU0_  PRIMARY IMAGE    *PrimaryHDU with array data type*
HDU1_  LSS     BINTABLE *Clustering catalog*
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

*Target clustering catalog with weights and vetoed*


Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =======================
KEY    Example Value Type Comment
====== ============= ==== =======================
NAXIS1 171           int  width of table in bytes
NAXIS2 125817        int  number of rows in table
====== ============= ==== =======================


Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ======== ===== ======================================
Name            Type     Units Description
=============== ======== ===== ======================================
RA              float64  deg   Right Ascension
DEC             float64  deg   Declination
TARGETID        int64          Unique Target ID
Z               float64        Redshift
NTILE           int64          Number of tiles
TILES           char[]         List of tiles observed, separated by -
COMP_TILE       float64        Tile completeness
rosette_number  float64        Rosette number
rosette_r       float64        Distance to center of rosette
FRACZ_TILELOCID float64        Fraction of good locations
BITWEIGHTS      int64[2]       PIP bitwise weight
PROB_OBS        float64        Probability of being observed AltMTL
WEIGHT_ZFAIL    float32        Redshift failure weight
WEIGHT          float32        Total weight
NZ              float64        N(z) contribution of source
WEIGHT_FKP      float64        FKP weight
=============== ======== ===== ======================================


Notes and Examples
==================

