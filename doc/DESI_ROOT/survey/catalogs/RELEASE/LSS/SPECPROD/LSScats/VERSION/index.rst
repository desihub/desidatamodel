.. _clustering:

=======
VERSION
=======

VERSION contains the final LSS catalogs, separated by target types (:ref:`see here for references<lsscats>`), that have been prepared to be used directly to obtain clustering statistics. It includes both data for randoms (separated into 18 files given ``{RANN}``).

We can also found healpix maps representing several quantities under hpmaps directory for each target separately.

Descriptions on how to use these to obtain clustering measurements are fully given in `Ross et al. (2024)`_. Any cuts applied to the data catalogs should be equally applied to the random catalogs.

Any number of the random catalogs, ``{RANN}`` can be used (with the impact only on statistical precision). Large-scale clustering measurements can be accurately obtained via the columns :py:attr:`RA`, :py:attr:`DEC`, :py:attr:`Z`, :py:attr:`WEIGHT`.

.. _Ross et al. (2024): https://arxiv.org/abs/2405.16593

.. toctree::
   :maxdepth: 1

   hpmaps/index
