=======================
frame-CAMERA-EXPID.fits
=======================

:Summary: Frame files contain the raw extracted electrons from DESI data, without
    any further calibration.
:Naming Convention: ``frame-{CAMERA}-{EXPID}.fits``, where ``{CAMERA}`` is
    one of the spectrograph cameras (*e.g.* ``z1``) and ``{EXPID}``
    is the 8-digit exposure ID.
:Regex: ``frame-[brz][0-9]-[0-9]{8}\.fits``
:File Type: FITS, 70 MB

Contents
========

====== ========== ======== ===================
Number EXTNAME    Type     Contents
====== ========== ======== ===================
HDU0_  FLUX       IMAGE    Extracted electrons (photons)
HDU1_  IVAR       IMAGE    Inverse variance of extracted electrons
HDU2_  MASK       IMAGE    Bad value mask; 0=good
HDU3_  WAVELENGTH IMAGE    Wavelength grid of the extraction
HDU3_  RESOLUTION IMAGE    Resolution matrix
HDU5_  FIBERMAP   BINTABLE Fibermap
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
PASS     1                                           int
RA       150.87                                      float
DEC      31.23                                       float
EBMV     0.0189034678041935                          float
MJD      58925.11304582807                           float
TRANSPAR 0.7192993760108948                          float
DOSVER   SIM                                         str
FEEVER   SIM                                         str
BUNIT    count/Angstrom                              str
AIRORVAC vac                                         str   Vacuum wavelengths
CAMERA   z7                                          str
FIBERMIN 3500                                        int
CHECKSUM BeFKEbFIBbFIBbFI                            str   HDU checksum
DATASUM  2975688342                                  int   data unit checksum
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

Fibermap propagated from the raw data inputs; see
:doc:`fibermap file <../../../../../DESI_SPECTRO_DATA/NIGHT/EXPID/fibermap-EXPID>`.

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
FILTER      char[200]        SDSS_R, DECAM_Z, WISE1, etc.
SPECTROID   int64            Spectrograph ID [0-9]
POSITIONER  int32            Positioner Location ID [0-9542]
LOCATION    int32
DEVICE_LOC  int32
PETAL_LOC   int32
FIBER       int32            Fiber ID [0-4999]
LAMBDAREF   float32          Reference wavelength at which to align fiber
RA_TARGET   float64          Target right ascension [degrees]
DEC_TARGET  float64          Target declination [degrees]
RA_OBS      float64          RA of obs from (X,Y)_FVCOBS and optics [deg]
DEC_OBS     float64          dec of obs from (X,Y)_FVCOBS and optics [deg]
X_TARGET    float32          X on focal plane derived from (RA,DEC)_TARGET
Y_TARGET    float32          Y on focal plane derived from (RA,DEC)_TARGET
X_FVCOBS    float32          X location observed by Fiber View Cam [mm]
Y_FVCOBS    float32          Y location observed by Fiber View Cam [mm]
Y_FVCERR    float32          Y location uncertainty from Fiber View Cam [mm]
X_FVCERR    float32          X location uncertainty from Fiber View Cam [mm]
=========== ========== ===== ===============================================

Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
