=========
GROUPTYPE
=========

During commissioning and survey validation, per-tile spectra, coadds, and redshifts
are grouped in ``tiles/GROUPTYPE/TILEID/GROUPID``.

``GROUPTYPE`` can be one of:

``1x_depth``
    Selected custom subsets of exposures of deep (:math:`N>>1` exposures) tiles
    to achieve a combined depth for each subset matching the main survey depth.
    That is, they are subsets of the total exposures taken for that tile,
    selected to achieve a specific depth, for systematics comparisons with the full depth
    coadds+redshifts in the cumulative group that has all exposures for each tile.

``4x_depth``
    Similar to ``1x_depth``, but selected to achieve a combined depth of 4x
    the main survey depth.

``cumulative``
    Coadds of all spectra in a given tile.

``perexp``
    Spectra grouped by tile and then exposure.

``pernight``
    Coadds of all spectra in a given tile in a given night.


.. toctree::
   :maxdepth: 1

   TILEID/index
