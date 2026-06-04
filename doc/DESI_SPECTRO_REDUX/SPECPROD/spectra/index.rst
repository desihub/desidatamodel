=======
spectra
=======

Starting with the Matterhorn production (test run for DR3), 
spectra are grouped by ``spectra/SURVEY/PROGRAM/PIXGROUP/UNIQPIX``, where
``UNIXPIX = HEALPIX + 4*NSIDE^2`` are adaptively-sided healpixels to balance
the number of targets per file.

For current public releases, see the :doc:`healpix <../healpix/index>` directory tree
which uses fixed-size nside=64 healpixels.

.. toctree::
   :maxdepth: 1

   SURVEY/index
