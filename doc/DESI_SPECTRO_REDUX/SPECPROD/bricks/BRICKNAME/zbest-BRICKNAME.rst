====================
zbest-BRICKNAME.fits
====================

**Organization of spectra by brick is deprecated; see spectra/ instead.**

*This is a placeholder for the redshift data model*

This holds the classification and redshift information for targets.
It contains the same TARGETIDs as the input brick-{camera}-{brickname}.fits
files, but they could be in a different order.

regex: ``zbest-[0-9]{4}[pm][0-9]{3}\.fits``

Nominally the HDUs will be:

  - HDU0 (empty)
  - HDU1 (ZBEST) : binary table with best redshift fit results

Inputs
======

Written by ``desi_zfind.py``, using individual brick-{channel}-{expid}.fits files.

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
