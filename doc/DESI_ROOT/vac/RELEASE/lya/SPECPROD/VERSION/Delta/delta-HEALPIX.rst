=============
delta-HEALPIX
=============

:Summary: This file contains the main output from the picca delta extraction:
    the lyman alpha transmission fluctuations for all analysed quasars in a given healpix
:Naming Convention: ``delta-HEALPIX.fits``, where
    ``HEALPIX`` is the healpix id.
:Regex: ``delta-[0-9]+\.fits\.gz``
:File Type: FITS

Contents
========

====== =========== ======== ========================
Number EXTNAME     Type     Contents
====== =========== ======== ========================
HDU0_  PRIMARY     PRIMARY  Empty
HDU1_  LAMBDA      IMAGE    Wavelength grid
HDU2_  METADATA    BINTABLE Per forest metadata
HDU3_  DELTA       IMAGE    Flux transmission field
HDU4_  WEIGHT      IMAGE    Weights
HDU5_  CONT        IMAGE    Quasar continua
====== =========== ======== ========================


FITS Header Units
=================

HDU0
----

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = LAMBDA

Wavelength grid

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ============= ================ ===== ===========================
    KEY           Example Value    Type  Comment
    ============= ================ ===== ===========================
    NAXIS1        2716             int   number of wavelength pixels
    WAVE_SOLUTION lin              str   chosen wavelength solution
    DELTA_LAMBDA  0.8              float pixel step
    BUNIT         Angstrom         str   wavelength units
    CHECKSUM      UZ3aaZ2aVZ2aaZ2a str   HDU checksum
    DATASUM       1634060384       str   HDU data checksum
    ============= ================ ===== ===========================

Data: FITS image [float64, 2716]

HDU2
----

EXTNAME = METADATA

Per-forest metadata

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ============= ================ ======== ===========================
    KEY           Example Value    Type     Comment
    ============= ================ ======== ===========================
    NAXIS1        84               int      table width
    NAXIS2        340              int      number of forests
    BLINDING      none             str      blinding scheme used
    CHECKSUM      UZ3aaZ2aVZ2aaZ2a str      HDU checksum
    DATASUM       1634060384       str      HDU data checksum
    ============= ================ ======== ===========================


Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

==================== ======== ===== ===================
Name                 Type     Units Description
==================== ======== ===== ===================
LOS_ID               int64          PICCA unique target ID
RA                   float64  rad   Target Right Ascension [radians]
DEC                  float64  rad   Target declination [radians]
Z                    float64        Redshift
MEANSNR              float64        mean signal-to-noise ratio
TARGETID             int64          Unique target ID
NIGHT                char[12]       Observation night(s)
PETAL                char[12]       Observation petal(s)
TILE                 char[12]       Observation tile(s)
==================== ======== ===== ===================

HDU3
----

EXTNAME = DELTA

Flux transmission field in wavelength bins

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ============= ================ ===== ===========================
    KEY           Example Value    Type  Comment
    ============= ================ ===== ===========================
    NAXIS1        2716             int   number of wavelength pixels
    NAXIS2        340              int   number of forests
    BUNIT                          str   delta units (unitless)
    CHECKSUM      UZ3aaZ2aVZ2aaZ2a str   HDU checksum
    DATASUM       1634060384       str   HDU data checksum
    ============= ================ ===== ===========================

Data: FITS image [float64, 2716x340]

HDU4
----

EXTNAME = WEIGHT

Weights in wavelength bins

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ============= ================ ===== ===========================
    KEY           Example Value    Type  Comment
    ============= ================ ===== ===========================
    NAXIS1        2716             int   number of wavelength pixels
    NAXIS2        340              int   number of forests
    BUNIT                          str   weight units (unitless)
    CHECKSUM      UZ3aaZ2aVZ2aaZ2a str   HDU checksum
    DATASUM       1634060384       str   HDU data checksum
    ============= ================ ===== ===========================

Data: FITS image [float64, 2716x340]

HDU5
----

EXTNAME = CONT

Quasar continuum in wavelength bins

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ============= ============================== ===== ===========================
    KEY           Example Value                  Type  Comment
    ============= ============================== ===== ===========================
    NAXIS1        2716                           int   number of wavelength pixels
    NAXIS2        340                            int   number of forests
    BUNIT         10**-17 erg/(s cm2 Angstrom)   str   quasar continuum units
    CHECKSUM      UZ3aaZ2aVZ2aaZ2a               str   HDU checksum
    DATASUM       1634060384                     str   HDU data checksum
    ============= ============================== ===== ===========================

Data: FITS image [float64, 2716x340]

Notes and Examples
==================

These files are generated with https://github.com/igmhub/picca/blob/master/bin/picca_delta_extraction.py
The code was run twice:

.. code-block:: bash

    picca_delta_extraction.py config/delta_extraction_ciii_step_1.ini
    picca_delta_extraction.py config/delta_extraction_lya.ini
