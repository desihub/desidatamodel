========
qso_mgii
========

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``qso_mgii-6-80605-1xsubset5.fits``, where ... *Give a human readable
    description of the filename, e.g. ``blat-{EXPID}`` where ``{EXPID}``
    is the 8-digit exposure ID.*
:Regex: ``qso_mgii-6-80605-1xsubset5.fits`` *Give a regular expression for this filename.
    For example, a six-digit number would correspond to ``[0-9]{6}``.*
:File Type: FITS, 22 KB  *This section gives the type of the file
    and its approximate size.*

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    *Brief Description*
HDU1_  MGII    BINTABLE *Brief Description*
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

*Summarize the contents of this HDU.*

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = MGII

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =======================
KEY    Example Value Type Comment
====== ============= ==== =======================
NAXIS1 83            int  width of table in bytes
NAXIS2 150           int  number of rows in table
====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ======== ===== ===================
Name            Type     Units Description
=============== ======== ===== ===================
TARGETID        int64          label for field   1
RA              float64        label for field   2
DEC             float64        label for field   3
Z_RR            float64        label for field   4
ZERR            float32        label for field   5
IS_QSO_MGII     logical        label for field   6
SV1_DESI_TARGET int64          label for field   7
SPECTYPE        char[10]       label for field   8
DELTA_CHI2      float32        label for field   9
A               float32        label for field  10
SIGMA           float32        label for field  11
B               float32        label for field  12
VAR_A           float32        label for field  13
VAR_SIGMA       float32        label for field  14
VAR_B           float32        label for field  15
=============== ======== ===== ===================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
