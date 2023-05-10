========================
zpix-SURVEY-PROGRAM.fits
========================

:Summary: This file summarizes some set of files TBD.
:Naming Convention: ``ztile-SURVEY-PROGRAM.fits``, where ``SURVEY`` is
    *e.g.* ``main`` or ``sv1`` and ``PROGRAM`` is *e.g.* ``bright or ``dark``.
:Regex: ``zpix-(cmx|main|sv1|sv2|sv3|special)-(backup|bright|dark|other)\.fits``
:File Type: FITS, 296 MB

Contents
========

====== ============ ======== ===================
Number EXTNAME      Type     Contents
====== ============ ======== ===================
HDU0_               IMAGE    Empty
HDU1_  ZCATALOG     BINTABLE Redshift catalog joined with target catalog
HDU2_  EXP_FIBERMAP BINTABLE *Brief Description*
====== ============ ======== ===================


FITS Header Units
=================

HDU0
----

This HDU has no non-standard required keywords.

Empty HDU.

.. _zcatalog-zpix-hdu1:

HDU1
----

EXTNAME = ZCATALOG

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ============ ============= ==== =======================
    KEY          Example Value Type Comment
    ============ ============= ==== =======================
    NAXIS1       631           int  width of table in bytes
    NAXIS2       139728        int  number of rows in table
    LONGSTRN     OGIP 1.0      str
    RRVER        0.15.0        str  Redrock version
    TEMNAM00     GALAXY        str
    TEMVER00     2.6           str
    TEMNAM01     QSO           str
    TEMVER01     0.1           str
    TEMNAM02     STAR:::A      str
    TEMVER02     0.1           str
    TEMNAM03     STAR:::B      str
    TEMVER03     0.1           str
    TEMNAM04     STAR:::CV     str
    TEMVER04     0.1           str
    TEMNAM05     STAR:::F      str
    TEMVER05     0.1           str
    TEMNAM06     STAR:::G      str
    TEMVER06     0.1           str
    TEMNAM07     STAR:::K      str
    TEMVER07     0.1           str
    TEMNAM08     STAR:::M      str
    TEMVER08     0.1           str
    TEMNAM09     STAR:::WD     str
    TEMVER09     0.1           str
    SPGRP        healpix       str
    HPXNSIDE     64            int
    HPXNEST      True          str
    SURVEY [1]_  sv2           str
    PROGRAM [1]_ dark          str
    ============ ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

========================== =========== ===== ===================
Name                       Type        Units Description
========================== =========== ===== ===================
TARGETID                   int64             ID (unique to file? and the whole survey?)
SURVEY [1]_                char[7]
PROGRAM [1]_               char[6]
HEALPIX                    int32
SPGRPVAL                   int32
Z                          float64           label for field   4
ZERR                       float64           label for field   5
ZWARN                      int64             label for field   6
CHI2                       float64           label for field   2
COEFF                      float64[10]       label for field   3
NPIXELS                    int64             label for field   7
SPECTYPE                   char[6]           label for field   8
SUBTYPE                    char[20]          label for field   9
NCOEFF                     int64             label for field  10
DELTACHI2                  float64           label for field  11
COADD_FIBERSTATUS          int32             label for field  12
TARGET_RA                  float64           Barycentric Right Ascension in ICRS
TARGET_DEC                 float64           Barycentric Declination in ICRS
PMRA                       float32           Reference catalog proper motion in the RA direction
PMDEC                      float32           Reference catalog proper motion in the Dec direction
REF_EPOCH                  float32           Reference catalog reference epoch (*e.g.*, 2015.5 for Gaia_ DR2)
FA_TARGET                  int64             label for field  18
FA_TYPE                    binary            label for field  19
OBJTYPE                    char[3]           label for field  20
SUBPRIORITY                float64           Random subpriority [0-1] to break assignment ties
OBSCONDITIONS              int32             Flag the target to be observed in graytime.
RELEASE                    int16             Legacy Surveys (`LS`_) `Release`_
BRICKNAME                  char[8]           Brick name from tractor input
BRICKID                    int32             Brick ID from tractor input
BRICK_OBJID                int32             OBJID (unique to brick, but not to file)
MORPHTYPE                  char[4]           `Morphological Model`_ type
EBV                        float32           Galactic extinction E(B-V) reddening from SFD98_
FLUX_G                     float32           `LS`_ flux from tractor input (g)
FLUX_R                     float32           `LS`_ flux from tractor input (r)
FLUX_Z                     float32           `LS`_ flux from tractor input (z)
FLUX_W1                    float32           WISE flux in W1
FLUX_W2                    float32           WISE flux in W2
FLUX_IVAR_G                float32           Inverse Variance of FLUX_G
FLUX_IVAR_R                float32           Inverse Variance of FLUX_R
FLUX_IVAR_Z                float32           Inverse Variance of FLUX_Z
FLUX_IVAR_W1               float32           Inverse Variance of FLUX_W1
FLUX_IVAR_W2               float32           Inverse Variance of FLUX_W2
FIBERFLUX_G                float32           Predicted g-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERFLUX_R                float32           Predicted r-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERFLUX_Z                float32           Predicted z-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERTOTFLUX_G             float32           Predicted g-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
FIBERTOTFLUX_R             float32           Predicted r-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
FIBERTOTFLUX_Z             float32           Predicted z-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
MASKBITS                   int16             Bitwise mask indicating that an object touches a pixel in the ``coadd/*/*/*maskbits*`` maps, as cataloged on the `DR9 bitmasks page`_
SERSIC                     float32           Power-law index for the Sersic profile model (``type="SER"``)
SHAPE_R                    float32           Half-light radius of galaxy model for galaxy type ``type`` (>0)
SHAPE_E1                   float32           `Ellipticity component`_ 1 of galaxy model for galaxy type ``type``
SHAPE_E2                   float32           `Ellipticity component`_ 2 of galaxy model for galaxy type ``type``
REF_ID                     int64             Tyc1*1,000,000+Tyc2*10+Tyc3 for `Tycho-2`_; "sourceid" for `Gaia`_ DR2
REF_CAT                    char[2]           Reference catalog source for this star: "T2" for `Tycho-2`_, "G2" for `Gaia`_ DR2, "L3" for the SGA_, empty otherwise
GAIA_PHOT_G_MEAN_MAG       float32           `Gaia`_ G band magnitude
GAIA_PHOT_BP_MEAN_MAG      float32           `Gaia`_ BP band magnitude
GAIA_PHOT_RP_MEAN_MAG      float32           `Gaia`_ RP band magnitude
PARALLAX                   float32           Reference catalog parallax
PHOTSYS                    char[1]           'N' for the MzLS/BASS photometric system, 'S' for DECaLS
PRIORITY_INIT              int64             label for field  57
NUMOBS_INIT                int64             label for field  58
CMX_TARGET [1]_            int64             Target selection bitmask for commissioning
SV1_DESI_TARGET [1]_       int64             DESI (dark time program) target selection bitmask for SV1
SV1_BGS_TARGET [1]_        int64             BGS (bright time program) target selection bitmask for SV1
SV1_MWS_TARGET [1]_        int64             MWS (bright time program) target selection bitmask for SV1
SV1_SCND_TARGET [1]_       int64             Secondary target selection bitmask for SV1
SV2_DESI_TARGET [1]_       int64             DESI (dark time program) target selection bitmask for SV2
SV2_BGS_TARGET [1]_        int64             BGS (bright time program) target selection bitmask for SV2
SV2_MWS_TARGET [1]_        int64             MWS (bright time program) target selection bitmask for SV2
SV2_SCND_TARGET [1]_       int64             Secondary target selection bitmask for SV2
SV3_DESI_TARGET [1]_       int64             DESI (dark time program) target selection bitmask for SV3
SV3_BGS_TARGET [1]_        int64             BGS (bright time program) target selection bitmask for SV3
SV3_MWS_TARGET [1]_        int64             MWS (bright time program) target selection bitmask for SV3
SV3_SCND_TARGET [1]_       int64             Secondary target selection bitmask for SV3
DESI_TARGET                int64             DESI (dark time program) target selection bitmask
BGS_TARGET                 int64             BGS (bright time program) target selection bitmask
MWS_TARGET                 int64             MWS (bright time program) target selection bitmask
SCND_TARGET [1]_           int64             Secondary target selection bitmask
PLATE_RA                   float64           label for field  66
PLATE_DEC                  float64           label for field  67
COADD_NUMEXP               int16             label for field  68
COADD_EXPTIME              float32           label for field  69
COADD_NUMNIGHT             int16             label for field  70
COADD_NUMTILE              int16             label for field  71
MEAN_DELTA_X               float32           label for field  72
RMS_DELTA_X                float32           label for field  73
MEAN_DELTA_Y               float32           label for field  74
RMS_DELTA_Y                float32           label for field  75
MEAN_FIBER_RA              float64           label for field  76
STD_FIBER_RA               float32           label for field  77
MEAN_FIBER_DEC             float64           label for field  78
STD_FIBER_DEC              float32           label for field  79
MEAN_PSF_TO_FIBER_SPECFLUX float32           label for field  80
TSNR2_GPBDARK_B            float32           label for field  81
TSNR2_ELG_B                float32           label for field  82
TSNR2_GPBBRIGHT_B          float32           label for field  83
TSNR2_LYA_B                float32           label for field  84
TSNR2_BGS_B                float32           label for field  85
TSNR2_GPBBACKUP_B          float32           label for field  86
TSNR2_QSO_B                float32           label for field  87
TSNR2_LRG_B                float32           label for field  88
TSNR2_GPBDARK_R            float32           label for field  89
TSNR2_ELG_R                float32           label for field  90
TSNR2_GPBBRIGHT_R          float32           label for field  91
TSNR2_LYA_R                float32           label for field  92
TSNR2_BGS_R                float32           label for field  93
TSNR2_GPBBACKUP_R          float32           label for field  94
TSNR2_QSO_R                float32           label for field  95
TSNR2_LRG_R                float32           label for field  96
TSNR2_GPBDARK_Z            float32           label for field  97
TSNR2_ELG_Z                float32           label for field  98
TSNR2_GPBBRIGHT_Z          float32           label for field  99
TSNR2_LYA_Z                float32           label for field 100
TSNR2_BGS_Z                float32           label for field 101
TSNR2_GPBBACKUP_Z          float32           label for field 102
TSNR2_QSO_Z                float32           label for field 103
TSNR2_LRG_Z                float32           label for field 104
TSNR2_GPBDARK              float32           label for field 105
TSNR2_ELG                  float32           label for field 106
TSNR2_GPBBRIGHT            float32           label for field 107
TSNR2_LYA                  float32           label for field 108
TSNR2_BGS                  float32           label for field 109
TSNR2_GPBBACKUP            float32           label for field 110
TSNR2_QSO                  float32           label for field 111
TSNR2_LRG                  float32           label for field 112
SV_NSPEC [1]_              int32
SV_PRIMARY [1]_            logical
MAIN_NSPEC [1]_            int32
MAIN_PRIMARY [1]_          logical
ZCAT_NSPEC                 int16
ZCAT_PRIMARY               logical
========================== =========== ===== ===================

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

HDU2
----

EXTNAME = EXP_FIBERMAP

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =======================
    KEY    Example Value Type Comment
    ====== ============= ==== =======================
    NAXIS1 162           int  width of table in bytes
    NAXIS2 1374500       int  number of rows in table
    ====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

===================== ======= ===== ===================
Name                  Type    Units Description
===================== ======= ===== ===================
TARGETID              int64         label for field   1
PRIORITY              int32         label for field   2
SUBPRIORITY           float64       label for field   3
NIGHT                 int32         label for field   4
EXPID                 int32         label for field   5
MJD                   float64       label for field   6
TILEID                int32         label for field   7
EXPTIME               float64       label for field   8
PETAL_LOC             int16         label for field   9
DEVICE_LOC            int32         label for field  10
LOCATION              int64         label for field  11
FIBER                 int32         label for field  12
FIBERSTATUS           int32         label for field  13
FIBERASSIGN_X         float32       label for field  14
FIBERASSIGN_Y         float32       label for field  15
LAMBDA_REF            float32       label for field  16
PLATE_RA              float64       label for field  17
PLATE_DEC             float64       label for field  18
NUM_ITER              int64         label for field  19
FIBER_X               float64       label for field  20
FIBER_Y               float64       label for field  21
DELTA_X               float64       label for field  22
DELTA_Y               float64       label for field  23
FIBER_RA              float64       label for field  24
FIBER_DEC             float64       label for field  25
PSF_TO_FIBER_SPECFLUX float64       label for field  26
===================== ======= ===== ===================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
