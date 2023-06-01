=========================================
rejection_log.fits.gz
=========================================

:Summary: This file contains auxiliar output from the picca delta extraction: statistics on rejected forests
:Naming Convention: ``rejection_log.fits.gz``
:Regex: ``rejection_log\.fits\.gz``
:File Type: FITS

Contents
========

====== ============= ======== ========================
Number EXTNAME       Type     Contents
====== ============= ======== ========================
HDU0_  PRIMARY       PRIMARY  Empty
HDU1_  REJECTION_LOG BINTABLE Rejected forest statistics
====== ============= ======== ========================


FITS Header Units
=================

HDU0
----

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = REJECTION_LOG

Rejected forest statistics

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ============= ============= ===== ===========================
    KEY           Example Value Type  Comment
    ============= ============= ===== ===========================
    NAXIS         2             int   number of array dimensions
    NAXIS1        104           int   table width
    NAXIS2        24719         int   number of rejected forests
    ============= ============= ===== ===========================


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
FOREST_SIZE          int64          Number of pixels in the forest
REJECTION_STATUS     char[12]       Rejection status of forest
==================== ======== ===== ===================


    
Notes and Examples
==================

These files are generated with https://github.com/igmhub/picca/blob/master/bin/picca_delta_extraction.py 
The code was run twice:

.. code-block:: bash

    picca_delta_extraction.py config/delta_extraction_ciii_step_1.ini
    picca_delta_extraction.py config/delta_extraction_lya.ini