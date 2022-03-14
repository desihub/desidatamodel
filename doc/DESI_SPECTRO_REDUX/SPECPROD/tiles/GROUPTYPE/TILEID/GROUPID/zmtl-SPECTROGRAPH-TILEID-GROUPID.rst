====
zmtl
====

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``zmtl-3-388-thru20210417.fits``, where ... *Give a human readable
    description of the filename, e.g. ``blat-{EXPID}`` where ``{EXPID}``
    is the 8-digit exposure ID.*
:Regex: ``zmtl-3-388-thru20210417.fits`` *Give a regular expression for this filename.
    For example, a six-digit number would correspond to ``[0-9]{6}``.*
:File Type: FITS, 67 KB  *This section gives the type of the file
    and its approximate size.*

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    *Brief Description*
HDU1_  ZMTL    BINTABLE *Brief Description*
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

EXTNAME = ZMTL

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================================================================================== ==== =======================
KEY      Example Value                                                                              Type Comment
======== ========================================================================================== ==== =======================
NAXIS1   112                                                                                        int  width of table in bytes
NAXIS2   500                                                                                        int  number of rows in table
QN_ADDED T                                                                                          bool
SQ_ADDED F                                                                                          bool
AB_ADDED F                                                                                          bool
ZC_ADDED F                                                                                          bool
QNMODFIL /global/cfs/cdirs/desi/target/catalogs/lya/qn_models/qn_train_coadd_indtrain_0_0_boss10.h5 str
BADPTLQA F                                                                                          bool
======== ========================================================================================== ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ======= ===== ===================
Name            Type    Units Description
=============== ======= ===== ===================
RA              float64 deg   label for field   1
DEC             float64 deg   label for field   2
TARGETID        int64         label for field   3
SV3_DESI_TARGET int64         label for field   4
SV3_BGS_TARGET  int64         label for field   5
SV3_MWS_TARGET  int64         label for field   6
SV3_SCND_TARGET int64         label for field   7
Z               float64       label for field   8
ZWARN           int64         label for field   9
SPECTYPE        char[6]       label for field  10
DELTACHI2       float64       label for field  11
NUMOBS          int32         label for field  12
ZTILEID         int32         label for field  13
Z_QN            float64       label for field  14
Z_QN_CONF       float64       label for field  15
IS_QSO_QN       int16         label for field  16
=============== ======= ===== ===================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
