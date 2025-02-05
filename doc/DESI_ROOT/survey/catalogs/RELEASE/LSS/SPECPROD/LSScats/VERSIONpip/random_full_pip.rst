=====================
RANDOM full catalogs
=====================

:Summary: LSS catalogs containing information on all of the random targets identified as reachable by DESI fiberassign, for one of the input randoms. The files are split by target type, random file number, and whether of not vetos for angular positions and healpix map cuts have been applied
:Naming Convention: ``{TARGET}_{RANN}_full{VETO}.ran.fits``, where ``{TARGET}`` is the target type: ``QSO``, ``ELG``, ``ELG_LOPnotqso``, ``LRG``, for dark or ``BGS_ANY``, ``BGS_BRIGHT`` for bright. ``{RANN}`` is the number between 0 and 17 designating the given random file, and ``{VETO}`` is _noveto if vetos have not been applied, blank if vetos have been applied and _HPmapcut if both vetos and healpix map cuts have been applied.
:Regex: ``[a-zA-Z_]+\_[0-9]+\_full[a-z_]{0,7,9}.ran.fits``
:File Type: FITS, 5 GB 

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    Empty
HDU1_  LSS     BINTABLE Random data
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

Catalog of randoms

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =====================
    KEY    Example Value Type Comment
    ====== ============= ==== =====================
    NAXIS1 391           int  length of dimension 1
    NAXIS2 15297348      int  length of dimension 2
    DESIDR dr1           str
    ====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

========================== ========= ============ ===================================================================================================================================================================================================================================================
Name                       Type      Units        Description
========================== ========= ============ ===================================================================================================================================================================================================================================================
LOCATION                   int64                  Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBER                      int64                  Fiber ID on the CCDs [0-4999]
TARGETID                   int64                  Unique DESI target ID
RA                         float64   deg          Barycentric Right Ascension in ICRS
DEC                        float64   deg          Barycentric declination in ICRS
TILEID                     int64                  Unique DESI tile ID
PRIORITY                   int32                  Target current priority
TSNR2_ELG                  float32                ELG template (S/N)^2 summed over B,R,Z
TSNR2_LYA                  float32                LYA template (S/N)^2 summed over B,R,Z
TSNR2_BGS                  float32                BGS template (S/N)^2 summed over B,R,Z
TSNR2_QSO                  float32                QSO template (S/N)^2 summed over B,R,Z
TSNR2_LRG                  float32                LRG template (S/N)^2 summed over B,R,Z
TILELOCID                  int64                  Is 10000*TILEID+LOCATION
ZPOSSLOC                   logical                True/False whether the location could have been assigned to the given target class
GOODHARDLOC                logical                True/False whether the fiber had good hardware
GOODPRI                    logical                True/False whether the priority of what was assigned to the location was less or equals to the base priority of the given target class
NTILE                      int64                  Number of tiles target was available on
TILES                      char[36]               TILEIDs of those tile, in string form separated by -
TILELOCIDS                 char[111]              TILELOCIDs that the target was available for, separated -
NOBS_G                     int16                  Number of images for central pixel in g-band
NOBS_R                     int16                  Number of images for central pixel in r-band
NOBS_Z                     int16                  Number of images for central pixel in z-band
MASKBITS                   int16                  Bitwise mask from the imaging indicating potential issue or blending
PHOTSYS                    char[1]                N for the MzLS/BASS photometric system, S for DECaLS
HALPHA                     float32                Intensity of Halpha emission at FWHM of 6 minutes (from Finkbeiner - ApJS 146 2003 - 407)
HALPHA_ERROR               float32                Intensity error of Halpha emission at FWHM of 6 minutes (from Finkbeiner - ApJS 146 2003 - 407)
CALIB_G                    float32                g-band systematic magnitude calibration residuals constructed by comparing LS stars to stars from Pan-STARRS1 (details in Appendix A from DESI 2024 II paper)
CALIB_R                    float32                r-band systematic magnitude calibration residuals constructed by comparing LS stars to stars from Pan-STARRS1 (details in Appendix A from DESI 2024 II paper)
CALIB_Z                    float32                z-band systematic magnitude calibration residuals constructed by comparing LS stars to stars from Pan-STARRS1 (details in Appendix A from DESI 2024 II paper)
EBV_CHIANG_SFDcorr         float32                EBV dust reddening SFD correction (from Chiang - ApJ 958 2023 - 118)
EBV_MPF_Mean_FW15          float32                Mean EBV dust reddening generated from a combination of stellar reddening derived from PS1 and 2MASS photometry and Gaia EDR3 parallaxes with a FWHM of 15 minutes (more details in Mudur Park and Finkbeiner - ApJ 949 2023)
EBV_MPF_Mean_ZptCorr_FW15  float32                Zero point correction in EBV dust reddening generated from a combination of stellar reddening derived from PS1 and 2MASS photometry and Gaia EDR3 parallaxes with a FWHM of 15 minutes (more details in Mudur Park and Finkbeiner - ApJ 949 2023)
EBV_MPF_Var_FW15           float32                Variance in EBV dust reddening generated from a combination of stellar reddening derived from PS1 and 2MASS photometry and Gaia EDR3 parallaxes with a FWHM of 15 minutes (more details in Mudur Park and Finkbeiner - ApJ 949 2023)
EBV_MPF_VarCorr_FW15       float32                Uncertainty corrections in EBV dust reddening generated from a combination of stellar reddening derived from PS1 and 2MASS photometry and Gaia EDR3 parallaxes with a FWHM of 15 minutes (more details in Mudur Park and Finkbeiner - ApJ 949 2023)
EBV_MPF_Mean_FW6P1         float32                Mean EBV dust reddening generated from a combination of stellar reddening derived from PS1 and 2MASS photometry and Gaia EDR3 parallaxes with a FWHM of 6.1 minutes (more details in Mudur Park and Finkbeiner - ApJ 949 2023)
EBV_MPF_Mean_ZptCorr_FW6P1 float32                Zero point correction in EBV dust reddening generated from a combination of stellar reddening derived from PS1 and 2MASS photometry and Gaia EDR3 parallaxes with a FWHM of 6.1 minutes (more details in Mudur Park and Finkbeiner - ApJ 949 2023)
EBV_MPF_Var_FW6P1          float32                Variance in EBV dust reddening generated from a combination of stellar reddening derived from PS1 and 2MASS photometry and Gaia EDR3 parallaxes with a FWHM of 6.1 minutes (more details in Mudur Park and Finkbeiner - ApJ 949 2023)
EBV_MPF_VarCorr_FW6P1      float32                Uncertainty corrections in EBV dust reddening generated from a combination of stellar reddening derived from PS1 and 2MASS photometry and Gaia EDR3 parallaxes with a FWHM of 6.1 minutes (more details in Mudur Park and Finkbeiner - ApJ 949 2023)
EBV_SGF14                  float32                EBV dust reddening from Schlafly Green and Finkbeiner map from PanSTARRS1 (details in Appendix A from DESI 2024 II paper)
BETA_ML                    float32                Maximum value of the dust emissivity index posterior from Planck (Planck Collaboration - A and A 594 2016 - A10)
BETA_MEAN                  float32                Mean value of the dust emissivity index posterior from Planck (Planck Collaboration - A and A 594 2016 - A10)
BETA_RMS                   float32                Root mean square value of the dust emissivity index posterior from Planck (Planck Collaboration - A and A 594 2016 - A10)
HI                         float32                HI column density assembled by combining the Effelsberg-Bonn HI Survey and the third revision of the Galactic All-Sky Survey (from HI4PI Collaboration - A and A 594 2016 - A116)
KAPPA_PLANCK               float64                Map of lensing convergence from Planck where values are the mean-field-subtracted minimum-variance estimate from temperature and polarization (from Planck Collaboration - A and A 641 2020 - A8)
STARDENS                   float32                Density (deg-2) of stars in the position from Gaia limited to point-like sources in the range 12 less than G less than 17 calculated using the desitarget randoms.stellar_density function
PSFDEPTH_G                 float32   nanomaggy^-2 PSF-based depth in g-band
PSFDEPTH_R                 float32   nanomaggy^-2 PSF-based depth in r-band
PSFDEPTH_Z                 float32   nanomaggy^-2 PSF-based depth in z-band
GALDEPTH_G                 float32   nanomaggy^-2 Galaxy model-based depth in LS g-band
GALDEPTH_R                 float32   nanomaggy^-2 Galaxy model-based depth in LS r-band
GALDEPTH_Z                 float32   nanomaggy^-2 Galaxy model-based depth in LS z-band
PSFDEPTH_W1                float32   nanomaggy^-2 PSF-based depth in WISE W1
PSFDEPTH_W2                float32   nanomaggy^-2 PSF-based depth in WISE W2
PSFSIZE_G                  float32   arcsec       Median PSF size evaluated at the BRICK_PRIMARY objects in this brick in g-band
PSFSIZE_R                  float32   arcsec       Median PSF size evaluated at the BRICK_PRIMARY objects in this brick in r-band
PSFSIZE_Z                  float32   arcsec       Median PSF size evaluated at the BRICK_PRIMARY objects in this brick in z-band
EBV                        float32   mag          Galactic extinction E(B-V) reddening from SFD98
FRAC_TLOBS_TILES           float64                Fraction of targets with the same TILES value that contribute to FRACZ_TILELOCID
========================== ========= ============ ===================================================================================================================================================================================================================================================


Notes and Examples
==================

