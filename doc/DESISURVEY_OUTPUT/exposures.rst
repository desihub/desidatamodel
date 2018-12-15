===================
exposures_surveysim
===================

:Summary: Record of simulated exposures.
:Naming Convention: ``exposures.fits``
:Regex: ``exposures\.fits``
:File Type: FITS, 2 MB  (scales with the number of exposures)

*Note*: currently this is only an output from surveysim, but it may become an
output of survey operations, caching in a file the information that is also
contained in the operations database.

Contents
========

====== ========= ======== ===================
Number EXTNAME   Type     Contents
====== ========= ======== ===================
HDU0_  META      IMAGE    Blank
HDU1_  EXPOSURES BINTABLE Per-exposure metadata
HDU2_  TILEDATA  BINTABLE Per-tile metadata
====== ========= ======== ===================

FITS Header Units
=================

HDU0
----

EXTNAME = META

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ================= ==== =======
KEY     Example Value     Type Comment
======= ================= ==== =======
TILES   desi--tiles.fits  str  Name of the tiles file specified in desisurvey config.
NEXP    41875             int  Number of exposures recorded so far.
COMMENT Baseline (seed=1) str  Comment describing this simulation.
INITIAL 2019-12-01        str  YEAR-MM-DD of initial night used for integer offsets (or blank before any observing).
EXTNAME META              str  Extension name.
======= ================= ==== =======

Empty HDU.

HDU1
----

EXTNAME = EXPOSURES

Per-exposure metadata.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ============= ==== =====================
KEY     Example Value Type Comment
======= ============= ==== =====================
NAXIS1  41875         int  length of dimension 1
NAXIS2  8             int  length of dimension 2
EXTNAME EXPOSURES     str  extension name
======= ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

======== ======= ====== ===========
Name     Type    Units  Description
======== ======= ====== ===========
MJD      float64        MJD when shutter was opened for this exposure.
EXPTIME  float32 s      Length of time shutter was open.
TILEID   int32          ID of the observed tile.
SNR2FRAC float32        Fractional SNR2 accumulated on this tile during this exposure.
AIRMASS  float32        Average airmass during this exposure.
SEEING   float32 arcsec Average FWHM atmospheric seeing during this exposure. 
TRANSP   float32        Average atmospheric transparency during this exposure.
SKY      float32        Average sky background level during this exposure.
======== ======= ====== ===========

HDU2
----

EXTNAME = TILEDATA

Per-tile metadata.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ============= ==== =====================
KEY     Example Value Type Comment
======= ============= ==== =====================
NAXIS1  20            int  length of dimension 1
NAXIS2  10            int  length of dimension 2
EXTNAME TILEDATA      str  extension name
======= ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

======== ======= ===== ===========
Name     Type    Units Description
======== ======= ===== ===========
AVAIL    int32         Night when this tile was first available (or -1 if not yet available).
PLANNED  int32         Night when this tile was first planned (or -1 if not yet planned).
EXPTIME  float32 s     Total exposure time of this tile.
SNR2FRAC float32       Total fractional SNR2 accumulated on this tile.
NEXP     int32         Total number of exposures of this tile.
======== ======= ===== ===========

There is one table row per tile, indexed to match `desisurvey.tiles.Tiles 
<https://desisurvey.readthedocs.io/en/latest/api.html#desisurvey.tiles.Tiles>`__.

The integer ``AVAIL`` and ``PLANNED`` values are nights since the date specified
by the ``NIGHT`` keyword in HDU0.

A tile is considered "available" once it has fibers assigned. A tile is considered
"planned" once its priority has been set non-zero. In general, these changes of
state occur independently: availability is determined by the fiber assignment
policy and when covering tiles have been completed, while the priorities are
set by `survey strategy rules
<https://desisurvey.readthedocs.io/en/latest/api.html#module-desisurvey.rules>`__.
**A tile will not be scheduled until it is both available and planned.**

Notes and Examples
==================

An `ExposuresList
<https://surveysim.readthedocs.io/en/latest/api.html?highlight=ExposureList#surveysim.exposures.ExposureList>`__
object records exposures during simulation::

    import surveysim.exposures
    explist = surveysim.exposures.ExposureList()
    
Its internal state after a simulation (or each night) can be saved using, for example::

    explist.save('exposures.fits', comment='Baseline (seed=1)')
    
This state can then later be restored using::

    explist = surveysim.exposures.ExposureList(restore='exposures.fits')
