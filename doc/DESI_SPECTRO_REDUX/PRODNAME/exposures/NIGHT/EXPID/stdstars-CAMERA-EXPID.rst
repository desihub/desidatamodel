========
stdstars
========

*This is a placeholder description*

This file contains the normalized standard star models fitted to the
frame data.

Naming convention: stdstars-sp{SPECTROGRAPH}-{EXPID}.fits

HDUS:

  - HDU0 FLUX : stdstar flux[nstd, nwave] in erg/s/cm^2/Angstrom
  - HDU1 WAVE : wavelength grid used (SHOULD BE 'WAVELENGTH' INSTEAD?)
  - HDU2 FIBERS : 1D array of which fibers were used (?!?)
  - HDU3 METADATA : metadata from input standard star templates