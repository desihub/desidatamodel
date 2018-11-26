=========
scheduler
=========

:Summary: Cached state of the next tile selector.
:Naming Convention: ``scheduler_YEAR-MM-DD.fits``, where ``YEAR-MM-DD`` is
    the date of the sunset (i.e. night) when the scheduler was run.
:Regex: ``scheduler_[0-9]{4}-[0-9]{2}-[0-9]{2}\.fits``
:File Type: FITS, 5 KB

Contents
========

====== ======= ===== ===================
Number EXTNAME Type  Contents
====== ======= ===== ===================
HDU0_          IMAGE *Brief Description*
====== ======= ===== ===================


FITS Header Units
=================

HDU0
----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =======
KEY    Example Value Type Comment
====== ============= ==== =======
NAXIS1 10            int
NIGHT  2020-03-15    str
NDONE  3             int
====== ============= ==== =======

Data: FITS image [float64, 10]


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
