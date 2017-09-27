=================
simpix
=================

General Description
===================

Summary
-------

simpix files contain the noiseless CCD pixel image.
The corresponding pix-\*.fits files contain the noisy realization of this
image like the real data would see.  It optionally contains the x and y
trace locations vs. wavelength.

Naming Convention
-----------------

``simpix-{CAMERA}-{EXPID}.fits``, where ``{CAMERA}`` is the spectrograph
camera, e.g. b0, r1, z9; and ``{EXPID}`` is the 8-digit exposure ID.

regex: ``simpix-[brz][0-9]{1}-[0-9]{8}.fits``

File Type
---------

FITS, 128 MB
Contents
========

====== ========= ===== ===================
Number EXTNAME   Type  Contents
====== ========= ===== ===================
HDU0_  ELECTRONS IMAGE Noiseless simulated image
HDU1_  XCOEFF    IMAGE Optional: Legendre coefficients for x vs. wavelength
HDU2_  YCOEFF    IMAGE Optional: Legendre coefficients for y vs. wavelength
====== ========= ===== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = ELECTRONS

Noiseless simulated image in electrons

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============= ==== =====================
KEY      Example Value Type Comment
======== ============= ==== =====================
NAXIS1   4096          int  Number of pixels in y (wavelength direction)
NAXIS2   4096          int  Number of pixels in x (fiber direction)
VSPECTER 0.0.0         str  Specter version used to simulate this image
======== ============= ==== =====================

HDU1
----

EXTNAME = XCOEFF

Legendre coefficients to describe the spectral trace x vs. wavelength.

To evaluate, convert the wavelength in Angstroms to the domain [-1,1]
using WAVEMIN and WAVEMAX, and then evaluate the Legendre polynomial::

    w = 2*(wavelength - WAVEMIN) / (WAVEMAX - WAVEMIN) - 1.0
    x = numpy.polynomial.legval(w, xcoeff[i])

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

Most keywords are inherited from the input PSF, which inherited them from
the input Zemax spot files.

======== ================================ ===== =============================================
KEY      Example Value                    Type  Comment
======== ================================ ===== =============================================
NAXIS1   8                                int   Number of Legendre coefficients
NAXIS2   500                              int   Number of spectra
EXTNAME  XCOEFF                           str
DATAMIN  1.17549435082e-38                float minimum allowed data value
DATAMAX  3.40282346638e+38                float maximum allowed data value
DATATYPE Normalized Image                 str   Type of image
SPECTRO  DESI-0224-v1.ZMX(95% are better) str
ARM      Blue                             str   Spectrograph Arm
ARMINT   1                                int   Spectrograph Arm
WAVECENT 476.5                            float Center Wavelength (nm)
XCENT    5.379251126                      float Detector X Centroid (mm)
YCENT    -29.956071488                    float Detector Y Centroid (mm)
XDIRCOS  -0.0353851399911                 float x direction cosine
YDIRCOS  -0.976475545755                  float y direction cosine
ZDIRCOS  4.77449053078e-312               float z direction cosine
PIXSIZE  0.001                            float size of pixel (mm)
DIFFRACT T                                bool  diffraction added?
DETEFF   T                                bool  detector effects added?
PUPIL    126.5                            float Camera Pupil (mm)
FOCALLEN 215.0                            float Camera focal length (mm)
E2VFLAG  T                                bool  e2v detector
TEMP     175.0                            float Detector T (K)
DETSIG   5.0                              float sigma for detector (um)
DETTHICK 0.0                              float thickness of detector (um)
DATE     2013-09-12                       str   Date
CTYPE1   X                                str   X coordinate (mm)
CTYPE2   Y                                str   Y coordinate (mm)
CRPIX1   113.0                            float Reference X pixel
CRPIX2   113.0                            float Reference Y pixel
CRVAL1   5.380413942                      float Reference X value
CRVAL2   -29.95920258                     float Reference Y value
CDELT1   0.001                            float X pixel size (mm)
CDELT2   0.001                            float Y pixel size (mm)
PSFTYPE  SPOTGRID                         str   Grid of simulated PSF spots
NPIX_X   4096                             int   Number of CCD pixels in X direction
NPIX_Y   4096                             int   Number of CCD pixels in Y direction
NSPEC    500                              int   Number of spectra
NWAVE    11                               int   Number of wavelength samples
CCDPIXSZ 0.015                            float CCD pixel size [mm]
DFIBER   0.23                             float Center-to-center pitch of fibers on slit [mm]
DGROUP   0.556                            float Spacing between fiber groups on slit [mm]
NGROUPS  20                               int   Number of fiber groups per slit
NFIBGRP  25                               int   Number of fibers per group
WAVEMIN  3533                             int   Min wavelength for Legendre domain [-1,1]
WAVEMAX  5998                             int   Max wavelength for Legendre domain [-1,1]
WMIN_ALL 3569                             int   Min wavelength seen by all spectra [Ang]
WMAX_ALL 5949                             int   Max wavelength seen by all spectra [Ang]
======== ================================ ===== =============================================

Data: FITS image [float64]

HDU2
----

EXTNAME = YCOEFF

Legendre coefficients to describe the spectral trace y vs. wavelength.
See the description in HDU1 for how to evaluate these.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============= ==== ========================================
KEY      Example Value Type Comment
======== ============= ==== ========================================
NAXIS1   8             int
NAXIS2   500           int
EXTNAME  YCOEFF        str
WAVEMIN  3533          int  Min wavelength on the CCD [Ang]
WAVEMAX  5998          int  Max wavelength on the CCD [Ang]
WMIN_ALL 3569          int  Min wavelength seen by all spectra [Ang]
WMAX_ALL 5949          int  Max wavelength seen by all spectra [Ang]
======== ============= ==== ========================================

Data: FITS image [float64]


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
