=======
pdGFA
=======

:Summary: Fiber Photometry Camera images for ProtoDESI.
:Naming Convention: ``pd-GFA#-MJD5.fits``, where ``#`` is the
   image ID and ``MJD5`` is the five-digit MJD.
:Regex: ``pd-GFA#-MJD5\.fits``


Contents
========

====== ======== ============================== ================================================================
Number EXTNAME  Type                           Contents
====== ======== ============================== ================================================================
HDU0_     NPIXxNPIX float image      raw image

====== ======== ============================== ================================================================

FITS Header Units
=================

HDU0
----

FITS Image: Raw


Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========= ==== ========================================
Header   Value     Type Comment
======== ========= ==== ========================================
XTENSION BINTABLE  str  Binary table written by MWRFITS v1.8
BITPIX   8         int  Required value
NAXIS    2         int  Required value
NAXIS1  3326       int  Number of bytes per row
NAXIS2   2504   int  Number of rows
PCOUNT   0         int  Normally 0 (no varying arrays)
GCOUNT   1         int  Required value
TFIELDS          int  Number of columns in table
======== ========= ==== ========================================

Required Columns
~~~~~~~~~~~~~~~~

================= ======== =======
Column            Type     Comment
================= ======== =======
OBJID             int32[5]
HOLETYPE          char[6]
RA                double
DEC               double
MAG               float[5]
STARL             float
EXPL              float
DEVAUCL           float
OBJTYPE           char[16]
XFOCAL            double
YFOCAL            double
SPECTROGRAPHID    int32
FIBERID           int32
THROUGHPUT        int32
PRIMTARGET        int32
SECTARGET         int32
OFFSETID          int32
SCI_EXPTIME       float
SOURCETYPE        char[7]
LAMBDA_EFF        float
ZOFFSET           float
BLUEFIBER         int32
BOSS_TARGET1      int64
BOSS_TARGET2      int64
ANCILLARY_TARGET1 int64
ANCILLARY_TARGET2 int64
RUN               int32
RERUN             char[5]
CAMCOL            int32
FIELD             int32
ID                int32
CALIBFLUX         float[5]
CALIBFLUX_IVAR    float[5]
SFD_EBV           float

FILE char[?]  Filename
TAI-BEG float Timestamp
EXPTIME float Exposure Time
BIN int32 binning
IMG-X  int64 Image size -x
IMG-Y  float Image size -y
TEL-RA float Telescope RA
TEL-DEC float Tel.DEC
AMASS float Airmass
F0-RA float Fiber 1 RA
F0-DEC float Fiber 1 DEC
F1-RA float Fiber 1 RA
F1-DEC float Fiber 1 DEC
F2-RA float Fiber 2 RA
F2-DEC float Fiber 2 DEC
F3-RA float Fiber 3 RA
F3-DEC float Fiber 3 DEC
TELFOC float Tel.Focus
ZEN float Zenith Distance
HA float Hour Angle
GS-FILE char[?] Guide Star filename
GS-RA float Guide ref pixel RA
GS-DEC float Guide ref pixel DEC
GS-X float Guide ref pixel X
GS-Y float Guide ref pixel Y
================= ======== =======


HDU1
----

FITS Image: Raw

