===============================
Welcome to the DESI Data Model!
===============================

The DESI Data Tree
------------------

DESI data are grouped broadly by category, using environment variables to
define the base directory under which files of that category are kept.
These variables have a standard location relative to :envvar:`DESI_ROOT`, but code
uses these variables so that one can swap out different input/output locations
for testing.

.. toctree::
   :maxdepth: 1

   $DESI_ROOT : represents the top level of the DESI directory tree. <DESI_ROOT/index>
   $DESI_SPECTRO_DATA : raw data <DESI_SPECTRO_DATA/index>
   $DESI_SPECTRO_REDUX : processed spectro data <DESI_SPECTRO_REDUX/index>
   $DESI_SPECTRO_SIM : simulated spectro data <DESI_SPECTRO_SIM/index>
   $DESI_SPECTRO_CALIB : spectro calibration data <DESI_SPECTRO_CALIB/index>
   $DESI_SURVEYOPS : data files used for day-to-day survey operations <DESI_SURVEYOPS/index>
   $DESI_TARGET : target selection and fiber assignment (see also Myers et al. 2023) <DESI_TARGET/index>
   $DESIMODEL : data used for simulating DESI <DESIMODEL/index>
   $DESISURVEY_OUTPUT : outputs from desisurvey and surveysim <DESISURVEY_OUTPUT/index>
   $PROTODESI : data and logs from the ProtoDESI campaign <PROTODESI/index>
   bitmasks
   datamodel
   api
   changes

Imaging data and their catalogs are documented separately by the
`Legacy Survey <https://www.legacysurvey.org/>`_.

The desidatamodel_ package on GitHub includes the data model input files
and some Python utility code for generating and checking data model files.

.. _desidatamodel: https://github.com/desihub/desidatamodel

References
----------

`Myers, A. D., et al., AJ 165, 50, 2023 <https://ui.adsabs.harvard.edu/abs/2023AJ....165...50M/abstract>`_

Indices and Tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

