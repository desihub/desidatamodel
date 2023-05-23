===
lss
===

``$DESI_ROOT/vac/RELEASE/lss`` contains LSS catalogs reading from most other DESI products, ready for archiving with 
the early data release. Intermediate files are saved, until we build the clustering-ready catalogs 
(including weights). 

``VERSION`` contains different possible versions of the LSS catalogs, given a production run and a tile selection. As of the EDR release date, there is one single version named ``v2.0`` (we use v2.0 in order to distinguish these catalogs from an internal DESI earlier v1.0 version).

The final clustering-ready catalogs can be found under :ref:`LSScats/clustering<clustering>`, together with the random samples for the same target types. 
Information about the different target types and the use of the different weights can be found in `EDR. DESI Collaboration (in prep.)`_ and in the explanation of :ref:`LSScats<lsscats>` subdirectory.

The catalogs are generated using tools from github_lss_repository_. For EDR we use the `github release tag v2.0.0-EDR`_

.. _EDR. DESI Collaboration (in prep.): https://ui.adsabs.harvard.edu/public-libraries/XCj7bW-vSMaNZVV0C0QyGA

.. _github_lss_repository: https://github.com/desihub/LSS

.. _github release tag v2.0.0-EDR: https://github.com/desihub/LSS/releases/tag/v2.0.0-EDR


.. toctree::
   :maxdepth: 1

   VERSION/index
