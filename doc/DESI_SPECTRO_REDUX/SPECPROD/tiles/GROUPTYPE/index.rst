=========
GROUPTYPE
=========

During commissioning and survey validation, per-tile spectra, coadds, and redshifts
are grouped in ``tiles/GROUPTYPE/TILEID/GROUPID``.

``GROUPTYPE`` can be one of:

``1x_depth``
    Special coadd.

``4x_depth``
    Special coadd.

``cumulative``
    Coadds of all spectra in a given tile.

``perexp``
    Spectra grouped by tile and then exposure.

``pernight``
    Coadds of all spectra in a given tile in a given night.


.. toctree::
   :maxdepth: 1

   TILEID/index
