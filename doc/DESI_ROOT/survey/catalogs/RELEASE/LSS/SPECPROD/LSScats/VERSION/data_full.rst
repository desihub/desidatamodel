==================
DATA full catalogs
==================

:Summary: LSS catalogs containing information on all targets identified as reachable by DESI fiberassign, with one entry for each. The files are split by target type and whether of not vetos for angular positions and healpix maps have been applied
:Naming Convention: ``{TARGET}_full{VETO}.dat.fits``, where ``{TARGET}`` is the target type: ``QSO``, ``ELG``, ``ELG_LOPnotqso``, ``LRG``, for dark or ``BGS_ANY``, ``BGS_BRIGHT`` for bright. ``{VETO}`` is _noveto if vetos have not been applied, blank if vetos have been applied and _HPmapcut if both vetos and healpix map cuts have been applied. 
:Regex: ``[a-zA-Z_]+\_full[a-z_]{0,7,9}.dat.fits``
:File Type: FITS, 4 GB  (size varies considerably depending on target type)

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    Empty
HDU1_  LSS     BINTABLE Catalog data
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
    NAXIS1 846           int  width of table in bytes
    NAXIS2 5243196       int  number of rows in table
    DESIDR dr1           str
    ====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

========================== =========== ============ =======================================================================================================================================
Name                       Type        Units        Description
========================== =========== ============ =======================================================================================================================================
TARGETID                   int64                    Unique DESI target ID
MWS_TARGET                 int64                    Milky Way Survey targeting bits
SUBPRIORITY                float64                  Random subpriority [0-1) to break assignment ties
PRIORITY_INIT              int64                    Target initial priority from target selection bitmasks and OBSCONDITIONS
TARGET_STATE               char[30]                 Combination of target class and its current observational state
TIMESTAMP                  char[25]    s            UTC/ISO time at which the target state was updated
LOCATION                   int64                    Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
TILEID                     int64                    Unique DESI tile ID
TILELOCID                  int64                    Is 10000*TILEID+LOCATION
LASTNIGHT                  int32                    Final night of observation included in a series of coadds
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
FIBER                      int32                    Fiber ID on the CCDs [0-4999]
COADD_FIBERSTATUS          int32                    bitwise-AND of input FIBERSTATUS
FIBERASSIGN_X              float32     mm           Fiberassign expected CS5 X location on focal plane
FIBERASSIGN_Y              float32     mm           Fiberassign expected CS5 Y location on focal plane
PRIORITY                   int32                    Target current priority
COADD_NUMEXP               int16                    Number of exposures in coadd
COADD_EXPTIME              float32     s            Summed exposure time for coadd
COADD_NUMNIGHT             int16                    Number of nights in coadd
MEAN_DELTA_X               float32     mm           Mean (over exposures) fiber difference requested - actual CS5 X location on focal plane
RMS_DELTA_X                float32     mm           RMS (over exposures) of the fiber difference between measured and requested CS5 X location on focal plane
MEAN_DELTA_Y               float32     mm           Mean (over exposures) fiber difference requested - actual CS5 Y location on focal plane
RMS_DELTA_Y                float32     mm           RMS (over exposures) of the fiber difference between measured and requested CS5 Y location on focal plane
MEAN_PSF_TO_FIBER_SPECFLUX float32                  Mean of input exposures fraction of light from point-like source captured by 1.5 arcsec diameter fiber given atmospheric seeing
TSNR2_ELG_B                float32                  ELG B template (S/N)^2
TSNR2_LYA_B                float32                  LYA B template (S/N)^2
TSNR2_BGS_B                float32                  BGS B template (S/N)^2
TSNR2_QSO_B                float32                  QSO B template (S/N)^2
TSNR2_LRG_B                float32                  LRG B template (S/N)^2
TSNR2_ELG_R                float32                  ELG R template (S/N)^2
TSNR2_LYA_R                float32                  LYA R template (S/N)^2
TSNR2_BGS_R                float32                  BGS R template (S/N)^2
TSNR2_QSO_R                float32                  QSO R template (S/N)^2
TSNR2_LRG_R                float32                  LRG R template (S/N)^2
TSNR2_ELG_Z                float32                  ELG Z template (S/N)^2
TSNR2_LYA_Z                float32                  LYA Z template (S/N)^2
TSNR2_BGS_Z                float32                  BGS Z template (S/N)^2
TSNR2_QSO_Z                float32                  QSO Z template (S/N)^2
TSNR2_LRG_Z                float32                  LRG Z template (S/N)^2
TSNR2_ELG                  float32                  ELG template (S/N)^2 summed over B,R,Z
TSNR2_LYA                  float32                  LYA template (S/N)^2 summed over B,R,Z
TSNR2_BGS                  float32                  BGS template (S/N)^2 summed over B,R,Z
TSNR2_QSO                  float32                  QSO template (S/N)^2 summed over B,R,Z
TSNR2_LRG                  float32                  LRG template (S/N)^2 summed over B,R,Z
ZWARN_MTL                  int64                    The ZWARN from the zmtl file (contains extra bits)
Z_QN                       float64                  Redshift measured by QuasarNET using line with highest confidence
Z_QN_CONF                  float64                  Redshift confidence from QuasarNET
IS_QSO_QN                  int16                    Spectroscopic classification from QuasarNET (1 for a quasar)
PRIORITY_ASSIGNED          int32                    (only for data) PRIORITY of the target that was assigned to the given FIBER and TILEID (redundant with PRIORITY in the random catalogs)
GOODPRI                    logical                  True/False whether the priority of what was assigned to the location was &lt;= the base priority of the given target class
GOODHARDLOC                logical                  True/False whether the fiber had good hardware
LOCATION_ASSIGNED          logical                  True/False for assigned/unassigned for the target in question
TILELOCID_ASSIGNED         logical                  0/1 for unassigned/assigned for TILELOCID in question (it could have been assigned to a different target)
NTILE                      int64                    Number of tiles target was available on
TILES                      char[36]                 TILEIDs of those tile, in string form separated by &#x27;-&#x27;
TILELOCIDS                 char[111]                TILELOCIDs that the target was available for, separated by &#x27;-&#x27;
BRICKID                    int32                    Brick ID from tractor input
BRICKNAME                  char[8]                  Brick name from tractor input
MORPHTYPE                  char[4]                  Imaging Surveys morphological type from Tractor
RA                         float64     deg          Barycentric Right Ascension in ICRS
DEC                        float64     deg          Barycentric declination in ICRS
DCHISQ                     float32[5]               Difference in chi-squared between Tractor model fits
EBV                        float32     mag          Galactic extinction E(B-V) reddening from SFD98
FLUX_G                     float32     nanomaggy    Flux in the Legacy Survey g-band (AB)
FLUX_R                     float32     nanomaggy    Flux in the Legacy Survey r-band (AB)
FLUX_Z                     float32     nanomaggy    Flux in the Legacy Survey z-band (AB)
FLUX_IVAR_G                float32     nanomaggy^-2 Inverse variance of FLUX_G (AB)
FLUX_IVAR_R                float32     nanomaggy^-2 Inverse variance of FLUX_R (AB)
FLUX_IVAR_Z                float32     nanomaggy^-2 Inverse variance of FLUX_Z (AB)
MW_TRANSMISSION_G          float32                  Milky Way dust transmission in LS g-band
MW_TRANSMISSION_R          float32                  Milky Way dust transmission in LS r-band
MW_TRANSMISSION_Z          float32                  Milky Way dust transmission in LS z-band
NOBS_G                     int16                    Number of images for central pixel in g-band
NOBS_R                     int16                    Number of images for central pixel in r-band
NOBS_Z                     int16                    Number of images for central pixel in z-band
PSFDEPTH_G                 float32     nanomaggy^-2 PSF-based depth in g-band
PSFDEPTH_R                 float32     nanomaggy^-2 PSF-based depth in r-band
PSFDEPTH_Z                 float32     nanomaggy^-2 PSF-based depth in z-band
GALDEPTH_G                 float32     nanomaggy^-2 Galaxy model-based depth in LS g-band
GALDEPTH_R                 float32     nanomaggy^-2 Galaxy model-based depth in LS r-band
GALDEPTH_Z                 float32     nanomaggy^-2 Galaxy model-based depth in LS z-band
FLUX_W1                    float32     nanomaggy    WISE flux in W1 (AB)
FLUX_W2                    float32     nanomaggy    WISE flux in W2 (AB)
FLUX_IVAR_W1               float32     nanomaggy^-2 Inverse variance of FLUX_W1 (AB)
FLUX_IVAR_W2               float32     nanomaggy^-2 Inverse variance of FLUX_W2 (AB)
MW_TRANSMISSION_W1         float32                  Milky Way dust transmission in WISE W1
MW_TRANSMISSION_W2         float32                  Milky Way dust transmission in WISE W2
FIBERFLUX_G                float32     nanomaggy    Predicted g-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERFLUX_R                float32     nanomaggy    Predicted r-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERFLUX_Z                float32     nanomaggy    Predicted z-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERTOTFLUX_G             float32     nanomaggy    Predicted g-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
FIBERTOTFLUX_R             float32     nanomaggy    Predicted r-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
FIBERTOTFLUX_Z             float32     nanomaggy    Predicted z-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
WISEMASK_W1                binary                   Bitwise mask for WISE W1 data
WISEMASK_W2                binary                   Bitwise mask for WISE W2 data
MASKBITS                   int16                    Bitwise mask from the imaging indicating potential issue or blending
SHAPE_R                    float32     arcsec       Half-light radius of galaxy model (&gt;0)
PHOTSYS                    char[1]                  &#x27;N&#x27; for the MzLS/BASS photometric system, &#x27;S&#x27; for DECaLS
DESI_TARGET                int64                    DESI (dark time program) target selection bitmask
BGS_TARGET                 int64                    BGS (Bright Galaxy Survey) target selection bitmask
COMP_TILE                  float64                  Assignment completeness for all targets of this type with the same value for TILES
FRACZ_TILELOCID            float64                  The fraction of targets of this type at this TILELOCID that received an observation (after forcing each target to a unique TILELOCID)
lrg_mask [1]_              binary                   Imaging mask bits relevant to LRG targets
WEIGHT_ZFAIL               float64                  Should be all 1 at this point for main survey
mod_success_rate           float64                  Expected spectroscopic success rate given the target and observation properties
========================== =========== ============ =======================================================================================================================================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
