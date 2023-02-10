=====
tiles
=====

Spectra, coadds, and redshifts organized **per tile** are under
``tiles/GROUPTYPE/TILEID/GROUPID``.  These come in various groups (GROUPTYPE),
e.g. whether they are data from a single exposure, a single night,
all data for a given tile across all nights, or a custom combination.

Related: all data for a given patch of sky, including data grouped across
overlapping tiles and coadds of targets observed on multiple tiles, are
organized under the :doc:`healpix <../healpix/index>` directories.

``GROUPTYPE`` can be one of:

``cumulative``
    Coadds of all spectra on a given tile across all nights.

``pernight``
    Coadds of all spectra on a given tile in a given night.

``perexp``
    Spectra grouped by tile and then exposure.

``1x_depth``
    Selected custom subsets of exposures of deep (:math:`N>>1` exposures) tiles
    to achieve a combined depth for each subset matching the main survey depth.
    That is, they are subsets of the total exposures taken for that tile,
    selected to achieve a specific depth, for systematics comparisons with the full depth
    coadds+redshifts in the cumulative group that has all exposures for each tile.

``4x_depth``
    Similar to ``1x_depth``, but selected to achieve a combined depth of 4x
    the main survey depth.

The ``GROUPID`` depends on the ``GROUPTYPE``:

=========== =======
GROUPTYPE   GROUPID
=========== =======
cumulative  YEARMMDD NIGHT - all data through that night
pernight    YEARMMDD NIGHT - only data from that night
perexp      EXPID - only data from that single exposure
1x_depth    subset number
4x_depth    subset number
=========== =======

e.g. spectra, coadds, and
redshifts for all exposures of tile 80605 observed on 20210109 are
under ``tiles/pernight/80605/20210109``, while all data for tile 80605
for all nights through 20210205 (including previous nights like 20210109)
are under ``tiles/cumulative/80605/20210205``.

Subdirectories of ``tiles/`` :

.. toctree::
   :maxdepth: 1

   GROUPTYPE/index
