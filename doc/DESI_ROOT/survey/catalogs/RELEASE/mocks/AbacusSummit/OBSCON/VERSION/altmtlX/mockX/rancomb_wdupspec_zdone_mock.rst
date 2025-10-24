===================
RANDCOMB FILE ZDONE
===================

:Summary: Match of potential assignments from randoms with information from the observed mock sample given the TILEID and the LOCATION
:Naming Convention: ``rancomb_{RANN}{OBSCON}wdupspec_zdone.fits``, where ``{RANN}`` is the number of the random file (0 through 17) and ``{OBSCON}`` is the observing program, either ``dark`` or ``bright``.
:Regex: ``rancomb_[0-9]+(dark|bright)wdupspec_zdone.fits`` 
:File Type: FITS, 2 GB  

Contents
========

====== ======== ======== ===================
Number EXTNAME  Type     Contents
====== ======== ======== ===================
HDU0_           IMAGE    Empty
HDU1_  LSS      BINTABLE Catalog data
====== ======== ======== ===================


FITS Header Units
=================

HDU0
----

Empty HDU.

HDU1
----

EXTNAME = LSS

Main data HDU. Merger of randoms to target info in given fibers

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =====================
    KEY    Example Value Type Comment
    ====== ============= ==== =====================
    NAXIS1 80            int  length of dimension 1
    NAXIS2 39479166      int  length of dimension 2
    DESIDR dr1           str  DESI Data Release
    ====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

========= ======= ===== =======================================================
Name      Type    Units Description
========= ======= ===== =======================================================
LOCATION  int64         Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBER     int64         Fiber ID on the CCDs [0-4999]
TARGETID  int64         Unique DESI target ID
RA        float64 deg   Barycentric Right Ascension in ICRS
DEC       float64 deg   Barycentric declination in ICRS
TILEID    int64         Unique DESI tile ID
PRIORITY  int32         Priority of the DESI target that was assigned to the given TILEID and LOCATION
TSNR2_ELG float32       ELG template (S/N)^2 summed over B,R,Z
TSNR2_LYA float32       LYA template (S/N)^2 summed over B,R,Z
TSNR2_BGS float32       BGS template (S/N)^2 summed over B,R,Z
TSNR2_QSO float32       QSO template (S/N)^2 summed over B,R,Z
TSNR2_LRG float32       LRG template (S/N)^2 summed over B,R,Z
========= ======= ===== =======================================================

