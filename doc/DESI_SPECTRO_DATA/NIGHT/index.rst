=====
NIGHT
=====

| $DESI_SPECTRO_DATA/NIGHT
| Default $DESI_ROOT/spectro/data/NIGHT

``NIGHT`` is the night of observation in YYYYMMDD format.  The "night" roles
over at noon local time, so all data taken between sunset and sunrise
belong to the same night (i.e. the date of the sunset). Under each night, data
are grouped in subdirectories by exposure ID (zero-padded 8-digit).

.. toctree::
   :maxdepth: 1

   EXPID/index.rst