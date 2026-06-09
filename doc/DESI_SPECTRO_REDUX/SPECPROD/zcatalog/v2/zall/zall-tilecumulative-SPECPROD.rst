=================================
zall-tilecumulative-SPECPROD.fits
=================================

:Summary: Concatenation of all ``ztile-*-cumulative.fits`` files, combining
          core redshift and targeting columns across all TILEs, SURVEYs, and
          PROGRAMs.
:Naming Convention: ``zcatalog/v2/zall/zall-tilecumulative-{SPECPROD}.fits``, where ``{SPECPROD}``
    is the official name of the full reduction, *e.g.* ``iron``.
:Regex: ``zall-tilecumulative-[a-z0-9][a-z0-9_-]*(?<!-imaging)(?<!-extra)\.fits``
:File Type: FITS, ~5 GB

This file contains a concatenation of all input
:doc:`ztile-*-cumulative.fits <../SURVEY/ztile-SURVEY-PROGRAM-GROUPTYPE>` core files,
combining redshift catalog entries across TILEs, SURVEYs and PROGRAMs. It adds
``SURVEY`` and ``PROGRAM`` columns identifying each entry's origin, and adds
``SV_PRIMARY``/``SV_NSPEC`` and ``MAIN_PRIMARY``/``MAIN_NSPEC`` when the same
``TARGETID`` appears in multiple surveys.

The companion
:doc:`zall-tilecumulative-SPECPROD-imaging.fits <./zall-tilecumulative-SPECPROD-imaging>`
and
:doc:`zall-tilecumulative-SPECPROD-extra.fits <./zall-tilecumulative-SPECPROD-extra>`
files contain the imaging photometry and extra columns respectively, row-matched
to this file.

Contents
========

====== ========= ======== ============================================================
Number EXTNAME   Type     Contents
====== ========= ======== ============================================================
HDU0_  PRIMARY   IMAGE    Empty
HDU1_  ZCATALOG  BINTABLE Core redshift catalog across all tiles, surveys, and programs
====== ========= ======== ============================================================


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

EXTNAME = ZCATALOG

Core redshift and targeting columns stacked from all
:doc:`ztile-SURVEY-PROGRAM-GROUPTYPE.fits <../SURVEY/ztile-SURVEY-PROGRAM-GROUPTYPE>`
cumulative files.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ============ ================ ==== =======================
    KEY          Example Value    Type Comment
    ============ ================ ==== =======================
    NAXIS1       280              int  width of table in bytes
    NAXIS2       10000000         int  number of rows in table
    CHECKSUM     QA6lQ26iQ96iQ96i str  HDU checksum
    DATASUM      4284326946       str  data unit checksum
    ZCATVER      v2               str  Version of zcatalog files
    ============ ================ ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

========================== =========== ======= =====================================================================================================================================
Name                       Type        Units   Description
========================== =========== ======= =====================================================================================================================================
TARGETID                   int64               Unique DESI target ID
SURVEY                     char[7]             Survey name
PROGRAM                    char[6]             DESI program type - BRIGHT, DARK, BACKUP, OTHER
TILEID                     int32               Unique DESI tile ID
LASTNIGHT                  int32               Final night of observation included in a series of coadds
Z_BEST                     float64             Best redshift: equals Z (Redrock) for most targets, Z_QSO (QuasarNET) for confirmed QSOs where the two differ by >1000 km/s
Z_CONF                     uint8               Redshift confidence: 0=no confidence, 1=low confidence (ZWARN==0), 3=high confidence (passes LSS quality cuts)
ZERR_BEST                  float64             Redshift error for Z_BEST
ZWARN_BEST                 int32               Redshift warning bitmask for Z_BEST
SPECTYPE_BEST              char[6]             Spectral type for Z_BEST (e.g. GALAXY, QSO, STAR)
SUBTYPE_BEST               char[3]             Spectral subtype for Z_BEST
CHI2_BEST                  float32             Best fit chi squared for Z_BEST
DELTACHI2_BEST             float32             chi2 difference between first- and second-best fits for Z_BEST
PETAL_LOC                  int16               Petal location [0-9]
FIBER                      int32               Fiber ID on the CCDs [0-4999]
COADD_FIBERSTATUS          int32               bitwise-AND of input FIBERSTATUS
TARGET_RA                  float64     deg     Barycentric Right Ascension in ICRS
TARGET_DEC                 float64     deg     Barycentric Declination in ICRS
DESINAME                   char[22]            Human readable identifier of a sky location DESI JXXX.XXXX[+/-]YY.YYYY, where X,Y=truncated decimal TARGET_RA, TARGET_DEC, precise to 0.36 arcsec. Multiple objects can map to a single DESINAME if very close on the sky.
OBJTYPE                    char[3]             Object type: TGT, SKY, NON, BAD
FIBERASSIGN_X              float32     mm      Fiberassign expected CS5 X location on focal plane
FIBERASSIGN_Y              float32     mm      Fiberassign expected CS5 Y location on focal plane
PRIORITY                   int32               Target current priority
CMX_TARGET [1]_            int64               Target selection bitmask for commissioning
SV1_DESI_TARGET [1]_       int64               DESI (dark time program) target selection bitmask for SV1
SV1_BGS_TARGET [1]_        int64               BGS (bright time program) target selection bitmask for SV1
SV1_MWS_TARGET [1]_        int64               MWS (bright time program) target selection bitmask for SV1
SV1_SCND_TARGET [1]_       int64               Secondary target selection bitmask for SV1
SV2_DESI_TARGET [1]_       int64               DESI (dark time program) target selection bitmask for SV2
SV2_BGS_TARGET [1]_        int64               BGS (bright time program) target selection bitmask for SV2
SV2_MWS_TARGET [1]_        int64               MWS (bright time program) target selection bitmask for SV2
SV2_SCND_TARGET [1]_       int64               Secondary target selection bitmask for SV2
SV3_DESI_TARGET [1]_       int64               DESI (dark time program) target selection bitmask for SV3
SV3_BGS_TARGET [1]_        int64               BGS (bright time program) target selection bitmask for SV3
SV3_MWS_TARGET [1]_        int64               MWS (bright time program) target selection bitmask for SV3
SV3_SCND_TARGET [1]_       int64               Secondary target selection bitmask for SV3
DESI_TARGET [1]_           int64               DESI (dark time program) target selection bitmask
BGS_TARGET [1]_            int64               BGS (bright time program) target selection bitmask
MWS_TARGET [1]_            int64               MWS (bright time program) target selection bitmask
SCND_TARGET [1]_           int64               Secondary target selection bitmask
COADD_NUMEXP               int16               Number of exposures in coadd
COADD_EXPTIME              float32     s       Summed exposure time for coadd
COADD_NUMNIGHT             int16               Number of nights in coadd
COADD_NUMTILE              int16               Number of tiles in coadd
MIN_MJD                    float64     d       Minimum value of the Modified Julian Date (when the shutter was open for the first exposure used in the coadded spectrum)
MAX_MJD                    float64     d       Maximum value of the Modified Julian Date (when the shutter was open for the last exposure used in the coadded spectrum)
MEAN_MJD                   float64     d       Mean value of the Modified Julian Date (when the shutter was open for exposures used in the coadded spectrum)
GOOD_SPEC                  logical             True if this is a science target with good hardware/fiber status
EFFTIME_SPEC               float32     s       Effective exposure time for spectroscopy (from TSNR2_LRG; see Notes)
ZCAT_NSPEC                 int16               Number of times this TARGETID appears in this catalog
ZCAT_PRIMARY               logical             Boolean flag (True/False) for the primary coadded spectrum in this zcatalog
SV_NSPEC [1]_              int16               Number of coadded spectra for this TARGETID in SV (SV1+2+3)
SV_PRIMARY [1]_            logical             Boolean flag (True/False) for the primary coadded spectrum in SV (SV1+2+3)
MAIN_NSPEC [1]_            int16               Number of coadded spectra for this TARGETID in Main survey
MAIN_PRIMARY [1]_          logical             Boolean flag (True/False) for the primary coadded spectrum in Main survey
========================== =========== ======= =====================================================================================================================================

.. [1] Optional

Notes:

  * ``SV_NSPEC`` and ``SV_PRIMARY`` are present when any SV (sv1/sv2/sv3) entries exist.
  * ``MAIN_NSPEC`` and ``MAIN_PRIMARY`` are present when any ``SURVEY=main`` entries exist.
  * ``FIRSTNIGHT`` is in the companion
    :doc:`zall-tilecumulative-SPECPROD-extra.fits <./zall-tilecumulative-SPECPROD-extra>` file.
  * The targeting bitmasks ``DESI_TARGET``, ``BGS_TARGET``, ``MWS_TARGET``, and ``SCND_TARGET``
    only apply to ``SURVEY="main"`` targets; they are `not` set for targets in other surveys.
  * Similarly, the ``SV1_DESI_TARGET`` etc. target masks are only set for the corresponding
    survey; there is no propagation of targeting bits across surveys.
  * ``EFFTIME_SPEC`` is the effective exposure time computed as ``SNR2TIME * TSNR2_X``,
    where ``TSNR2_X`` is chosen by program: ``TSNR2_LRG`` for dark, ``TSNR2_BGS`` for
    bright, ``TSNR2_GPBBACKUP`` for backup. ``SNR2TIME`` is a per-tracer normalization
    factor from the TSNR ensemble template files in ``desimodel``.
