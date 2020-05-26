========
psfnight
========

:Summary: PSF model for the night derived from combining multiple
          arc lamp calibration exposures.
:Naming Convention: ``psfnight-CAMERA-NIGHT.fits``, where ``CAMERA`` is
    *e.g.*, "b0", "r5", etc. and ``NIGHT`` is the observation night in
    YYYYMMDD format.
:Regex: ``psfnight-[brz][0-9]-[0-9]{8}.fits``
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
B00RCHI2 1.84975520965803     float best fit chi2/ndf for fiber bundle 0
B00NDATA 206699               int   number of pixels in fit for fiber bundle 0
B00NPAR  2798                 int   number of parameters in fit for fiber bundle 0
B01RCHI2 1.91929795474055     float best fit chi2/ndf for fiber bundle 1
B01NDATA 208829               int   number of pixels in fit for fiber bundle 1
B01NPAR  2849                 int   number of parameters in fit for fiber bundle 1
B02RCHI2 1.842735255276405    float best fit chi2/ndf for fiber bundle 2
B02NDATA 205198               int   number of pixels in fit for fiber bundle 2
B02NPAR  2825                 int   number of parameters in fit for fiber bundle 2
B03RCHI2 1.849946668156615    float best fit chi2/ndf for fiber bundle 3
B03NDATA 204885               int   number of pixels in fit for fiber bundle 3
B03NPAR  2835                 int   number of parameters in fit for fiber bundle 3
B04RCHI2 1.984298163449575    float best fit chi2/ndf for fiber bundle 4
B04NDATA 204077               int   number of pixels in fit for fiber bundle 4
B04NPAR  2864                 int   number of parameters in fit for fiber bundle 4
B05RCHI2 1.99761138022869     float best fit chi2/ndf for fiber bundle 5
B05NDATA 204185               int   number of pixels in fit for fiber bundle 5
B05NPAR  2872                 int   number of parameters in fit for fiber bundle 5
B06RCHI2 1.92259821135567     float best fit chi2/ndf for fiber bundle 6
B06NDATA 200559               int   number of pixels in fit for fiber bundle 6
B06NPAR  2852                 int   number of parameters in fit for fiber bundle 6
B07RCHI2 1.901096426001315    float best fit chi2/ndf for fiber bundle 7
B07NDATA 197662               int   number of pixels in fit for fiber bundle 7
B07NPAR  2856                 int   number of parameters in fit for fiber bundle 7
B08RCHI2 1.965604142967395    float best fit chi2/ndf for fiber bundle 8
B08NDATA 196749               int   number of pixels in fit for fiber bundle 8
B08NPAR  2883                 int   number of parameters in fit for fiber bundle 8
B09RCHI2 1.999804791865025    float best fit chi2/ndf for fiber bundle 9
B09NDATA 195995               int   number of pixels in fit for fiber bundle 9
B09NPAR  2883                 int   number of parameters in fit for fiber bundle 9
B10RCHI2 1.8555853188554      float best fit chi2/ndf for fiber bundle 10
B10NDATA 193620               int   number of pixels in fit for fiber bundle 10
B10NPAR  2862                 int   number of parameters in fit for fiber bundle 10
B11RCHI2 1.888476788326665    float best fit chi2/ndf for fiber bundle 11
B11NDATA 194212               int   number of pixels in fit for fiber bundle 11
B11NPAR  2861                 int   number of parameters in fit for fiber bundle 11
B12RCHI2 1.974525824769095    float best fit chi2/ndf for fiber bundle 12
B12NDATA 199172               int   number of pixels in fit for fiber bundle 12
B12NPAR  2881                 int   number of parameters in fit for fiber bundle 12
B13RCHI2 2.033594251609805    float best fit chi2/ndf for fiber bundle 13
B13NDATA 200026               int   number of pixels in fit for fiber bundle 13
B13NPAR  2876                 int   number of parameters in fit for fiber bundle 13
B14RCHI2 1.922152754141425    float best fit chi2/ndf for fiber bundle 14
B14NDATA 199229               int   number of pixels in fit for fiber bundle 14
B14NPAR  2844                 int   number of parameters in fit for fiber bundle 14
B15RCHI2 1.926621814264785    float best fit chi2/ndf for fiber bundle 15
B15NDATA 204006               int   number of pixels in fit for fiber bundle 15
B15NPAR  2866                 int   number of parameters in fit for fiber bundle 15
B16RCHI2 1.93840857000781     float best fit chi2/ndf for fiber bundle 16
B16NDATA 208641               int   number of pixels in fit for fiber bundle 16
B16NPAR  2892                 int   number of parameters in fit for fiber bundle 16
B17RCHI2 1.924174403095215    float best fit chi2/ndf for fiber bundle 17
B17NDATA 208344               int   number of pixels in fit for fiber bundle 17
B17NPAR  2876                 int   number of parameters in fit for fiber bundle 17
B18RCHI2 1.83979514536894     float best fit chi2/ndf for fiber bundle 18
B18NDATA 193848               int   number of pixels in fit for fiber bundle 18
B18NPAR  2643                 int   number of parameters in fit for fiber bundle 18
B19RCHI2 1.788328121547175    float best fit chi2/ndf for fiber bundle 19
B19NDATA 208202               int   number of pixels in fit for fiber bundle 19
B19NPAR  2819                 int   number of parameters in fit for fiber bundle 19
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
