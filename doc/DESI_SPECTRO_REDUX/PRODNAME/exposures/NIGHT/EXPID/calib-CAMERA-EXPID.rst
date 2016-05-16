=======================
calib-CAMERA-EXPID.fits
=======================

*The current pipeline calls this file calib-CAMERA-EXPID.fits rather
than fluxcalib...  The data format also doesn't match what is outlined
below.*

regex: ``calib-[brz][0-9]-[0-9]{8}\.fits``

This holds the flux calibration model for a given camera and exposure.
Nominally the HDUs will be:

  - HDU0 (FLUXCALIB) : calib[nspec, nwave]
  - HDU1 (IVAR) : inverse variance[nspec, nwave] of fluxcalib
  - HDU2 (MASK) : mask[nspec, nwave] of fluxcalib (0=good)
  - HDU3 (WAVELENGTH) : wavelength[nwave] in Angstroms
  - HDU4 (METADATA) : binary table with one row per standard star giving
    the details of which model was used, etc.  Details TBD.
