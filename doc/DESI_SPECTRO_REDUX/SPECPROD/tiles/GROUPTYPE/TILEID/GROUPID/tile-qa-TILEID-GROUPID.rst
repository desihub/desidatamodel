===========================
tile-qa-TILEID-GROUPID.fits
===========================

:Summary: These files are mostly associated with ``cumulative`` tile coadds.
    They contain information which helps to decide during operations
    if the observation is valid or not.
:Naming Convention: ``tile-qa-TILEID-GROUPID.fits``, where
    ``TILEID`` is the tile number and
    ``GROUPID`` depends on the ``GROUPTYPE`` of the tile coadd.
:Regex: ``tile-qa-[0-9]+-(thru[0-9]{8}|[0-9]{8})\.fits``
:File Type: FITS, 627 KB

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    Keywords only
HDU1_  FIBERQA BINTABLE Per-fiber information table
HDU2_  PETALQA BINTABLE Per-petal information table
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

No data, checksum/datasum header keywords only.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    CHECKSUM D5aEE4a9D4aED4a9 str  HDU checksum updated 2021-07-16T19:03:01
    DATASUM  0                str  data unit checksum updated 2021-07-16T19:03:01
    ======== ================ ==== ==============================================

Empty HDU.

HDU1
----

EXTNAME = FIBERQA

This table contains the per-fiber information which helps to decide if the observation is valid
or not.
For each fiber, the QA information is computed from the QA information for that fiber
in all exposures used for that tile coadd reduction (see :doc:`exposure-qa-EXPID <../../../../exposures/NIGHT/EXPID/exposure-qa-EXPID>`).
That information is also used to define some column content of the PETALQA extension.


Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== =================== ===== ==============================================
    KEY      Example Value       Type  Comment
    ======== =================== ===== ==============================================
    NAXIS1   124                 int   length of dimension 1
    NAXIS2   5000                int   length of dimension 2
    TILEID   20096               int   Tile ID
    LASTNITE 20210608            int   Last night of data included in this coadd reduction
    NGOODFIB 3992                int   Number of fibers with EFFTIME_SPEC above the threshold
    NGOODPET 9                   int   Number of petals with good fibers (only used for plotting routines)
    EFFTIME  214.8598327636719   float [s] Median of EFFTIME_SPEC of fibers that are good in all exposures
    VALID    T                   bool  A tile is valid if EFFTIME > MINTFRAC*GOALTIME AND NGOODFIB > threshold
    RMSDIST  0.01416921149939299 float [mm] RMS distance of good fibers
    TILERA   229.546             float [deg] Tile Right Ascension
    TILEDEC  -0.056              float [deg] Tile Declination
    GOALTIME 180.0               float [s] Aimed EFFTIME_SPEC
    GOALTYPE BRIGHT              str   Sky conditions used for some noise estimation
    FAPRGRM  bright              str   Program to which this tile belongs
    SURVEY   main                str   Survey of origin of the targets
    EBVFAC   1.12631027332157    float 10.0 ** (2.165 * median(EBV) / 2.5))
    MINTFRAC 0.85                float Fraction of GOALTIME to be reached by EFFTIME_SPEC to consider the tile has completed
    CHECKSUM 73CQ71BN71BN71BN    str   HDU checksum updated 2021-07-16T19:03:01
    DATASUM  105714500           str   data unit checksum updated 2021-07-16T19:03:01
    ======== =================== ===== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

============= ======= ===== ===========
Name          Type    Units Description
============= ======= ===== ===========
TARGETID      int64         Unique target ID
PETAL_LOC     int16         Petal location [0-9]
DEVICE_LOC    int32         Device location on focal plane [0-523]
LOCATION      int64         Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBER         int32         Fiber ID on the CCDs [0-4999]
TARGET_RA     float64 deg   Target Right Ascension
TARGET_DEC    float64 deg   Target Declination
MEAN_FIBER_X  float32 mm    Mean (over exposures) fiber CS5 X location on focal plane
MEAN_FIBER_Y  float32 mm    Mean (over exposures) fiber CS5 Y location on focal plane
MEAN_DELTA_X  float32 mm    Mean (over exposures) fiber difference between measured and requested CS5 X location on focal plane
MEAN_DELTA_Y  float32 mm    Mean (over exposures) fiber difference between measured and requested CS5 Y location on focal plane
RMS_DELTA_X   float32 mm    RMS (over exposures) of the fiber difference between measured and requested CS5 X location on focal plane
RMS_DELTA_Y   float32 mm    RMS (over exposures) of the fiber difference between measured and requested CS5 Y location on focal plane
DESI_TARGET   int64         Dark survey + calibration bitmask
BGS_TARGET    int64         Bright Galaxy Survey bitmask
EBV           float32 mag   Galactic extinction E(B-V) reddening
TSNR2_LRG     float64       LRG Template-based squared signal-to-noise ratio
Z             float64       Spectroscopic redshift (from the redrock file)
SPECTYPE      char[6]       Spectroscopic type (from the redrock file)
DELTACHI2     float64       Chi2 difference between the first- and second best redshifts (from the redrock file)
QAFIBERSTATUS int32         Fiber status bitmask, inflated with further QA diagnoses
EFFTIME_SPEC  float32 s     Spectroscopic effective time, based on template-based squared signal-to-noise ratio
============= ======= ===== ===========

HDU2
----

EXTNAME = PETALQA

This table contains the per-petal information which helps to decide if the observation is valid
or not, and if a petal should be considered as "bad" (i.e. as if it would not have been observed),
because of a too-low quality.
It is the mean (over exposures) of the PETALQA extension of the :doc:`exposure-qa-EXPID <../../../../exposures/NIGHT/EXPID/exposure-qa-EXPID>`
values, to which we refer for the column definition.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   66               int  length of dimension 1
    NAXIS2   10               int  length of dimension 2
    CHECKSUM 5m3P8l1M5l1M5l1M str  HDU checksum updated 2021-07-16T19:03:01
    DATASUM  807618843        str  data unit checksum updated 2021-07-16T19:03:01
    ======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

============== ======= ===== ===========
Name           Type    Units Description
============== ======= ===== ===========
PETAL_LOC      int16         Petal location [0-9]
WORSTREADNOISE float32       Mean of the per-exposure WORSREADNOISE
NGOODPOS       float32       Mean of the per-exposure NGOODPOS
NSTDSTAR       float32       Mean of the per-exposure NSTDSTAR
STARRMS        float32       Mean of the per-exposure STARRMS
TSNR2FRA [1]_  float32       Deprecated column
NCFRAME        float32       Mean of the per-exposure NCFRAME
BSKYTHRURMS    float32       Mean of the per-exposure BSKYTHRURMS
BSKYCHI2PDF    float32       Mean of the per-exposure BSKYCHI2PDF
RSKYTHRURMS    float32       Mean of the per-exposure RSKYTHRURMS
RSKYCHI2PDF    float32       Mean of the per-exposure RSKYCHI2PDF
ZSKYTHRURMS    float32       Mean of the per-exposure ZSKYTHRURMS
ZSKYCHI2PDF    float32       Mean of the per-exposure ZSKYCHI2PDF
BTHRUFRAC      float32       Mean of the per-exposure BTHRUFRAC
RTHRUFRAC      float32       Mean of the per-exposure RTHRUFRAC
ZTHRUFRAC      float32       Mean of the per-exposure ZTHRUFRAC
EFFTIME_SPEC   float32 s     Median of the EFFTIME_SPEC values for all good fibers (for all exposures) from that petal
============== ======= ===== ===========

.. [1] Optional

Notes and Examples
==================

* For some data releases, this ``tile-qa-TILEID-GROUPID.fits`` also exists for the tile per-night coadd reductions.
* The QAFIBERSTATUS bitmasks are defined here :doc:`bitmasks <../../../../../../bitmasks>`.
* Some FIBERQA extension header keywords are originally coming from the :doc:`fiberassign-TILEID <../../../../../../DESI_TARGET/fiberassign/fiberassign-TILEID>` file (TILEID, TILERA, TILEDEC, GOALTIME, GOALTYPE, FAPRGRM, SURVEY, EBVFAC, MINTFRAC).
* The FIBERQA EFFTIME_SPEC is proportional to the TSNR2 values in the TSNR2 extension of the :doc:`redrock-SPECTROGRAPH-TILEID-GROUPID <redrock-SPECTROGRAPH-TILEID-GROUPID>` file; for the BACKUP and BRIGHT programs, the TSNR2_BGS is used; for the DARK program, the TSNR2_ELG or TSNR2_LRG is used.
