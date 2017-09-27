======================
PROTODESI_FPC
======================

:Summary: Data model for protoDESI Fiber Photometry Camera images for ProtoDESI.

:Naming Convention: ``PROTODESI_FPC_{EXPID}.fits``, where ``{EXPID}``
    is the 8-digit exposure ID.
:Regex: ``PROTODESI_FPC_[0-9]{8}.fits`` *Give a regular expression for this filename.
    For example, a six-digit number would correspond to ``[0-9]{6}``.*
:File Type: FITS, 16 MB  *This section gives the type of the file
    and its approximate size.*

Contents
========

====== ======= ======================== ===================
Number EXTNAME Type                     Contents
====== ======= ======================== ===================
HDU0_  PRIMARY NPIX1xNPIX2 float image  Raw image
====== ======= ======================== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

Raw image

Header Keywords (dump)
~~~~~~~~~~~~~~~~~~~~~~

======== ======================================== ===== ==============================================
KEY      Example Value                            Type  Comment
======== ======================================== ===== ==============================================
NAXIS1   3352                                     int   length of data axis 1
NAXIS2   2532                                     int   length of data axis 2
BZERO    32768                                    int   offset data range to that of unsigned short
BSCALE   1                                        int   default scaling factor or unsigned short
DEVICE   FPC                                      str   imaging device
DATE-OBS 2016-08-17T17:49:22.235092               str   datetime at observation start (UTC)
TIME-OBS 17:49:22.235092                          str   time at observation start (UTC)
MJD-OBS  57617.74261846                           float MJD at observation start
OPENSHUT 2016-08-17T17:49:22.235092               str   time at shutter open (UTC)
LST      08:09:06.860                             str   LST at observation start (HH:mm:ss.ss)
EXPREQ   1.0                                      float [s] Requested Exposure duration, also defined as REQTIME
FILENAME /data/images/PROTODESI_FPC_00000050.fits str   absolute path of file on desirpi1
CCDTEMP  -1.907                                   float CCD temperature **before or after exposure?**
CCDSET   -9.788                                   float setpoint of CCD TEC
CCDPOWER 100.0                                    float cooling power of TEC
TECFROZE F                                        bool  whether TEC is frozen or not
INSTRUME PROTODESI                                str   instrument
EXPNUM   50                                       int   exposure ID
CCDCOOL  T                                        bool  whether TEC is enabled or not
CHECKSUM R2QLS1OIR1OIR1OI                         str   HDU checksum updated 2016-08-17T17:49:25
DATASUM  2903024359                               str   data unit checksum updated 2016-08-17T17:49:25
======== ======================================== ===== ==============================================

Other Header Keywords (not currently present)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================================== ===== ==============================================
KEY      Example Value                            Type  Comment
======== ======================================== ===== ==============================================
XTENSION BINTABLE, IMAGE                          str   binary table written by MWRFITS v1.8
BITPIX   16                                       int   required value
NAXIS    2                                        int   required value
PCOUNT   0                                        int   normally 0 (no varying arrays)
GCOUNT   1                                        int   required value
TFIELDS                                           int   number of columns in table
TIMESYS  UTC                                      str   time system
EXPTIME  1500.1                                   float measured exposure time
CCDBIN1  1                                        int   pixel binning, axis 1
CCDBIN2  1                                        int   pixel binning, axis 2
TELEQUIN 2000.0                                   float equinox of telescope coordinates
TELRA    19:17:34.440                             str   [HH:MM:SS] telescope RA
RA       19:17:34.440                             str   [HH:MM:SS] RA
TELDEC   20:39:59.760                             str   [DD:MM:SS] telescope DEC
DEC      00:00:48.240                             str   [DD:MM:SS] DEC
HA       20:39:59.760                             str   [HH:MM:SS] telescope hour angle
ZD       30.7000                                  float [deg] telescope zenith distance
AIRMASS  1.1620                                   float Airmass
TELFOCUS 1.22, 145.3, 2.9, 4300.1, 0.2,0.0        str   DESI hexapod settings
TELSTAT  Track                                    str   telescope tracking status
FIELDID  2321                                     int   DESI field identifier
OBSTYPE  object                                   str   observation type: zero, dark, dome flat, sky flat, object, test, calibration, guider
SEQID    4x4 dither                               str   sequence name
SEQNUM   2                                        int   number of image in sequence
SEQTOT   16                                       int   total number of images in sequence
======== ======================================== ===== ==============================================


======== ======================================== ===== ==============================================
KEY      Example Value                            Type  Comment
======== ======================================== ===== ==============================================
F0-RA                                             float fiber 0 RA
F0-DEC                                            float fiber 0 DEC
F1-RA                                             float fiber 1 RA
F1-DEC                                            float fiber 1 DEC
F2-RA                                             float fiber 2 RA
F2-DEC                                            float fiber 2 DEC
FIPOS    T                                        bool  fiber positioner data available if true
CYCLES   3                                        int   number of positioner iterations
ONTARGET 3                                        int   number of fibers on target
FAILED   5                                        int   number of failed fiber assignments
MAXRES   12.5                                     float [micron] maximum target-fiber position residual
======== ======================================== ===== ==============================================


======== ======================================== ===== ==============================================
KEY      Example Value                            Type  Comment
======== ======================================== ===== ==============================================
GS-FILE                                           str   guide Star filename
GS-RA                                             float guide ref pixel RA
GS-DEC                                            float guide ref pixel DEC
GS-X                                              float guide ref pixel X
GS-Y                                              float guide ref pixel Y
======== ======================================== ===== ==============================================


======== ======================================== ===== ==============================================
KEY      Example Value                            Type  Comment
======== ======================================== ===== ==============================================
GUIDER   1                                        int   guider (0-absent,1-ok,2-lost star,3-lost all stars)
G-MODE   auto                                     str   guider operation mode
G-CCDNUM 4                                        int   number of active guide CCDs
G-FEEDBK 0.75                                     float guider feedback percentage
G-MEANX  0.1                                      float Guider x-axis mean offsets
G-MEANY  0.2                                      float Guider y-axis mean offsets
G-MEANX2 12.1                                     float Guider x-axis second moment mean offsets
G-MEANY2 12.1                                     float Guider y-axis second moment mean offsets
G-MEANXY 12.1                                     float Guider cross-axis second moment mean offsets
G-MAXX   0.9                                      float Guider x-axis maximum offset
G-MAXY   0.9                                      float Guider y-axis maximum offset
G-FLXVAR 12.4                                     float Guide stars flux variance
G-TRANSP 0.8                                      float Guider average  sky transparency
G-SEEING 0.5                                      float [arcsec] Guider average seeing
G-LATENC 0.15                                     float [s] Guider average latency between exposures
G-EXPTIM 0.5                                      float [s] Guider average exposure time
======== ======================================== ===== ==============================================

Data: FITS image [int16, 3352x2532]


Notes and Examples
==================

The missing keywords listed above in the Other Keywords section, grouped roughly by categories,
are either found in an older version of data model, or defined in DESI-1229 and deemed relevant for protoDESI run.

While this data model is up to date, FPC and GFA images may not be in their final shape and are subject to change.
