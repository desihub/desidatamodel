====
full
====

``full`` contains information on all targets identified as reachable by DESI fiberassign, split by target types (LRG, ELG, QSO and BGS), including many columns of photometrically and spectroscopically derived information. These files are available before (``{VETO}`` = ``_noveto`` in the file name) and after vetos related to angular coordinates are applied. 

It includes both data for randoms (given ``{RANN}`` number) and data. These files are created from the :ref:`inputs_wspec<inputs_wspec>` files.

The catalogs that are prepared for clustering measurements in the ``clustering`` directory are derived from these catalogs.

.. toctree::
   :maxdepth: 1

   TARGET_RANN_fullVETO.ran.fits : Information on all random targets identified as reachable <fullVETO_ran>
   TARGET_fullVETO.dat.fits : Information on all observed targets identified as reachable <fullVETO_dat>
   
  
