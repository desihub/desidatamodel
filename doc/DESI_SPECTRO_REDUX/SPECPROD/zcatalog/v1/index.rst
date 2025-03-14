==
v1
==

The v1 redshift catalogs combine redshifts and classifications from individual
redrock files with the corresponding target and observing metadata.

The :doc:`ztile <ztile-SURVEY-PROGRAM-GROUPTYPE>` catalogs contain redshifts for each survey/program combination,
fit to coadded exposures of each tile (but not coadded across tiles).
The :doc:`zpix <zpix-SURVEY-PROGRAM>` catalogs are similar to the ztile catalogs, but they also
coadd data across tiles before redshift fitting.
The :doc:`zall-pix <zall-pix-SPECPROD>` and
:doc:`zall-tilecumulative <zall-tilecumulative-SPECPROD>`
catalogs stack the individual zpix and ztile files into combined catalogs
across all surveys and programs.

.. toctree::
   :maxdepth: 1

   zall-pix-SPECPROD
   zall-tilecumulative-SPECPROD
   zpix-SURVEY-PROGRAM
   ztile-SURVEY-PROGRAM-GROUPTYPE
