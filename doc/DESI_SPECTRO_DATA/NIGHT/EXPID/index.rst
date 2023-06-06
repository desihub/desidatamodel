=====
EXPID
=====

| $DESI_SPECTRO_DATA/NIGHT/EXPID
| Default $DESI_ROOT/spectro/data/NIGHT/EXPID

Raw data for each exposure of the DESI instrument.

``NIGHT`` is the night of observation in YYYYMMDD format.  The "night" roles
over at noon local time, so all data taken between sunset and sunrise
belong to the same night (i.e. the date of the sunset).
``EXPID`` is the 8-digit zero-padded exposure ID.

Each exposure id (expid) generates multiple files:

.. toctree::
   :maxdepth: 1

   centroids-{expid}.json : Guide camera centroids <centroids-EXPID>
   coordinates-{expid}.fits : Coordinates file <coordinates-EXPID>
   desi-{expid}.fits.fz : Raw data <desi-EXPID>
   etc-{expid}.json : Exposure Time Calculator (ETC) analysis <etc-EXPID>
   fiberassign-{tileid}.fits.gz : Table of which fibers were assigned to which targets <fiberassign-TILEID>
   fibermap-{expid}.fits : Table of which fibers were assigned to which targets (*obsolete*) <fibermap-EXPID>
   focus-{expid}.fits.fz : Placeholder for focus GFA raw data <focus-EXPID>
   fvc-{expid}.fits.fz : Fiber View Camera data <fvc-EXPID>
   fvc-primary-{expid}.fits : Fiber View Camera data <fvc-primary-EXPID>
   FVC-measure-{expid}.fits : Fiber View Camera data <FVC-measure-EXPID>
   gfa-{expid}.fits : GFA file <gfa-EXPID>
   guide-{expid}.fits.fz : Placeholder for guide GFA raw data <guide-EXPID>
   guide-rois-{expid}.fits.fz : Placeholder for guide GFA raw data <guide-rois-EXPID>
   manifest_{expid}.json : Manifest file used in early commissioning <manifest_EXPID>
   pm-{expid}.fits : Platemaker data <pm-EXPID>
   request-{expid}.json : Commands used to initiate an exposure <request-EXPID>
   sky-{expid}.fits.fz : Placeholder for guide GFA raw data <sky-EXPID>
