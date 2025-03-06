==========
VERSIONpip
==========

VERSIONpip contains same catalogs as :ref:`VERSION <clustering_dr>`, but with completeness weights that are built from the record of alternative fiber assignment histories. These assignment histories also allow pairwise-inverse-probability (PIP) weights to be calculated for 2-point clustering measurements. Healpix maps are the same and are found in the same :ref:`hpmaps VERSION <hpmaps_lsscats>` directory. 


.. toctree::
   :maxdepth: 1

   {TARGET}_frac_tlobs.fits : For list of tileids, FRAC_TLOBS <frac_tlobs_pip>
   {TARGET}_full{VETO}.dat.fits : Information on all observed targets identified as reachable <data_full_pip>
   {TARGET}_{RANN}_full{VETO}.ran.fits : Information on all random targets identified as reachable <random_full_pip>
   {TARGET}_{GALCAP}_nz.txt : Target densities as a function of redshift <nz_lss_pip>
   {TARGET}_{GALCAP}_{RANN}_clustering.ran.fits : Use for clustering measurements (randoms) <random_clustering_pip>
   {TARGET}_{GALCAP}_clustering.dat.fits : Use for clustering measurements (data) <data_clustering_pip>


.. toctree::
   :maxdepth: 1

