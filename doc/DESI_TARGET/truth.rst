===============
truth-\*.fits
===============

General Description
===================

Summary
-------

DESI Truth files contain a single binary table covering the entire footprint.  
They contain the variables that define the procedence of a target and its 
true properties. This file goes together with a mock target catalog.


Naming Convention
-----------------

TBD, let's try ``truth-{version}.fits`` where ``version`` is the code version
that wrote this, preferably a git tag of desitargets.

regex: ``truth-v?[0-9]+\.[0-9]+(\.[0-9]+|)\.fits``

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    Blank
HDU1_  TRUTH   BINTABLE Truth table
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

Empty header.

HDU1
----

TRUTH.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================================================== ==== ===================================
KEY      Example Value                                            Type Comment
======== ======================================================== ==== ===================================
EXTNAME  TRUTH                                                    str  name of this binary table extension
DEPNAM00 desitarget                                               str
DEPVER00 0.1.0                                                    str  desitarget.__version__
DEPNAM01 desitarget-git                                           str
DEPVAL01 0.1.0                                                    str  git revision
DEPNAM02 tractor-files                                            str
DEPVER02 /project/projectdirs/cosmo/data/legacysurvey/dr1/tractor str  input directory
======== ======================================================== ==== ===================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

===================== ========== ===== ===================
Name                  Type       Units Description
===================== ========== ===== ===================
TARGETID              int64            ID (unique to file and the whole survey)
BRICKNAME             char[8]          Brick name from tractor input
RA                    float64          Right ascension [degrees]
DEC                   float64          Declination [degrees]
TRUEZ                 float64          True redshift in mock catalog (without peculiar velocity)
TRUETYPE              char[10]         True object type in mock catalog
===================== ========== ===== ===================


Notes and Examples
==================

In general, the above format contains:

* Columns needed for traceability (e.g. TARGETID, BRICKNAME)
* Columns needed by fiber assignment (e.g. RA, DEC)
* Columns mimicking results from the spectroscopic pipeline (e.g. TRUEZ, TRUETYPE)

This file is created by the targets.mock submodule. 
