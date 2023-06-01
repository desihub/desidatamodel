================
delta_attributes
================

:Summary: This file contains auxiliar output from the picca delta extraction:
    summary statistics of the computed deltas.
:Naming Convention: ``delta_attributes.fits.gz`` or
    ``delta_attributes_iterationITERATION.fits.gz``,
    where ``ITERATION`` is the iteration step.
:Regex: ``delta_attributes(_iteration[0-9]+)?\.fits\.gz``
:File Type: FITS

Contents
========

====== ============ ======== ========================
Number EXTNAME      Type     Contents
====== ============ ======== ========================
HDU0_  PRIMARY      PRIMARY  Empty
HDU1_  STACK_DELTAS BINTABLE Delta mean properties
HDU2_  VAR_FUNC     BINTABLE Variance fitted functions
HDU3_  CONT         BINTABLE Mean quasar continuum
HDU4_  FIT_METADATA BINTABLE Extra fit metadata
====== ============ ======== ========================


FITS Header Units
=================

HDU0
----

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = STACK_DELTAS

Delta mean properties

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ============= ============= ===== ===========================
    KEY           Example Value Type  Comment
    ============= ============= ===== ===========================
    NAXIS         2             int   number of array dimensions
    NAXIS1        24            int   table width
    NAXIS2        2716          int   number of wavelenght pixels
    ============= ============= ===== ===========================


Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

==================== ======== ============= ===================
Name                 Type     Units         Description
==================== ======== ============= ===================
LOGLAM               float64  log(Angstrom) log(wavelength)
STACK                float64                mean(1+delta)
WEIGHT               float64                Mean weight
==================== ======== ============= ===================

HDU2
----

EXTNAME = VAR_FUNC

Variance fitted functions

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ============= ============= ===== ===========================
    KEY           Example Value Type  Comment
    ============= ============= ===== ===========================
    NAXIS         2             int   number of array dimensions
    NAXIS1        48            int   table width
    NAXIS2        20            int   number of wavelenght pixels
    ============= ============= ===== ===========================


Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

==================== ======== ============= ===================
Name                 Type     Units         Description
==================== ======== ============= ===================
LOGLAM               float64  log(Angstrom) log(wavelength)
ETA                  float64                Intrinsic variace of fluctuations
VAR_LSS              float64                Mean weight
NUM_PIXELS           int32                  Number of pixels in the fit
VALID_FIT            bool                   Indicates valid fit
==================== ======== ============= ===================

HDU3
----

EXTNAME = CONT

Mean quasar continuum

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ============= ============= ===== ===========================
    KEY           Example Value Type  Comment
    ============= ============= ===== ===========================
    NAXIS         2             int   number of array dimensions
    NAXIS1        84            int   table width
    NAXIS2        206           int   number of rest-frame pixels
    ============= ============= ===== ===========================


Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

==================== ======== ============= ===================
Name                 Type     Units         Description
==================== ======== ============= ===================
LOGLAM_REST          float64  log(Angstrom) Logarithm of the rest-frame wavelength
MEAN_CONT            float64                Mean quasar continuum
WEIGHT               float64                Mean quasar continuum
==================== ======== ============= ===================

HDU4
----

EXTNAME = FIT_METADATA

Mean quasar continuum

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ============= ============= ===== ===========================
    KEY           Example Value Type  Comment
    ============= ============= ===== ===========================
    NAXIS         2             int   number of array dimensions
    NAXIS1        43            int   table width
    NAXIS2        23168         int   number of forests
    ============= ============= ===== ===========================


Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

==================== ======== ====== ===================
Name                 Type     Units         Description
==================== ======== ====== ===================
LOS_ID               int64           PICCA unique target ID
ZERO_POINT           float64         Continuum zero-point paramter
SLOPE                float64         Continuum slope parameter
CHI2                 float64         Continuum fit chi2
NUM_DATAPOINTS       int64           Number of wavelenth pixels
ACCEPTED_FIT         bool            Fit acceptance
==================== ======== ====== ===================



Notes and Examples
==================

These files are generated with https://github.com/igmhub/picca/blob/master/bin/picca_delta_extraction.py
The code was run twice:

.. code-block:: bash

    picca_delta_extraction.py config/delta_extraction_ciii_step_1.ini
    picca_delta_extraction.py config/delta_extraction_lya.ini
