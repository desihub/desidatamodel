===
LSS
===

``${DESI_ROOT}/survey/catalogs/RELEASE/LSS`` host the LSS catalogs tagged by the spectroscopic production used (SPECPROD), named after mountains, e.g. “iron” for DR1. Normally, we will publish just one SPECPROD per data release.

In addition, we include initial 18 random files with all potential assigments (randomRANN) and products used to calculate the PIP weights with the AltMTL method (altmtl; Lasker et al. 2024).

.. toctree::
   :maxdepth: 1

   SPECPROD/index
   randomRANN/index
   altmtl/index
   tiles-OBSCON.fits The list of tiles <tiles-obscon>
   collisions-OBSCON.fits list of FIBER and LOCATION positions that are rejected from fiber assignment due to collisions with pre-defined keep out zones in the focal plane <collisions-obscon>
