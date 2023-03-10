========================================
redrock-SPECTROGRAPH-TILEID-GROUPID.fits
========================================

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``redrock-SPECTROGRAPH-TILEID-GROUPID.fits``, where
    ``SPECTROGRAPH`` is the spectrograph ID, ``TILEID`` is the tile number and
    ``GROUPID`` depends on the ``GROUPTYPE`` of the tile coadd.
:Regex: ``redrock-[0-9]-[0-9]+-([14]xsubset[1-6]|lowspeedsubset[1-6]|exp[0-9]{8}|thru[0-9]{8}|[0-9]{8})\.fits``
:File Type: FITS, 450 KB

Contents
========

====== ============ ======== ===================
Number EXTNAME      Type     Contents
====== ============ ======== ===================
HDU0_               IMAGE    Keywords only
HDU1_  REDSHIFTS    BINTABLE *Brief Description*
HDU2_  FIBERMAP     BINTABLE *Brief Description*
HDU3_  EXP_FIBERMAP BINTABLE *Brief Description*
HDU4_  TSNR2        BINTABLE *Brief Description*
====== ============ ======== ===================


FITS Header Units
=================

HDU0
----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ========== ============= ==== ===============
    KEY        Example Value Type Comment
    ========== ============= ==== ===============
    LONGSTRN   OGIP 1.0      str
    RRVER      0.15.0        str  Redrock version
    TEMNAM00   GALAXY        str
    TEMVER00   2.6           str
    TEMNAM01   QSO           str
    TEMVER01   0.1           str
    TEMNAM02   STAR:::A      str
    TEMVER02   0.1           str
    TEMNAM03   STAR:::B      str
    TEMVER03   0.1           str
    TEMNAM04   STAR:::CV     str
    TEMVER04   0.1           str
    TEMNAM05   STAR:::F      str
    TEMVER05   0.1           str
    TEMNAM06   STAR:::G      str
    TEMVER06   0.1           str
    TEMNAM07   STAR:::K      str
    TEMVER07   0.1           str
    TEMNAM08   STAR:::M      str
    TEMVER08   0.1           str
    TEMNAM09   STAR:::WD     str
    TEMVER09   0.1           str
    SPGRP      1x_depth      str
    SPGRPVAL   3             int
    TILEID     80605         int
    SPECTRO    6             int
    PETAL      6             int
    NIGHT [1]_ 20210708      int
    ========== ============= ==== ===============

Empty HDU.

HDU1
----

EXTNAME = REDSHIFTS

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =====================
    KEY    Example Value Type Comment
    ====== ============= ==== =====================
    NAXIS1 170           int  length of dimension 1
    NAXIS2 500           int  length of dimension 2
    ====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

========= =========== ===== ====================================================================
Name      Type        Units Description
========= =========== ===== ====================================================================
TARGETID  int64             Unique DESI target ID
CHI2      float64           Best fit chi squared
COEFF     float64[10]       Redrock template coefficients
Z         float64           Redshift measured by Redrock
ZERR      float64           Redshift error from redrock
ZWARN     int64             Redshift warning bitmask from Redrock
NPIXELS   int64
SPECTYPE  char[6]           Spectral type of Redrock best fit template (e.g. GALAXY, QSO, STAR)
SUBTYPE   char[20]          Spectral subtype
NCOEFF    int64             Number of Redrock template coefficients
DELTACHI2 float64           chi2 difference between first- and second-best redrock template fits
========= =========== ===== ====================================================================

HDU2
----

EXTNAME = FIBERMAP

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =====================
    KEY    Example Value Type Comment
    ====== ============= ==== =====================
    NAXIS1 371           int  length of dimension 1
    NAXIS2 500           int  length of dimension 2
    ====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

========================== ======= ============ ===============================================================================================================================
Name                       Type    Units        Description
========================== ======= ============ ===============================================================================================================================
TARGETID                   int64                Unique DESI target ID
PETAL_LOC                  int16                Petal location [0-9]
DEVICE_LOC                 int32                Device location on focal plane [0-523]
LOCATION                   int64                Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBER                      int32
COADD_FIBERSTATUS          int32                bitwise-AND of input FIBERSTATUS
TARGET_RA                  float64 deg          Target right ascension
TARGET_DEC                 float64 deg          Target declination
PMRA                       float32 mas yr^-1    proper motion in the +RA direction (already including cos(dec))
PMDEC                      float32 mas yr^-1    Proper motion in the +Dec direction
REF_EPOCH                  float32 yr           Reference epoch for Gaia/Tycho astrometry. Typically 2015.5 for Gaia
LAMBDA_REF                 float32 Angstrom     Requested wavelength at which targets should be centered on fibers
FA_TARGET                  int64                Targeting bit internally used by fiberassign (linked with FA_TYPE)
FA_TYPE                    binary               Fiberassign internal target type (science, standard, sky, safe, suppsky)
OBJTYPE                    char[3]              Object type: TGT, SKY, NON, BAD
FIBERASSIGN_X              float32 mm           Fiberassign expected CS5 X location on focal plane
FIBERASSIGN_Y              float32 mm           Fiberassign expected CS5 Y location on focal plane
PRIORITY                   int32                Target current priority
SUBPRIORITY                float64              Random subpriority [0-1) to break assignment ties
OBSCONDITIONS              int32                Bitmask of allowed observing conditions
RELEASE                    int16                Imaging surveys release ID
BRICKNAME                  char[8]              Brick name from tractor input
BRICKID                    int32                Brick ID from tractor input
BRICK_OBJID                int32                Imaging Surveys OBJID on that brick
MORPHTYPE                  char[4]              Imaging Surveys morphological type from Tractor
EBV                        float32 mag          Galactic extinction E(B-V) reddening from SFD98
FLUX_G                     float32 nanomaggy    Flux in the Legacy Survey g-band (AB)
FLUX_R                     float32 nanomaggy    Flux in the Legacy Survey r-band (AB)
FLUX_Z                     float32 nanomaggy    Flux in the Legacy Survey z-band (AB)
FLUX_W1                    float32 nanomaggy    WISE flux in W1 (AB)
FLUX_W2                    float32 nanomaggy    WISE flux in W2 (AB)
FLUX_IVAR_G                float32 nanomaggy^-2 Inverse variance of FLUX_G (AB)
FLUX_IVAR_R                float32 nanomaggy^-2 Inverse variance of FLUX_R (AB)
FLUX_IVAR_Z                float32 nanomaggy^-2 Inverse variance of FLUX_Z (AB)
FLUX_IVAR_W1               float32 nanomaggy^-2 Inverse variance of FLUX_W1 (AB)
FLUX_IVAR_W2               float32 nanomaggy^-2 Inverse variance of FLUX_W2 (AB)
FIBERFLUX_G                float32 nanomaggy    Predicted g-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERFLUX_R                float32 nanomaggy    Predicted r-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERFLUX_Z                float32 nanomaggy    Predicted z-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERTOTFLUX_G             float32 nanomaggy    Predicted g-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
FIBERTOTFLUX_R             float32 nanomaggy    Predicted r-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
FIBERTOTFLUX_Z             float32 nanomaggy    Predicted z-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
MASKBITS                   int16                Bitwise mask from the imaging indicating potential issue or blending
SERSIC                     float32              Power-law index for the Sersic profile model (MORPHTYPE=”SER”)
SHAPE_R                    float32 arcsec       Half-light radius of galaxy model (&gt;0)
SHAPE_E1                   float32              Ellipticity component 1 of galaxy model for galaxy type MORPHTYPE
SHAPE_E2                   float32              Ellipticity component 2 of galaxy model for galaxy type MORPHTYPE
REF_ID                     int64                Tyc1*1,000,000+Tyc2*10+Tyc3 for Tycho-2; “sourceid” for Gaia DR2
REF_CAT                    char[2]              Reference catalog source for star: “T2” for Tycho-2, “G2” for Gaia DR2, “L2” for the SGA, empty otherwise
GAIA_PHOT_G_MEAN_MAG       float32 mag          Gaia G band magnitude
GAIA_PHOT_BP_MEAN_MAG      float32 mag          Gaia BP band magnitude
GAIA_PHOT_RP_MEAN_MAG      float32 mag          Gaia RP band magnitude
PARALLAX                   float32 mas          Reference catalog parallax
PHOTSYS                    char[1]              &#x27;N&#x27; for the MzLS/BASS photometric system, &#x27;S&#x27; for DECaLS
PRIORITY_INIT              int64                Target initial priority from target selection bitmasks and OBSCONDITIONS
NUMOBS_INIT                int64                Initial number of observations for target calculated across target selection bitmasks and OBSCONDITIONS
SV1_DESI_TARGET [1]_       int64                DESI (dark time program) target selection bitmask for SV1
SV1_BGS_TARGET [1]_        int64                BGS (bright time program) target selection bitmask for SV1
SV1_MWS_TARGET [1]_        int64                MWS (bright time program) target selection bitmask for SV1
SV1_SCND_TARGET [1]_       int64                Secondary target selection bitmask for SV1
DESI_TARGET                int64                DESI (dark time program) target selection bitmask
BGS_TARGET                 int64                BGS (Bright Galaxy Survey) target selection bitmask
MWS_TARGET                 int64                Milky Way Survey targeting bits
SCND_TARGET [1]_           int64                Target selection bitmask for secondary programs
PLATE_RA                   float64 deg          Right Ascension to be used by PlateMaker
PLATE_DEC                  float64 deg          Declination to be used by PlateMaker
TILEID                     int32                Unique DESI tile ID
COADD_NUMEXP               int16                Number of exposures in coadd
COADD_EXPTIME              float32 s            Summed exposure time for coadd
COADD_NUMNIGHT             int16                Number of nights in coadd
COADD_NUMTILE              int16                Number of tiles in coadd
MEAN_DELTA_X               float32 mm           Mean (over exposures) fiber difference requested - actual CS5 X location on focal plane
RMS_DELTA_X                float32 mm           RMS (over exposures) of the fiber difference between measured and requested CS5 X location on focal plane
MEAN_DELTA_Y               float32 mm           Mean (over exposures) fiber difference requested - actual CS5 Y location on focal plane
RMS_DELTA_Y                float32 mm           RMS (over exposures) of the fiber difference between measured and requested CS5 Y location on focal plane
MEAN_FIBER_RA              float64 deg          Mean (over exposures) RA of actual fiber position
STD_FIBER_RA               float32 arcsec       Standard deviation (over exposures) of RA of actual fiber position
MEAN_FIBER_DEC             float64 deg          Mean (over exposures) DEC of actual fiber position
STD_FIBER_DEC              float32 arcsec       Standard deviation (over exposures) of DEC of actual fiber position
MEAN_PSF_TO_FIBER_SPECFLUX float32              Mean of input exposures fraction of light from point-like source captured by 1.5 arcsec diameter fiber given atmospheric seeing
MEAN_FIBER_X               float32
MEAN_FIBER_Y               float32
========================== ======= ============ ===============================================================================================================================

.. [1] Optional

HDU3
----

EXTNAME = EXP_FIBERMAP

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =====================
    KEY    Example Value Type Comment
    ====== ============= ==== =====================
    NAXIS1 162           int  length of dimension 1
    NAXIS2 500           int  length of dimension 2
    ====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

===================== ======= ======== =======================================================================================================
Name                  Type    Units    Description
===================== ======= ======== =======================================================================================================
TARGETID              int64            Unique DESI target ID
PRIORITY              int32            Target current priority
SUBPRIORITY           float64          Random subpriority [0-1) to break assignment ties
NIGHT                 int32
EXPID                 int32            DESI Exposure ID number
MJD                   float64          Modified Julian Date when shutter was opened for this exposure
TILEID                int32            Unique DESI tile ID
EXPTIME               float64 s        Length of time shutter was open
PETAL_LOC             int16            Petal location [0-9]
DEVICE_LOC            int32            Device location on focal plane [0-523]
LOCATION              int64            Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBER                 int32
FIBERSTATUS           int32            Fiber status mask. 0=good
FIBERASSIGN_X         float32 mm       Fiberassign expected CS5 X location on focal plane
FIBERASSIGN_Y         float32 mm       Fiberassign expected CS5 Y location on focal plane
LAMBDA_REF            float32 Angstrom Requested wavelength at which targets should be centered on fibers
PLATE_RA              float64 deg      Right Ascension to be used by PlateMaker
PLATE_DEC             float64 deg      Declination to be used by PlateMaker
NUM_ITER              int64            Number of positioner iterations
FIBER_X               float64 mm       CS5 X location requested by PlateMaker
FIBER_Y               float64 mm       CS5 Y location requested by PlateMaker
DELTA_X               float64 mm       CS5 X requested minus actual position
DELTA_Y               float64 mm       CS5 Y requested minus actual position
FIBER_RA              float64 deg      RA of actual fiber position
FIBER_DEC             float64 deg      DEC of actual fiber position
PSF_TO_FIBER_SPECFLUX float64          fraction of light from point-like source captured by 1.5 arcsec diameter fiber given atmospheric seeing
===================== ======= ======== =======================================================================================================

HDU4
----

EXTNAME = TSNR2

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =====================
    KEY    Example Value Type Comment
    ====== ============= ==== =====================
    NAXIS1 136           int  length of dimension 1
    NAXIS2 500           int  length of dimension 2
    ====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

================= ======= ===== ======================================
Name              Type    Units Description
================= ======= ===== ======================================
TARGETID          int64         Unique DESI target ID
TSNR2_GPBDARK_B   float32
TSNR2_ELG_B       float32       ELG B template (S/N)^2
TSNR2_GPBBRIGHT_B float32
TSNR2_LYA_B       float32       LYA B template (S/N)^2
TSNR2_BGS_B       float32       BGS B template (S/N)^2
TSNR2_GPBBACKUP_B float32
TSNR2_QSO_B       float32       QSO B template (S/N)^2
TSNR2_LRG_B       float32       LRG B template (S/N)^2
TSNR2_GPBDARK_R   float32
TSNR2_ELG_R       float32       ELG R template (S/N)^2
TSNR2_GPBBRIGHT_R float32
TSNR2_LYA_R       float32       LYA R template (S/N)^2
TSNR2_BGS_R       float32       BGS R template (S/N)^2
TSNR2_GPBBACKUP_R float32
TSNR2_QSO_R       float32       QSO R template (S/N)^2
TSNR2_LRG_R       float32       LRG R template (S/N)^2
TSNR2_GPBDARK_Z   float32
TSNR2_ELG_Z       float32       ELG Z template (S/N)^2
TSNR2_GPBBRIGHT_Z float32
TSNR2_LYA_Z       float32       LYA Z template (S/N)^2
TSNR2_BGS_Z       float32       BGS Z template (S/N)^2
TSNR2_GPBBACKUP_Z float32
TSNR2_QSO_Z       float32       QSO Z template (S/N)^2
TSNR2_LRG_Z       float32       LRG Z template (S/N)^2
TSNR2_GPBDARK     float32
TSNR2_ELG         float32       ELG template (S/N)^2 summed over B,R,Z
TSNR2_GPBBRIGHT   float32
TSNR2_LYA         float32       LYA template (S/N)^2 summed over B,R,Z
TSNR2_BGS         float32       BGS template (S/N)^2 summed over B,R,Z
TSNR2_GPBBACKUP   float32
TSNR2_QSO         float32       QSO template (S/N)^2 summed over B,R,Z
TSNR2_LRG         float32       LRG template (S/N)^2 summed over B,R,Z
================= ======= ===== ======================================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
