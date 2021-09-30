===
psf
===

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``psf-b6-00087725.fits``, where ... *Give a human readable
    description of the filename, e.g. ``blat-{EXPID}`` where ``{EXPID}``
    is the 8-digit exposure ID.*
:Regex: ``psf-b6-00087725.fits`` *Give a regular expression for this filename.
    For example, a six-digit number would correspond to ``[0-9]{6}``.*
:File Type: FITS, 540 KB  *This section gives the type of the file
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
WAVEMIN  3509.0        float
WAVEMAX  5993.0        float
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
WAVEMIN  3509.0        float
WAVEMAX  5993.0        float
======== ============= ===== =====================

Data: FITS image [float64, 7x500]

HDU2
----

EXTNAME = PSF

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== =========================================================== ===== ===============================================
KEY      Example Value                                               Type  Comment
======== =========================================================== ===== ===============================================
NAXIS1   8016                                                        int   width of table in bytes
NAXIS2   59                                                          int   number of rows in table
PSFTYPE  GAUSS-HERMITE                                               str
PSFVER   3                                                           str
MJD      0                                                           int   MJD of arc lamp exposure
PLATEID  0                                                           int   plate ID of arc lamp exposure
CAMERA   &#x27;b6      &#x27;                                        str   camera ID
ARCEXP   0                                                           int   ID of arc lamp exposure used to fit PSF
NPIX_X   4096                                                        int   number of columns in input CCD image
NPIX_Y   4096                                                        int   number of rows in input CCD image
HSIZEX   8                                                           int   Half size of PSF in fit, NX=2*HSIZEX+1
HSIZEY   5                                                           int   Half size of PSF in fit, NY=2*HSIZEY+1
FIBERMIN 0                                                           int   first fiber (starting at 0)
FIBERMAX 499                                                         int   last fiber (included)
NPARAMS  57                                                          int   number of PSF parameters
LEGDEG   1                                                           int   degree of Legendre pol.(wave) for parameters
GHDEGX   6                                                           int   degree of Hermite polynomial along CCD columns
GHDEGY   6                                                           int   degree of Hermite polynomial along CCD rows
WAVEMIN  3509.0                                                      float minimum wavelength (A), used for the Legendre p
WAVEMAX  5994.0                                                      float maximum wavelength (A), used for the Legendre p
PSFERROR 0.0                                                         float assumed PSF fractional error in chi2
READNOIS 0.0                                                         float assumed read out noise in chi2
GAIN     1.0                                                         float assumed gain in chi2
B00RCHI2 1.836984215992436                                           float best fit chi2/ndf for fiber bundle 0
B00NDATA 63016                                                       int   number of pixels in fit for fiber bundle 0
B00NPAR  873                                                         int   number of parameters in fit for fiber bundle 0
B01RCHI2 1.450455309972844                                           float
B01NDATA 62504                                                       int
B01NPAR  879                                                         int
B02RCHI2 1.501777577771852                                           float
B02NDATA 60329                                                       int
B02NPAR  856                                                         int
B03RCHI2 1.353098341326042                                           float
B03NDATA 60612                                                       int
B03NPAR  837                                                         int
B04RCHI2 1.393846212264994                                           float
B04NDATA 61688                                                       int
B04NPAR  883                                                         int
B05RCHI2 1.353290927482766                                           float
B05NDATA 63799                                                       int
B05NPAR  898                                                         int
B06RCHI2 1.327607557289588                                           float
B06NDATA 63843                                                       int
B06NPAR  909                                                         int
B07RCHI2 1.299438519087348                                           float
B07NDATA 63082                                                       int
B07NPAR  915                                                         int
B08RCHI2 1.305195528095314                                           float
B08NDATA 61735                                                       int
B08NPAR  889                                                         int
B09RCHI2 1.34726304555094                                            float
B09NDATA 65711                                                       int
B09NPAR  938                                                         int
B10RCHI2 1.418991389158124                                           float
B10NDATA 63740                                                       int
B10NPAR  910                                                         int
B11RCHI2 1.425152100838912                                           float
B11NDATA 64365                                                       int
B11NPAR  920                                                         int
B12RCHI2 1.414957751949352                                           float
B12NDATA 66931                                                       int
B12NPAR  943                                                         int
B13RCHI2 1.408107653346664                                           float
B13NDATA 65489                                                       int
B13NPAR  927                                                         int
B14RCHI2 1.456124250925412                                           float
B14NDATA 64266                                                       int
B14NPAR  912                                                         int
B15RCHI2 1.439404607933888                                           float
B15NDATA 62426                                                       int
B15NPAR  864                                                         int
B16RCHI2 1.509295084838608                                           float
B16NDATA 66132                                                       int
B16NPAR  919                                                         int
B17RCHI2 1.572693713816206                                           float
B17NDATA 62162                                                       int
B17NPAR  872                                                         int
B18RCHI2 1.50754203874392                                            float
B18NDATA 60629                                                       int
B18NPAR  858                                                         int
B19RCHI2 1.48766354972339                                            float
B19NDATA 59069                                                       int
B19NPAR  834                                                         int
EXPID    0.0                                                         float
MEANDX   0.1791090517729592                                          float
MINDX    0.1393103124719346                                          float
MAXDX    0.2034368166544596                                          float
MEANDY   -0.0711518168437059                                         float
MINDY    -0.2412226803392059                                         float
MAXDY    0.3326411714624555                                          float
IN_PSF   SPECPROD/calibnight/20210508/psfnight-b6-20210508.fits      str
IN_IMAGE SPECPROD/preproc/20210508/00087725/preproc-b6-00087725.fits str
======== =========================================================== ===== ===============================================

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
