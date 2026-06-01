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
:doc:`v1 <v1/index>` is a bugfix version with minor updates over
:doc:`v0 <v0/index>`.
:doc:`v2 <v2/index>` is available starting from Data Release 2. It
significantly reformats the files by splitting each catalog into separate files
for core redshift columns, imaging photometry, and all remaining columns, to
reduce per-file sizes at DR2+ data volumes. It also introduces new redshift
quality columns (``Z_BEST``, ``Z_CONF``, ``GOOD_SPEC``,
``GOOD_Z_{BGS,LRG,ELG,QSO}``).

.. toctree::
   :maxdepth: 1

   v0/index
   v1/index
   v2/index
