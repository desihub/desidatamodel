======================
exposure-qa-EXPID.fits
======================

:Summary: These files contain the per-exposure QA measurements.
    Those are propagated when making coadd reductions,
    and helps to decide during operations if the observation is valid or not.
:Naming Convention: ``exposure-qa-{expid}``, where ``{expid}``
    is the 8-digit exposure ID.
:Regex: ``exposure-qa-[0-9]{8}\.fits``
:File Type: FITS, 441 KB

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
    CHECKSUM C4gFE4Z9C4fCC4Z9 str  HDU checksum updated 2021-07-16T14:31:54
    DATASUM  0                str  data unit checksum updated 2021-07-16T14:31:54
    ======== ================ ==== ==============================================

Empty HDU.

HDU1
----

EXTNAME = FIBERQA

This table contains the per-fiber information which helps to decide if the observation is valid
or not.
That information is also used to define some column content of the PETALQA extension.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ============= =================== ===== ==============================================
    KEY           Example Value       Type  Comment
    ============= =================== ===== ==============================================
    NAXIS1        86                  int   length of dimension 1
    NAXIS2        5000                int   length of dimension 2
    NIGHT         20210514            int   Exposure night
    EXPID         88364               int   Exposure ID
    NGOODFIB      4611                int   Number of fibers with EFFTIME_SPEC above the threshold
    NGOODPET      10                  int   Number of petals with good fibers
    WORSTRDN      5.072375888924774   float Worst read noise for all amplifiers of all cameras
    FPRMS2D       0.01157238915902728 float [mm] RMS of the positioners accuracy (measured-requested) in the CS5 location of the focal plane
    PMINEXPF [1]_ 0.8370916420971888  float Deprecated
    PMAXEXPF [1]_ 1.27911264193688    float Deprecated
    EFFTIME       217.9705047607422   float [s] Spectroscopic effective time
    TILEID        21181               int   Tile ID
    EXPTIME       589.277             float [s] Tile exposure time
    MJD-OBS       59349.20075297      float [d] Modified Julian Date of observation
    TARGTRA       199.993521          float [deg] Target right ascension (to TCS)
    TARGTDEC      32.447031           float [deg] Target declination (to TCS)
    MOUNTEL       84.320435           float [deg] Mount elevation angle
    MOUNTHA       -6.689017           float [deg] Mount hour angle
    AIRMASS       1.004188            float Airmass
    ETCTEFF [1]_  1015.311096         float [s] Effective time computed (on-the-fly) by the ETC
    TILERA        199.992             float [deg] Tile center Right Ascension
    TILEDEC       32.447              float [deg] Tile center Declination
    GOALTIME [1]_ 180.0               float [s] Aimed EFFTIME_SPEC
    GOALTYPE [1]_ BRIGHT              str   Sky conditions used for some noise estimation
    FAPRGRM [1]_  bright              str   Program to which this tile belongs
    SURVEY [1]_   main                str   Survey of origin of the targets
    EBVFAC [1]_   1.02512649227135    float 10.0 ** (2.165 * median(EBV) / 2.5))
    MINTFRAC [1]_ 0.85                float Fraction of GOALTIME to be reached by EFFTIME_SPEC to consider the tile has completed
    CHECKSUM      YP2AYM16YM1AYM13    str   HDU checksum updated 2021-07-16T14:31:54
    DATASUM       2084006317          str   data unit checksum updated 2021-07-16T14:31:54
    ============= =================== ===== ==============================================

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
FIBER_X       float64 mm    Fiber CS5 X location on focal plane
FIBER_Y       float64 mm    Fiber CS5 Y location on focal plane
DELTA_X       float64 mm    Fiber difference between measured and requested CS5 X location on focal plane
DELTA_Y       float64 mm    Fiber difference between measured and requested CS5 Y location on focal plane
EBV           float32 mag   Galactic extinction E(B-V) reddening
QAFIBERSTATUS int32         Fiber status bitmask, inflated with further QA diagnoses
EFFTIME_SPEC  float32 s     Spectroscopic effective time, based on template-based squared signal-to-noise ratio
============= ======= ===== ===========

HDU2
----

EXTNAME = PETALQA

This table contains some per-petal QA information which helps to decide if the observation is valid
or not, and if a petal should be considered as "bad" (i.e. as if it would not have been observed),
because of a too-low quality.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   62               int  length of dimension 1
    NAXIS2   10               int  length of dimension 2
    CHECKSUM 8aaf9WRc8aXc8WXc str  HDU checksum updated 2021-07-16T14:31:54
    DATASUM  666368269        str  data unit checksum updated 2021-07-16T14:31:54
    ======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

============== ======= ===== ===========
Name           Type    Units Description
============== ======= ===== ===========
PETAL_LOC      int16         Petal location [0-9]
WORSTREADNOISE float32       Worst read noise (each individual value being the worst across amplifiers)
NGOODPOS       int16         Number of valid positioners
NGOODFIB       int16         Number of good fibers
NSTDSTAR       int16         Number of standard stars used by the spectroscopic pipeline for calibration
STARRMS        float32       RMS of the r-band flux ratio of standard stars
TSNR2FRA [1]_  float32       Deprecated
EFFTIME_SPEC   float32 s     Median of the EFFTIME_SPEC values for all good fibers from that petal
NCFRAME        int16         Number of cframe files for that petal
BSKYTHRURMS    float32       Sky throuput RMS for the b-camera
BSKYCHI2PDF    float32       Reduced chi2 for the sky fibers for the b-camera
RSKYTHRURMS    float32       Sky throuput RMS for the r-camera
RSKYCHI2PDF    float32       Reduced chi2 for the sky fibers for the r-camera
ZSKYTHRURMS    float32       Sky throuput RMS for the z-camera
ZSKYCHI2PDF    float32       Reduced chi2 for the sky fibers for the z-camera
BTHRUFRAC      float32       Relative (single petal vs. all petals) throughput for the b-camera
RTHRUFRAC      float32       Relative (single petal vs. all petals) throughput for the r-camera
ZTHRUFRAC      float32       Relative (single petal vs. all petals) throughput for the z-camera
============== ======= ===== ===========

.. [1] Optional

Notes and Examples
==================

* These ``exposure-qa-{expid}`` files are used to compute several of the :doc:`tile-qa-TILEID-GROUPID <../../../tiles/GROUPTYPE/TILEID/GROUPID/tile-qa-TILEID-GROUPID>` entries.
* The QAFIBERSTATUS bitmasks are defined here :doc:`bitmasks <../../../../../../bitmasks>`.
* Some FIBERQA extension header keywords are originally coming from the :doc:`fiberassign-TILEID <../../../../../DESI_TARGET/fiberassign/tiles/TILES_VERSION/TILEXX/fiberassign-TILEID>` file (TILEID, TILERA, TILEDEC, GOALTIME, GOALTYPE, FAPRGRM, SURVEY, EBVFAC, MINTFRAC).
* The FIBERQA EFFTIME_SPEC is proportional to the TSNR2 values in the TSNR2 extension of the :doc:`redrock-SPECTROGRAPH-TILEID-GROUPID <../../../tiles/GROUPTYPE/TILEID/GROUPID/redrock-SPECTROGRAPH-TILEID-GROUPID>` file; for the BACKUP and BRIGHT programs, the TSNR2_BGS is used; for the DARK program, the TSNR2_ELG or TSNR2_LRG is used.
* For the SURVEY=cmx m33 tile (TILEID=80615) tile and all the SURVEY=sv1 tiles (except TILEID=80971-80976, the dc3r2 ones), proper-motion correction was applied at the :doc:`fiberassign </DESI_TARGET/fiberassign/tiles/TILES_VERSION/TILEXX/fiberassign-TILEID>` design step; thus the following columns can have different values than in the :doc:`desitarget products </DESI_TARGET/TARG_DIR/DR/VERSION/targets/PHASE/RESOLVE/OBSCON/PHASEtargets-OBSCON-RESOLVE-hp-HP>`: ``TARGET_RA``, ``TARGET_DEC``, ``REF_EPOCH``, ``PLATE_RA``, ``PLATE_DEC``, and ``PLATE_REF_EPOCH``.
