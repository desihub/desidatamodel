===================
clustering
===================

:Summary: Final clustering catalog that should be used for xi statistics, including
          completeness weights and vetomasks
:Naming Convention: ``{target}_{reg}_clustering.dat.fits``, where ``{target}``
                    is the target type (LRG, ELG...), and ``{reg}`` can be S, or N 
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
RA              float64  deg   From target files (link)
DEC             float64  deg   ""
TARGETID        int64          ""
Z               float64        Redshift redrock or quasar catalog
NTILE           int64          Number of tiles target was reachable on
TILES           char[]         List of tiles target was reachable on, separated by -
COMP_TILE       float64        Completeness within the tile group given in TILES
rosette_number  float64        Rosette number
rosette_r       float64        Distance to center of rosette
FRACZ_TILELOCID float64        Of observed targets at the given TILELOCID
BITWEIGHTS      int64[2]       PIP bitwise weight from AltMTL run
PROB_OBS        float64        Probability of being observed in AltMTL runs
WEIGHT_ZFAIL    float32        Weight to correct for variations in redshift success
WEIGHT_COMP     float32        Weight to correct for assignment incompleteness
WEIGHT_SYS      float32        Weight to correct for variations in projected density due to photometry
WEIGHT          float32        Total weight for selection function variations
NZ              float64        comoving n(z) estimate assuming complete sample
WEIGHT_FKP      float64        FKP weight
=============== ======== ===== ======================================


Notes and Examples
==================

