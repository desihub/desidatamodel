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
HDU00_              IMAGE    Empty
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
====== ============ ======== ========================================


FITS Header Units
=================

HDU00
-----

Empty data, just header keywords with code versions

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================= ==== ==============================================
KEY      Example Value     Type Comment
======== ================= ==== ==============================================
FLAVOR   science           str
DEPNAM00 python            str
DEPVER00 3.5.2             str
DEPNAM01 numpy             str
DEPVER01 1.11.3            str
DEPNAM02 scipy             str
DEPVER02 0.18.1            str
DEPNAM03 astropy           str
DEPVER03 1.3.2             str
DEPNAM04 yaml              str
DEPVER04 3.12              str
DEPNAM05 mpi4py            str
DEPVER05 2.0.0             str
DEPNAM06 desiutil          str
DEPVER06 1.9.4.dev498      str
DEPNAM07 desispec          str
DEPVER07 0.14.0.dev1348    str
DEPNAM08 desitarget        str
DEPVER08 0.11.0.dev801     str
DEPNAM09 desimodel         str
DEPVER09 0.6.0.dev178      str
DEPNAM10 desisim           str
DEPVER10 0.18.3.dev863     str
DEPNAM11 specter           str
DEPVER11 0.7.0dev1         str
DEPNAM12 speclite          str
DEPVER12 0.5               str
DEPNAM13 specsim           str
DEPVER13 0.10dev717.dev717 str
DOSVER   SIM               str
FEEVER   SIM               str
FIBERMIN 50                int
DEPNAM14 matplotlib        str
DEPVER14 1.5.3             str
CHECKSUM LFMPL9MNLCMNL9MN  str  HDU checksum updated 2017-06-17T17:32:16
DATASUM  0                 str  data unit checksum updated 2017-06-17T17:32:16
HPXPIXEL 16890             int  healpix pixel using NESTED ordering
HPXNSIDE 64                int  healpix nside
HPXNEST  T                 bool healpix NESTED ordering (not RING)
======== ================= ==== ==============================================

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
ENCODING ascii            str
EXTNAME  FIBERMAP         str
CHECKSUM CNEMCM9KCMEKCM9K str  HDU checksum updated 2017-06-12T23:41:38
DATASUM  4109638159       str  data unit checksum updated 2017-06-12T23:41:38
======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=========== ========== ===== ===============================================
Name        Type       Units Description
=========== ========== ===== ===============================================
OBJTYPE     char[10]         Target type [ELG, LRG, QSO, STD, STAR, SKY]
TARGETCAT   char[20]         Name/version of the target catalog
BRICKNAME   char[8]          Brickname from target imaging
TARGETID    int64            Unique target ID
DESI_TARGET int64            DESI dark+calib targeting bit mask
BGS_TARGET  int64            DESI Bright Galaxy Survey targeting bit mask
MWS_TARGET  int64            DESI Milky Way Survey targeting bit mask
MAG         float32[5]       magnitudes in each of the filters
FILTER      char[50]         SDSS_R, DECAM_Z, WISE1, etc.
SPECTROID   int32            Spectrograph ID [0-9]
POSITIONER  int32            Positioner ID [0-4999] (deprecated)
LOCATION    int32            Positioner location ID 1000*PETAL + DEVICE
DEVICE_LOC  int32            Device location on petal [0-542]
PETAL_LOC   int32            Petal location on focal plane [0-9]
FIBER       int32            Fiber ID [0-4999]
LAMBDAREF   float32          Reference wavelength at which to align fiber
RA_TARGET   float64          Target right ascension [degrees]
DEC_TARGET  float64          Target declination [degrees]
RA_OBS      float64          RA of obs from (X,Y)_FVCOBS and optics [deg]
DEC_OBS     float64          dec of obs from (X,Y)_FVCOBS and optics [deg]
X_TARGET    float64          X on focal plane derived from (RA,DEC)_TARGET
Y_TARGET    float64          Y on focal plane derived from (RA,DEC)_TARGET
X_FVCOBS    float64          X location observed by Fiber View Cam [mm]
Y_FVCOBS    float64          Y location observed by Fiber View Cam [mm]
Y_FVCERR    float32          Y location uncertainty from Fiber View Cam [mm]
X_FVCERR    float32          X location uncertainty from Fiber View Cam [mm]
NIGHT       int32            Night of exposure YYYYMMDD
EXPID       int32            Exposure ID
=========== ========== ===== ===============================================

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
EXTNAME  B_WAVELENGTH     str  extension name
BUNIT    Angstrom         str
CHECKSUM IS7FJS5CIS5CIS5C str  HDU checksum updated 2017-06-12T23:41:38
DATASUM  3517056679       str  data unit checksum updated 2017-06-12T23:41:38
======== ================ ==== ==============================================

Data: 1D float32 image [nwave]

HDU03
-----

EXTNAME = B_FLUX

Flux[nspec,nwave] array in 1e-17 erg/(s cm2 Angstrom) of b-channel spectra

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================== ==== ==============================================
KEY      Example Value              Type Comment
======== ========================== ==== ==============================================
NAXIS1   2380                       int  Number of wavelengths
NAXIS2   1225                       int  Number of spectra
EXTNAME  B_FLUX                     str  extension name
BUNIT    1e-17 erg/(s cm2 Angstrom) str
CHECKSUM TeamUZWmTdamTZUm           str  HDU checksum updated 2017-06-12T23:41:39
DATASUM  2960563931                 str  data unit checksum updated 2017-06-12T23:41:39
======== ========================== ==== ==============================================

Data: 2D float32 image [nspec, nwave]

HDU04
-----

EXTNAME = B_IVAR

Inverse variance of b-channel flux array

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2380             int  Number of wavelengths
NAXIS2   1225             int  Number of spectra
EXTNAME  B_IVAR           str  extension name
CHECKSUM 9VDdGTCZ9TCdETCZ str  HDU checksum updated 2017-06-12T23:41:39
DATASUM  1834901626       str  data unit checksum updated 2017-06-12T23:41:39
======== ================ ==== ==============================================

Data: 2D float32 image [nspec, nwave]

HDU05
-----

EXTNAME = B_MASK

Mask[nspec,nwave] of b-channel flux array

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2380             int  Number of wavelengths
NAXIS2   1225             int  Number of spectra
BSCALE   1                int
BZERO    2147483648       int
EXTNAME  B_MASK           str  name of this binary table extension
CHECKSUM PaM2QVM1PZM1PZM1 str  HDU checksum updated 2017-06-12T23:41:39
DATASUM  1460550          str  data unit checksum updated 2017-06-12T23:41:39
======== ================ ==== ==============================================

Data: 2D float32 image [nspec, nwave]

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
EXTNAME  B_RESOLUTION     str  extension name
CHECKSUM 7ALhA9Kf8AKfA9Kf str  HDU checksum updated 2017-06-12T23:41:41
DATASUM  897957910        str  data unit checksum updated 2017-06-12T23:41:41
======== ================ ==== ==============================================

Data: 3D float32 image [nspec, ndiag, nwave]

A sparse resolution matrix may be created for spectrum ``i`` with::

    from desispec.resolution import Resolution
    R = Resolution(data[i])
    
Or using lower-level scipy.sparse matrices:

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
EXTNAME  R_WAVELENGTH     str  extension name
BUNIT    Angstrom         str
CHECKSUM 9MRYAKOX9KOXAKOX str  HDU checksum updated 2017-06-12T23:41:42
DATASUM  305316813        str  data unit checksum updated 2017-06-12T23:41:42
======== ================ ==== ==============================================

Data: 1D float32 image [nwave]

HDU08
-----

EXTNAME = R_FLUX

Flux[nspec,nwave] array in 1e-17 erg/(s cm2 Angstrom) of r-channel spectra

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================== ==== ==============================================
KEY      Example Value              Type Comment
======== ========================== ==== ==============================================
NAXIS1   2116                       int  Number of wavelengths
NAXIS2   1225                       int  Number of spectra
EXTNAME  R_FLUX                     str  extension name
BUNIT    1e-17 erg/(s cm2 Angstrom) str  Flux units
CHECKSUM EVZoGUYlEUYlEUYl           str  HDU checksum updated 2017-06-12T23:41:42
DATASUM  3800150027                 str  data unit checksum updated 2017-06-12T23:41:42
======== ========================== ==== ==============================================

Data: 2D float32 image [nspec, nwave]

HDU09
-----

EXTNAME = R_IVAR

Inverse variance of r-channel flux array

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2116             int  Number of wavelengths
NAXIS2   1225             int  Number of spectra
EXTNAME  R_IVAR           str  extension name
CHECKSUM oHfIr9ZFoGfFo9ZF str  HDU checksum updated 2017-06-12T23:41:42
DATASUM  3521235630       str  data unit checksum updated 2017-06-12T23:41:42
======== ================ ==== ==============================================

Data: 2D float32 image [nspec, nwave]

HDU10
-----

EXTNAME = R_MASK

Mask[nspec,nwave] of r-channel flux array

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2116             int  Number of wavelengths
NAXIS2   1225             int  Number of spectra
BSCALE   1                int
BZERO    2147483648       int
EXTNAME  R_MASK           str  name of this binary table extension
CHECKSUM ncKOnZIOnaIOnYIO str  HDU checksum updated 2017-06-12T23:41:43
DATASUM  1298386          str  data unit checksum updated 2017-06-12T23:41:43
======== ================ ==== ==============================================

Data: 2D float32 image [nspec, nwave]

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
EXTNAME  R_RESOLUTION     str  extension name
CHECKSUM 9HQT99QQ9GQQ99QQ str  HDU checksum updated 2017-06-12T23:41:45
DATASUM  695209495        str  data unit checksum updated 2017-06-12T23:41:45
======== ================ ==== ==============================================

Data: 3D float32 image [nspec, ndiag, nwave]

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
EXTNAME  Z_WAVELENGTH     str  extension name
BUNIT    Angstrom         str
CHECKSUM cHLHe9KGcGKGc9KG str  HDU checksum updated 2017-06-12T23:41:45
DATASUM  692648483        str  data unit checksum updated 2017-06-12T23:41:45
======== ================ ==== ==============================================

Data: 1D float32 image [nwave]

HDU13
-----

EXTNAME = Z_FLUX

Flux[nspec,nwave] array in 1e-17 erg/(s cm2 Angstrom) of z-channel spectra

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================== ==== ==============================================
KEY      Example Value              Type Comment
======== ========================== ==== ==============================================
NAXIS1   2399                       int  Number of wavelengths
NAXIS2   1225                       int  Number of spectra
EXTNAME  Z_FLUX                     str  extension name
BUNIT    1e-17 erg/(s cm2 Angstrom) str
CHECKSUM UARhW8RhUARhU7Rh           str  HDU checksum updated 2017-06-12T23:41:45
DATASUM  1166849465                 str  data unit checksum updated 2017-06-12T23:41:45
======== ========================== ==== ==============================================

Data: 2D float32 image [nspec, nwave]

HDU14
-----

EXTNAME = Z_IVAR

Inverse variance of z-channel flux array

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2399             int  Number of wavelengths
NAXIS2   1225             int  Number of spectra
EXTNAME  Z_IVAR           str  extension name
CHECKSUM fA44g713fA13f513 str  HDU checksum updated 2017-06-12T23:41:46
DATASUM  3583056072       str  data unit checksum updated 2017-06-12T23:41:46
======== ================ ==== ==============================================

Data: 2D float32 image [nspec, nwave]

HDU15
-----

EXTNAME = Z_MASK

Mask[nspec,nwave] of z-channel flux array

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2399             int  Number of wavelengths
NAXIS2   1225             int  Number of spectra
BSCALE   1                int
BZERO    2147483648       int
EXTNAME  Z_MASK           str  name of this binary table extension
CHECKSUM U7IfV6GZU6GfU6GZ str  HDU checksum updated 2017-06-12T23:41:46
DATASUM  2148956187       str  data unit checksum updated 2017-06-12T23:41:46
======== ================ ==== ==============================================

Data: 2D float32 image [nspec, nwave]

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
EXTNAME  Z_RESOLUTION     str  extension name
CHECKSUM gDaDiBX9gBaAgBU9 str  HDU checksum updated 2017-06-12T23:41:49
DATASUM  256401500        str  data unit checksum updated 2017-06-12T23:41:49
======== ================ ==== ==============================================

Data: 3D float32 image [nspec, ndiag, nwave]


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
  * TILEID column added to FIBERMAP HDU
