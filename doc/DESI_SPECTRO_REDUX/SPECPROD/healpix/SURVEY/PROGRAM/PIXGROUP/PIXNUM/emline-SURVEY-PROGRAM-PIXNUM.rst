=================================
emline-SURVEY-PROGRAM-PIXNUM.fits
=================================

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``coadd-SURVEY-PROGRAM-PIXNUM.fits``, where ``SURVEY`` is
    *e.g.* ``main`` or ``sv1``, ``PROGRAM`` is *e.g.* ``bright or ``dark``
    and ``PIXNUM`` is the HEALPixel number.
:Regex: ``coadd-(cmx|main|sv1|sv2|sv3)-(backup|bright|dark|other)-[0-9]+\.fits``
:File Type: FITS, 123 KB

Contents
========

====== ========= ======== ===================
Number EXTNAME   Type     Contents
====== ========= ======== ===================
HDU0_            IMAGE    *Brief Description*
HDU1_  EMLINEFIT BINTABLE *Brief Description*
====== ========= ======== ===================


FITS Header Units
=================

HDU0
----

*Summarize the contents of this HDU.*

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = EMLINEFIT

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================================================================== ===== =======================
KEY      Example Value                                                                                        Type  Comment
======== ==================================================================================================== ===== =======================
NAXIS1   345                                                                                                  int   width of table in bytes
NAXIS2   305                                                                                                  int   number of rows in table
RRFN     /global/cfs/cdirs/desi/spectro/redux/fuji/healpix/sv2/bright/111/11167/redrock-sv2-bright-11167.fits str
COADDFN  /global/cfs/cdirs/desi/spectro/redux/fuji/healpix/sv2/bright/111/11167/coadd-sv2-bright-11167.fits   str
RFHW     40                                                                                                   int
MINRFHW  20                                                                                                   int
RFCONTW  200                                                                                                  int
RV       3.1                                                                                                  float
EMNAMES  OII,HDELTA,HGAMMA,HBETA,OIII,HALPHA                                                                  str
RFWAVE00 3727.092,3729.874                                                                                    str
RFWAVE01 4102.892                                                                                             str
RFWAVE02 4341.684                                                                                             str
RFWAVE03 4862.683                                                                                             str
RFWAVE04 4960.295,5008.239                                                                                    str
RFWAVE05 6564.613                                                                                             str
======== ==================================================================================================== ===== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

================= ======= ===== ===================
Name              Type    Units Description
================= ======= ===== ===================
TARGETID          int64         label for field   1
Z                 float64       label for field   2
ZWARN             int64         label for field   3
SPECTYPE          char[6]       label for field   4
DELTACHI2         float64       label for field   5
TARGET_RA         float64       label for field   6
TARGET_DEC        float64       label for field   7
OBJTYPE           char[3]       label for field   8
OII_FLUX          float32       label for field   9
OII_FLUX_IVAR     float32       label for field  10
OII_SIGMA         float32       label for field  11
OII_SIGMA_IVAR    float32       label for field  12
OII_CONT          float32       label for field  13
OII_CONT_IVAR     float32       label for field  14
OII_SHARE         float32       label for field  15
OII_SHARE_IVAR    float32       label for field  16
OII_EW            float32       label for field  17
OII_EW_IVAR       float32       label for field  18
OII_CHI2          float32       label for field  19
OII_NDOF          int32         label for field  20
HDELTA_FLUX       float32       label for field  21
HDELTA_FLUX_IVAR  float32       label for field  22
HDELTA_SIGMA      float32       label for field  23
HDELTA_SIGMA_IVAR float32       label for field  24
HDELTA_CONT       float32       label for field  25
HDELTA_CONT_IVAR  float32       label for field  26
HDELTA_SHARE      float32       label for field  27
HDELTA_SHARE_IVAR float32       label for field  28
HDELTA_EW         float32       label for field  29
HDELTA_EW_IVAR    float32       label for field  30
HDELTA_CHI2       float32       label for field  31
HDELTA_NDOF       int32         label for field  32
HGAMMA_FLUX       float32       label for field  33
HGAMMA_FLUX_IVAR  float32       label for field  34
HGAMMA_SIGMA      float32       label for field  35
HGAMMA_SIGMA_IVAR float32       label for field  36
HGAMMA_CONT       float32       label for field  37
HGAMMA_CONT_IVAR  float32       label for field  38
HGAMMA_SHARE      float32       label for field  39
HGAMMA_SHARE_IVAR float32       label for field  40
HGAMMA_EW         float32       label for field  41
HGAMMA_EW_IVAR    float32       label for field  42
HGAMMA_CHI2       float32       label for field  43
HGAMMA_NDOF       int32         label for field  44
HBETA_FLUX        float32       label for field  45
HBETA_FLUX_IVAR   float32       label for field  46
HBETA_SIGMA       float32       label for field  47
HBETA_SIGMA_IVAR  float32       label for field  48
HBETA_CONT        float32       label for field  49
HBETA_CONT_IVAR   float32       label for field  50
HBETA_SHARE       float32       label for field  51
HBETA_SHARE_IVAR  float32       label for field  52
HBETA_EW          float32       label for field  53
HBETA_EW_IVAR     float32       label for field  54
HBETA_CHI2        float32       label for field  55
HBETA_NDOF        int32         label for field  56
OIII_FLUX         float32       label for field  57
OIII_FLUX_IVAR    float32       label for field  58
OIII_SIGMA        float32       label for field  59
OIII_SIGMA_IVAR   float32       label for field  60
OIII_CONT         float32       label for field  61
OIII_CONT_IVAR    float32       label for field  62
OIII_SHARE        float32       label for field  63
OIII_SHARE_IVAR   float32       label for field  64
OIII_EW           float32       label for field  65
OIII_EW_IVAR      float32       label for field  66
OIII_CHI2         float32       label for field  67
OIII_NDOF         int32         label for field  68
HALPHA_FLUX       float32       label for field  69
HALPHA_FLUX_IVAR  float32       label for field  70
HALPHA_SIGMA      float32       label for field  71
HALPHA_SIGMA_IVAR float32       label for field  72
HALPHA_CONT       float32       label for field  73
HALPHA_CONT_IVAR  float32       label for field  74
HALPHA_SHARE      float32       label for field  75
HALPHA_SHARE_IVAR float32       label for field  76
HALPHA_EW         float32       label for field  77
HALPHA_EW_IVAR    float32       label for field  78
HALPHA_CHI2       float32       label for field  79
HALPHA_NDOF       int32         label for field  80
================= ======= ===== ===================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
