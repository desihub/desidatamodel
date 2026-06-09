========================
zpix-SURVEY-PROGRAM.fits
========================

:Summary: Core redshift and targeting columns from the healpix-based redshift
          catalogs, one file per SURVEY and PROGRAM.
:Naming Convention: ``zcatalog/v2/SURVEY/zpix-SURVEY-PROGRAM.fits``, where ``SURVEY`` is
    *e.g.* ``main`` or ``sv1`` and ``PROGRAM`` is *e.g.* ``bright`` or ``dark``.
:Regex: ``zpix-(cmx|main|sv1|sv2|sv3|special)-(backup|bright|dark|other)\.fits``
:File Type: FITS, ~100 MB

Contents
========

====== ========= ======== ============================================================
Number EXTNAME   Type     Contents
====== ========= ======== ============================================================
HDU0_  PRIMARY   IMAGE    Empty
HDU1_  ZCATALOG  BINTABLE Core redshift catalog joined with targeting metadata
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

.. _zcatalog-v2-zpix-hdu1:

HDU1
----

EXTNAME = ZCATALOG

Core redshift and targeting columns from the
:doc:`healpix-based Redrock redshift catalogs </DESI_SPECTRO_REDUX/SPECPROD/healpix/SURVEY/PROGRAM/PIXGROUP/PIXNUM/redrock-SURVEY-PROGRAM-PIXNUM>`.
Imaging photometry columns are in the companion
:doc:`zpix-SURVEY-PROGRAM-imaging.fits <./zpix-SURVEY-PROGRAM-imaging>` file.
All remaining columns (full Redrock output, TSNR2, emission lines, QuasarNET,
quality flags) are in
:doc:`zpix-SURVEY-PROGRAM-extra.fits <./zpix-SURVEY-PROGRAM-extra>`.

``Z_BEST`` is the recommended redshift to use. It equals ``Z`` (Redrock) for most
targets, but is set to ``Z_QSO`` (QuasarNET) for confirmed QSO targets where the
two differ by more than 1000 km/s. ``Z_CONF`` encodes the overall confidence:
0 = no confidence; 1 = ZWARN==0 but not LSS-quality; 3 = passes LSS quality cuts
for at least one extragalactic tracer class.

``TEMNAMnn`` and ``TEMVERnn`` record the Redrock template names and versions
used for the redshift fits.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ============ ================ ==== =======================
    KEY          Example Value    Type Comment
    ============ ================ ==== =======================
    NAXIS1       261              int  width of table in bytes
    NAXIS2       139728           int  number of rows in table
    LONGSTRN     OGIP 1.0         str
    RRVER        0.15.0           str  Redrock version
    TEMNAM00     GALAXY           str  Redrock template 00 name
    TEMVER00     2.6              str  Redrock template 00 version
    TEMNAM01     QSO:::HIZ        str
    TEMVER01     0.1              str
    TEMNAM02     QSO:::LOZ        str
    TEMVER02     1.0              str
    TEMNAM03     STAR:::A         str
    TEMVER03     0.1              str
    TEMNAM04     STAR:::B         str
    TEMVER04     0.1              str
    TEMNAM05     STAR:::CV        str
    TEMVER05     0.1              str
    TEMNAM06     STAR:::F         str
    TEMVER06     0.1              str
    TEMNAM07     STAR:::G         str
    TEMVER07     0.1              str
    TEMNAM08     STAR:::K         str
    TEMVER08     0.1              str
    TEMNAM09     STAR:::M         str
    TEMVER09     0.1              str
    TEMNAM10     STAR:::WD        str
    TEMVER10     0.1              str
    SPGRP        healpix          str  Spectral grouping method
    HPXNSIDE     64               int  Healpix nside
    HPXNEST      T                bool Nested healpix (not ring)
    SURVEY [1]_  main             str  DESI sub-survey (e.g. sv1, sv3, main)
    PROGRAM [1]_ dark             str  DESI program (e.g. dark, bright)
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
UNIQPIX [1]_               int32               Unique HEALPixel identifier encoding both pixel number and NSIDE (DR3+); HEALPIX and NSIDE are in the companion extra file
HEALPIX [1]_               int32               HEALPixel containing this location at NSIDE=64 in the NESTED scheme (DR2 only)
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
========================== =========== ======= =====================================================================================================================================

.. [1] Optional
.. _`LS`: https://www.legacysurvey.org/
.. _`DR9 bitmasks page`: https://www.legacysurvey.org/dr9/bitmasks
.. _`Gaia`: https://gea.esac.esa.int/archive/documentation//GDR2/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html
.. _SFD98: https://ui.adsabs.harvard.edu/abs/1998ApJ...500..525S/abstract

Notes:

  * The targeting bitmasks ``DESI_TARGET``, ``BGS_TARGET``, ``MWS_TARGET``, and ``SCND_TARGET``
    only apply to ``SURVEY="main"`` targets; they are `not` set for targets in other surveys.
  * Similarly, the ``SV1_DESI_TARGET`` etc. target masks are only set for the corresponding
    survey; there is no propagation of targeting bits across surveys.
  * ``GOOD_Z_{BGS,LRG,ELG,QSO}`` flags are in the companion
    :doc:`zpix-SURVEY-PROGRAM-extra.fits <./zpix-SURVEY-PROGRAM-extra>` file.
  * This file does not contain ``SV_NSPEC``, ``SV_PRIMARY``, ``MAIN_NSPEC``, or
    ``MAIN_PRIMARY``; these are added when zpix files are combined into
    :doc:`zall-pix-SPECPROD.fits <../zall/zall-pix-SPECPROD>`.
  * ``EFFTIME_SPEC`` is the effective exposure time computed as ``SNR2TIME * TSNR2_X``,
    where ``TSNR2_X`` is chosen by program: ``TSNR2_LRG`` for dark, ``TSNR2_BGS`` for
    bright, ``TSNR2_GPBBACKUP`` for backup. ``SNR2TIME`` is a per-tracer normalization
    factor from the TSNR ensemble template files in ``desimodel``.


Notes and Examples
==================

For the SURVEY=cmx m33 tile (TILEID=80615) tile and all the SURVEY=sv1 tiles (except TILEID=80971-80976, the dc3r2 ones), proper-motion correction was applied at the :doc:`fiberassign </DESI_TARGET/fiberassign/tiles/TILES_VERSION/TILEXX/fiberassign-TILEID>` design step; thus the following columns can have different values than in the :doc:`desitarget products </DESI_TARGET/TARG_DIR/DR/VERSION/targets/PHASE/RESOLVE/OBSCON/PHASEtargets-OBSCON-RESOLVE-hp-HP>`: ``TARGET_RA``, ``TARGET_DEC``, ``REF_EPOCH``, ``PLATE_RA``, ``PLATE_DEC``, and ``PLATE_REF_EPOCH``.
