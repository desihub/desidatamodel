===
sdR
===

:Summary: Raw data.
:Naming Convention: ``sdR-{EXPID}.fits``, where ``EXPID`` is an 8-digit number.
:Regex: ``sdR-[0-9]{8}\.fits``

Contents
========

====== ======== =========================== ===========
Number EXTNAME  Type                        Contents
====== ======== =========================== ===========
HDU0_  FLUX     IMAGE                       Flux in ADU
====== ======== =========================== ===========

HDU0
====

EXTNAME = FLUX

Data: FITS image [float64]
