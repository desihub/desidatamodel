=========================================
zmtl-SPECTROGRAPH-TILEID-thruGROUPID.fits
=========================================

:Summary: The ``zmtl`` files contain information about redshifts used by the
	  :doc:`MTL ("Merged Target List") process </SURVEYOPS/mtl/index>` to update
	  the observational state of targets in the MTL ledgers. In particular,
	  the redshift information is crucial for deciding whether a target
	  is a Lyman-alpha quasar that requires additional DESI observations.
:Naming Convention: ``zmtl-SPECTROGRAPH-TILEID-thruGROUPID.fits``, where
    ``SPECTROGRAPH`` is the spectrograph ID, ``TILEID`` is the tile number and
    ``GROUPID`` depends on the ``GROUPTYPE`` of the tile coadd.
:Regex: ``zmtl-[0-9]-[0-9]+-(thru|)[0-9]{8}\.fits``
:File Type: FITS, 67 KB

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_  PRIMARY IMAGE    Empty
HDU1_  ZMTL    BINTABLE Redshifts to inform MTL updates
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = ZMTL

Redshifts to inform MTL updates

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ========================================================================================== ==== =======================
    KEY      Example Value                                                                              Type Comment
    ======== ========================================================================================== ==== =======================
    NAXIS1   112                                                                                        int  width of table in bytes
    NAXIS2   500                                                                                        int  number of rows in table
    QN_ADDED T                                                                                          bool ``True`` if `QuasarNET`_ information included
    SQ_ADDED F                                                                                          bool ``True`` if `SQUEzE`_ information included
    AB_ADDED F                                                                                          bool ``True`` if absorption line information included
    ZC_ADDED F                                                                                          bool ``True`` if combined redshift information included
    QNMODFIL /global/cfs/cdirs/desi/target/catalogs/lya/qn_models/qn_train_coadd_indtrain_0_0_boss10.h5 str  Filename of `QuasarNET`_ model
    BADPTLQA F                                                                                          bool ``True`` if all fibers on a petal were masked
    ======== ========================================================================================== ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

==================== ======= ===== ===================
Name                 Type    Units Description
==================== ======= ===== ===================
RA                   float64 deg   Right ascension
DEC                  float64 deg   Declination
TARGETID             int64         Unique targeting ID
SV1_DESI_TARGET [1]_ int64         DESI (dark time program) target selection bitmask (sv1 phase of DESI Survey Validation)
SV1_BGS_TARGET [1]_  int64         BGS (bright time program) target selection bitmask (sv1 phase of DESI Survey Validation)
SV1_MWS_TARGET [1]_  int64         MWS (bright time program) target selection bitmask (sv1 phase of DESI Survey Validation)
SV1_SCND_TARGET [1]_ int64         SCND (secondary program) target selection bitmask (sv1 phase of DESI Survey Validation)
SV3_DESI_TARGET [1]_ int64         DESI (dark time program) target selection bitmask (sv3 phase of DESI Survey Validation)
SV3_BGS_TARGET [1]_  int64         BGS (bright time program) target selection bitmask (sv3 phase of DESI Survey Validation)
SV3_MWS_TARGET [1]_  int64         MWS (bright time program) target selection bitmask (sv3 phase of DESI Survey Validation)
SV3_SCND_TARGET [1]_ int64         SCND (secondary program) target selection bitmask (sv3 phase of DESI Survey Validation)
DESI_TARGET [1]_     int64         DESI (dark time program) target selection bitmask
BGS_TARGET [1]_      int64         BGS (bright time program) target selection bitmask
MWS_TARGET [1]_      int64         MWS (bright time program) target selection bitmask
SCND_TARGET  [1]_    int64         SCND (secondary program) target selection bitmask
Z                    float64       Redshift from ``Redrock``
ZWARN                int64         Redshift warning bimask
SPECTYPE             char[6]       Spectroscopic classification from ``Redrock``
DELTACHI2            float64       Chi-squared difference between the first- and second-best redshifts from ``Redrock``
NUMOBS               int32         Number of spectroscopic observations (on this specific, single tile)
ZTILEID              int32         Unique tile ID (identical to ``TILEID``)
Z_QN                 float64       Redshift from `QuasarNET`_
Z_QN_CONF            float64       Redshift confidence from `QuasarNET`_
IS_QSO_QN            int16         Spectroscopic classification	from `QuasarNET`_ (1 for a quasar)
==================== ======= ===== ===================

.. [1] Only `either` the four ``SV1``, ``SV3`` `or` Main Survey columns will be present. ``TARGET``
       bitmask columns are preceded by the survey ``PHASE`` except in the case of Main Survey files
       (i.e. ``DESI_TARGET`` is called ``SV1_DESI_TARGET`` when the survey ``PHASE`` is ``sv1``).


Notes and Examples
==================

See the DESI Survey Operations paper (Schlafly et al., in preparation) for
details of how the quantities in the ``zmtl`` files are used to update the
observational state of a target in the MTL ledgers.


.. _`QuasarNET`: https://ui.adsabs.harvard.edu/abs/2018arXiv180809955B/abstract
.. _`SQUEzE`: https://ui.adsabs.harvard.edu/abs/2020MNRAS.496.4931P/abstract
