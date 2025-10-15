=======
VERSION
=======

``${DESI_ROOT}/survey/catalogs/{RELEASE}/mocks/AbacusSummit/{OBSCON}/{VERSION}`` host 25 Abacus LSS catalogs (and associated randoms) separated by OBSCON: ``DARK`` or ``BRIGHT`` and followed by internal version, where for ``DARK`` (LRG, ELG and QSO) is ``v4.2`` and for ``BRIGHT`` (BGS) is ``v1``. 

From the landing page, you will find the initial catalog in the Y1 footprint (called forFA files), the lrg_mask file (used only to mask LRGs, present only on the ``DARK`` obscon) and 2 directories called ``altmtl{MOCKREA}`` and ``mock{MOCKREA}`` where ``{MOCKREA}`` is the mock realization from [0,25). 

Here you can find 3 distinct mock flavours depending on the level of realism:

  * *Complete*: no fiber assigment effects, just the tracers that are reachable by any DESI fiber (found under ``mock{MOCKREA}``)

  * *FFA*: from Fast Fiber Assigment. It estimates fiber assigment probabilistically learning from the data, based on number of passes and local density (found under ``mock{MOCKREA}``)

  * *altmtl*: Estimated using the same fba algorithm, passes and hardware configuration as the data (found under ``altmtl{MOCKREA}``). To replicate the fiber assigment processing, follow the instructions in `LSS repo`_. 


Details about the content and production of the LSS catalogs that we follow for the mocks are found in `Ross et al. (2025)`_. These mocks were used in the main BAO cosmological analysis, more details in `DESI Collaboration (2025)`_.

Details comparing the three mock flavous can be found in `Bianchi et al. (2025)`_

.. _Ross et al. (2025): https://iopscience.iop.org/article/10.1088/1475-7516/2025/01/125
.. _Bianchi et al. (2025): https://iopscience.iop.org/article/10.1088/1475-7516/2025/04/074
.. _LSS repo: https://github.com/desihub/LSS/
.. _DESI Collaboration (2025): https://iopscience.iop.org/article/10.1088/1475-7516/2025/02/021

.. toctree::
   :maxdepth: 1

   mock{MOCKREA} : It contains both the FFA and Complete mock flavours, depending on the lñeven of realism <mockX/index>
   altmtl{MOCKREA} : It contains the AltMTL mock flavour, with the highest level of realism <altmtlX/index>
   forFA{MOCKREA}.fits : Initial file with tracers from the Abacus CutSky with appropiate columns and selected on the DR1 footprint <forfa-x>
   forFA{MOCKREA}_matched_input_full_lrg_imask.fits : Optional, only present for OBSCON = DARK. Used to remove LRGs affected by bright stars <lrgmask-x>
