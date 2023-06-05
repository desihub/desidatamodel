===============================
Welcome to the DESI Data Model!
===============================

The DESI Data Tree
------------------

These pages define the directory structure and file formats for DESI
data products relative to a root directory :envvar:`DESI_ROOT`.
Each data release has its own :envvar:`DESI_ROOT`, e.g. the
`Early Data Release <https://data.desi.lbl.gov/doc/releases/edr/>`_
at https://data.desi.lbl.gov/public/edr.

Data Directories
================

Directories under DESI_ROOT

   * `spectro/data/NIGHT/EXPID/ <DESI_SPECTRO_DATA/NIGHT/EXPID/index.html>`_: Raw data 
   * `spectro/redux/SPECPROD/ <DESI_SPECTRO_REDUX/SPECPROD/index.html>`_: Processed spectra, classifications, and redshifts 
   * `target/ <DESI_TARGET/index.html>`_: Target selection and fiber assignment catalogs
   * `vac/RELEASE/ <DESI_ROOT/vac/RELEASE/index.html>`_: Value Added Catalogs

The following directories are more expert-level (e.g. pipeline calibration inputs)
and are documented for DESI collaboration internal use and may not be included
in data releases:

   * `survey/ops/surveyops/ <DESI_SURVEYOPS/index.html>`_: Data files used for day-to-day survey operations
   * `spectro/desi_spectro_calib/ <DESI_SPECTRO_CALIB/index.html>`_: Spectrograph calibration data
   * `protodesi/ <PROTODESI/index.html>`_: Data and logs from the ProtoDESI campaign (no spectra)
   * `$DESISURVEY_OUTPUT <DESISURVEY_OUTPUT/index.html>`_: Outputs from desisurvey and surveysim
   * `$DESI_SPECTRO_SIM <DESI_SPECTRO_SIM/index.html>`_: Simulated spectro data
   * `$DESIMODEL <DESIMODEL/index.html>`_: Data used for simulating DESI


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
=================

.. toctree::
   :maxdepth: 1

   bitmasks
   Environment variables <envvar>

Imaging data and their catalogs are documented separately by the
`Legacy Survey <https://www.legacysurvey.org/>`_.

The desidatamodel_ package on GitHub includes the data model input files
and some Python utility code for generating and checking data model files.

.. toctree::
   :maxdepth: 1

   datamodel
   api
   changes


.. _desidatamodel: https://github.com/desihub/desidatamodel

References
----------

  * Target Selection: `Myers, A. D., et al. 2023, AJ 165, 50 <https://ui.adsabs.harvard.edu/abs/2023AJ....165...50M/abstract>`_
  * Spectroscopic Pipeline: `Guy, J., et al. 2023, AJ 165, 4, 144 <https://ui.adsabs.harvard.edu/abs/2023AJ....165..144G/abstract>`_
  * Early Data Release: **TODO: arxiv link**

Index and Search Pages
----------------------

* :ref:`genindex`
* :ref:`search`

