===
lss
===

``$DESI_ROOT/vac/RELEASE/lss`` contains LSS catalogs reading from most other DESI products, ready for archiving with
the early data release. Intermediate files are saved, until we build the clustering-ready catalogs
(including weights).

``VERSION`` contains different possible versions of the LSS catalogs, given a production run and a tile selection. 

In EDR, there is one single version named ``v2.0`` (we use v2.0 in order to distinguish these catalogs from an internal DESI earlier v1.0 version).
In DR1, there is one version named ``guadalupe/v1.0``. This data should only be used to reproduce results from the early detection of the BAO signal presented in `Moon et al. (2023)`_. The main survey results from Data Releases are to be found in :ref:`../../catalogs/dr1/LSS<catalogs>` directory.

For EDR and DR1 Guadalupe, the final clustering-ready catalogs can be found under :ref:`LSScats/clustering<clustering>`, together with the random samples for the same target types.
Information about the different target types and the use of the different weights can be found in `EDR. DESI Collaboration (2024)`_ and Appendix A in `DR1. DESI Collaboration (2025) in preparation`_

Further information is also found in :ref:`LSScats<lsscats>` subdirectory. The catalogs are generated using tools from github_lss_repository_. For EDR we use the `github release tag v2.0.0-EDR`_

.. _Moon et al. (2023): https://academic.oup.com/mnras/article/525/4/5406/7258657

.. _EDR. DESI Collaboration (2024): https://iopscience.iop.org/article/10.3847/1538-3881/ad3217

.. _DR1. DESI Collaboration (2025) in preparation: https://www.desi.lbl.gov/

.. _github_lss_repository: https://github.com/desihub/LSS

.. _github release tag v2.0.0-EDR: https://github.com/desihub/LSS/releases/tag/v2.0.0-EDR


.. toctree::
   :maxdepth: 1

   VERSION/index
