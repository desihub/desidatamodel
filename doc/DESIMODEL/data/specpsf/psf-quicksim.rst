===
psf
===

:Summary: PSF data for quicksim.
:Naming Convention: ``psf-quicksim.fits``
:Regex: ``psf-quicksim\.fits``
:File Type: FITS, 554 KB

Contents
========

====== ========== ======== =======================
Number EXTNAME    Type     Contents
====== ========== ======== =======================
HDU0_  PRIMARY    IMAGE    Empty
HDU1_  QUICKSIM-B BINTABLE b-camera PSF parameters
HDU2_  QUICKSIM-R BINTABLE r-camera PSF parameters
HDU3_  QUICKSIM-Z BINTABLE z-camera PSF parameters
====== ========== ======== =======================


FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = QUICKSIM-B

b-camera PSF parameters.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================================== ==== ===================================
KEY      Example Value                            Type Comment
======== ======================================== ==== ===================================
NAXIS1   40                                       int  width of table in bytes
NAXIS2   4761                                     int  number of rows in table
EXTNAME  QUICKSIM-B                               str  name of this binary table extension
PSFFILE  psf-b.fits                               str  Input PSF file
PSFSHA1  a88fbc9ab3567518a5c89bb6a15055e68bc4b94e str  SHA1 checksum input PSF
WMIN_ALL 3569                                     int  Starting wavelength [Angstroms]
WMAX_ALL 5949                                     int  Last wavelength [Angstroms]
WAVEUNIT Angstrom                                 str  Wavelengths in Angstroms
======== ======================================== ==== ===================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

================= ======= ============== ===========================================
Name              Type    Units          Description
================= ======= ============== ===========================================
wavelength        float64 Angstrom       wavelength
fwhm_wave         float64 Angstrom       FWHM in wavelength (y) direction
fwhm_spatial      float64 pixel          FWHM in cross-dispersion (x) direction
neff_spatial      float64 pixel          Number of effective pixels covered
angstroms_per_row float64 Angstrom/pixel Angstroms per CCD pixels at this wavelength
================= ======= ============== ===========================================

HDU2
----

EXTNAME = QUICKSIM-R

r-camera PSF parameters.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================================== ==== ===================================
KEY      Example Value                            Type Comment
======== ======================================== ==== ===================================
NAXIS1   40                                       int  width of table in bytes
NAXIS2   4233                                     int  number of rows in table
EXTNAME  QUICKSIM-R                               str  name of this binary table extension
PSFFILE  psf-r.fits                               str  Input PSF file
PSFSHA1  0709be9b7275c7f6ef3a1bd9003426ae9a68b2aa str  SHA1 checksum input PSF
WMIN_ALL 5625                                     int  Starting wavelength [Angstroms]
WMAX_ALL 7741                                     int  Last wavelength [Angstroms]
WAVEUNIT Angstrom                                 str  Wavelengths in Angstroms
======== ======================================== ==== ===================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

================= ======= ============== ===========================================
Name              Type    Units          Description
================= ======= ============== ===========================================
wavelength        float64 Angstrom       wavelength
fwhm_wave         float64 Angstrom       FWHM in wavelength (y) direction
fwhm_spatial      float64 pixel          FWHM in cross-dispersion (x) direction
neff_spatial      float64 pixel          Number of effective pixels covered
angstroms_per_row float64 Angstrom/pixel Angstroms per CCD pixels at this wavelength
================= ======= ============== ===========================================

HDU3
----

EXTNAME = QUICKSIM-Z

z-camera PSF parameters.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================================== ==== ===================================
KEY      Example Value                            Type Comment
======== ======================================== ==== ===================================
NAXIS1   40                                       int  width of table in bytes
NAXIS2   4799                                     int  number of rows in table
EXTNAME  QUICKSIM-Z                               str  name of this binary table extension
PSFFILE  psf-z.fits                               str  Input PSF file
PSFSHA1  d19b2f2054a89182cc9f7bd03508b105982943ae str  SHA1 checksum input PSF
WMIN_ALL 7435                                     int  Starting wavelength [Angstroms]
WMAX_ALL 9834                                     int  Last wavelength [Angstroms]
WAVEUNIT Angstrom                                 str  Wavelengths in Angstroms
======== ======================================== ==== ===================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

================= ======= ============== ===========================================
Name              Type    Units          Description
================= ======= ============== ===========================================
wavelength        float64 Angstrom       wavelength
fwhm_wave         float64 Angstrom       FWHM in wavelength (y) direction
fwhm_spatial      float64 pixel          FWHM in cross-dispersion (x) direction
neff_spatial      float64 pixel          Number of effective pixels covered
angstroms_per_row float64 Angstrom/pixel Angstroms per CCD pixels at this wavelength
================= ======= ============== ===========================================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
