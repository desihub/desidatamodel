===========
VERSION
===========

:envvar:`VERSION` contains the clustering catalogs for each target separately and the associated random catalogs. It can be like `test` or X.Y (`1.1` or `3` for example).
Here clustering catalogs are found, as well as the xi statistics in ``xi`` and some validation plots in ``plots``

.. toctree::
   :maxdepth: 1

   {target}_full_noveto.dat.fits : Selection of a specific target type, consolidated from previous steps. No veto masked applied. <target> = LRG, ELG, QSO, BGS_ANY, BGS_BRIGHT, ELG_HIP (ELG_HIPnotqso), LRG_main. <full_noveto>
   {target}_full.dat.fits : Selection of a specific type, AFTER veto mask applied. The main clustering catalog is built from this. <target> = LRG, ELG, QSO, BGS_ANY, BGS_BRIGHT, ELG_HIP (ELG_HIPnotqso), LRG_main. <full>
   {target}_{reg}_clustering.dat.fits : Main catalog for clustering statistics, including weights. <target> = LRG, ELG, QSO, BGS_ANY, BGS_BRIGHT, ELG_HIP (ELG_HIPnotqso), LRG_main. <reg> = N, S or empty value (for both north and south). <clustering>
   {target}_{RANNUM}_full_noveto.ran.fits : Randoms selected to specific target type. No veto masked applied. <target> = LRG, ELG, QSO, BGS_ANY, BGS_BRIGHT, ELG_HIP (ELG_HIPnotqso), LRG_main. <RANNUM> is random number. <full_noveto_random>
   {target}_{RANNUM}_full.ran.fits : Randoms selected to specific target type, AFTER veto mask applied. <target> = LRG, ELG, QSO, BGS_ANY, BGS_BRIGHT, ELG_HIP (ELG_HIPnotqso), LRG_main. <RANNUM> is random number. <full_random>
   {target}_{reg}_{RANNUM}_clustering.ran.fits : Randoms associated to a clustering catalog, for given target and region. <target> = LRG, ELG, QSO, BGS_ANY, BGS_BRIGHT, ELG_HIP (ELG_HIPnotqso), LRG_main. <reg> = N, S or empty value (for both north and south). <RANNUM> is random number. <clustering_random>
   {target}_comp_tile.fits : Completeness for set of tiles given a target. <target> = LRG, ELG, QSO, BGS_ANY, BGS_BRIGHT, ELG_HIP (ELG_HIPnotqso), LRG_main <comp_tile>
   {target}_comp_tileloc.fits : Completeness as a function of tilelocid given a target. <target> = LRG, ELG, QSO, BGS_ANY, BGS_BRIGHT, ELG_HIP (ELG_HIPnotqso), LRG_main <comp_tileloc>
   {target}_{reg}_nz.txt : N(z) distribution.  <target> = LRG, ELG, QSO, BGS_ANY, BGS_BRIGHT, ELG_HIP (ELG_HIPnotqso), LRG_main. <reg> = N, S or empty value (for both north and south) <nz>
   plots/index
   xi/index
