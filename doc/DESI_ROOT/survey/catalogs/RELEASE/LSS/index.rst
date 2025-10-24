.. _catalogs:


===
LSS
===

``${DESI_ROOT}/survey/catalogs/RELEASE/LSS`` host the LSS catalogs tagged by the spectroscopic production used (SPECPROD), named after mountains, e.g. ``iron`` for DR1. Normally, we will publish just one SPECPROD per data release.

In addition, we include initial 18 random files with all potential assigments (randomRANN), products used to calculate the PIP weights with the AltMTL method (altmtl; `Lasker et al. (2025)`_), as well as auxiliary files associated with the given release: the list of tiles for the given release and the list of fibers that collide, for a given OBSCON: ``DARK`` or ``BRIGHT``.

Details about the content and production of the LSS catalogs are found in `Ross et al. (2025)`_

.. _Lasker et al. (2025): https://iopscience.iop.org/article/10.1088/1475-7516/2025/01/127
.. _Ross et al. (2025): https://iopscience.iop.org/article/10.1088/1475-7516/2025/01/125

.. toctree::
   :maxdepth: 1

   SPECPROD/index
   randomRANN/index
   altmtl/index
   tiles-{OBSCON}.fits : List of tiles <tiles-obscon>
   collisions-{OBSCON}.fits : List of FIBER and LOCATION positions that are rejected from fiber assignment due to collisions with pre-defined keep out zones in the focal plane <collisions-obscon>
