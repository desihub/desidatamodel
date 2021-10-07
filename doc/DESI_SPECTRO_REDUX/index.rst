==================
DESI_SPECTRO_REDUX
==================

This directory contains production runs of the spectroscopic data reduction
pipeline.  Each different run is contained in different SPECPROD subdirectory.

The desispec code refers to this location with the environment variable
$DESI_SPECTRO_REDUX .  The canonical location is $DESI_ROOT/spectro/redux,
but changing the environment variable allows the code to write to other
test directories.

.. toctree::
   :maxdepth: 1

   $DESI_SPECTRO_REDUX/$SPECPROD <SPECPROD/index>
