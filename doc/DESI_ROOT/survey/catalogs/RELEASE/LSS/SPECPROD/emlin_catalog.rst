=============
emlin_catalog
=============

:Summary: Concatenation of all of the dark time emission line file outputs
:Naming Convention: ``emlin_catalog.fits``
:Regex: ``emlin_catalog\.fits``
:File Type: FITS, 3 GB

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

EXTNAME = EMLIN

Concatenation of all of the dark time tile-based emission line file outputs (CROSS-REF)

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =======================
    KEY    Example Value Type Comment
    ====== ============= ==== =======================
    NAXIS1 312           int  width of table in bytes
    NAXIS2 11632889      int  number of rows in table
    DESIDR dr1           str  DESI Data Release
    ====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

================= ======= ================================= ====================================================================================================================
Name              Type    Units                             Description
================= ======= ================================= ====================================================================================================================
TARGETID          int64                                     Unique DESI target ID
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
LOCATION          int64                                     Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
TILEID            int64                                     Unique DESI tile ID
================= ======= ================================= ====================================================================================================================


Notes and Examples
==================


