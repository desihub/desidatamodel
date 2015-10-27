=========
fiberflat
=========

General Description
===================

Summary
-------

Fiber flat

Naming Convention
-----------------

*TODO*

``fiberflat-b0-00000001.fits``, where ...
*Give a human readable description of the filename, e.g.
``blat-{EXPID}`` where ``{EXPID}`` is the 8-digit exposure ID.*

regex: ``fiberflat-b0-00000001.fits``
*Give a regular expression for this filename.
For example, a six-digit number would correspond to ``[0-9]{6}``.*

File Type
---------

FITS, 45 MB

Contents
========

====== ========== ===== ===================
Number EXTNAME    Type  Contents
====== ========== ===== ===================
HDU0_  FIBERFLAT  IMAGE fiberflat[nspec, nwave]
HDU1_  IVAR       IMAGE inverse variance of fiberflat
HDU2_  MASK       IMAGE bitmask of fiberflat (0=good)
HDU3_  MEANSPEC   IMAGE average spectrum[nwave]
HDU4_  WAVELENGTH IMAGE wavelength grid[nwave] in Angstroms
====== ========== ===== ===================


FITS Header Units
=================

*TODO: Describe in detail*

*These empty headers are needed to avoid sphinx build errors*

HDU0
----

*TODO*

HDU1
----

*TODO*

HDU2
----

*TODO*

HDU3
----

*TODO*

HDU4
----

*TODO*
