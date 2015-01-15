==================
coadd-BRICKID.fits
==================

*This is a placeholder for the coadd data model*

This holds the calibrated coadded spectra organized by location
on the sky (brick).

Nominally the HDUs will be:

  - HDU0 (FLUX) : flux[nspec, nwave] - erg/s/cm2/A
  - HDU1 (IVAR) : ivar[nspec, nwave] - (erg/s/cm2/A)^-2
  - HDU2 (MASK) : mask[nspec, nwave] - 0 is good
  - HDU3 (RESOLUTION) : R[nspec, ndiag, nwave] - Resolution Matrix
  - HDU4 (METADATA) : binary table about these spectra, including
    - targetid
    - *some way of listing which exposures contributed*

Inputs
======

Written by XXX, using:

  - brick