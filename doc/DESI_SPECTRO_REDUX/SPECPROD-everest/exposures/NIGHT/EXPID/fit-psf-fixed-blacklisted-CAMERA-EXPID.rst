===
fit
===

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``fit-psf-fixed-blacklisted-r3-00067919.fits``, where ... *Give a human readable
    description of the filename, e.g. ``blat-{EXPID}`` where ``{EXPID}``
    is the 8-digit exposure ID.*
:Regex: ``fit-psf-fixed-blacklisted-r3-00067919.fits`` *Give a regular expression for this filename.
    For example, a six-digit number would correspond to ``[0-9]{6}``.*
:File Type: FITS, 537 KB  *This section gives the type of the file
    and its approximate size.*

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
WAVEMIN  5548.0        float
WAVEMAX  7839.0        float
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
WAVEMIN  5548.0        float
WAVEMAX  7839.0        float
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
NAXIS1   8016                 int   width of table in bytes
NAXIS2   59                   int   number of rows in table
PSFTYPE  GAUSS-HERMITE        str
PSFVER   3                    str
MJD      0                    int   MJD of arc lamp exposure
PLATEID  0                    int   plate ID of arc lamp exposure
CAMERA   &#x27;r3      &#x27; str   camera ID
ARCEXP   0                    int   ID of arc lamp exposure used to fit PSF
NPIX_X   4114                 int   number of columns in input CCD image
NPIX_Y   4128                 int   number of rows in input CCD image
HSIZEX   8                    int   Half size of PSF in fit, NX=2*HSIZEX+1
HSIZEY   5                    int   Half size of PSF in fit, NY=2*HSIZEY+1
FIBERMIN 0                    int   first fiber (starting at 0)
FIBERMAX 499                  int   last fiber (included)
NPARAMS  57                   int   number of PSF parameters
LEGDEG   1                    int   degree of Legendre pol.(wave) for parameters
GHDEGX   6                    int   degree of Hermite polynomial along CCD columns
GHDEGY   6                    int   degree of Hermite polynomial along CCD rows
WAVEMIN  5548.0               float minimum wavelength (A), used for the Legendre p
WAVEMAX  7840.0               float maximum wavelength (A), used for the Legendre p
PSFERROR 0.0                  float assumed PSF fractional error in chi2
READNOIS 0.0                  float assumed read out noise in chi2
GAIN     1.0                  float assumed gain in chi2
B00RCHI2 1.21122461367993     float best fit chi2/ndf for fiber bundle 0
B00NDATA 124347               int   number of pixels in fit for fiber bundle 0
B00NPAR  1555                 int   number of parameters in fit for fiber bundle 0
B01RCHI2 1.31028334031294     float
B01NDATA 122816               int
B01NPAR  1556                 int
B02RCHI2 1.32678257048269     float
B02NDATA 119670               int
B02NPAR  1490                 int
B03RCHI2 1.31386491495622     float
B03NDATA 120221               int
B03NPAR  1550                 int
B04RCHI2 1.22016887429432     float
B04NDATA 117647               int
B04NPAR  1527                 int
B05RCHI2 1.37260451340339     float
B05NDATA 114963               int
B05NPAR  1522                 int
B06RCHI2 1.2614944388851      float
B06NDATA 114700               int
B06NPAR  1530                 int
B07RCHI2 1.26795964949353     float
B07NDATA 116751               int
B07NPAR  1555                 int
B08RCHI2 1.24720840207264     float
B08NDATA 116268               int
B08NPAR  1564                 int
B09RCHI2 1.31704762641115     float
B09NDATA 114371               int
B09NPAR  1499                 int
B10RCHI2 1.19254657292127     float
B10NDATA 110475               int
B10NPAR  1458                 int
B11RCHI2 1.23662438306734     float
B11NDATA 112600               int
B11NPAR  1522                 int
B12RCHI2 1.2317402772049      float
B12NDATA 115043               int
B12NPAR  1542                 int
B13RCHI2 1.23696548874535     float
B13NDATA 116548               int
B13NPAR  1541                 int
B14RCHI2 1.19376222839883     float
B14NDATA 114504               int
B14NPAR  1462                 int
B15RCHI2 1.20745141509192     float
B15NDATA 116110               int
B15NPAR  1513                 int
B16RCHI2 1.25952264744875     float
B16NDATA 119949               int
B16NPAR  1537                 int
B17RCHI2 1.30426488016153     float
B17NDATA 119126               int
B17NPAR  1523                 int
B18RCHI2 1.18970803759828     float
B18NDATA 119666               int
B18NPAR  1514                 int
B19RCHI2 1.17313642682565     float
B19NDATA 118368               int
B19NPAR  1507                 int
======== ==================== ===== ===============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

======= ============= ===== ===================
Name    Type          Units Description
======= ============= ===== ===================
PARAM   char[8]             label for field   1
COEFF   float64[1000]       label for field   2
LEGDEGX int32               label for field   3
LEGDEGW int32               label for field   4
======= ============= ===== ===================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
