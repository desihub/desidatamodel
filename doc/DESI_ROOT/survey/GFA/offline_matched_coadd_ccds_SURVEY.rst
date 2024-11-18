===============================
offline_matched_coadd_ccds_main
===============================

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``offline_matched_coadd_ccds_main-thru_20241117.fits``, where ... *Give a human readable
    description of the filename, e.g. ``blat-{EXPID}`` where ``{EXPID}``
    is the 8-digit exposure ID.*
:Regex: ``offline_matched_coadd_ccds_main-thru_20241117.fits`` *Give a regular expression for this filename.
    For example, a six-digit number would correspond to ``[0-9]{6}``.*
:File Type: FITS, 250 MB  *This section gives the type of the file
    and its approximate size.*

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    *Brief Description*
HDU1_          BINTABLE *Brief Description*
HDU2_          BINTABLE *Brief Description*
HDU3_          BINTABLE *Brief Description*
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

*Summarize the contents of this HDU.*

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =====================
    KEY    Example Value Type Comment
    ====== ============= ==== =====================
    NAXIS1 1749          int  length of dimension 1
    NAXIS2 140700        int  length of dimension 2
    ====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

============================ =========== ===== ================================================================================
Name                         Type        Units Description
============================ =========== ===== ================================================================================
MEDIAN                       float64
MEAN                         float64
N_NON_FINITE                 int64
MAX                          float64
MIN                          float64
SIG_ROBUST                   float64
SIG                          float64
MEDIAN_Q1                    float64
MEAN_Q1                      float64
N_NON_FINITE_Q1              int64
MAX_Q1                       float64
MIN_Q1                       float64
SIG_ROBUST_Q1                float64
SIG_Q1                       float64
MEDIAN_Q2                    float64
MEAN_Q2                      float64
N_NON_FINITE_Q2              int64
MAX_Q2                       float64
MIN_Q2                       float64
SIG_ROBUST_Q2                float64
SIG_Q2                       float64
MEDIAN_Q3                    float64
MEAN_Q3                      float64
N_NON_FINITE_Q3              int64
MAX_Q3                       float64
MIN_Q3                       float64
SIG_ROBUST_Q3                float64
SIG_Q3                       float64
MEDIAN_Q4                    float64
MEAN_Q4                      float64
N_NON_FINITE_Q4              int64
MAX_Q4                       float64
MIN_Q4                       float64
SIG_ROBUST_Q4                float64
SIG_Q4                       float64
CAMERA                       char[6]           Camera identifier. Passband and SPECGRPH ([brz][0-9]).
EXTNAME                      char[6]
CONTRAST                     float64
SKY_MAG_AB                   float64
SKY_MAG_AB_SUBREGION         float64
SKY_MAG_AB_PER_AMP           float32[4]
PETAL_LOC                    binary            Petal location [0-9]
EXPID                        int64             DESI Exposure ID number
MJD                          float64     d     Modified Julian Date when shutter was opened for this exposure
LST_DEG                      float64
MOON_ILLUMINATION            float64
PROGRAM                      char[88]          DESI program type - BRIGHT, DARK, BACKUP, OTHER
SKYRA                        float64
SKYDEC                       float64
ZENITH_DIST_DEG              float64
DOMSHUTL                     char[8]
DOMSHUTU                     char[8]
PMCOVER                      char[8]
MOONRA                       float64
MOONDEC                      float64
MOON_ZD_DEG                  float64
T_C_FOR_DARK                 float64
T_C_FOR_DARK_IS_GUESS        int64
TIME_S_FOR_DARK              float64
NIGHT                        int64             Night of observation (YYYYMMDD) starting at local noon before observations start
FOCUS                        char[39]
EXPTIME                      float64     s     Length of time shutter was open
CUBE_INDEX                   int64
COADD_INDEX_START            int64
COADD_INDEX_END              int64
COADD_MJDOBS_MIN             float64
COADD_MJDOBS_MAX             float64
RACEN                        float64
DECCEN                       float64
FNAME_RAW                    char[76]
GITREV                       char[7]
FIBER_FRACFLUX               float64
FIBER_FRACFLUX_ELG           float64
FIBER_FRACFLUX_BGS           float64
N_SOURCES_FOR_PSF            int64
APER_CORR_FAC                float64
XCENTROID_PSF                float64
YCENTROID_PSF                float64
PSF_FWHM_PIX                 float64
PSF_FWHM_ASEC                float64
PSF_CENTROID_CBOX            float64
PSF_CENTROID_FAILED          int64
RADPROF_FWHM_ASEC            float64
PSF_CENTROIDING_FLAG         int64
PSF_ASYMMETRY_RATIO          float32
PSF_ASYMMETRY_NUMERATOR      float32
PSF_ASYMMETRY_DENOMINATOR    float32
PSF_TOTAL_FLUX               float32
PROFILE_RADIUS_PIX           float32[26]
PSF_RADIAL_PROFILE           float32[26]
MOUNTHA_HEADER               float64
MOUNTDEC_HEADER              float64
HA_DEG                       float64
HA_DEG_PER_GFA               float64
MOON_SEP_DEG                 float64
ZD_DEG_PER_GFA               float64
HEADER_AIRMASS               float64
AIRMASS                      float64           Average airmass during this exposure
AIRMASS_PER_GFA              float64
ZP_ADU_PER_S                 float64
N_STARS_FOR_ZP               int64
TRANSPARENCY                 float64
KTERM                        float32
FRACFLUX_NOMINAL_POINTSOURCE float32
FRACFLUX_NOMINAL_ELG         float32
FRACFLUX_NOMINAL_BGS         float32
DET_SN_THRESH                float64
NPIX_BAD_TOTAL               int64
NPIX_BAD_PER_AMP             int64[4]
OVERSCAN_MEDIANS_ADU         float32[4]
PRESCAN_MEDIANS_ADU          float32[4]
FWHM_MAJOR_PIX               float64
FWHM_MINOR_PIX               float64
FWHM_PIX                     float64
FWHM_ASEC                    float64
N_SOURCES                    int64
N_SOURCES_FOR_SHAPE          int64
NAXIS                        int64[2]
CD                           float64[4]
CDELT                        float64[2]
CRPIX                        float64[2]
CRVAL                        float64[2]
CTYPE                        char[16]
LONGPOLE                     float64
LATPOLE                      float64
PV2                          float64[2]
FNAME_MASTER_DARK            char[112]
DO_FIT_DARK_SCALING          binary
MASTER_DARK_EXPTIME          float64
MASTER_DARK_GCCDTEMP         float64
DARK_TEMP_SCALING_FACTOR     float64
TOTAL_DARK_SCALING_FACTOR    float64
DARK_RESCALE_FACTORS_PER_AMP float64[4]
DARK_RESCALE_FACTOR_BESTFIT  float64
DARK_RESCALE_FACTOR_ADOPTED  float64
APPLY_DARK_RESCALE_FACTOR    binary
DARK_RESCALE_NCALLS          int64[4]
DARK_RESCALE_CONVERGED       binary[4]
REQ_MJD_MIN                  float64
REQ_MJD_MAX                  float64
N_PMGSTARS_ALL               int64
N_PMGSTARS_RETAINED          int64
FIBERFAC                     float64
FIBERFAC_ELG                 float64
FIBERFAC_BGS                 float64
SPECTRO_EXPID                int64
============================ =========== ===== ================================================================================

HDU2
----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =====================
    KEY    Example Value Type Comment
    ====== ============= ==== =====================
    NAXIS1 364           int  length of dimension 1
    NAXIS2 23290         int  length of dimension 2
    ====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

============================ ======== ===== ================================================================================
Name                         Type     Units Description
============================ ======== ===== ================================================================================
EXPID                        int64          DESI Exposure ID number
CUBE_INDEX                   int64
NIGHT                        int64          Night of observation (YYYYMMDD) starting at local noon before observations start
EXPTIME                      float64  s     Length of time shutter was open
FNAME_RAW                    char[76]
SKYRA                        float64
SKYDEC                       float64
PROGRAM                      char[88]       DESI program type - BRIGHT, DARK, BACKUP, OTHER
MOON_ILLUMINATION            float64
MOON_ZD_DEG                  float64
MOON_SEP_DEG                 float64
KTERM                        float32
FRACFLUX_NOMINAL_POINTSOURCE float32
FRACFLUX_NOMINAL_ELG         float32
FRACFLUX_NOMINAL_BGS         float32
MJD                          float64  d     Modified Julian Date when shutter was opened for this exposure
FWHM_ASEC                    float64
TRANSPARENCY                 float64
SKY_MAG_AB                   float64
FIBER_FRACFLUX               float64
FIBER_FRACFLUX_ELG           float64
FIBER_FRACFLUX_BGS           float64
AIRMASS                      float64        Average airmass during this exposure
RADPROF_FWHM_ASEC            float64
FIBERFAC                     float64
FIBERFAC_ELG                 float64
FIBERFAC_BGS                 float64
MINCONTRAST                  float64
MAXCONTRAST                  float64
============================ ======== ===== ================================================================================

HDU3
----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =====================
    KEY    Example Value Type Comment
    ====== ============= ==== =====================
    NAXIS1 364           int  length of dimension 1
    NAXIS2 23142         int  length of dimension 2
    ====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

============================ ======== ===== ================================================================================
Name                         Type     Units Description
============================ ======== ===== ================================================================================
EXPID                        int64          DESI Exposure ID number
CUBE_INDEX                   int64
NIGHT                        int64          Night of observation (YYYYMMDD) starting at local noon before observations start
EXPTIME                      float64  s     Length of time shutter was open
FNAME_RAW                    char[76]
SKYRA                        float64
SKYDEC                       float64
PROGRAM                      char[88]       DESI program type - BRIGHT, DARK, BACKUP, OTHER
MOON_ILLUMINATION            float64
MOON_ZD_DEG                  float64
MOON_SEP_DEG                 float64
KTERM                        float32
FRACFLUX_NOMINAL_POINTSOURCE float32
FRACFLUX_NOMINAL_ELG         float32
FRACFLUX_NOMINAL_BGS         float32
MJD                          float64  d     Modified Julian Date when shutter was opened for this exposure
FWHM_ASEC                    float64
TRANSPARENCY                 float64
SKY_MAG_AB                   float64
FIBER_FRACFLUX               float64
FIBER_FRACFLUX_ELG           float64
FIBER_FRACFLUX_BGS           float64
AIRMASS                      float64        Average airmass during this exposure
RADPROF_FWHM_ASEC            float64
FIBERFAC                     float64
FIBERFAC_ELG                 float64
FIBERFAC_BGS                 float64
MINCONTRAST                  float64
MAXCONTRAST                  float64
============================ ======== ===== ================================================================================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
