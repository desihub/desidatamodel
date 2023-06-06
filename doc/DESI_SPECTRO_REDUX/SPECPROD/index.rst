========
SPECPROD
========

Default $DESI_ROOT/spectro/redux/SPECPROD

DESI spectroscopic data processing productions are grouped by spectroscopic
production names (SPECPROD), named after mountains for data releases,
e.g. "fuji" for the `Early Data Release <https://data.desi.lbl.gov/doc/releases/edr>`_.

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
