===============================
Welcome to the DESI Data Model!
===============================

The DESI Data Tree
------------------

These pages define the directory structure and file formats for DESI
data products relative to a root directory :envvar:`DESI_ROOT`.
Each data release has its own :envvar:`DESI_ROOT`, *e.g.* the
`Data Release 1 <https://data.desi.lbl.gov/doc/releases/dr1/>`_
at https://data.desi.lbl.gov/public/dr1.

Data Directories
----------------

Directories under :envvar:`DESI_ROOT`:

   * :doc:`spectro/redux/SPECPROD/ <DESI_SPECTRO_REDUX/SPECPROD/index>`: Processed spectra, classifications, and redshifts
   * :doc:`survey/catalogs/RELEASE/LSS <DESI_ROOT/survey/catalogs/RELEASE/LSS/index>`: The Large Scale Structure catalog
   * :doc:`vac/RELEASE/ <DESI_ROOT/vac/RELEASE/index>`: Value Added Catalogs
   * :doc:`target/ <DESI_TARGET/index>`: Target selection and fiber assignment catalogs
   * :doc:`spectro/data/NIGHT/EXPID/ <DESI_SPECTRO_DATA/NIGHT/EXPID/index>`: Raw data

The following directories are more expert-level (*e.g.* pipeline calibration inputs)
and are documented for DESI collaboration internal use and may not be included
in data releases:

   * :doc:`survey/ops/surveyops/ <DESI_SURVEYOPS/index>`: Data files used for day-to-day survey operations
   * :doc:`spectro/desi_spectro_calib/ <DESI_SPECTRO_CALIB/index>`: Spectrograph calibration data
   * :doc:`protodesi/ <PROTODESI/index>`: Data and logs from the ProtoDESI campaign (no spectra)
   * :doc:`$DESISURVEY_OUTPUT <DESISURVEY_OUTPUT/index>`: Outputs from desisurvey and surveysim
   * :doc:`$DESI_SPECTRO_SIM <DESI_SPECTRO_SIM/index>`: Simulated spectro data
   * :doc:`$DESIMODEL <DESIMODEL/index>`: Data used for simulating DESI


.. comment: the following toctree items exist to keep sphinx happy, but
   are purposefully hidden (e.g. because the text above links
   a level deeper)

.. toctree::
   :hidden:

   vac/ : Value Added Catalogs <DESI_ROOT/vac/index>
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


Other information
-----------------

Bitmask definitions and environment variables used by the DESI data pipelines:

.. toctree::
   :maxdepth: 1

   bitmasks
   column_descriptions
   Environment variables <envvar>
   Units in data files <units>

Imaging data and their catalogs are documented separately by the
`Legacy Survey <https://www.legacysurvey.org/>`_.

The desidatamodel_ package on GitHub includes the data model input files
and some Python utility code for generating and checking data model files.
These links will be useful for developers:

.. toctree::
   :maxdepth: 1

   datamodel
   api
   changes


.. _desidatamodel: https://github.com/desihub/desidatamodel

References
----------

* Target Selection: `Myers, A. D., et al. 2023, AJ 165, 50 <https://ui.adsabs.harvard.edu/abs/2023AJ....165...50M/abstract>`_
* Spectroscopic Pipeline: `Guy, J., et al. 2023, AJ 165, 144 <https://ui.adsabs.harvard.edu/abs/2023AJ....165..144G/abstract>`_
* Early Data Release: `DESI Collaboration et al. 2024, AJ 168, 58 <https://ui.adsabs.harvard.edu/abs/2024AJ....168...58D/abstract>`_
* Data Release 1: `DESI Collaboration et al. 2025, in prep <https://arxiv.org>`_

Index and Search Pages
----------------------

* :ref:`genindex`
* :ref:`search`

