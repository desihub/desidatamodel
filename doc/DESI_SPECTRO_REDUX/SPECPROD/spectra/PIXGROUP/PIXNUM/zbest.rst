=====
zbest
=====

:Summary: Best fit redshifts for each targets in a spectra file.
:Naming Convention: ``zbest-NSIDE-PIXNUM.fits``, where NSIDE is the healpix
    Nside (typically 64) and PIXNUM is the nested scheme healpix number.
:Regex: TODO
:File Type: FITS, 1 MB

Note: the corresponding spectra file in this directory has one entry per
exposure of each target, while this zbest file has one entry per target,
thus it can have a different number of entries and is not row-matched to
the spectra file.

Contents
========

====== ======= ======== =============================
Number EXTNAME Type     Contents
====== ======= ======== =============================
HDU0_          IMAGE    Blank HDU
HDU1_  ZBEST   BINTABLE Table with best fit redshifts
====== ======= ======== =============================


FITS Header Units
=================

HDU0
----

Empty HDU.

This HDU has no non-standard required keywords.

TODO: this HDU should have code versions used but it doesn't yet.

HDU1
----

EXTNAME = ZBEST

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ============= ==== ===================================
KEY     Example Value Type Comment
======= ============= ==== ===================================
NAXIS1  143           int  width of table in bytes
NAXIS2  1165          int  number of rows in table
EXTNAME ZBEST         str  name of this binary table extension
======= ============= ==== ===================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

========= =========== ===== =============================================
Name      Type        Units Description
========= =========== ===== =============================================
CHI2      float64           Best fit chi2
COEFF     float64[10]       Redrock template coefficients
Z         float64           Best fit redshift
ZERR      float64           Uncertainty on best fit redshift
ZWARN     int64             Warning flags; 0 is good
SPECTYPE  char[6]           Spectral type
SUBTYPE   char[1]           Spectral subtype (maybe blank)
TARGETID  int64             TARGETID for this row
DELTACHI2 float64           Delta(chi2) to next best fit
BRICKNAME char[8]           Imaging brickname where this target came from
========= =========== ===== =============================================

Upcoming changes
================

The following changes are not yet in the zbest files, but will be added in
the future:

  * Code versions in HDU 0
  * NEXP, NTILE columns in ZBEST HDU
  * Coadded signal-to-noise per band
  * SUBTYPE will expand beyond a 1-character array