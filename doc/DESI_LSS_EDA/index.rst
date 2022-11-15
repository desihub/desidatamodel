============
DESI_LSS_EDA
============

:envvar:`DESI_LSS_EDA` contains LSS catalogs reading from most other DESI products, ready for archiving with 
the early data assembly. Intermediate files are saved, until we build the clustering-ready catalogs 
(including weights). The canonical location is ``$DESI_ROOT/survey/catalogs/edav1/_SURVEY_``, with the 
intention of changing `eda_prep` to `edav1` once finalized. Here, ``_SURVEY_`` defines the LSS-defined selection of tiles, 
like ``sv3`` or ``da02``. Only `sv3` will be released publicly with the EDR. When ready, the `edav1/sv3` 
directory will be copied to `/global/cfs/cdirs/desi/public/edr/vac/LSS/sv3/v1.0`. We will negotiate sym-links as 
necessary. The catalogs are generated using tools from github_lss_repository_

.. _github_lss_repository: https://github.com/desihub/LSS

.. toctree::
   :maxdepth: 1

   survey/index
