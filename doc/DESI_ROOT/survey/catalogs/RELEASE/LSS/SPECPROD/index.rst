========
SPECPROD
========

``${DESI_ROOT}/survey/catalogs/RELEASE/LSS/SPECPROD`` contains initial compacted files that reads from fiber assigment and spectroscopic reduction data, separated by PHOTSYS (``bright`` and ``dark``). Also compiled initial files separated by target types BGS_ANY, BGS_BRIGHT (for PHOTSYS = bright), LRG, ELG_LOPnotqso, QSO (for PHOTSYS = dark), as well as the end-products LSS catalogs (``LSScats``) and initial processed random catalogs (18 realizations).   

.. toctree::
   :maxdepth: 1

   LSScats/index
   rancomb_{RANN}{PHOTSYS}wdupspec_zdone.fits : Initial randoms associated with a given PHOTSYS with RANN from 0 to 17 (both included) <rancomb_wdupspec_zdone>
   unique_badfibers.txt : List of bad fibers for the given release <unique_badfibers>
   emlin_catalog.fits : Emission lines catalogs used in the spectroscopic reduction version (SPECPROD) <emlin_catalog>
   datcomb_{PHOTSYS}_spec_zdone.fits : Compacted catalog file of all fiber assigments <datcomb_photsys_spec>
   datcomb_{PHOTSYS}_zmtl_zdone.fits : Compacted catalog file of redshift fitting after spectroscopic reduction <datcomb_photsys_zmtl>
   datcomb_{TARGET}_tarspecwdup_zdone.fits : Merged files separated per TARGET type reached by fibers <datcomb_tarspecwdup_zdone>
