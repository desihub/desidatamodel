===========
DESI_LSS
===========

:envvar:`DESI_LSS` contains LSS catalogs reading from DESI_TARGET products. Intermediate files 
are saved, until we build the clustering-ready catalogs (including weights). 
The canonical location is ``$DESI_ROOT/survey/catalogs/_FOOTPRINT_/LSS/``. 
Here, ``_FOOTPRINT_`` defines the data release, like ``DA02_fh`` or ``SV3``.
This catalogs are generated using tools from github_lss_repository_

.. _github_lss_repository: https://github.com/desihub/LSS

.. toctree::
   :maxdepth: 1

   specprod/index
