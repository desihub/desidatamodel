====================
specprod
====================

:envvar:`specprod` contains catalogs reading from :envvar:`DESI_LSS` products and spectroscopic information. 
The name reflects the name of the spectroscopic production pipeline, it can be `daily` or consolidated
versions like `everest` or `fuji`.

.. toctree::
   :maxdepth: 1

   datcomb_{program}_tarwdup_{tag}.fits : All potential fiberassigment targets with photometric info. Includes duplicates. {program} = dark or bright. {tag} = name given, like zdone (DA02) or Alltiles (SV3). <tarwdup>
   datcomb_{program}_tarspecwdup_{tag}.fits : All potential fiberassigment targets with spectroscopic and photometric info. Includes duplicates. {program} = dark or bright. {tag} = name given, like zdone (DA02) or Alltiles (SV3). <tarspecwdup>
   Alltiles_{program}_tilelocs.dat.fits: List of unique TARGETIDs with number of observations per tile. {program} = dark or bright <Alltiles>
   rancomb_{RANNUM}{program}_Alltilelocinfo.fits : List of random points with number of observations. {program} = dark or bright. {RANNUM} is the random number <Alltiles_random>
   rancomb_{RANNUM}{program}wdupspec_{tag}.fits : All potential fiberassigments on randoms. {program} = dark or bright. {RANNUM} is the random number. {tag} = name given, like zdone (DA02) or Alltiles (SV3). <wdupspec_random>
   LSScats/index
