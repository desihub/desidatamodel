======
forFA
======

``${DESI_ROOT}/survey/catalogs/{RELEASE}/mocks/EZmock/{OBSCON}/{VERSION}/forFA`` host 1000 parent EZmock catalogs and associated LRG masks (present only on the ``DARK`` obscon).

Details about the content and production of the LSS catalogs that we follow for the mocks are found in `Ross et al. (2025)`_

.. _Ross et al. (2025): https://iopscience.iop.org/article/10.1088/1475-7516/2025/01/125

.. toctree::
   :maxdepth: 1

   forFA{MOCKREA}.fits : Initial file with tracers from the Abacus CutSky with appropiate columns and selected on the DR1 footprint <forfa-x>
   forFA{MOCKREA}_matched_input_full_lrg_imask.fits : Optional, only present for OBSCON = DARK. Used to remove LRGs affected by bright stars <lrgmask-x>
