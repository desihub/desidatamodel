====================
psfboot-CAMERA-EXPID
====================

:Summary: psfboot file.
:Naming Convention: ``psfboot-CAMERA-EXPID.fits``, where ``CAMERA`` is *e.g.*,
    "b0", "r1", "z2", and ``EXPID`` is an 8 digit exposure number.
:Regex: ``psfboot-[brz][0-9]-[0-9]{8}\.fits``
:File Type: FITS, 64 KB

This file is a first fit to the x vs. y vs. wavelength solutions and
the mean Gaussian sigma wavelength dispersion per fiber.  It is used as
a starting point for more refined fits.

Contents
========

====== ======= ===== ==========================================
Number EXTNAME Type  Contents
====== ======= ===== ==========================================
HDU0_  COEFFX  IMAGE Legendre coefficients for x vs. wavelength
HDU1_  COEFFY  IMAGE Legendre coefficients for y vs. wavelength
HDU2_  SIGMA   IMAGE Gaussian sigma per fiber
====== ======= ===== ==========================================


FITS Header Units
=================

HDU0
----

EXTNAME = COEFFX

Legendre coefficients for x vs. wavelength.  Header keywords
WAVEMIN and WAVEMAX provide the mapping from wavelength to the
[-1,1] domain used for the Legenre polynomials.  i.e. starting
with wavelength w::

    wx = 2.0*(w-WAVEMIN)/(WAVEMAX-WAVEMIN) - 1.0  #- Map to [-1,1]
    x[i] = Sum_j XCOEFF[i,j] L_j(wx)              #- evaluate Legendre series

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ============= ===== ===============================
KEY     Example Value Type  Comment
======= ============= ===== ===============================
NAXIS1  6             int   Number of Legendre coefficients
NAXIS2  500           int   Number of spectra
WAVEMIN 5563.41034186 float
WAVEMAX 7807.04444877 float
======= ============= ===== ===============================

Data: FITS image [float64, 6x500]

HDU1
----

EXTNAME = COEFFY

Legendre coefficients for y vs. wavelength; see the HDU0 description
for how to interpret these.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ============= ===== ===============================
KEY     Example Value Type  Comment
======= ============= ===== ===============================
NAXIS1  6             int   Number of Legendre coefficients
NAXIS2  500           int   Number of spectra
WAVEMIN 5563.41034186 float
WAVEMAX 7807.04444877 float
======= ============= ===== ===============================

Data: FITS image [float64, 6x500]

HDU2
----

EXTNAME = SIGMA

Mean Gaussian sigma wavelength dispersion per fiber.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =================================================
KEY    Example Value Type Comment
====== ============= ==== =================================================
NAXIS1 500           int  Mean wavelength dispersion per fiber in Angstroms
====== ============= ==== =================================================

Data: FITS image [float64, 500]


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
