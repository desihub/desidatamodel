==============
psfboot-CAMERA
==============

:Summary: psfboot file.
:Naming Convention: ``psfboot-CAMERA.fits``, where ``CAMERA`` is *e.g.*,
    "b0", "r1", "z2".
:Regex: ``psfboot-[brz][0-9]\.fits``
:File Type: FITS, 64 KB

Contents
========

====== ======= ===== ===================
Number EXTNAME Type  Contents
====== ======= ===== ===================
HDU0_          IMAGE *Brief Description*
HDU1_          IMAGE *Brief Description*
HDU2_          IMAGE *Brief Description*
====== ======= ===== ===================


FITS Header Units
=================

HDU0
----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ============= ===== =======
KEY     Example Value Type  Comment
======= ============= ===== =======
NAXIS1  6             int
NAXIS2  500           int
WAVEMIN 5563.41034186 float
WAVEMAX 7807.04444877 float
======= ============= ===== =======

Data: FITS image [float64, 6x500]

HDU1
----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ============= ===== =======
KEY     Example Value Type  Comment
======= ============= ===== =======
NAXIS1  6             int
NAXIS2  500           int
WAVEMIN 5563.41034186 float
WAVEMAX 7807.04444877 float
======= ============= ===== =======

Data: FITS image [float64, 6x500]

HDU2
----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =======
KEY    Example Value Type Comment
====== ============= ==== =======
NAXIS1 500           int
====== ============= ==== =======

Data: FITS image [float64, 500]


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
