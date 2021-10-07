==========================
psfnight-CAMERA-NIGHT.fits
==========================

:Summary: PSF model for the night derived from combining multiple
          arc lamp calibration exposures.
:Naming Convention: ``psfnight-CAMERA-NIGHT.fits``, where ``CAMERA`` is
    *e.g.*, "b0", "r5", etc. and ``NIGHT`` is the observation night in
    YYYYMMDD format.
:Regex: ``psfnight-[brz][0-9]-[0-9]{8}\.fits``
:File Type: FITS, 1 MB

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_  XTRACE  IMAGE    *Brief Description*
HDU1_  YTRACE  IMAGE    *Brief Description*
HDU2_  PSF     BINTABLE *Brief Description*
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = XTRACE

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============= ===== =====================
KEY      Example Value Type  Comment
======== ============= ===== =====================
NAXIS1   7             int   length of data axis 1
NAXIS2   500           int   length of data axis 2
FIBERMIN 0             int
FIBERMAX 499           int
WAVEMIN  7339.0        float
WAVEMAX  9915.0        float
PSFTYPE  GAUSS-HERMITE str
PSFVER   3             int
======== ============= ===== =====================

Data: FITS image [float64, 7x500]

HDU1
----

EXTNAME = YTRACE

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============= ===== =====================
KEY      Example Value Type  Comment
======== ============= ===== =====================
NAXIS1   7             int   length of data axis 1
NAXIS2   500           int   length of data axis 2
FIBERMIN 0             int
FIBERMAX 499           int
WAVEMIN  7339.0        float
WAVEMAX  9915.0        float
======== ============= ===== =====================

Data: FITS image [float64, 7x500]

HDU2
----

EXTNAME = PSF

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================== ===== ===============================================
KEY      Example Value        Type  Comment
======== ==================== ===== ===============================================
NAXIS1   16016                int   width of table in bytes
NAXIS2   59                   int   number of rows in table
PSFTYPE  GAUSS-HERMITE        str
PSFVER   3                    str
MJD      0                    int   MJD of arc lamp exposure
PLATEID  0                    int   plate ID of arc lamp exposure
CAMERA   &#x27;z8      &#x27; str   camera ID
ARCEXP   0                    int   ID of arc lamp exposure used to fit PSF
NPIX_X   4114                 int   number of columns in input CCD image
NPIX_Y   4128                 int   number of rows in input CCD image
HSIZEX   8                    int   Half size of PSF in fit, NX=2*HSIZEX+1
HSIZEY   5                    int   Half size of PSF in fit, NY=2*HSIZEY+1
FIBERMIN 0                    int   first fiber (starting at 0)
FIBERMAX 499                  int   last fiber (included)
NPARAMS  57                   int   number of PSF parameters
LEGDEG   3                    int   degree of Legendre pol.(wave) for parameters
GHDEGX   6                    int   degree of Hermite polynomial along CCD columns
GHDEGY   6                    int   degree of Hermite polynomial along CCD rows
WAVEMIN  7339.0               float minimum wavelength (A), used for the Legendre p
WAVEMAX  9916.0               float maximum wavelength (A), used for the Legendre p
PSFERROR 0.0                  float assumed PSF fractional error in chi2
READNOIS 0.0                  float assumed read out noise in chi2
GAIN     1.0                  float assumed gain in chi2
B00RCHI2 1.256430376296926    float best fit chi2/ndf for fiber bundle 0
B00NDATA 133945               int   number of pixels in fit for fiber bundle 0
B00NPAR  2001                 int   number of parameters in fit for fiber bundle 0
B01RCHI2 1.292249289456854    float
B01NDATA 132777               int
B01NPAR  2000                 int
B02RCHI2 1.35177757140687     float
B02NDATA 130896               int
B02NPAR  1996                 int
B03RCHI2 1.212828517555558    float
B03NDATA 129431               int
B03NPAR  1990                 int
B04RCHI2 1.243345438017128    float
B04NDATA 128124               int
B04NPAR  1991                 int
B05RCHI2 1.241974739017806    float
B05NDATA 126997               int
B05NPAR  1986                 int
B06RCHI2 1.212335817110134    float
B06NDATA 125037               int
B06NPAR  1984                 int
B07RCHI2 1.228098049663856    float
B07NDATA 123165               int
B07NPAR  1980                 int
B08RCHI2 1.23179393043617     float
B08NDATA 122424               int
B08NPAR  1980                 int
B09RCHI2 1.247813953480912    float
B09NDATA 120904               int
B09NPAR  1979                 int
B10RCHI2 1.24325324817453     float
B10NDATA 120800               int
B10NPAR  1982                 int
B11RCHI2 1.229845840372646    float
B11NDATA 121900               int
B11NPAR  1979                 int
B12RCHI2 1.252979603776246    float
B12NDATA 123681               int
B12NPAR  1987                 int
B13RCHI2 1.265793265082578    float
B13NDATA 124585               int
B13NPAR  1985                 int
B14RCHI2 1.32821646467175     float
B14NDATA 125916               int
B14NPAR  1986                 int
B15RCHI2 1.224176003872552    float
B15NDATA 128151               int
B15NPAR  1991                 int
B16RCHI2 1.288490502974476    float
B16NDATA 130207               int
B16NPAR  1996                 int
B17RCHI2 1.326174162158112    float
B17NDATA 131147               int
B17NPAR  1998                 int
B18RCHI2 1.206508500311996    float
B18NDATA 123257               int
B18NPAR  1857                 int
B19RCHI2 1.166665900852116    float
B19NDATA 134219               int
B19NPAR  1991                 int
EXPID    0.0                  float
======== ==================== ===== ===============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

======= ============= ===== ===================
Name    Type          Units Description
======= ============= ===== ===================
PARAM   char[8]             label for field   1
COEFF   float64[2000]       label for field   2
LEGDEGX int32               label for field   3
LEGDEGW int32               label for field   4
======= ============= ===== ===================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
