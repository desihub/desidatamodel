===============================
Welcome to the DESI Data Model!
===============================

The DESI Data Tree
------------------

DESI data are grouped broadly by category, using environment variables to
define the base directory under which files of that category are kept.
These variables have a standard location relative to $DESI_ROOT, but code
uses these variables so that one can swap out different input/output locations
for testing.

.. toctree::
   :maxdepth: 1

   $DESI_SPECTRO_DATA : raw data <DESI_SPECTRO_DATA/index>
   $DESI_SPECTRO_REDUX : processed spectro data <DESI_SPECTRO_REDUX/index>
   $DESI_SPECTRO_SIM : simulated spectro data <DESI_SPECTRO_SIM/index>
   $DESI_SPECTRO_CALIB : spectro calibration data <DESI_SPECTRO_CALIB/index>
   $DESI_SURVEY : contains data related to daily operations, fiberassignment, etc. <DESI_SURVEY/index>
   $DESI_SURVEYOPS : data files used for day-to-day survey operations <DESI_SURVEYOPS/index>
   $DESI_TARGET : target selection and fiber assignment (see also `Myers *et al.* 2023`_) <DESI_TARGET/index>
   $DESIMODEL : data used for simulating DESI <DESIMODEL/index>
   $DESISURVEY_OUTPUT : outputs from desisurvey_ and surveysim_ <DESISURVEY_OUTPUT/index>
   $PROTODESI : data and logs from the ProtoDESI campaign <PROTODESI/index>
   bitmasks
   datamodel
   api
   changes

Imaging data and their catalogs are documented separately by the
`Legacy Survey <http://legacysurvey.org/>`_.

.. _desisurvey: https://github.com/desihub/desisurvey
.. _surveysim: https://github.com/desihub/surveysim
.. _`Myers *et al.* 2023`: https://ui.adsabs.harvard.edu/abs/2023AJ....165...50M/abstract

Indices and Tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
