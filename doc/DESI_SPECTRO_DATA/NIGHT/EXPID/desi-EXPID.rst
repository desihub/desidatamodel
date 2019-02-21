==========
desi-EXPID
==========

:Summary: Raw data from the DESI spectrographs, with one fpack-compressed
    HDU per spectrograph camera
:Naming Convention: ``desi-EXPID.fits.fz``, where EXPID is the zero-padded
    8-digit exposure ID.
:Regex: ``desi-[0-9]{8}\.fits\.fz``
:File Type: FITS, 500 MB

Contents
========

There is one HDU per spectrograph camera with EXTNAMEs like
B0, B1, ... R0, R1, ... Z8, Z9.  The structure of each of these is
the same; only one is explicitly documented below.

================= ========= ======== ====================================
Number            EXTNAME   Type     Contents
================= ========= ======== ====================================
HDU0_             SP0       IMAGE    Blank except for header keywords
HDU1_             SPECTCON0 BINTABLE Telemetry data
HDU2_             B0        IMAGE    Raw data from the b0 spectrograph
`HDU3 -- HDU31`_  various   IMAGE    Raw data similar to b0 spectrograph.
================= ========= ======== ====================================

FITS Header Units
=================

HDU0
----

EXTNAME = SP0

Blank except for header keywords.

Keywords marked **MISSING** were listed in a previous version of this file,
but are not present in the spectrograph functional verification test "sp0" files.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================================================== ===== ===============================================
KEY      Example Value                                              Type  Comment
======== ========================================================== ===== ===============================================
INSTRUME DESI                                                       str   Instrument name
PROCTYPE RAW                                                        str   Data processing level
PRODTYPE image                                                      str   Data product type
PROGRAM  spec tests                                                 str   Program name
EXPID    1000                                                       int   Exposure number
EXPFRAME 0                                                          int   Frame number
FILENAME /exposures/desi/sps/20190220/00001000/sp0-00001000.fits.fz str   Name of
FLAVOR   zero                                                       str   Observation type
REQTIME  0.0                                                        float [s] Requested exposure time
EXPTIME  0.0                                                        float [s] Actual exposure time
OBSID    kp4m20190220t212702                                        str   Unique observation identifier
TIMESYS  UTC                                                        str   Time system used for date-obs
NIGHT    20190220                                                   str   Observing night
DATE-OBS 2019-02-20T21:27:02.730679                                 str   [UTC] Observation data and start time
TIME-OBS 21:27:02.730679                                            str   [UTC] Observation start time
MJD-OBS  58534.894                                                  float Modified Julian Date of observation
ST       00:02:43.730                                               str   Local Sidereal time at observation start (HH:MM
SPECGRPH SP0                                                        str   Spectrograph name
MODULE   SPECTROGRAPHS                                              str   Image Sources/Component
DOSVER   1.001                                                      float DOS software version
DEVICES  SPECTCON0,CCDS0Z,CCDS0R,CCDS0B                             str
CHECKSUM 2aAn3a3k2a9k2a9k                                           str   HDU checksum updated 2019-02-20T21:27:57
DATASUM           0                                                 str   data unit checksum updated 2019-02-20T21:27:57
TELRA    335.03                                                     float Telescope pointing RA [degrees] **MISSING**
TELDEC   19.88                                                      float Telescope pointing dec [degrees] **MISSING**
AIRMASS  1.0                                                        float Airmass at middle of exposure **MISSING**
TILEID   4                                                          int   DESI tile ID **MISSING**
FEEVER   SIM                                                        str   **MISSING**
DETECTOR SIM                                                        str   **MISSING**
DEPNAM00 python                                                     str   **MISSING**
DEPVER00 3.5.2                                                      str   **MISSING**
======== ========================================================== ===== ===============================================

Empty HDU.

HDU1
----

EXTNAME = SPECTCON0

This is a telemetry table.  Note that some of the column names contain a hyphen,
*e.g.* ``DATE-OBS``.  This not a great idea, because some FITS readers may
interpret the hyphen as a minus sign.  Also note that all the columns are
upper-case except for ``unit``.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   208              int  width of table in bytes
NAXIS2   1                int  number of rows in table
EXPID    1000             int  Exposure number
EXPFRAME 0                int  Frame number
SPECGRPH SP0              str  Spectrograph name
DEVICE   SPECTCON0        str  Device/controller name
CHECKSUM BEcVECcUBCcUBCcU str  HDU checksum updated 2019-02-20T21:27:57
DATASUM  1390334580       str  data unit checksum updated 2019-02-20T21:27:57
======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

======== ======== ===== ===================
Name     Type     Units Description
======== ======== ===== ===================
unit     int32          label for field   1
DATE-OBS char[26]       label for field   2
TIME-OBS char[15]       label for field   3
MJD-OBS  float32        label for field   4
ST       char[12]       label for field   5
OBSID    char[19]       label for field   6
STATUS   char[5]        label for field   7
HARTL    char[4]        label for field   8
HARTLP   char[3]        label for field   9
HARTR    char[4]        label for field  10
HARTRP   char[3]        label for field  11
WAGO     char[5]        label for field  12
NIRSHUT  char[4]        label for field  13
NIRSEAL  char[8]        label for field  14
NIRPOW   char[2]        label for field  15
EXPSHUT  char[6]        label for field  16
EXPSEAL  char[8]        label for field  17
EXPPOW   char[2]        label for field  18
ILLUM    char[8]        label for field  19
NIRTEMP  float32        label for field  20
NIRHUMID float32        label for field  21
BLUTEMP  float32        label for field  22
BLUHUMID float32        label for field  23
REDTEMP  float32        label for field  24
REDHUMID float32        label for field  25
MIRROR   char[3]        label for field  26
MOUNT    char[3]        label for field  27
NIRDICHR char[3]        label for field  28
REDDICHR char[3]        label for field  29
BLUEVPHG char[7]        label for field  30
REDVPHG  char[7]        label for field  31
NIRVPHG  char[7]        label for field  32
BLUECAM  char[3]        label for field  33
REDCAM   char[3]        label for field  34
NIRCAM   char[3]        label for field  35
======== ======== ===== ===================

HDU2
----

EXTNAME = B0

Unprocessed spectrograph raw data, including overscans, from camera B0.

Keywords marked **MISSING** were listed in a previous version of this file,
but are not present in the spectrograph functional verification test "sp0" files.
This includes the ``INHERIT`` keyword.

In a previous version of this model, the CCD quadrants were labeled 1, 2, 3, 4;
now they are labeled A, B, C, D.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

========= =================================== ===== ==============================================
KEY       Example Value                       Type  Comment
========= =================================== ===== ==============================================
NAXIS1    8                                   int   width of table in bytes
NAXIS2    4194                                int   number of rows in table
BZERO     32768                               int   offset data range to that of unsigned short
BSCALE    1                                   int   default scaling factor
SPECGRPH  0                                   int   Spectrograph name
DETECTOR  M1-20                               str   Detector (ccd) identification
CAMERA    z0                                  str   Camera name
CCDNAME   CCDS0Z                              str   CCD name
CCDSIZE   4194,4256                           str   CCD size in pixels (rows, columns)
CCDTMING  default_lbnl_timing_20180905.txt    str   CCD timing file
CCDCFG    default_lbnl_20181010.cfg           str   CCD configuration file
SETTINGS  detectors_20181114.json             str   Name of DESI CCD settings file
FEEVER    v20160312                           str   CCD Controller version
PRESECA   [1:7, 2:2065]                       str   Prescan section for quadrant A
PRRSECA   [8:2064, 1:1]                       str   Row prescan section for quadrant A
DATASECA  [8:2064, 2:2065]                    str   Data section for quadrant A
TRIMSECA  [8:2064, 2:2065]                    str   Trim section for quadrant A
BIASSECA  [2065:2128, 2:2065]                 str   Bias section for quadrant A
ORSECA    [8:2064, 2066:2097]                 str   Row overscan section for quadrant A
CCDSECA   [1:2057, 1:2064]                    str   CCD section for quadrant A
DETSECA   [1:2057, 1:2064]                    str   Detector section for quadrant A
AMPSECA   [1:2057, 1:2064]                    str   AMP section for quadrant A
PRESECB   [4250:4256, 2:2065]                 str   Prescan section for quadrant B
PRRSECB   [2193:4249, 1:1]                    str   Row prescan section for quadrant B
DATASECB  [2193:4249, 2:2065]                 str   Data section for quadrant B
TRIMSECB  [2193:4249, 2:2065]                 str   Trim section for quadrant B
BIASSECB  [2129:2192, 2:2065]                 str   Bias section for quadrant B
ORSECB    [2193:4249, 2066:2097]              str   Row overscan section for quadrant B
CCDSECB   [2058:4114, 1:2064]                 str   CCD section for quadrant B
DETSECB   [2058:4114, 1:2064]                 str   Detector section for quadrant B
AMPSECB   [4114:2058, 1:2064]                 str   AMP section for quadrant B
PRESECC   [1:7, 2130:4193]                    str   Prescan section for quadrant C
PRRSECC   [8:2064, 4194:4194]                 str   Row prescan section for quadrant C
DATASECC  [8:2064, 2130:4193]                 str   Data section for quadrant C
TRIMSECC  [8:2064, 2130:4193]                 str   Trim section for quadrant C
BIASSECC  [2065:2128, 2130:4193]              str   Bias section for quadrant C
ORSECC    [8:2064, 2098:2129]                 str   Row overscan section for quadrant C
CCDSECC   [1:2057, 2065:4128]                 str   CCD section for quadrant C
DETSECC   [1:2057, 2065:4128]                 str   Detector section for quadrant C
AMPSECC   [1:2057, 4128:2065]                 str   AMP section for quadrant C
PRESECD   [4250:4256, 2130:4193]              str   Prescan section for quadrant D
PRRSECD   [2193:4249, 4194:4194]              str   Row prescan section for quadrant D
DATASECD  [2193:4249, 2130:4193]              str   Data section for quadrant D
TRIMSECD  [2193:4249, 2130:4193]              str   Trim section for quadrant D
BIASSECD  [2129:2192, 2130:4193]              str   Bias section for quadrant D
ORSECD    [2193:4249, 2098:2129]              str   Row bias section for quadrant D
CCDSECD   [2058:4114, 2065:4128]              str   CCD section for quadrant D
DETSECD   [2058:4114, 2065:4128]              str   Detector section for quadrant D
AMPSECD   [4114:2058, 4128:2065]              str   AMP section for quadrant D
DAC0      -9.0002,-8.8683                     str   [V] set value, measured value
DAC1      -9.0002,-8.8683                     str   [V] set value, measured value
DAC2      -9.0002,-8.8374                     str   [V] set value, measured value
DAC3      -9.0002,-8.8786                     str   [V] set value, measured value
DAC4      5.9998,6.0174                       str   [V] set value, measured value
DAC5      5.9998,6.0648                       str   [V] set value, measured value
DAC6      5.9998,6.0227                       str   [V] set value, measured value
DAC7      5.9998,6.0437                       str   [V] set value, measured value
DAC8      -25.0003,-24.6047                   str   [V] set value, measured value
DAC9      -25.0003,-24.6492                   str   [V] set value, measured value
DAC10     -25.0003,-24.8422                   str   [V] set value, measured value
DAC11     -25.0003,-24.3228                   str   [V] set value, measured value
DAC12     0.0,0.1039                          str   [V] set value, measured value
DAC13     0.0,0.0594                          str   [V] set value, measured value
DAC14     0.0,0.0742                          str   [V] set value, measured value
DAC15     0.0,0.0742                          str   [V] set value, measured value
DAC16     39.9961,39.4086                     str   [V] set value, measured value
DAC17     20.0008,11.9682                     str   [V] set value, measured value
CLOCK0    9.9999,0.0                          str   [V] high rail, low rail
CLOCK1    9.9999,0.0                          str   [V] high rail, low rail
CLOCK2    9.9999,0.0                          str   [V] high rail, low rail
CLOCK3    -2.0001,3.9999                      str   [V] high rail, low rail
CLOCK4    9.9999,0.0                          str   [V] high rail, low rail
CLOCK5    9.9999,0.0                          str   [V] high rail, low rail
CLOCK6    9.9999,0.0                          str   [V] high rail, low rail
CLOCK7    -2.0001,3.9999                      str   [V] high rail, low rail
CLOCK8    9.9992,2.9993                       str   [V] high rail, low rail
CLOCK9    9.9992,2.9993                       str   [V] high rail, low rail
CLOCK10   9.9992,2.9993                       str   [V] high rail, low rail
CLOCK11   9.9992,2.9993                       str   [V] high rail, low rail
CLOCK12   9.9992,2.9993                       str   [V] high rail, low rail
CLOCK13   9.9992,2.9993                       str   [V] high rail, low rail
CLOCK14   9.9992,2.9993                       str   [V] high rail, low rail
CLOCK15   9.9992,2.9993                       str   [V] high rail, low rail
CLOCK16   9.9999,3.0                          str   [V] high rail, low rail
CLOCK17   9.0,0.9999                          str   [V] high rail, low rail
CLOCK18   9.0,0.9999                          str   [V] high rail, low rail
OFFSET0   0.4000000059604645,-8.8683          str   [V] set value, measured value
OFFSET1   0.4000000059604645,-8.8683          str   [V] set value, measured value
OFFSET2   0.4000000059604645,-8.8374          str   [V] set value, measured value
OFFSET3   0.4000000059604645,-8.8786          str   [V] set value, measured value
OFFSET4   2.0,6.0174                          str   [V] set value, measured value
OFFSET5   2.0,6.0648                          str   [V] set value, measured value
OFFSET6   2.0,6.0174                          str   [V] set value, measured value
OFFSET7   2.0,6.0437                          str   [V] set value, measured value
DELAYS    30, 30, 25, 40, 7, 3000, 7, 7, 7, 7 str   [10] Delay settings
PGAGAIN   3                                   int   Controller gain
BLDTIME   0.3355                              float [s] Time to build image
DIGITIME  48.0327                             float [s] Time to digitize image
OBSNUM    1000                                int
FEEBOX    lbnl053                             str
VESSEL    2                                   int
CDSPARAMS na, na, na, na                      str
CHECKSUM  9aEAAZB53aBA9YB5                    str   HDU checksum updated 2019-02-20T21:27:58
DATASUM   1562144619                          str   data unit checksum updated 2019-02-20T21:27:58
GAINA    1.0                                  float Gains from ICS **MISSING**
GAINB    1.0                                  float **MISSING**
GAINC    1.0                                  float **MISSING**
GAIND    1.0                                  float **MISSING**
RDNOISEA 3.0                                  float Expected readnoise from ICS, not measured from these data **MISSING**
RDNOISEB 3.0                                  float **MISSING**
RDNOISEC 3.0                                  float **MISSING**
RDNOISED 3.0                                  float **MISSING**
INHERIT  T                                    bool  https://fits.gsfc.nasa.gov/registry/inherit.html **MISSING**
========= =================================== ===== ==============================================

Data: FITS image [int16 (compressed), 4256x4194]

HDU3 -- HDU31
-------------

EXTNAME = spectrographs(B1, Z9)

Data: See B0.

Notes and Examples
==================

Provenance
----------

* 2019-02-21: Revised based on headers from spectrograph functional verification files.

Problems
--------

* The compressed HDUs in the "sp0" files contain ``ZSIMPLE`` keyword.  This would
  be appropriate in a compressed *primary* HDU but not in a compressed extension.
  Make sure that the images are actually compressed *as extensions*, not as
  individual images that are then shoved into an HDU.
* See also notes on individual HDUs.

Expected Changes
----------------

* Coordinate with ICS for header keywords (*e.g.* ``FLAVOR`` -> ``PROGRAM``).
* Update telemetry HDU.
