.. _clustering_dr:

=======
VERSION
=======

VERSION contains the final LSS catalogs, separated by target types (:ref:`see here for references<lsscats>`)??? To check lsscats., that have been prepared to be used directly to obtain clustering statistics. It includes both data for randoms (separated into 18 files given ``{RANN}``).

We can also found healpix maps representing several quantities under hpmaps directory for each target separately.

Descriptions on how to use these to obtain clustering measurements are fully given in `Ross et al. (2024)`_. Any cuts applied to the data catalogs should be equally applied to the random catalogs.

Any number of the random catalogs, ``{RANN}`` can be used (with the impact only on statistical precision). 

``full`` contains information on all targets identified as reachable by DESI fiberassign, split by target types (LRG, ELG, QSO and BGS), including many columns of photometrically and spectroscopically derived information. These files are available before (``{VETO}`` = ``_noveto`` in the file name), after vetos related to angular coordinates are applied (blank) and after an extra healpix map cut is applied (``{VETO}`` = ``_HPmapcut`` in the file name).

Large-scale clustering measurements can be accurately obtained via the columns :py:attr:`RA`, :py:attr:`DEC`, :py:attr:`Z`, :py:attr:`WEIGHT`.

.. _Ross et al. (2024): https://arxiv.org/abs/2405.16593

.. toctree::
   :maxdepth: 1

   hpmaps/index
   TARGET_frac_tlobs.fits : For list of tileids, FRAC_TLOBS <frac_tlobs>
   TARGET_fullVETO.dat.fits : Information on all observed targets identified as reachable <data_full>
   TARGET_RANN_fullVETO.ran.fits : Information on all random targets identified as reachable <random_full>
   TARGET_PHOTSYS_nz.txt : Target densities as a function of redshift <nz_lss>
   TARGET_PHOTSYS_RANN_clustering.ran.fits : Use for clustering measurements (randoms) <random_clustering>
   TARGET_PHOTSYS_clustering.dat.fits : Use for clustering measurements (data) <data_clustering>
