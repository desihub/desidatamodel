===================================
qso_mgii-SURVEY-PROGRAM-PIXNUM.fits
===================================

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``qso_mgii-SURVEY-PROGRAM-PIXNUM.fits``, where ``SURVEY`` is
    *e.g.* ``main`` or ``sv1``, ``PROGRAM`` is *e.g.* ``bright or ``dark``
    and ``PIXNUM`` is the HEALPixel number.
:Regex: ``qso_mgii-(cmx|main|special|sv1|sv2|sv3)-(backup|bright|dark|other)-[0-9]+\.fits``
:File Type: FITS, 22 KB

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    Empty.
HDU1_  MGII    BINTABLE *Brief Description*
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

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =======================
    KEY    Example Value Type Comment
    ====== ============= ==== =======================
    NAXIS1 83            int  width of table in bytes
    NAXIS2 154           int  number of rows in table
    ====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

==================== ======== ===== ===================
Name                 Type     Units Description
==================== ======== ===== ===================
TARGETID             int64          Unique target ID
RA                   float64        Target Right Ascension [degrees]
DEC                  float64        Target declination [degrees]
Z_RR                 float64        Redshift collected from redrock file
ZERR                 float32        Redshift error from redrock file
IS_QSO_MGII          logical        Is the object pass the MgII selection ?
SV1_DESI_TARGET [1]_ int64          Dark survey + calibration targeting bits for SV1
DESI_TARGET          int64          Dark survey + calibration targeting bits
SPECTYPE             char[10]       Spectype from redrock file
DELTA_CHI2           float32        Difference of chi2 between redrock fit and MgII fitter over the lambda interval considered during the fit [2]_
A                    float32        fitted parameter by MgII fitter [2]_ [3]_
SIGMA                float32        fitted parameter by MgII fitter [2]_ [3]_
B                    float32        fitted parameter by MgII fitter [3]_
VAR_A                float32        error on A [2]_
VAR_SIGMA            float32        error on SIGMA
VAR_B                float32        error on B
==================== ======== ===== ===================

.. [1] Optional

.. [2] MgII selection is performed with these parameters.
       See: https://github.com/desihub/desispec/blob/720153babcf85dd93530252b0c1f631d48edfc0d/py/desispec/mgii_afterburner.py#L5

.. [3] MgII fitter use the following form: ``fit_function = lambda x, A, sigma, B : A * np.exp(-1.0 * (x)**2 / (2 * sigma**2)) + B``
       See: https://github.com/desihub/desispec/blob/720153babcf85dd93530252b0c1f631d48edfc0d/py/desispec/mgii_afterburner.py#L283


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
