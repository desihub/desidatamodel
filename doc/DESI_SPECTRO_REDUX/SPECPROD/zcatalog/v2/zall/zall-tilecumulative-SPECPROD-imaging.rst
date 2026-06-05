=========================================
zall-tilecumulative-SPECPROD-imaging.fits
=========================================

:Summary: Concatenation of all ``ztile-*-cumulative-imaging.fits`` files,
          combining Legacy Survey imaging photometry columns across all TILEs,
          SURVEYs, and PROGRAMs.
:Naming Convention: ``zcatalog/v2/zall/zall-tilecumulative-{SPECPROD}-imaging.fits``, where
    ``{SPECPROD}`` is the official name of the full reduction, *e.g.* ``iron``.
:Regex: ``zall-tilecumulative-[a-z0-9_-]+-imaging\.fits``
:File Type: FITS, ~50 GB

This file is row-matched to
:doc:`zall-tilecumulative-SPECPROD.fits <./zall-tilecumulative-SPECPROD>` and
contains the imaging photometry columns stacked from all
:doc:`ztile-*-cumulative-imaging.fits <../SURVEY/ztile-SURVEY-PROGRAM-GROUPTYPE-imaging>`
files.

Contents
========

====== ================ ======== ============================================================
Number EXTNAME          Type     Contents
====== ================ ======== ============================================================
HDU0_  PRIMARY          IMAGE    Empty
HDU1_  ZCATALOG_IMAGING BINTABLE Legacy Survey imaging photometry columns
====== ================ ======== ============================================================


FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ============ ================ ==== =======================
    KEY          Example Value    Type Comment
    ============ ================ ==== =======================
    CHECKSUM     9aaGCVYE9aaECUYE str  HDU checksum
    DATASUM      0                str  data unit checksum
    ZCATVER      v2               str  Version of zcatalog files
    ============ ================ ==== =======================

Empty HDU.

HDU1
----

EXTNAME = ZCATALOG_IMAGING

Legacy Survey (`LS`_) imaging photometry columns stacked from all
:doc:`ztile-SURVEY-PROGRAM-GROUPTYPE-imaging.fits <../SURVEY/ztile-SURVEY-PROGRAM-GROUPTYPE-imaging>`
cumulative files. Column definitions are identical to that file; see it for
descriptions.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ============ ================ ==== =======================
    KEY          Example Value    Type Comment
    ============ ================ ==== =======================
    NAXIS1       228              int  width of table in bytes
    NAXIS2       10000000         int  number of rows in table
    CHECKSUM     QA6lQ26iQ96iQ96i str  HDU checksum
    DATASUM      4284326946       str  data unit checksum
    ZCATVER      v2               str  Version of zcatalog files
    ============ ================ ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

See
:doc:`ztile-SURVEY-PROGRAM-GROUPTYPE-imaging.fits <../SURVEY/ztile-SURVEY-PROGRAM-GROUPTYPE-imaging>`
for the full column list. The key columns are TARGETID and TILEID;
all other columns are the imaging photometry columns from the Legacy Survey.

.. _`LS`: https://www.legacysurvey.org/
