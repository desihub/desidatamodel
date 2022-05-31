=============
PROTODESI_GFA
=============

:Summary: GFA images for ProtoDESI, including guider "postage stamps". Should we also save full frame images?
:Naming Convention: ``PROTODESI_GFA[01]G_roi_[0-9]{8}_[0-9]{4}\.fits``.
:Regex: ``PROTODESI_GFA[01]G_roi_[0-9]{8}_[0-9]{4}\.fits``
:File Type: FITS

Contents
========

====== ======== ===== =========
Number EXTNAME  Type  Contents
====== ======== ===== =========
HDU0_  PRIMARY  IMAGE Raw image
HDU1_  GFA      IMAGE Raw image
====== ======== ===== =========

FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

Empty HDU.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================================================= ===== ==============================================
Header   Value                                                     Type  Comment
======== ========================================================= ===== ==============================================
DEVICE   'GFA1G   '                                                str
OBSNUM   1622                                                      int
OBSFRAME 7                                                         int
OBSTYPE  'ROI     '                                                str
DATE-OBS '2016-08-31T03:10:47.945228'                              str
TIME-OBS '03:10:47.945228'                                         str
MJD-OBS  57631.13249937                                            float
OPENSHUT '2016-08-31T03:10:47.945228'                              str
LST      '18:23:19.990'                                            str
EXPREQ   1.                                                        float
EXPTIME  1.                                                        float
FILENAME '/data/images/gfa/PROTODESI_GFA1G_roi_00001622_0007.fits' str
ROI_LIST '(190.51099891749917, 124.5090160850238)'                 str
CHECKSUM 'Y72la70kS70kY70k'                                        str   HDU checksum updated 2016-08-31T03:10:47
DATASUM  '         0'                                              str   data unit checksum updated 2016-08-31T03:10:47
======== ========================================================= ===== ==============================================

HDU1
----

EXTNAME = GFA

This is the actual GFA image, which got stored in an extension instead
of the primary.

======== ================== ===== ==============================================
Header   Value              Type  Comment
======== ================== ===== ==============================================
BITPIX   16                 int   number of bits per data pixel
NAXIS    2                  int   number of data axes
NAXIS1   64                 int   length of data axis 1
NAXIS2   64                 int   length of data axis 2
PCOUNT   0                  int   required keyword; must = 0
GCOUNT   1                  int   required keyword; must = 1
BZERO    32768              int   offset data range to that of unsigned short
BSCALE   1                  int   default scaling factor
ROI_X    190.510998917499   float
ROI_Y    124.509016085024   float
SHAPE    '64,64   '         str
DTYPE    'uint16  '         str
CHECKSUM 'EeRhFZQZEbQfEZQZ' str   HDU checksum updated 2016-08-31T03:10:47
DATASUM  '1260997802'       str   data unit checksum updated 2016-08-31T03:10:47
======== ================== ===== ==============================================

Data: int16 FITS image [64, 64]
