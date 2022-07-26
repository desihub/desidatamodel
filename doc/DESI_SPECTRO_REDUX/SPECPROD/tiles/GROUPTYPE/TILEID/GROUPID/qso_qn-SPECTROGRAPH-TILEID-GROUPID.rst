=======================================
qso_qn-SPECTROGRAPH-TILEID-GROUPID.fits
=======================================

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
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
HDU1_  QN_RR   BINTABLE *Brief Description*
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

*Summarize the contents of this HDU.*

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

==================== =========== ===== ===================
Name                 Type        Units Description
==================== =========== ===== ===================
TARGETID             int64             Unique target ID
RA                   float64           Target Right Ascension [degrees]
DEC                  float64           Target declination [degrees]
Z_NEW                float64           New redshift computed with redrock with QN prior and only qso templates
ZERR_NEW             float32           Redshift error from the new run of redrock
SV1_DESI_TARGET [1]_ int64             Dark survey + calibration targeting bits for SV1
DESI_TARGET [1]_     int64             Dark survey + calibration targeting bits
COEFFS               float32[10]       Coefficient of the fit for the new run of redrock
SPECTYPE             char[10]          Spectype from the redrock file
Z_RR                 float32           Redshift collected from redrock file
Z_QN                 float32           Redshift computed with quasarnp [2]_
IS_QSO_QN_NEW_RR     logical           Is the object detected QSO with quasarnp and a new redshift fit with prior is performed?
C_LYA                float32           Confidence line for LYA (*i.e.*) ~ probability to be a QSO [3]_
C_CIV                float32           Confidence line for CIV [3]_
C_CIII               float32           Confidence line for CIII [3]_
C_MgII               float32           Confidence line for MgII [3]_
C_Hbeta              float32           Confidence line for Hbeta [3]_
C_Halpha             float32           Confidence line for Halpha [3]_
Z_LYA                float32           Redshift estimated by quasarnp with LYA line [2]_
Z_CIV                float32           Redshift estimated by quasarnp with CIV line [2]_
Z_CIII               float32           Redshift estimated by quasarnp with CIII line [2]_
Z_MgII               float32           Redshift estimated by quasarnp with MgII line [2]_
Z_Hbeta              float32           Redshift estimated by quasarnp with Hbeta line [2]_
Z_Halpha             float32           Redshift estimated by quasarnp with Halpha line [2]_
==================== =========== ===== ===================

.. [1] Optional

.. [2] Z_QN is the redshift estimated on the line of the highest confidence

.. [3] The QN selection is performed with these parameters. As it stands, in QN afterburner everything with np.max(confindence) > 0.5 is considered as a quasar. However, specific cut will be used depends on each target class; QSO_target will use np.max(confidence) > 0.95.
       See: https://github.com/echaussidon/desispec/blob/720153babcf85dd93530252b0c1f631d48edfc0d/bin/desi_qso_qn_afterburner#L236

Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
