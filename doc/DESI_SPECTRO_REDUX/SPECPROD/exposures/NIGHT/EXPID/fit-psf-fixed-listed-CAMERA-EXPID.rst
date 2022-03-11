===
fit
===

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``fit-psf-fixed-listed-r4-00085370.fits``, where ... *Give a human readable
    description of the filename, e.g. ``blat-{EXPID}`` where ``{EXPID}``
    is the 8-digit exposure ID.*
:Regex: ``fit-psf-fixed-listed-r4-00085370.fits`` *Give a regular expression for this filename.
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
WAVEMIN  5553.0        float
WAVEMAX  7797.0        float
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
WAVEMIN  5553.0        float
WAVEMAX  7797.0        float
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
CAMERA   &#x27;r4      &#x27; str   camera ID
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
WAVEMIN  5553.0               float minimum wavelength (A), used for the Legendre p
WAVEMAX  7798.0               float maximum wavelength (A), used for the Legendre p
PSFERROR 0.0                  float assumed PSF fractional error in chi2
READNOIS 0.0                  float assumed read out noise in chi2
GAIN     1.0                  float assumed gain in chi2
B00RCHI2 1.18577631126628     float best fit chi2/ndf for fiber bundle 0
B00NDATA 124885               int   number of pixels in fit for fiber bundle 0
B00NPAR  1592                 int   number of parameters in fit for fiber bundle 0
B01RCHI2 1.39798479223023     float best fit chi2/ndf for fiber bundle 1
B01NDATA 121253               int   number of pixels in fit for fiber bundle 1
B01NPAR  1520                 int   number of parameters in fit for fiber bundle 1
B02RCHI2 1.42237444435106     float best fit chi2/ndf for fiber bundle 2
B02NDATA 121678               int   number of pixels in fit for fiber bundle 2
B02NPAR  1527                 int   number of parameters in fit for fiber bundle 2
B03RCHI2 1.55025007015837     float best fit chi2/ndf for fiber bundle 3
B03NDATA 120122               int   number of pixels in fit for fiber bundle 3
B03NPAR  1581                 int   number of parameters in fit for fiber bundle 3
B04RCHI2 1.2526823567582      float best fit chi2/ndf for fiber bundle 4
B04NDATA 121057               int   number of pixels in fit for fiber bundle 4
B04NPAR  1600                 int   number of parameters in fit for fiber bundle 4
B05RCHI2 1.36435750337787     float best fit chi2/ndf for fiber bundle 5
B05NDATA 120482               int   number of pixels in fit for fiber bundle 5
B05NPAR  1545                 int   number of parameters in fit for fiber bundle 5
B06RCHI2 1.25163361513086     float best fit chi2/ndf for fiber bundle 6
B06NDATA 116053               int   number of pixels in fit for fiber bundle 6
B06NPAR  1520                 int   number of parameters in fit for fiber bundle 6
B07RCHI2 1.37653791308337     float best fit chi2/ndf for fiber bundle 7
B07NDATA 115847               int   number of pixels in fit for fiber bundle 7
B07NPAR  1576                 int   number of parameters in fit for fiber bundle 7
B08RCHI2 1.29228070424323     float best fit chi2/ndf for fiber bundle 8
B08NDATA 115666               int   number of pixels in fit for fiber bundle 8
B08NPAR  1581                 int   number of parameters in fit for fiber bundle 8
B09RCHI2 1.20572723562022     float best fit chi2/ndf for fiber bundle 9
B09NDATA 114492               int   number of pixels in fit for fiber bundle 9
B09NPAR  1589                 int   number of parameters in fit for fiber bundle 9
B10RCHI2 1.52286506009472     float best fit chi2/ndf for fiber bundle 10
B10NDATA 116078               int   number of pixels in fit for fiber bundle 10
B10NPAR  1594                 int   number of parameters in fit for fiber bundle 10
B11RCHI2 1.21531711639458     float best fit chi2/ndf for fiber bundle 11
B11NDATA 117322               int   number of pixels in fit for fiber bundle 11
B11NPAR  1601                 int   number of parameters in fit for fiber bundle 11
B12RCHI2 2.53769799721894     float best fit chi2/ndf for fiber bundle 12
B12NDATA 117325               int   number of pixels in fit for fiber bundle 12
B12NPAR  1576                 int   number of parameters in fit for fiber bundle 12
B13RCHI2 1.36855830290453     float best fit chi2/ndf for fiber bundle 13
B13NDATA 116914               int   number of pixels in fit for fiber bundle 13
B13NPAR  1571                 int   number of parameters in fit for fiber bundle 13
B14RCHI2 1.21449547754341     float best fit chi2/ndf for fiber bundle 14
B14NDATA 119453               int   number of pixels in fit for fiber bundle 14
B14NPAR  1589                 int   number of parameters in fit for fiber bundle 14
B15RCHI2 1.21542637620209     float best fit chi2/ndf for fiber bundle 15
B15NDATA 121377               int   number of pixels in fit for fiber bundle 15
B15NPAR  1598                 int   number of parameters in fit for fiber bundle 15
B16RCHI2 1.28753526500556     float best fit chi2/ndf for fiber bundle 16
B16NDATA 120486               int   number of pixels in fit for fiber bundle 16
B16NPAR  1567                 int   number of parameters in fit for fiber bundle 16
B17RCHI2 1.20861101909093     float best fit chi2/ndf for fiber bundle 17
B17NDATA 122425               int   number of pixels in fit for fiber bundle 17
B17NPAR  1584                 int   number of parameters in fit for fiber bundle 17
B18RCHI2 1.22079793165092     float best fit chi2/ndf for fiber bundle 18
B18NDATA 123805               int   number of pixels in fit for fiber bundle 18
B18NPAR  1580                 int   number of parameters in fit for fiber bundle 18
B19RCHI2 1.24524211762302     float best fit chi2/ndf for fiber bundle 19
B19NDATA 125587               int   number of pixels in fit for fiber bundle 19
B19NPAR  1589                 int   number of parameters in fit for fiber bundle 19
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
