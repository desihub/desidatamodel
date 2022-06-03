==========================
tarwdup
==========================

:Summary: This file is generated with LSS scripts. It is a file with information about
          all targets after match with potential assigment in fiber assigment
:Naming Convention: ``datcomb_{program}_tarwdup_{tag}.fits``, where ``{program}`` is
                    either dark or bright and ``{tag}`` is a random string
:Regex: ``datcomb_[a-z]_tarwdup_[a-zA-Z0-9]\.fits``
:File Type: FITS, 1 GB

Contents
========

====== ======= ======== =================================
Number EXTNAME Type     Contents
====== ======= ======== =================================
HDU0_  PRIMARY IMAGE    *PrimaryHDU with array data type*
HDU1_          BINTABLE *Targets with duplicates*
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

*Merge between potential assigments from fiber assigment and input targets*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =======================
KEY    Example Value Type Comment
====== ============= ==== =======================
NAXIS1 151           int  width of table in bytes
NAXIS2 7528042       int  number of rows in table
====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

============= ======== ===== ============================
Name          Type     Units Description
============= ======== ===== ============================
RA            float64  deg   Taken from target ledger at TIMESTAMP (link)
DEC           float64  deg   ""
TARGETID      int64          ""
DESI_TARGET   int64          ""
BGS_TARGET    int64          ""
MWS_TARGET    int64          ""
SUBPRIORITY   float64        ""
PRIORITY_INIT int64          ""
TARGET_STATE  char[30]       "" 
TIMESTAMP     char[25]       ""
ZWARN_MTL     int64          ""
PRIORITY      int64          ""
FIBER         int32          Taken from POTENTIAL_ASSIGNMENTS HDU of fiberassign (link)
LOCATION      int32          ""
TILEID        int64          Tile ID in the file name of the fiberassign file
============= ======== ===== ============================


Notes and Examples
==================

