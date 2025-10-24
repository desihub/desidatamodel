=============
mock{MOCKREA}
=============

For each EZmock realization here you will find  the FFA flavour (``ffa``). ``{OBSCON}`` can be either ``dark`` or ``bright``.

  * FFA clustering files

For the FFA clustering catalogs, we also share the ``full`` catalogs.

This directory also includes 18 randoms associated for each realization.

We add another sample unique to EZmock (not present for Abacus) defined as the combination of LRGs and ELGs, called ``LRG+ELG_LOP``. More information about this can be found in: `Valcin et al. (2025)`_


Large-scale clustering measurements can be accurately obtained via the columns :py:attr:`RA`, :py:attr:`DEC`, :py:attr:`Z`, :py:attr:`WEIGHT`. Samples are split by Galactic hemisphere, defined by GALCAP ``NGC`` and ``SGC`` or combined without distinction.

.. warning::

   **CAVEAT WITH REALIZATION 925 for OBSCON = DARK:** In this realization we are missing the files pota-DARK.fits and combdark_wdupspec_zdone.fits, therefore this realization is not replicable from scratch. Nonetheless, the rest of files are good, including the clustering catalogs.

.. _Valcin et al. (2025): https://arxiv.org/abs/2508.05467v2

.. toctree::
   :maxdepth: 1

   pota-{OBSCON}.fits : potential assigment for all tracers combined <potential_mock>
   {TRACER}_{FLAVOUR}_nz.txt : Tracer densities as a function of redshift, in the given flavour <nz_lss_mock>
   {TRACER}_{FLAVOUR}_{GALCAP}_{RANN}_clustering.ran.fits : Use for clustering measurements (randoms) <mock_ran_clustering>
   {TRACER}_{FLAVOUR}_{GALCAP}_clustering.dat.fits : Use for clustering measurements (data) <mock_clustering>
   ffa_full_{TRACER}.fits : full sample for the ffa flavour, separated by tracer <full_ffa_mock>
   comb{OBSCON}_wdupspec_zdone.fits : Match of potential assigments with parent mock catalog <comb_wdupspec_zdone> 
