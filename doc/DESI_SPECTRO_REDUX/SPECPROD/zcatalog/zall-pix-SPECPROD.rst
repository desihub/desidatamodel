======================
zall-pix-SPECPROD.fits
======================

:Summary: Concatenation of all ``zpix-*.fits`` files.
:Naming Convention: ``zall-pix-{SPECPROD}.fits``, where ``{SPECPROD}`` is the
    official name of the full reduction, *e.g.* ``everest``.
:Regex: ``zall-pix-[a-z0-9_-]+\.fits``
:File Type: FITS, 2 GB

Contents
========

====== ============ ======== ===================
Number EXTNAME      Type     Contents
====== ============ ======== ===================
HDU0_               IMAGE    Empty
HDU1_  ZCATALOG     BINTABLE Redshift catalog joined with target catalog
====== ============ ======== ===================


FITS Header Units
=================

HDU0
----

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

See `HDU1 of zpix-SURVEY-PROGRAM.fits <zpix-SURVEY-PROGRAM.html#hdu1>`_.
