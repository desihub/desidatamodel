=================================
offline_matched_coadd_ccds_SURVEY
=================================

:Summary: The ``gfa_reduce`` pipeline performs an "offline" analysis of full-frame DESI Guide-Focus-Alignment (GFA) images which does not influence observing operations in real time but nevertheless may provide useful metrics related to observing conditions and GFA detector behavior. For instance, ``gfa_reduce`` provides independent measurements
    of observing conditions such as seeing and transparency.
:Naming Convention: ``offline_matched_coadd_ccds_{SURVEY}-thru_{NIGHT}.fits``, where
    ``{SURVEY}`` is *e.g.,* 'main' and ``{NIGHT}`` is the observation night in YYYYMMDD format.
:Regex: ``offline_matched_coadd_ccds_(main|SV1|SV2|SV3)-thru_[0-9]{8}\.fits``
:File Type: FITS, 250 MB

Contents
========

====== ======================= ======== ===============================================================================================
Number EXTNAME                 Type     Contents
====== ======================= ======== ===============================================================================================
HDU0_                          IMAGE    Empty HDU
HDU1_  CAMERA_SUMMARY          BINTABLE Summary results of individual guide cameras.
HDU2_  EXPOSURE_SUMMARY        BINTABLE Summary results accumulated per-exposure for all guide cameras.
HDU3_  EXPOSURE_SUMMARY_STRICT BINTABLE Summary results accumulated per-exposure for all guide cameras with stricter data quality cuts.
====== ======================= ======== ===============================================================================================


FITS Header Units
=================

HDU0
----

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = CAMERA_SUMMARY

``CAMERA_SUMMARY`` is a simple concatenation of all per-exposure ``gfa_reduce`` ``_ccds`` tables.
``CAMERA_SUMMARY`` has one row per exposure per guider camera, so the total number of rows is
roughly 6 times the number of exposures. There are more than 100 columns in the
``CAMERA_SUMMARY`` table, most of which shouldn't be relevant for the purpose of estimating
effective exposure times.


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

============================ =========== ============= ================================================================================
Name                         Type        Units         Description
============================ =========== ============= ================================================================================
MEDIAN                       float64     adu           Median of raw CCD image.
MEAN                         float64     adu           Mean of raw CCD image.
N_NON_FINITE                 int64       adu           Number of non-finite pixel values in raw CCD image.
MAX                          float64     adu           Max pixel value of raw CCD image.
MIN                          float64     adu           Min pixel value of raw CCD image.
SIG_ROBUST                   float64     adu           Robust standard deviation of raw CCD image.
SIG                          float64     adu           Standard deviation of raw CCD image.
MEDIAN_Q1                    float64     adu           Median of quadrant 1 (amp G)
MEAN_Q1                      float64     adu           Mean of quadrant 1 (amp G)
N_NON_FINITE_Q1              int64       adu           Number of non-finite pixel values in quadrant 1 (amp G)
MAX_Q1                       float64     adu           Maximum raw GFA image pixel value in ADU in quadrant 1 (amp G)
MIN_Q1                       float64     adu           Minimum raw GFA image pixel value in ADU in quadrant 1 (amp G)
SIG_ROBUST_Q1                float64     adu           Robust standard deviation of quadrant 1 (amp G)
SIG_Q1                       float64     adu           Standard deviation of quadrant 1 (amp G)
MEDIAN_Q2                    float64     adu           Median of quadrant 2 (amp H)
MEAN_Q2                      float64     adu           Mean of quadrant 2 (amp H)
N_NON_FINITE_Q2              int64       adu           Number of non-finite pixel values in quadrant 2 (amp H)
MAX_Q2                       float64     adu           Maximum raw GFA image pixel value in ADU in quadrant 2 (amp H)
MIN_Q2                       float64     adu           Minimum raw GFA image pixel value in ADU in quadrant 2 (amp H)
SIG_ROBUST_Q2                float64     adu           Robust standard deviation of quadrant 2 (amp H)
SIG_Q2                       float64     adu           Standard deviation of quadrant 2 (amp H)
MEDIAN_Q3                    float64     adu           Median of quadrant 3 (amp E)
MEAN_Q3                      float64     adu           Mean of quadrant 3 (amp E)
N_NON_FINITE_Q3              int64       adu           Number of non-finite pixel values in quadrant 3 (amp E)
MAX_Q3                       float64     adu           Maximum raw GFA image pixel value in ADU in quadrant 3 (amp E)
MIN_Q3                       float64     adu           Minimum raw GFA image pixel value in ADU in quadrant 3 (amp E)
SIG_ROBUST_Q3                float64     adu           Robust standard deviation of quadrant 3 (amp E)
SIG_Q3                       float64     adu           Standard deviation of quadrant 3 (amp E)
MEDIAN_Q4                    float64     adu           Median of quadrant 4 (amp F)
MEAN_Q4                      float64     adu           Mean of quadrant 4 (amp F)
N_NON_FINITE_Q4              int64       adu           Number of non-finite pixel values in quadrant 4 (amp F)
MAX_Q4                       float64     adu           Maximum raw GFA image pixel value in ADU in quadrant 4 (amp F)
MIN_Q4                       float64     adu           Minimum raw GFA image pixel value in ADU in quadrant 4 (amp F)
SIG_ROBUST_Q4                float64     adu           Robust standard deviation of quadrant 4 (amp F)
SIG_Q4                       float64     adu           Standard deviation of quadrant 4 (amp F)
CAMERA                       char[6]                   Camera identifier. Passband and SPECGRPH ([brz][0-9]).
EXTNAME                      char[6]                   String guide camera name; one of GUIDE0, GUIDE2, GUIDE3, GUIDE5, GUIDE7, GUIDE8
CONTRAST                     float64                   Pattern-matching contrast for ``gfa_reduce`` astrometry; larger CONTRAST indicates a more robust astrometric solution
SKY_MAG_AB                   float64     mag arcsec^-2 GFA-measured sky brightness.
SKY_MAG_AB_SUBREGION         float64     mag arcsec^-2 Sky brightness in a subregion of the GFA image.
SKY_MAG_AB_PER_AMP           float32[4]  mag arcsec^-2 Per-amp GFA-measured sky brightness.
PETAL_LOC                    binary                    Petal location [0-9]
EXPID                        int64                     DESI Exposure ID number
MJD                          float64     d             Modified Julian Date when shutter was opened for this exposure
LST_DEG                      float64     deg           Local Sidereal Time in degrees
MOON_ILLUMINATION            float64                   Moon illumination fraction.
PROGRAM                      char[88]                  DESI program type - BRIGHT, DARK, BACKUP, OTHER
SKYRA                        float64     deg           Boresight RA from TCS.
SKYDEC                       float64     deg           Boresight DEC from TCS.
ZENITH_DIST_DEG              float64     deg           Boresight zenith distance.
DOMSHUTL                     char[8]                   Dome lower shutter status inherited from TCS.
DOMSHUTU                     char[8]                   Dome upper shutter status inherited from TCS.
PMCOVER                      char[8]                   Primary mirror cover status inherited from TCS.
MOONRA                       float64     deg           RA of the Moon at the relevant epoch.
MOONDEC                      float64     deg           Dec of the Moon at the relevant epoch.
MOON_ZD_DEG                  float64     deg           Moon angular distance from zenith.
T_C_FOR_DARK                 float64     deg           Temperature used for dark current calculation (degrees Celsius).
T_C_FOR_DARK_IS_GUESS        int64                     Flag for whether temperature for dark current was a guess due to lack of metadata.
TIME_S_FOR_DARK              float64                   Exposure time used for dark current calculation.
NIGHT                        int64                     Night of observation (YYYYMMDD) starting at local noon before observations start
FOCUS                        char[39]                  Hexapod focus settings inherited from TCS.
EXPTIME                      float64     s             Length of time shutter was open
CUBE_INDEX                   int64                     Integer frame counter within the guide cube; ``CUBE_INDEX`` increases with time within each guide cube; 0 for acquisition images; -1 for matched coadds
COADD_INDEX_START            int64                     Starting index of the coadd within the guider image cube sequence.
COADD_INDEX_END              int64                     Ending index (inclusive) of the coadd within the guider image cube sequence.
COADD_MJDOBS_MIN             float64     d             Minimum MJD of guider frames contributing to the coadd.
COADD_MJDOBS_MAX             float64     d             Maximum MJD of guider frames contributing to the coadd.
RACEN                        float64     deg           Central RA of the guider image.
DECCEN                       float64     deg           Central Dec of the guider image.
FNAME_RAW                    char[76]                  Raw file name for guider image cube.
GITREV                       char[7]                   Git version for gfa_reduce software.
FIBER_FRACFLUX               float64                   Fraction of flux in a DESI fiber for a point source.
FIBER_FRACFLUX_ELG           float64                   Fraction of flux in a DESI fiber for a fiducial ELG morphology.
FIBER_FRACFLUX_BGS           float64                   Fraction of flux in a DESI fiber for a fiducial BGS morphology.
N_SOURCES_FOR_PSF            int64                     Number of sources used for PSF model ; key observing conditions quantities rely on the PSF model, so at least 3 sources for PSF-making is desirable
APER_CORR_FAC                float64                   Correction factor to go from aperture to total light used for zeropoint determination.
XCENTROID_PSF                float64       pix         Diagnostic giving PSF postage stamp's x-axis centroid location to potentially flag ill-determined PSF models.
YCENTROID_PSF                float64       pix         Diagnostic giving PSF postage stamp's y-axis centroid location to potentially flag ill-determined PSF models.
PSF_FWHM_PIX                 float64       pix         PSF FWHM in pixels.
PSF_FWHM_ASEC                float64       asec        PSF FWHM in arcseconds.
PSF_CENTROID_CBOX            float64       pix         Centering box sidelength used for PSF centroid determination.
PSF_CENTROID_FAILED          int64                     Flag indicating whether PSF centroiding failed.
RADPROF_FWHM_ASEC            float64       asec        PSF FWHM in arcseconds determined from a fit to a 1-dimensional radial profile of the PSF.
PSF_CENTROIDING_FLAG         int64                     *Description needed.*
PSF_ASYMMETRY_RATIO          float32                   *Description needed.*
PSF_ASYMMETRY_NUMERATOR      float32                   *Description needed.*
PSF_ASYMMETRY_DENOMINATOR    float32                   *Description needed.*
PSF_TOTAL_FLUX               float32                   *Description needed.*
PROFILE_RADIUS_PIX           float32[26]               *Description needed.*
PSF_RADIAL_PROFILE           float32[26]               *Description needed.*
MOUNTHA_HEADER               float64                   *Description needed.*
MOUNTDEC_HEADER              float64                   *Description needed.*
HA_DEG                       float64                   *Description needed.*
HA_DEG_PER_GFA               float64                   *Description needed.*
MOON_SEP_DEG                 float64                   *Description needed.*
ZD_DEG_PER_GFA               float64                   *Description needed.*
HEADER_AIRMASS               float64                   *Description needed.*
AIRMASS                      float64                   Average airmass during this exposure
AIRMASS_PER_GFA              float64                   *Description needed.*
ZP_ADU_PER_S                 float64                   *Description needed.*
N_STARS_FOR_ZP               int64                     *Description needed.*
TRANSPARENCY                 float64                   *Description needed.*
KTERM                        float32                   *Description needed.*
FRACFLUX_NOMINAL_POINTSOURCE float32                   *Description needed.*
FRACFLUX_NOMINAL_ELG         float32                   *Description needed.*
FRACFLUX_NOMINAL_BGS         float32                   *Description needed.*
DET_SN_THRESH                float64                   *Description needed.*
NPIX_BAD_TOTAL               int64                     Number of bad pixels in overscan/prescan ; NPIX_BAD_TOTAL of 10 or larger may indicate insufficient GFA "denoising" (bad A/D conversion)
NPIX_BAD_PER_AMP             int64[4]                  *Description needed.*
OVERSCAN_MEDIANS_ADU         float32[4]                *Description needed.*
PRESCAN_MEDIANS_ADU          float32[4]                *Description needed.*
FWHM_MAJOR_PIX               float64                   *Description needed.*
FWHM_MINOR_PIX               float64                   *Description needed.*
FWHM_PIX                     float64                   *Description needed.*
FWHM_ASEC                    float64                   *Description needed.*
N_SOURCES                    int64                     *Description needed.*
N_SOURCES_FOR_SHAPE          int64                     *Description needed.*
NAXIS                        int64[2]                  *Description needed.*
CD                           float64[4]                *Description needed.*
CDELT                        float64[2]                *Description needed.*
CRPIX                        float64[2]                *Description needed.*
CRVAL                        float64[2]                *Description needed.*
CTYPE                        char[16]                  *Description needed.*
LONGPOLE                     float64                   *Description needed.*
LATPOLE                      float64                   *Description needed.*
PV2                          float64[2]                *Description needed.*
FNAME_MASTER_DARK            char[112]                 File name of master dark used for dark current correction.
DO_FIT_DARK_SCALING          binary                    *Description needed.*
MASTER_DARK_EXPTIME          float64                   *Description needed.*
MASTER_DARK_GCCDTEMP         float64                   *Description needed.*
DARK_TEMP_SCALING_FACTOR     float64                   *Description needed.*
TOTAL_DARK_SCALING_FACTOR    float64                   *Description needed.*
DARK_RESCALE_FACTORS_PER_AMP float64[4]                *Description needed.*
DARK_RESCALE_FACTOR_BESTFIT  float64                   *Description needed.*
DARK_RESCALE_FACTOR_ADOPTED  float64                   *Description needed.*
APPLY_DARK_RESCALE_FACTOR    binary                    *Description needed.*
DARK_RESCALE_NCALLS          int64[4]                  *Description needed.*
DARK_RESCALE_CONVERGED       binary[4]                 *Description needed.*
REQ_MJD_MIN                  float64                   *Description needed.*
REQ_MJD_MAX                  float64                   *Description needed.*
N_PMGSTARS_ALL               int64                     *Description needed.*
N_PMGSTARS_RETAINED          int64                     *Description needed.*
FIBERFAC                     float64                   *Description needed.*
FIBERFAC_ELG                 float64                   *Description needed.*
FIBERFAC_BGS                 float64                   *Description needed.*
SPECTRO_EXPID                int64                     *Description needed.*
============================ =========== ============= ================================================================================

HDU2
----

EXTNAME = EXPOSURE_SUMMARY

This HDU is intended to be the same as ``EXPOSURE_SUMMARY_STRICT``, except that ``EXPOSURE_SUMMARY`` employs more permissive
quality cuts in the sense that no ``CONTRAST`` or ``N_SOURCES_FOR_PSF`` cuts are applied.
``EXPOSURE_SUMMARY`` still includes minimal quality cuts to remove cases of bad GFA readout such
as broken A/D conversion (lack of denoising) and zero-valued quadrants.
The idea behind ``EXPOSURE_SUMMARY`` is that it avoids cuts that could bias toward retaining
cameras with relatively good observing conditions (*e.g.*, ``N_SOURCES_FOR_PSF`` is
preferentially higher when the transparency is better and the sky brightness is lower).
We found that in practice such biases generally don't matter at any appreciable level,
so in general it's recommended to use ``EXPOSURE_SUMMARY_STRICT`` rather than ``EXPOSURE_SUMMARY``. The downside of
``EXPOSURE_SUMMARY`` is that in rare cases it may get very wrong values, especially for the
transparency when ``gfa_reduce`` astrometric pattern matching has catastrophically
failed (low CONTRAST parameter).

In some cases the lack of a ``CONTRAST`` cut in ``EXPOSURE_SUMMARY`` can be valuable.
In rare instances (such as very poor observing conditions) a science exposure
can be omitted from ``EXPOSURE_SUMMARY_STRICT`` due to failed ``gfa_reduce`` astrometry. But the
PMGSTARS forced photometry is still usable, since the PMGSTARS forced
photometry proceeds as usual even if ``gfa_reduce`` astrometry has failed.
For this reason, as of late April 2021, the spectroscopy pipeline's tSNR
afterburner uses ``EXPOSURE_SUMMARY`` rather than ``EXPOSURE_SUMMARY_STRICT`` (PR `#1245`_).

.. _`#1245`: ​https://github.com/desihub/desispec/pull/1245
.. _`DESI-5418`: https://desi.lbl.gov/DocDB/cgi-bin/private/ShowDocument?docid=5418

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

============================ ======== ============= ================================================================================
Name                         Type     Units         Description
============================ ======== ============= ================================================================================
EXPID                        int64                  DESI Exposure ID number
CUBE_INDEX                   int64                  Integer frame counter within the guide cube; ``CUBE_INDEX`` increases with time within each guide cube; 0 for acquisition images; -1 for matched coadds
NIGHT                        int64                  Night of observation (YYYYMMDD) starting at local noon before observations start
EXPTIME                      float64  s             Exposure time; usually 5 seconds for guider frames, 15 seconds for acquisition images, and 5 seconds for matched coadds (average rather than sum)
FNAME_RAW                    char[76]               Raw file name processed by ``gfa_reduce``
SKYRA                        float64  deg           Telescope bore sight RA taken from raw header metadata
SKYDEC                       float64  deg           Telescope bore sight Dec taken from raw header metadata
PROGRAM                      char[88]               DESI program type - BRIGHT, DARK, BACKUP, OTHER
MOON_ILLUMINATION            float64                Moon illumination fraction (0 to 1)
MOON_ZD_DEG                  float64  deg           Moon zenith distance in degrees
MOON_SEP_DEG                 float64  deg           Moon angular separation in degrees relative to the observation's sky location
KTERM                        float32                Assumed r band k-term value in magnitudes per airmass; from `DESI-5418`_
FRACFLUX_NOMINAL_POINTSOURCE float32                Point source nominal fraction of light in 1.52 arcsec diameter fiber-like aperture
FRACFLUX_NOMINAL_ELG         float32                Nominal fraction of light in 1.52 arcsec diameter fiber-like aperture for an ELG-like profile (r_half = 0.45 arcsec exponential)
FRACFLUX_NOMINAL_BGS         float32                Nominal fraction of light in 1.52 arcsec diameter fiber-like aperture for a BGS-like profile (r_half = 1.5 arcsec de Vaucouleurs)
MJD                          float64  d             Modified Julian Date when shutter was opened for this exposure
FWHM_ASEC                    float64  arcsec        FWHM in arcseconds based on fitting the PSF with a beta = 3.5 Moffat profile
TRANSPARENCY                 float64                Transparency in r band; based on comparison against PS1 r magnitudes; zeropoints from `DESI-5418`_; k-term given by ``KTERM`` column
SKY_MAG_AB                   float64  mag arcsec^-2 r band sky brightness measured from detrended GFA background levels; AB mag per square arcsec; zeropoints from `DESI-5418`_
FIBER_FRACFLUX               float64                Point source fraction of light in 1.52 arcsec diameter aperture ASSUMING THE APERTURE IS PERFECTLY ALIGNED WITH THE PSF CENTROID
FIBER_FRACFLUX_ELG           float64                Same as ``FIBER_FRACFLUX`` but for an ELG-like profile (r_half = 0.45 arcsec exponential) rather than a point source
FIBER_FRACFLUX_BGS           float64                Same as ``FIBER_FRACFLUX`` but for a BGS-like profile (r_half = 1.5 arcsec de Vaucouleurs) rather than a point source
AIRMASS                      float64                Average airmass during this exposure
RADPROF_FWHM_ASEC            float64  arcsec        PSF FWHM in arcsec measured directly from the PSF radial profile
FIBERFAC                     float64                PMGSTARS forced photometry amount of light in 1.52 arcsec diameter aperture normalized to nominal, assuming a point source profile
FIBERFAC_ELG                 float64                PMGSTARS forced photometry amount of light in 1.52 arcsec diameter aperture normalized to nominal, assuming an ELG-like profile (r_half = 0.45 arcsec exponential)
FIBERFAC_BGS                 float64                PMGSTARS forced photometry amount of light in 1.52 arcsec diameter aperture normalized to nominal, assuming a BGS-like profile (r_half = 1.5 arcsec de Vaucouleurs)
MINCONTRAST                  float64                Minimum ``gfa_reduce`` astrometric pattern matching contrast parameter among retained cameras
MAXCONTRAST                  float64                Maximum ``gfa_reduce`` astrometric pattern matching contrast parameter among retained cameras
============================ ======== ============= ================================================================================

HDU3
----

EXTNAME = EXPOSURE_SUMMARY_STRICT

This table aggregates information from ``CAMERA_SUMMARY`` on a per-exposure basis by taking
the median across individual guide cameras, subject to some quality cuts applied
to ``CAMERA_SUMMARY`` on a per-camera basis to remove potentially bad GFA measurements. These quality cuts are:

* remove rows of ``CAMERA_SUMMARY`` with ``min(MAX_Q1, MAX_Q2, MAX_Q3, MAX_Q4) = 0``. Having a maximum raw pixel value of zero in a quadrant indicates a major readout problem.
* remove rows of ``CAMERA_SUMMARY`` with ``NPIX_BAD_TOTAL >= 10``, since this is indicative of insufficient denoising (bad A/D conversion).
* remove rows of ``CAMERA_SUMMARY`` with ``N_SOURCES_FOR_PSF < 3``.
* remove rows of ``CAMERA_SUMMARY`` with ``CONTRAST < 2 (CONTRAST < 1.85)`` in the case of acquisition images (matched coadds). The goal is to remove instances where ``gfa_reduce`` astrometry pattern matching failed.

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

============================ ======== ============= ================================================================================
Name                         Type     Units         Description
============================ ======== ============= ================================================================================
EXPID                        int64                  DESI Exposure ID number
CUBE_INDEX                   int64                  Integer frame counter within the guide cube; ``CUBE_INDEX`` increases with time within each guide cube; 0 for acquisition images; -1 for matched coadds
NIGHT                        int64                  Night of observation (YYYYMMDD) starting at local noon before observations start
EXPTIME                      float64  s             Exposure time; usually 5 seconds for guider frames, 15 seconds for acquisition images, and 5 seconds for matched coadds (average rather than sum)
FNAME_RAW                    char[76]               Raw file name processed by ``gfa_reduce``
SKYRA                        float64  deg           Telescope bore sight RA taken from raw header metadata
SKYDEC                       float64  deg           Telescope bore sight Dec taken from raw header metadata
PROGRAM                      char[88]               DESI program type - BRIGHT, DARK, BACKUP, OTHER
MOON_ILLUMINATION            float64                Moon illumination fraction (0 to 1)
MOON_ZD_DEG                  float64  deg           Moon zenith distance in degrees
MOON_SEP_DEG                 float64  deg           Moon angular separation in degrees relative to the observation's sky location
KTERM                        float32                Assumed r band k-term value in magnitudes per airmass; from `DESI-5418`_
FRACFLUX_NOMINAL_POINTSOURCE float32                Point source nominal fraction of light in 1.52 arcsec diameter fiber-like aperture
FRACFLUX_NOMINAL_ELG         float32                Nominal fraction of light in 1.52 arcsec diameter fiber-like aperture for an ELG-like profile (r_half = 0.45 arcsec exponential)
FRACFLUX_NOMINAL_BGS         float32                Nominal fraction of light in 1.52 arcsec diameter fiber-like aperture for a BGS-like profile (r_half = 1.5 arcsec de Vaucouleurs)
MJD                          float64  d             Modified Julian Date when shutter was opened for this exposure
FWHM_ASEC                    float64  arcsec        FWHM in arcseconds based on fitting the PSF with a beta = 3.5 Moffat profile
TRANSPARENCY                 float64                Transparency in r band; based on comparison against PS1 r magnitudes; zeropoints from `DESI-5418`_; k-term given by ``KTERM`` column
SKY_MAG_AB                   float64  mag arcsec^-2 r band sky brightness measured from detrended GFA background levels; AB mag per square asec; zeropoints from `DESI-5418`_
FIBER_FRACFLUX               float64                Point source fraction of light in 1.52 arcsec diameter aperture ASSUMING THE APERTURE IS PERFECTLY ALIGNED WITH THE PSF CENTROID
FIBER_FRACFLUX_ELG           float64                Same as ``FIBER_FRACFLUX`` but for an ELG-like profile (r_half = 0.45 arcsec exponential) rather than a point source
FIBER_FRACFLUX_BGS           float64                Same as ``FIBER_FRACFLUX`` but for a BGS-like profile (r_half = 1.5 arcsec de Vaucouleurs) rather than a point source
AIRMASS                      float64                Average airmass during this exposure
RADPROF_FWHM_ASEC            float64  arcsec        PSF FWHM in arcsec measured directly from the PSF radial profile
FIBERFAC                     float64                PMGSTARS forced photometry amount of light in 1.52 arcsec diameter aperture normalized to nominal, assuming a point source profile
FIBERFAC_ELG                 float64                PMGSTARS forced photometry amount of light in 1.52 arcsec diameter aperture normalized to nominal, assuming an ELG-like profile (r_half = 0.45 arcsec exponential)
FIBERFAC_BGS                 float64                PMGSTARS forced photometry amount of light in 1.52 arcsec diameter aperture normalized to nominal, assuming a BGS-like profile (r_half = 1.5 arcsec de Vaucouleurs)
MINCONTRAST                  float64                Minimum ``gfa_reduce`` astrometric pattern matching contrast parameter among retained cameras
MAXCONTRAST                  float64                Maximum ``gfa_reduce`` astrometric pattern matching contrast parameter among retained cameras
============================ ======== ============= ================================================================================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
