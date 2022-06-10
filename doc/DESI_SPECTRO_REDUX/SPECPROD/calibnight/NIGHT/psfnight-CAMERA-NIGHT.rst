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

.. collapse:: Required Header Keywords table

   .. rst-class:: keywords

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

.. collapse:: Required Header Keywords table

   .. rst-class:: keywords

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

.. collapse:: Required Header Keywords table

    .. rst-class:: keywords

    ======== ==================== ===== ===============================================
    KEY      Example Value        Type  Comment
    ======== ==================== ===== ===============================================
    NAXIS1   8016                 int   width of table in bytes
    NAXIS2   59                   int   number of rows in table
    PSFTYPE  GAUSS-HERMITE        str
    PSFVER   3                    str
    MJD      0                    int   MJD of arc lamp exposure
    PLATEID  0                    int   plate ID of arc lamp exposure
    CAMERA   &#x27;r9      &#x27; str   camera ID
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
    WAVEMIN  5546.0               float minimum wavelength (A), used for the Legendre p
    WAVEMAX  7835.0               float maximum wavelength (A), used for the Legendre p
    PSFERROR 0.0                  float assumed PSF fractional error in chi2
    READNOIS 0.0                  float assumed read out noise in chi2
    GAIN     1.0                  float assumed gain in chi2
    B00RCHI2 1.265121999136178    float best fit chi2/ndf for fiber bundle 0
    B00NDATA 140488               int   number of pixels in fit for fiber bundle 0
    B00NPAR  1746                 int   number of parameters in fit for fiber bundle 0
    B01RCHI2 1.244445290488158    float best fit chi2/ndf for fiber bundle 1
    B01NDATA 141467               int   number of pixels in fit for fiber bundle 1
    B01NPAR  1786                 int   number of parameters in fit for fiber bundle 1
    B02RCHI2 1.287672518525548    float best fit chi2/ndf for fiber bundle 2
    B02NDATA 142582               int   number of pixels in fit for fiber bundle 2
    B02NPAR  1802                 int   number of parameters in fit for fiber bundle 2
    B03RCHI2 1.297067743767708    float best fit chi2/ndf for fiber bundle 3
    B03NDATA 140419               int   number of pixels in fit for fiber bundle 3
    B03NPAR  1793                 int   number of parameters in fit for fiber bundle 3
    B04RCHI2 1.28304830748024     float best fit chi2/ndf for fiber bundle 4
    B04NDATA 138599               int   number of pixels in fit for fiber bundle 4
    B04NPAR  1785                 int   number of parameters in fit for fiber bundle 4
    B05RCHI2 1.269246986023668    float best fit chi2/ndf for fiber bundle 5
    B05NDATA 136603               int   number of pixels in fit for fiber bundle 5
    B05NPAR  1778                 int   number of parameters in fit for fiber bundle 5
    B06RCHI2 1.299512103689112    float best fit chi2/ndf for fiber bundle 6
    B06NDATA 137571               int   number of pixels in fit for fiber bundle 6
    B06NPAR  1807                 int   number of parameters in fit for fiber bundle 6
    B07RCHI2 1.347344727978646    float best fit chi2/ndf for fiber bundle 7
    B07NDATA 135041               int   number of pixels in fit for fiber bundle 7
    B07NPAR  1788                 int   number of parameters in fit for fiber bundle 7
    B08RCHI2 1.222211322234266    float best fit chi2/ndf for fiber bundle 8
    B08NDATA 130583               int   number of pixels in fit for fiber bundle 8
    B08NPAR  1737                 int   number of parameters in fit for fiber bundle 8
    B09RCHI2 1.283488581543704    float best fit chi2/ndf for fiber bundle 9
    B09NDATA 127868               int   number of pixels in fit for fiber bundle 9
    B09NPAR  1716                 int   number of parameters in fit for fiber bundle 9
    B10RCHI2 1.275975791937288    float best fit chi2/ndf for fiber bundle 10
    B10NDATA 131593               int   number of pixels in fit for fiber bundle 10
    B10NPAR  1770                 int   number of parameters in fit for fiber bundle 10
    B11RCHI2 1.250307604266956    float best fit chi2/ndf for fiber bundle 11
    B11NDATA 133944               int   number of pixels in fit for fiber bundle 11
    B11NPAR  1778                 int   number of parameters in fit for fiber bundle 11
    B12RCHI2 1.231315819103986    float best fit chi2/ndf for fiber bundle 12
    B12NDATA 134637               int   number of pixels in fit for fiber bundle 12
    B12NPAR  1767                 int   number of parameters in fit for fiber bundle 12
    B13RCHI2 1.238502289060944    float best fit chi2/ndf for fiber bundle 13
    B13NDATA 134287               int   number of pixels in fit for fiber bundle 13
    B13NPAR  1761                 int   number of parameters in fit for fiber bundle 13
    B14RCHI2 1.296845822866915    float best fit chi2/ndf for fiber bundle 14
    B14NDATA 139568               int   number of pixels in fit for fiber bundle 14
    B14NPAR  1818                 int   number of parameters in fit for fiber bundle 14
    B15RCHI2 1.319475598189398    float best fit chi2/ndf for fiber bundle 15
    B15NDATA 139759               int   number of pixels in fit for fiber bundle 15
    B15NPAR  1802                 int   number of parameters in fit for fiber bundle 15
    B16RCHI2 1.2373008163902      float best fit chi2/ndf for fiber bundle 16
    B16NDATA 139822               int   number of pixels in fit for fiber bundle 16
    B16NPAR  1778                 int   number of parameters in fit for fiber bundle 16
    B17RCHI2 1.262409294037498    float best fit chi2/ndf for fiber bundle 17
    B17NDATA 140633               int   number of pixels in fit for fiber bundle 17
    B17NPAR  1770                 int   number of parameters in fit for fiber bundle 17
    B18RCHI2 1.270007569982172    float best fit chi2/ndf for fiber bundle 18
    B18NDATA 143004               int   number of pixels in fit for fiber bundle 18
    B18NPAR  1790                 int   number of parameters in fit for fiber bundle 18
    B19RCHI2 1.275991847448398    float best fit chi2/ndf for fiber bundle 19
    B19NDATA 143320               int   number of pixels in fit for fiber bundle 19
    B19NPAR  1780                 int   number of parameters in fit for fiber bundle 19
    EXPID    0.0                  float
    ======== ==================== ===== ===============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

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
