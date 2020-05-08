==========================
coadd-SPECTRO-TILEID-NIGHT
==========================

:Summary: Coadded spectra
:Naming Convention: ``coadd-{spectro}-{tileid}-{night}.fits``, where
    ``{spectro}`` is the spectrograph number 0-9, 
    ``{tileid}`` is the tile ID,
    and ``{night}`` is the YEARMMDD date of sunset for that night.
:Regex: ``coadd-[0-9]-[0-9]+-[0-9]+\.fits``
:File Type: FITS, 1 GB

This file follows nearly the same format as the spectra files, except there is
one entry per target instead of one entry per exposure per target, and
the FIBERMAP replaces some exposure-specific columns with summary columns,
e.g. ``NIGHT`` becomes ``FIRST_NIGHT``, ``LAST_NIGHT``, and ``NUM_NIGHT``.

As-of software release 20.4 (desispec 0.34.4), the SCORES HDU is the last
HDU instead of HDU2.

Contents
========

====== ============ ======== ========================================
Number EXTNAME      Type     Contents
====== ============ ======== ========================================
HDU00_ PRIMARY      IMAGE    Empty
HDU01_ FIBERMAP     BINTABLE fibermap table
HDU02_ B_WAVELENGTH IMAGE    Wavelength array of b-channel spectra
HDU03_ B_FLUX       IMAGE    Flux of b-channel spectra
HDU04_ B_IVAR       IMAGE    Inverse variance of b-channel spectra
HDU05_ B_MASK       IMAGE    Mask of b-channel spectra
HDU06_ B_RESOLUTION IMAGE    Resolution matrices of b-channel spectra
HDU07_ R_WAVELENGTH IMAGE    Wavelength array of r-channel spectra
HDU08_ R_FLUX       IMAGE    Flux of r-channel spectra
HDU09_ R_IVAR       IMAGE    Inverse variance of r-channel spectra
HDU10_ R_MASK       IMAGE    Mask of r-channel spectra
HDU11_ R_RESOLUTION IMAGE    Resolution matrices of r-channel spectra
HDU12_ Z_WAVELENGTH IMAGE    Wavelength array of z-channel spectra
HDU13_ Z_FLUX       IMAGE    Flux of z-channel spectra
HDU14_ Z_IVAR       IMAGE    Inverse variance of z-channel spectra
HDU15_ Z_MASK       IMAGE    Mask of z-channel spectra
HDU16_ Z_RESOLUTION IMAGE    Resolution matrices of z-channel spectra
HDU17_ SCORES       BINTABLE QA scores table
====== ============ ======== ========================================


FITS Header Units
=================

HDU00
-----

EXTNAME = PRIMARY

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
CHECKSUM EAnFF7l9EAlEE5l9 str  HDU checksum updated 2018-03-29T22:45:34
DATASUM  0                str  data unit checksum updated 2018-03-29T22:45:34
======== ================ ==== ==============================================

Empty HDU.

HDU01
-----

EXTNAME = FIBERMAP

fibermap table with two additional columns NIGHT and EXPID

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   248              int  length of dimension 1
NAXIS2   1225             int  length of dimension 2
CHECKSUM EAnFF7l9EAlEE5l9 str  HDU checksum updated 2018-03-29T22:45:34
DATASUM  0                str  data unit checksum updated 2018-03-29T22:45:34
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
TARGET_RA                         float64       Target Right Ascension [degrees]
TARGET_DEC                        float64       Target declination [degrees]
PMRA                              float32       Proper motion in +RA direction (already includi
PMDEC                             float32       Proper motion in +dec direction
PMRA_IVAR                         float32       Inverse variance of PMRA
PMDEC_IVAR                        float32       Inverse variance of PMDEC
REF_EPOCH                         float32       proper motion reference epoch
LAMBDA_REF                        float32       Wavelength at which fiber was centered
FA_TARGET                         int64
FA_TYPE                           binary        Internal fiberassign target type
OBJTYPE                           char[3]       SKY, TGT, NON
FIBERASSIGN_X                     float32       Expected CS5 X on focal plane
FIBERASSIGN_Y                     float32       Expected CS5 Y on focal plane
NUMTARGET                         int16         Number of targets covered by positioner
PRIORITY                          int32         Assignment priority; larger=higher priority
SUBPRIORITY                       float64       Assignment subpriority [0-1)
OBSCONDITIONS                     int32         bitmask of allowable observing conditions
NUMOBS_MORE                       int32         current number of additional observations reque
RELEASE                           int16         imaging surveys release ID
BRICKID                           int32         Imaging Surveys brick ID
BRICKNAME                         char[8]
BRICK_OBJID                       int32         Imaging Surveys OBJID on that brick
MORPHTYPE                         char[4]       Imaging Surveys morphological type
TARGET_RA_IVAR                    float32       Inverse variance of TARGET_RA
TARGET_DEC_IVAR                   float32       Inverse variance of TARGET_DEC
EBV                               float32       Galactic extinction E(B-V) reddening from SFD98
FLUX_G                            float32       g-band flux
FLUX_R                            float32       r-band flux
FLUX_Z                            float32       z-band flux
FLUX_IVAR_G                       float32       Inverse variance of FLUX_G
FLUX_IVAR_R                       float32       Inverse variance of FLUX_R
FLUX_IVAR_Z                       float32       Inverse variance of FLUX_Z
MW_TRANSMISSION_G                 float32       Milky Way dust transmission in g [0-1]
MW_TRANSMISSION_R                 float32       Milky Way dust transmission in r [0-1]
MW_TRANSMISSION_Z                 float32       Milky Way dust transmission in z [0-1]
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
FLUX_W1                           float32       WISE W1-band flux
FLUX_W2                           float32       WISE W2-band flux
FLUX_W3                           float32
FLUX_W4                           float32
FLUX_IVAR_W1                      float32       Inverse variance of FLUX_W1
FLUX_IVAR_W2                      float32       Inverse variance of FLUX_W2
FLUX_IVAR_W3                      float32
FLUX_IVAR_W4                      float32
MW_TRANSMISSION_W1                float32
MW_TRANSMISSION_W2                float32
MW_TRANSMISSION_W3                float32
MW_TRANSMISSION_W4                float32
ALLMASK_G                         int16
ALLMASK_R                         int16
ALLMASK_Z                         int16
FIBERFLUX_G                       float32       g-band object model flux for 1&quot; seeing and 1.5&quot;
FIBERFLUX_R                       float32       r-band object model flux for 1&quot; seeing and 1.5&quot;
FIBERFLUX_Z                       float32       z-band object model flux for 1&quot; seeing and 1.5&quot;
FIBERTOTFLUX_G                    float32       like FIBERFLUX_G but including all objects over
FIBERTOTFLUX_R                    float32       like FIBERFLUX_R but including all objects over
FIBERTOTFLUX_Z                    float32       like FIBERFLUX_Z but including all objects over
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
REF_ID                            int64         Astrometric catalog reference ID (SOURCE_ID fro
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
PHOTSYS                           char[1]       N for BASS/MzLS, S for DECam
CMX_TARGET                        int64
PRIORITY_INIT                     int64         initial priority
NUMOBS_INIT                       int64         initial number of requested observations
HPXPIXEL                          int64         Healpix pixel number (NESTED)
BLOBDIST                          float32
FIBERFLUX_IVAR_G                  float32
FIBERFLUX_IVAR_R                  float32
FIBERFLUX_IVAR_Z                  float32
DESI_TARGET                       int64         Dark survey + calibration targeting bits
BGS_TARGET                        int64         Bright Galaxy Survey targeting bits
MWS_TARGET                        int64         Milky Way Survey targeting bits
NUM_ITER                          int64         Number of positioner iterations
FIBER_X                           float64
FIBER_Y                           float64
MEAN_DELTA_X                      float64
MEAN_DELTA_Y                      float64
FIBER_RA                          float64       RA of actual fiber position
FIBER_DEC                         float64       DEC of actual fiber position
NIGHT                             int32
EXPID                             int32
MJD                               float64
TILEID                            int32
COADD_NUMEXP                      int16
RMS_DELTA_X                       float64
RMS_DELTA_Y                       float64
FIRST_NIGHT                       int64
LAST_NIGHT                        int64
NUM_NIGHT                         int64
FIRST_EXPID                       int64
LAST_EXPID                        int64
NUM_EXPID                         int64
FIRST_TILEID                      int64
LAST_TILEID                       int64
NUM_TILEID                        int64
FIRST_FIBER                       int64
LAST_FIBER                        int64
NUM_FIBER                         int64
================================= ======= ===== =========================================================


HDU02
-----

EXTNAME = B_WAVELENGTH

Wavelength[nwave] array in Angstroms of b-channel spectra

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2380             int  Number of wavelengths
BUNIT    Angstrom         str
======== ================ ==== ==============================================

Data: FITS image [float64, nwave]

HDU03
-----

EXTNAME = B_FLUX

Flux[nspec,nwave] array in 1e-17 erg/(s cm2 Angstrom) of b-channel spectra

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== =============================== ==== ==============================================
KEY      Example Value                   Type Comment
======== =============================== ==== ==============================================
NAXIS1   2380                            int  Number of wavelengths
NAXIS2   1225                            int  Number of spectra
BUNIT    10**-17 erg/(s cm2 Angstrom)    str
======== =============================== ==== ==============================================

Data: FITS image [float32, nspec x nwave]

HDU04
-----

EXTNAME = B_IVAR

Inverse variance of b-channel flux array

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================================= ==== ==============================================
KEY      Example Value                     Type Comment
======== ================================= ==== ==============================================
NAXIS1   2380                              int  Number of wavelengths
NAXIS2   1225                              int  Number of spectra
BUNIT    10**+34 (s2 cm4 Angstrom2) / erg2 str
======== ================================= ==== ==============================================

Data: FITS image [float32, nspec x nwave]

HDU05
-----

EXTNAME = B_MASK

Mask[nspec,nwave] of b-channel flux array.

Prior to desispec/0.24.0 and software release 18.9, the B_MASK HDU was compressed.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2380             int  Number of wavelengths
NAXIS2   1225             int  Number of spectra
BZERO    2147483648       int
BSCALE   1                int
======== ================ ==== ==============================================

Data: FITS image [int32 (compressed), 2975x5550]

HDU06
-----

EXTNAME = B_RESOLUTION

Diagonals of b-channel resolution matrix

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2380             int  Number of wavelengths
NAXIS2   9                int  Number of diagonals
NAXIS3   1225             int  Number of spectra
======== ================ ==== ==============================================

Data: FITS image [float32, nspec x ndiag x nwave]

A sparse resolution matrix may be created for spectrum ``i`` with::

    from desispec.resolution import Resolution
    R = Resolution(data[i])

Or using lower-level scipy.sparse matrices::

    import scipy.sparse
    import numpy as np
    nspec, ndiag, nwave = data.shape
    offsets = ndiag//2 - np.arange(ndiag, dtype=int)
    R = scipy.sparse.dia_matrix((data[i], offsets), shape=(nwave, nwave))

HDU07
-----

EXTNAME = R_WAVELENGTH

Wavelength[nwave] array in Angstroms of r-channel spectra

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2116             int  Number of wavelengths
BUNIT    Angstrom         str
======== ================ ==== ==============================================

Data: FITS image [float64, nwave]

HDU08
-----

EXTNAME = R_FLUX

Flux[nspec,nwave] array in 1e-17 erg/(s cm2 Angstrom) of r-channel spectra

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== =============================== ==== ==============================================
KEY      Example Value                   Type Comment
======== =============================== ==== ==============================================
NAXIS1   2380                            int  Number of wavelengths
NAXIS2   1225                            int  Number of spectra
BUNIT    10**-17 erg/(s cm2 Angstrom)    str
======== =============================== ==== ==============================================

Data: FITS image [float32, nspec x nwave]

HDU09
-----

EXTNAME = R_IVAR

Inverse variance of r-channel flux array

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================================= ==== ==============================================
KEY      Example Value                     Type Comment
======== ================================= ==== ==============================================
NAXIS1   2380                              int  Number of wavelengths
NAXIS2   1225                              int  Number of spectra
BUNIT    10**+34 (s2 cm4 Angstrom2) / erg2 str
======== ================================= ==== ==============================================

Data: FITS image [float32, nspec x nwave]

HDU10
-----

EXTNAME = R_MASK

Mask[nspec,nwave] of r-channel flux array.

Prior to desispec/0.24.0 and software release 18.9, the R_MASK HDU was compressed.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2116             int  Number of wavelengths
NAXIS2   1225             int  Number of spectra
BZERO    2147483648       int
BSCALE   1                int
======== ================ ==== ==============================================

Data: FITS image [int32 (compressed), 2975x5550]

HDU11
-----

EXTNAME = R_RESOLUTION

Diagonals of r-channel resolution matrix.

See B_RESOLUTION HDU for description of the format.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2116             int  Number of wavelengths
NAXIS2   9                int  Number of diagonals
NAXIS3   1225             int  Number of spectra
======== ================ ==== ==============================================

Data: FITS image [float32, nspec x ndiag x nwave]

HDU12
-----

EXTNAME = Z_WAVELENGTH

Wavelength[nwave] array in Angstroms of z-channel spectra

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2399             int  Number of wavelengths
BUNIT    Angstrom         str
======== ================ ==== ==============================================

Data: FITS image [float64, nwave]

HDU13
-----

EXTNAME = Z_FLUX

Flux[nspec,nwave] array in 1e-17 erg/(s cm2 Angstrom) of z-channel spectra

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== =============================== ==== ==============================================
KEY      Example Value                   Type Comment
======== =============================== ==== ==============================================
NAXIS1   2380                            int  Number of wavelengths
NAXIS2   1225                            int  Number of spectra
BUNIT    10**-17 erg/(s cm2 Angstrom)    str
======== =============================== ==== ==============================================

Data: FITS image [float32, nspec x nwave]

HDU14
-----

EXTNAME = Z_IVAR

Inverse variance of z-channel flux array

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================================= ==== ==============================================
KEY      Example Value                     Type Comment
======== ================================= ==== ==============================================
NAXIS1   2380                              int  Number of wavelengths
NAXIS2   1225                              int  Number of spectra
BUNIT    10**+34 (s2 cm4 Angstrom2) / erg2 str
======== ================================= ==== ==============================================

Data: FITS image [float32, nspec x nwave]

HDU15
-----

EXTNAME = Z_MASK

Mask[nspec,nwave] of z-channel flux array.

Prior to desispec/0.24.0 and software release 18.9, the Z_MASK HDU was compressed.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2399             int  Number of wavelengths
NAXIS2   1225             int  Number of spectra
BZERO    2147483648       int
BSCALE   1                int
======== ================ ==== ==============================================

Data: FITS image [int32 (compressed), 2975x5550]

HDU16
-----

EXTNAME = Z_RESOLUTION

Diagonals of z-channel resolution matrix.

See B_RESOLUTION HDU for description of the format.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2399             int  Number of wavelengths
NAXIS2   11               int  Number of diagonal elements
NAXIS3   1225             int  Number of spectra
======== ================ ==== ==============================================

Data: FITS image [float32, nspec x ndiag x nwave]

HDU17
-----

EXTNAME = SCORES

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   72               int  length of dimension 1
NAXIS2   500              int  length of dimension 2
ENCODING ascii            str
CHECKSUM TO8BWM59TM5ATM59 str  HDU checksum updated 2020-04-28T00:36:04
DATASUM  2417260239       str  data unit checksum updated 2020-04-28T00:36:04
======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=================== ======= ===== ===========
Name                Type    Units Description
=================== ======= ===== ===========
INTEG_COADD_FLUX_B  float64       integ. flux in wave. range 4000,5800A
MEDIAN_COADD_FLUX_B float64       median flux in wave. range 4000,5800A
MEDIAN_COADD_SNR_B  float64       median SNR/sqrt(A) in wave. range 4000,5800A
INTEG_COADD_FLUX_R  float64       integ. flux in wave. range 5800,7600A
MEDIAN_COADD_FLUX_R float64       median flux in wave. range 5800,7600A
MEDIAN_COADD_SNR_R  float64       median SNR/sqrt(A) in wave. range 5800,7600A
INTEG_COADD_FLUX_Z  float64       integ. flux in wave. range 7600,9800A
MEDIAN_COADD_FLUX_Z float64       median flux in wave. range 7600,9800A
MEDIAN_COADD_SNR_Z  float64       median SNR/sqrt(A) in wave. range 7600,9800A
=================== ======= ===== ===========

Notes and Examples
==================

The format supports arbitrary channel names as long as for each channel {X}
there is a set of HDUs named {X}_WAVELENGTH, {X}_FLUX, {X}_IVAR, {X}_MASK,
{X}_RESOLUTION.

Upcoming changes
================

The following changes are not yet in the spectra files, but will be added in
the future:

* signal-to-noise per band
