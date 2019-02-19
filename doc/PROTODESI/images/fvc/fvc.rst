===
fvc
===

:Summary: Fiber View Camera images for ProtoDESI.
:Naming Convention: ``fvc\.[0-9]{8}(_[0-9]{4}|[0-9]{6})\.fits``
:Regex: ``fvc\.[0-9]{8}(_[0-9]{4}|[0-9]{6})\.fits``
:File Type: FITS, 72 MB

Contents
========

====== ======== ===== =========
Number EXTNAME  Type  Contents
====== ======== ===== =========
HDU0_  PRIMARY  IMAGE Raw image
====== ======== ===== =========

FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

Raw image data.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ===================== ===== ===========================================
Header   Value                 Type  Comment
======== ===================== ===== ===========================================
BITPIX   16                    int   number of bits per data pixel
NAXIS    2                     int   number of data axes
NAXIS1   6000                  int   length of data axis 1
NAXIS2   6000                  int   length of data axis 2
BZERO    32768                 int   offset data range to that of unsigned short
BSCALE   1                     int   default scaling factor
EXPID    200728.000032         float Exposure ID
EXPTIME  1.                    float Exposure time in seconds
RDTIME   9.25288391113281      float readout time in seconds
DRKEXP   0                     int   0/1 for open-shutter/dark exposure
DRKFLAG  0                     int   0/1 for unsubtracted/dark-corrected
SIMFLAG  0                     int   0/1 for real/fake image
SIMFIB   0                     int   0/1 for real/fake fiber spots
CCDTEMP  -10.                  float CCD temperature (C)
BASETMP  -10.                  float Camera base temperature (C)
TEMPSET  -10.                  float CCD temperature set point (C)
COOLPOW  50.                   float CCD cooler power (%)
PIXSZX   6.00000021222513E-06  float Camera Pixel Size in x (m)
PIXSZY   6.00000021222513E-06  float Camera Pixel Size in y (m)
CCDX1    0                     int   Physical array start x
CCDX2    8304                  int   Physical array end x
CCDY1    0                     int   Physical array start y
CCDY2    6220                  int   Physical array end y
VISX1    64                    int   Visible array start x
VISX2    8240                  int   Visible array end x
VISY1    45                    int   Visible array start y
VISY2    6177                  int   Visible array end y
SUBX1    1152                  int   Sub-array start x
SUBX2    7151                  int   Sub-array end x
SUBY1    111                   int   Sub-array start y
SUBY2    6110                  int   Sub-array end y
HBIN     0                     int   Horizontal binning
VBIN     0                     int   Vertical binning
OBSNUM   200728                int   Observation Number
OBSFRM   32                    int   Observation Frame
HDREV    256                   int   Camera hardware revision
FWREV    513                   int   Camera firmware revision
DATE     '2016-09-28T11:11:12' str   file creation date (YYYY-MM-DDThh:mm:ss UT)
======== ===================== ===== ===========================================

Data: int16 FITS image [6000, 6000]
