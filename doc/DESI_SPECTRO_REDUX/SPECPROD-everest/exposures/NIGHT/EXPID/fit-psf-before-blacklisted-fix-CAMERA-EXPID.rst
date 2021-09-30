===
fit
===

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``fit-psf-before-blacklisted-fix-z4-00086211.fits``, where ... *Give a human readable
    description of the filename, e.g. ``blat-{EXPID}`` where ``{EXPID}``
    is the 8-digit exposure ID.*
:Regex: ``fit-psf-before-blacklisted-fix-z4-00086211.fits`` *Give a regular expression for this filename.
    For example, a six-digit number would correspond to ``[0-9]{6}``.*
:File Type: FITS, 998 KB  *This section gives the type of the file
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
WAVEMIN  7330.0        float
WAVEMAX  9932.0        float
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
WAVEMIN  7330.0        float
WAVEMAX  9932.0        float
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
CAMERA   &#x27;z4      &#x27; str   camera ID
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
WAVEMIN  7330.0               float minimum wavelength (A), used for the Legendre p
WAVEMAX  9933.0               float maximum wavelength (A), used for the Legendre p
PSFERROR 0.0                  float assumed PSF fractional error in chi2
READNOIS 0.0                  float assumed read out noise in chi2
GAIN     1.0                  float assumed gain in chi2
B00RCHI2 1.15027421643793     float best fit chi2/ndf for fiber bundle 0
B00NDATA 131049               int   number of pixels in fit for fiber bundle 0
B00NPAR  1947                 int   number of parameters in fit for fiber bundle 0
B01RCHI2 1.09572329091669     float
B01NDATA 128148               int
B01NPAR  1870                 int
B02RCHI2 1.12664502179126     float
B02NDATA 126497               int
B02NPAR  1861                 int
B03RCHI2 1.1550019382166      float
B03NDATA 125162               int
B03NPAR  1920                 int
B04RCHI2 1.18800037382513     float
B04NDATA 124898               int
B04NPAR  1940                 int
B05RCHI2 1.15700574480482     float
B05NDATA 121664               int
B05NPAR  1854                 int
B06RCHI2 1.59928134351731     float
B06NDATA 117930               int
B06NPAR  1819                 int
B07RCHI2 1.14788481203604     float
B07NDATA 116164               int
B07NPAR  1883                 int
B08RCHI2 1.16974737936224     float
B08NDATA 115893               int
B08NPAR  1896                 int
B09RCHI2 1.22409721441499     float
B09NDATA 115304               int
B09NPAR  1890                 int
B10RCHI2 1.19425999332713     float
B10NDATA 117718               int
B10NPAR  1919                 int
B11RCHI2 1.20379660237682     float
B11NDATA 118409               int
B11NPAR  1915                 int
B12RCHI2 1.40701798191161     float
B12NDATA 118107               int
B12NPAR  1897                 int
B13RCHI2 1.14639844309485     float
B13NDATA 119620               int
B13NPAR  1904                 int
B14RCHI2 1.91818832756228     float
B14NDATA 122612               int
B14NPAR  1920                 int
B15RCHI2 1.15740022174291     float
B15NDATA 124322               int
B15NPAR  1923                 int
B16RCHI2 1.34119222615329     float
B16NDATA 124648               int
B16NPAR  1911                 int
B17RCHI2 1.15500381389443     float
B17NDATA 128109               int
B17NPAR  1934                 int
B18RCHI2 1.17499129453445     float
B18NDATA 131860               int
B18NPAR  1955                 int
B19RCHI2 1.16358065447123     float
B19NDATA 133140               int
B19NPAR  1968                 int
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
