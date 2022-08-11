===============================
rancomb_13bright_Alltilelocinfo
===============================

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``rancomb_13bright_Alltilelocinfo.fits``, where ... *Give a human readable
    description of the filename, e.g. ``blat-{EXPID}`` where ``{EXPID}``
    is the 8-digit exposure ID.*
:Regex: ``rancomb_13bright_Alltilelocinfo.fits`` *Give a regular expression for this filename.
    For example, a six-digit number would correspond to ``[0-9]{6}``.*
:File Type: FITS, 327 MB  *This section gives the type of the file
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

    ====== ============= ==== =====================
    KEY    Example Value Type Comment
    ====== ============= ==== =====================
    NAXIS1 66            int  length of dimension 1
    NAXIS2 5196355       int  length of dimension 2
    ====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

========== ======== ===== ========================================================================
Name       Type     Units Description
========== ======== ===== ========================================================================
TARGETID   int64          Unique DESI target ID
NTILE      int64          Number of tiles target was available on
TILES      char[11]       TILEIDs of those tile, in string form separated by &#x27;-&#x27;
TILELOCIDS char[39]       TILELOCIDs that the target was available for, separated by &#x27;-&#x27;
========== ======== ===== ========================================================================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
