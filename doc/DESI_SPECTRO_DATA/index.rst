=================
DESI_SPECTRO_DATA
=================

Default $DESI_ROOT/spectro/data

:envvar:`DESI_SPECTRO_DATA` contains raw data as produced by the telescope.
The canonical location is ``$DESI_ROOT/spectro/data``, but one can set the
environment variable :envvar:`DESI_SPECTRO_DATA` to point anywhere.
The exposures are grouped by night as a YEARMMDD string.  The "night" roles
over at noon local time, so all data taken between sunset and sunrise belong
to the same night (i.e. the date of the sunset).  Under each night, data
are grouped in subdirectories by exposure ID (zero-padded 8-digit).

Subdirectories:

.. toctree::
   :maxdepth: 1

   NIGHT/index
