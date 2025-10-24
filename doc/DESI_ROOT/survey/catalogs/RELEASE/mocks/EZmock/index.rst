======
EZmock
======

``${DESI_ROOT}/survey/catalogs/{RELEASE}/mocks/EZmock`` hosts 1000 EZmock LSS mock catalogs (and associated random catalogs), separated by ``{OBSCON}``: ``DARK`` or ``BRIGHT`` and followed by an internal version (both ``v1`` for ``DARK`` and ``BRIGHT``).  

From the landing page, you will find 1000 directories called ``mock{MOCKREA}`` where ``{MOCKREA}`` is the mock realization from [1,1000]. 

Here you can find one mock flavour:

  * *FFA* (Fast Fiber Assigment): estimates fiber assigment probabilistically by learning from the data, based on number of passes and local density. These catalogs are stored under each ``mock{MOCKREA}`` directory.

Detailed information about the content and production of these LSS mock catalogs is available in `Ross et al. (2025)`_

.. _Ross et al. (2025): https://iopscience.iop.org/article/10.1088/1475-7516/2025/01/125

.. toctree::
   :maxdepth: 1

   OBSCON : dark or bright <OBSCON/index>
