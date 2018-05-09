================
ZenithExtinction
================

:Summary: Atmospheric extinction data.
:Naming Convention: ``ZenithExtinction-{observatory}.fits``, where
    ``{observatory}`` is the name of the name of the observatory where
    the extinction was measured, *e.g.* 'KPNO'.
:Regex: ``ZenithExtinction-[A-Z]+\.fits``
:File Type: FITS, 1 MB

Contents
========

====== ========== ======== ======================
Number EXTNAME    Type     Contents
====== ========== ======== ======================
HDU0_  PRIMARY    IMAGE    Empty
HDU1_  EXTINCTION BINTABLE Atmospheric Extinction
====== ========== ======== ======================


FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = EXTINCTION

Atmospheric extinction in magnitudes per airmass.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ============= ==== =========================================
KEY     Example Value Type Comment
======= ============= ==== =========================================
NAXIS1  16            int  Number of bytes per row
NAXIS2  74000         int  Number of rows
EXTNAME EXTINCTION    str  KPNO extinction in magnitudes per airmass
======= ============= ==== =========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

========== ======= ===== ====================================
Name       Type    Units Description
========== ======= ===== ====================================
WAVELENGTH float64       Wavelength in Angstroms
EXTINCTION float64       Extinction in magnitudes per airmass
========== ======= ===== ====================================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
