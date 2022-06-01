============================
Alltiles
============================

:Summary: For targets, the list of unique TARGETIDs with number of observations
          after fiber assigment.
:Naming Convention: ``Alltiles_{program}_tilelocs.dat.fits``, 
                    where ``{program}`` is dark or bright
:Regex: ``Alltiles_[a-z]_tilelocs\.dat\.fits``
:File Type: FITS, 142 MB

Contents
========

====== ======= ======== =================================
Number EXTNAME Type     Contents
====== ======= ======== =================================
HDU0_  PRIMARY IMAGE    *PrimaryHDU with array data type*
HDU1_          BINTABLE *Table with randoms and NOBS*
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

*Table for unique TARGETIDS associated with tiles where 
it has potentially being observed after fiber assigment*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =======================
KEY    Example Value Type Comment
====== ============= ==== =======================
NAXIS1 218           int  width of table in bytes
NAXIS2 686352        int  number of rows in table
====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

========== ======== ===== =======================================
Name       Type     Units Description
========== ======== ===== =======================================
TARGETID   int64          Unique ID
NTILE      int64          Number of tiles
TILES      char[]         List of tiles observed, separated by -
TILELOCIDS char[]         TILELOC IDs, separated by -
========== ======== ===== =======================================


Notes and Examples
==================

