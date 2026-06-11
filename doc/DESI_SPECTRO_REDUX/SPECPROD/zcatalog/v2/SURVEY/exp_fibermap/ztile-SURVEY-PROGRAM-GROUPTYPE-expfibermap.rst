===============================================
ztile-SURVEY-PROGRAM-GROUPTYPE-expfibermap.fits
===============================================

:Summary: Per-exposure fibermap entries for the tile-based redshift catalogs,
          one file per SURVEY, PROGRAM, and spectral GROUPTYPE.
:Naming Convention: ``zcatalog/v2/SURVEY/exp_fibermap/ztile-SURVEY-PROGRAM-GROUPTYPE-expfibermap.fits``, where
    ``SURVEY`` is *e.g.* ``main`` or ``sv1``, ``PROGRAM`` is *e.g.* ``bright``
    or ``dark``, and ``GROUPTYPE`` is ``cumulative`` or ``pernight``.
:Regex: ``ztile-(cmx|main|sv1|sv2|sv3|special)-(backup|bright|dark|other)-(cumulative|perexp|pernight|1x_depth|4x_depth|lowspeed)-expfibermap\.fits``
:File Type: FITS, ~50 MB

Contents
========

====== ============ ======== ============================================================
Number EXTNAME      Type     Contents
====== ============ ======== ============================================================
HDU0_  PRIMARY      IMAGE    Empty
HDU1_  EXP_FIBERMAP BINTABLE Per-exposure entries from input fibermaps
====== ============ ======== ============================================================


FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ============ ================ ==== =======================
    KEY          Example Value    Type Comment
    ============ ================ ==== =======================
    CHECKSUM     9aaGCVYE9aaECUYE str  HDU checksum
    DATASUM      0                str  data unit checksum
    ZCATVER      v2               str  Version of zcatalog files
    ============ ================ ==== =======================

Empty HDU.

HDU1
----

EXTNAME = EXP_FIBERMAP

Input fibermap entries for columns that apply per-exposure and cannot be
coadded, *e.g.* the individual nights and exposures on which each target was
observed. Each row corresponds to one exposure of one target.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== =======================
    KEY      Example Value    Type Comment
    ======== ================ ==== =======================
    NAXIS1   162              int  width of table in bytes
    NAXIS2   5000             int  number of rows in table
    CHECKSUM diandZUmdfamdZUm str  HDU checksum
    DATASUM  2531100066       str  data unit checksum
    ======== ================ ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

===================== ======= ======== =======================================================================================================
Name                  Type    Units    Description
===================== ======= ======== =======================================================================================================
TARGETID              int64            Unique DESI target ID
PRIORITY              int32            Target current priority
SUBPRIORITY           float64          Random subpriority [0-1) to break assignment ties
NIGHT                 int32            Night of observation (YYYYMMDD) starting at local noon before observations start
EXPID                 int32            DESI Exposure ID number
MJD                   float64          Modified Julian Date when shutter was opened for this exposure
TILEID                int32            Unique DESI tile ID
EXPTIME               float64 s        Length of time shutter was open
PETAL_LOC             int16            Petal location [0-9]
DEVICE_LOC            int32            Device location on focal plane [0-523]
LOCATION              int64            Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBER                 int32            Fiber ID on the CCDs [0-4999]
FIBERSTATUS           int32            Fiber status mask. 0=good
FIBERASSIGN_X         float32 mm       Fiberassign expected CS5 X location on focal plane
FIBERASSIGN_Y         float32 mm       Fiberassign expected CS5 Y location on focal plane
LAMBDA_REF            float32 Angstrom Requested wavelength at which targets should be centered on fibers
PLATE_RA              float64 deg      Barycentric Right Ascension in ICRS to be used by PlateMaker
PLATE_DEC             float64 deg      Barycentric Declination in ICRS to be used by PlateMaker
NUM_ITER              int64            Number of positioner iterations
FIBER_X               float64 mm       CS5 X location requested by PlateMaker
FIBER_Y               float64 mm       CS5 Y location requested by PlateMaker
DELTA_X               float64 mm       CS5 X requested minus actual position
DELTA_Y               float64 mm       CS5 Y requested minus actual position
FIBER_RA              float64 deg      RA of actual fiber position
FIBER_DEC             float64 deg      DEC of actual fiber position
PSF_TO_FIBER_SPECFLUX float64          fraction of light from point-like source captured by 1.5 arcsec diameter fiber given atmospheric seeing
IN_COADD_B            logical          If True this fiber in this exposure was used in the coadd of camera B
IN_COADD_R            logical          If True this fiber in this exposure was used in the coadd of camera R
IN_COADD_Z            logical          If True this fiber in this exposure was used in the coadd of camera Z
===================== ======= ======== =======================================================================================================


Notes and Examples
==================

For the SURVEY=cmx m33 tile (TILEID=80615) tile and all the SURVEY=sv1 tiles (except TILEID=80971-80976, the dc3r2 ones), proper-motion correction was applied at the :doc:`fiberassign </DESI_TARGET/fiberassign/tiles/TILES_VERSION/TILEXX/fiberassign-TILEID>` design step; thus the following columns can have different values than in the :doc:`desitarget products </DESI_TARGET/TARG_DIR/DR/VERSION/targets/PHASE/RESOLVE/OBSCON/PHASEtargets-OBSCON-RESOLVE-hp-HP>`: ``TARGET_RA``, ``TARGET_DEC``, ``REF_EPOCH``, ``PLATE_RA``, ``PLATE_DEC``, and ``PLATE_REF_EPOCH``.

For targets with a non-zero proper motion, ``FIBER_RA`` and ``FIBER_DEC`` refer to the position at the reference epoch (but note that the proper-motion correction has been applied at the time of the observation, it is just not recorded in ``FIBER_RA`` and ``FIBER_DEC``).
