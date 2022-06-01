=========
fits_file
=========

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``fits_file.fits``, where ... *Give a human readable
    description of the filename, e.g. ``blat-{EXPID}`` where ``{EXPID}``
    is the 8-digit exposure ID.*
:Regex: ``fits_file.fits`` *Give a regular expression for this filename.
    For example, a six-digit number would correspond to ``[0-9]{6}``.*
:File Type: FITS, 28 KB  *This section gives the type of the file
    and its approximate size.*

Contents
========

====== ======== ======== ===================
Number EXTNAME  Type     Contents
====== ======== ======== ===================
HDU0_  PRIMARY  IMAGE    *Brief Description*
HDU1_  Galaxies BINTABLE *Brief Description*
====== ======== ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== ====================================
    KEY    Example Value Type Comment
    ====== ============= ==== ====================================
    NAXIS1 100           int
    NAXIS2 100           int
    BSCALE 1             int
    BZERO  32768         int  Data are really unsigned 16-bit int.
    ====== ============= ==== ====================================

Data: FITS image [int16, 100x100]

HDU1
----

EXTNAME = Galaxies

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =====================
    KEY    Example Value Type Comment
    ====== ============= ==== =====================
    NAXIS1 32            int  length of dimension 1
    NAXIS2 3             int  length of dimension 2
    ====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

====== ======== ===== ===========
Name   Type     Units Description
====== ======== ===== ===========
target char[20]
V_mag  float32  mag
vdisp  float64  km/s
====== ======== ===== ===========


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
