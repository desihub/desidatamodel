===========================
fluxcalib-CAMERA-EXPID.fits
===========================

*This is a placeholder*

This holds the flux calibration model for a given camera and exposure.
Nominally the HDUs will be:

  - HDU0 (CALIB) : calib[nspec, nwave]
  - HDU1 (METADATA) : binary table with one row per standard star giving
    the details of which model was used, etc.  Details TBD.

flux [erg/s/cm2/A] = calib * photons [counts/bin]

The wavelength array will be defined by header keywords CRVAL1 and CDELT1

wave = CRVAL1 + np.arange(NAXIS1) * CDELT1