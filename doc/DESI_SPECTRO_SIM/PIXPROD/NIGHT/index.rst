=====
NIGHT
=====

$DESI_SPECTRO_SIM contains simulated raw data, with the canonical location
of $DESI_ROOT/spectro/sim.  Simulated files are additionally grouped under
a $PIXPROD subdirectory to isolate different simulation runs.

The intention is that $DESI_SPECTRO_SIM/$PIXPROD will contain a superset of
the files in $DESI_SPECTRO_DATA, such that one could set
DESI_SPECTRO_DATA=$DESI_SPECTRO_SIM/$PIXPROD and run the pipeline.

Within each NIGHT (YEARMMDD), individual exposures are grouped in subdirectories
by EXPID.

.. toctree::
   :maxdepth: 1

   EXPID/index
