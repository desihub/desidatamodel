============
fba{MOCKREA}
============

``${DESI_ROOT}/survey/catalogs/RELEASE/mocks/AbacusSummit/OBSCON/VERSION/altmtl{MOCKREA}/fba{MOCKREA}`` contains the fba compiled data of potential and assigned data, matched to the parent forFA file.

Two different files can be found here, or all potential assigments matched to the data (with duplicates) or only those that were assigned to a fiber (with duplicates).

These files are generated after running the AltMTL processing on mocks, not made public for logistical purposes, but replicable using the `LSS repo`_.

.. _LSS repo: https://github.com/desihub/LSS/


.. toctree::
   :maxdepth: 1

   datcomb_{obscon}{assign}wdup.fits : Compilation, if assign in name, means the actual observed tracers <datcomb_wdup>
