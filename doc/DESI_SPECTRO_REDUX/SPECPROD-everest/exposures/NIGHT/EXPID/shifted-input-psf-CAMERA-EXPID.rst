=======
shifted
=======

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``shifted-input-psf-b3-00091227.fits``, where ... *Give a human readable
    description of the filename, e.g. ``blat-{EXPID}`` where ``{EXPID}``
    is the 8-digit exposure ID.*
:Regex: ``shifted-input-psf-b3-00091227.fits`` *Give a regular expression for this filename.
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
WAVEMIN  3517.0        float
WAVEMAX  6030.0        float
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
WAVEMIN  3517.0        float
WAVEMAX  6030.0        float
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
CAMERA   &#x27;b3      &#x27;                                        str   camera ID
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
WAVEMIN  3517.0                                                      float minimum wavelength (A), used for the Legendre p
WAVEMAX  6031.0                                                      float maximum wavelength (A), used for the Legendre p
PSFERROR 0.0                                                         float assumed PSF fractional error in chi2
READNOIS 0.0                                                         float assumed read out noise in chi2
GAIN     1.0                                                         float assumed gain in chi2
B00RCHI2 1.40294942889583                                            float best fit chi2/ndf for fiber bundle 0
B00NDATA 68264                                                       int   number of pixels in fit for fiber bundle 0
B00NPAR  946                                                         int   number of parameters in fit for fiber bundle 0
B01RCHI2 1.733095250638646                                           float
B01NDATA 67711                                                       int
B01NPAR  939                                                         int
B02RCHI2 1.4699840748889                                             float
B02NDATA 66087                                                       int
B02NPAR  919                                                         int
B03RCHI2 1.42275622559437                                            float
B03NDATA 65868                                                       int
B03NPAR  918                                                         int
B04RCHI2 1.312931953858558                                           float
B04NDATA 64018                                                       int
B04NPAR  892                                                         int
B05RCHI2 1.440825880630306                                           float
B05NDATA 63405                                                       int
B05NPAR  907                                                         int
B06RCHI2 1.354313557635046                                           float
B06NDATA 64061                                                       int
B06NPAR  932                                                         int
B07RCHI2 1.391987340930202                                           float
B07NDATA 63789                                                       int
B07NPAR  915                                                         int
B08RCHI2 1.362763163095464                                           float
B08NDATA 66363                                                       int
B08NPAR  949                                                         int
B09RCHI2 1.385725468778914                                           float
B09NDATA 62479                                                       int
B09NPAR  888                                                         int
B10RCHI2 1.243421166764708                                           float
B10NDATA 63339                                                       int
B10NPAR  910                                                         int
B11RCHI2 1.258784161214062                                           float
B11NDATA 66930                                                       int
B11NPAR  957                                                         int
B12RCHI2 1.301293580506404                                           float
B12NDATA 69148                                                       int
B12NPAR  1000                                                        int
B13RCHI2 1.340729434224558                                           float
B13NDATA 69267                                                       int
B13NPAR  983                                                         int
B14RCHI2 1.352119348188448                                           float
B14NDATA 67459                                                       int
B14NPAR  924                                                         int
B15RCHI2 1.322737519633258                                           float
B15NDATA 68172                                                       int
B15NPAR  958                                                         int
B16RCHI2 1.37980409702169                                            float
B16NDATA 67306                                                       int
B16NPAR  955                                                         int
B17RCHI2 1.444266966121702                                           float
B17NDATA 68477                                                       int
B17NPAR  966                                                         int
B18RCHI2 1.398522623578382                                           float
B18NDATA 69522                                                       int
B18NPAR  957                                                         int
B19RCHI2 1.451212719697346                                           float
B19NDATA 67876                                                       int
B19NPAR  955                                                         int
EXPID    0.0                                                         float
MEANDX   0.6392934280476198                                          float
MINDX    0.6392934280438567                                          float
MAXDX    0.6392934280620466                                          float
MEANDY   -0.3037226950397474                                         float
MINDY    -0.3037226950441436                                         float
MAXDY    -0.3037226950327749                                         float
IN_PSF   SPCALIB/spec/sm6/psfnight-b3-20201214.fits                  str
IN_IMAGE SPECPROD/preproc/20210605/00091227/preproc-b3-00091227.fits str
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
