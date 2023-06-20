.. _clustering:

==========
clustering
==========

``clustering`` contains LSS catalogs, separated by target types (:ref:`see here for references<lsscats>`), that have been prepared to be used directly to obtain clustering statistics. It includes both data for randoms (separated into 18 files given ``{RANN}``).

Descriptions on how to use these to obtain clustering measurements are fully given in `EDR. DESI Collaboration (in prep.)`_ and in `Lasker et al (in prep.)`_. Any cuts applied to the data catalogs should be equally applied to the random catalogs.

Any number of the random catalogs, ``{RANN}`` can be used (with the impact only on statistical precision). Large-scale clustering measurements can be accurately obtained via the columns :py:attr:`RA`, :py:attr:`DEC`, :py:attr:`Z`, :py:attr:`WEIGHT`.

For small-scales, pairwise inverse-probability (PIP) weights can be obtained via the BITWEIGHTS column and we further recommend angular up-weighting (as in `Mohammad et al. (2020)`_). If using PIP weights, the :py:attr:`WEIGHT` column should still be used for the random counts (but not used for the data counts).

.. _EDR. DESI Collaboration (in prep.): https://arxiv.org/abs/2306.06308
.. _Lasker et al (in prep.): https://ui.adsabs.harvard.edu/public-libraries/XCj7bW-vSMaNZVV0C0QyGA
.. _Mohammad et al. (2020): https://academic.oup.com/mnras/article/498/1/128/5891251

.. toctree::
   :maxdepth: 1

   TARGET_PHOTSYS_RANN_clustering.ran.fits : Use for clustering measurements (randoms) <clustering_ran>
   TARGET_PHOTSYS_clustering.dat.fits : Use for clustering measurements (data) <clustering_dat>

