==========
frac_tlobs
==========

:Summary: For a given target type, the fraction of targets with the same TILES value that contribute to FRACZ_TILELOCID, as a function of TILES
:Naming Convention: ``{TARGET}_frac_tlobs.fits``, where ``{TARGET}`` is the target type, QSO, ELG, LRG for dark and BGS for bright
:Regex: ``[a-z]_frac_tlobs.fits`` 
:File Type: FITS, 3 MB  

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    Empty
HDU1_  LSS     BINTABLE TILES List
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

FRAC_TLOBS_TILES for TILEIDs

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =======================
    KEY    Example Value Type Comment
    ====== ============= ==== =======================
    NAXIS1 44            int  width of table in bytes
    NAXIS2 78492         int  number of rows in table
    DESIDR dr1           str
    ====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

================ ======== ===== ================================================================================
Name             Type     Units Description
================ ======== ===== ================================================================================
TILES            char[36]       TILEIDs of those tile, in string form separated by &#x27;-&#x27;
FRAC_TLOBS_TILES float64        Fraction of targets with the same TILES value that contribute to FRACZ_TILELOCID
================ ======== ===== ================================================================================


Notes and Examples
==================

