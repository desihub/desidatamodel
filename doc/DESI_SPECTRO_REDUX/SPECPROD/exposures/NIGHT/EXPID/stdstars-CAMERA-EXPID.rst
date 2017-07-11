========
stdstars
========

*This is a placeholder description*

This file contains the normalized standard star models fitted to the
frame data.

Naming convention: stdstars-{SPECTROGRAPH}-{EXPID}.fits wher
{SPECTROGRAPH} is the single-digit spectrograph number 0-9, and
{EXPID} is the zero-padded 8-digit exposure number.

regex: ``stdstars-[0-9]-[0-9]{8}\.fits``

HDUS:

  - HDU0 FLUX : stdstar flux[nstd, nwave] in erg/s/cm^2/Angstrom
  - HDU1 WAVELENGTH : wavelength grid used, Angstroms
  - HDU2 FIBERS : 1D array of which fibers these models correspond to
  - HDU3 METADATA : metadata from input standard star templates

Note: dc3 productions used "WAVE" instead of "WAVELENGTH" for HDU 1.