===
fit
===

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``fit-psf-before-listed-fix-b0-00085370.fits``, where ... *Give a human readable
    description of the filename, e.g. ``blat-{EXPID}`` where ``{EXPID}``
    is the 8-digit exposure ID.*
:Regex: ``fit-psf-before-listed-fix-b0-00085370.fits`` *Give a regular expression for this filename.
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
WAVEMIN  3518.0        float
WAVEMAX  5990.0        float
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
WAVEMIN  3518.0        float
WAVEMAX  5990.0        float
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
CAMERA   &#x27;b0      &#x27; str   camera ID
ARCEXP   0                    int   ID of arc lamp exposure used to fit PSF
NPIX_X   4096                 int   number of columns in input CCD image
NPIX_Y   4096                 int   number of rows in input CCD image
HSIZEX   8                    int   Half size of PSF in fit, NX=2*HSIZEX+1
HSIZEY   5                    int   Half size of PSF in fit, NY=2*HSIZEY+1
FIBERMIN 0                    int   first fiber (starting at 0)
FIBERMAX 499                  int   last fiber (included)
NPARAMS  57                   int   number of PSF parameters
LEGDEG   1                    int   degree of Legendre pol.(wave) for parameters
GHDEGX   6                    int   degree of Hermite polynomial along CCD columns
GHDEGY   6                    int   degree of Hermite polynomial along CCD rows
WAVEMIN  3518.0               float minimum wavelength (A), used for the Legendre p
WAVEMAX  5991.0               float maximum wavelength (A), used for the Legendre p
PSFERROR 0.0                  float assumed PSF fractional error in chi2
READNOIS 0.0                  float assumed read out noise in chi2
GAIN     1.0                  float assumed gain in chi2
B00RCHI2 1.42824068505651     float best fit chi2/ndf for fiber bundle 0
B00NDATA 60750                int   number of pixels in fit for fiber bundle 0
B00NPAR  837                  int   number of parameters in fit for fiber bundle 0
B01RCHI2 1.33305200083454     float best fit chi2/ndf for fiber bundle 1
B01NDATA 63035                int   number of pixels in fit for fiber bundle 1
B01NPAR  879                  int   number of parameters in fit for fiber bundle 1
B02RCHI2 1.34683423886548     float best fit chi2/ndf for fiber bundle 2
B02NDATA 58815                int   number of pixels in fit for fiber bundle 2
B02NPAR  834                  int   number of parameters in fit for fiber bundle 2
B03RCHI2 1.2885724137343      float best fit chi2/ndf for fiber bundle 3
B03NDATA 61373                int   number of pixels in fit for fiber bundle 3
B03NPAR  871                  int   number of parameters in fit for fiber bundle 3
B04RCHI2 1.29663983853049     float best fit chi2/ndf for fiber bundle 4
B04NDATA 63311                int   number of pixels in fit for fiber bundle 4
B04NPAR  899                  int   number of parameters in fit for fiber bundle 4
B05RCHI2 1.29840534644784     float best fit chi2/ndf for fiber bundle 5
B05NDATA 64046                int   number of pixels in fit for fiber bundle 5
B05NPAR  910                  int   number of parameters in fit for fiber bundle 5
B06RCHI2 1.28051063154453     float best fit chi2/ndf for fiber bundle 6
B06NDATA 62233                int   number of pixels in fit for fiber bundle 6
B06NPAR  877                  int   number of parameters in fit for fiber bundle 6
B07RCHI2 1.42477247164795     float best fit chi2/ndf for fiber bundle 7
B07NDATA 60656                int   number of pixels in fit for fiber bundle 7
B07NPAR  866                  int   number of parameters in fit for fiber bundle 7
B08RCHI2 1.24380164636569     float best fit chi2/ndf for fiber bundle 8
B08NDATA 61861                int   number of pixels in fit for fiber bundle 8
B08NPAR  887                  int   number of parameters in fit for fiber bundle 8
B09RCHI2 1.23391166138797     float best fit chi2/ndf for fiber bundle 9
B09NDATA 61939                int   number of pixels in fit for fiber bundle 9
B09NPAR  895                  int   number of parameters in fit for fiber bundle 9
B10RCHI2 1.28758717165365     float best fit chi2/ndf for fiber bundle 10
B10NDATA 64702                int   number of pixels in fit for fiber bundle 10
B10NPAR  940                  int   number of parameters in fit for fiber bundle 10
B11RCHI2 1.28594140793397     float best fit chi2/ndf for fiber bundle 11
B11NDATA 65271                int   number of pixels in fit for fiber bundle 11
B11NPAR  945                  int   number of parameters in fit for fiber bundle 11
B12RCHI2 1.24151177166137     float best fit chi2/ndf for fiber bundle 12
B12NDATA 63222                int   number of pixels in fit for fiber bundle 12
B12NPAR  900                  int   number of parameters in fit for fiber bundle 12
B13RCHI2 1.26267347694333     float best fit chi2/ndf for fiber bundle 13
B13NDATA 61638                int   number of pixels in fit for fiber bundle 13
B13NPAR  877                  int   number of parameters in fit for fiber bundle 13
B14RCHI2 1.38044457999712     float best fit chi2/ndf for fiber bundle 14
B14NDATA 62336                int   number of pixels in fit for fiber bundle 14
B14NPAR  870                  int   number of parameters in fit for fiber bundle 14
B15RCHI2 1.39382994920686     float best fit chi2/ndf for fiber bundle 15
B15NDATA 64062                int   number of pixels in fit for fiber bundle 15
B15NPAR  906                  int   number of parameters in fit for fiber bundle 15
B16RCHI2 1.39051144900517     float best fit chi2/ndf for fiber bundle 16
B16NDATA 65206                int   number of pixels in fit for fiber bundle 16
B16NPAR  924                  int   number of parameters in fit for fiber bundle 16
B17RCHI2 1.39866539357759     float best fit chi2/ndf for fiber bundle 17
B17NDATA 66418                int   number of pixels in fit for fiber bundle 17
B17NPAR  946                  int   number of parameters in fit for fiber bundle 17
B18RCHI2 1.83068069195406     float best fit chi2/ndf for fiber bundle 18
B18NDATA 63657                int   number of pixels in fit for fiber bundle 18
B18NPAR  884                  int   number of parameters in fit for fiber bundle 18
B19RCHI2 1.89762061043448     float best fit chi2/ndf for fiber bundle 19
B19NDATA 61188                int   number of pixels in fit for fiber bundle 19
B19NPAR  857                  int   number of parameters in fit for fiber bundle 19
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
