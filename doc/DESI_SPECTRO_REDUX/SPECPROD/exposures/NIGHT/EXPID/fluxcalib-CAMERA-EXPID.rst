===========================
fluxcalib-CAMERA-EXPID.fits
===========================

:Summary: This holds the flux calibration model for a given camera and exposure.
:Naming Convention: ``fluxcalib-{CAMERA}-{EXPID}.fits``, where ``{CAMERA}`` is
    one of the spectrograph cameras (*e.g.* ``z1``) and ``{EXPID}``
    is the 8-digit exposure ID.
:Regex: ``fluxcalib-[brz][0-9]-[0-9]{8}\.fits``
:File Type: FITS, 13 MB

Contents
========

====== ========== ======== ===================
Number EXTNAME    Type     Contents
====== ========== ======== ===================
HDU0_  FLUXCALIB  IMAGE    Flux calibration model
HDU1_  IVAR       IMAGE    Inverse variance of flux
HDU2_  MASK       IMAGE    Mask (0 = good)
HDU3_  WAVELENGTH IMAGE    wavelength in Angstrom
HDU4_  FIBERCORR  BINTABLE *Brief Description*
====== ========== ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = FLUXCALIB

Flux calibration model such that calibrated flux = uncalibrated photons / model.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============================================================== ======= ===============================================
KEY      Example Value                                                  Type    Comment
======== ============================================================== ======= ===============================================
NAXIS1   2326                                                           int
NAXIS2   500                                                            int
EXPID    71111                                                          int     Exposure number
EXPFRAME 0                                                              int     Frame number
TILEID   80674                                                          int     DESI Tile ID
FIBASSGN /data/tiles/SVN_tiles/080/fiberassign-080674.fits.gz           str     Fiber assign
FLAVOR   science                                                        str     Observation type
SEQUENCE DESI                                                           str     OCS Sequence name
PURPOSE  Commissioning                                                  str     Purpose of observing night
PROGRAM  SV1 LRG+QSO                                                    str     Program name
PROPID   2019B-5000                                                     str     Proposal ID
OBSERVER DESIObserver                                                   str     Names of observers
LEAD     RunManager                                                     str     Lead observer
INSTRUME DESI                                                           str     Instrument name
OBSERVAT KPNO                                                           str     Observatory name
OBS-LAT  31.96403                                                       str     [deg] Observatory latitude
OBS-LONG -111.59989                                                     str     [deg] Observatory east longitude
OBS-ELEV 2097.0                                                         float   [m] Observatory elevation
TELESCOP KPNO 4.0-m telescope                                           str     Telescope name
CORRCTOR DESI Corrector                                                 str     Corrector Identification
NIGHT    20210106                                                       int     Observing night
TIMESYS  UTC                                                            str     Time system used for date-obs
DATE-OBS 2021-01-07T07:05:48.566533888                                  str     [UTC] Observation data and start tim
TIME-OBS 2021-01-07T07:05:48.566533888                                  str     [UTC] Observation start time
MJD-OBS  59221.295701                                                   float   Modified Julian Date of observation
ST       06:47:41.380000                                                str     Local Sidereal time at observation start (HH:MM
EXPTIME  900.028                                                        float   [s] Actual exposure time
REQRA    87.0                                                           float   [deg] Requested right ascension (observer input
REQDEC   -23.2                                                          float   [deg] Requested declination (observer input)
VCCD     ON                                                             str     True (ON) if CCD voltage is on
VCCDON   2020-12-14T02:10:11.025061                                     str     Time when CCD voltage was turned on
VCCDSEC  2092287.4                                                      float   [s] CCD on time in seconds
EPOCH    2000.0                                                         float   Epoch of observation
USEETC   F                                                              bool    ETC data available if true
USESKY   T                                                              bool    DOS Control: use Sky Monitor
USEFOCUS T                                                              bool    DOS Control: use focus
USEROTAT T                                                              bool    DOS Control: use rotator
USEGUIDR T                                                              bool    DOS Control: use guider
USEDONUT T                                                              bool    DOS Control: use donuts
SPECGRPH 2                                                              int     Spectrograph logical name (SP)
SPECID   5                                                              int     Spectrograph serial number (SM)
FEEBOX   lbnl051                                                        str     CCD Controller serial number
VESSEL   10                                                             int     Cryostat serial number
FEEVER   v20160312                                                      str     CCD Controller version
FEEPOWER ON                                                             str     FEE power status
FEEDMASK 2134851391                                                     int     FEE dac mask
FEECMASK 1048575                                                        int     FEE clk mask
CCDTEMP  -136.7276                                                      float   [deg C] CCD controller CCD temperature
RADESYS  FK5                                                            str     Coordinate reference frame of major/minor axes
DOSVER   trunk                                                          str     DOS software version
OCSVER   1.2                                                            float   OCS software version
CONSTVER DESI:CURRENT                                                   str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi_nopetal3.ini      str     DOS Conf
PRESECA  [1:7, 2:2065]                                                  str     Prescan section for quadrant A
PRESECC  [1:7, 2130:4193]                                               str     Prescan section for quadrant C
OFFSET3  0.4000000059604645,-8.961                                      str     [V] set value, measured value
DAC2     -9.0002,-9.0537                                                str     [V] set value, measured value
CCDSECD  [2058:4114, 2065:4128]                                         str     CCD section for quadrant D
DAC16    39.9961,39.0852                                                str     [V] set value, measured value
OFFSET4  2.0,5.9806                                                     str     [V] set value, measured value
OFFSET6  2.0,6.0174                                                     str     [V] set value, measured value
TRIMSECA [8:2064, 2:2065]                                               str     Trim section for quadrant A
OFFSET2  0.4000000059604645,-9.0537                                     str     [V] set value, measured value
DELAYS   20, 20, 25, 40, 7, 3000, 7, 7, 7, 7                            str     [10] Delay settings
CLOCK6   9.9999,0.0                                                     str     [V] high rail, low rail
CLOCK1   9.9999,0.0                                                     str     [V] high rail, low rail
DAC0     -9.0002,-9.0331                                                str     [V] set value, measured value
CLOCK5   9.9999,0.0                                                     str     [V] high rail, low rail
PGAGAIN  3                                                              int     Controller gain
DAC4     5.9998,5.9806                                                  str     [V] set value, measured value
CLOCK14  9.9992,2.9993                                                  str     [V] high rail, low rail
ORSECD   [2193:4249, 2098:2129]                                         str     Row bias section for quadrant D
CLOCK10  9.9992,2.9993                                                  str     [V] high rail, low rail
CASETEMP 58.0915                                                        float   [deg C] CCD controller case temperature
CLOCK2   9.9999,0.0                                                     str     [V] high rail, low rail
CLOCK0   9.9999,0.0                                                     str     [V] high rail, low rail
CLOCK16  9.9999,3.0                                                     str     [V] high rail, low rail
CLOCK17  9.0,0.9999                                                     str     [V] high rail, low rail
AMPSECD  [4114:2058, 4128:2065]                                         str     AMP section for quadrant D
DAC17    20.0008,12.0292                                                str     [V] set value, measured value
DAC15    0.0,-0.0297                                                    str     [V] set value, measured value
CDSPARMS 400, 400, 8, 2000                                              str     CDS parameters
DAC9     -25.0003,-25.0499                                              str     [V] set value, measured value
CCDSECA  [1:2057, 1:2064]                                               str     CCD section for quadrant A
DATASECD [2193:4249, 2130:4193]                                         str     Data section for quadrant D
DETSECB  [2058:4114, 1:2064]                                            str     Detector section for quadrant B
DAC12    0.0,-0.0148                                                    str     [V] set value, measured value
DETSECD  [2058:4114, 2065:4128]                                         str     Detector section for quadrant D
DATASECA [8:2064, 2:2065]                                               str     Data section for quadrant A
DAC6     5.9998,6.0174                                                  str     [V] set value, measured value
PRRSECC  [8:2064, 4194:4194]                                            str     Row prescan section for quadrant C
DAC5     5.9998,6.0069                                                  str     [V] set value, measured value
BIASSECC [2065:2128, 2130:4193]                                         str     Bias section for quadrant C
OFFSET5  2.0,6.0069                                                     str     [V] set value, measured value
CCDSIZE  4194,4256                                                      str     CCD size in pixels (rows, columns)
CLOCK12  9.9992,2.9993                                                  str     [V] high rail, low rail
DATASECC [8:2064, 2130:4193]                                            str     Data section for quadrant C
CCDNAME  CCDSM5R                                                        str     CCD name
BIASSECA [2065:2128, 2:2065]                                            str     Bias section for quadrant A
DAC14    0.0,-0.0148                                                    str     [V] set value, measured value
TRIMSECC [8:2064, 2130:4193]                                            str     Trim section for quadrant C
CLOCK7   -2.0001,3.9999                                                 str     [V] high rail, low rail
DETSECC  [1:2057, 2065:4128]                                            str     Detector section for quadrant C
CAMERA   r2                                                             str     Camera name
BIASSECB [2129:2192, 2:2065]                                            str     Bias section for quadrant B
DAC10    -25.0003,-25.228                                               str     [V] set value, measured value
OFFSET1  0.4000000059604645,-8.9713                                     str     [V] set value, measured value
CPUTEMP  57.4863                                                        float   [deg C] CCD controller CPU temperature
CCDPREP  purge,clear                                                    str     CCD prep actions
CLOCK15  9.9992,2.9993                                                  str     [V] high rail, low rail
DIGITIME 47.5282                                                        float   [s] Time to digitize image
AMPSECC  [1:2057, 4128:2065]                                            str     AMP section for quadrant C
CLOCK4   9.9999,0.0                                                     str     [V] high rail, low rail
SETTINGS detectors_sm_20201113.json                                     str     Name of DESI CCD settings file
CCDCFG   default_lbnl_20190717.cfg                                      str     CCD configuration file
DAC8     -25.0003,-24.9312                                              str     [V] set value, measured value
DATASECB [2193:4249, 2:2065]                                            str     Data section for quadrant B
ORSECA   [8:2064, 2066:2097]                                            str     Row overscan section for quadrant A
BLDTIME  0.3509                                                         float   [s] Time to build image
CLOCK3   -2.0001,3.9999                                                 str     [V] high rail, low rail
CLOCK11  9.9992,2.9993                                                  str     [V] high rail, low rail
CCDSECC  [1:2057, 2065:4128]                                            str     CCD section for quadrant C
CCDTMING default_lbnl_timing_20180905.txt                               str     CCD timing file
TRIMSECD [2193:4249, 2130:4193]                                         str     Trim section for quadrant D
ORSECB   [2193:4249, 2066:2097]                                         str     Row overscan section for quadrant B
TRIMSECB [2193:4249, 2:2065]                                            str     Trim section for quadrant B
AMPSECA  [1:2057, 1:2064]                                               str     AMP section for quadrant A
PRESECD  [4250:4256, 2130:4193]                                         str     Prescan section for quadrant D
PRRSECA  [8:2064, 1:1]                                                  str     Row prescan section for quadrant A
PRRSECB  [2193:4249, 1:1]                                               str     Row prescan section for quadrant B
DAC1     -9.0002,-8.9713                                                str     [V] set value, measured value
CLOCK13  9.9992,2.9993                                                  str     [V] high rail, low rail
ORSECC   [8:2064, 2098:2129]                                            str     Row overscan section for quadrant C
CRYOPRES 7.913e-08                                                      str     [mb] Cryostat pressure (IP)
DETSECA  [1:2057, 1:2064]                                               str     Detector section for quadrant A
CRYOTEMP 163.044                                                        float   [deg K] Cryostat CCD temperature
DAC3     -9.0002,-8.9713                                                str     [V] set value, measured value
DETECTOR M1-28                                                          str     Detector (ccd) identification
CCDSECB  [2058:4114, 1:2064]                                            str     CCD section for quadrant B
PRRSECD  [2193:4249, 4194:4194]                                         str     Row prescan section for quadrant D
AMPSECB  [4114:2058, 1:2064]                                            str     AMP section for quadrant B
DAC11    -25.0003,-24.575                                               str     [V] set value, measured value
OFFSET0  0.4000000059604645,-9.0331                                     str     [V] set value, measured value
DAC7     5.9998,6.0069                                                  str     [V] set value, measured value
PRESECB  [4250:4256, 2:2065]                                            str     Prescan section for quadrant B
DAC13    0.0,-0.0445                                                    str     [V] set value, measured value
CLOCK9   9.9992,2.9993                                                  str     [V] high rail, low rail
OFFSET7  2.0,6.0122                                                     str     [V] set value, measured value
CLOCK18  9.0,0.9999                                                     str     [V] high rail, low rail
BIASSECD [2129:2192, 2130:4193]                                         str     Bias section for quadrant D
CLOCK8   9.9992,2.9993                                                  str     [V] high rail, low rail
REQTIME  900.0                                                          float   [s] Requested exposure time
OBSID    kp4m20210107t070548                                            str     Unique observation identifier
PROCTYPE RAW                                                            str     Data processing level
PRODTYPE image                                                          str     Data product type
CHECKSUM 9oLhIlIg9lIgGlIg                                               str     HDU checksum updated 2021-07-08T16:29:43
DATASUM  3868609569                                                     str     data unit checksum updated 2021-07-08T16:29:43
GAINA    1.653                                                          float   e/ADU (gain applied to image)
SATULEVA 65535.0                                                        float   saturation or non lin. level, in ADU, inc. bias
OVERSCNA 1915.308411250455                                              float   ADUs (gain not applied)
OBSRDNA  2.678536350537513                                              float   electrons (gain is applied)
SATUELEA 105163.350196203                                               float   saturation or non lin. level, in electrons
GAINB    1.594                                                          float   e/ADU (gain applied to image)
SATULEVB 65535.0                                                        float   saturation or non lin. level, in ADU, inc. bias
OVERSCNB 1948.220166541344                                              float   ADUs (gain not applied)
OBSRDNB  4.455614504287378                                              float   electrons (gain is applied)
SATUELEB 101357.3270545331                                              float   saturation or non lin. level, in electrons
GAINC    1.509                                                          float   e/ADU (gain applied to image)
SATULEVC 65535.0                                                        float   saturation or non lin. level, in ADU, inc. bias
OVERSCNC 1911.363014193147                                              float   ADUs (gain not applied)
OBSRDNC  2.445932073934072                                              float   electrons (gain is applied)
SATUELEC 96008.06821158253                                              float   saturation or non lin. level, in electrons
GAIND    1.47                                                           float   e/ADU (gain applied to image)
SATULEVD 65535.0                                                        float   saturation or non lin. level, in ADU, inc. bias
OVERSCND 1963.037798019037                                              float   ADUs (gain not applied)
OBSRDND  2.457774458163971                                              float   electrons (gain is applied)
SATUELED 93450.78443691201                                              float   saturation or non lin. level, in electrons
FIBERMIN 1000                                                           int
MODULE   CI                                                             str
FRAMES   None                                                           Unknown
COSMSPLT F                                                              bool
MAXSPLIT 0                                                              int
SPLITIDS 71111                                                          str
OBSTYPE  SCIENCE                                                        str
MANIFEST F                                                              bool
OBJECT                                                                  str
SEQNUM   1                                                              int
OPENSHUT None                                                           Unknown
CAMSHUT  open                                                           str
ACQTIME  15                                                             int
GUIDTIME 5.0                                                            float
FOCSTIME 60.0                                                           float
SKYTIME  60.0                                                           float
WHITESPT F                                                              bool
ZENITH   F                                                              bool
SEANNEX  F                                                              bool
BEYONDP  F                                                              bool
FIDUCIAL off                                                            str
BACKLIT  off                                                            str
AIRMASS  1.831907                                                       float
FOCUS    1320.9,-64.7,-154.1,-29.8,38.4,275.1                           str
TRUSTEMP 11.567                                                         float
PMIRTEMP 9.625                                                          float
PMREADY  T                                                              bool
PMCOVER  open                                                           str
PMCOOL   off                                                            str
DOMSHUTU open                                                           str
DOMSHUTL open                                                           str
DOMLIGHH off                                                            str
DOMLIGHL off                                                            str
DOMEAZ   194.344                                                        float
DOMINPOS T                                                              bool
GUIDOFFR 0.045553                                                       float
GUIDOFFD 0.227617                                                       float
MOONDEC  -7.198095                                                      float
MOONRA   208.083286                                                     float
MOONSEP  115.55174866496                                                float
MOUNTAZ  196.394609                                                     float
MOUNTDEC -23.217009                                                     float
MOUNTEL  33.003489                                                      float
MOUNTHA  14.925591                                                      float
INCTRL   T                                                              bool
INPOS    T                                                              bool
MNTOFFD  -45.36                                                         float
MNTOFFR  12.44                                                          float
PARALLAC 15.103223                                                      float
SKYDEC   -23.217009                                                     float
SKYRA    86.995259                                                      float
TARGTDEC -23.217009                                                     float
TARGTRA  86.995259                                                      float
TARGTAZ  196.394609                                                     float
TARGTEL  33.003489                                                      float
TRGTOFFD 0.0                                                            float
TRGTOFFR 0.0                                                            float
ZD       56.996511                                                      float
TILERA   87.0                                                           float
TILEDEC  -23.2                                                          float
TCSST    06:47:41.004                                                   str
TCSMJD   59221.296127                                                   float
ACQCAM   GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                      str
GUIDECAM GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                      str
FOCUSCAM FOCUS1,FOCUS4,FOCUS6,FOCUS9                                    str
SKYCAM   SKYCAM0,SKYCAM1                                                str
REQADC   314.15,74.68                                                   str
ADCCORR  T                                                              bool
ADC1PHI  314.149996                                                     float
ADC2PHI  74.681293                                                      float
ADC1HOME F                                                              bool
ADC2HOME F                                                              bool
ADC1NREV -1.0                                                           float
ADC2NREV 0.0                                                            float
ADC1STAT STOPPED                                                        str
ADC2STAT STOPPED                                                        str
HEXPOS   1320.9,-64.7,-154.1,-29.8,38.4,275.1                           str
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                                        str
ROTOFFST 274.6                                                          float
ROTENBLD T                                                              bool
ROTRATE  0.474                                                          float
RESETROT F                                                              bool
USEPOS   T                                                              bool
PETALS   PETAL0,PETAL1,PETAL2,PETAL4,PETAL5,PETAL6,PETAL7,PETAL8,PETAL9 str
POSCYCLE 1                                                              int
POSONTGT 953                                                            int
POSONFRC 0.2496                                                         float
POSDISAB 667                                                            int
POSENABL 3818                                                           int
POSRMS   0.0174                                                         float
POSITER  1                                                              int
POSFRACT 0.95                                                           float
POSTOLER 0.005                                                          float
POSMVALL T                                                              bool
GUIDMODE catalog                                                        str
USEAOS   F                                                              bool
USESPCTR T                                                              bool
SPCGRPHS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                        str
ILLSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                        str
CCDSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                        str
TDEWPNT  -15.69                                                         float
TAIRFLOW 0.0                                                            float
TAIRITMP 11.7                                                           float
TAIROTMP 12.0                                                           float
TAIRTEMP 10.303                                                         float
TCASITMP 0.0                                                            float
TCASOTMP 11.1                                                           float
TCSITEMP 10.0                                                           float
TCSOTEMP 11.0                                                           float
TCIBTEMP 0.0                                                            float
TCIMTEMP 0.0                                                            float
TCITTEMP 0.0                                                            float
TCOSTEMP 0.0                                                            float
TCOWTEMP 0.0                                                            float
TDBTEMP  9.6                                                            float
TFLOWIN  0.0                                                            float
TFLOWOUT 0.0                                                            float
TGLYCOLI 11.5                                                           float
TGLYCOLO 11.3                                                           float
THINGES  11.5                                                           float
THINGEW  11.1                                                           float
TPMAVERT 9.597                                                          float
TPMDESIT 5.6                                                            float
TPMEIBT  9.1                                                            float
TPMEITT  9.2                                                            float
TPMEOBT  9.1                                                            float
TPMEOTT  9.4                                                            float
TPMNIBT  9.3                                                            float
TPMNITT  9.4                                                            float
TPMNOBT  10.1                                                           float
TPMNOTT  10.3                                                           float
TPMRTDT  9.0                                                            float
TPMSIBT  9.2                                                            float
TPMSITT  9.5                                                            float
TPMSOBT  8.8                                                            float
TPMSOTT  9.1                                                            float
TPMSTAT  ready                                                          str
TPMWIBT  9.2                                                            float
TPMWITT  9.6                                                            float
TPMWOBT  10.1                                                           float
TPMWOTT  10.5                                                           float
TPCITEMP 9.4                                                            float
TPCOTEMP 9.5                                                            float
TPR1HUM  0.0                                                            float
TPR1TEMP 0.0                                                            float
TPR2HUM  0.0                                                            float
TPR2TEMP 0.0                                                            float
TSERVO   40.0                                                           float
TTRSTEMP 11.0                                                           float
TTRWTEMP 10.4                                                           float
TTRUETBT -4.5                                                           float
TTRUETTT 10.9                                                           float
TTRUNTBT 10.6                                                           float
TTRUNTTT 10.7                                                           float
TTRUSTBT 11.0                                                           float
TTRUSTST 10.8                                                           float
TTRUSTTT 11.0                                                           float
TTRUTSBT 11.7                                                           float
TTRUTSMT 11.6                                                           float
TTRUTSTT 11.4                                                           float
TTRUWTBT 10.9                                                           float
TTRUWTTT 10.9                                                           float
ALARM    F                                                              bool
ALARM-ON F                                                              bool
BATTERY  100.0                                                          float
SECLEFT  5226.0                                                         float
UPSSTAT  System Normal - On Line(7)                                     str
INAMPS   70.8                                                           float
OUTWATTS 5000.0,7200.0,4800.0                                           str
COMPDEW  -10.1                                                          float
COMPHUM  9.6                                                            float
COMPAMB  19.2                                                           float
COMPTEMP 24.0                                                           float
DEWPOINT 12.3                                                           float
HUMIDITY 11.0                                                           float
PRESSURE 795.0                                                          float
OUTTEMP  0.0                                                            float
WINDDIR  281.0                                                          float
WINDSPD  9.3                                                            float
GUST     7.0                                                            float
AMNIENTN 14.2                                                           float
CFLOOR   9.8                                                            float
NWALLIN  14.5                                                           float
NWALLOUT 10.2                                                           float
WWALLIN  13.6                                                           float
WWALLOUT 10.5                                                           float
AMBIENTS 15.2                                                           float
FLOOR    13.1                                                           float
EWALLCMP 11.1                                                           float
EWALLCOU 10.8                                                           float
ROOF     9.9                                                            float
ROOFAMB  10.2                                                           float
DOMEBLOW 10.4                                                           float
DOMEBUP  10.6                                                           float
DOMELLOW 10.1                                                           float
DOMELUP  9.8                                                            float
DOMERLOW 9.7                                                            float
DOMERUP  9.2                                                            float
PLATFORM 9.7                                                            float
SHACKC   15.4                                                           float
SHACKW   13.9                                                           float
STAIRSL  10.1                                                           float
STAIRSM  9.8                                                            float
STAIRSU  9.8                                                            float
TELBASE  10.4                                                           float
UTILWALL 10.8                                                           float
UTILROOM 9.0                                                            float
TNFSPROC 8.1896                                                         float
TGFAPROC 9.8439                                                         float
SIMGFAP  F                                                              bool
USEFVC   T                                                              bool
USEFID   T                                                              bool
USEILLUM T                                                              bool
USEXSRVR T                                                              bool
USEOPENL T                                                              bool
STOPGUDR T                                                              bool
STOPFOCS T                                                              bool
STOPSKY  T                                                              bool
KEEPGUDR F                                                              bool
KEEPFOCS F                                                              bool
KEEPSKY  F                                                              bool
REACQUIR F                                                              bool
FILENAME /exposures/desi/20210106/00071111/desi-00071111.fits.fz        str
EXCLUDED                                                                str
SIMGFACQ F                                                              bool
POSCNVGD F                                                              bool
GUIEXPID 71111                                                          int
IGFRMNUM 10                                                             int
FOCEXPID 71111                                                          int
IFFRMNUM 1                                                              int
SKYEXPID 71111                                                          int
ISFRMNUM 1                                                              int
FGFRMNUM 100                                                            int
FFFRMNUM 15                                                             int
FSFRMNUM 13                                                             int
HELIOCOR 0.9999749365720424                                             float
NSPEC    500                                                            int     Number of spectra
WAVEMIN  5760.0                                                         float   First wavelength [Angstroms]
WAVEMAX  7620.0                                                         float   Last wavelength [Angstroms]
WAVESTEP 0.8                                                            float   Wavelength step size [Angstroms]
SPECTER  0.10.0                                                         str     https://github.com/desihub/specter
IN_PSF   SPECPROD/exposures/20210106/00071111/psf-r2-00071111.fits      str     Input sp
IN_IMG   SPECPROD/preproc/20210106/00071111/preproc-r2-00071111.fits    str
ORIG_PSF SPECPROD/calibnight/20210106/psfnight-r2-20210106.fits         str
BUNIT    10**+17 cm2 count s / erg                                      str     i.e. (elec/A) / (1e-17 erg/s/cm2/A)
IN_FRAME SPECPROD/exposures/20210106/00071111/frame-r2-00071111.fits    str
IN_SKY   SPECPROD/exposures/20210106/00071111/sky-r2-00071111.fits      str
FIBERFLT SPECPROD/calibnight/20210106/fiberflatnight-r2-20210106.fits   str
STDMODEL SPECPROD/exposures/20210106/00071111/stdstars-2-00071111.fits  str
======== ============================================================== ======= ===============================================

Data: FITS image [float32, 2326x500]

HDU1
----

EXTNAME = IVAR

Inverse variance of flux calibration model.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2326             int
NAXIS2   500              int
CHECKSUM YXHMcU9JZUGJaU9J str  HDU checksum updated 2021-07-08T16:29:44
DATASUM  2925906445       str  data unit checksum updated 2021-07-08T16:29:44
======== ================ ==== ==============================================

Data: FITS image [float32, 2326x500]

HDU2
----

EXTNAME = MASK

Mask of flux calibration model; 0=good.

Prior to desispec/0.24.0 and software release 18.9, the MASK HDU was compressed.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2326             int
NAXIS2   500              int
BSCALE   1                int
BZERO    2147483648       int
CHECKSUM WHahaERgZEXgaEXg str  HDU checksum updated 2021-07-08T16:29:44
DATASUM  68479139         str  data unit checksum updated 2021-07-08T16:29:44
======== ================ ==== ==============================================

Data: FITS image [int32, 2326x500]

HDU3
----

EXTNAME = WAVELENGTH

Wavelengths at which the flux calibration model is evaluated.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2326             int
BUNIT    Angstrom         str
CHECKSUM PAF9Q8D6PAD6P5D6 str  HDU checksum updated 2021-07-08T16:29:44
DATASUM  1502044794       str  data unit checksum updated 2021-07-08T16:29:44
======== ================ ==== ==============================================

Data: FITS image [float32, 2326]

HDU4
----

EXTNAME = FIBERCORR

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   16               int  length of dimension 1
NAXIS2   500              int  length of dimension 2
ENCODING ascii            str
CHECKSUM GgA3Gg60GgA0Gg50 str  HDU checksum updated 2021-07-08T16:29:44
DATASUM  2049692696       str  data unit checksum updated 2021-07-08T16:29:44
======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

================= ======= ===== ===========
Name              Type    Units Description
================= ======= ===== ===========
FLAT_TO_PSF_FLUX  float64
PSF_TO_FIBER_FLUX float64
================= ======= ===== ===========


Notes and Examples
==================

We may add an additional HDU with ``EXTNAME=METADATA`` containing a
binary table with one row per standard star giving
the details of which model was used, etc.
This is not yet implemented and details TBD.
