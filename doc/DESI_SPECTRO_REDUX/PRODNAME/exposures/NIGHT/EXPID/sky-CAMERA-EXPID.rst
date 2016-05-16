==========================
skymodel-CAMERA-EXPID.fits
==========================

*This is a placeholder*

This holds the sky model for a given camera and exposure.
Nominally the HDUs will be:

  - HDU0 (PHOT) : phot[nspec, nwave] - photons/bin
  - HDU1 (IVAR) : ivar[nspec, nwave] - (photons/bin)^-2

The wavelength array will be defined by header keywords CRVAL1 and CDELT1

wave = CRVAL1 + np.arange(NAXIS1) * CDELT1