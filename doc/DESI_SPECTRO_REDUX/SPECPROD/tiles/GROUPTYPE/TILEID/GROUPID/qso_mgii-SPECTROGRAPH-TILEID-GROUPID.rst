=========================================
qso_mgii-SPECTROGRAPH-TILEID-GROUPID.fits
=========================================

:Summary: This file contains the output of the MgII fitter which is a classifier algorithm
    to collect spectra with MgII broad emission line.
:Naming Convention: ``qso_mgii-SPECTROGRAPH-TILEID-GROUPID.fits``, where
    ``SPECTROGRAPH`` is the spectrograph ID, ``TILEID`` is the tile number and
    ``GROUPID`` depends on the ``GROUPTYPE`` of the tile coadd.
:Regex: ``qso_mgii-[0-9]-[0-9]+-([14]xsubset[1-6]|lowspeedsubset[1-6]|exp[0-9]{8}|thru[0-9]{8}|[0-9]{8})\.fits``
:File Type: FITS, 19 KB

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    Empty.
HDU1_  MGII    BINTABLE Output of MgII fitter.
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = MGII

Output of MgII fitter.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =======================
    KEY    Example Value Type Comment
    ====== ============= ==== =======================
    NAXIS1 83            int  width of table in bytes
    NAXIS2 131           int  number of rows in table
    ====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

==================== ======== ===== ==============================================================================================================
Name                 Type     Units Description
==================== ======== ===== ==============================================================================================================
TARGETID             int64          Unique DESI target ID
RA                   float64  deg   Target Right Ascension
DEC                  float64  deg   Target declination
Z_RR                 float64        Redshift collected from redrock file
ZERR                 float32        Redshift error from redrock
IS_QSO_MGII          logical        Boolean: True if the object passes the MgII selection
SV1_DESI_TARGET [1]_ int64          DESI (dark time program) target selection bitmask for SV1
DESI_TARGET [1]_     int64          DESI (dark time program) target selection bitmask
SPECTYPE             char[10]       Spectral type of Redrock best fit template (e.g. GALAXY, QSO, STAR)
DELTA_CHI2           float32        Difference of chi2 between redrock fit and MgII fitter over the lambda interval considered during the fit [2]_
A                    float32        fitted parameter by MgII fitter [2]_ [3]_
SIGMA                float32        fitted parameter by MgII fitter [2]_ [3]_
B                    float32        fitted parameter by MgII fitter [3]_
VAR_A                float32        error on A [2]_
VAR_SIGMA            float32        error on SIGMA
VAR_B                float32        error on B
==================== ======== ===== ==============================================================================================================

.. [1] Optional

.. [2] MgII selection is performed with these parameters.
       See: https://github.com/desihub/desispec/blob/720153babcf85dd93530252b0c1f631d48edfc0d/py/desispec/mgii_afterburner.py#L5

.. [3] MgII fitter use the following form: ``fit_function = lambda x, A, sigma, B : A * np.exp(-1.0 * (x)**2 / (2 * sigma**2)) + B``
       See: https://github.com/desihub/desispec/blob/720153babcf85dd93530252b0c1f631d48edfc0d/py/desispec/mgii_afterburner.py#L283

Notes and Examples
==================

These files are generated with https://github.com/desihub/desispec/blob/master/bin/desi_qso_mgii_afterburner

As mentionned on the top of the previous file, the MgII fitter is available here: https://github.com/desihub/desispec/blob/master/py/desispec/mgii_afterburner.py
