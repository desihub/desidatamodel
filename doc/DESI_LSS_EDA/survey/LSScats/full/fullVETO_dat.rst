============================================
The "full" LSS catalogs for data
============================================

:Summary: LSS catalogs containing information on all targets identified as reachable by DESI fiberassign, with one entry for each. The files are split by target type and whether of not vetos for angular positions have been applied.
:Naming Convention: ``{TARGET}_full{VETO}.dat.fits``, where ``{TARGET}`` is the target type and ``{VETO}`` is _noveto if vetos have not been applied and blank otherwise.
:Regex: For example, ``BGS_BRIGHT_full_noveto.dat.fits`` is the file for BGS_BRIGHT targets before any vetos have been applied.
    
:File Type: FITS, 1 GB  (size varies considerably depending on target type)

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    Empty HDU
HDU1_  LSS     BINTABLE Catalog
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = LSS

Catalog data for the given target type; one entry per unique TARGETID

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =======================
    KEY    Example Value Type Comment
    ====== ============= ==== =======================
    NAXIS1 712           int  width of table in bytes
    NAXIS2 1781907       int  number of rows in table
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
Z_not4clus                 float64           Redshift measured by Redrock, using only the data from the single TILEID
ZERR                       float64           Redshift error from Redrock, using only the data from the single TILEID
ZWARN                      int64             Redshift warning bitmask measured by Redrock, using only the data from the single TILEID
CHI2                       float64           Best fit :math:`\chi^2`, using only the data from the single TILEID
COEFF                      float64[10]       Redrock template coefficients, using only the data from the single TILEID
NPIXELS                    int64
SPECTYPE                   char[6]           Spectype from redrock file, using only the data from the single TILEID
SUBTYPE                    char[20]          Spectral subtype, using only the data from the single TILEID
NCOEFF                     int64
DELTACHI2                  float64           Delta-chi-squared for template fit from Redrock, using only the data from the single TILEID
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
TSNR2_ELG                  float32           ELG template (S/N)^2 summed over B,R,Z, using only the data from the single TILEID
TSNR2_LYA                  float32           LYA template (S/N)^2 summed over B,R,Z, using only the data from the single TILEID
TSNR2_BGS                  float32           BGS template (S/N)^2 summed over B,R,Z, using only the data from the single TILEID
TSNR2_QSO                  float32           QSO template (S/N)^2 summed over B,R,Z, using only the data from the single TILEID
TSNR2_LRG                  float32           LRG template (S/N)^2 summed over B,R,Z, using only the data from the single TILEID
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
DESI_TARGET                int64             Main survey targeting bits
BGS_TARGET                 int64             Bright Galaxy Survey targeting bits
COMP_TILE                  float64           Assignment completeness for all targets of this type with the same value for TILES
FRACZ_TILELOCID            float64           The fraction of targets of this type at this TILELOCID that received an observation (after forcing each target to a unique TILELOCID)
Z_HP                       float64           Redshift measured by Redrock; using spectra coadded across all TILEIDs
DELTACHI2_HP               float64           Delta-chi-squared for template fit from Redrock, using spectra coadded across all TILEIDs
TSNR2_ELG_HP               float32           ELG template (S/N)^2 summed over B,R,Z, using spectra coadded across all TILEIDs
TSNR2_BGS_HP               float32           BGS template (S/N)^2 summed over B,R,Z, using spectra coadded across all TILEIDs
TSNR2_QSO_HP               float32           QSO template (S/N)^2 summed over B,R,Z, using spectra coadded across all TILEIDs
TSNR2_LRG_HP               float32           LRG template (S/N)^2 summed over B,R,Z, using spectra coadded across all TILEIDs
rosette_number             float64           Number identification for the targeting region (one of 20 `rosettes`)
rosette_r                  float64           Angular distance from rosette center in degrees
BITWEIGHTS                 int64[2]          Bit array denoting which of the 128 realizations the target was assigned in
PROB_OBS                   float64           Probability of being observed, given `BITWEIGHTS`
elg_mask [1]_              binary            Imaging mask bits relevant to ELG targets; only in ELG files
OII_FLUX [1]_              float32           Fitted flux for the [OII] doublet; only in ELG files
OII_FLUX_IVAR [1]_         float32           Inverse variance of the fitted flux for the [OII] doublet; only in ELG files
o2c [1]_                   float64           The criteria for assessing strength of OII emission for ELG observations; only in ELG files
lrg_mask [1]_              binary            Imaging mask bits relevant to LRG targets; only in LRG files
Z_RR [1]_                  float64           Redshift collected from redrock file; only in QSO files
ZERR_QF [1]_               float64
TSNR2_LYA_QF [1]_          float32
TSNR2_QSO_QF [1]_          float32
Z_QN_QF [1]_               float32
QSO_MASKBITS [1]_          int32
========================== =========== ===== =====================================================================================================================================

.. [1] Optional

Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
