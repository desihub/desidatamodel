======
qso_qn
======

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``qso_qn-main-dark-9377.fits``, where ... *Give a human readable
    description of the filename, e.g. ``blat-{EXPID}`` where ``{EXPID}``
    is the 8-digit exposure ID.*
:Regex: ``qso_qn-main-dark-9377.fits`` *Give a regular expression for this filename.
    For example, a six-digit number would correspond to ``[0-9]{6}``.*
:File Type: FITS, 19 KB  *This section gives the type of the file
    and its approximate size.*

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    *Brief Description*
HDU1_  QN+RR   BINTABLE *Brief Description*
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

EXTNAME = QN+RR

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =======================
KEY    Example Value Type Comment
====== ============= ==== =======================
NAXIS1 151           int  width of table in bytes
NAXIS2 75            int  number of rows in table
====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

================ =========== ===== ===================
Name             Type        Units Description
================ =========== ===== ===================
TARGETID         int64             label for field   1
RA               float64           label for field   2
DEC              float64           label for field   3
Z_NEW            float64           label for field   4
ZERR_NEW         float32           label for field   5
DESI_TARGET      int64             label for field   6
COEFFS           float32[10]       label for field   7
SPECTYPE         char[10]          label for field   8
Z_RR             float32           label for field   9
Z_QN             float32           label for field  10
IS_QSO_QN_NEW_RR logical           label for field  11
C_LYA            float32           label for field  12
C_CIV            float32           label for field  13
C_CIII           float32           label for field  14
C_MgII           float32           label for field  15
C_Hbeta          float32           label for field  16
C_Halpha         float32           label for field  17
Z_LYA            float32           label for field  18
Z_CIV            float32           label for field  19
Z_CIII           float32           label for field  20
Z_MgII           float32           label for field  21
Z_Hbeta          float32           label for field  22
Z_Halpha         float32           label for field  23
================ =========== ===== ===================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
