========
zcatalog
========

Redshift catalogs combine redshifts and classifications from individual
redrock files with the corresponding target and observing metadata.

Starting from Data Release 1, multiple zcatalog versions may be released with
each SPECPROD. In general the highest version number is the "preferred" catalog.
Different versions can have different formats and thus are documented separately.

Earlier releases have the redshift catalogs at this level, following the
:doc:`v0 <v0/index>`
format except without the columns ``MAIN_NSPEC`` and ``MAIN_PRIMARY``.
:doc:`v1 <v1/index>` is basically a bugfix version with minor updates over
:doc:`v0 <v0/index>`, but a future
planned v2 will significantly reformat the files to make them easier to work
with the rapidly increasing data volumes of the DESI catalogs.

.. toctree::
   :maxdepth: 1

   v0/index
   v1/index
