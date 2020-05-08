=======================
frame-CAMERA-EXPID.fits
=======================

:Summary: fiber-flatfielded and sky-subtracted but not flux calibrated
          per-camera spectra.
:Naming Convention: ``sframe-{CAMERA}-{EXPID}.fits``, where ``{CAMERA}`` is
    one of the spectrograph cameras (*e.g.* ``z1``) and ``{EXPID}``
    is the 8-digit exposure ID.
:Regex: ``sframe-[brz][0-9]-[0-9]{8}\.fits``
:File Type: FITS, 70 MB

Contents
========

====== ========== ======== ===================
Number EXTNAME    Type     Contents
====== ========== ======== ===================
HDU0_  FLUX       IMAGE    flatfielded sky subtracted photons
HDU1_  IVAR       IMAGE    Inverse variance of FLUX
HDU2_  MASK       IMAGE    Bad value mask; 0=good
HDU3_  WAVELENGTH IMAGE    Wavelength grid of the extraction
HDU3_  RESOLUTION IMAGE    Resolution matrix
HDU5_  FIBERMAP   BINTABLE Fibermap
HDU6_  CHI2PIX    IMAGE    chi2 of PSF fit to CCD pixels
====== ========== ======== ===================

FITS Header Units
=================

HDU0
----

EXTNAME = FLUX

Extracted electrons[nspec, nwave]

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== =========================================== ===== ==================================
KEY      Example Value                               Type  Comment
======== =========================================== ===== ==================================
NAXIS1   6001                                        int   Number of wavelength samples
NAXIS2   500                                         int   Number of extracted spectra
NIGHT    20200316                                    str   Night of observation YEARMMDD
EXPID    20                                          int   DESI exposure ID
TILEID   11108                                       int   DESI tile ID
PROGRAM  DARK                                        str   program [dark, bright, ...]
FLAVOR   science                                     str   Flavor [arc, flat, science, zero, ...]
TELRA    150.87                                      float Telescope pointing RA [degrees]
TELDEC   31.23                                       float Telescope pointing dec [degrees]
AIRMASS  1.307154717878038                           float Airmass at middle of exposure
EXPTIME  1142.541228573218                           float Exposure time [sec]
SEEING   0.7572662830352783                          float Seeing FWHM [arcsec]
MOONFRAC 0.4083473802955095                          float Moon illumination fraction 0-1; 1=full
MOONALT  -79.39563600071901                          float Moon altitude [degrees]
MOONSEP  131.2947533254612                           float Moon:tile separation angle [degrees]
DATE-OBS 2020-03-17T02:42:47.160'                    str   Start of exposure
MJD      58924.37858796309                           float
SNR2FRAC 0.501188337802887                           float
TRANSP   0.9980747699737549                          float
SKY      1.0                                         float
RA       150.73                                      float
DEC      30.52                                       float
PASS     1                                           int
DOSVER   SIM                                         str
FEEVER   SIM                                         str
BUNIT    count/Angstrom                              str
AIRORVAC vac                                         str   Vacuum wavelengths
CAMERA   z1                                          str
FIBERMIN 500                                         int
CHECKSUM 1HdW1GZU1GbU1GZU                            str   HDU checksum updated 2018-03-01T15:04:16
DATASUM  4250999040                                  str   data unit checksum updated 2018-03-01T15:04:16
======== =========================================== ===== ==================================

Data: FITS image [float32]

HDU1
----

EXTNAME = IVAR

Inverse variance of the electrons in HDU0.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================= ==== =====================
KEY      Example Value     Type Comment
======== ================= ==== =====================
NAXIS1   6001              int  Number of wavlengths
NAXIS2   500               int  Number of spectra
CHECKSUM BeFKEbFIBbFIBbFI  str  HDU checksum
DATASUM  2975688342        int  data unit checksum
======== ================= ==== =====================

Data: FITS image [float32]

HDU2
----

EXTNAME = MASK

Mask of spectral data; 0=good.

Prior to desispec/0.24.0 and software release 18.9, the MASK HDU was compressed.

TODO: Add link to definition of which bits mean what.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2951             int  length of original image axis
NAXIS2   500              int  length of original image axis
BSCALE   1                int
BZERO    2147483648       int
CHECKSUM gaU7iZS4gaS4gWS4 str  HDU checksum updated 2016-06-10T16:57:58
DATASUM  737750           str  data unit checksum updated 2016-06-10T16:57:58
======== ================ ==== ==============================================

Data: FITS image [int32, 2951x500]

HDU3
----

EXTNAME = WAVELENGTH

1D array of wavelengths.  NAXIS1 here is the same length as NAXIS2 of
the first 2 HDUs.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== =====================
KEY      Example Value    Type Comment
======== ================ ==== =====================
NAXIS1   6001             int  Number of wavelengths
BUNIT    Angstrom         str
CHECKSUM gaU7iZS4gaS4gWS4 str  HDU checksum updated 2016-06-10T16:57:58
DATASUM  737750           str  data unit checksum updated 2016-06-10T16:57:58
======== ================ ==== =====================

Data: FITS image [float64]

HDU4
----

EXTNAME = RESOLUTION

Resolution matrix stored as a 3D sparse matrix:

Rdata[nspec, ndiag, nwave]

To convert this into sparse matrices for convolving a model that is sampled
at the same wavelengths as the extractions (HDU EXTNAME='WAVELENGTH'):

.. code::

    from scipy.sparse import spdiags
    from astropy.io import fits
    import numpy as np

    #- read a model and its wavelength vector from somewhere
    #- IMPORTANT: cast them to .astype(np.float64) to get native endian

    #- read the resolution data
    resdata = fits.getdata(framefile, 'RESOLUTION').astype(np.float64)

    nspec, nwave = model.shape
    convolvedmodel = np.zeros((nspec, nwave))
    diags = np.arange(10, -11, -1)

    for i in range(nspec):
        R = spdiags(resdata[i], diags, nwave, nwave)
        convolvedmodel[i] = R.dot(model)

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== =====================
KEY      Example Value    Type Comment
======== ================ ==== =====================
NAXIS1   6001             int  length of data axis 1
NAXIS2   21               int  length of data axis 2
NAXIS3   500              int  length of data axis 3
CHECKSUM gaU7iZS4gaS4gWS4 str  HDU checksum updated 2016-06-10T16:57:58
DATASUM  737750           str  data unit checksum updated 2016-06-10T16:57:58
======== ================ ==== =====================

Data: FITS image [float32]

HDU5
----

EXTNAME = FIBERMAP

Fibermap information combining fiberassign request with actual fiber locations.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   378              int  length of dimension 1
NAXIS2   500              int  length of dimension 2
ENCODING ascii            str
CHECKSUM UUVAVUS8UUSAUUS5 str  HDU checksum updated 2018-03-01T15:08:15
DATASUM  4154192770       str  data unit checksum updated 2018-03-01T15:08:15
======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

================================= ======= ===== ===========
Name                              Type    Units Description
================================= ======= ===== ===========
TARGETID                          int64         Unique target ID
PETAL_LOC                         int16         Focal plane petal location 0-9
DEVICE_LOC                        int32         Device location 0-5xx
LOCATION                          int64         1000*PETAL_LOC + DEVICE_LOC
FIBER                             int32         Fiber number 0-4999
FIBERSTATUS                       int32         Fiber status mask; 0=good
TARGET_RA                         float64
TARGET_DEC                        float64
PMRA                              float32
PMDEC                             float32
PMRA_IVAR                         float32
PMDEC_IVAR                        float32
REF_EPOCH                         float32
LAMBDA_REF                        float32
FA_TARGET                         int64
FA_TYPE                           binary
OBJTYPE                           char[3]
FIBERASSIGN_X                     float32
FIBERASSIGN_Y                     float32
NUMTARGET                         int16
PRIORITY                          int32
SUBPRIORITY                       float64
OBSCONDITIONS                     int32
NUMOBS_MORE                       int32
RELEASE                           int16
BRICKID                           int32
BRICKNAME                         char[8]
BRICK_OBJID                       int32
MORPHTYPE                         char[4]
TARGET_RA_IVAR                    float32
TARGET_DEC_IVAR                   float32
EBV                               float32
FLUX_G                            float32
FLUX_R                            float32
FLUX_Z                            float32
FLUX_IVAR_G                       float32
FLUX_IVAR_R                       float32
FLUX_IVAR_Z                       float32
MW_TRANSMISSION_G                 float32
MW_TRANSMISSION_R                 float32
MW_TRANSMISSION_Z                 float32
FRACFLUX_G                        float32
FRACFLUX_R                        float32
FRACFLUX_Z                        float32
FRACMASKED_G                      float32
FRACMASKED_R                      float32
FRACMASKED_Z                      float32
FRACIN_G                          float32
FRACIN_R                          float32
FRACIN_Z                          float32
NOBS_G                            int16
NOBS_R                            int16
NOBS_Z                            int16
PSFDEPTH_G                        float32
PSFDEPTH_R                        float32
PSFDEPTH_Z                        float32
GALDEPTH_G                        float32
GALDEPTH_R                        float32
GALDEPTH_Z                        float32
FLUX_W1                           float32
FLUX_W2                           float32
FLUX_W3                           float32
FLUX_W4                           float32
FLUX_IVAR_W1                      float32
FLUX_IVAR_W2                      float32
FLUX_IVAR_W3                      float32
FLUX_IVAR_W4                      float32
MW_TRANSMISSION_W1                float32
MW_TRANSMISSION_W2                float32
MW_TRANSMISSION_W3                float32
MW_TRANSMISSION_W4                float32
ALLMASK_G                         int16
ALLMASK_R                         int16
ALLMASK_Z                         int16
FIBERFLUX_G                       float32
FIBERFLUX_R                       float32
FIBERFLUX_Z                       float32
FIBERTOTFLUX_G                    float32
FIBERTOTFLUX_R                    float32
FIBERTOTFLUX_Z                    float32
WISEMASK_W1                       binary
WISEMASK_W2                       binary
MASKBITS                          int16
FRACDEV                           float32
FRACDEV_IVAR                      float32
SHAPEDEV_R                        float32
SHAPEDEV_E1                       float32
SHAPEDEV_E2                       float32
SHAPEDEV_R_IVAR                   float32
SHAPEDEV_E1_IVAR                  float32
SHAPEDEV_E2_IVAR                  float32
SHAPEEXP_R                        float32
SHAPEEXP_E1                       float32
SHAPEEXP_E2                       float32
SHAPEEXP_R_IVAR                   float32
SHAPEEXP_E1_IVAR                  float32
SHAPEEXP_E2_IVAR                  float32
REF_ID                            int64
REF_CAT                           char[2]
GAIA_PHOT_G_MEAN_MAG              float32
GAIA_PHOT_G_MEAN_FLUX_OVER_ERROR  float32
GAIA_PHOT_BP_MEAN_MAG             float32
GAIA_PHOT_BP_MEAN_FLUX_OVER_ERROR float32
GAIA_PHOT_RP_MEAN_MAG             float32
GAIA_PHOT_RP_MEAN_FLUX_OVER_ERROR float32
GAIA_PHOT_BP_RP_EXCESS_FACTOR     float32
GAIA_ASTROMETRIC_EXCESS_NOISE     float32
GAIA_DUPLICATED_SOURCE            logical
GAIA_ASTROMETRIC_SIGMA5D_MAX      float32
GAIA_ASTROMETRIC_PARAMS_SOLVED    logical
PARALLAX                          float32
PARALLAX_IVAR                     float32
PHOTSYS                           char[1]
CMX_TARGET                        int64
PRIORITY_INIT                     int64
NUMOBS_INIT                       int64
HPXPIXEL                          int64
BLOBDIST                          float32
FIBERFLUX_IVAR_G                  float32
FIBERFLUX_IVAR_R                  float32
FIBERFLUX_IVAR_Z                  float32
DESI_TARGET                       int64
BGS_TARGET                        int64
MWS_TARGET                        int64
NUM_ITER                          int64
FIBER_X                           float64
FIBER_Y                           float64
DELTA_X                           float64
DELTA_Y                           float64
FIBER_RA                          float64
FIBER_DEC                         float64
================================= ======= ===== ===========


HDU6
----

EXTNAME = CHI2PIX

chi2 of PSF fit to CCD pixels per spectrum wavelength bin.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2751             int  Number of wavelengths
NAXIS2   500              int  Number of spectra
CHECKSUM 9a6AJX549a59GU59 str  HDU checksum updated 2020-04-29T23:23:47
DATASUM  1952331107       str  data unit checksum updated 2020-04-29T23:23:47
======== ================ ==== ==============================================

Data: FITS image [float32, 2751x500]


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
