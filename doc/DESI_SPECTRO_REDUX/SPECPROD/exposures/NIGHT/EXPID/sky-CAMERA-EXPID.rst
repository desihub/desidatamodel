=====================
sky-CAMERA-EXPID.fits
=====================

:Summary: This holds the sky model for a given camera and exposure.
:Naming Convention: ``sky-{CAMERA}-{EXPID}.fits``, where ``{CAMERA}`` is
    one of the spectrograph cameras (*e.g.* ``z1``) and ``{EXPID}``
    is the 8-digit exposure ID.
:Regex: ``sky-[brz][0-9]-[0-9]{8}\.fits``
:File Type: FITS, 17 MB

Contents
========

====== ========== ===== ===================
Number EXTNAME    Type  Contents
====== ========== ===== ===================
HDU0_  SKY        IMAGE sky model in electrons per Angstrom
HDU1_  IVAR       IMAGE inverse variance of sky model
HDU2_  MASK       IMAGE sky mask (0 = good)
HDU3_  WAVELENGTH IMAGE wavelength in Angstrom
HDU4_  STATIVAR   IMAGE statistical-only inverse variance of sky model
HDU5_  THRPUTCORR IMAGE achromatic throughput correction per fiber
====== ========== ===== ===================

The SKY HDU is the sky model per-fiber accounting for different fiber
resolutions, but it does *not* include the empirical per-fiber throughput
correction in the THRPUTCORR HDU.  The final sky model per fiber is
``SKY * THRPUTCORR``.


FITS Header Units
=================

HDU0
----

EXTNAME = SKY

2D array of sky flux model of dimension [nspec, nwave] in units of electrons per Ansgtrom (fiber flat fielded). nspec is the number of fibers per camera. nwave in the length of the wavelength array. The spectra of all fibers share the same
wavelength grid (given in HDU WAVELENGTH). The sky model is different for each fiber because it is adapted to the resolution of each fiber, it contains corrections on bright sky line, and in some cases an anisotropic component.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ===================================================================== ======= ===============================================
KEY      Example Value                                                         Type    Comment
======== ===================================================================== ======= ===============================================
NAXIS1   2326                                                                  int
NAXIS2   500                                                                   int
EXPID    89018                                                                 int     Exposure number
EXPFRAME 0                                                                     int     Frame number
FRAMES   None                                                                  Unknown Number of Frames in Archive
TILEID   20572                                                                 int     DESI Tile ID
FIBASSGN /data/tiles/SVN_tiles/020/fiberassign-020572.fits.gz                  str     Fiber assign
FLAVOR   science                                                               str     Observation type
SEQUENCE DESI                                                                  str     OCS Sequence name
PURPOSE  Main Survey                                                           str     Purpose of observing night
PROGRAM  BRIGHT                                                                str     Program name
PROPID   2019B-5000                                                            str     Proposal ID
OBSERVER John Della Costa                                                      str     Names of observers
LEAD     Claire Poppett                                                        str     Lead observer
INSTRUME DESI                                                                  str     Instrument name
OBSERVAT KPNO                                                                  str     Observatory name
OBS-LAT  31.96403                                                              str     [deg] Observatory latitude
OBS-LONG -111.59989                                                            str     [deg] Observatory east longitude
OBS-ELEV 2097.0                                                                float   [m] Observatory elevation
TELESCOP KPNO 4.0-m telescope                                                  str     Telescope name
CORRCTOR DESI Corrector                                                        str     Corrector Identification
NIGHT    20210517                                                              int     Observing night
TIMESYS  UTC                                                                   str     Time system used for date-obs
DATE-OBS 2021-05-18T04:09:23.803681024                                         str     [UTC] Observation data and start tim
TIME-OBS 2021-05-17T04:09:23.803681024                                         str     [UTC] Observation start time
MJD-OBS  59352.17319217                                                        float   Modified Julian Date of observation
OPENSHUT 2021-05-18T04:09:24.589732                                            str     Time shutter opened
ST       12:27:16.340000                                                       str     Local Sidereal time at observation start (HH:MM
EXPTIME  495.472                                                               float   [s] Actual exposure time
REQRA    191.365                                                               float   [deg] Requested right ascension (observer input
REQDEC   -7.419                                                                float   [deg] Requested declination (observer input)
FOCUS    1069.2,-207.8,-238.0,-19.7,17.5,161.5                                 str     Telescope focus settings
VCCD     ON                                                                    str     True (ON) if CCD voltage is on
VCCDON   2021-05-02T12:14:19.872135                                            str     Time when CCD voltage was turned on
VCCDSEC  1353858.8                                                             float   [s] CCD on time in seconds
TRUSTEMP 12.6                                                                  float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.862                                                                float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                                                float   Epoch of observation
MOUNTAZ  172.168591                                                            float   [deg] Mount azimuth angle
MOUNTDEC -7.42824                                                              float   [deg] Mount declination
MOUNTEL  50.316418                                                             float   [deg] Mount elevation angle
MOUNTHA  -5.033834                                                             float   [deg] Mount hour angle
SKYDEC   -7.42824                                                              float   [deg] Telescope declination (pointing on sky)
SKYRA    191.366158                                                            float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.42824                                                              float   [deg] Target declination (to TCS)
TARGTRA  191.366158                                                            float   [deg] Target right ascension (to TCS)
USEETC   T                                                                     bool    ETC data available if true
USESKY   T                                                                     bool    DOS Control: use Sky Monitor
USEFOCUS T                                                                     bool    DOS Control: use focus
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                                               str     Hexapod trim values
USEROTAT T                                                                     bool    DOS Control: use rotator
ROTOFFST 156.5                                                                 float   [arcsec] Rotator offset
ROTENBLD T                                                                     bool    Rotator enabled
ROTRATE  0.0                                                                   float   [arcsec/min] Rotator rate
USEGUIDR T                                                                     bool    DOS Control: use guider
USEDONUT T                                                                     bool    DOS Control: use donuts
SPECGRPH 3                                                                     int     Spectrograph logical name (SP)
SPECID   6                                                                     int     Spectrograph serial number (SM)
FEEBOX   lbnl074                                                               str     CCD Controller serial number
VESSEL   11                                                                    int     Cryostat serial number
FEEVER   v20160312                                                             str     CCD Controller version
FEEPOWER ON                                                                    str     FEE power status
FEEDMASK 2134851391                                                            int     FEE dac mask
FEECMASK 1048575                                                               int     FEE clk mask
CCDTEMP  -139.7433                                                             float   [deg C] CCD controller CCD temperature
RADESYS  FK5                                                                   str     Coordinate reference frame of major/minor axes
DOSVER   trunk                                                                 str     DOS software version
OCSVER   1.2                                                                   float   OCS software version
CONSTVER DESI:CURRENT                                                          str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini                      str     DOS Configuration
PRRSECC  [8:2064, 4194:4194]                                                   str     Row prescan section for quadrant C
CCDSECA  [1:2057, 1:2064]                                                      str     CCD section for quadrant A
CLOCK15  9.9992,2.9993                                                         str     [V] high rail, low rail
DETECTOR M1-50                                                                 str     Detector (ccd) identification
CCDSECD  [2058:4114, 2065:4128]                                                str     CCD section for quadrant D
PRRSECB  [2193:4249, 1:1]                                                      str     Row prescan section for quadrant B
CCDSECB  [2058:4114, 1:2064]                                                   str     CCD section for quadrant B
CLOCK7   -2.0001,3.9999                                                        str     [V] high rail, low rail
DAC17    20.0008,14.274                                                        str     [V] set value, measured value
AMPSECC  [1:2057, 4128:2065]                                                   str     AMP section for quadrant C
CLOCK8   9.9992,2.9993                                                         str     [V] high rail, low rail
DAC3     -10.5005,-10.3824                                                     str     [V] set value, measured value
BIASSECC [2065:2128, 2130:4193]                                                str     Bias section for quadrant C
OFFSET3  0.4000000059604645,-10.3824                                           str     [V] set value, measured value
CLOCK5   9.9999,0.0                                                            str     [V] high rail, low rail
DAC9     -25.0003,-24.6789                                                     str     [V] set value, measured value
TRIMSECC [8:2064, 2130:4193]                                                   str     Trim section for quadrant C
CLOCK10  9.9992,2.9993                                                         str     [V] high rail, low rail
CLOCK1   9.9999,0.0                                                            str     [V] high rail, low rail
AMPSECA  [1:2057, 1:2064]                                                      str     AMP section for quadrant A
PRESECD  [4250:4256, 2130:4193]                                                str     Prescan section for quadrant D
DAC14    0.0,0.0148                                                            str     [V] set value, measured value
DAC4     5.9998,6.028                                                          str     [V] set value, measured value
OFFSET7  2.0,6.4908                                                            str     [V] set value, measured value
DETSECB  [2058:4114, 1:2064]                                                   str     Detector section for quadrant B
BIASSECD [2129:2192, 2130:4193]                                                str     Bias section for quadrant D
CCDCFG   M1-50_lbnl_20210128.cfg                                               str     CCD configuration file
CLOCK6   9.9999,0.0                                                            str     [V] high rail, low rail
DAC11    -25.0003,-24.7086                                                     str     [V] set value, measured value
CLOCK11  9.9992,2.9993                                                         str     [V] high rail, low rail
DIGITIME 55.9325                                                               float   [s] Time to digitize image
SETTINGS detectors_sm_20210128.json                                            str     Name of DESI CCD settings file
OFFSET2  0.4000000059604645,-8.961                                             str     [V] set value, measured value
DAC0     -9.0002,-8.9095                                                       str     [V] set value, measured value
DATASECC [8:2064, 2130:4193]                                                   str     Data section for quadrant C
PRESECC  [1:7, 2130:4193]                                                      str     Prescan section for quadrant C
DATASECD [2193:4249, 2130:4193]                                                str     Data section for quadrant D
OFFSET6  2.0,6.028                                                             str     [V] set value, measured value
BLDTIME  0.3502                                                                float   [s] Time to build image
DATASECA [8:2064, 2:2065]                                                      str     Data section for quadrant A
OFFSET0  0.4000000059604645,-8.9095                                            str     [V] set value, measured value
CLOCK16  9.9999,3.0                                                            str     [V] high rail, low rail
DELAYS   20, 20, 25, 30, 7, 3000, 7, 7, 400, 7                                 str     [10] Delay settings
CAMERA   r3                                                                    str     Camera name
DAC2     -9.0002,-8.9713                                                       str     [V] set value, measured value
DAC16    48.0,46.7082                                                          str     [V] set value, measured value
CDSPARMS 400, 400, 8, 2000                                                     str     CDS parameters
DETSECA  [1:2057, 1:2064]                                                      str     Detector section for quadrant A
CLOCK2   9.9999,0.0                                                            str     [V] high rail, low rail
OFFSET5  2.0,6.028                                                             str     [V] set value, measured value
DAC5     5.9998,6.0227                                                         str     [V] set value, measured value
CLOCK12  9.9992,2.9993                                                         str     [V] high rail, low rail
DAC6     5.9998,6.028                                                          str     [V] set value, measured value
CRYOPRES 7.776e-08                                                             str     [mb] Cryostat pressure (IP)
DAC1     -9.0002,-8.8065                                                       str     [V] set value, measured value
CLOCK3   -2.0001,3.9999                                                        str     [V] high rail, low rail
BIASSECB [2129:2192, 2:2065]                                                   str     Bias section for quadrant B
CLOCK0   9.9999,0.0                                                            str     [V] high rail, low rail
PGAGAIN  3                                                                     int     Controller gain
TRIMSECA [8:2064, 2:2065]                                                      str     Trim section for quadrant A
DATASECB [2193:4249, 2:2065]                                                   str     Data section for quadrant B
CLOCK18  9.0,0.9999                                                            str     [V] high rail, low rail
DAC15    0.0,0.0445                                                            str     [V] set value, measured value
ORSECB   [2193:4249, 2066:2097]                                                str     Row overscan section for quadrant B
DAC8     -25.0003,-25.0202                                                     str     [V] set value, measured value
AMPSECD  [4114:2058, 4128:2065]                                                str     AMP section for quadrant D
CCDPREP  purge,clear                                                           str     CCD prep actions
CRYOTEMP 162.995                                                               float   [deg K] Cryostat CCD temperature
PRESECA  [1:7, 2:2065]                                                         str     Prescan section for quadrant A
DAC7     6.4999,6.4908                                                         str     [V] set value, measured value
TRIMSECD [2193:4249, 2130:4193]                                                str     Trim section for quadrant D
ORSECC   [8:2064, 2098:2129]                                                   str     Row overscan section for quadrant C
OFFSET4  2.0,6.028                                                             str     [V] set value, measured value
CCDNAME  CCDSM6R                                                               str     CCD name
DETSECD  [2058:4114, 2065:4128]                                                str     Detector section for quadrant D
PRESECB  [4250:4256, 2:2065]                                                   str     Prescan section for quadrant B
TRIMSECB [2193:4249, 2:2065]                                                   str     Trim section for quadrant B
CCDSECC  [1:2057, 2065:4128]                                                   str     CCD section for quadrant C
CASETEMP 57.3533                                                               float   [deg C] CCD controller case temperature
OFFSET1  0.4000000059604645,-8.8065                                            str     [V] set value, measured value
PRRSECD  [2193:4249, 4194:4194]                                                str     Row prescan section for quadrant D
CLOCK17  9.0,0.9999                                                            str     [V] high rail, low rail
CPUTEMP  56.625                                                                float   [deg C] CCD controller CPU temperature
CLOCK4   9.9999,0.0                                                            str     [V] high rail, low rail
CCDSIZE  4194,4256                                                             str     CCD size in pixels (rows, columns)
ORSECA   [8:2064, 2066:2097]                                                   str     Row overscan section for quadrant A
ORSECD   [2193:4249, 2098:2129]                                                str     Row bias section for quadrant D
DAC10    -25.0003,-24.9906                                                     str     [V] set value, measured value
CLOCK9   9.9992,2.9993                                                         str     [V] high rail, low rail
BIASSECA [2065:2128, 2:2065]                                                   str     Bias section for quadrant A
DETSECC  [1:2057, 2065:4128]                                                   str     Detector section for quadrant C
DAC12    0.0,0.0297                                                            str     [V] set value, measured value
PRRSECA  [8:2064, 1:1]                                                         str     Row prescan section for quadrant A
AMPSECB  [4114:2058, 1:2064]                                                   str     AMP section for quadrant B
DAC13    0.0,0.0148                                                            str     [V] set value, measured value
CLOCK13  9.9992,2.9993                                                         str     [V] high rail, low rail
CCDTMING flatdark_lbnl_timing.txt                                              str     CCD timing file
CLOCK14  9.9992,2.9993                                                         str     [V] high rail, low rail
REQTIME  5400.0                                                                float   [s] Requested exposure time
OBSID    kp4m20210518t040923                                                   str     Unique observation identifier
PROCTYPE RAW                                                                   str     Data processing level
PRODTYPE image                                                                 str     Data product type
CHECKSUM ZTSUZRQRZRQRZRQR                                                      str     HDU checksum updated 2021-07-08T02:23:26
DATASUM  1643075339                                                            str     data unit checksum updated 2021-07-08T02:23:26
GAINA    1.681                                                                 float   e/ADU (gain applied to image)
SATULEVA 28000.0                                                               float   saturation or non lin. level, in ADU, inc. bias
OVERSCNA 1979.582408393367                                                     float   ADUs (gain not applied)
OBSRDNA  2.585806480767717                                                     float   electrons (gain is applied)
SATUELEA 43740.32197149075                                                     float   saturation or non lin. level, in electrons
GAINB    1.625                                                                 float   e/ADU (gain applied to image)
SATULEVB 57000.0                                                               float   saturation or non lin. level, in ADU, inc. bias
OVERSCNB 1997.201734623403                                                     float   ADUs (gain not applied)
OBSRDNB  3.133874296395381                                                     float   electrons (gain is applied)
SATUELEB 89379.54718123697                                                     float   saturation or non lin. level, in electrons
GAINC    1.477                                                                 float   e/ADU (gain applied to image)
SATULEVC 59000.0                                                               float   saturation or non lin. level, in ADU, inc. bias
OVERSCNC 1974.612874331026                                                     float   ADUs (gain not applied)
OBSRDNC  2.321672207733021                                                     float   electrons (gain is applied)
SATUELEC 84226.49678461307                                                     float   saturation or non lin. level, in electrons
GAIND    1.492                                                                 float   e/ADU (gain applied to image)
SATULEVD 62000.0                                                               float   saturation or non lin. level, in ADU, inc. bias
OVERSCND 1998.213031811645                                                     float   ADUs (gain not applied)
OBSRDND  2.272893499465638                                                     float   electrons (gain is applied)
SATUELED 89522.66615653702                                                     float   saturation or non lin. level, in electrons
FIBERMIN 1500                                                                  int
MODULE   CI                                                                    str
COSMSPLT F                                                                     bool
MAXSPLIT 0                                                                     int
VISITIDS 89018                                                                 str
OBSTYPE  SCIENCE                                                               str
MANIFEST F                                                                     bool
OBJECT                                                                         str
NTSSURVY None                                                                  Unknown
SBPROF   BGS                                                                   str
SEQNUM   1                                                                     int
SEQSTART 2021-05-18T04:05:52.591326                                            str
CAMSHUT  open                                                                  str
ACQTIME  15.0                                                                  float
GUIDTIME 5.0                                                                   float
FOCSTIME 60.0                                                                  float
SKYTIME  60.0                                                                  float
WHITESPT F                                                                     bool
ZENITH   F                                                                     bool
SEANNEX  F                                                                     bool
BEYONDP  F                                                                     bool
FIDUCIAL off                                                                   str
BACKLIT  off                                                                   str
AIRMASS  1.297559                                                              float
PMREADY  T                                                                     bool
PMCOVER  open                                                                  str
PMCOOL   off                                                                   str
DOMSHUTU open                                                                  str
DOMSHUTL open                                                                  str
DOMLIGHH off                                                                   str
DOMLIGHL off                                                                   str
DOMEAZ   169.39                                                                float
DOMINPOS T                                                                     bool
GUIDOFFR 0.112694                                                              float
GUIDOFFD 0.158532                                                              float
SUNRA    55.176731                                                             float
SUNDEC   19.588404                                                             float
MOONDEC  22.623481                                                             float
MOONRA   131.403971                                                            float
MOONSEP  66.138                                                                float
SLEWANGL 3.338                                                                 float
INCTRL   T                                                                     bool
INPOS    T                                                                     bool
MNTOFFD  4.07                                                                  float
MNTOFFR  -3.41                                                                 float
PARALLAC -6.039296                                                             float
TARGTAZ  172.936367                                                            float
TARGTEL  50.371093                                                             float
TRGTOFFD 0.0                                                                   float
TRGTOFFR 0.0                                                                   float
ZD       39.628907                                                             float
TILERA   191.365                                                               float
TILEDEC  -7.419                                                                float
TCSST    12:27:19.084                                                          str
TCSMJD   59352.173655                                                          float
SKYLEVEL 1.983                                                                 float
PMSEEING 1.19                                                                  float
PMTRANS  100.93                                                                float
ACQCAM   GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                             str
GUIDECAM GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                             str
FOCUSCAM FOCUS1,FOCUS4,FOCUS6,FOCUS9                                           str
SKYCAM   SKYCAM0,SKYCAM1                                                       str
REQADC   326.05,19.61                                                          str
ADCCORR  T                                                                     bool
ADC1PHI  326.050002                                                            float
ADC2PHI  19.609999                                                             float
ADC1HOME F                                                                     bool
ADC2HOME F                                                                     bool
ADC1NREV 0.0                                                                   float
ADC2NREV 0.0                                                                   float
ADC1STAT STOPPED                                                               str
ADC2STAT STOPPED                                                               str
HEXPOS   1069.1,-207.8,-238.0,-19.7,17.5,162.3                                 str
RESETROT F                                                                     bool
SPLITEXP F                                                                     bool
USESPLIT T                                                                     bool
USEPOS   T                                                                     bool
PETALS   PETAL0,PETAL1,PETAL2,PETAL3,PETAL4,PETAL5,PETAL6,PETAL7,PETAL8,PETAL9 str
POSCYCLE 1                                                                     int
POSONTGT 4060                                                                  int
POSONFRC 0.9995                                                                float
POSDISAB 917                                                                   int
POSENABL 4062                                                                  int
POSRMS   0.0068                                                                float
POSITER  1                                                                     int
POSFRACT 0.95                                                                  float
POSTOLER 0.005                                                                 float
POSMVALL T                                                                     bool
GUIDMODE catalog                                                               str
USESPCTR T                                                                     bool
SPCGRPHS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                               str
ILLSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                               str
CCDSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                               str
TDEWPNT  3.26                                                                  float
TAIRFLOW 0.0                                                                   float
TAIRITMP 16.1                                                                  float
TAIROTMP 15.9                                                                  float
TAIRTEMP 10.85                                                                 float
TCASITMP 6.6                                                                   float
TCASOTMP 13.4                                                                  float
TCSITEMP 12.2                                                                  float
TCSOTEMP 13.0                                                                  float
TCIBTEMP 0.0                                                                   float
TCIMTEMP 0.0                                                                   float
TCITTEMP 0.0                                                                   float
TCOSTEMP 0.0                                                                   float
TCOWTEMP 0.0                                                                   float
TDBTEMP  9.2                                                                   float
TFLOWIN  0.0                                                                   float
TFLOWOUT 0.0                                                                   float
TGLYCOLI 14.8                                                                  float
TGLYCOLO 14.7                                                                  float
THINGES  12.1                                                                  float
THINGEW  12.6                                                                  float
TPMAVERT 11.868                                                                float
TPMDESIT 8.9                                                                   float
TPMEIBT  11.9                                                                  float
TPMEITT  11.9                                                                  float
TPMEOBT  12.1                                                                  float
TPMEOTT  12.3                                                                  float
TPMNIBT  11.6                                                                  float
TPMNITT  11.6                                                                  float
TPMNOBT  11.7                                                                  float
TPMNOTT  11.9                                                                  float
TPMRTDT  9.36                                                                  float
TPMSIBT  11.9                                                                  float
TPMSITT  11.9                                                                  float
TPMSOBT  11.8                                                                  float
TPMSOTT  12.0                                                                  float
TPMSTAT  ready                                                                 str
TPMWIBT  11.6                                                                  float
TPMWITT  11.6                                                                  float
TPMWOBT  11.3                                                                  float
TPMWOTT  11.7                                                                  float
TPCITEMP 11.4                                                                  float
TPCOTEMP 11.4                                                                  float
TPR1HUM  0.0                                                                   float
TPR1TEMP 0.0                                                                   float
TPR2HUM  0.0                                                                   float
TPR2TEMP 0.0                                                                   float
TSERVO   40.0                                                                  float
TTRSTEMP 11.8                                                                  float
TTRWTEMP 11.6                                                                  float
TTRUETBT -1.7                                                                  float
TTRUETTT 14.0                                                                  float
TTRUNTBT 12.9                                                                  float
TTRUNTTT 13.8                                                                  float
TTRUSTBT 13.0                                                                  float
TTRUSTST 10.8                                                                  float
TTRUSTTT 12.2                                                                  float
TTRUTSBT 12.2                                                                  float
TTRUTSMT 12.1                                                                  float
TTRUTSTT 13.4                                                                  float
TTRUWTBT 12.3                                                                  float
TTRUWTTT 13.8                                                                  float
ALARM    F                                                                     bool
ALARM-ON F                                                                     bool
BATTERY  100.0                                                                 float
SECLEFT  6402.0                                                                float
UPSSTAT  System Normal - On Line(7)                                            str
INAMPS   70.5                                                                  float
OUTWATTS 5300.0,6900.0,4900.0                                                  str
COMPDEW  1.2                                                                   float
COMPHUM  41.7                                                                  float
COMPAMB  23.4                                                                  float
COMPTEMP 14.1                                                                  float
DEWPOINT 19.3                                                                  float
HUMIDITY 89.0                                                                  float
PRESSURE 795.0                                                                 float
OUTTEMP  21.2                                                                  float
WINDDIR  323.0                                                                 float
WINDSPD  14.7                                                                  float
GUST     14.7                                                                  float
AMNIENTN 16.7                                                                  float
CFLOOR   13.0                                                                  float
NWALLIN  17.6                                                                  float
NWALLOUT 11.7                                                                  float
WWALLIN  17.4                                                                  float
WWALLOUT 12.9                                                                  float
AMBIENTS 18.7                                                                  float
FLOOR    16.6                                                                  float
EWALLCMP 12.8                                                                  float
EWALLCOU 12.3                                                                  float
ROOF     13.1                                                                  float
ROOFAMB  11.7                                                                  float
DOMEBLOW 11.6                                                                  float
DOMEBUP  11.9                                                                  float
DOMELLOW 11.1                                                                  float
DOMELUP  11.1                                                                  float
DOMERLOW 11.3                                                                  float
DOMERUP  11.3                                                                  float
PLATFORM 10.6                                                                  float
SHACKC   18.3                                                                  float
SHACKW   17.7                                                                  float
STAIRSL  10.8                                                                  float
STAIRSM  10.8                                                                  float
STAIRSU  10.8                                                                  float
TELBASE  13.1                                                                  float
UTILWALL 13.0                                                                  float
UTILROOM 11.8                                                                  float
SP0NIRT  139.99                                                                float
SP0REDT  139.99                                                                float
SP0BLUT  162.99                                                                float
SP0NIRP  1.032e-07                                                             float
SP0REDP  1.065e-07                                                             float
SP0BLUP  1.047e-07                                                             float
SP1NIRT  139.99                                                                float
SP1REDT  139.99                                                                float
SP1BLUT  162.97                                                                float
SP1NIRP  6.938e-08                                                             float
SP1REDP  5.151e-08                                                             float
SP1BLUP  8.18e-08                                                              float
SP2NIRT  139.99                                                                float
SP2REDT  139.99                                                                float
SP2BLUT  163.02                                                                float
SP2NIRP  4.071e-08                                                             float
SP2REDP  9.252e-08                                                             float
SP2BLUP  8.485e-08                                                             float
SP3NIRT  139.91                                                                float
SP3REDT  140.01                                                                float
SP3BLUT  162.99                                                                float
SP3NIRP  4.101e-08                                                             float
SP3REDP  6.756e-08                                                             float
SP3BLUP  7.769e-08                                                             float
SP4NIRT  139.99                                                                float
SP4REDT  140.06                                                                float
SP4BLUT  162.99                                                                float
SP4NIRP  6.448e-08                                                             float
SP4REDP  4.941e-08                                                             float
SP4BLUP  6.535e-08                                                             float
SP5NIRT  140.08                                                                float
SP5REDT  140.06                                                                float
SP5BLUT  163.02                                                                float
SP5NIRP  6.728e-08                                                             float
SP5REDP  6.013e-08                                                             float
SP5BLUP  1.152e-07                                                             float
SP6NIRT  139.99                                                                float
SP6REDT  139.99                                                                float
SP6BLUT  162.97                                                                float
SP6NIRP  2.744e-07                                                             float
SP6REDP  6.644e-08                                                             float
SP6BLUP  6.739e-08                                                             float
SP7NIRT  140.01                                                                float
SP7REDT  140.01                                                                float
SP7BLUT  162.99                                                                float
SP7NIRP  4.848e-08                                                             float
SP7REDP  5.032e-08                                                             float
SP7BLUP  1.041e-07                                                             float
SP8NIRT  139.99                                                                float
SP8REDT  139.99                                                                float
SP8BLUT  162.97                                                                float
SP8NIRP  4.212e-08                                                             float
SP8REDP  6.672e-08                                                             float
SP8BLUP  8.506e-08                                                             float
SP9NIRT  139.99                                                                float
SP9REDT  140.06                                                                float
SP9BLUT  163.07                                                                float
SP9NIRP  5.579e-08                                                             float
SP9REDP  5.113e-08                                                             float
SP9BLUP  1.265e-07                                                             float
TNFSPROC 11.458                                                                float
TGFAPROC 4.3534                                                                float
SIMGFAP  F                                                                     bool
USEFVC   T                                                                     bool
USEFID   T                                                                     bool
USEILLUM T                                                                     bool
USEXSRVR T                                                                     bool
USEOPENL T                                                                     bool
STOPGUDR T                                                                     bool
STOPFOCS T                                                                     bool
STOPSKY  T                                                                     bool
KEEPGUDR F                                                                     bool
KEEPFOCS F                                                                     bool
KEEPSKY  F                                                                     bool
REACQUIR F                                                                     bool
FILENAME /exposures/desi/20210517/00089018/desi-00089018.fits.fz               str
EXCLUDED                                                                       str
SIMGFACQ F                                                                     bool
TCSKRA   0.3 0.003 0.00003                                                     str
TCSKDEC  0.3 0.003 0.00003                                                     str
TCSGRA   0.3                                                                   float
TCSGDEC  0.3                                                                   float
TCSMFRA  1                                                                     int
TCSMFDEC 1                                                                     int
TCSPIRA  1.0,0.0,0.0,0.0                                                       str
TCSPIDEC 1.0,0.0,0.0,0.0                                                       str
POSCVFRC 0.499                                                                 float
POSCNVGD 2027                                                                  int
CONVERGD F                                                                     bool
GUIEXPID 89018                                                                 int
IGFRMNUM 10                                                                    int
FOCEXPID 89018                                                                 int
IFFRMNUM 1                                                                     int
SKYEXPID 89017                                                                 int
ISFRMNUM 7                                                                     int
FGFRMNUM 71                                                                    int
FFFRMNUM 9                                                                     int
FSFRMNUM 6                                                                     int
HELIOCOR 0.999933029837803                                                     float
NSPEC    500                                                                   int     Number of spectra
WAVEMIN  5760.0                                                                float   First wavelength [Angstroms]
WAVEMAX  7620.0                                                                float   Last wavelength [Angstroms]
WAVESTEP 0.8                                                                   float   Wavelength step size [Angstroms]
SPECTER  0.10.0                                                                str     https://github.com/desihub/specter
IN_PSF   SPECPROD/exposures/20210517/00089018/psf-r3-00089018.fits             str     Input sp
IN_IMG   SPECPROD/preproc/20210517/00089018/preproc-r3-00089018.fits           str
ORIG_PSF SPECPROD/calibnight/20210517/psfnight-r3-20210517.fits                str
BUNIT    electron/Angstrom                                                     str
IN_FRAME SPECPROD/exposures/20210517/00089018/frame-r3-00089018.fits           str
FIBERFLT SPECPROD/calibnight/20210517/fiberflatnight-r3-20210517.fits          str
======== ===================================================================== ======= ===============================================

Data: FITS image [float32, 2326x500]

HDU1
----

EXTNAME = IVAR

Inverse variance of sky model in units of (electrons per Ansgtrom)^-2.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2326             int
NAXIS2   500              int
CHECKSUM WMCiXJ9ZWJCfWJ9Z str  HDU checksum updated 2021-07-08T02:23:26
DATASUM  3732109365       str  data unit checksum updated 2021-07-08T02:23:26
======== ================ ==== ==============================================

Data: FITS image [float32, 2326x500]

HDU2
----

EXTNAME = MASK

Sky mask; 0=good. See the :doc:`bitmask documentation </bitmasks>` page for the definition of the bits.
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
CHECKSUM kIf3lGc0kGc0kGc0 str  HDU checksum updated 2021-07-08T02:23:26
DATASUM  581500           str  data unit checksum updated 2021-07-08T02:23:26
======== ================ ==== ==============================================

Data: FITS image [int32, 2326x500]

HDU3
----

EXTNAME = WAVELENGTH

1D array of wavelengths, in Angstrom. Note the wavelength is in the solar system barycenter frame, so that the sky flux array
can be directly subtracted to the flat-fielded frame fluxes which are on the same wavelength grid. In order to compare the
sky spectrum of different exposures, or with litterature data, one has to convert back the wavelength array to the observer frame,
by dividing it by Doppler factor saved in header keyword HELIOCOR in HDU0. See also the frame :ref:`WAVELENGTH documentation <frame-hdu3-wavelength>` for more details.


Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2326             int
CHECKSUM 7BAoAA3l7A9lAA9l str  HDU checksum updated 2021-07-08T02:23:26
DATASUM  1502044794       str  data unit checksum updated 2021-07-08T02:23:26
======== ================ ==== ==============================================

Data: FITS image [float32, 2326]

HDU4
----

EXTNAME = STATIVAR

Statistical-only inverse variance of sky model.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2326             int
NAXIS2   500              int
CHECKSUM SAMkT5JjSAJjS3Jj str  HDU checksum updated 2021-07-08T02:23:27
DATASUM  3877575180       str  data unit checksum updated 2021-07-08T02:23:27
======== ================ ==== ==============================================

Data: FITS image [float32, 2326x500]

HDU5
----

EXTNAME = THRPUTCORR

Multiplicative achromatic throughput correction per fiber. This term has been measured on the bright sky lines
of each fiber from the exposure (EXPID). It is used as a correction to the mean sky model.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   500              int
BUNIT    Angstrom         str
CHECKSUM VPA5WO62VOA2VO52 str  HDU checksum updated 2021-07-08T02:23:27
DATASUM  63793519         str  data unit checksum updated 2021-07-08T02:23:27
======== ================ ==== ==============================================

Data: FITS image [float32, 500]


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
