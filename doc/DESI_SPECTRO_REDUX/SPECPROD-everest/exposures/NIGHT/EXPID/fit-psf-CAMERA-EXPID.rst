===
fit
===

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``fit-psf-r7-00079816.fits``, where ... *Give a human readable
    description of the filename, e.g. ``blat-{EXPID}`` where ``{EXPID}``
    is the 8-digit exposure ID.*
:Regex: ``fit-psf-r7-00079816.fits`` *Give a regular expression for this filename.
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
WAVEMIN  5545.0        float
WAVEMAX  7838.0        float
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
WAVEMIN  5545.0        float
WAVEMAX  7838.0        float
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
CAMERA   &#x27;r7      &#x27; str   camera ID
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
WAVEMIN  5545.0               float minimum wavelength (A), used for the Legendre p
WAVEMAX  7839.0               float maximum wavelength (A), used for the Legendre p
PSFERROR 0.0                  float assumed PSF fractional error in chi2
READNOIS 0.0                  float assumed read out noise in chi2
GAIN     1.0                  float assumed gain in chi2
B00RCHI2 4.19638602204035     float best fit chi2/ndf for fiber bundle 0
B00NDATA 128599               int   number of pixels in fit for fiber bundle 0
B00NPAR  1517                 int   number of parameters in fit for fiber bundle 0
B01RCHI2 1.27924798035216     float
B01NDATA 133628               int
B01NPAR  1676                 int
B02RCHI2 1.3446802329037      float
B02NDATA 127433               int
B02NPAR  1624                 int
B03RCHI2 1.29507856928009     float
B03NDATA 129352               int
B03NPAR  1603                 int
B04RCHI2 1.26368221361041     float
B04NDATA 126860               int
B04NPAR  1639                 int
B05RCHI2 1.24305919663926     float
B05NDATA 125840               int
B05NPAR  1583                 int
B06RCHI2 1.28465818626954     float
B06NDATA 128183               int
B06NPAR  1675                 int
B07RCHI2 1.28814571022934     float
B07NDATA 124931               int
B07NPAR  1653                 int
B08RCHI2 1.33903607484854     float
B08NDATA 124208               int
B08NPAR  1660                 int
B09RCHI2 1.92174885989951     float
B09NDATA 122948               int
B09NPAR  1663                 int
B10RCHI2 1.25508531307669     float
B10NDATA 122365               int
B10NPAR  1636                 int
B11RCHI2 1.40041933965708     float
B11NDATA 121000               int
B11NPAR  1634                 int
B12RCHI2 1.28290670031963     float
B12NDATA 123661               int
B12NPAR  1641                 int
B13RCHI2 1.28605600973873     float
B13NDATA 124279               int
B13NPAR  1638                 int
B14RCHI2 1.30201724639237     float
B14NDATA 127740               int
B14NPAR  1663                 int
B15RCHI2 1.28460756119231     float
B15NDATA 129716               int
B15NPAR  1666                 int
B16RCHI2 1.23906244448262     float
B16NDATA 128418               int
B16NPAR  1590                 int
B17RCHI2 1.36125706589826     float
B17NDATA 130010               int
B17NPAR  1642                 int
B18RCHI2 1.33951572272939     float
B18NDATA 133169               int
B18NPAR  1667                 int
B19RCHI2 1.51090664478632     float
B19NDATA 132927               int
B19NPAR  1653                 int
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
