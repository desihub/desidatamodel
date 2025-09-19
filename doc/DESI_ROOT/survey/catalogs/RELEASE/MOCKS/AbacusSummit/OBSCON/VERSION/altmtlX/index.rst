

=======
altmtlX
=======

``${DESI_ROOT}/survey/catalogs/RELEASE/MOCKS/AbacusSummit/OBSCON/VERSION/altmtlX`` host the AltMTL LSS mock catalogs (and associated randoms) for each ``X`` realization

Here you will find two directories, fbaX contains the compilation of running fiber assigment after running the altmtl pipeline (not public, but replicated `following the instructions in LSS code`_) and mockX contains intermediate files and final clustering files (unders LSScats directory, following the same structure as the data)

.. _following the instructions in LSS code: https://github.com/desihub/LSS/blob/main/Sandbox/LSSpipe_Y1mock_2ndgen.txt

.. toctree::
   :maxdepth: 1

   fbaX/index
   mockX/index
