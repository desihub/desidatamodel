===
psf
===

:Summary: PSF data.
:Naming Convention: ``psf-{ARM}.fits``, where ``{ARM}`` is one of 'b', 'r', 'z'.
:Regex: ``psf-[brz]\.fits``
:File Type: FITS, 23 MB

Contents
========

====== ======== ===== ===============================================
Number EXTNAME  Type  Contents
====== ======== ===== ===============================================
HDU0_  XCOEFF   IMAGE Legendre coeff for CCD x vs. wavelength
HDU1_  YCOEFF   IMAGE Legendre coeff for CCD y vs. wavelength
HDU2_  SPOTS    IMAGE Zemax PSF spots
HDU3_  SPOTX    IMAGE CCD x locations of spots
HDU4_  SPOTY    IMAGE CCD y locations of spots
HDU5_  FIBERPOS IMAGE Location of each fiber along slit
HDU6_  SPOTPOS  IMAGE Locations along slit where spots were generated
HDU7_  SPOTWAVE IMAGE Wavelength of generated spots
====== ======== ===== ===============================================

SPOTS[i,j] is 2D image[y,x] of Zemax spot on the CCD at SPOTX[j], SPOTY[i]
and along the slit at SPOTPOS[i] which is wavelength SPOTWAVE[i].

FITS Header Units
=================

HDU0
----

EXTNAME = XCOEFF

Legendre coeff for CCD x vs. wavelength.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============================= ===== =============================================
KEY      Example Value                 Type  Comment
======== ============================= ===== =============================================
NAXIS1   8                             int   length of data axis 1
NAXIS2   500                           int   length of data axis 2
EXTNAME  XCOEFF                        str
DATAMIN  1.175494350822e-38            float minimum allowed data value
DATAMAX  3.402823466385e+38            float maximum allowed data value
DATATYPE Normalized Image              str   Type of image
SPECTRO  DESI-0224-v1.ZMX (95% better) str
ARM      Red                           str   Spectrograph Arm
ARMINT   3                             int   Spectrograph Arm
WAVECENT 669.0                         float Center Wavelength (nm)
XCENT    6.159039977                   float Detector X Centroid (mm)
YCENT    -29.960402484                 float Detector Y Centroid (mm)
XDIRCOS  0.01699287200071              float x direction cosine
YDIRCOS  -0.9885050150412              float y direction cosine
ZDIRCOS  4.774490530784e-312           float z direction cosine
PIXSIZE  0.001                         float size of pixel (mm)
DIFFRACT T                             bool  diffraction added?
DETEFF   T                             bool  detector effects added?
PUPIL    126.5                         float Camera Pupil (mm)
FOCALLEN 215.0                         float Camera focal length (mm)
E2VFLAG  F                             bool  e2v detector
TEMP     175.0                         float Detector T (K)
DETSIG   5.0                           float sigma for detector (um)
DETTHICK 250.0                         float thickness of detector (um)
DATE     2013-09-12                    str   Date
CTYPE1   X                             str   X coordinate (mm)
CTYPE2   Y                             str   Y coordinate (mm)
CRPIX1   113.0                         float Reference X pixel
CRPIX2   113.0                         float Reference Y pixel
CRVAL1   6.158579827                   float Reference X value
CRVAL2   -29.961502809                 float Reference Y value
CDELT1   0.001                         float X pixel size (mm)
CDELT2   0.001                         float Y pixel size (mm)
PSFTYPE  SPOTGRID                      str   Grid of simulated PSF spots
NPIX_X   4114                          int   Number of CCD pixels in X direction
NPIX_Y   4128                          int   Number of CCD pixels in Y direction
NSPEC    500                           int   Number of spectra
NWAVE    11                            int   Number of wavelength samples
CCDPIXSZ 0.015                         float CCD pixel size [mm]
DFIBER   0.23                          float Center-to-center pitch of fibers on slit [mm]
DGROUP   0.556                         float Spacing between fiber groups on slit [mm]
NGROUPS  20                            int   Number of fiber groups per slit
NFIBGRP  25                            int   Number of fibers per group
WAVEMIN  5564                          int   Min wavelength for Legendre domain [-1,1]
WAVEMAX  7805                          int   Max wavelength for Legendre domain [-1,1]
WMIN_ALL 5625                          int   Min wavelength seen by all spectra [Ang]
WMAX_ALL 7741                          int   Max wavelength seen by all spectra [Ang]
======== ============================= ===== =============================================

Data: FITS image [float64, 8x500]

HDU1
----

EXTNAME = YCOEFF

Legendre coeff for CCD y vs. wavelength.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============= ==== ========================================
KEY      Example Value Type Comment
======== ============= ==== ========================================
NAXIS1   8             int  length of data axis 1
NAXIS2   500           int  length of data axis 2
EXTNAME  YCOEFF        str
WAVEMIN  5564          int  Min wavelength on the CCD [Ang]
WAVEMAX  7805          int  Max wavelength on the CCD [Ang]
WMIN_ALL 5625          int  Min wavelength seen by all spectra [Ang]
WMAX_ALL 7741          int  Max wavelength seen by all spectra [Ang]
======== ============= ==== ========================================

Data: FITS image [float64, 8x500]

HDU2
----

EXTNAME = SPOTS

Zemax simulated spots.

SPOTS[i,j] is 2D image[y,x] of Zemax spot on the CCD at SPOTX[j], SPOTY[i]
and along the slit at SPOTPOS[i] which is wavelength SPOTWAVE[i].

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ============= ==== =====================
KEY     Example Value Type Comment
======= ============= ==== =====================
NAXIS1  225           int  length of data axis 1
NAXIS2  225           int  length of data axis 2
NAXIS3  11            int  length of data axis 3
NAXIS4  11            int  length of data axis 4
EXTNAME SPOTS         str
======= ============= ==== =====================

Data: FITS image [float32, 225x225x11x11]

HDU3
----

EXTNAME = SPOTX

X locations of spots.

SPOTS[i,j] is 2D image[y,x] of Zemax spot on the CCD at SPOTX[j], SPOTY[i]
and along the slit at SPOTPOS[i] which is wavelength SPOTWAVE[i].

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ============= ==== =====================
KEY     Example Value Type Comment
======= ============= ==== =====================
NAXIS1  11            int  length of data axis 1
NAXIS2  11            int  length of data axis 2
EXTNAME SPOTX         str
======= ============= ==== =====================

Data: FITS image [float32, 11x11]

HDU4
----

EXTNAME = SPOTY

Y locations of spots.

SPOTS[i,j] is 2D image[y,x] of Zemax spot on the CCD at SPOTX[j], SPOTY[i]
and along the slit at SPOTPOS[i] which is wavelength SPOTWAVE[i].

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ============= ==== =====================
KEY     Example Value Type Comment
======= ============= ==== =====================
NAXIS1  11            int  length of data axis 1
NAXIS2  11            int  length of data axis 2
EXTNAME SPOTY         str
======= ============= ==== =====================

Data: FITS image [float32, 11x11]

HDU5
----

EXTNAME = FIBERPOS

Location along the slit of each fiber.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ============= ==== =====================
KEY     Example Value Type Comment
======= ============= ==== =====================
NAXIS1  500           int  length of data axis 1
EXTNAME FIBERPOS      str
======= ============= ==== =====================

Data: FITS image [float64, 500]

HDU6
----

EXTNAME = SPOTPOS

Location along the slit of each spot.

SPOTS[i,j] is 2D image[y,x] of Zemax spot on the CCD at SPOTX[j], SPOTY[i]
and along the slit at SPOTPOS[i] which is wavelength SPOTWAVE[i].

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ============= ==== =====================
KEY     Example Value Type Comment
======= ============= ==== =====================
NAXIS1  11            int  length of data axis 1
EXTNAME SPOTPOS       str
======= ============= ==== =====================

Data: FITS image [float64, 11]

HDU7
----

EXTNAME = SPOTWAVE

Wavelengths at which each spot was measured.

SPOTS[i,j] is 2D image[y,x] of Zemax spot on the CCD at SPOTX[j], SPOTY[i]
and along the slit at SPOTPOS[i] which is wavelength SPOTWAVE[i].

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ============= ==== =====================
KEY     Example Value Type Comment
======= ============= ==== =====================
NAXIS1  11            int  length of data axis 1
EXTNAME SPOTWAVE      str
======= ============= ==== =====================

Data: FITS image [float64, 11]


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
