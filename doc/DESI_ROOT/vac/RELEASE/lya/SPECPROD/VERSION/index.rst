=======
VERSION
=======

This is the Lyman alpha catalog for the DESI EDR data.

.. toctree::
   :maxdepth: 1

   delta_attributes
   delta-HEALPIX
   rejection_log

Description
===========

This value-added catalog contains the measured Lyman-alpha forest fluctuations from DESI EDR data. A paper describing this catalog will be released soon (https://desi.lbl.gov/desipub/app/PB/pub/show_publication?pubid=210). 

Reproduction
============

To reproduce this catalog, the software picca is needed. Instructions to install it can be found in its GitHub repo: https://github.com/igmhub/picca (will include a tagged version when the final catalog is out). 

Once the code is installed, the catalog can be easily reproduced by using the configuration files under `configs/`. First the calibration:

.. code-block:: bash

    picca_delta_extraction.py configs/delta_extraction_ciii_calib_step_1.ini

and then the actual Lyman-alpha run:

.. code-block:: bash

    picca_delta_extraction.py configs/delta_extraction_lya.ini

These two scripts should be run using slurm jobs with about 2 hours of walltime.

File structure
==============

The flux-transmission field is stored under ``Delta/``. This folder contains per-healpixel files ``delta-*.fits.gz``. They contain the mentioned flux-transmission field, metadata and quasar continua.

Under ``Log/`` there are complementary output files:

* ``delta_attributes(_iteration*).fits.gz``: These files contain information about the fits performed in the analysis, for variance functions and forest continua. They also contain delta statistics at each iteration.
* ``rejection_log.fits.gz``: Forest can be rejected for multiple reasons, this file contains the rejection reason for each of them.

Under ``configs/`` there are the files required to reproduce the results:

* ``continuum_fitting_mask.txt``: This file contains the mask used in our runs
* ``delta_extraction_ciii_calib_step_1.ini``: This file contains the configuration used for the calibration run
* ``delta_extraction_lya.ini``: This file contains the configuration used for the actual run

Data model
==========

* For the flux-transmission field files under ``Deltas/`` see ``delta-HEALPIX.md``
* For the attributes files under ``Log/`` see ``delta_attributes.md``
* For the rejection log under ``Log/`` see ``rejection_log.md``
