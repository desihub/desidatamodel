==
v2
==

Overview of v2 Redshift Catalog Files
-------------------------------------

The v2 redshift catalogs are available starting from Data Release 2 (DR2).
They significantly reorganize the column layout compared to
:doc:`v1 <../v1/index>` by splitting each catalog into three separate FITS files
by column type, plus a per-exposure fibermap file. This reduces per-file sizes at
the scale of the growing DESI data volumes.

For each SURVEY and PROGRAM, four files are produced for each of "ztile" and "zpix" prefixes:

- ``SURVEY/(ztile|zpix)-SURVEY-PROGRAM.fits`` --- core redshift and targeting columns
- ``SURVEY/(ztile|zpix)-SURVEY-PROGRAM-imaging.fits`` --- Legacy Survey imaging photometry columns
- ``SURVEY/(ztile|zpix)-SURVEY-PROGRAM-extra.fits`` --- all remaining columns (full Redrock output,
  TSNR2, emission line fits, QuasarNET, quality flags)
- ``SURVEY/exp_fibermap/(ztile|zpix)-SURVEY-PROGRAM-expfibermap.fits`` --- per-exposure fibermap

The :doc:`ztile <SURVEY/ztile-SURVEY-PROGRAM-GROUPTYPE>` catalogs contain redshifts fit to
coadded exposures of each tile but not across tiles. The
:doc:`zpix <SURVEY/zpix-SURVEY-PROGRAM>` catalogs coadd data across tiles (by healpixel or uniqpix)
before redshift fitting.

Additionally, the "zall" files contain catalogs combined across all surveys and programs:

- :doc:`zall/zall-pix*.fits <zall/zall-pix-SPECPROD>` --- combined zpix catalogs
- :doc:`zall/zall-tilecumulative <zall/zall-tilecumulative-SPECPROD>` --- combined zall catalogs

Most users will be interested in the
:doc:`zall/zall-pix*.fits <zall/zall-pix-SPECPROD>` catalogs (across all survey/programs)
or the
:doc:`SURVEY/zpix-SURVEY-PROGRAM.fits <zall/zall-pix-SPECPROD>` catalogs
(specific to individual survey/programs)

New Columns in v2
-----------------

v2 also introduces new redshift quality columns not present in v1:

- ``Z_BEST``: best redshift, choosing between the standard Redrock ``Z`` and the QuasarNET ``Z_QSO`` for QSO targets. It is the recommended redshift value for most users. The associated Redrock columns are ``ZERR_BEST``, ``ZWARN_BEST`` etc. 
- ``Z_CONF``: integer confidence level: 0=no confidence, 1=low confidence (``ZWARN_BEST==0`` but not LSS-quality), 3=high confidence (passes LSS quality cuts). A non-zero ``Z_CONF`` also requires ``GOOD_SPEC==True``.
- ``GOOD_SPEC``: True if the spectrum is a science target with good hardware status.
- ``GOOD_Z_{BGS,LRG,ELG,QSO}``: per-tracer redshift quality flags passing LSS cuts.

Subdirectories
--------------

Files are stored under ``zcatalog/v2/{SURVEY}/`` for per-survey catalogs and
``zcatalog/v2/zall/`` for the all-survey combined catalogs.

.. toctree::
   :maxdepth: 1

   SURVEY/index
   zall/index
