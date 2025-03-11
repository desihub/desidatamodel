===================================
ztile-SURVEY-PROGRAM-GROUPTYPE.fits
===================================

:Summary: This file contatenates the individual
          :doc:`tile-based Redrock redshift catalogs </DESI_SPECTRO_REDUX/SPECPROD/tiles/GROUPTYPE/TILEID/GROUPID/redrock-SPECTROGRAPH-TILEID-GROUPID>`
          into a single file per SURVEY, PROGRAM, and spectral GROUPTYPE.
:Naming Convention: ``ztile-SURVEY-PROGRAM-GROUPTYPE.fits``, where ``SURVEY`` is
    *e.g.* ``main`` or ``sv1``, ``PROGRAM`` is *e.g.* ``bright or ``dark``,
    and ``GROUPTYPE`` is ``cumulative`` or ``pernight``.
:Regex: ``ztile-(cmx|main|sv1|sv2|sv3|special)-(backup|bright|dark|other)-(cumulative|perexp|pernight|1x_depth|4x_depth|lowspeed)\.fits``
:File Type: FITS, 4 MB

Contents
========

====== ============ ======== ===================
Number EXTNAME      Type     Contents
====== ============ ======== ===================
HDU0_  PRIMARY      IMAGE    Empty
HDU1_  ZCATALOG     BINTABLE Redshift catalog joined with target catalog
HDU2_  EXP_FIBERMAP BINTABLE Per-exposure entries from input fibermaps
====== ============ ======== ===================


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
    ZCATVER      v1               str  Version of zcatalog files
    ============ ================ ==== =======================

Empty HDU.

.. _zcatalog-ztile-hdu1:

HDU1
----

EXTNAME = ZCATALOG

Redshift catalog joined with the targeting metadata from the REDSHIFTS
and FIBERMAP HDUs of the
:doc:`input redrock files </DESI_SPECTRO_REDUX/SPECPROD/tiles/GROUPTYPE/TILEID/GROUPID/redrock-SPECTROGRAPH-TILEID-GROUPID>`.

``TEMNAMnn`` and ``TEMVERnn`` record the redrock template names and versions
used for the redshift fits.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ============ ================ ==== =======================
    KEY          Example Value    Type Comment
    ============ ================ ==== =======================
    NAXIS1       677              int  width of table in bytes
    NAXIS2       5000             int  number of rows in table
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
    SPGRP        cumulative       str  Spectral grouping method
    SURVEY [1]_  sv3              str  DESI sub-survey (e.g. sv1, sv3, main)
    PROGRAM [1]_ dark             str  DESI program (e.g. dark, bright)
    CHECKSUM     QA6lQ26iQ96iQ96i str  HDU checksum
    DATASUM      4284326946       str  data unit checksum
    ZCATVER      v1               str  Version of zcatalog files
    ============ ================ ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

========================== =========== ============ =====================================================================================================================================
Name                       Type        Units        Description
========================== =========== ============ =====================================================================================================================================
TARGETID                   int64                    Unique DESI target ID
SURVEY [1]_                char[7]                  Survey name
PROGRAM [1]_               char[6]                  DESI program type - BRIGHT, DARK, BACKUP, OTHER
FIRSTNIGHT                 int32                    KPNO Calendar Date when the first exposure was obtained (regardless of data quality)
LASTNIGHT                  int32                    Final night of observation included in a series of coadds
SPGRPVAL                   int32                    Value by which spectra are grouped for a coadd (e.g. a YEARMMDD night)
Z                          float64                  Redshift measured by Redrock
ZERR                       float64                  Redshift error from redrock
ZWARN                      int64                    Redshift warning bitmask from Redrock
CHI2                       float64                  Best fit chi squared
COEFF                      float64[10]              Redrock template coefficients
NPIXELS                    int64                    Number of unmasked pixels contributing to the Redrock fit
SPECTYPE                   char[6]                  Spectral type of Redrock best fit template (e.g. GALAXY, QSO, STAR)
SUBTYPE                    char[20]                 Spectral subtype
NCOEFF                     int64                    Number of Redrock template coefficients
DELTACHI2                  float64                  chi2 difference between first- and second-best redrock template fits
PETAL_LOC                  int16                    Petal location [0-9]
DEVICE_LOC                 int32                    Device location on focal plane [0-523]
LOCATION                   int64                    Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBER                      int32                    Fiber ID on the CCDs [0-4999]
COADD_FIBERSTATUS          int32                    bitwise-AND of input FIBERSTATUS
TARGET_RA                  float64     deg          Barycentric Right Ascension in ICRS
TARGET_DEC                 float64     deg          Barycentric Declination in ICRS
PMRA                       float32     mas yr^-1    Reference catalog proper motion in the RA direction
PMDEC                      float32     mas yr^-1    Reference catalog proper motion in the Dec direction
REF_EPOCH                  float32     yr           Reference catalog reference epoch (*e.g.*, 2015.5 for Gaia_ DR2)
LAMBDA_REF                 float32     Angstrom     Requested wavelength at which targets should be centered on fibers
FA_TARGET                  int64                    Targeting bit internally used by fiberassign (linked with FA_TYPE)
FA_TYPE                    binary                   Fiberassign internal target type (science, standard, sky, safe, suppsky)
OBJTYPE                    char[3]                  Object type: TGT, SKY, NON, BAD
FIBERASSIGN_X              float32     mm           Fiberassign expected CS5 X location on focal plane
FIBERASSIGN_Y              float32     mm           Fiberassign expected CS5 Y location on focal plane
PRIORITY                   int32                    Target current priority
SUBPRIORITY                float64                  Random subpriority [0-1] to break assignment ties
OBSCONDITIONS              int32                    Flag the target to be observed in graytime.
RELEASE                    int16                    Legacy Surveys (`LS`_) `Release`_
BRICKNAME                  char[8]                  Brick name from tractor input
BRICKID                    int32                    Brick ID from tractor input
BRICK_OBJID                int32                    OBJID (unique to brick, but not to file)
MORPHTYPE                  char[4]                  `Morphological Model`_ type
EBV                        float32     mag          Galactic extinction E(B-V) reddening from SFD98_
FLUX_G                     float32     nanomaggy    `LS`_ flux from tractor input (g)
FLUX_R                     float32     nanomaggy    `LS`_ flux from tractor input (r)
FLUX_Z                     float32     nanomaggy    `LS`_ flux from tractor input (z)
FLUX_W1                    float32     nanomaggy    WISE flux in W1
FLUX_W2                    float32     nanomaggy    WISE flux in W2
FLUX_IVAR_G                float32     nanomaggy^-2 Inverse Variance of FLUX_G
FLUX_IVAR_R                float32     nanomaggy^-2 Inverse Variance of FLUX_R
FLUX_IVAR_Z                float32     nanomaggy^-2 Inverse Variance of FLUX_Z
FLUX_IVAR_W1               float32     nanomaggy^-2 Inverse Variance of FLUX_W1
FLUX_IVAR_W2               float32     nanomaggy^-2 Inverse Variance of FLUX_W2
FIBERFLUX_G                float32     nanomaggy    Predicted g-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERFLUX_R                float32     nanomaggy    Predicted r-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERFLUX_Z                float32     nanomaggy    Predicted z-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERTOTFLUX_G             float32     nanomaggy    Predicted g-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
FIBERTOTFLUX_R             float32     nanomaggy    Predicted r-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
FIBERTOTFLUX_Z             float32     nanomaggy    Predicted z-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
MASKBITS                   int16                    Bitwise mask indicating that an object touches a pixel in the ``coadd/*/*/*maskbits*`` maps, as cataloged on the `DR9 bitmasks page`_
SERSIC                     float32                  Power-law index for the Sersic profile model (``type="SER"``)
SHAPE_R                    float32     arcsec       Half-light radius of galaxy model for galaxy type ``type`` (>0)
SHAPE_E1                   float32                  `Ellipticity component`_ 1 of galaxy model for galaxy type ``type``
SHAPE_E2                   float32                  `Ellipticity component`_ 2 of galaxy model for galaxy type ``type``
REF_ID                     int64                    Tyc1*1,000,000+Tyc2*10+Tyc3 for `Tycho-2`_; "sourceid" for `Gaia`_ DR2
REF_CAT                    char[2]                  Reference catalog source for this star: "T2" for `Tycho-2`_, "G2" for `Gaia`_ DR2, "L3" for the SGA_, empty otherwise
GAIA_PHOT_G_MEAN_MAG       float32     mag          `Gaia`_ G band magnitude
GAIA_PHOT_BP_MEAN_MAG      float32     mag          `Gaia`_ BP band magnitude
GAIA_PHOT_RP_MEAN_MAG      float32     mag          `Gaia`_ RP band magnitude
PARALLAX                   float32     mas          Reference catalog parallax
PHOTSYS                    char[1]                  'N' for the MzLS/BASS photometric system, 'S' for DECaLS
PRIORITY_INIT              int64                    Target initial priority from target selection bitmasks and OBSCONDITIONS
NUMOBS_INIT                int64                    Initial number of observations for target calculated across target selection bitmasks and OBSCONDITIONS
CMX_TARGET [1]_            int64                    Target selection bitmask for commissioning
SV1_DESI_TARGET [1]_       int64                    DESI (dark time program) target selection bitmask for SV1
SV1_BGS_TARGET [1]_        int64                    BGS (bright time program) target selection bitmask for SV1
SV1_MWS_TARGET [1]_        int64                    MWS (bright time program) target selection bitmask for SV1
SV1_SCND_TARGET [1]_       int64                    Secondary target selection bitmask for SV1
SV2_DESI_TARGET [1]_       int64                    DESI (dark time program) target selection bitmask for SV2
SV2_BGS_TARGET [1]_        int64                    BGS (bright time program) target selection bitmask for SV2
SV2_MWS_TARGET [1]_        int64                    MWS (bright time program) target selection bitmask for SV2
SV2_SCND_TARGET [1]_       int64                    Secondary target selection bitmask for SV2
SV3_DESI_TARGET [1]_       int64                    DESI (dark time program) target selection bitmask for SV3
SV3_BGS_TARGET [1]_        int64                    BGS (bright time program) target selection bitmask for SV3
SV3_MWS_TARGET [1]_        int64                    MWS (bright time program) target selection bitmask for SV3
SV3_SCND_TARGET [1]_       int64                    Secondary target selection bitmask for SV3
DESI_TARGET                int64                    DESI (dark time program) target selection bitmask
BGS_TARGET                 int64                    BGS (bright time program) target selection bitmask
MWS_TARGET                 int64                    MWS (bright time program) target selection bitmask
SCND_TARGET                int64                    Secondary target selection bitmask
PLATE_RA                   float64     deg          Barycentric Right Ascension in ICRS to be used by PlateMaker
PLATE_DEC                  float64     deg          Barycentric Declination in ICRS to be used by PlateMaker
TILEID                     int32                    Unique DESI tile ID
COADD_NUMEXP               int16                    Number of exposures in coadd
COADD_EXPTIME              float32     s            Summed exposure time for coadd
COADD_NUMNIGHT             int16                    Number of nights in coadd
COADD_NUMTILE              int16                    Number of tiles in coadd
MEAN_DELTA_X               float32     mm           Mean (over exposures) fiber difference requested - actual CS5 X location on focal plane
RMS_DELTA_X                float32     mm           RMS (over exposures) of the fiber difference between measured and requested CS5 X location on focal plane
MEAN_DELTA_Y               float32     mm           Mean (over exposures) fiber difference requested - actual CS5 Y location on focal plane
RMS_DELTA_Y                float32     mm           RMS (over exposures) of the fiber difference between measured and requested CS5 Y location on focal plane
MEAN_PSF_TO_FIBER_SPECFLUX float32                  Mean of input exposures fraction of light from point-like source captured by 1.5 arcsec diameter fiber given atmospheric seeing
MEAN_FIBER_RA              float64     deg          Mean (over exposures) RA of actual fiber position
STD_FIBER_RA               float32     arcsec       Standard deviation (over exposures) of RA of actual fiber position
MEAN_FIBER_DEC             float64     deg          Mean (over exposures) DEC of actual fiber position
STD_FIBER_DEC              float32     arcsec       Standard deviation (over exposures) of DEC of actual fiber position
MIN_MJD                    float64     d            Minimum value of the Modified Julian Date (when the shutter was open for the first exposure used in the coadded spectrum)
MAX_MJD                    float64     d            Maximum value of the Modified Julian Date (when the shutter was open for the last exposure used in the coadded spectrum)
MEAN_MJD                   float64     d            Mean value of the Modified Julian Date (when the shutter was open for exposures used in the coadded spectrum)
MEAN_FIBER_X               float32     mm           Mean (over exposures) fiber CS5 X location on focal plane
MEAN_FIBER_Y               float32     mm           Mean (over exposures) fiber CS5 X location on focal plane
TSNR2_GPBDARK_B            float32                  template (S/N)^2 for dark targets in guider pass band on B
TSNR2_ELG_B                float32                  ELG B template (S/N)^2
TSNR2_GPBBRIGHT_B          float32                  template (S/N)^2 for bright targets in guider pass band on B
TSNR2_LYA_B                float32                  LYA B template (S/N)^2
TSNR2_BGS_B                float32                  BGS B template (S/N)^2
TSNR2_GPBBACKUP_B          float32                  template (S/N)^2 for backup targets in guider pass band on B
TSNR2_QSO_B                float32                  QSO B template (S/N)^2
TSNR2_LRG_B                float32                  LRG B template (S/N)^2
TSNR2_GPBDARK_R            float32                  template (S/N)^2 for dark targets in guider pass band on R
TSNR2_ELG_R                float32                  ELG R template (S/N)^2
TSNR2_GPBBRIGHT_R          float32                  template (S/N)^2 for bright targets in guider pass band on R
TSNR2_LYA_R                float32                  LYA R template (S/N)^2
TSNR2_BGS_R                float32                  BGS R template (S/N)^2
TSNR2_GPBBACKUP_R          float32                  template (S/N)^2 for backup targets in guider pass band on R
TSNR2_QSO_R                float32                  QSO R template (S/N)^2
TSNR2_LRG_R                float32                  LRG R template (S/N)^2
TSNR2_GPBDARK_Z            float32                  template (S/N)^2 for dark targets in guider pass band on Z
TSNR2_ELG_Z                float32                  ELG Z template (S/N)^2
TSNR2_GPBBRIGHT_Z          float32                  template (S/N)^2 for bright targets in guider pass band on Z
TSNR2_LYA_Z                float32                  LYA Z template (S/N)^2
TSNR2_BGS_Z                float32                  BGS Z template (S/N)^2
TSNR2_GPBBACKUP_Z          float32                  template (S/N)^2 for backup targets in guider pass band on Z
TSNR2_QSO_Z                float32                  QSO Z template (S/N)^2
TSNR2_LRG_Z                float32                  LRG Z template (S/N)^2
TSNR2_GPBDARK              float32                  template (S/N)^2 for dark targets in guider pass band
TSNR2_ELG                  float32                  ELG template (S/N)^2 summed over B,R,Z
TSNR2_GPBBRIGHT            float32                  template (S/N)^2 for bright targets in guider pass band
TSNR2_LYA                  float32                  LYA template (S/N)^2 summed over B,R,Z
TSNR2_BGS                  float32                  BGS template (S/N)^2 summed over B,R,Z
TSNR2_GPBBACKUP            float32                  template (S/N)^2 for backup targets in guider pass band
TSNR2_QSO                  float32                  QSO template (S/N)^2 summed over B,R,Z
TSNR2_LRG                  float32                  LRG template (S/N)^2 summed over B,R,Z
SV_NSPEC [1]_              int16                    Number of coadded spectra for this TARGETID in SV (SV1+2+3)
SV_PRIMARY [1]_            logical                  Boolean flag (True/False) for the primary coadded spectrum in SV (SV1+2+3)
MAIN_NSPEC [1]_            int16                    Number of coadded spectra for this TARGETID in Main survey
MAIN_PRIMARY [1]_          logical                  Boolean flag (True/False) for the primary coadded spectrum in Main survey
ZCAT_NSPEC                 int16                    Number of times this TARGETID appears in this catalog
ZCAT_PRIMARY               logical                  Boolean flag (True/False) for the primary coadded spectrum in this zcatalog
DESINAME                   char[22]                 Human readable identifier of a sky location DESI JXXX.XXXX[+/-]YY.YYYY, where X,Y=truncated decimal TARGET_RA, TARGET_DEC, precise to 0.36 arcsec. Multiple objects can map to a single DESINAME if very close on the sky.
========================== =========== ============ =====================================================================================================================================

.. [1] Optional
.. _`LS`: https://www.legacysurvey.org/
.. _`DR9 bitmasks page`: https://www.legacysurvey.org/dr9/bitmasks
.. _`ellipticity component`: https://www.legacysurvey.org/dr9/catalogs/#ellipticities
.. _`Release`: https://www.legacysurvey.org/release/
.. _`Morphological Model`: https://www.legacysurvey.org/dr9/catalogs/#goodness-of-fits-and-morphological-type
.. _`Tycho-2`: https://heasarc.gsfc.nasa.gov/W3Browse/all/tycho2.html
.. _`Gaia`: https://gea.esac.esa.int/archive/documentation//GDR2/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html
.. _SFD98: https://ui.adsabs.harvard.edu/abs/1998ApJ...500..525S/abstract
.. _SGA: https://www.legacysurvey.org/sga/sga2020

Notes:

  * ztile files do not have ``SV_NSPEC`` or ``SV_PRIMARY`` columns;
    these are added when the ztile files are combined into
    :doc:`zall-tilecumulative <./zall-tilecumulative-SPECPROD>` files.
  * ``MAIN_NSPEC`` and ``MAIN_PRIMARY`` were introduced with DR1 for the DESI Main Survey.
  * The targeting bitmasks ``DESI_TARGET``, ``BGS_TARGET``, ``MWS_TARGET``, and ``SCND_TARGET``
    only apply to ``SURVEY="main"`` targets; they are `not` set for targets in other surveys.
  * Similarly, the ``SV1_DESI_TARGET`` etc target masks are only set for the corresponding
    survey; there is no propagation of targeting bits across surveys.


HDU2
----

EXTNAME = EXP_FIBERMAP

Input fibermap entries for columns that apply per-exposure and can't be coadded,
e.g. the individual TILEIDs and FIBERs on which each target was observed.

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
