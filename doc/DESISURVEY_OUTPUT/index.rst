=================
DESISURVEY_OUTPUT
=================

:envvar:`DESISURVEY_OUTPUT` contains the outputs of desisurvey_ and surveysim_,
with the canonical location of ``$DESI_ROOT/survey``.  We expect this
directory structure will be updated as part of integrating desisurvey
(afternoon planning and next tile selector) into online operations.

.. _desisurvey: https://github.com/desihub/desisurvey
.. _surveysim: https://github.com/desihub/surveysim

.. warning::
    These files are not expected to be released, and :envvar:`DESISURVEY_OUTPUT` is
    not normally defined automatically in the DESI environment.

.. toctree::
   :maxdepth: 1

   ephem_{start}-{stop}.fits : cached ephemeris for survey planning <ephem>
   surveyinit.fits : Design hour angles? <surveyinit>
   planner_YEAR-MM-DD.fits : Afternoon planner state <planner>
   scheduler_YEAR-MM-DD.fits : Next tile selector state <scheduler>
   stats_surveysim.fits : per-tile and per-night statistics from surveysim run <stats>
   exposures_surveysim.fits : exposure metadata from surveysim run <exposures>

