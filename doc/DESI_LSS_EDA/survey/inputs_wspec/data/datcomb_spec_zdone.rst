=========================
datcomb_bright_spec_zdone
=========================

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``datcomb_bright_spec_zdone.fits``, where ... *Give a human readable
    description of the filename, e.g. ``blat-{EXPID}`` where ``{EXPID}``
    is the 8-digit exposure ID.*
:Regex: ``datcomb_bright_spec_zdone.fits`` *Give a regular expression for this filename.
    For example, a six-digit number would correspond to ``[0-9]{6}``.*
:File Type: FITS, 455 MB  *This section gives the type of the file
    and its approximate size.*

Contents
========

====== ======== ======== ===================
Number EXTNAME  Type     Contents
====== ======== ======== ===================
HDU0_           IMAGE    *Brief Description*
HDU1_  ZCATALOG BINTABLE *Brief Description*
====== ======== ======== ===================


FITS Header Units
=================

HDU0
----

*Summarize the contents of this HDU.*

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = ZCATALOG

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ============= ==== =====================
    KEY      Example Value Type Comment
    ======== ============= ==== =====================
    NAXIS1   336           int  length of dimension 1
    NAXIS2   1421660       int  length of dimension 2
    LONGSTRN OGIP 1.0      str
    RRVER    0.15.2        str
    TEMNAM00 GALAXY        str
    TEMVER00 2.6           str
    TEMNAM01 QSO           str
    TEMVER01 0.1           str
    TEMNAM02 STAR:::A      str
    TEMVER02 0.1           str
    TEMNAM03 STAR:::B      str
    TEMVER03 0.1           str
    TEMNAM04 STAR:::CV     str
    TEMVER04 0.1           str
    TEMNAM05 STAR:::F      str
    TEMVER05 0.1           str
    TEMNAM06 STAR:::G      str
    TEMVER06 0.1           str
    TEMNAM07 STAR:::K      str
    TEMVER07 0.1           str
    TEMNAM08 STAR:::M      str
    TEMVER08 0.1           str
    TEMNAM09 STAR:::WD     str
    TEMVER09 0.1           str
    SPGRP    cumulative    str
    SURVEY   main          str
    PROGRAM  bright        str
    ======== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

========================== =========== ===== =========================================================================================================
Name                       Type        Units Description
========================== =========== ===== =========================================================================================================
TARGETID                   int64             Unique DESI target ID
Z                          float64           Redshift measured by Redrock
ZERR                       float64           Redshift error from redrock
ZWARN                      int64             Redshift warning bitmask measured by Redrock
CHI2                       float64           Best fit :math:`\chi^2`
COEFF                      float64[10]       Redrock template coefficients
NPIXELS                    int64
SPECTYPE                   char[6]           Spectype from redrock file
SUBTYPE                    char[20]          Spectral subtype
NCOEFF                     int64
DELTACHI2                  float64           Delta-chi-squared for template fit from Redrock
LOCATION                   int64             Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBER                      int32             Fiber ID on the CCDs [0-4999]
COADD_FIBERSTATUS          int32
FIBERASSIGN_X              float32           Expected CS5 X location on focal plane
FIBERASSIGN_Y              float32           Expected CS5 Y location on focal plane
PRIORITY                   int32             Target current priority
TILEID                     int32             Unique DESI tile ID
COADD_NUMEXP               int16
COADD_EXPTIME              float32
COADD_NUMNIGHT             int16
MEAN_DELTA_X               float32           Mean (over exposures) fiber difference between measured and requested CS5 X location on focal plane
RMS_DELTA_X                float32           RMS (over exposures) of the fiber difference between measured and requested CS5 X location on focal plane
MEAN_DELTA_Y               float32           Mean (over exposures) fiber CS5 Y location on focal plane
RMS_DELTA_Y                float32           RMS (over exposures) of the fiber difference between measured and requested CS5 Y location on focal plane
MEAN_PSF_TO_FIBER_SPECFLUX float32
TSNR2_ELG_B                float32           ELG B template (S/N)^2
TSNR2_LYA_B                float32           LYA B template (S/N)^2
TSNR2_BGS_B                float32           BGS B template (S/N)^2
TSNR2_QSO_B                float32           QSO B template (S/N)^2
TSNR2_LRG_B                float32           LRG B template (S/N)^2
TSNR2_ELG_R                float32           ELG R template (S/N)^2
TSNR2_LYA_R                float32           LYA R template (S/N)^2
TSNR2_BGS_R                float32           BGS R template (S/N)^2
TSNR2_QSO_R                float32           QSO R template (S/N)^2
TSNR2_LRG_R                float32           LRG R template (S/N)^2
TSNR2_ELG_Z                float32           ELG Z template (S/N)^2
TSNR2_LYA_Z                float32           LYA Z template (S/N)^2
TSNR2_BGS_Z                float32           BGS Z template (S/N)^2
TSNR2_QSO_Z                float32           QSO Z template (S/N)^2
TSNR2_LRG_Z                float32           LRG Z template (S/N)^2
TSNR2_ELG                  float32           ELG template (S/N)^2 summed over B,R,Z
TSNR2_LYA                  float32           LYA template (S/N)^2 summed over B,R,Z
TSNR2_BGS                  float32           BGS template (S/N)^2 summed over B,R,Z
TSNR2_QSO                  float32           QSO template (S/N)^2 summed over B,R,Z
TSNR2_LRG                  float32           LRG template (S/N)^2 summed over B,R,Z
ZWARN_MTL                  int64             The ZWARN from the zmtl file (contains extra bits)
Z_QN                       float64           Redshift measured by QuasarNET
Z_QN_CONF                  float64           Redshift confidence from QuasarNET
IS_QSO_QN                  int16             Spectroscopic classification from QuasarNET (1 for a quasar)
========================== =========== ===== =========================================================================================================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
