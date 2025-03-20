======================================
mapprops_healpix_nested_nside256
======================================

:Summary: Observing conditions and other quantities used to correct for systematics in healpix format.
:Naming Convention: ``{TARGET}_mapprops_healpix_nested_nside256_{PHOTSYS}.fits``, where ``{TARGET}`` is the target type (LRG, ELG_LOPnotqso, QSO, BGS_ANY, BGS_BRIGHT...) and ``PHOTSYS`` is north or south (N or S)
:Regex: ``[A-Za-z_]+_mapprops_healpix_nested_nside256_[NS].fits``
:File Type: FITS, 99 MB

Contents
========

====== ========= ======== ===================
Number EXTNAME   Type     Contents
====== ========= ======== ===================
HDU0_            IMAGE    Empty
HDU1_  PIXWEIGHT BINTABLE Healpix map
====== ========= ======== ===================


FITS Header Units
=================

HDU0
----

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = PIXWEIGHT

Healpix maps of quantities that are potentially useful for systematic tests/regressions,
matched to the footprint of the DESI data and created as described in Appendix A of `DESI Collaboration et al. (2024)`_

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =======================
    KEY    Example Value Type Comment
    ====== ============= ==== =======================
    NAXIS1 132           int  width of table in bytes
    NAXIS2 786432        int  number of rows in table
    DESIDR dr1           str  DESI Data Release
    ====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

========================== ======= ============ ===================================================================================================================================================================================================================================================
Name                       Type    Units        Description
========================== ======= ============ ===================================================================================================================================================================================================================================================
EBV_CHIANG_SFDcorr         float32              EBV dust reddening SFD correction (from Chiang - ApJ 958 2023 - 118)
STARDENS                   float32              Density (deg-2) of stars in the position from Gaia limited to point-like sources in the range 12 less than G less than 17 calculated using the desitarget randoms.stellar_density function
HALPHA                     float32              Intensity of Halpha emission at FWHM of 6 minutes (from Finkbeiner - ApJS 146 2003 - 407)
HALPHA_ERROR               float32              Intensity error of Halpha emission at FWHM of 6 minutes (from Finkbeiner - ApJS 146 2003 - 407)
CALIB_G                    float32              g-band systematic magnitude calibration residuals constructed by comparing LS stars to stars from Pan-STARRS1 (details in Appendix A from DESI 2024 II paper)
CALIB_R                    float32              r-band systematic magnitude calibration residuals constructed by comparing LS stars to stars from Pan-STARRS1 (details in Appendix A from DESI 2024 II paper)
CALIB_Z                    float32              z-band systematic magnitude calibration residuals constructed by comparing LS stars to stars from Pan-STARRS1 (details in Appendix A from DESI 2024 II paper)
EBV_MPF_Mean_FW15          float32              Mean EBV dust reddening generated from a combination of stellar reddening derived from PS1 and 2MASS photometry and Gaia EDR3 parallaxes with a FWHM of 15 minutes (more details in Mudur Park and Finkbeiner - ApJ 949 2023)
EBV_MPF_Mean_ZptCorr_FW15  float32              Zero point correction in EBV dust reddening generated from a combination of stellar reddening derived from PS1 and 2MASS photometry and Gaia EDR3 parallaxes with a FWHM of 15 minutes (more details in Mudur Park and Finkbeiner - ApJ 949 2023)
EBV_MPF_Var_FW15           float32              Variance in EBV dust reddening generated from a combination of stellar reddening derived from PS1 and 2MASS photometry and Gaia EDR3 parallaxes with a FWHM of 15 minutes (more details in Mudur Park and Finkbeiner - ApJ 949 2023)
EBV_MPF_VarCorr_FW15       float32              Uncertainty corrections in EBV dust reddening generated from a combination of stellar reddening derived from PS1 and 2MASS photometry and Gaia EDR3 parallaxes with a FWHM of 15 minutes (more details in Mudur Park and Finkbeiner - ApJ 949 2023)
EBV_MPF_Mean_FW6P1         float32              Mean EBV dust reddening generated from a combination of stellar reddening derived from PS1 and 2MASS photometry and Gaia EDR3 parallaxes with a FWHM of 6.1 minutes (more details in Mudur Park and Finkbeiner - ApJ 949 2023)
EBV_MPF_Mean_ZptCorr_FW6P1 float32              Zero point correction in EBV dust reddening generated from a combination of stellar reddening derived from PS1 and 2MASS photometry and Gaia EDR3 parallaxes with a FWHM of 6.1 minutes (more details in Mudur Park and Finkbeiner - ApJ 949 2023)
EBV_MPF_Var_FW6P1          float32              Variance in EBV dust reddening generated from a combination of stellar reddening derived from PS1 and 2MASS photometry and Gaia EDR3 parallaxes with a FWHM of 6.1 minutes (more details in Mudur Park and Finkbeiner - ApJ 949 2023)
EBV_MPF_VarCorr_FW6P1      float32              Uncertainty corrections in EBV dust reddening generated from a combination of stellar reddening derived from PS1 and 2MASS photometry and Gaia EDR3 parallaxes with a FWHM of 6.1 minutes (more details in Mudur Park and Finkbeiner - ApJ 949 2023)
EBV_SGF14                  float32              EBV dust reddening from Schlafly Green and Finkbeiner map from PanSTARRS1 (details in Appendix A from DESI 2024 II paper)
BETA_ML                    float32              Maximum value of the dust emissivity index posterior from Planck (Planck Collaboration - A and 594 2016 - A10)
BETA_MEAN                  float32              Mean value of the dust emissivity index posterior from Planck (Planck Collaboration - A and A 594 2016 - A10)
BETA_RMS                   float32              Root mean square value of the dust emissivity index posterior from Planck (Planck Collaboration - A and A 594 2016 - A10)
HI                         float32              HI column density assembled by combining the Effelsberg-Bonn HI Survey and the third revision of the Galactic All-Sky Survey (from HI4PI Collaboration - A and A 594 016 - A116)
KAPPA_PLANCK               float32              Map of lensing convergence from Planck where values are the mean-field-subtracted minimum-variance estimate from temperature and polarization (from Planck Collaboration - A and A 641 2020 - A8)
EBV                        float32 mag          Galactic extinction E(B-V) reddening from SFD98
PSFDEPTH_G                 float32 nanomaggy^-2 PSF-based depth in g-band
PSFDEPTH_R                 float32 nanomaggy^-2 PSF-based depth in r-band
PSFDEPTH_Z                 float32 nanomaggy^-2 PSF-based depth in z-band
GALDEPTH_G                 float32 nanomaggy^-2 Galaxy model-based depth in LS g-band
GALDEPTH_R                 float32 nanomaggy^-2 Galaxy model-based depth in LS r-band
GALDEPTH_Z                 float32 nanomaggy^-2 Galaxy model-based depth in LS z-band
PSFDEPTH_W1                float32 nanomaggy^-2 PSF-based depth in WISE W1
PSFDEPTH_W2                float32 nanomaggy^-2 PSF-based depth in WISE W2
PSFSIZE_G                  float32 arcsec       Median PSF size evaluated at the BRICK_PRIMARY objects in this brick in g-band
PSFSIZE_R                  float32 arcsec       Median PSF size evaluated at the BRICK_PRIMARY objects in this brick in r-band
PSFSIZE_Z                  float32 arcsec       Median PSF size evaluated at the BRICK_PRIMARY objects in this brick in z-band
========================== ======= ============ ===================================================================================================================================================================================================================================================


Notes and Examples
==================

.. _DESI Collaboration et al. (2024): https://ui.adsabs.harvard.edu/abs/2024arXiv241112020D/abstract
