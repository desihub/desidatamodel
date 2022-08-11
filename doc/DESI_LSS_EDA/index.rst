============
DESI_LSS_EDA
============

:envvar:`DESI_LSS_EDA` contains LSS catalogs reading from DESI_TARGET products, ready for early
data release. Intermediate files are saved, until we build the clustering-ready catalogs (including weights). 
The canonical location is ``$DESI_ROOT/survey/catalogs/eda_prep/_RELEASE_``. 
Here, ``_RELEASE_`` defines the data release, like ``sv3`` or ``da02``.
This catalogs are generated using tools from github_lss_repository_

.. _github_lss_repository: https://github.com/desihub/LSS

.. toctree::
   :maxdepth: 1

   release/index
