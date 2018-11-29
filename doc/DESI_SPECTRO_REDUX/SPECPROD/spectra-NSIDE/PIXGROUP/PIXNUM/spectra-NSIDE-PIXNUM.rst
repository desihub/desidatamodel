=========================
spectra-NSIDE-PIXNUM.fits
=========================

:Summary: DESI spectra grouped by nested healpix number
:Naming Convention: ``spectra-{nside}-{pixnum}.fits``, where
    ``{nside}`` is the healpix nside and ``{pixnum}`` is the nested scheme
    healpix number.
:Regex: ``spectra-[0-9]+-[0-9]+\.fits``
:File Type: FITS, 1 GB

Contents
========

====== ============ ======== ========================================
Number EXTNAME      Type     Contents
====== ============ ======== ========================================
HDU00_ PRIMARY      IMAGE    Empty
HDU01_ FIBERMAP     BINTABLE fibermap table
HDU02_ SCORES       BINTABLE scores table
HDU03_ B_WAVELENGTH IMAGE    Wavelength array of b-channel spectra
HDU04_ B_FLUX       IMAGE    Flux of b-channel spectra
HDU05_ B_IVAR       IMAGE    Inverse variance of b-channel spectra
HDU06_ B_MASK       IMAGE    Mask of b-channel spectra
HDU07_ B_RESOLUTION IMAGE    Resolution matrices of b-channel spectra
HDU08_ R_WAVELENGTH IMAGE    Wavelength array of r-channel spectra
HDU09_ R_FLUX       IMAGE    Flux of r-channel spectra
HDU10_ R_IVAR       IMAGE    Inverse variance of r-channel spectra
HDU11_ R_MASK       IMAGE    Mask of r-channel spectra
HDU12_ R_RESOLUTION IMAGE    Resolution matrices of r-channel spectra
HDU13_ Z_WAVELENGTH IMAGE    Wavelength array of z-channel spectra
HDU14_ Z_FLUX       IMAGE    Flux of z-channel spectra
HDU15_ Z_IVAR       IMAGE    Inverse variance of z-channel spectra
HDU16_ Z_MASK       IMAGE    Mask of z-channel spectra
HDU17_ Z_RESOLUTION IMAGE    Resolution matrices of z-channel spectra
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

================= ======= ===== ============================================
Name              Type    Units Description
================= ======= ===== ============================================
TARGETID          int64         Unique target ID
DESI_TARGET       int64         DESI dark+calib targeting bit mask
BGS_TARGET        int64         DESI Bright Galaxy Survey targeting bit mask
MWS_TARGET        int64         DESI Milky Way Survey targeting bit mask
SECONDARY_TARGET  int64
TARGET_RA         float64       Target right ascension [degrees]
TARGET_DEC        float64       Target declination [degrees]
TARGET_RA_IVAR    float64
TARGET_DEC_IVAR   float64
BRICKID           int64
BRICK_OBJID       int64
MORPHTYPE         char[4]
PRIORITY          int32
SUBPRIORITY       float64
REF_ID            int64
PMRA              float32
PMDEC             float32
PMRA_IVAR         float32
PMDEC_IVAR        float32
FLUX_G            float32
FLUX_R            float32
FLUX_Z            float32
FLUX_W1           float32
FLUX_W2           float32
FLUX_IVAR_G       float32
FLUX_IVAR_R       float32
FLUX_IVAR_Z       float32
FLUX_IVAR_W1      float32
FLUX_IVAR_W2      float32
FIBERFLUX_G       float32
FIBERFLUX_R       float32
FIBERFLUX_Z       float32
FIBERFLUX_W1      float32
FIBERFLUX_W2      float32
FIBERTOTFLUX_G    float32
FIBERTOTFLUX_R    float32
FIBERTOTFLUX_Z    float32
FIBERTOTFLUX_W1   float32
FIBERTOTFLUX_W2   float32
MW_TRANSMISSION_G float32
MW_TRANSMISSION_R float32
MW_TRANSMISSION_Z float32
EBV               float32
PHOTSYS           char[1]
FIBER             int32         Fiber ID [0-4999]
PETAL_LOC         int32
DEVICE_LOC        int32
LOCATION          int32
FIBERSTATUS       int32
OBJTYPE           char[3]
LAMBDA_REF        float32
DESIGN_X          float32
DESIGN_Y          float32
DESIGN_Q          float32
DESIGN_S          float32
NUMTARGET         int16
FIBER_RA          float64
FIBER_DEC         float64
FIBER_RA_IVAR     float32
FIBER_DEC_IVAR    float32
DELTA_X           float32
DELTA_Y           float32
DELTA_X_IVAR      float32
DELTA_Y_IVAR      float32
NUM_ITER          int32
SPECTROID         int32
BRICKNAME         char[8]       Brickname from target imaging
LAMBDAREF         float64       Reference wavelength at which to align fiber
================= ======= ===== ============================================

HDU02
-----

EXTNAME = SCORES

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   288              int  width of table in bytes
NAXIS2   3526             int  number of rows in table
======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

===================== ======= ===== ===========
Name                  Type    Units Description
===================== ======= ===== ===========
SUM_RAW_COUNT_B       float64
MEDIAN_RAW_COUNT_B    float64
MEDIAN_RAW_SNR_B      float64
SUM_FFLAT_COUNT_B     float64
MEDIAN_FFLAT_COUNT_B  float64
MEDIAN_FFLAT_SNR_B    float64
SUM_SKYSUB_COUNT_B    float64
MEDIAN_SKYSUB_COUNT_B float64
MEDIAN_SKYSUB_SNR_B   float64
SUM_CALIB_COUNT_B     float64
MEDIAN_CALIB_COUNT_B  float64
MEDIAN_CALIB_SNR_B    float64
SUM_RAW_COUNT_R       float64
MEDIAN_RAW_COUNT_R    float64
MEDIAN_RAW_SNR_R      float64
SUM_FFLAT_COUNT_R     float64
MEDIAN_FFLAT_COUNT_R  float64
MEDIAN_FFLAT_SNR_R    float64
SUM_SKYSUB_COUNT_R    float64
MEDIAN_SKYSUB_COUNT_R float64
MEDIAN_SKYSUB_SNR_R   float64
SUM_CALIB_COUNT_R     float64
MEDIAN_CALIB_COUNT_R  float64
MEDIAN_CALIB_SNR_R    float64
SUM_RAW_COUNT_Z       float64
MEDIAN_RAW_COUNT_Z    float64
MEDIAN_RAW_SNR_Z      float64
SUM_FFLAT_COUNT_Z     float64
MEDIAN_FFLAT_COUNT_Z  float64
MEDIAN_FFLAT_SNR_Z    float64
SUM_SKYSUB_COUNT_Z    float64
MEDIAN_SKYSUB_COUNT_Z float64
MEDIAN_SKYSUB_SNR_Z   float64
SUM_CALIB_COUNT_Z     float64
MEDIAN_CALIB_COUNT_Z  float64
MEDIAN_CALIB_SNR_Z    float64
===================== ======= ===== ===========

HDU03
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

HDU04
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

HDU05
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

HDU06
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
ZSIMPLE  T                bool This keyword probably should not be here.
BZERO    2147483648       int
BSCALE   1                int
======== ================ ==== ==============================================

Data: FITS image [int32, 2975x5550]

HDU07
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

HDU08
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

HDU09
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

HDU10
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

HDU11
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
ZSIMPLE  T                bool This keyword probably should not be here.
BZERO    2147483648       int
BSCALE   1                int
======== ================ ==== ==============================================

Data: FITS image [int32, 2975x5550]

HDU12
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

HDU13
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

HDU14
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

HDU15
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

HDU16
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
ZSIMPLE  T                bool This keyword probably should not be here.
BZERO    2147483648       int
BSCALE   1                int
======== ================ ==== ==============================================

Data: FITS image [int32, 2975x5550]

HDU17
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
