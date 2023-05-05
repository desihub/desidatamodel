===
LSS
===

:envvar:`LSS` contains LSS catalogs reading from most other DESI products, ready for archiving with 
the early data release. Intermediate files are saved, until we build the clustering-ready catalogs 
(including weights). 

Here ``specprod`` defines the production used to reduce the data. For the Early Data Release (EDR), this is :envvar:`fuji`.  

The final clustering-ready catalogs can be found under :ref:`LSScats/clustering<clustering>`, together with the random samples for the same target types. 
Information about the different target types and the use of the different weights can be found in `DESI Collaboration, in preparation (2023)`_ and in the explanation of :ref:`LSScats<lsscats>` subdirectory.

The catalogs are generated using tools from github_lss_repository_.

.. _DESI Collaboration, in preparation (2023): https://ref_EDR

.. _github_lss_repository: https://github.com/desihub/LSS
.. _REF1: https_//refref

.. toctree::
   :maxdepth: 1

   specprod/index
