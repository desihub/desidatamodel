=====
NIGHT
=====

``NIGHT`` is the night of observation in YYYYMMDD format.  The "night" roles
over at noon local time, so all data taken between sunset and sunrise belong to the same night (i.e. the date of the sunset).

Each exposure id (expid) has two files:

.. toctree::
   :maxdepth: 1

   desi-{expid}.fits.fz : Raw data <desi-EXPID>
   fibermap-{expid}.fits : Table of which fibers were assigned to which targets <fibermap-EXPID>
   gfa-{expid}.fits : Placeholder for GFA data <gfa-EXPID>
