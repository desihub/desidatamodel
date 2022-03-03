===
mtl
===

``mtl`` is the root directory for the Merged Target List ledgers. The MTL
ledgers record the state of each DESI target as redshift information is
acquired. There is a set of ledgers for each of phase 2 of Survey Validation
(``sv2``) the One-Percent Survey (``sv3``) and the Main Survey (``main``).

The ``mtl-done-tiles.ecsv`` and ``scnd-mtl-done-tiles.ecsv`` files in the
``mtl`` directory track which tiles have had target states updated over the
course of all DESI survey phases (i.e. all of ``sv2``, ``sv3`` and ``main``).


Files and subdirectories:

.. toctree::
   :maxdepth: 1

   mtl-done-tiles.ecsv : Record of updated tiles for primary targets <mtl-done-tiles>
   scnd-mtl-done-tiles.ecsv : Record of updated tiles for secondary targets <scnd-mtl-done-tiles>
   main/index
   sv2/index
   sv3/index

