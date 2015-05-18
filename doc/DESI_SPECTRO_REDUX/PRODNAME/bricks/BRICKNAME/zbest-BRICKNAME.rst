====================
zbest-BRICKNAME.fits
====================

*This is a placeholder for the redshift data model*

This holds the classification and redshift information for targets.
The formats are TBD, but it should be row-matched to the spectra in
coadd-BRICKNAME.rst .  This is not yet the case.

Nominally the HDUs will be:

  - HDU0 (empty)
  - HDU1 (ZBEST) : binary table with best redshift fit results
  - ...

Inputs
======

Written by XXX, using:

  - coadd (coadded spectra)
  - brick (individual spectra)
  
HDU1
----

EXTNAME = ZBEST

*Current description of ZBEST; this will evolve*
  
Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

========= ======== ===== ===========
Name      Type     Units Description
========= ======== ===== ===========
BRICKNAME char[8]        Brick name from targeting, e.g. 1234p567
TARGETID  int64          Unique target ID
Z         float64        Best fit redshift
ZERR      float64        Uncertainty on redshift
ZWARN     int64          Warning bitmask (TBD)
TYPE      char[20]       Object type (options TBD)
SUBTYPE   char[20]       Object subtype (options TBD)
========= ======== ===== ===========
