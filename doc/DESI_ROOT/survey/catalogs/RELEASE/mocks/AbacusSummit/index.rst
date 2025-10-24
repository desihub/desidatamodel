============
AbacusSummit
============

``${DESI_ROOT}/survey/catalogs/{RELEASE}/mocks/AbacusSummit`` hosts 25 Abacus LSS catalogs (and associated random catalogs), separated by ``{OBSCON}`` (``DARK`` or ``BRIGHT``) and followed by an internal version. For ``DARK`` (LRG, ELG and QSO) the internal version is ``v4.2`` and for ``BRIGHT`` (BGS) it is ``v1``. 

On this page you will find: the initial catalog in the Y1 footprint (called forFA files), the lrg_mask file (used only to mask LRGs, present only under ``DARK`` obscon) and two directories per mock realization called ``altmtl{MOCKREA}`` and ``mock{MOCKREA}``, where ``{MOCKREA}`` is the mock realization index from 0 to 24. 

You will find three distinct mock flavors, depending on the level of realism:

  * *Complete*: no fiber-assigment effects; includes the tracers reachable by any DESI fiber (located under ``mock{MOCKREA}``)

  * *FFA* (Fast Fiber Assigment): estimates fiber assigment probabilistically by learning from the data, based on number of passes and local density (also under ``mock{MOCKREA}``)

  * *altmtl*: estimated using the same fba algorithm, passes and hardware configuration as in the actual data (found under ``altmtl{MOCKREA}``). To replicate the fiber-assigment processing, see the instructions in `LSS repo`_. 


Details about the content and production of the LSS catalogs are given in `Ross et al. (2025)`_. These mocks were used in the main BAO cosmological analysis; more information is available in `DESI Collaboration (2025)`_.

A comparison of the three mock flavors is described in `Bianchi et al. (2025)`_

.. _Ross et al. (2025): https://iopscience.iop.org/article/10.1088/1475-7516/2025/01/125
.. _Bianchi et al. (2025): https://iopscience.iop.org/article/10.1088/1475-7516/2025/04/074
.. _LSS repo: https://github.com/desihub/LSS/
.. _DESI Collaboration (2025): https://iopscience.iop.org/article/10.1088/1475-7516/2025/02/021

.. toctree::
   :maxdepth: 1

   
   OBSCON : dark or bright <OBSCON/index>
