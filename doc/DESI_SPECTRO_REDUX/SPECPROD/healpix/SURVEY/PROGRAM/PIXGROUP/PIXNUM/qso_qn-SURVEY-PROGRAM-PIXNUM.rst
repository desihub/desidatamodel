=================================
qso_qn-SURVEY-PROGRAM-PIXNUM.fits
=================================

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``qso_qn-SURVEY-PROGRAM-PIXNUM.fits``, where ``SURVEY`` is
    *e.g.* ``main`` or ``sv1``, ``PROGRAM`` is *e.g.* ``bright or ``dark``
    and ``PIXNUM`` is the HEALPixel number.
:Regex: ``qso_qn-(cmx|main|special|sv1|sv2|sv3)-(backup|bright|dark|other)-[0-9]+\.fits``
:File Type: FITS, 19 KB  *This section gives the type of the file
    and its approximate size.*

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    *Brief Description*
HDU1_  QN_RR   BINTABLE *Brief Description*
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

*Summarize the contents of this HDU.*

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = QN_RR

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =======================
    KEY    Example Value Type Comment
    ====== ============= ==== =======================
    NAXIS1 151           int  width of table in bytes
    NAXIS2 75            int  number of rows in table
    ====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

==================== =========== ===== ===================
Name                 Type        Units Description
==================== =========== ===== ===================
TARGETID             int64             Unique target ID
RA                   float64           Target Right Ascension [degrees]
DEC                  float64           Target declination [degrees]
Z_NEW                float64           New redshift computed with redrock with QN prior and only qso templates
ZERR_NEW             float32           Redshift error from the new run of redrock
SV1_DESI_TARGET      int64             Dark survey + calibration targeting bits for SV1
DESI_TARGET          int64             Dark survey + calibration targeting bits
COEFFS               float32[10]       Coefficient of the fit for the new run of redrock
SPECTYPE             char[10]          Spectype from the redrock file
Z_RR                 float32           Redshift collected from redrock file
Z_QN [1]_            float32           Redshift computed with quasarnp
IS_QSO_QN_NEW_RR     logical           Is the object detected QSO with quasarnp and a new redshift fit with prior is performed ?
C_LYA [2]_           float32           Confidence line for LYA (ie) ~ probability to be a QSO
C_CIV [2]_           float32           Confidence line for CIV
C_CIII [2]_          float32           Confidence line for CIII
C_MgII [2]_          float32           Confidence line for MgII
C_Hbeta [2]_         float32           Confidence line for Hbeta
C_Halpha [2]_        float32           Confidence line for Halpha
Z_LYA [1]_           float32           Redshift estimated by quasarnp with LYA line
Z_CIV [1]_           float32           Redshift estimated by quasarnp with CIV line
Z_CIII [1]_          float32           Redshift estimated by quasarnp with CIII line
Z_MgII [1]_          float32           Redshift estimated by quasarnp with MgII line
Z_Hbeta [1]_         float32           Redshift estimated by quasarnp with Hbeta line
Z_Halpha [1]_        float32           Redshift estimated by quasarnp with Halpha line
==================== =========== ===== ===================

.. [1] Z_QN is the redshift estimated on the line of the highest confidence

.. [2] The QN selection is performed with these parameters. As it stands, in QN afterburner everything with np.max(confindence) > 0.5 is considered as a quasar. However, specific cut will be used depends on each target class; QSO_target will use np.max(confidence) > 0.95.
       See: https://github.com/echaussidon/desispec/blob/720153babcf85dd93530252b0c1f631d48edfc0d/bin/desi_qso_qn_afterburner#L236


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
