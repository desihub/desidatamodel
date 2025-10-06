=============
mock{MOCKREA}
=============

``${DESI_ROOT}/survey/catalogs/{RELEASE}/MOCKS/AbacusSummit/{OBSCON}/{VERSION}/altmtl{MOCKREA}/mock{MOCKREA}`` contains intermediate files reading from the forFA files and altmtl outputs (in the fba directory), as well as intermediate randoms files. Also the directory with the clustering ready catalogs (LSScats) is found here. ``{MOCKREA}`` is the realization number (25 of them) 



.. toctree::
   :maxdepth: 1

   LSScats/index
   Alltiles_{OBSCON}_tilelocs.dat.fits : Information on the tiles and locations <Alltiles_tilelocs_mock>
   collision_{OBSCON}_mock{MOCKREA}.fits : Information of fiber and positions with collisions <collisions-obscon_mock> 
   datcomb_{OBSCON}_tarspecwdup_zdone.fits : Merged files reached by fibers <datcomb_tarspecwdup_zdone_mock>
   rancomb_{RANN}{OBSCON}wdupspec_zdone.fits : Initial randoms associated with a given OBSCON with RANN from 0 to 17 (both included) <rancomb_wdupspec_zdone_mock>
   rancomb_{RANN}{OBSCON}_Alltilelocinfo.fits : List of unique TARGETIDs with number of appearances as reachable according to fiber assigment <rancomb_Alltilelocinfo_mock> 
