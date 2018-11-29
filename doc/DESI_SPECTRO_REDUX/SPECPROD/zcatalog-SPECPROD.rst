=================
zcatalog-SPECPROD
=================

:Summary: This file concatenates all
    :doc:`zbest <./spectra-NSIDE/PIXGROUP/PIXNUM/zbest-NSIDE-PIXNUM>` files
    and then cross matches them with the input target catalog.
:Naming Convention: ``zcatalog-{SPECPROD}.fits``, where ``{SPECPROD}`` is the
    :envvar:`SPECPROD` name of the reduction run.
:Regex: ``zcatalog-[a-z0-9_-]+\.fits``
:File Type: FITS, 14 MB

Contents
========

====== ======== ======== ===========================================
Number EXTNAME  Type     Contents
====== ======== ======== ===========================================
HDU0_  PRIMARY  IMAGE    Empty
HDU1_  ZCATALOG BINTABLE Redshift catalog joined with target catalog
====== ======== ======== ===========================================


FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = ZCATALOG

The concatenated redshift data for all
:doc:`zbest <./spectra-NSIDE/PIXGROUP/PIXNUM/zbest-NSIDE-PIXNUM>` files,
cross matched with the original input target catalog.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============= ===== =================================
KEY      Example Value Type  Comment
======== ============= ===== =================================
NAXIS1   332           int   width of table in bytes
NAXIS2   44215         int   number of targets (rows) in table
RRVER    0.13.2        str   Redrock version
TEMNAM00 GALAXY        str
TEMVER00 2.6           float
TEMNAM01 QSO           str
TEMVER01 unknown       str
TEMNAM02 STAR:::A      str
TEMVER02 unknown       str
TEMNAM03 STAR:::B      str
TEMVER03 unknown       str
TEMNAM04 STAR:::CV     str
TEMVER04 unknown       str
TEMNAM05 STAR:::F      str
TEMVER05 unknown       str
TEMNAM06 STAR:::G      str
TEMVER06 unknown       str
TEMNAM07 STAR:::K      str
TEMVER07 unknown       str
TEMNAM08 STAR:::M      str
TEMVER08 unknown       str
TEMNAM09 STAR:::WD     str
TEMVER09 unknown       str
======== ============= ===== =================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

================================= =========== ===== ===================
Name                              Type        Units Description
================================= =========== ===== ===================
TARGETID                          int64             label for field   1
CHI2                              float64           label for field   2
COEFF                             float64[10]       label for field   3
Z                                 float64           label for field   4
ZERR                              float64           label for field   5
ZWARN                             int64             label for field   6
NPIXELS                           int64             label for field   7
SPECTYPE                          char[6]           label for field   8
SUBTYPE                           char[20]          label for field   9
NCOEFF                            int64             label for field  10
DELTACHI2                         float64           label for field  11
BRICKNAME                         char[8]           label for field  12
NUMEXP                            int32             label for field  13
NUMTILE                           int32             label for field  14
RELEASE                           int32             label for field  15
BRICKID                           int32             label for field  16
BRICK_OBJID                       int32             label for field  17
MORPHTYPE                         char[4]           label for field  18
RA                                float64           label for field  19
DEC                               float64           label for field  20
RA_IVAR                           float32           label for field  21
DEC_IVAR                          float32           label for field  22
FLUX_G                            float32           label for field  23
FLUX_R                            float32           label for field  24
FLUX_Z                            float32           label for field  25
FLUX_W1                           float32           label for field  26
FLUX_W2                           float32           label for field  27
FLUX_IVAR_G                       float32           label for field  28
FLUX_IVAR_R                       float32           label for field  29
FLUX_IVAR_Z                       float32           label for field  30
FLUX_IVAR_W1                      float32           label for field  31
FLUX_IVAR_W2                      float32           label for field  32
MW_TRANSMISSION_G                 float32           label for field  33
MW_TRANSMISSION_R                 float32           label for field  34
MW_TRANSMISSION_Z                 float32           label for field  35
MW_TRANSMISSION_W1                float32           label for field  36
MW_TRANSMISSION_W2                float32           label for field  37
NOBS_G                            int16             label for field  38
NOBS_R                            int16             label for field  39
NOBS_Z                            int16             label for field  40
FRACFLUX_G                        float32           label for field  41
FRACFLUX_R                        float32           label for field  42
FRACFLUX_Z                        float32           label for field  43
FRACMASKED_G                      float32           label for field  44
FRACMASKED_R                      float32           label for field  45
FRACMASKED_Z                      float32           label for field  46
FRACIN_G                          float32           label for field  47
FRACIN_R                          float32           label for field  48
FRACIN_Z                          float32           label for field  49
ALLMASK_G                         float32           label for field  50
ALLMASK_R                         float32           label for field  51
ALLMASK_Z                         float32           label for field  52
PSFDEPTH_G                        float32           label for field  53
PSFDEPTH_R                        float32           label for field  54
PSFDEPTH_Z                        float32           label for field  55
GALDEPTH_G                        float32           label for field  56
GALDEPTH_R                        float32           label for field  57
GALDEPTH_Z                        float32           label for field  58
FRACDEV                           float32           label for field  59
FRACDEV_IVAR                      float32           label for field  60
SHAPEDEV_R                        float32           label for field  61
SHAPEDEV_R_IVAR                   float32           label for field  62
SHAPEDEV_E1                       float32           label for field  63
SHAPEDEV_E1_IVAR                  float32           label for field  64
SHAPEDEV_E2                       float32           label for field  65
SHAPEDEV_E2_IVAR                  float32           label for field  66
SHAPEEXP_R                        float32           label for field  67
SHAPEEXP_R_IVAR                   float32           label for field  68
SHAPEEXP_E1                       float32           label for field  69
SHAPEEXP_E1_IVAR                  float32           label for field  70
SHAPEEXP_E2                       float32           label for field  71
SHAPEEXP_E2_IVAR                  float32           label for field  72
FIBERFLUX_G                       float32           label for field  73
FIBERFLUX_R                       float32           label for field  74
FIBERFLUX_Z                       float32           label for field  75
FIBERTOTFLUX_G                    float32           label for field  76
FIBERTOTFLUX_R                    float32           label for field  77
FIBERTOTFLUX_Z                    float32           label for field  78
REF_ID                            int64             label for field  79
GAIA_PHOT_G_MEAN_MAG              float32           label for field  80
GAIA_PHOT_G_MEAN_FLUX_OVER_ERROR  float32           label for field  81
GAIA_PHOT_BP_MEAN_MAG             float32           label for field  82
GAIA_PHOT_BP_MEAN_FLUX_OVER_ERROR float32           label for field  83
GAIA_PHOT_RP_MEAN_MAG             float32           label for field  84
GAIA_PHOT_RP_MEAN_FLUX_OVER_ERROR float32           label for field  85
GAIA_ASTROMETRIC_EXCESS_NOISE     float32           label for field  86
GAIA_DUPLICATED_SOURCE            logical           label for field  87
PARALLAX                          float32           label for field  88
PARALLAX_IVAR                     float32           label for field  89
PMRA                              float32           label for field  90
PMRA_IVAR                         float32           label for field  91
PMDEC                             float32           label for field  92
PMDEC_IVAR                        float32           label for field  93
BRIGHTSTARINBLOB                  logical           label for field  94
EBV                               float32           label for field  95
PHOTSYS                           char[1]           label for field  96
DESI_TARGET                       int64             label for field  97
BGS_TARGET                        int64             label for field  98
MWS_TARGET                        int64             label for field  99
PRIORITY                          int64             label for field 100
SUBPRIORITY                       float64           label for field 101
NUMOBS                            int64             label for field 102
HPXPIXEL                          int64             label for field 103
================================= =========== ===== ===================

Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
