========================
desidatamodel Change Log
========================

23.1 (unreleased)
-----------------

* Update column descriptions for galaxy clustering files meeting EDR datamodel (PR `#152`_).
* Update column descriptions for tile-based spectra/redshift/afterburner files
  (PR `#145`_).
* Update column descriptions from a master list of columns (PR `#144`_).
* Update spectra and coadd text with additional examples (PR `#143`_).
* Rename ``SURVEYOPS`` (PR `#142`_).
* Add links to maskbit definitions (PR `#139`_).
* Update :doc:`the contributing page <datamodel>` (PR `#138`_).
* Update documentation for QSO afterburner files (PR `#134`_).
* Resolve maggy/maggies discrepancies in DESI_TARGET/DESI_SURVEY (PR `#133`_).
* Update documentation of QA files (PR `#132`_).
* Document top level exposure and tile summary files (PR `#131`_).
* Populate the data model for the zmtl files (PR `#130`_).
* Improve documenetation of ``emline`` files (PR `#128`_).
* Add documentation of various calibration files (PR `#127`_).
* Further cleanup of ``fuji`` and ``guadalupe`` header keywords and columns (PR `#126`_).
* Update data model for target files to reflect ets/dr9 release (PR `#105`_).
* Update data model for fiberassign files in the tiles product (PR `#103`_).

.. _`#103`: https://github.com/desihub/desidatamodel/pull/103
.. _`#105`: https://github.com/desihub/desidatamodel/pull/105
.. _`#126`: https://github.com/desihub/desidatamodel/pull/126
.. _`#127`: https://github.com/desihub/desidatamodel/pull/127
.. _`#128`: https://github.com/desihub/desidatamodel/pull/128
.. _`#130`: https://github.com/desihub/desidatamodel/pull/130
.. _`#131`: https://github.com/desihub/desidatamodel/pull/131
.. _`#132`: https://github.com/desihub/desidatamodel/pull/132
.. _`#133`: https://github.com/desihub/desidatamodel/pull/133
.. _`#134`: https://github.com/desihub/desidatamodel/pull/134
.. _`#138`: https://github.com/desihub/desidatamodel/pull/138
.. _`#139`: https://github.com/desihub/desidatamodel/pull/139
.. _`#142`: https://github.com/desihub/desidatamodel/pull/142
.. _`#143`: https://github.com/desihub/desidatamodel/pull/143
.. _`#144`: https://github.com/desihub/desidatamodel/pull/144
.. _`#145`: https://github.com/desihub/desidatamodel/pull/145
.. _`#152`: https://github.com/desihub/desidatamodel/pull/152

22.2 (2022-05-31)
-----------------

* Updates for ``fuji`` and ``guadalupe`` reductions (PR `#102`_). Includes support for:
    * Variable-length string-valued columns.
    * Cross references to HDUs in other data models.
    * Notation for optional header keywords and columns.
    * Improved visual styling for header keyword and column description tables.
* Add data model for MTL ledgers (PR `#101`_).
* Migrated to GitHub Actions for testing.
* Update :doc:`DESI_SPECTRO_DATA <DESI_SPECTRO_DATA/index>` model based on
  Main Survey data (PR `#94`_).
* Update :doc:`DESI_SPECTRO_REDUX <DESI_SPECTRO_REDUX/index>` model based on
  ``everest`` production (PRs `#93`_, `#90`_).
* Update desitarget data model to reflect the ets release (PR `#85`_):
    * Alter filenames to add ``PHASE/OBSCON/RESOLVE`` and remove ``DR``.
    * Add full directory structure for ``DESI_TARGET/TARG_DIR``.
* Use the DR8 data model for targets and deprecate DR7 (PR `#84`_):
    * Updates columns to match the DR8 target files.
    * Adds a targets-dr8.rst file to deprecate once DR9 is released.
    * Updates the header information to match the DR8 target files.
    * Adds units for some columns.
    * Directory structure now reflects the (HEALPix-split) target files.
    * Adds urls for the DR8 target files for upcoming research notes.
* Update Travis test configuration (PR `#81`_).
* Update data model to reflect 19.9 software release (PR `#78`_).

.. _`#78`: https://github.com/desihub/desidatamodel/pull/78
.. _`#81`: https://github.com/desihub/desidatamodel/pull/81
.. _`#84`: https://github.com/desihub/desidatamodel/pull/84
.. _`#85`: https://github.com/desihub/desidatamodel/pull/85
.. _`#90`: https://github.com/desihub/desidatamodel/pull/90
.. _`#93`: https://github.com/desihub/desidatamodel/pull/93
.. _`#94`: https://github.com/desihub/desidatamodel/pull/94
.. _`#101`: https://github.com/desihub/desidatamodel/pull/101
.. _`#102`: https://github.com/desihub/desidatamodel/pull/102

19.2 (2019-10-01)
------------------

*This is primarily a reference tag to capture changes prior to the planned
19.9 release.*  The release date *does not* reflect the state of pipeline
outputs as of October 2019.

* Update raw data model based on spectrograph tests (PR `#73`_).
* Allow documentation of similar ranges of HDUs (PR `#75`_).
* Update data model for desisurvey and surveysim (PR `#70`_, `#71`_).

.. _`#70`: https://github.com/desihub/desidatamodel/pull/70
.. _`#71`: https://github.com/desihub/desidatamodel/pull/71
.. _`#73`: https://github.com/desihub/desidatamodel/pull/73
.. _`#75`: https://github.com/desihub/desidatamodel/pull/75


18.11 (2018-12-11)
------------------

* Lots of format cleanup updates (PR `#68`_).
* ``MASK`` HDUs will no longer be compressed (PR `#60`_).
* Deprecate ``DESI_TARGET`` files (``sky``, ``stdstar``) that aren't in use (PR `#59`_).
* Describe apertures in the skies file as "radius" not "size" (PR `#59`_).
* Add randoms/gfas/skies/pixweight files to the ``DESI_TARGET`` model (PR `#57`_).
* Update the targets file in the ``DESI_TARGET`` model (PR `#57`_).
* Ensure that ``BUNIT`` and ``TUNIT*`` values obey the FITS standard (PR `#54`_).

.. _`#54`: https://github.com/desihub/desidatamodel/pull/54
.. _`#57`: https://github.com/desihub/desidatamodel/pull/57
.. _`#59`: https://github.com/desihub/desidatamodel/pull/59
.. _`#60`: https://github.com/desihub/desidatamodel/pull/60
.. _`#68`: https://github.com/desihub/desidatamodel/pull/68

18.6 (2018-07-20)
-----------------

Tag for 18.6 software release (with a slight delay).

* Updates for quicklook pipeline (PR `#48`_, `#50`_).
* Raw data now stored in ``NIGHT``/``EXPID`` directories (PR `#52`_)

.. _`#48`: https://github.com/desihub/desidatamodel/pull/48
.. _`#50`: https://github.com/desihub/desidatamodel/pull/50
.. _`#52`: https://github.com/desihub/desidatamodel/pull/52

18.3 (2018-05-09)
-----------------

Tag for 18.3 software release (albeit 1.5 months later).

* Switching to YY.[M]M versioning to match software releases.
* Fill in missing file summaries and HDU descriptions (PR `#47`_).
* Update data model to reflect reference run 18.3 (PR `#46`_).
* Drop support for Python 2.

.. _`#46`: https://github.com/desihub/desidatamodel/pull/46
.. _`#47`: https://github.com/desihub/desidatamodel/pull/47

1.2.0 (2018-03-23)
------------------

* Vet data model against reference run 18.2a.  Numerous changes to data
  model Python code to support, *e.g.* compressed HDUs (PR `#42`_).
* Many accumulated changes since 2015.

.. _`#42`: https://github.com/desihub/desidatamodel/pull/42

1.1.1 (2015-11-06)
------------------

* Some fixes for Python 3 tests (PR `#5`_).

.. _`#5`: https://github.com/desihub/desidatamodel/pull/5

1.1.0 (2015-11-06)
------------------

* Use :mod:`astropy.io.fits` consistently (PR `#4`_).

.. _`#4`: https://github.com/desihub/desidatamodel/pull/4

1.0.0 (2015-10-29)
------------------

* Support for ``desiInstall``, etc. (PR `#1`_).

.. _`#1`: https://github.com/desihub/desidatamodel/pull/1

0.2.0 (2015-05-22)
------------------

* See git log files.

0.1.0 (2015-01-16)
------------------

* See git log files.

0.0.4 (2015-01-12)
------------------

* See git log files.

0.0.3 (2014-07-21)
------------------

* See git log files.

0.0.2 (2014-06-10)
------------------

* See git log files.

0.0.1 (2014-05-29)
------------------

* See git log files.
