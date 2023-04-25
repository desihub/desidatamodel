============
DESI_LSS_EDR
============

:envvar:`DESI_LSS_EDR` contains LSS catalogs reading from most other DESI products, ready for archiving with 
the early data release. Intermediate files are saved, until we build the clustering-ready catalogs 
(including weights). Here ``_release_`` defines the LSS-defined selection of tiles for the Early Data Release. 
The final clustering-ready catalogs can be found under ``LSScats/clustering`` together with the random samples for the same target types. 
Information about the different target types and the use of the different weights can be found in REF1_ and in the explanation of LSScats subdirectory.
The catalogs are generated using tools from github_lss_repository_.

References: REF1_

.. _github_lss_repository: https://github.com/desihub/LSS
.. _REF1: https_//refref

.. toctree::
   :maxdepth: 1

   survey/index
