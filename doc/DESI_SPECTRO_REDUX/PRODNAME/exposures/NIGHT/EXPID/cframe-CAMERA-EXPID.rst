========================
cframe-CAMERA-EXPID.fits
========================

This holds the calibrated spectra for a given camera and exposure.
See the datamodel for frame-CAMERA-EXPID files for details of the format.

  - HDU0 (FLUX) : flux[nspec, nwave] - erg/s/cm2/A
  - HDU1 (IVAR) : ivar[nspec, nwave] - (erg/s/cm2/A)^-2
  - HDU2 (MASK) : mask[nspec, nwave] - 0 is good
  - HDU3 (RESOLUTION) : R[nspec, ndiag, nwave] - Resolution Matrix