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


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
