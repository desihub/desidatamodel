===============
BGS_BRIGHT_full
===============

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``BGS_BRIGHT_full.dat.fits``, where ... *Give a human readable
    description of the filename, e.g. ``blat-{EXPID}`` where ``{EXPID}``
    is the 8-digit exposure ID.*
:Regex: ``BGS_BRIGHT_full.dat.fits`` *Give a regular expression for this filename.
    For example, a six-digit number would correspond to ``[0-9]{6}``.*
:File Type: FITS, 1 GB  *This section gives the type of the file
    and its approximate size.*

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    *Brief Description*
HDU1_  LSS     BINTABLE *Brief Description*
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

EXTNAME = LSS

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =======================
    KEY    Example Value Type Comment
    ====== ============= ==== =======================
    NAXIS1 712           int  width of table in bytes
    NAXIS2 1536070       int  number of rows in table
    ====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

========================== =========== ===== =====================================================================================================================================
Name                       Type        Units Description
========================== =========== ===== =====================================================================================================================================
TARGETID                   int64             Unique DESI target ID
MWS_TARGET                 int64             Milky Way Survey targeting bits
SUBPRIORITY                float64           Random subpriority [0-1] to break assignment ties
PRIORITY_INIT              int64             Target initial priority from target selection bitmasks and OBSCONDITIONS
TARGET_STATE               char[30]          Combination of target class and its current observational state
TIMESTAMP                  char[25]          UTC/ISO time at which the target state was updated
PRIORITY                   int64             Target current priority
FIBER                      int32             Fiber ID on the CCDs [0-4999]
LOCATION                   int64             Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
TILEID                     int64             Unique DESI tile ID
TILELOCID                  int64             Is 10000*TILEID+LOCATION
Z_not4clus                 float64           Redshift name changed after vetos are applied
ZERR                       float64           Redshift error from redrock
ZWARN                      int64             Redshift warning bitmask measured by Redrock
CHI2                       float64           Best fit :math:`\chi^2`
COEFF                      float64[10]       Redrock template coefficients
NPIXELS                    int64
SPECTYPE                   char[6]           Spectype from redrock file
SUBTYPE                    char[20]          Spectral subtype
NCOEFF                     int64
DELTACHI2                  float64           Delta-chi-squared for template fit from Redrock
COADD_FIBERSTATUS          int32
FIBERASSIGN_X              float32           Expected CS5 X location on focal plane
FIBERASSIGN_Y              float32           Expected CS5 Y location on focal plane
COADD_NUMEXP               int16
COADD_EXPTIME              float32
COADD_NUMNIGHT             int16
MEAN_DELTA_X               float32           Mean (over exposures) fiber difference between measured and requested CS5 X location on focal plane
RMS_DELTA_X                float32           RMS (over exposures) of the fiber difference between measured and requested CS5 X location on focal plane
MEAN_DELTA_Y               float32           Mean (over exposures) fiber CS5 Y location on focal plane
RMS_DELTA_Y                float32           RMS (over exposures) of the fiber difference between measured and requested CS5 Y location on focal plane
MEAN_PSF_TO_FIBER_SPECFLUX float32
TSNR2_ELG_B                float32           ELG B template (S/N)^2
TSNR2_LYA_B                float32           LYA B template (S/N)^2
TSNR2_BGS_B                float32           BGS B template (S/N)^2
TSNR2_QSO_B                float32           QSO B template (S/N)^2
TSNR2_LRG_B                float32           LRG B template (S/N)^2
TSNR2_ELG_R                float32           ELG R template (S/N)^2
TSNR2_LYA_R                float32           LYA R template (S/N)^2
TSNR2_BGS_R                float32           BGS R template (S/N)^2
TSNR2_QSO_R                float32           QSO R template (S/N)^2
TSNR2_LRG_R                float32           LRG R template (S/N)^2
TSNR2_ELG_Z                float32           ELG Z template (S/N)^2
TSNR2_LYA_Z                float32           LYA Z template (S/N)^2
TSNR2_BGS_Z                float32           BGS Z template (S/N)^2
TSNR2_QSO_Z                float32           QSO Z template (S/N)^2
TSNR2_LRG_Z                float32           LRG Z template (S/N)^2
TSNR2_ELG                  float32           ELG template (S/N)^2 summed over B,R,Z
TSNR2_LYA                  float32           LYA template (S/N)^2 summed over B,R,Z
TSNR2_BGS                  float32           BGS template (S/N)^2 summed over B,R,Z
TSNR2_QSO                  float32           QSO template (S/N)^2 summed over B,R,Z
TSNR2_LRG                  float32           LRG template (S/N)^2 summed over B,R,Z
ZWARN_MTL                  int64             The ZWARN from the zmtl file (contains extra bits)
Z_QN                       float64           Redshift measured by QuasarNET
Z_QN_CONF                  float64           Redshift confidence from QuasarNET
IS_QSO_QN                  int16             Spectroscopic classification from QuasarNET (1 for a quasar)
GOODHARDLOC                logical           True/False whether the fiber had good hardware
NTILE                      int64             Number of tiles target was available on
TILES                      char[11]          TILEIDs of those tile, in string form separated by -
TILELOCIDS                 char[39]          TILELOCIDs that the target was available for, separated by -
LOCATION_ASSIGNED          logical           0/1 for unassigned/assigned for the target in question
TILELOCID_ASSIGNED         logical           0/1 for unassigned/assigned for TILELOCID in question (it could have been assigned to a different target)
GOODTSNR                   logical           True/False whether the TSNR_&lt;class&gt; value used was above the minimum threshold for the given target class
sort                       float64           Number constructed to sort the table prior to cutting to unique TARGETID
BRICKID                    int32             Brick ID from tractor input
BRICKNAME                  char[8]           Brick name from tractor input
MORPHTYPE                  char[4]           Imaging Surveys morphological type
RA                         float64           Right Ascension
DEC                        float64           Declination
DCHISQ                     float32[5]        Difference in chi-squared between model fits
EBV                        float32           Galactic extinction E(B-V) reddening from SFD98
FLUX_G                     float32           Flux in the Legacy Survey g-band (AB)
FLUX_R                     float32           Flux in the Legacy Survey r-band (AB)
FLUX_Z                     float32           Flux in the Legacy Survey z-band (AB)
FLUX_IVAR_G                float32           Inverse variance of FLUX_G (AB)
FLUX_IVAR_R                float32           Inverse variance of FLUX_R (AB)
FLUX_IVAR_Z                float32           Inverse variance of FLUX_Z (AB)
MW_TRANSMISSION_G          float32           Milky Way dust transmission in g-band
MW_TRANSMISSION_R          float32           Milky Way dust transmission in r-band
MW_TRANSMISSION_Z          float32           Milky Way dust transmission in z-band
NOBS_G                     int16             Number of images for central pixel in g-band
NOBS_R                     int16             Number of images for central pixel in r-band
NOBS_Z                     int16             Number of images for central pixel in z-band
PSFDEPTH_G                 float32           PSF-based depth in g-band
PSFDEPTH_R                 float32           PSF-based depth in r-band
PSFDEPTH_Z                 float32           PSF-based depth in z-band
GALDEPTH_G                 float32           Galaxy model-based depth in g-band
GALDEPTH_R                 float32           Galaxy model-based depth in r-band
GALDEPTH_Z                 float32           Galaxy model-based depth in z-band
FLUX_W1                    float32           WISE flux in W1 (AB)
FLUX_W2                    float32           WISE flux in W2 (AB)
FLUX_IVAR_W1               float32           Inverse variance of FLUX_W1 (AB)
FLUX_IVAR_W2               float32           Inverse variance of FLUX_W2 (AB)
MW_TRANSMISSION_W1         float32           Milky Way dust transmission in WISE W1
MW_TRANSMISSION_W2         float32           Milky Way dust transmission in WISE W2
FIBERFLUX_G                float32           Predicted g-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERFLUX_R                float32           Predicted r-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERFLUX_Z                float32           Predicted z-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERTOTFLUX_G             float32           Predicted g-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
FIBERTOTFLUX_R             float32           Predicted r-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
FIBERTOTFLUX_Z             float32           Predicted z-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
WISEMASK_W1                binary            Bitwise mask for WISE W1 data
WISEMASK_W2                binary            Bitwise mask for WISE W2 data
MASKBITS                   int16             Bitwise mask from the imaging indicating potential issue or blending
SHAPE_R                    float32           Half-light radius of galaxy model (&gt;0)
PHOTSYS                    char[1]           N for the MzLS/BASS photometric system, S for DECaLS
DESI_TARGET                int64             Dark survey + calibration targeting bits
BGS_TARGET                 int64             Bright Galaxy Survey targeting bits
COMP_TILE                  float64           Assignment completeness for all targets of this type with the same value for TILES
FRACZ_TILELOCID            float64           The fraction of targets of this type at this TILELOCID that received an observation (after forcing each target to a unique TILELOCID)
elg_mask_optional          binary            Imaging mask bits relevant to ELG targets
OII_FLUX_optional          float32           Fitted flux for the [OII] doublet
OII_FLUX_IVAR_optional     float32           Inverse variance of the fitted flux for the [OII] doublet
o2c_optional               float64           The criteria for assessing strength of OII emission for ELG observations
lrg_mask_optional          binary            Imaging mask bits relevant to LRG targets
Z_RR_optional              float64           Redshift collected from redrock file
ZERR_QF_optional           float64
TSNR2_LYA_QF_optional      float32
TSNR2_QSO_QF_optional      float32
Z_QN_QF_optional           float32
QSO_MASKBITS_optional      int32
========================== =========== ===== =====================================================================================================================================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
