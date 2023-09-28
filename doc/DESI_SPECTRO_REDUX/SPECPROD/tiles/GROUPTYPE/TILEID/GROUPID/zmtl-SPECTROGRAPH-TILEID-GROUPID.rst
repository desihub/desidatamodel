=========================================
zmtl-SPECTROGRAPH-TILEID-thruGROUPID.fits
=========================================

:Summary: The ``zmtl`` files contain information about redshifts used by the
	  :doc:`MTL ("Merged Target List") process </DESI_SURVEYOPS/mtl/index>` to update
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
HDU0_          IMAGE    Empty
HDU1_  ZMTL    BINTABLE Redshifts to inform MTL updates
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

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

==================== ======= ===== ====================================================================
Name                 Type    Units Description
==================== ======= ===== ====================================================================
RA                   float64 deg   Target Right Ascension
DEC                  float64 deg   Target declination
TARGETID             int64         Unique DESI target ID
SV1_DESI_TARGET [1]_ int64         DESI (dark time program) target selection bitmask for SV1
SV1_BGS_TARGET [1]_  int64         BGS (bright time program) target selection bitmask for SV1
SV1_MWS_TARGET [1]_  int64         MWS (bright time program) target selection bitmask for SV1
SV1_SCND_TARGET [1]_ int64         Secondary target selection bitmask for SV1
SV3_DESI_TARGET [1]_ int64         DESI (dark time program) target selection bitmask for SV3
SV3_BGS_TARGET [1]_  int64         BGS (bright time program) target selection bitmask for SV3
SV3_MWS_TARGET [1]_  int64         MWS (bright time program) target selection bitmask for SV3
SV3_SCND_TARGET [1]_ int64         Secondary target selection bitmask for SV3
DESI_TARGET [1]_     int64         DESI (dark time program) target selection bitmask
BGS_TARGET [1]_      int64         BGS (Bright Galaxy Survey) target selection bitmask
MWS_TARGET [1]_      int64         Milky Way Survey targeting bits
SCND_TARGET  [1]_    int64         Target selection bitmask for secondary programs
Z                    float64       Redshift measured by Redrock
ZWARN                int64         Redshift warning bitmask from Redrock, plus DESI-specific bits set
SPECTYPE             char[6]       Spectral type of Redrock best fit template (e.g. GALAXY, QSO, STAR)
DELTACHI2            float64       chi2 difference between first- and second-best redrock template fits
NUMOBS               int32         Number of spectroscopic observations (on this specific, single tile)
ZTILEID              int32         ID of tile that most recently updated target's state
Z_QN                 float64       Redshift measured by QuasarNET
Z_QN_CONF            float64       Redshift confidence from QuasarNET
IS_QSO_QN            int16         Spectroscopic classification from QuasarNET (1 for a quasar)
==================== ======= ===== ====================================================================

.. [1] Only `either` the four ``SV1``, ``SV3`` `or` Main Survey columns will be present. ``TARGET``
       bitmask columns are preceded by the survey ``PHASE`` except in the case of Main Survey files
       (i.e. ``DESI_TARGET`` is called ``SV1_DESI_TARGET`` when the survey ``PHASE`` is ``sv1``).


Notes and Examples
==================

See the DESI Survey Operations paper (Schlafly et al., in preparation) for
details of how the quantities in the ``zmtl`` files are used to update the
observational state of a target in the MTL ledgers.

For more information, see `QuasarNET`_ for QuasarNET and
`SQUEzE`_ for SQUEzE.

.. _`QuasarNET`: https://ui.adsabs.harvard.edu/abs/2018arXiv180809955B/abstract
.. _`SQUEzE`: https://ui.adsabs.harvard.edu/abs/2020MNRAS.496.4931P/abstract
