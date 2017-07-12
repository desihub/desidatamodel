=======================
coadd-NSIDE-PIXNUM.fits
=======================

*This is a placeholder for the coadd data model; these are not yet generated*

This holds the calibrated coadded spectra organized by healpix location
on the sky.

regex: ``coadd-[0-9]{4}[pm][0-9]{3}\.fits``

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

Written by desi_update_coadds.py, using:

  - brick
