===========================
ELG_LOPnotqso_7_full_noveto
===========================

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``ELG_LOPnotqso_7_full_noveto.ran.fits``, where ... *Give a human readable
    description of the filename, e.g. ``blat-{EXPID}`` where ``{EXPID}``
    is the 8-digit exposure ID.*
:Regex: ``ELG_LOPnotqso_7_full_noveto.ran.fits`` *Give a regular expression for this filename.
    For example, a six-digit number would correspond to ``[0-9]{6}``.*
:File Type: FITS, 1 GB  *This section gives the type of the file
    and its approximate size.*

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    *Brief Description*
HDU1_  LSS     BINTABLE *Brief Description*
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

EXTNAME = LSS

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =======================
    KEY    Example Value Type Comment
    ====== ============= ==== =======================
    NAXIS1 259           int  width of table in bytes
    NAXIS2 4469949       int  number of rows in table
    ====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

========================== ======== ===== ==========================================================================================================================
Name                       Type     Units Description
========================== ======== ===== ==========================================================================================================================
LOCATION                   int64          Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBER                      int32          Fiber ID on the CCDs [0-4999]
TARGETID                   int64          Unique DESI target ID
RA                         float64        Right Ascension
DEC                        float64        Declination
TILEID                     int64          Unique DESI tile ID
ZWARN                      int64          Redshift warning bitmask measured by Redrock
COADD_FIBERSTATUS          int32
FIBERASSIGN_X              float32        Expected CS5 X location on focal plane
FIBERASSIGN_Y              float32        Expected CS5 Y location on focal plane
PRIORITY                   int32          Target current priority
COADD_NUMEXP               int16
COADD_EXPTIME              float32
COADD_NUMNIGHT             int16
MEAN_DELTA_X               float32        Mean (over exposures) fiber difference between measured and requested CS5 X location on focal plane
RMS_DELTA_X                float32        RMS (over exposures) of the fiber difference between measured and requested CS5 X location on focal plane
MEAN_DELTA_Y               float32        Mean (over exposures) fiber CS5 Y location on focal plane
RMS_DELTA_Y                float32        RMS (over exposures) of the fiber difference between measured and requested CS5 Y location on focal plane
MEAN_PSF_TO_FIBER_SPECFLUX float32
TSNR2_ELG_B                float32        ELG B template (S/N)^2
TSNR2_LYA_B                float32        LYA B template (S/N)^2
TSNR2_BGS_B                float32        BGS B template (S/N)^2
TSNR2_QSO_B                float32        QSO B template (S/N)^2
TSNR2_LRG_B                float32        LRG B template (S/N)^2
TSNR2_ELG_R                float32        ELG R template (S/N)^2
TSNR2_LYA_R                float32        LYA R template (S/N)^2
TSNR2_BGS_R                float32        BGS R template (S/N)^2
TSNR2_QSO_R                float32        QSO R template (S/N)^2
TSNR2_LRG_R                float32        LRG R template (S/N)^2
TSNR2_ELG_Z                float32        ELG Z template (S/N)^2
TSNR2_LYA_Z                float32        LYA Z template (S/N)^2
TSNR2_BGS_Z                float32        BGS Z template (S/N)^2
TSNR2_QSO_Z                float32        QSO Z template (S/N)^2
TSNR2_LRG_Z                float32        LRG Z template (S/N)^2
TSNR2_ELG                  float32        ELG template (S/N)^2 summed over B,R,Z
TSNR2_LYA                  float32        LYA template (S/N)^2 summed over B,R,Z
TSNR2_BGS                  float32        BGS template (S/N)^2 summed over B,R,Z
TSNR2_QSO                  float32        QSO template (S/N)^2 summed over B,R,Z
TSNR2_LRG                  float32        LRG template (S/N)^2 summed over B,R,Z
TILELOCID                  int64          Is 10000*TILEID+LOCATION
NTILE                      int64          Number of tiles target was available on
TILES                      char[9]        TILEIDs of those tile, in string form separated by &#x27;-&#x27;
TILELOCIDS                 char[35]       TILELOCIDs that the target was available for, separated by &#x27;-&#x27;
ZPOSSLOC                   logical        True/False whether the location could have been assigned to the given target class
GOODHARDLOC                logical        True/False whether the fiber had good hardware
LOCFULL                    logical        True/False whether all targets of the given target type available at the location were assigned on some tile
NOBS_G                     int16          Number of images for central pixel in g-band
NOBS_R                     int16          Number of images for central pixel in r-band
NOBS_Z                     int16          Number of images for central pixel in z-band
MASKBITS                   int16          Bitwise mask from the imaging indicating potential issue or blending
PHOTSYS                    char[1]        &#x27;N&#x27; for the MzLS/BASS photometric system, &#x27;S&#x27; for DECaLS
GOODPRI                    logical        True/False whether the priority of what was assigned to the location was &lt;= the base priority of the given target class
GOODTSNR                   logical        True/False whether the TSNR_&lt;class&gt; value used was above the minimum threshold for the given target class
sort                       float64        Number constructed to sort the table prior to cutting to unique TARGETID
elg_mask_optional          binary         Imaging mask bits relevant to ELG targets
lrg_mask_optional          binary         Imaging mask bits relevant to LRG targets
========================== ======== ===== ==========================================================================================================================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
