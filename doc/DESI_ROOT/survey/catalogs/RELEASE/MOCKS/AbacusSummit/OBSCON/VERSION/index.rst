

============
AbacusSummit
============

``${DESI_ROOT}/survey/catalogs/RELEASE/MOCKS/AbacusSummit/OBSCON/VERSION`` host 25 Abacus LSS catalogs (and associated randoms) separated by OBSCON: ``DARK`` or ``BRIGHT`` and followed by internal version, where for ``DARK`` (LRG, ELG and QSO) is ``v4.2`` and for ``BRIGHT`` (BGS) is ``v2``. 

From the landing page, you will find the initial catalog in the Y1 footprint (called forFA files), the lrg_mask file (used only to mask LRGs, present only on the ``DARK`` obscon) and 2 directories called ``altmtlX`` and ``mockX`` where ``X`` is the mock realization from [0,25). 

Here you can find 3 distinct mock flavours depending on the level of realism:
- Complete: no fiber assigment, it is all the catalog that is reachable by any DESI fiber (found under ``mockX``)
- FFA: estimate fiber assigment probabilistically learning from the data, based on number of passes and local density (found under ``mockX``)
- altmtl: Estimated using the same fba algorithm, passes and hardware configuration as the data (found under ``altmtlX``). 
        * For one realization in OBSCON = ``DARK``, we have also estimated PIP weights based on 128 fba repetitions (see the AltMTL method; `Lasker et al. (2025)`_)


Details about the content and production of the LSS catalogs that we follow for the mocks are found in `Ross et al. (2025)`_
Details comparing the three mock flavous can be found in `Bianchi et al. (2025)`_

.. _Lasker et al. (2025): https://iopscience.iop.org/article/10.1088/1475-7516/2025/01/127
.. _Ross et al. (2025): https://iopscience.iop.org/article/10.1088/1475-7516/2025/01/125
.. _Bianchi et al. (2025): https://iopscience.iop.org/article/10.1088/1475-7516/2025/04/074

.. toctree::
   :maxdepth: 1

   mockX/index
   altmtlX/index
   forFA{X}.fits : Initial file with tracers from the Abacus CutSky with appropiate columns and selected on the DR1 footprint <forfa-x>
   forFA{X}_matched_input_full_lrg_imask.fits : Optional, only present for OBSCON = DARK. Used to remove LRGs affected by bright stars <lrgmask-x>
