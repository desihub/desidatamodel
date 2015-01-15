=====
NIGHT
=====

$DESI_SPECTRO_SIM contains simulated raw data, with the canonical location
of $DESI_ROOT/spectro/sim.  Simulated files are additionally grouped under
a $PIXPROD subdirectory to isolate different simulation runs.

The intention is that $DESI_SPECTRO_SIM/$PIXPROD will contain a superset of
the files in $DESI_SPECTRO_DATA, such that one could set
DESI_SPECTRO_DATA=$DESI_SPECTRO_SIM/$PIXPROD and run the pipeline.
The simulator does not yet output truly raw data (only preprocessed data)
so this is not yet possible.


.. toctree::
   :maxdepth: 1

   fibermap-EXPID.rst
   pix-CAMERA-EXPID.rst
   simpix-CAMERA-EXPID.rst
   simspec-EXPID.rst
