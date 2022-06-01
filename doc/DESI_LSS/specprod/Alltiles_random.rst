============================
Alltiles_random
============================

:Summary: For random associated with RANNUM given in the directory,
          the list of unique TARGETIDs with number of observations (NOBS)
          after fiber assigment.
:Naming Convention: ``rancomb_{RANNUM}{program}_Alltilelocinfo.fits``, where ``{RANNUM}``
                    is the random number and ``{program}`` is dark or bright
:Regex: ``rancomb_[0-9][a-z]_Alltilelocinfo\.fits``
:File Type: FITS, 245 MB

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

*Table for randoms with RANNUM, given by the directory with 
unique TARGETIDS (randoms) associated with tiles where it has 
potentially being observed after fiber assigment*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =======================
KEY    Example Value Type Comment
====== ============= ==== =======================
NAXIS1 60            int  width of table in bytes
NAXIS2 4283389       int  number of rows in table
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

