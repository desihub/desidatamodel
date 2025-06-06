========================
desidatamodel Change Log
========================

25.4 (unreleased)
-----------------

* No changes yet.

25.3 (2025-03-17)
-----------------

* Update package infrastructure, fix search function, add missing columns (PR `#199`_).
* Update the units for ``SKY_MAG_*`` quantities in the ``SPECPROD/exposures-SPECPROD.rst``
  description (PR `#200`_).
* Add description of GFA summary files (PR `#202`_).
* Add data model for full DR1 LSS catalogs (PR `#205`_).
* Update data model based on final DR1 files (PR `#207`_).

.. _`#199`: https://github.com/desihub/desidatamodel/pull/199
.. _`#200`: https://github.com/desihub/desidatamodel/pull/200
.. _`#202`: https://github.com/desihub/desidatamodel/pull/202
.. _`#205`: https://github.com/desihub/desidatamodel/pull/205
.. _`#207`: https://github.com/desihub/desidatamodel/pull/207

24.9 (2024-09-12)
-----------------

* Fix column name in ``fluxcalib`` description (PR `#193`_).
* Add 5 coadd-related columns to the fibermap of the Redrock files (PR `#192`_).
* Add ``DESINAME`` description (PR `#189`_).
* Update definition of ``ZCAT_NSPEC`` (PR `#187`_).
* Add note about equivalent width values in ``fuji`` and ``guadalupe`` (PR `#181`_).
* Add note about units in FITS files (PR `#178`_).
* Update ``column_descriptions.csv`` for short Description (for FITS headers)
  and FullDescription (longer, for data model) (PR `#196`_).

.. _`#178`: https://github.com/desihub/desidatamodel/pull/178
.. _`#181`: https://github.com/desihub/desidatamodel/pull/181
.. _`#187`: https://github.com/desihub/desidatamodel/pull/187
.. _`#189`: https://github.com/desihub/desidatamodel/pull/189
.. _`#192`: https://github.com/desihub/desidatamodel/pull/192
.. _`#193`: https://github.com/desihub/desidatamodel/pull/193
.. _`#196`: https://github.com/desihub/desidatamodel/pull/196

23.1 (2023-06-12)
-----------------

* Warnings about ``TARGET_RA``, etc. (PR `#177`_).
* Automate generation of ``bitmasks.rst`` (PR `#176`_).
* Reorganize front pages for DESI non-experts (PR `#172`_).
* Clean up ``DESI_SPECTRO_REDUX`` and ``DESI_TARGET`` after verification of EDR (PR `#171`_).
* Add Lyman-alpha VAC data model (PR `#169`_).
* Final clean up for DESI EDR (PR `#167`_).
* Add LSS catalog to data model (PR `#166`_).
* Updates to redshift catalog files and other spectroscopic reduction files
  (PRs `#164`_, `#162`_, `#161`_).
* Clarify definition of RA, Dec (PR `#160`_).
* Add ``$DESI_ROOT/vac`` directory (PR `#157`_).
* Updates to raw data files; validation now selects multiple candidate
  files for testing (PR `#151`_).
* Update description of guide files in raw data (PR `#154`_).
* Update description of sky files in raw data (PR `#153`_).
* Update column descriptions for galaxy clustering files meeting EDR datamodel (PR `#152`_).
* Update column descriptions for tile-based spectra/redshift/afterburner files
  (PR `#145`_).
* Update column descriptions from a master list of columns (PR `#144`_).
* Update spectra and coadd text with additional examples (PR `#143`_).
* Rename ``SURVEYOPS`` (PR `#142`_).
* Add links to maskbit definitions (PR `#139`_).
* Update :doc:`the contributing page <datamodel>` (PR `#138`_).
* Update documentation for QSO afterburner files (PR `#134`_).
* Resolve maggy/maggies discrepancies in ``DESI_TARGET`` / ``DESI_SURVEY`` (PR `#133`_).
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
.. _`#151`: https://github.com/desihub/desidatamodel/pull/151
.. _`#152`: https://github.com/desihub/desidatamodel/pull/152
.. _`#153`: https://github.com/desihub/desidatamodel/pull/153
.. _`#154`: https://github.com/desihub/desidatamodel/pull/154
.. _`#157`: https://github.com/desihub/desidatamodel/pull/157
.. _`#160`: https://github.com/desihub/desidatamodel/pull/160
.. _`#161`: https://github.com/desihub/desidatamodel/pull/161
.. _`#162`: https://github.com/desihub/desidatamodel/pull/162
.. _`#164`: https://github.com/desihub/desidatamodel/pull/164
.. _`#166`: https://github.com/desihub/desidatamodel/pull/166
.. _`#167`: https://github.com/desihub/desidatamodel/pull/167
.. _`#169`: https://github.com/desihub/desidatamodel/pull/169
.. _`#171`: https://github.com/desihub/desidatamodel/pull/171
.. _`#172`: https://github.com/desihub/desidatamodel/pull/172
.. _`#176`: https://github.com/desihub/desidatamodel/pull/176
.. _`#177`: https://github.com/desihub/desidatamodel/pull/177

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
