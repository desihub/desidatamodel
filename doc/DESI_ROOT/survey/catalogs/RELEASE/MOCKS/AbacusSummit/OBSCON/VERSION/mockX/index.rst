.. _clustering_mock_complete_ffa:

=====
mockX
=====

For each mock realization here you will find 3 classes of file. The FFA or complete flavour is controled by the parameter ``FLAVOUR`` (``complete`` or ``ffa``)
- Potential assigment files (for all tracers or under some configurations, for each tracer separately)
- FFA clustering files (only present for ``OBSCON`` = DARK)
- Complete clustering files

For the FFA clustering catalogs, we also share the ``full`` catalogs.

This directory also includes 18 randoms associated for each realization, for each flavour

Large-scale clustering measurements can be accurately obtained via the columns :py:attr:`RA`, :py:attr:`DEC`, :py:attr:`Z`, :py:attr:`WEIGHT`. Samples are split by Galactic hemisphere, defined by GALCAP ``NGC`` and ``SGC`` or combined without distinction.

.. toctree::
   :maxdepth: 1

   pota-{OBSCON}.fits and pota-{OBSCON}_{TAG}_{TARGET}.fits : potential assigment for all tracers combined, or separated by TRACER under TAG circumstances (joined_unreduced or withntile) <potential_mock>
   {TRACER}_{FLAVOUR}_nz.txt : Tracer densities as a function of redshift, in the given flavour <nz_lss_mock>
   {TRACER}_{FLAVOUR}_{GALCAP}_{RANN}_clustering.ran.fits : Use for clustering measurements (randoms) <mock_ran_clustering>
   {TRACER}_{FLAVOUR}_{GALCAP}_clustering.dat.fits : Use for clustering measurements (data) <mock_clustering>
   ffa_full_{TRACER}.fits : full sample for the ffa flavour, separated by tracer <full_ffa_mock>
