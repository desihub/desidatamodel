=====================
sky-CAMERA-EXPID.fits
=====================

*This is a placeholder*

regex: ``sky-[brz][0-9]-[0-9]{8}\.fits``

This holds the sky model for a given camera and exposure.
Nominally the HDUs will be:

  - HDU0 (SKY) : phot[nspec, nwave] - photons/bin
  - HDU1 (IVAR) : ivar[nspec, nwave] - (photons/bin)^-2
  - HDU2 (MASK) : mask[nspec, nwave] - 0=good
  - HDU3 (WAVELENGTH) : wave[nwave]  - wavelength in Angstroms
