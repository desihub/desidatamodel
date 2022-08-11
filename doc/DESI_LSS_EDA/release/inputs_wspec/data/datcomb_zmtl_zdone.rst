=======================
datcomb_dark_zmtl_zdone
=======================

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``datcomb_dark_zmtl_zdone.fits``, where ... *Give a human readable
    description of the filename, e.g. ``blat-{EXPID}`` where ``{EXPID}``
    is the 8-digit exposure ID.*
:Regex: ``datcomb_dark_zmtl_zdone.fits`` *Give a regular expression for this filename.
    For example, a six-digit number would correspond to ``[0-9]{6}``.*
:File Type: FITS, 45 MB  *This section gives the type of the file
    and its approximate size.*

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    *Brief Description*
HDU1_          BINTABLE *Brief Description*
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

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =======================
    KEY    Example Value Type Comment
    ====== ============= ==== =======================
    NAXIS1 38            int  width of table in bytes
    NAXIS2 1252151       int  number of rows in table
    ====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

========= ======= ===== ============================================================
Name      Type    Units Description
========= ======= ===== ============================================================
TARGETID  int64         Unique DESI target ID
ZWARN_MTL int64         The ZWARN from the zmtl file (contains extra bits)
TILEID    int32         Unique DESI tile ID
Z_QN      float64       Redshift measured by QuasarNET
Z_QN_CONF float64       Redshift confidence from QuasarNET
IS_QSO_QN int16         Spectroscopic classification from QuasarNET (1 for a quasar)
========= ======= ===== ============================================================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
