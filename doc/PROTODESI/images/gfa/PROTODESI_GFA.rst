=============
PROTODESI_GFA
=============

:Summary: GFA images for ProtoDESI, including guider "postage stamps". Should we also save full frame images?
:Naming Convention: ``PROTODESI_GFA[01]G_roi_[0-9]{8}_[0-9]{4}\.fits``.
:Regex: ``PROTODESI_GFA[01]G_roi_[0-9]{8}_[0-9]{4}\.fits``


Contents
========

====== ======== ============================== ================================================================
Number EXTNAME  Type                           Contents
====== ======== ============================== ================================================================
HDU0_           NPIXxNPIX float image          raw image

====== ======== ============================== ================================================================

FITS Header Units
=================

HDU0
----

FITS Image: Postage Stamp of guide star. Raw.


Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========= ==== ========================================
Header   Value     Type Comment
======== ========= ==== ========================================
XTENSION BINTABLE  str  Binary table written by MWRFITS v1.8
BITPIX   8         int  Required value
NAXIS    2         int  Required value
NAXIS1   2048      int  Number of bytes per row
NAXIS2   2064      int  Number of rows
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
IMG-X             int64    Image size -x
IMG-Y             int64    Image size -y
TEL-RA            float    Telescope RA
TEL-DEC           float    Tel.DEC
AMASS             float    Airmass
TELFOC            float    Tel.Focus
ZEN               float    Zenith Distance
HA                float    Hour Angle
FIELD             int64    Field ID
TEMP              float    Camera Temperature
MODE              str      Mode of Guider
GS-RA             float    Guide ref pixel RA
GS-DEC            float    Guide ref pixel DEC
GS-X              float    Guide ref pixel X
GS-Y              float    Guide ref pixel Y
GS-PSF            float    FWHM of PSF size for guide star
================= ======== =======
