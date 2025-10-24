================
lrg imaging mask
================

:Summary: Extra masking layer for the LRG tracers, associated with bright stars in the foreground. one row per LRG with masking information. Only present in DARK OBSCON
:Naming Convention: ``forFA{MOCKREA}_matched_input_full_lrg_imask.fits``, where  ``{MOCKREA}`` is the mock realization (25 of them).
:Regex: ``forFA[0-9]+_matched_input_full_lrg_imask\.fits``
:File Type: FITS, 262 MB

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE
HDU1_  MASK    BINTABLE Catalog of LRGs
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

Empty HDU.

HDU1
----

EXTNAME = MASK

Main Table

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =====================
    KEY    Example Value Type Comment
    ====== ============= ==== =====================
    NAXIS1 9             int  length of dimension 1
    NAXIS2 30570460      int  length of dimension 2
    DESIDR dr1           str  DESI Data Release
    ====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

======== ====== ===== =====================
Name     Type   Units Description
======== ====== ===== =====================
lrg_mask binary
TARGETID int64        Unique DESI target ID
======== ====== ===== =====================

