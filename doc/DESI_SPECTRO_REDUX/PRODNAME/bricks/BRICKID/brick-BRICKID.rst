==================
brick-BRICKID.fits
==================

*This is a placeholder for the brick data model*

This holds the calibrated individual exposure spectra organized by location
on the sky (brick).

Nominally the HDUs will be:

  - HDU0 (FLUX) : flux[nspec, nwave] - erg/s/cm2/A
  - HDU1 (IVAR) : ivar[nspec, nwave] - (erg/s/cm2/A)^-2
  - HDU2 (MASK) : mask[nspec, nwave] - 0 is good
  - HDU3 (RESOLUTION) : R[nspec, ndiag, nwave] - Resolution Matrix
  - HDU4 (FIBERMAP) : the corresponding fibermap entries for these spectra,
    potentially augmented with additional columns such as
    - night
    - expid

This should contain the same information as cframe files, just differently
organized.  They should be complete enough to generate a coadd based only
on information in this file.

Inputs
======

Written by XXX, using:

  - cframe