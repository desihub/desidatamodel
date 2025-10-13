======
EZmock
======

``${DESI_ROOT}/survey/catalogs/{RELEASE}/mocks/EZmock`` host 1000 EZmock LSS catalogs (and associated randoms) separated by OBSCON: ``DARK`` or ``BRIGHT`` and followed by internal version (both ``v1`` for ``DARK`` and ``BRIGHT``).  

From the landing page, you will find the initial catalogs in the Y1 footprint (called forFA files) in the ``forFA`` directory, including the imaging lrg_mask files (used only to mask LRGs, present only on the ``DARK`` obscon) plus 1 directory called ``mock{MOCKREA}`` where ``{MOCKREA}`` is the mock realization from [1,1000]. 

Here you can find 1 mock flavour:

  * *FFA*: from Fast Fiber Assigment. It estimates fiber assigment probabilistically learning from the data, based on number of passes and local density (found under ``mock{MOCKREA}``)

Details about the content and production of the LSS catalogs that we follow for the mocks are found in `Ross et al. (2025)`_

.. _Ross et al. (2025): https://iopscience.iop.org/article/10.1088/1475-7516/2025/01/125

.. toctree::
   :maxdepth: 1

   OBSCON : <OBSCON/index>
