========================
cframe-CAMERA-EXPID.fits
========================

This holds the calibrated spectra for a given camera and exposure.
See the datamodel for frame-CAMERA-EXPID files for details of the format.

regex: ``cframe-[brz][0-9]-[0-9]{8}\.fits``

  - HDU0 (FLUX) : flux[nspec, nwave] - erg/s/cm2/A
  - HDU1 (IVAR) : ivar[nspec, nwave] - (erg/s/cm2/A)^-2
  - HDU2 (WAVELENGTH) : wavelength[nwave] in Angstroms
  - HDU3 (RESOLUTION) : R[nspec, ndiag, nwave] - Resolution Matrix
  - HDU4 (MASK) : mask[nspec, nwave] - 0 is good *MISSING FROM CURRENT FILES*
