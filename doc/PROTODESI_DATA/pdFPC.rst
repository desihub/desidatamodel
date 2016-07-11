=======
pdFPC
=======

:Summary: Fiber Photometry Camera images for ProtoDESI.
:Naming Convention: ``pdFPC-ID#-MJD5.fits``, where ``ID#`` is the
   image ID and ``MJD5`` is the five-digit MJD.
:Regex: ``pdFPC-[0-9]{3}-[0-9]{5}\.fits``


Contents
========

====== ========== ======================= ================================================================
Number EXTNAME    Type                    Contents
====== ========== ======================= ================================================================
HDU0_             NPIX1xNPIX2 float image  raw image
HDU1_                                      Analyzed image/postage stamps?
====== ========== ======================= ================================================================

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
NAXIS1   3326      int  Number of bytes per row
NAXIS2   2504      int  Number of rows
PCOUNT   0         int  Normally 0 (no varying arrays)
GCOUNT   1         int  Required value
TFIELDS            int  Number of columns in table
======== ========= ==== ========================================

Required Columns
~~~~~~~~~~~~~~~~

================= ======== =======
Column            Type     Comment
================= ======== =======
TAI-BEG           float    Timestamp
EXPTIME           float    Exposure Time
BIN               int32    binning
TEMP              float    Temp of camera
IMG-X             int64    Image size -x
IMG-Y             float    Image size -y
TEL-RA            float    Telescope RA
TEL-DEC           float    Tel.DEC
AMASS             float    Airmass
FIELD             int64    Field ID
F0-RA             float    Fiber 0 RA
F0-DEC            float    Fiber 0 DEC
F1-RA             float    Fiber 1 RA
F1-DEC            float    Fiber 1 DEC
F2-RA             float    Fiber 2 RA
F2-DEC            float    Fiber 2 DEC
F3-RA             float    Fiber 3 RA
F3-DEC            float    Fiber 3 DEC
TELFOC            float    Tel.Focus
ZEN               float    Zenith Distance
HA                float    Hour Angle
GS-FILE           char[?]  Guide Star filename
GS-RA             float    Guide ref pixel RA
GS-DEC            float    Guide ref pixel DEC
GS-X              float    Guide ref pixel X
GS-Y              float    Guide ref pixel Y
FRAMETYPE         str      Frame type: bias, dark, flat, object
================= ======== =======


HDU1
----

FITS Image: Raw

