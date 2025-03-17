=======================================
qso_qn-SPECTROGRAPH-TILEID-GROUPID.fits
=======================================

:Summary: This file contains the output of QuasarNet (QSO classification algorithm and redshift fitter).
    When there is a disagreement between the redshift from QN and Redrock, a new redshift is fitted
    using only QSO templates and redshift from QN as prior.
:Naming Convention: ``qso_qn-SPECTROGRAPH-TILEID-GROUPID.fits``, where
    ``SPECTROGRAPH`` is the spectrograph ID, ``TILEID`` is the tile number and
    ``GROUPID`` depends on the ``GROUPTYPE`` of the tile coadd.
:Regex: ``qso_qn-[0-9]-[0-9]+-([14]xsubset[1-6]|lowspeedsubset[1-6]|exp[0-9]{8}|thru[0-9]{8}|[0-9]{8})\.fits``
:File Type: FITS, 33 KB

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    Empty.
HDU1_  QN_RR   BINTABLE Output of QuasarNet afterburner.
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = QN_RR

Contains the result of QuasarNet afterburner and the new redshift fit from run of Redrock with QSO templates and redshift prior from QuasarNet.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =======================
    KEY    Example Value Type Comment
    ====== ============= ==== =======================
    NAXIS1 151           int  width of table in bytes
    NAXIS2 155           int  number of rows in table
    ====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

==================== =========== ===== ========================================================================================
Name                 Type        Units Description
==================== =========== ===== ========================================================================================
TARGETID             int64             Unique DESI target ID
RA                   float64     deg   Target Right Ascension
DEC                  float64     deg   Target declination
Z_NEW                float64           New redshift computed with redrock with QN prior and only qso templates
ZERR_NEW             float32           Redshift error from the new run of redrock
SV1_DESI_TARGET [1]_ int64             DESI (dark time program) target selection bitmask for SV1
SV2_DESI_TARGET [1]_ int64             DESI (dark time program) target selection bitmask for SV2
SV3_DESI_TARGET [1]_ int64             DESI (dark time program) target selection bitmask for SV3
DESI_TARGET [1]_     int64             DESI (dark time program) target selection bitmask
COEFFS               float32[10]       Coefficient of the fit for the new run of redrock
SPECTYPE             char[10]          Spectral type of Redrock best fit template (e.g. GALAXY, QSO, STAR)
Z_RR                 float32           Redshift collected from redrock file
Z_QN                 float32           Redshift measured by QuasarNET using line with highest confidence
IS_QSO_QN_NEW_RR     logical           QN identified as QSO at different redshift or classification than Redrock
C_LYA                float32           Confidence for LyA line, i.e. ~probability to be a QSO
C_CIV                float32           Confidence for CIV line
C_CIII               float32           Confidence for CIII line
C_MgII               float32           Confidence for MgII line
C_Hbeta              float32           Confidence for Hbeta line
C_Halpha             float32           Confidence for Halpha line
Z_LYA                float32           Redshift estimated by QuasarNET with LyA line
Z_CIV                float32           Redshift estimated by QuasarNET with CIV line
Z_CIII               float32           Redshift estimated by QuasarNET with CIII line
Z_MgII               float32           Redshift estimated by QuasarNET with MgII line
Z_Hbeta              float32           Redshift estimated by QuasarNET with Hbeta line
Z_Halpha             float32           Redshift estimated by QuasarNET with Halpha line
==================== =========== ===== ========================================================================================

.. [1] Optional

Notes:

``IS_QSO_QN_NEW_RR`` is set if QuasarNET selects this as a QSO *and* the answer
is different from Redrock, either because Redrock didn't identify it as a QSO
or because the Redrock redshift differed by more than 0.05.  If both
QuasarNET and Redrock agree that it is a QSO and agree on the redshift, then
``IS_QSO_QN_NEW_RR=False``.

The QuasarNET QSO selection is performed with the C_XXX confidence parameters.
``IS_QSO_QN_NEW_RR`` uses a relatively loose cut of ``max(C_XXX) >= 0.5``;
downstream code may choose to use a tighter cut.


Notes and Examples
==================

These files are generated with https://github.com/desihub/desispec/blob/main/bin/desi_qso_qn_afterburner
