=========================
datcomb_obscon_zmtl_zdone
=========================

:Summary: To summarize
:Naming Convention: ``datcomb_{OBSCON}_zmtl_zdone.fits``, where {OBSCON} is dark or bright
:Regex: ``datcomb_[a,z]{4,6}_zmtl_zdone.fits`` 
:File Type: FITS, 349 MB  

Contents
========

====== ======== ======== ===================
Number EXTNAME  Type     Contents
====== ======== ======== ===================
HDU0_           IMAGE    Empty
HDU1_  LSS      BINTABLE Catalog data
====== ======== ======== ===================


FITS Header Units
=================

HDU0
----

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =======================
    KEY    Example Value Type Comment
    ====== ============= ==== =======================
    NAXIS1 38            int  width of table in bytes
    NAXIS2 9651846       int  number of rows in table
    DESIDR dr1           str
    ====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

========= ======= ===== =================================================================
Name      Type    Units Description
========= ======= ===== =================================================================
TARGETID  int64         Unique DESI target ID
ZWARN_MTL int64         The ZWARN from the zmtl file (contains extra bits)
TILEID    int32         Unique DESI tile ID
Z_QN      float64       Redshift measured by QuasarNET using line with highest confidence
Z_QN_CONF float64       Redshift confidence from QuasarNET
IS_QSO_QN int16         Spectroscopic classification from QuasarNET (1 for a quasar)
========= ======= ===== =================================================================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
