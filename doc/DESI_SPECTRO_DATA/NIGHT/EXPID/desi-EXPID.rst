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
HDU0_             SPS       IMAGE    Blank except for header keywords
HDU1_             B0        IMAGE    Raw data from the b0 spectrograph
`HDU2 -- HDU30`_  various   IMAGE    Raw data similar to b0 spectrograph.
HDU31_            SPECTCONS BINTABLE Telemetry data
================= ========= ======== ====================================

FITS Header Units
=================

HDU0
----

EXTNAME = SPS

Blank except for header keywords.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================================================== ===== ===============================================
KEY      Example Value                                              Type  Comment
======== ========================================================== ===== ===============================================
OBSERVAT KPNO                                                       str   Observatory name
OBS-LAT  31.96403                                                   str   [deg] Observatory latitude **TYPE**: Should be float.
OBS-LONG -111.59989                                                 str   [deg] Observatory east longitude **TYPE**: Should be float.
OBS-ELEV 2097.                                                      float [m] Observatory elevation
TELESCOP KPNO 4.0-m telescope                                       str   Telescope name
INSTRUME DESI                                                       str   Instrument name
PROGRAM  CALIB                                                      str   Program name
PROPID   2015A-0001                                                 str   Proposal ID **UNEXPECTED**: Does DESI *have* a PROPID?
MANIFEST F                                                          bool  DOS exposure manifest
EXPID    1000                                                       int   Exposure number
EXPFRAME 0                                                          int   Frame number
FRAMES                                                              str   Number of Frames in Archive **TYPE**: Should be integer.
SEQUENCE Spectrographs                                              str   OCS Sequence name
SEQID    15 requests                                                str   Exposure sequence identifier
SEQNUM   1                                                          int   Number of exposure in sequence
SEQTOT   15                                                         int   Total number of exposures in sequence
FILENAME /exposures/desi/20190306/00001209/desi-00001209.fits.fz    str   Name of (F
FLAVOR   dark                                                       str   Observation type
REQTIME  900.                                                       float [s] Requested exposure time
EXPTIME  900.                                                       float [s] Actual exposure time
OBJECT                                                              str   Object name
CAMSHUT  closed                                                     str   Shutter status during observation
TIMESYS  UTC                                                        str   Time system used for date-obs
RADESYS  FK5                                                        str   Coordinate reference frame of major/minor axes
EPOCH    2000.                                                      float Epoch of observation **WARNING**: EQUINOX
NIGHT    20190307                                                   str   Observing night
DATE-OBS 2019-03-07T01:58:00.646185                                 str   [UTC] Observation data and start time
MJD-OBS  58549.082                                                  float Modified Julian Date of observation
ST       05:29:37.900                                               str   Local Sidereal time at observation start (HH:MM
DELTARA  0.                                                         float [arcsec] Offset], right ascension, observer inp
DELTADEC 0.                                                         float [arcsec] Offset], declination, observer input
SPCGRPHS SP0,SP2                                                    str   Participating spectrographs
GUIDMODE catalog                                                    str   Guider mode
AOS      F                                                          bool  AOS data available if true
TDEWPNT  -1.97                                                      float Telescope air dew point
TAIRFLOW 0.                                                         float Telescope air flow
TAIRITMP 20.3                                                       float [deg] Telescope air in temperature
TAIROTMP 20.4                                                       float [deg] Telescope air out temperature
TAIRTEMP 20.794                                                     float [deg] Telescope air temperature
TCASITMP 20.2                                                       float [deg] Telescope Cass Cage in temperature
TCASOTMP 20.5                                                       float [deg] Telescope Cass Cage out temperature
TCSITEMP 20.6                                                       float [deg] Telescope center section in temperature
TCSOTEMP 20.6                                                       float [deg] Telescope center section out temperature
TCIBTEMP 20.7                                                       float [deg] Telescope chimney IB temperature
TCIMTEMP 20.6                                                       float [deg] Telescope chimney IM temperature
TCITTEMP 20.7                                                       float [deg] Telescope chimney IT temperature
TCOSTEMP 20.9                                                       float [deg] Telescope chimney OS temperature
TCOWTEMP 20.8                                                       float [deg] Telescope chimney OW temperature
TDBTEMP  20.3                                                       float [deg] Telescope dec bore temperature
TFLOWIN  0.                                                         float Telescope flow rate in
TFLOWOUT 0.                                                         float Telescope flow rate out
TGLYCOLI 20.4                                                       float [deg] Telescope glycol in temperature
TGLYCOLO 20.2                                                       float [deg] Telescope glycol out temperature
THINGES  20.7                                                       float [deg] Telescope hinge S temperature
THINGEW  20.8                                                       float [deg] Telescope hinge W temperature
TPMAVERT -99.9                                                      float [deg] Telescope mirror averagetemperature
TPMDESIT 12.                                                        float [deg] Telescope mirror desired temperature
TPMEIBT  19.9                                                       float [deg] Telescope mirror EIB temperature
TPMEITT  20.2                                                       float [deg] Telescope mirror EIT temperature
TPMEOBT  20.                                                        float [deg] Telescope mirror EOB temperature
TPMEOTT  20.2                                                       float [deg] Telescope mirror EOT temperature
TPMNIBT  19.8                                                       float [deg] Telescope mirror NIB temperature
TPMNITT  20.2                                                       float [deg] Telescope mirror NIT temperature
TPMNOBT  20.                                                        float [deg] Telescope mirror NOB temperature
TPMNOTT  20.3                                                       float [deg] Telescope mirror NOT temperature
TPMRTDT  -99.9                                                      float [deg] Telescope mirror RTD temperature
TPMSIBT  20.1                                                       float [deg] Telescope mirror SIB temperature
TPMSITT  20.3                                                       float [deg] Telescope mirror SIT temperature
TPMSOBT  19.9                                                       float [deg] Telescope mirror SOB temperature
TPMSOTT  20.2                                                       float [deg] Telescope mirror SOT temperature
TPMSTAT  air off                                                    str   Telescope mirror status
TPMWIBT  20.                                                        float [deg] Telescope mirror WIB temperature
TPMWITT  20.4                                                       float [deg] Telescope mirror WIT temperature
TPMWOBT  20.                                                        float [deg] Telescope mirror WOB temperature
TPMWOTT  20.4                                                       float [deg] Telescope mirror WOT temperature
TPCITEMP 20.3                                                       float [deg] Telescope primary cell in temperature
TPCOTEMP 20.2                                                       float [deg] Telescope primary cell out temperature
TPR1HUM  0.                                                         float Telescope probe 1 humidity
TPR1TEMP 0.                                                         float [deg] Telescope probe1 temperature
TPR2HUM  -99.99                                                     float Telescope probe 2 humidity
TPR2TEMP -99.99                                                     float [deg] Telescope probe2 temperature
TSERVO   40.                                                        float Telescope servo setpoint
TTRSTEMP 20.6                                                       float [deg] Telescope top ring S temperature
TTRWTEMP 20.6                                                       float [deg] Telescope top ring W temperature
TTRUETBT 20.3                                                       float [deg] Telescope truss ETB temperature
TTRUETTT 20.3                                                       float [deg] Telescope truss ETT temperature
TTRUNTBT 20.4                                                       float [deg] Telescope truss NTB temperature
TTRUNTTT 20.4                                                       float [deg] Telescope truss NTT temperature
TTRUSTBT 20.4                                                       float [deg] Telescope truss STB temperature
TTRUSTST 20.7                                                       float [deg] Telescope truss STS temperature
TTRUSTTT 20.4                                                       float [deg] Telescope truss STT temperature
TTRUTSBT 20.3                                                       float [deg] Telescope truss TSB temperature
TTRUTSMT 20.3                                                       float [deg] Telescope truss TSM temperature
TTRUTSTT 20.3                                                       float [deg] Telescope truss TST temperature
TTRUWTBT 20.3                                                       float [deg] Telescope truss WTB temperature
TTRUWTTT 20.4                                                       float [deg] Telescope truss WTT temperature
ALARM    F                                                          bool  UPS major alarm or check battery
ALARM-ON F                                                          bool  UPS active alarm condition
BATTERY  100.                                                       float [%] UPS Battery left
SECLEFT  10494.                                                     float [s] UPS Seconds left
UPSSTAT  System Normal - On Line(7)                                 str   UPS Status
INAMPS   42.8                                                       float [A] UPS total input current
OUTWATTS 2400.0,4200.0,2900.0                                       str   [W] UPS Phase A, B, C output watts
COMPDEW  -5.9                                                       float [deg C] Computer room dewpoint
COMPHUM  17.                                                        float [%] Computer room humidity
COMPAMB  17.8                                                       float [deg C] Computer room ambient temperature
COMPTEMP 20.                                                        float [deg C] Computer room hygrometer temperature
DEWPOINT -11.7                                                      float [deg C] (outside) dewpoint
GUST     107.4                                                      float [m/s] Wind gusts speed
HUMIDITY 17.5                                                       float [%] (outside) humidity
PRESSURE 791.4                                                      float [torr] (outside) air pressure
OUTTEMP  12.4                                                       float [deg C] outside temperature
WINDDIR  197.1                                                      float [deg] wind direction
WINDSPD  36.9                                                       float [m/s] wind speed
CFLOOR   13.8                                                       float [deg C] temperature on C floor
NWALLIN  15.5                                                       float [deg C] temperature at north wall inside
NWALLOUT 13.2                                                       float [deg C] temperature at north wall outside
WWALLIN  15.4                                                       float [deg C] temperature at west wall inside
WWALLOUT 13.6                                                       float [deg C] temperature at west wall outside
AMNIENTN 14.9                                                       float [deg C] ambient temperature north
AMBIENTS 16.1                                                       float [deg C] ambient temperature south
FLOOR    14.7                                                       float [deg C] temperature at floor (LCR)
EWALLCMP 14.1                                                       float [deg C] temperature at east wall, computer room
EWALLCOU 13.4                                                       float [deg C] temperature at east wall, Coude room
ROOF     14.                                                        float [deg C] temperature on roof
ROOFAMB  13.9                                                       float [deg C] ambient temperature on roof
DOMEBLOW 14.8                                                       float [deg C] temperature at dome back, lower
DOMEBUP  14.8                                                       float [deg C] temperature at dome back, upper
DOMELLOW 14.9                                                       float [deg C] temperature at dome left, lower
DOMELUP  15.3                                                       float [deg C] temperature at dome left, upper
DOMERLOW 14.8                                                       float [deg C] temperature at dome right, lower
DOMERUP  14.6                                                       float [deg C] temperature at dome right, upper
GLYCOL   6.6                                                        float [deg C] glycol temperature
MFLOOR                                                              str   [deg C] temperature on main floor **TYPE**: Should be float.
PLATFORM 14.9                                                       float [deg C] temperature at platform
SHACKC   16.6                                                       float [deg C] temperature at shack ceiling
SHACKW   15.3                                                       float [deg C] temperature at shack wall
STAIRSL  14.5                                                       float [deg C] temperature at stairs, lower
STAIRSM  14.6                                                       float [deg C] temperature at stairs, mid
STAIRSU  14.8                                                       float [deg C] temperature at stairs, upper
TELBASE  13.2                                                       float [deg C] temperature at telescope base
UTILWALL 14.7                                                       float [deg C] temperature at utility room wall
UTILROOM 14.9                                                       float [deg C] temperature in utilitiy room
MODULE   SPS                                                        str   Image Sources/Component
ADCCORR  T                                                          bool  Correct pointing for ADC setting if True
EXCLUDED                                                            str   Components excluded from this exposure
DOSVER   current                                                    str   DOS software version
CONSTVER DEFAULT                                                    str   Constants version
HIERARCH OBSERVERS = '[''DESIObserver'']'                           str   **UNEXPECTED**: Why do we need HIERARCH cards?
LEAD     RunManager                                                 str
OCSVER   1.2                                                        float
INIFILE  /n/home/msdos/dos_home/architectures/kpno/spectrograph.ini str
CHECKSUM 5PAo7M2l5M8l5M8l                                           str   HDU checksum updated 2019-03-07T02:13:53
DATASUM  0                                                          str   data unit checksum updated 2019-03-07T02:13:53 **TYPE**: Should be integer.
TELRA    335.03                                                     float Telescope pointing RA [degrees] **MISSING**
TELDEC   19.88                                                      float Telescope pointing dec [degrees] **MISSING**
AIRMASS  1.0                                                        float Airmass at middle of exposure **MISSING**
TILEID   4                                                          int   DESI tile ID **MISSING**
DEPNAM00 python                                                     str   **MISSING**
DEPVER00 3.5.2                                                      str   **MISSING**
======== ========================================================== ===== ===============================================

Empty HDU.

HDU1
----

EXTNAME = B0

Unprocessed spectrograph raw data, including overscans, from camera B0.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== =================================== ===== ==============================================
KEY      Example Value                       Type  Comment
======== =================================== ===== ==============================================
NAXIS1   8                                   int   width of table in bytes
NAXIS2   4194                                int   number of rows in table
BZERO    32768                               int   offset data range to that of unsigned short
BSCALE   1                                   int   default scaling factor
INSTRUME DESI                                str  Instrument name
PROCTYPE RAW                                 str  Data processing level
PRODTYPE image                               str  Data product type
PROGRAM  spec tests                          str  Program name
EXPID    1209                                int   Exposure number
EXPFRAME 0                                   int   Frame number
FILENAME .../sp0-00001209.fits.fz            str   Name
FLAVOR   dark                                str   Observation type
REQTIME  900.                                float [s] Requested exposure time
EXPTIME  900.                                float [s] Actual exposure time
OBSID    kp4m20190307t015800                 str   Unique observation identifier
TIMESYS  UTC                                 str   Time system used for date-obs
NIGHT    20190307                            str   Observing night
DATE-OBS 2019-03-07T01:58:00.646185          str   [UTC] Observation data and start time
TIME-OBS 01:58:00.646185                     str   [UTC] Observation start time
MJD-OBS  58549.082                           float Modified Julian Date of observation
ST       05:29:37.900                        str   Local Sidereal time at observation start (HH:MM
SPECGRPH 0                                   int   Spectrograph name
DETECTOR M1-20                               str   Detector (ccd) identification
CAMERA   z0                                  str   Camera name
CCDNAME  CCDS0Z                              str   CCD name
CCDPREP  purge,clear                         str   CCD prep actions
CCDSIZE  4194,4256                           str   CCD size in pixels (rows, columns)
CCDTMING default_lbnl_timing_20180905.txt    str   CCD timing file
CCDCFG   default_lbnl_20181010.cfg           str   CCD configuration file
SETTINGS detectors_20181114.json             str   Name of DESI CCD settings file
FEEVER   v20160312                           str   CCD Controller version
PRESECA  [1:7, 2:2065]                       str   Prescan section for quadrant A
PRRSECA  [8:2064, 1:1]                       str   Row prescan section for quadrant A
DATASECA [8:2064, 2:2065]                    str   Data section for quadrant A
TRIMSECA [8:2064, 2:2065]                    str   Trim section for quadrant A
BIASSECA [2065:2128, 2:2065]                 str   Bias section for quadrant A
ORSECA   [8:2064, 2066:2097]                 str   Row overscan section for quadrant A
CCDSECA  [1:2057, 1:2064]                    str   CCD section for quadrant A
DETSECA  [1:2057, 1:2064]                    str   Detector section for quadrant A
AMPSECA  [1:2057, 1:2064]                    str   AMP section for quadrant A
PRESECB  [4250:4256, 2:2065]                 str   Prescan section for quadrant B
PRRSECB  [2193:4249, 1:1]                    str   Row prescan section for quadrant B
DATASECB [2193:4249, 2:2065]                 str   Data section for quadrant B
TRIMSECB [2193:4249, 2:2065]                 str   Trim section for quadrant B
BIASSECB [2129:2192, 2:2065]                 str   Bias section for quadrant B
ORSECB   [2193:4249, 2066:2097]              str   Row overscan section for quadrant B
CCDSECB  [2058:4114, 1:2064]                 str   CCD section for quadrant B
DETSECB  [2058:4114, 1:2064]                 str   Detector section for quadrant B
AMPSECB  [4114:2058, 1:2064]                 str   AMP section for quadrant B
PRESECC  [1:7, 2130:4193]                    str   Prescan section for quadrant C
PRRSECC  [8:2064, 4194:4194]                 str   Row prescan section for quadrant C
DATASECC [8:2064, 2130:4193]                 str   Data section for quadrant C
TRIMSECC [8:2064, 2130:4193]                 str   Trim section for quadrant C
BIASSECC [2065:2128, 2130:4193]              str   Bias section for quadrant C
ORSECC   [8:2064, 2098:2129]                 str   Row overscan section for quadrant C
CCDSECC  [1:2057, 2065:4128]                 str   CCD section for quadrant C
DETSECC  [1:2057, 2065:4128]                 str   Detector section for quadrant C
AMPSECC  [1:2057, 4128:2065]                 str   AMP section for quadrant C
PRESECD  [4250:4256, 2130:4193]              str   Prescan section for quadrant D
PRRSECD  [2193:4249, 4194:4194]              str   Row prescan section for quadrant D
DATASECD [2193:4249, 2130:4193]              str   Data section for quadrant D
TRIMSECD [2193:4249, 2130:4193]              str   Trim section for quadrant D
BIASSECD [2129:2192, 2130:4193]              str   Bias section for quadrant D
ORSECD   [2193:4249, 2098:2129]              str   Row bias section for quadrant D
CCDSECD  [2058:4114, 2065:4128]              str   CCD section for quadrant D
DETSECD  [2058:4114, 2065:4128]              str   Detector section for quadrant D
AMPSECD  [4114:2058, 4128:2065]              str   AMP section for quadrant D
DAC0     -9.0002,-8.8683                     str   [V] set value, measured value
DAC1     -9.0002,-8.8683                     str   [V] set value, measured value
DAC2     -9.0002,-8.8374                     str   [V] set value, measured value
DAC3     -9.0002,-8.8786                     str   [V] set value, measured value
DAC4     5.9998,6.0174                       str   [V] set value, measured value
DAC5     5.9998,6.0648                       str   [V] set value, measured value
DAC6     5.9998,6.0227                       str   [V] set value, measured value
DAC7     5.9998,6.0437                       str   [V] set value, measured value
DAC8     -25.0003,-24.6047                   str   [V] set value, measured value
DAC9     -25.0003,-24.6492                   str   [V] set value, measured value
DAC10    -25.0003,-24.8422                   str   [V] set value, measured value
DAC11    -25.0003,-24.3228                   str   [V] set value, measured value
DAC12    0.0,0.1039                          str   [V] set value, measured value
DAC13    0.0,0.0594                          str   [V] set value, measured value
DAC14    0.0,0.0742                          str   [V] set value, measured value
DAC15    0.0,0.0742                          str   [V] set value, measured value
DAC16    39.9961,39.4086                     str   [V] set value, measured value
DAC17    20.0008,11.9682                     str   [V] set value, measured value
CLOCK0   9.9999,0.0                          str   [V] high rail, low rail
CLOCK1   9.9999,0.0                          str   [V] high rail, low rail
CLOCK2   9.9999,0.0                          str   [V] high rail, low rail
CLOCK3   -2.0001,3.9999                      str   [V] high rail, low rail
CLOCK4   9.9999,0.0                          str   [V] high rail, low rail
CLOCK5   9.9999,0.0                          str   [V] high rail, low rail
CLOCK6   9.9999,0.0                          str   [V] high rail, low rail
CLOCK7   -2.0001,3.9999                      str   [V] high rail, low rail
CLOCK8   9.9992,2.9993                       str   [V] high rail, low rail
CLOCK9   9.9992,2.9993                       str   [V] high rail, low rail
CLOCK10  9.9992,2.9993                       str   [V] high rail, low rail
CLOCK11  9.9992,2.9993                       str   [V] high rail, low rail
CLOCK12  9.9992,2.9993                       str   [V] high rail, low rail
CLOCK13  9.9992,2.9993                       str   [V] high rail, low rail
CLOCK14  9.9992,2.9993                       str   [V] high rail, low rail
CLOCK15  9.9992,2.9993                       str   [V] high rail, low rail
CLOCK16  9.9999,3.0                          str   [V] high rail, low rail
CLOCK17  9.0,0.9999                          str   [V] high rail, low rail
CLOCK18  9.0,0.9999                          str   [V] high rail, low rail
OFFSET0  0.4000000059604645,-8.8683          str   [V] set value, measured value
OFFSET1  0.4000000059604645,-8.8683          str   [V] set value, measured value
OFFSET2  0.4000000059604645,-8.8374          str   [V] set value, measured value
OFFSET3  0.4000000059604645,-8.8786          str   [V] set value, measured value
OFFSET4  2.0,6.0174                          str   [V] set value, measured value
OFFSET5  2.0,6.0648                          str   [V] set value, measured value
OFFSET6  2.0,6.0174                          str   [V] set value, measured value
OFFSET7  2.0,6.0437                          str   [V] set value, measured value
DELAYS   30, 30, 25, 40, 7, 3000, 7, 7, 7, 7 str   [10] Delay settings
PGAGAIN  3                                   int   Controller gain
BLDTIME  0.3355                              float [s] Time to build image
DIGITIME 48.0327                             float [s] Time to digitize image
OBSNUM   1000                                int
FEEBOX   lbnl053                             str
VESSEL   2                                   int
HIERARCH CDSPARAMS = 'na, na, na, na'        str   **UNEXPECTED**: Why do we need HIERARCH cards?
CHECKSUM 9aEAAZB53aBA9YB5                    str   HDU checksum updated 2019-02-20T21:27:58
DATASUM  1562144619                          str   data unit checksum updated 2019-02-20T21:27:58 **TYPE**: Should be integer.
GAINA    1.0                                 float Gains from ICS **MISSING**
GAINB    1.0                                 float **MISSING**
GAINC    1.0                                 float **MISSING**
GAIND    1.0                                 float **MISSING**
RDNOISEA 3.0                                 float Expected readnoise from ICS, not measured from these data **MISSING**
RDNOISEB 3.0                                 float **MISSING**
RDNOISEC 3.0                                 float **MISSING**
RDNOISED 3.0                                 float **MISSING**
INHERIT  T                                   bool  https://fits.gsfc.nasa.gov/registry/inherit.html **MISSING**
======== =================================== ===== ==============================================

Data: FITS image [int16 (compressed), 4256x4194]

HDU2 -- HDU30
-------------

EXTNAME = B1, B2, B3, B4, B5, B6, B7, B8, B9, R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, Z0, Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z9

Data: See B0.

HDU31
-----

EXTNAME = SPECTCONS

This is a telemetry table.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============================================================= ===== ==============================================
KEY      Example Value                                                 Type  Comment
======== ============================================================= ===== ==============================================
NAXIS1   248                                                           int   width of table in bytes
NAXIS2   1                                                             int   number of rows in table
INSTRUME DESI                                                          str   Instrument name
PROCTYPE RAW                                                           str   Data processing level
PRODTYPE image                                                         str   Data product type
PROGRAM  spec tests                                                    str   Program name
EXPID    1209                                                          int   Exposure number
EXPFRAME 0                                                             int   Frame number
FILENAME /exposures/desi/specs/20190306/00001209/sp0-00001209.fits.fz  str   Name **UNEXPECTED**: Why is this here?
FLAVOR   dark                                                          str   Observation type
REQTIME  900.                                                          float [s] Requested exposure time
EXPTIME  900.                                                          float [s] Actual exposure time
OBSID    kp4m20190307t015800                                           str   Unique observation identifier
TIMESYS  UTC                                                           str   Time system used for date-obs
NIGHT    20190307                                                      str   Observing night
DATE-OBS 2019-03-07T01:58:00.646185                                    str   [UTC] Observation data and start time
TIME-OBS 01:58:00.646185                                               str   [UTC] Observation start time
MJD-OBS  58549.082                                                     float Modified Julian Date of observation
ST       05:29:37.900                                                  str   Local Sidereal time at observation start (HH:MM
SPECGRPH SP0                                                           str   Spectrograph name **UNEXPECTED**: This is for *all* spectrographs, right?
DEVICES  SPECTCON0, SPECTCON2                                          str
CHECKSUM 1mWa3kUZ1kUa1kUY                                              str   HDU checksum updated 2019-03-07T02:13:54
DATASUM  1650618112'                                                   str   data unit checksum updated 2019-03-07T02:13:54 **TYPE**: Should be integer.
======== ============================================================= ===== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

======== ======== ===== ===================
Name     Type     Units Description
======== ======== ===== ===================
unit     int32          **UNEXPECTED**: Why is this not all-caps?
DATE-OBS char[26]       **WARNING**: Remove hyphen! Also, isn't this the same for all spectrographs?
TIME-OBS char[15]       **WARNING**: Remove hyphen! Also, isn't this the same for all spectrographs?
MJD-OBS  float32        **WARNING**: Remove hyphen! Also, isn't this the same for all spectrographs?
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


Notes and Examples
==================

Provenance
----------

* 2019-02-21: Revised based on headers from spectrograph functional verification files.
* 2019-04-03: Revised based on raw data files created from spectrograph functional verification files.

Problems
--------

Maybe not a real problem: In a previous version of this model, the CCD quadrants were labeled 1, 2, 3, 4;
now they are labeled A, B, C, D.

The compressed HDUs in the "sp0" files contain ``ZSIMPLE`` keyword.  This would
be appropriate in a compressed *primary* HDU but not in a compressed extension.
Make sure that the images are actually compressed *as extensions*, not as
individual images that are then shoved into an HDU.

In the SPECTCONS table, array-valued columns have been replaced with pointers.  We *know* the number
of spectrographs, why does the array length need to be variable.

Why are many duplicate keywords present in SPECTCONS?  Can't we just use INHERIT?

Does ``MJD-OBS`` save sufficient decimal precision to actually reconstruct ``DATE-OBS`` to microsecond precision?

I have noted problems with individual header keywords or table columns using these terms:

MISSING
    Listed in a previous version of this file, but are not present in the most recent ``desi`` file constructed
    from spectrograph functional verification test ``sp`` files.
UNEXPECTED
    These don't appear to be relevant to DESI.
TYPE
    Appears to have the wrong type.
WARNING
    Generated a warning message from ``fitsverify``.

Expected Changes
----------------

* Coordinate with ICS for header keywords (*e.g.* ``FLAVOR`` -> ``PROGRAM``).
* Update telemetry HDU.
* Spectrographs will be in arbitrary order in the file.
