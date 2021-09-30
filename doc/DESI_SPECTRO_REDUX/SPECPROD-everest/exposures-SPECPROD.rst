=========
exposures
=========

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``exposures-everest.fits``, where ... *Give a human readable
    description of the filename, e.g. ``blat-{EXPID}`` where ``{EXPID}``
    is the 8-digit exposure ID.*
:Regex: ``exposures-everest.fits`` *Give a regular expression for this filename.
    For example, a six-digit number would correspond to ``[0-9]{6}``.*
:File Type: FITS, 19 MB  *This section gives the type of the file
    and its approximate size.*

Contents
========

====== ========= ======== ===================
Number EXTNAME   Type     Contents
====== ========= ======== ===================
HDU0_            IMAGE    *Brief Description*
HDU1_  EXPOSURES BINTABLE *Brief Description*
HDU2_  FRAMES    BINTABLE *Brief Description*
====== ========= ======== ===================


FITS Header Units
=================

HDU0
----

*Summarize the contents of this HDU.*

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = EXPOSURES

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =====================
KEY    Example Value Type Comment
====== ============= ==== =====================
NAXIS1 337           int  length of dimension 1
NAXIS2 3912          int  length of dimension 2
====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

====================== ======== ===== ===========
Name                   Type     Units Description
====================== ======== ===== ===========
NIGHT                  int32
EXPID                  int32
TILEID                 int32
TILERA                 float64
TILEDEC                float64
MJD                    float64
SURVEY                 char[7]
FAPRGRM                char[16]
FAFLAVOR               char[19]
EXPTIME                float64
EFFTIME_SPEC           float32
GOALTIME               float64
GOALTYPE               char[7]
MINTFRAC               float64
AIRMASS                float32
EBV                    float64
SEEING_ETC             float64
EFFTIME_ETC            float32
TSNR2_ELG              float32
TSNR2_QSO              float32
TSNR2_LRG              float32
TSNR2_LYA              float64
TSNR2_BGS              float32
TSNR2_GPBDARK          float32
TSNR2_GPBBRIGHT        float32
TSNR2_GPBBACKUP        float32
ELG_EFFTIME_DARK       float32
BGS_EFFTIME_BRIGHT     float32
LYA_EFFTIME_DARK       float64
GPB_EFFTIME_DARK       float32
GPB_EFFTIME_BRIGHT     float32
GPB_EFFTIME_BACKUP     float32
TRANSPARENCY_GFA       float64
SEEING_GFA             float64
FIBER_FRACFLUX_GFA     float64
FIBER_FRACFLUX_ELG_GFA float64
FIBER_FRACFLUX_BGS_GFA float64
FIBERFAC_GFA           float64
FIBERFAC_ELG_GFA       float64
FIBERFAC_BGS_GFA       float64
AIRMASS_GFA            float64
SKY_MAG_AB_GFA         float64
SKY_MAG_G_SPEC         float64
SKY_MAG_R_SPEC         float64
SKY_MAG_Z_SPEC         float64
EFFTIME_GFA            float64
EFFTIME_DARK_GFA       float64
EFFTIME_BRIGHT_GFA     float64
EFFTIME_BACKUP_GFA     float64
====================== ======== ===== ===========

HDU2
----

EXTNAME = FRAMES

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =====================
KEY    Example Value Type Comment
====== ============= ==== =====================
NAXIS1 167           int  length of dimension 1
NAXIS2 111720        int  length of dimension 2
====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ======== ===== ===========
Name            Type     Units Description
=============== ======== ===== ===========
NIGHT           int32
EXPID           int32
TILEID          int32
TILERA          float64
TILEDEC         float64
MJD             float64
EXPTIME         float32
AIRMASS         float32
EBV             float64
SEEING_ETC      float64
EFFTIME_ETC     float32
CAMERA          char[2]
TSNR2_GPBDARK   float32
TSNR2_ELG       float32
TSNR2_GPBBRIGHT float32
TSNR2_LYA       float64
TSNR2_BGS       float32
TSNR2_GPBBACKUP float32
TSNR2_QSO       float32
TSNR2_LRG       float32
SURVEY          char[7]
GOALTYPE        char[7]
FAPRGRM         char[16]
FAFLAVOR        char[19]
MINTFRAC        float64
GOALTIME        float64
=============== ======== ===== ===========


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
