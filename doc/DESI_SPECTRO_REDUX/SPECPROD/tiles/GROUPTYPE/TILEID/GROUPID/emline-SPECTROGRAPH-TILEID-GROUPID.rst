=======================================
emline-SPECTROGRAPH-TILEID-GROUPID.fits
=======================================

:Summary: This file records simple (Gaussian) emission line fits on the spectra for few major lines.
:Naming Convention: ``emline-SPECTROGRAPH-TILEID-GROUPID.fits``, where
    ``SPECTROGRAPH`` is the spectrograph ID, ``TILEID`` is the tile number and
    ``GROUPID`` depends on the ``GROUPTYPE`` of the tile coadd.
:Regex: ``emline-[0-9]-[0-9]+-([14]xsubset[1-6]|lowspeedsubset[1-6]|exp[0-9]{8}|thru[0-9]{8}|[0-9]{8})\.fits``
:File Type: FITS, 188 KB

Contents
========

====== ========= ======== ===================
Number EXTNAME   Type     Contents
====== ========= ======== ===================
HDU0_            IMAGE    Empty
HDU1_  EMLINEFIT BINTABLE Emission line fits table
====== ========= ======== ===================


FITS Header Units
=================

HDU0
----

Empty HDU.

HDU1
----

EXTNAME = EMLINEFIT

Table with the emission line fit results for few major lines.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== =============================================================================================== ===== =======================
    KEY      Example Value                                                                                   Type  Comment
    ======== =============================================================================================== ===== =======================
    NAXIS1   345                                                                                             int   width of table in bytes
    NAXIS2   500                                                                                             int   number of rows in table
    RRFN     /global/cfs/cdirs/desi/spectro/redux/fuji/tiles/1x_depth/80608/5/redrock-1-80608-1xsubset5.fits str   full path to the redrock file which contains the redshifts
    COADDFN  /global/cfs/cdirs/desi/spectro/redux/fuji/tiles/1x_depth/80608/5/coadd-1-80608-1xsubset5.fits   str   full path to the coadd file which contains the spectra
    RFHW     40                                                                                              int   [Angstrom] rest-frame wavelength width used for fitting on each side of the line
    MINRFHW  20                                                                                              int   [Angstrom] minimum requested *rest-frame* width on each side of the line to consider the fitting
    RFCONTW  200                                                                                             int   [Angstrom] rest-frame wavelength extent to fit the continuum
    RV       3.1                                                                                             float value of R_V to convert EBV to magnitudes
    EMNAMES  OII,HDELTA,HGAMMA,HBETA,OIII,HALPHA                                                             str   comma-separated list of emission lines to fit
    RFWAVE00 3727.092,3729.874                                                                               str   [Angstrom] rest-frame, vacuum, wavelength for the first emission line to fit
    RFWAVE01 4102.892                                                                                        str   [Angstrom] rest-frame, vacuum, wavelength for the second emission line to fit
    RFWAVE02 4341.684                                                                                        str   [Angstrom] rest-frame, vacuum, wavelength for the third emission line to fit
    RFWAVE03 4862.683                                                                                        str   [Angstrom] rest-frame, vacuum, wavelength for the forth emission line to fit
    RFWAVE04 4960.295,5008.239                                                                               str   [Angstrom] rest-frame, vacuum, wavelength for the fifth emission line to fit
    RFWAVE05 6564.613                                                                                        str   [Angstrom] rest-frame, vacuum, wavelength for the sixth emission line to fit
    ======== =============================================================================================== ===== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

================= ======= ================================= ====================================================================================================================
Name              Type    Units                             Description
================= ======= ================================= ====================================================================================================================
TARGETID          int64                                     Unique DESI target ID
Z                 float64                                   Redshift measured by Redrock
ZWARN             int64                                     Redshift warning bitmask from Redrock
SPECTYPE          char[6]                                   Spectral type of Redrock best fit template (e.g. GALAXY, QSO, STAR)
DELTACHI2         float64                                   chi2 difference between first- and second-best redrock template fits
TARGET_RA         float64 deg                               Target right ascension
TARGET_DEC        float64 deg                               Target declination
OBJTYPE           char[3]                                   Object type: TGT, SKY, NON, BAD
OII_FLUX          float32 10**-17 erg/(s cm2)               Fitted flux for the [OII] doublet
OII_FLUX_IVAR     float32 10**+34 (s2 cm4) / erg2           Inverse variance of the fitted flux for the [OII] doublet
OII_SIGMA         float32 Angstrom                          Fitted line width (in the observed frame) for the [OII] doublet
OII_SIGMA_IVAR    float32 Angstrom^-2                       Inverse variance of the fitted line width (in the observed frame) for the [OII] doublet
OII_CONT          float32 10**-17 erg/(s cm2 Angstrom)      Continuum used for the fitting (fixed value) for the [OII] doublet
OII_CONT_IVAR     float32 10**+34 (s2 cm4 Angstrom2) / erg2 Inverse variance of the continuum for the [OII] doublet
OII_SHARE         float32                                   Fitted F1/(F0+F1) for the [OII] doublet, where F0 and F1 are the individual line fluxes
OII_SHARE_IVAR    float32                                   Inverse variance of the fitted F1/(F0+F1) for the [OII] doublet
OII_EW            float32 Angstrom                          Fitted rest-frame equivalent width for the [OII] doublet
OII_EW_IVAR       float32 Angstrom^-2                       Inverse variance of the fitted rest-frame equivalent width for the [OII] doublet
OII_CHI2          float32                                   Reduced chi2 of the fit for the [OII] doublet
OII_NDOF          int32                                     Number of degrees of freedom of the fit for the [OII] doublet
HDELTA_FLUX       float32 10**-17 erg/(s cm2)               Fitted flux for the HDELTA line
HDELTA_FLUX_IVAR  float32 10**+34 (s2 cm4) / erg2           Inverse variance of the fitted flux for the HDELTA line
HDELTA_SIGMA      float32 Angstrom                          Fitted line width (in the observed frame) for the HDELTA line
HDELTA_SIGMA_IVAR float32 Angstrom^-2                       Inverse variance of the fitted line width (in the observed frame) for the HDELTA line
HDELTA_CONT       float32 10**-17 erg/(s cm2 Angstrom)      Continuum used for the fitting (fixed value) for the HDELTA line
HDELTA_CONT_IVAR  float32 10**+34 (s2 cm4 Angstrom2) / erg2 Inverse variance of the continuum for the HDELTA line
HDELTA_SHARE      float32                                   NaN (SHARE not relevant for HDELTA line)
HDELTA_SHARE_IVAR float32                                   NaN (SHARE not relevant for HDELTA line)
HDELTA_EW         float32 Angstrom                          Fitted rest-frame equivalent width for the HDELTA line
HDELTA_EW_IVAR    float32 Angstrom^-2                       Inverse variance of the fitted rest-frame equivalent width for the HDELTA line
HDELTA_CHI2       float32                                   Reduced chi2 of the fit for the HDELTA line
HDELTA_NDOF       int32                                     Number of degrees of freedom of the fit for the HDELTA line
HGAMMA_FLUX       float32 10**-17 erg/(s cm2)               Fitted flux for the HGAMMA line
HGAMMA_FLUX_IVAR  float32 10**+34 (s2 cm4) / erg2           Inverse variance of the fitted flux for the HGAMMA line
HGAMMA_SIGMA      float32 Angstrom                          Fitted line width (in the observed frame) for the HGAMMA line
HGAMMA_SIGMA_IVAR float32 Angstrom^-2                       Inverse variance of the fitted line width (in the observed frame) for the HGAMMA line
HGAMMA_CONT       float32 10**-17 erg/(s cm2 Angstrom)      Continuum used for the fitting (fixed value) for the HGAMMA line
HGAMMA_CONT_IVAR  float32 10**+34 (s2 cm4 Angstrom2) / erg2 Inverse variance of the continuum for the HGAMMA line
HGAMMA_SHARE      float32                                   NaN (SHARE not relevant for HGAMMA line)
HGAMMA_SHARE_IVAR float32                                   NaN (SHARE not relevant for HGAMMA line)
HGAMMA_EW         float32 Angstrom                          Fitted rest-frame equivalent width for the HGAMMA line
HGAMMA_EW_IVAR    float32 Angstrom^-2                       Inverse variance of the fitted rest-frame equivalent width for the HGAMMA line
HGAMMA_CHI2       float32                                   Reduced chi2 of the fit for the HGAMMA line
HGAMMA_NDOF       int32                                     Number of degrees of freedom of the fit for the HGAMMA line
HBETA_FLUX        float32 10**-17 erg/(s cm2)               Fitted flux for the HBETA line
HBETA_FLUX_IVAR   float32 10**+34 (s2 cm4) / erg2           Inverse variance of the fitted flux for the HBETA line
HBETA_SIGMA       float32 Angstrom                          Fitted line width (in the observed frame) for the HBETA line
HBETA_SIGMA_IVAR  float32 Angstrom^-2                       Inverse variance of the fitted line width (in the observed frame) for the HBETA line
HBETA_CONT        float32 10**-17 erg/(s cm2 Angstrom)      Continuum used for the fitting (fixed value) for the HBETA line
HBETA_CONT_IVAR   float32 10**+34 (s2 cm4 Angstrom2) / erg2 Inverse variance of the continuum for the HBETA line
HBETA_SHARE       float32                                   NaN (SHARE not relevant for HBETA line)
HBETA_SHARE_IVAR  float32                                   NaN (SHARE not relevant for HBETA line)
HBETA_EW          float32 Angstrom                          Fitted rest-frame equivalent width for the HBETA line
HBETA_EW_IVAR     float32 Angstrom^-2                       Inverse variance of the fitted rest-frame equivalent width for the HBETA line
HBETA_CHI2        float32                                   Reduced chi2 of the fit for the HBETA line
HBETA_NDOF        int32                                     Number of degrees of freedom of the fit for the HBETA line
OIII_FLUX         float32 10**-17 erg/(s cm2)               Fitted flux for the [OIII] doublet
OIII_FLUX_IVAR    float32 10**+34 (s2 cm4) / erg2           Inverse variance of the fitted flux for the [OIII] doublet
OIII_SIGMA        float32 Angstrom                          Fitted line width (in the observed frame) for the [OIII] doublet
OIII_SIGMA_IVAR   float32 Angstrom^-2                       Inverse variance of the fitted line width (in the observed frame) for the [OIII] doublet
OIII_CONT         float32 10**-17 erg/(s cm2 Angstrom)      Continuum used for the fitting (fixed value) for the [OIII] doublet
OIII_CONT_IVAR    float32 10**+34 (s2 cm4 Angstrom2) / erg2 Inverse variance of the continuum for the [OIII] doublet
OIII_SHARE        float32                                   F1/(F0+F1) for the [OIII] doublet, where F0 and F1 are the individual line fluxes (SHARE value fixed during the fit)
OIII_SHARE_IVAR   float32                                   Infinite value, as SHARE is fixed during the fit
OIII_EW           float32 Angstrom                          Fitted rest-frame equivalent width for the [OIII] doublet
OIII_EW_IVAR      float32 Angstrom^-2                       Inverse variance of the fitted rest-frame equivalent width for the [OIII] doublet
OIII_CHI2         float32                                   Reduced chi2 of the fit for the [OIII] doublet
OIII_NDOF         int32                                     Number of degrees of freedom of the fit for the [OIII] doublet
HALPHA_FLUX       float32 10**-17 erg/(s cm2)               Fitted flux for the HALPHA line
HALPHA_FLUX_IVAR  float32 10**+34 (s2 cm4) / erg2           Inverse variance of the fitted flux for the HALPHA line
HALPHA_SIGMA      float32 Angstrom                          Fitted line width (in the observed frame) for the HALPHA line
HALPHA_SIGMA_IVAR float32 Angstrom^-2                       Inverse variance of the fitted line width (in the observed frame) for the HALPHA line
HALPHA_CONT       float32 10**-17 erg/(s cm2 Angstrom)      Continuum used for the fitting (fixed value) for the HALPHA line
HALPHA_CONT_IVAR  float32 10**+34 (s2 cm4 Angstrom2) / erg2 Inverse variance of the continuum for the HALPHA line
HALPHA_SHARE      float32                                   NaN (SHARE not relevant for HALPHA line)
HALPHA_SHARE_IVAR float32                                   NaN (SHARE not relevant for HALPHA line)
HALPHA_EW         float32 Angstrom                          Fitted rest-frame equivalent width for the HALPHA line
HALPHA_EW_IVAR    float32 Angstrom^-2                       Inverse variance of the fitted rest-frame equivalent width for the HALPHA line
HALPHA_CHI2       float32                                   Reduced chi2 of the fit for the HALPHA line
HALPHA_NDOF       int32                                     Number of degrees of freedom of the fit for the HALPHA line
================= ======= ================================= ====================================================================================================================


Notes and Examples
==================

* The fit is done with the desispec.scripts.emline script.
* [OII] is fit as a doublet (3927 and 3929), with the line ratio left free during the fit.
* [OIII] is fit as a doublet (4960 and 5007), with the line ratio fixed during the fit.
* The SHARE is fitted only for the [OII] doublet; for the [OIII] doublet, its value is fixed (hence the infinite OIII_SHARE_IVAR); for the other lines, the SHARE is not used, and NaN are reported.
* If there are not enough pixels to fit or if the fit fails, NaN values are reported.
* The default settings are designed for the ELGs (e.g. max_sigma); values to be interpreted with caution for the other targets.
* The fitted flux is not forced to be positive, so negative values can happen.
* The Z,ZWARN,SPECTYPE,DELTACHI2 (TARGET_RA,TARGET_DEC,OBJTYPE, respectively) columns come from the REDSHIFTS (FIBERMAP, respectively) extension of the input redrock file (see :doc:`redrock-SPECTROGRAPH-TILEID-GROUPID <redrock-SPECTROGRAPH-TILEID-GROUPID>`).
* For the SURVEY=cmx m33 tile (TILEID=80615) tile and all the SURVEY=sv1 tiles (except TILEID=80971-80976, the dc3r2 ones), proper-motion correction was applied at the :doc:`fiberassign </DESI_TARGET/fiberassign/tiles/TILES_VERSION/TILEXX/fiberassign-TILEID>` design step; thus the following columns can have different values than in the :doc:`desitarget products </DESI_TARGET/TARG_DIR/DR/VERSION/targets/PHASE/RESOLVE/OBSCON/PHASEtargets-OBSCON-RESOLVE-hp-HP>`: ``TARGET_RA``, ``TARGET_DEC``, ``REF_EPOCH``, ``PLATE_RA``, ``PLATE_DEC``, and ``PLATE_REF_EPOCH``.
* For the fuji (EDR) and guadalupe productions, the equivalent widths are wrong (overestimated) by a factor (1+Z) ** 2; the code bug has been corrected for subsequent productions (e.g. iron).
