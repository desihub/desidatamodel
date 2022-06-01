====================
comp_tile
====================

:Summary:  completeness based on unique sets of tiles 
:Naming Convention: ``{target}_comp_tile.fits``, where ``{target}`` is
                    the target type (LRG, ELG...)
:Regex: ``[a-zA-Z]_comp_tile\.fits`` 
:File Type: FITS, 1 MB


Contents
========

====== ======= ======== =================================
Number EXTNAME Type     Contents
====== ======= ======== =================================
HDU0_          IMAGE    *PrimaryHDU with array data type*
HDU1_          BINTABLE *Completeness based on tiles*
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

*Tile completeness file*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =====================
KEY    Example Value Type Comment
====== ============= ==== =====================
NAXIS1 51            int  length of dimension 1
NAXIS2 21359         int  length of dimension 2
====== ============= ==== =====================


Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

========= ======== ===== ============
Name      Type     Units Description
========= ======== ===== ============
TILES     char[]         set of tiles
COMP_TILE float64        Completeness
========= ======== ===== ============


Notes and Examples
==================

