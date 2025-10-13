.. _clustering_altmtl_mock:

====================
LSScats AbacusSummit
====================

LSScats contains the most realistic LSS catalogs, separated by target types, that have been prepared to be used directly to obtain clustering statistics. It includes both data for randoms (separated into 18 files given RANN).

Any number of the random catalogs, ``RANN`` can be used (with the impact only on statistical precision).  

``full`` contains information on all targets identified as reachable by DESI fiberassign, split by target types (LRG, ELG, QSO and BGS), including many columns of photometrically and spectroscopically derived information. These files are available before (``{VETO}`` = ``_noveto`` in the file name), after vetos related to angular coordinates are applied (blank) and after an extra healpix map cut is applied (``{VETO}`` = ``_HPmapcut`` in the file name).

Large-scale clustering measurements can be accurately obtained via the columns :py:attr:`RA`, :py:attr:`DEC`, :py:attr:`Z`, :py:attr:`WEIGHT`. Samples are split by Galactic hemisphere, defined by GALCAP ``NGC`` and ``SGC``.

.. _Ross et al. (2025): https://iopscience.iop.org/article/10.1088/1475-7516/2025/01/125

.. toctree::
   :maxdepth: 1

   {TARGET}_frac_tlobs.fits : For list of tileids, FRAC_TLOBS <frac_tlobs_mock>
   {TARGET}_full{VETO}.dat.fits : Information on all observed targets identified as reachable <data_full_mock_altmtl>
   {TARGET}_{RANN}_full{VETO}.ran.fits : Information on all random targets identified as reachable <random_full_mock_altmtl>
   {TARGET}_{GALCAP}_nz.txt : Target densities as a function of redshift <nz_lss_mock_altmtl>
   {TARGET}_{GALCAP}_{RANN}_clustering.ran.fits : Use for clustering measurements (randoms) <random_clustering_mock_altmtl>
   {TARGET}_{GALCAP}_clustering.dat.fits : Use for clustering measurements (data) <data_clustering_mock_altmtl>
