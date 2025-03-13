========
SPECPROD
========

Default $DESI_ROOT/spectro/redux/SPECPROD

DESI spectroscopic data processing productions are grouped by spectroscopic
production names (SPECPROD), named after mountains for data releases,
*e.g.* "iron" for `Data Release 1 <https://data.desi.lbl.gov/doc/releases/dr1>`_.

Files in the top-level production directory:

* :doc:`exposures-SPECPROD.fits <exposures-SPECPROD>`: summary of exposures
* :doc:`tiles-SPECPROD.fits <tiles-SPECPROD>`: summary of tiles

Subdirectories under a spectroscopic production:

* :doc:`zcatalog/ <zcatalog/index>`: summary redshift catalogs
* :doc:`healpix/SURVEY/PROGRAM/PIXGROUP/PIXNUM <healpix/SURVEY/PROGRAM/PIXGROUP/PIXNUM/index>`:
  spectra, classifications, and redshifts coadded across tiles, grouped by survey, program, and healpixel.
* :doc:`tiles/GROUPTYPE/TILEID/GROUPID/index <tiles/GROUPTYPE/TILEID/GROUPID/index>`:
  spectra, classifications, and redshifts coadded per tile.
* :doc:`calibnight/NIGHT/ <calibnight/NIGHT/index>`: nightly calibrations
* :doc:`preproc/NIGHT/EXPID <preproc/NIGHT/EXPID/index>`: preprocessed spectrograph CCD images
* :doc:`exposures/NIGHT/EXPID <exposures/NIGHT/EXPID/index>`: per-exposure intermediate files

Other subdirectories that represent internal desispec_ pipeline details, but do not contain production data:

* exposure_tables/ : Details on individual exposures that are inputs to the pipeline.
  For example, bad exposures may be marked in these tables.
* processing_tables/ : Details on the processing status of individual exposures.
* run/ : Scripts and log files produced by the desispec_ pipeline.

.. _desispec: https://github.com/desihub/desispec

.. toctree::
   :maxdepth: 1
   :hidden:

   calibnight/index
   exposures/index
   healpix/index
   preproc/index
   tiles/index
   zcatalog/index
   exposures-SPECPROD
   tiles-SPECPROD
