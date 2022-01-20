========
pm-EXPID
========

:Summary: PlateMaker data.
:Naming Convention: ``pm-EXPID.fits``, where EXPID is the zero-padded
    8-digit exposure ID.
:Regex: ``pm-[0-9]{8}\.fits``
:File Type: FITS, 216 KB

Contents
========

====== ======== ======== ===================
Number EXTNAME  Type     Contents
====== ======== ======== ===================
HDU0_  PM       IMAGE    *Brief Description*
HDU1_  PMGSTARS BINTABLE *Brief Description*
HDU2_  PMCNTPOS BINTABLE *Brief Description*
====== ======== ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = PM

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================== ===== ===============================================
KEY      Example Value              Type  Comment
======== ========================== ===== ===============================================
NAXIS1   1                          int   length of data axis 1
MODULE   PM                         str   Image Sources/Component
EXPID    118526                     int   Exposure number
NIGHT    20220113                   int   Observing night
DATE-OBS 2022-01-14T11:04:16.816410 str   [UTC] Observation data and start time
MJD-OBS  59593.46130575             float Modified Julian Date of observation
ST       11:13:27.570               str   Local Sidereal time at observation start (HH:MM
FWCENTER -5.46,0.35                 str
PMNFSADC 334.05,26.06               str   Platemaker nfsproc adc angles
CHECKSUM IMjAJMi9IMiAIMi9           str   HDU checksum updated 2022-01-14T11:04:16
DATASUM  1072693248                 str   data unit checksum updated 2022-01-14T11:04:16
======== ========================== ===== ===============================================

Data: FITS image [float64, 1]

HDU1
----

EXTNAME = PMGSTARS

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   86               int  width of table in bytes
NAXIS2   18               int  number of rows in table
EXPID    118526           int
MODULE   GUIDESTARS       str
CHECKSUM Y9DGa999Z9AGa999 str  HDU checksum updated 2022-01-14T11:04:16
DATASUM  315340011        str  data unit checksum updated 2022-01-14T11:04:16
======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

========== ======= ===== ===================
Name       Type    Units Description
========== ======= ===== ===================
GFA_LOC    char[6]       label for field   1
RA         float64       label for field   2
DEC        float64       label for field   3
ROW        float64       label for field   4
COL        float64       label for field   5
RA_IVAR    float64       label for field   6
DEC_IVAR   float64       label for field   7
MAG        float64       label for field   8
MORPHTYPE  int64         label for field   9
GUIDE_FLAG int64         label for field  10
ETC_FLAG   int64         label for field  11
========== ======= ===== ===================

HDU2
----

EXTNAME = PMCNTPOS

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   40               int  width of table in bytes
NAXIS2   5133             int  number of rows in table
EXPID    118526           int
MODULE   CENTERPOS        str
CHECKSUM Z28Xe25XZ25Xd25X str  HDU checksum updated 2022-01-14T11:04:16
DATASUM  1190286968       str  data unit checksum updated 2022-01-14T11:04:16
======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

========== ======= ===== ===================
Name       Type    Units Description
========== ======= ===== ===================
PETAL_LOC  int64         label for field   1
DEVICE_LOC int64         label for field   2
XPIX       float64       label for field   3
YPIX       float64       label for field   4
FLAGS      int64         label for field   5
========== ======= ===== ===================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
