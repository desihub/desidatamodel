=======
preproc
=======

:Summary: Pre-processed spectrograph CCD raw data.
:Naming Convention: ``preproc-{camera}-{expid}.fits``, where
    ``{camera}`` is the spectrograph camera (e.g. "b0", "r1", "z9"),
    and ``{expid}`` is the zero-padded 8-digit exposure ID.
:Regex: ``preproc-[brz][0-9]-[0-9]{8}.fits``
:File Type: FITS, 192 MB

Contents
========

====== ========= ======== ===================
Number EXTNAME   Type     Contents
====== ========= ======== ===================
HDU0_  IMAGE     IMAGE    *Brief Description*
HDU1_  IVAR      IMAGE    *Brief Description*
HDU2_  MASK      IMAGE    *Brief Description*
HDU3_  READNOISE IMAGE    *Brief Description*
HDU4_  FIBERMAP  BINTABLE *Brief Description*
====== ========= ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = IMAGE

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

=========== ============================================================ ===== ===============================================
KEY         Example Value                                                Type  Comment
=========== ============================================================ ===== ===============================================
NAXIS1      4096                                                         int
NAXIS2      4096                                                         int
OBSERVAT    KPNO                                                         str   Observatory name
OBS-LAT     31.96403                                                     str   [deg] Observatory latitude
OBS-LONG    -111.59989                                                   str   [deg] Observatory east longitude
OBS-ELEV    2097.0                                                       float [m] Observatory elevation
TELESCOP    KPNO 4.0-m telescope                                         str   Telescope name
INSTRUME    DESI                                                         str   Instrument name
CORRCTOR    DESI Corrector                                               str   Corrector Identification
PROCTYPE    RAW                                                          str   Data processing level
PRODTYPE    image                                                        str   Data product type
PROGRAM     SV tile 70508 M67)                                           str   Program name
OBSERVER    DESIObserver                                                 str   Names of observers
LEAD        RunManager                                                   str   Lead observer
PROPID      2019B-5000                                                   str   Proposal ID
TILEID      70508                                                        int   DESI Tile ID
EXPID       52086                                                        int   Exposure number
EXPFRAME    0                                                            int   Frame number
FILENAME    /exposures/desi/specs/20200225/00052086/sp7-00052086.fits.fz str   Name
FLAVOR      science                                                      str   Observation type
REQTIME     300.0                                                        float [s] Requested exposure time
EXPTIME     300.0                                                        float [s] Actual exposure time
OBSID       kp4m20200226t051718                                          str   Unique observation identifier
FOCUS       988.2,-287.4,1086.0,-14.1,13.9,177.8                         str   Telescope focus settings
TIMESYS     UTC                                                          str   Time system used for date-obs
RADESYS     FK5                                                          str   Coordinate reference frame of major/minor axes
EPOCH       2000.0                                                       float Epoch of observation
NIGHT       20200225                                                     str   Observing night
DATE-OBS    2020-02-26T05:17:18.893418                                   str   [UTC] Observation data and start time
TIME-OBS    05:17:18.893418                                              str   [UTC] Observation start time
MJD-OBS     58905.22035756                                               float Modified Julian Date of observation
ST          08:13:02.530                                                 str   Local Sidereal time at observation start (HH:MM
REQRA       133.4125                                                     float [deg] Requested right ascension (observer input
REQDEC      11.6818                                                      float [deg] Requested declination (observer input)
TARGTRA     133.414392                                                   float [deg] Target right ascension (to TCS)
TARGTDEC    11.677921                                                    float [deg] Target declination (to TCS)
SKYRA       133.414392                                                   float [deg] Telescope right ascension (pointing on sk
SKYDEC      11.677921                                                    float [deg] Telescope declination (pointing on sky)
SPECGRPH    0                                                            int   Spectrograph logical name (SP)
SPECID      4                                                            int   Spectrograph serial number (SM)
DETECTOR    sn22797                                                      str   Detector (ccd) identification
CAMERA      b0                                                           str   Camera name
CCDNAME     CCDSM4B                                                      str   CCD name
CCDPREP     purge,clear                                                  str   CCD prep actions
CCDSIZE     4162,4232                                                    str   CCD size in pixels (rows, columns)
CCDTEMP     850.0                                                        float [deg C] CCD controller CCD temperature
CPUTEMP     56.625                                                       float [deg C] CCD controller CPU temperature
CASETEMP    56.3689                                                      float [deg C] CCD controller case temperature
CCDTMING    default_sta_timing_20180905.txt                              str   CCD timing file
CCDCFG      default_sta_20190717.cfg                                     str   CCD configuration file
SETTINGS    detectors_sm_20191211.json                                   str   Name of DESI CCD settings file
VESSEL      15                                                           int   Cryostat serial number
FEEVER      v20160312                                                    str   CCD Controller version
FEEBOX      lbnl081                                                      str   CCD Controller serial number
PRESECA     [1:4, 2:2049]                                                str   Prescan section for quadrant A
PRRSECA     [5:2052, 1:1]                                                str   Row prescan section for quadrant A
DATASECA    [5:2052, 2:2049]                                             str   Data section for quadrant A
TRIMSECA    [5:2052, 2:2049]                                             str   Trim section for quadrant A
BIASSECA    [2053:2116, 2:2049]                                          str   Bias section for quadrant A
ORSECA      [5:2052, 2050:2081]                                          str   Row overscan section for quadrant A
CCDSECA     [1:2048, 1:2048]                                             str   CCD section for quadrant A
DETSECA     [1:2048, 1:2048]                                             str   Detector section for quadrant A
AMPSECA     [1:2048, 1:2048]                                             str   AMP section for quadrant A
PRESECB     [4229:4232, 2:2049]                                          str   Prescan section for quadrant B
PRRSECB     [2181:4228, 1:1]                                             str   Row prescan section for quadrant B
DATASECB    [2181:4228, 2:2049]                                          str   Data section for quadrant B
TRIMSECB    [2181:4228, 2:2049]                                          str   Trim section for quadrant B
BIASSECB    [2117:2180, 2:2049]                                          str   Bias section for quadrant B
ORSECB      [2181:4228, 2050:2081]                                       str   Row overscan section for quadrant B
CCDSECB     [2049:4096, 1:2048]                                          str   CCD section for quadrant B
DETSECB     [2049:4096, 1:2048]                                          str   Detector section for quadrant B
AMPSECB     [2049:4096, 2048:1]                                          str   AMP section for quadrant B
PRESECC     [1:4, 2114:4161]                                             str   Prescan section for quadrant C
PRRSECC     [5:2052, 4162:4162]                                          str   Row prescan section for quadrant C
DATASECC    [5:2052, 2114:4161]                                          str   Data section for quadrant C
TRIMSECC    [5:2052, 2114:4161]                                          str   Trim section for quadrant C
BIASSECC    [2053:2116, 2114:4161]                                       str   Bias section for quadrant C
ORSECC      [5:2052, 2082:2113]                                          str   Row overscan section for quadrant C
CCDSECC     [1:2048, 2049:4096]                                          str   CCD section for quadrant C
DETSECC     [1:2048, 2049:4096]                                          str   Detector section for quadrant C
AMPSECC     [2048:1, 2049:4096]                                          str   AMP section for quadrant C
PRESECD     [4229:4232, 2114:4161]                                       str   Prescan section for quadrant D
PRRSECD     [2181:4228, 4162:4162]                                       str   Row prescan section for quadrant D
DATASECD    [2181:4228, 2114:4161]                                       str   Data section for quadrant D
TRIMSECD    [2181:4228, 2114:4161]                                       str   Trim section for quadrant D
BIASSECD    [2117:2180, 2114:4161]                                       str   Bias section for quadrant D
ORSECD      [2181:4228, 2082:2113]                                       str   Row bias section for quadrant D
CCDSECD     [2049:4096, 2049:4096]                                       str   CCD section for quadrant D
DETSECD     [2049:4096, 2049:4096]                                       str   Detector section for quadrant D
AMPSECD     [4096:2049, 4096:2049]                                       str   AMP section for quadrant D
DAC0        15.9998,15.9547                                              str   [V] set value, measured value
DAC1        15.9998,15.8208                                              str   [V] set value, measured value
DAC2        15.9998,15.8311                                              str   [V] set value, measured value
DAC3        15.9998,15.965                                               str   [V] set value, measured value
DAC4        0.0,0.0053                                                   str   [V] set value, measured value
DAC5        0.0,0.0105                                                   str   [V] set value, measured value
DAC6        0.0,0.0158                                                   str   [V] set value, measured value
DAC7        0.0,0.0105                                                   str   [V] set value, measured value
DAC8        26.9998,26.5933                                              str   [V] set value, measured value
DAC9        26.9998,26.9198                                              str   [V] set value, measured value
DAC10       26.9998,26.801                                               str   [V] set value, measured value
DAC11       26.9998,26.8901                                              str   [V] set value, measured value
DAC12       4.9997,22.62                                                 str   [V] set value, measured value
DAC13       -5.0006,-4.9816                                              str   [V] set value, measured value
DAC14       0.0,0.8216                                                   str   [V] set value, measured value
DAC15       19.9997,20.0616                                              str   [V] set value, measured value
DAC16       0.0,65.9274                                                  str   [V] set value, measured value
DAC17       -0.0,0.0122                                                  str   [V] set value, measured value
CLOCK0      3.9999,-4.0002                                               str   [V] high rail, low rail
CLOCK1      3.9999,-4.0002                                               str   [V] high rail, low rail
CLOCK2      3.9999,-4.0002                                               str   [V] high rail, low rail
CLOCK3      6.9999,-2.0001                                               str   [V] high rail, low rail
CLOCK4      3.9999,-4.0002                                               str   [V] high rail, low rail
CLOCK5      3.9999,-4.0002                                               str   [V] high rail, low rail
CLOCK6      3.9999,-4.0002                                               str   [V] high rail, low rail
CLOCK7      6.9999,-2.0001                                               str   [V] high rail, low rail
CLOCK8      3.0,-7.0002                                                  str   [V] high rail, low rail
CLOCK9      3.0,-7.0002                                                  str   [V] high rail, low rail
CLOCK10     3.0,-7.0002                                                  str   [V] high rail, low rail
CLOCK11     0.0,0.0                                                      str   [V] high rail, low rail
CLOCK12     3.0,-7.0002                                                  str   [V] high rail, low rail
CLOCK13     3.0,-7.0002                                                  str   [V] high rail, low rail
CLOCK14     3.0,-7.0002                                                  str   [V] high rail, low rail
CLOCK15     0.0,0.0                                                      str   [V] high rail, low rail
CLOCK16     0.0,0.0                                                      str   [V] high rail, low rail
CLOCK17     3.9999,-4.0002                                               str   [V] high rail, low rail
CLOCK18     3.9999,-4.0002                                               str   [V] high rail, low rail
OFFSET0     -1.5,15.965                                                  str   [V] set value, measured value
OFFSET1     -1.5,15.8208                                                 str   [V] set value, measured value
OFFSET2     -1.5,15.8208                                                 str   [V] set value, measured value
OFFSET3     -1.5,15.965                                                  str   [V] set value, measured value
OFFSET4     -1.100000023841858,0.0053                                    str   [V] set value, measured value
OFFSET5     -1.100000023841858,0.0158                                    str   [V] set value, measured value
OFFSET6     -1.100000023841858,0.0158                                    str   [V] set value, measured value
OFFSET7     -1.100000023841858,0.0158                                    str   [V] set value, measured value
DELAYS      13, 13, 25, 25, 8, 3000, 7, 7, 7, 7                          str   [10] Delay settings
CDSPARMS    400, 400, 8, 1000                                            str   CDS parameters
PGAGAIN     5                                                            int   Controller gain
OCSVER      1.2                                                          float OCS software version
DOSVER      trunk                                                        str   DOS software version
CONSTVER    DESI:CURRENT                                                 str   Constants version
BLDTIME     0.373                                                        float [s] Time to build image
DIGITIME    46.0944                                                      float [s] Time to digitize image
FIBERASSIGN /data/tiles/ALL_tiles/20191119/fiberassign-070508.fits       str
INIFILE     /data/msdos/dos_home/architectures/kpno/desi-2.ini           str
CHECKSUM    52kOA1jM51jMA1jM                                             str   HDU checksum updated 2020-04-23T14:17:54
DATASUM     1225190409                                                   str   data unit checksum updated 2020-04-23T14:17:54
OVERSCNA    1198.409442756195                                            float ADUs (gain not applied)
OBSRDNA     4.123114028338187                                            float electrons (gain is applied)
GAINA       1.133                                                        float e/ADU (gain applied to image)
OVERSCNB    1197.717050163806                                            float ADUs (gain not applied)
OBSRDNB     3.31066884511514                                             float electrons (gain is applied)
GAINB       1.117                                                        float e/ADU (gain applied to image)
OVERSCNC    1189.826305034543                                            float ADUs (gain not applied)
OBSRDNC     3.708568138334658                                            float electrons (gain is applied)
GAINC       1.122                                                        float e/ADU (gain applied to image)
OVERSCND    1180.445786398657                                            float ADUs (gain not applied)
OBSRDND     4.273139196431343                                            float electrons (gain is applied)
GAIND       1.122                                                        float e/ADU (gain applied to image)
TILERA      133.4125                                                     float
TILEDEC     11.6818                                                      float
=========== ============================================================ ===== ===============================================

Data: FITS image [float32, 4096x4096]

HDU1
----

EXTNAME = IVAR

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   4096             int
NAXIS2   4096             int
CHECKSUM AMS3DMQ1AMQ1AMQ1 str  HDU checksum updated 2020-04-23T14:17:55
DATASUM  3408402573       str  data unit checksum updated 2020-04-23T14:17:55
======== ================ ==== ==============================================

Data: FITS image [float32, 4096x4096]

HDU2
----

EXTNAME = MASK

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   8                int  width of table in bytes
NAXIS2   4096             int  number of rows in table
CHECKSUM 923dH22a922aE22a str  HDU checksum updated 2020-04-23T14:17:56
DATASUM  2257839383       str  data unit checksum updated 2020-04-23T14:17:56
======== ================ ==== ==============================================

Data: FITS image [int16 (compressed), 4096x4096]

HDU3
----

EXTNAME = READNOISE

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   4096             int
NAXIS2   4096             int
CHECKSUM icXSlbXQibXQibXQ str  HDU checksum updated 2020-04-23T14:17:56
DATASUM  1272477592       str  data unit checksum updated 2020-04-23T14:17:56
======== ================ ==== ==============================================

Data: FITS image [float32, 4096x4096]

HDU4
----

EXTNAME = FIBERMAP

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================================================================== ===== ==============================================
KEY      Example Value                                                      Type  Comment
======== ================================================================== ===== ==============================================
NAXIS1   571                                                                int   length of dimension 1
NAXIS2   500                                                                int   length of dimension 2
FA_PLAN  2022-07-01T00:00:00.000                                            str
FIELDNUM 0                                                                  int
TILEDEC  11.6818                                                            float
FA_VER   1.3.0.dev2495                                                      str
FA_SURV  cmx                                                                str
FIELDROT 0.0924696831285645                                                 float
TILERA   133.4125                                                           float
REQDEC   11.6818                                                            float
FA_HA    0.0                                                                float
REQRA    133.4125                                                           float
FA_RUN   2019-09-16T00:00:00                                                str
TILEID   70508                                                              int
OBSERVAT KPNO                                                               str
OBS-LAT  31.96403                                                           str
OBS-LONG -111.59989                                                         str
OBS-ELEV 2097.0                                                             float
TELESCOP KPNO 4.0-m telescope                                               str
INSTRUME DESI                                                               str
CORRCTOR DESI Corrector                                                     str
PROGRAM  SV tile 70508 M67)                                                 str
OBSERVER DESIObserver                                                       str
LEAD     RunManager                                                         str
PROPID   2019B-5000                                                         str
MANIFEST F                                                                  bool
EXPID    52086                                                              int
FRAMES   47                                                                 int
SEQUENCE DESI                                                               str
SEQNUM   1                                                                  int
FLAVOR   science                                                            str
OBSTYPE  SCIENCE                                                            str
REQTIME  300.0                                                              float
EXPTIME  15.0                                                               float
OBJECT                                                                      str
CAMSHUT  open                                                               str
FIDUCIAL off                                                                str
FOCUS    988.2,-287.4,1085.9,-14.1,14.0,0.1                                 str
ACQTIME  15.0                                                               float
GUIDTIME 5.0                                                                float
TIMESYS  UTC                                                                str
RADESYS  FK5                                                                str
EPOCH    2000.0                                                             float
NIGHT    20200225                                                           int
DATE-OBS 2020-02-26T05:13:22.725627                                         str
MJD-OBS  58905.21762414                                                     float
ST       08:09:05.720                                                       str
TARGTRA  133.414392                                                         float
TARGTDEC 11.67792                                                           float
TARGTEL  67.261576                                                          float
TARGTAZ  150.646923                                                         float
TRGTOFFD 0.0                                                                float
TRGTOFFR 0.0                                                                float
SKYRA    133.414392                                                         float
SKYDEC   11.67792                                                           float
ZD       22.738424                                                          float
MOUNTHA  -11.15567                                                          float
MOUNTAZ  150.646923                                                         float
MOUNTEL  67.261576                                                          float
MOUNTDEC 11.67792                                                           float
INCTRL   T                                                                  bool
INPOS    T                                                                  bool
WHITESPT F                                                                  bool
ZENITH   F                                                                  bool
SEANNEX  F                                                                  bool
BEYONDP  F                                                                  bool
PMREADY  T                                                                  bool
PMCOVER  open                                                               str
MNTOFFD  -0.0                                                               float
MNTOFFR  -0.0                                                               float
PARALLAC -25.12922                                                          float
DOMEAZ   154.557                                                            float
DOMINPOS T                                                                  bool
DOMSHUTU open                                                               str
DOMSHUTL not open                                                           str
DOMLIGHH off                                                                str
DOMLIGHL off                                                                str
TCSKRA   0.15 0.003 0.00003                                                 str
TCSKDEC  0.15 0.003 0.00003                                                 str
TCSGRA   0.3                                                                float
TCSGDEC  0.3                                                                float
TCSMFRA  1                                                                  int
TCSMFDEC 1                                                                  int
TCSPIRA  1.0,0.0,0.0,0.0                                                    str
TCSPIDEC 1.0,1.0,0.0,0.0                                                    str
GUIDOFFR 0.0                                                                float
GUIDOFFD -0.0                                                               float
AIRMASS  1.084097                                                           float
SPCGRPHS SP0,SP1,SP4,SP5,SP6,SP7,SP8,SP9,SP3                                str
TNFSPROC 19.7625                                                            float
MOONRA   6.494978                                                           float
MOONDEC  -2.692424                                                          float
GUIDMODE catalog                                                            str
AOS      F                                                                  bool
TCSST    08:09:02.093                                                       str
TCSMJD   58905.21802                                                        float
TDEWPNT  -10.96                                                             float
TAIRFLOW 0.0                                                                float
TAIRITMP 7.3                                                                float
TAIROTMP 7.6                                                                float
TAIRTEMP 0.518                                                              float
TCASITMP 10.6                                                               float
TCASOTMP 3.4                                                                float
TCSITEMP 3.1                                                                float
TCSOTEMP 2.4                                                                float
TCIBTEMP 21.6                                                               float
TCIMTEMP 21.6                                                               float
TCITTEMP 21.7                                                               float
TCOSTEMP 21.7                                                               float
TCOWTEMP 21.6                                                               float
TDBTEMP  4.4                                                                float
TFLOWIN  0.0                                                                float
TFLOWOUT 0.0                                                                float
TGLYCOLI 6.7                                                                float
TGLYCOLO 6.9                                                                float
THINGES  1.7                                                                float
THINGEW  3.8                                                                float
TPMAVERT 3.605                                                              float
TPMDESIT 3.0                                                                float
TPMEIBT  4.4                                                                float
TPMEITT  3.5                                                                float
TPMEOBT  4.8                                                                float
TPMEOTT  3.7                                                                float
TPMNIBT  4.4                                                                float
TPMNITT  3.5                                                                float
TPMNOBT  4.6                                                                float
TPMNOTT  3.8                                                                float
TPMRTDT  -99.9                                                              float
TPMSIBT  4.3                                                                float
TPMSITT  3.5                                                                float
TPMSOBT  4.7                                                                float
TPMSOTT  3.7                                                                float
TPMSTAT  ready                                                              str
TPMWIBT  4.4                                                                float
TPMWITT  3.3                                                                float
TPMWOBT  4.6                                                                float
TPMWOTT  3.6                                                                float
TPCITEMP 3.9                                                                float
TPCOTEMP 3.7                                                                float
TPR1HUM  -100.0                                                             float
TPR1TEMP -100.0                                                             float
TPR2HUM  -99.99                                                             float
TPR2TEMP -99.99                                                             float
TSERVO   40.0                                                               float
TTRSTEMP 1.0                                                                float
TTRWTEMP 0.4                                                                float
TTRUETBT 2.4                                                                float
TTRUETTT 2.6                                                                float
TTRUNTBT 2.2                                                                float
TTRUNTTT 2.3                                                                float
TTRUSTBT 2.4                                                                float
TTRUSTST 2.9                                                                float
TTRUSTTT 1.7                                                                float
TTRUTSBT 1.9                                                                float
TTRUTSMT 1.7                                                                float
TTRUTSTT 1.9                                                                float
TTRUWTBT 2.3                                                                float
TTRUWTTT 2.3                                                                float
TRUSTEMP 1.833                                                              float
PMIRTEMP 3.575                                                              float
ALARM    F                                                                  bool
ALARM-ON F                                                                  bool
BATTERY  100.0                                                              float
SECLEFT  4782.0                                                             float
UPSSTAT  System Normal - On Line(7)                                         str
INAMPS   82.6                                                               float
OUTWATTS 5700.0,8300.0,7500.0                                               str
COMPDEW  -8.8                                                               float
COMPHUM  14.5                                                               float
COMPAMB  17.2                                                               float
COMPTEMP 18.9                                                               float
DEWPOINT -17.8                                                              float
GUST     117.6                                                              float
HUMIDITY 26.6                                                               float
PRESSURE 793.5                                                              float
OUTTEMP  -0.9                                                               float
WINDDIR  30.3                                                               float
WINDSPD  38.1                                                               float
CFLOOR   3.8                                                                float
NWALLIN  11.3                                                               float
NWALLOUT 1.4                                                                float
WWALLIN  10.7                                                               float
WWALLOUT 2.3                                                                float
AMNIENTN 10.6                                                               float
AMBIENTS 12.5                                                               float
FLOOR    11.2                                                               float
EWALLCMP 2.9                                                                float
EWALLCOU 2.4                                                                float
ROOF     1.4                                                                float
ROOFAMB  0.5                                                                float
DOMEBLOW 0.4                                                                float
DOMEBUP  0.5                                                                float
DOMELLOW -0.1                                                               float
DOMELUP  -0.4                                                               float
DOMERLOW 0.1                                                                float
DOMERUP  -0.3                                                               float
PLATFORM -0.6                                                               float
SHACKC   12.4                                                               float
SHACKW   10.8                                                               float
STAIRSL  0.1                                                                float
STAIRSM  0.3                                                                float
STAIRSU  0.2                                                                float
TELBASE  3.9                                                                float
UTILWALL 2.3                                                                float
UTILROOM 1.6                                                                float
GUIDECAM GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                          str
ACQCAM   GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                          str
MODULE   GUIDE                                                              str
REQADC   321.92,347.51                                                      str
ADC1PHI  321.919733                                                         float
ADC2PHI  347.509849                                                         float
ADC1HOME F                                                                  bool
ADC2HOME F                                                                  bool
ADC1NREV 0.0                                                                float
ADC2NREV -1.0                                                               float
ADC1STAT STOPPED                                                            str
ADC2STAT STOPPED                                                            str
ADCCORR  T                                                                  bool
HEXPOS   988.2,-287.4,1085.9,-14.1,14.0,0.1                                 str
HEXTRIM  0.0,0.0,-200.0,0.0,0.0,0.0                                         str
ROTOFFST 173.5                                                              float
ROTENBLD T                                                                  bool
ROTRATE  0.478                                                              float
EXCLUDED                                                                    str
OCSVER   1.2                                                                float
DOSVER   trunk                                                              str
CONSTVER DESI:CURRENT                                                       str
USESPCTR T                                                                  bool
USEGUIDR T                                                                  bool
USEFVC   T                                                                  bool
USEFID   T                                                                  bool
USEETC   F                                                                  bool
USESKY   F                                                                  bool
USEFOCUS F                                                                  bool
USEDONUT F                                                                  bool
USEXSRVR T                                                                  bool
USEROTAT T                                                                  bool
USEILLUM T                                                                  bool
USEPOS   T                                                                  bool
SIMGFAP  F                                                                  bool
USEOPENL T                                                                  bool
RESETROT T                                                                  bool
STOPGUDR T                                                                  bool
STOPFOCS T                                                                  bool
STOPSKY  T                                                                  bool
KEEPGUDR T                                                                  bool
KEEPFOCS T                                                                  bool
KEEPSKY  T                                                                  bool
REACQUIR F                                                                  bool
INIFILE  /data/msdos/dos_home/architectures/kpno/desi-2.ini                 str
OPENSHUT 2020-02-26T05:13:22.725627                                         str
GSGUIDE0 (779.90,1278.98),(505.15,343.34)                                   str
GSGUIDE2 (728.51,1133.84),(774.31,1321.27)                                  str
GSGUIDE3 (946.72,158.97),(812.51,1595.79),(247.07,1414.84),(680.94,127.18)  str
GSGUIDE5 (236.33,1387.60),(788.40,377.01),(871.06,1022.95),(609.16,730.56)  str
GSGUIDE7 (142.92,1507.64),(319.93,1590.40),(319.93,1590.40),(497.74,737.50) str
GSGUIDE8 (159.02,903.23),(620.43,589.44),(371.58,1877.52)                   str
ARCHIVE  /exposures/desi/20200225/00052086/guide-00052086.fits.fz           str
GUIDEFIL guide-00052086.fits.fz                                             str
COORDFIL coordinates-00052086.fits                                          str
CHECKSUM bqI9co99boG9bo99                                                   str   HDU checksum updated 2020-04-23T14:17:56
DATASUM  184768983                                                          str   data unit checksum updated 2020-04-23T14:17:56
======== ================================================================== ===== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

================================= ======= ===== ===========
Name                              Type    Units Description
================================= ======= ===== ===========
TARGETID                          int64
PETAL_LOC                         int16
DEVICE_LOC                        int32
LOCATION                          int64
FIBER                             int32
FIBERSTATUS                       int32
TARGET_RA                         float64
TARGET_DEC                        float64
PMRA                              float32
PMDEC                             float32
PMRA_IVAR                         float32
PMDEC_IVAR                        float32
REF_EPOCH                         float32
LAMBDA_REF                        float32
FA_TARGET                         int64
FA_TYPE                           binary
OBJTYPE                           char[3]
FIBERASSIGN_X                     float32
FIBERASSIGN_Y                     float32
NUMTARGET                         int16
PRIORITY                          int32
SUBPRIORITY                       float64
OBSCONDITIONS                     int32
NUMOBS_MORE                       int32
RELEASE                           int16
BRICKID                           int32
BRICKNAME                         char[8]
BRICK_OBJID                       int32
MORPHTYPE                         char[4]
TARGET_RA_IVAR                    float32
TARGET_DEC_IVAR                   float32
EBV                               float32
FLUX_G                            float32
FLUX_R                            float32
FLUX_Z                            float32
FLUX_IVAR_G                       float32
FLUX_IVAR_R                       float32
FLUX_IVAR_Z                       float32
MW_TRANSMISSION_G                 float32
MW_TRANSMISSION_R                 float32
MW_TRANSMISSION_Z                 float32
FRACFLUX_G                        float32
FRACFLUX_R                        float32
FRACFLUX_Z                        float32
FRACMASKED_G                      float32
FRACMASKED_R                      float32
FRACMASKED_Z                      float32
FRACIN_G                          float32
FRACIN_R                          float32
FRACIN_Z                          float32
NOBS_G                            int16
NOBS_R                            int16
NOBS_Z                            int16
PSFDEPTH_G                        float32
PSFDEPTH_R                        float32
PSFDEPTH_Z                        float32
GALDEPTH_G                        float32
GALDEPTH_R                        float32
GALDEPTH_Z                        float32
FLUX_W1                           float32
FLUX_W2                           float32
FLUX_W3                           float32
FLUX_W4                           float32
FLUX_IVAR_W1                      float32
FLUX_IVAR_W2                      float32
FLUX_IVAR_W3                      float32
FLUX_IVAR_W4                      float32
MW_TRANSMISSION_W1                float32
MW_TRANSMISSION_W2                float32
MW_TRANSMISSION_W3                float32
MW_TRANSMISSION_W4                float32
ALLMASK_G                         int16
ALLMASK_R                         int16
ALLMASK_Z                         int16
FIBERFLUX_G                       float32
FIBERFLUX_R                       float32
FIBERFLUX_Z                       float32
FIBERTOTFLUX_G                    float32
FIBERTOTFLUX_R                    float32
FIBERTOTFLUX_Z                    float32
WISEMASK_W1                       binary
WISEMASK_W2                       binary
MASKBITS                          int16
FRACDEV                           float32
FRACDEV_IVAR                      float32
SHAPEDEV_R                        float32
SHAPEDEV_E1                       float32
SHAPEDEV_E2                       float32
SHAPEDEV_R_IVAR                   float32
SHAPEDEV_E1_IVAR                  float32
SHAPEDEV_E2_IVAR                  float32
SHAPEEXP_R                        float32
SHAPEEXP_E1                       float32
SHAPEEXP_E2                       float32
SHAPEEXP_R_IVAR                   float32
SHAPEEXP_E1_IVAR                  float32
SHAPEEXP_E2_IVAR                  float32
REF_ID                            int64
REF_CAT                           char[2]
GAIA_PHOT_G_MEAN_MAG              float32
GAIA_PHOT_G_MEAN_FLUX_OVER_ERROR  float32
GAIA_PHOT_BP_MEAN_MAG             float32
GAIA_PHOT_BP_MEAN_FLUX_OVER_ERROR float32
GAIA_PHOT_RP_MEAN_MAG             float32
GAIA_PHOT_RP_MEAN_FLUX_OVER_ERROR float32
GAIA_PHOT_BP_RP_EXCESS_FACTOR     float32
GAIA_ASTROMETRIC_EXCESS_NOISE     float32
GAIA_DUPLICATED_SOURCE            logical
GAIA_ASTROMETRIC_SIGMA5D_MAX      float32
GAIA_ASTROMETRIC_PARAMS_SOLVED    logical
PARALLAX                          float32
PARALLAX_IVAR                     float32
PHOTSYS                           char[1]
CMX_TARGET                        int64
PRIORITY_INIT                     int64
NUMOBS_INIT                       int64
HPXPIXEL                          int64
BLOBDIST                          float32
FIBERFLUX_IVAR_G                  float32
FIBERFLUX_IVAR_R                  float32
FIBERFLUX_IVAR_Z                  float32
DESI_TARGET                       int64
BGS_TARGET                        int64
MWS_TARGET                        int64
NUM_ITER                          int64
FIBER_X                           float64
FIBER_Y                           float64
DELTA_X                           float64
DELTA_Y                           float64
FIBER_RA                          float64
FIBER_DEC                         float64
================================= ======= ===== ===========


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
