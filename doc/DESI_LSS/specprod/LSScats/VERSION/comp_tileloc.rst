=======================
comp_tileloc
=======================

:Summary: Fraction of good tilelocids 
:Naming Convention: ``{target}_comp_tileloc.fits``, where ``{target}`` is
                    the target type (LRG, ELG...)
:Regex: ``[a-zA-Z]_comp_tileloc\.fits``
:File Type: FITS, 2 MB  

Contents
========

====== ======= ======== =================================
Number EXTNAME Type     Contents
====== ======= ======== =================================
HDU0_          IMAGE    *PrimaryHDU with array data type*
HDU1_          BINTABLE *Brief Description*
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

*Fraction of good tilelocid's*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =====================
KEY    Example Value Type Comment
====== ============= ==== =====================
NAXIS1 16            int  length of dimension 1
NAXIS2 155284        int  length of dimension 2
====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ======= ===== ===============================
Name            Type    Units Description
=============== ======= ===== ===============================
TILELOCID       int64         Unique tileloc id
FRACZ_TILELOCID float64       Fraction of observed tilelocids
=============== ======= ===== ===============================


Notes and Examples
==================

