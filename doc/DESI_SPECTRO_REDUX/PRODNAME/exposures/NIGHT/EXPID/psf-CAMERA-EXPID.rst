==============
Datamodel: psf
==============

General Description
===================

Summary
-------

The PSF file in exposures/{NIGHT}/{EXPID}/psf-{CAMERA}-{EXPID}.fits is a
soft link to the PSF file in calib2d/psf/{NIGHT}/psf-{CAMERA}-{PSFEXPID}.fits
that should be used for extracting this exposure.  Note that the science
exposure EXPID can point to a different PSFEXPID.

See the psf data model in
:doc:`../../../calib2d/psf/NIGHT/psf-gauss-hermite.rst for format details.

Naming Convention
-----------------

``psf-AS-EXPNUM.fits``, where A is the spectrograph arm ('b','r' or 'z'),
S the spectrograph identifier [0-9], and EXPNUM the exposure number.

regex: ``psf-[brz]{1}[0-9]{1}-[0-9]{8}.fits``

File Type
---------

softlink to FITS file
