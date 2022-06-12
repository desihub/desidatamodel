=======================
frame-CAMERA-EXPID.fits
=======================

:Summary: Frame files contain the raw extracted electrons from DESI data, without
    any further calibration.
:Naming Convention: ``frame-{CAMERA}-{EXPID}.fits``, where ``{CAMERA}`` is
    one of the spectrograph cameras (*e.g.* ``z1``) and ``{EXPID}``
    is the 8-digit exposure ID.
:Regex: ``frame-[brz][0-9]-[0-9]{8}\.fits``
:File Type: FITS, 70 MB

Contents
========

====== ========== ======== ===================
Number EXTNAME    Type     Contents
====== ========== ======== ===================
HDU0_  FLUX       IMAGE    Extracted flux in electrons per Angstrom
HDU1_  IVAR       IMAGE    Inverse variance of the extracted flux
HDU2_  MASK       IMAGE    Bad value mask; 0=good
HDU3_  WAVELENGTH IMAGE    Wavelength grid of the extraction (Angstrom)
HDU3_  RESOLUTION IMAGE    Resolution matrix
HDU5_  FIBERMAP   BINTABLE Fibermap
HDU6_  CHI2PIX    IMAGE    chi2 of PSF fit to CCD pixels
====== ========== ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = FLUX

2D array of extracted flux[nspec, nwave] in units of electrons per Angstrom. nspec is the number of fibers per camera.
nwave in the length of the wavelength array. The spectra of all fibers share the same
wavelength grid (given in HDU WAVELENGTH).

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ===================================================================== ======= ===============================================
KEY      Example Value                                                         Type    Comment
======== ===================================================================== ======= ===============================================
NAXIS1   2751                                                                  int     Number of wavelengths
NAXIS2   500                                                                   int     Number of spectra
EXPID    77755                                                                 int     Exposure number
EXPFRAME 0                                                                     int     Frame number
FRAMES   None                                                                  Unknown Number of Frames in Archive
TILEID   80818                                                                 int     DESI Tile ID
FIBASSGN /data/tiles/SVN_tiles/080/fiberassign-080818.fits.gz                  str     Fiber assign
FLAVOR   science                                                               str     Observation type
SEQUENCE DESI                                                                  str     OCS Sequence name
PURPOSE  SV                                                                    str     Purpose of observing night
PROGRAM  Dither fibermode tile 80818 (110.36, 78.76)                           str     Program name
PROPID   2019B-5000                                                            str     Proposal ID
OBSERVER Antonella Palmese                                                     str     Names of observers
LEAD     Ann Elliott                                                           str     Lead observer
INSTRUME DESI                                                                  str     Instrument name
OBSERVAT KPNO                                                                  str     Observatory name
OBS-LAT  31.96403                                                              str     [deg] Observatory latitude
OBS-LONG -111.59989                                                            str     [deg] Observatory east longitude
OBS-ELEV 2097.0                                                                float   [m] Observatory elevation
TELESCOP KPNO 4.0-m telescope                                                  str     Telescope name
CORRCTOR DESI Corrector                                                        str     Corrector Identification
NIGHT    20210223                                                              int     Observing night
TIMESYS  UTC                                                                   str     Time system used for date-obs
DATE-OBS 2021-02-24T06:21:55.373451008                                         str     [UTC] Observation data and start tim
TIME-OBS 2021-02-23T06:21:55.373451008                                         str     [UTC] Observation start time
MJD-OBS  59269.26522423                                                        float   Modified Julian Date of observation
OPENSHUT None                                                                  Unknown Time shutter opened
ST       09:12:55.689999                                                       str     Local Sidereal time at observation start (HH:MM
EXPTIME  180.034                                                               float   [s] Actual exposure time
REQRA    110.36                                                                float   [deg] Requested right ascension (observer input
REQDEC   78.76                                                                 float   [deg] Requested declination (observer input)
FOCUS    1117.7,-820.8,-60.5,15.2,30.4,201.4                                   str     Telescope focus settings
VCCD     ON                                                                    str     True (ON) if CCD voltage is on
VCCDON   2021-02-12T20:17:35.596905                                            str     Time when CCD voltage was turned on
VCCDSEC  986896.6                                                              float   [s] CCD on time in seconds
TRUSTEMP 11.7                                                                  float   [deg] Average Telescope truss temperature (only
PMIRTEMP 10.225                                                                float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                                                float   Epoch of observation
MOUNTAZ  353.114997                                                            float   [deg] Mount azimuth angle
MOUNTDEC 78.77085                                                              float   [deg] Mount declination
MOUNTEL  41.759267                                                             float   [deg] Mount elevation angle
MOUNTHA  27.3357                                                               float   [deg] Mount hour angle
SKYDEC   78.77085                                                              float   [deg] Telescope declination (pointing on sky)
SKYRA    110.326029                                                            float   [deg] Telescope right ascension (pointing on sk
TARGTDEC 78.77085                                                              float   [deg] Target declination (to TCS)
TARGTRA  110.326029                                                            float   [deg] Target right ascension (to TCS)
USEETC   F                                                                     bool    ETC data available if true
USESKY   T                                                                     bool    DOS Control: use Sky Monitor
USEFOCUS T                                                                     bool    DOS Control: use focus
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                                               str     Hexapod trim values
USEROTAT T                                                                     bool    DOS Control: use rotator
ROTOFFST 198.4                                                                 float   [arcsec] Rotator offset
ROTENBLD T                                                                     bool    Rotator enabled
ROTRATE  0.0                                                                   float   [arcsec/min] Rotator rate
USEGUIDR T                                                                     bool    DOS Control: use guider
USEDONUT T                                                                     bool    DOS Control: use donuts
SPECGRPH 7                                                                     int     Spectrograph logical name (SP)
SPECID   8                                                                     int     Spectrograph serial number (SM)
FEEBOX   lbnl067                                                               str     CCD Controller serial number
VESSEL   25                                                                    int     Cryostat serial number
FEEVER   v20160312                                                             str     CCD Controller version
FEEPOWER ON                                                                    str     FEE power status
FEEDMASK 2134851391                                                            int     FEE dac mask
FEECMASK 1048575                                                               int     FEE clk mask
CCDTEMP  850.0                                                                 float   [deg C] CCD controller CCD temperature
RADESYS  FK5                                                                   str     Coordinate reference frame of major/minor axes
DOSVER   trunk                                                                 str     DOS software version
OCSVER   1.2                                                                   float   OCS software version
CONSTVER DESI:CURRENT                                                          str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini                      str     DOS Configuration
DAC14    0.0,0.7072                                                            str     [V] set value, measured value
DAC6     0.0,-0.0368                                                           str     [V] set value, measured value
DAC11    26.9998,26.7268                                                       str     [V] set value, measured value
BIASSECC [2053:2116, 2114:4161]                                                str     Bias section for quadrant C
DAC15    19.9997,19.8848                                                       str     [V] set value, measured value
DAC5     0.0,-0.0368                                                           str     [V] set value, measured value
CASETEMP 58.3376                                                               float   [deg C] CCD controller case temperature
AMPSECB  [2049:4096, 2048:1]                                                   str     AMP section for quadrant B
DAC8     26.9998,26.5784                                                       str     [V] set value, measured value
OFFSET3  -1.5,15.8723                                                          str     [V] set value, measured value
DAC9     26.9998,26.3707                                                       str     [V] set value, measured value
OFFSET0  -1.5,15.8002                                                          str     [V] set value, measured value
SETTINGS detectors_sm_20210128.json                                            str     Name of DESI CCD settings file
DAC13    -5.0006,-5.0544                                                       str     [V] set value, measured value
CLOCK13  3.0,-7.0002                                                           str     [V] high rail, low rail
PRESECA  [1:4, 2:2049]                                                         str     Prescan section for quadrant A
BLDTIME  0.3548                                                                float   [s] Time to build image
CLOCK8   3.0,-7.0002                                                           str     [V] high rail, low rail
ORSECD   [2181:4228, 2082:2113]                                                str     Row bias section for quadrant D
DAC1     15.9998,15.7899                                                       str     [V] set value, measured value
PRRSECA  [5:2052, 1:1]                                                         str     Row prescan section for quadrant A
ORSECB   [2181:4228, 2050:2081]                                                str     Row overscan section for quadrant B
DATASECA [5:2052, 2:2049]                                                      str     Data section for quadrant A
DAC3     15.9998,15.862                                                        str     [V] set value, measured value
OFFSET7  -1.100000023841858,-0.0368                                            str     [V] set value, measured value
CRYOTEMP 162.97                                                                float   [deg K] Cryostat CCD temperature
TRIMSECC [5:2052, 2114:4161]                                                   str     Trim section for quadrant C
CPUTEMP  58.1015                                                               float   [deg C] CCD controller CPU temperature
TRIMSECB [2181:4228, 2:2049]                                                   str     Trim section for quadrant B
DETSECD  [2049:4096, 2049:4096]                                                str     Detector section for quadrant D
CLOCK1   3.9999,-4.0002                                                        str     [V] high rail, low rail
CLOCK5   3.9999,-4.0002                                                        str     [V] high rail, low rail
OFFSET2  -1.5,15.8414                                                          str     [V] set value, measured value
CLOCK2   3.9999,-4.0002                                                        str     [V] high rail, low rail
DAC16    0.0,63.525                                                            str     [V] set value, measured value
CCDSECD  [2049:4096, 2049:4096]                                                str     CCD section for quadrant D
PRESECC  [1:4, 2114:4161]                                                      str     Prescan section for quadrant C
PRRSECC  [5:2052, 4162:4162]                                                   str     Row prescan section for quadrant C
DETSECA  [1:2048, 1:2048]                                                      str     Detector section for quadrant A
DATASECC [5:2052, 2114:4161]                                                   str     Data section for quadrant C
DAC17    -0.0,0.0854                                                           str     [V] set value, measured value
OFFSET1  -1.5,15.7899                                                          str     [V] set value, measured value
CLOCK18  3.9999,-4.0002                                                        str     [V] high rail, low rail
DAC7     0.0,-0.0316                                                           str     [V] set value, measured value
CLOCK12  3.0,-7.0002                                                           str     [V] high rail, low rail
CCDTMING flatdark_sta_timing.txt                                               str     CCD timing file
TRIMSECA [5:2052, 2:2049]                                                      str     Trim section for quadrant A
PGAGAIN  5                                                                     int     Controller gain
PRESECB  [4229:4232, 2:2049]                                                   str     Prescan section for quadrant B
AMPSECC  [2048:1, 2049:4096]                                                   str     AMP section for quadrant C
DAC12    4.9997,5.0544                                                         str     [V] set value, measured value
DATASECD [2181:4228, 2114:4161]                                                str     Data section for quadrant D
DATASECB [2181:4228, 2:2049]                                                   str     Data section for quadrant B
CCDSECC  [1:2048, 2049:4096]                                                   str     CCD section for quadrant C
CLOCK4   3.9999,-4.0002                                                        str     [V] high rail, low rail
OFFSET4  -1.100000023841858,-0.0263                                            str     [V] set value, measured value
CLOCK11  0.0,0.0                                                               str     [V] high rail, low rail
CRYOPRES 1.017e-07                                                             str     [mb] Cryostat pressure (IP)
DETSECB  [2049:4096, 1:2048]                                                   str     Detector section for quadrant B
OFFSET6  -1.100000023841858,-0.0368                                            str     [V] set value, measured value
CCDPREP  purge,clear                                                           str     CCD prep actions
ORSECA   [5:2052, 2050:2081]                                                   str     Row overscan section for quadrant A
DETECTOR sn22829                                                               str     Detector (ccd) identification
BIASSECD [2117:2180, 2114:4161]                                                str     Bias section for quadrant D
CLOCK16  0.0,0.0                                                               str     [V] high rail, low rail
CLOCK15  0.0,0.0                                                               str     [V] high rail, low rail
DIGITIME 54.7765                                                               float   [s] Time to digitize image
CCDNAME  CCDSM8B                                                               str     CCD name
CDSPARMS 400, 400, 8, 1000                                                     str     CDS parameters
DETSECC  [1:2048, 2049:4096]                                                   str     Detector section for quadrant C
PRRSECD  [2181:4228, 4162:4162]                                                str     Row prescan section for quadrant D
CLOCK17  3.9999,-4.0002                                                        str     [V] high rail, low rail
BIASSECB [2117:2180, 2:2049]                                                   str     Bias section for quadrant B
AMPSECA  [1:2048, 1:2048]                                                      str     AMP section for quadrant A
DAC4     0.0,-0.021                                                            str     [V] set value, measured value
CCDSECA  [1:2048, 1:2048]                                                      str     CCD section for quadrant A
CLOCK14  3.0,-7.0002                                                           str     [V] high rail, low rail
CAMERA   b7                                                                    str     Camera name
CLOCK3   6.9999,-2.0001                                                        str     [V] high rail, low rail
PRESECD  [4229:4232, 2114:4161]                                                str     Prescan section for quadrant D
PRRSECB  [2181:4228, 1:1]                                                      str     Row prescan section for quadrant B
CCDSIZE  4162,4232                                                             str     CCD size in pixels (rows, columns)
CLOCK6   3.9999,-4.0002                                                        str     [V] high rail, low rail
BIASSECA [2053:2116, 2:2049]                                                   str     Bias section for quadrant A
ORSECC   [5:2052, 2082:2113]                                                   str     Row overscan section for quadrant C
DAC2     15.9998,15.8311                                                       str     [V] set value, measured value
AMPSECD  [4096:2049, 4096:2049]                                                str     AMP section for quadrant D
OFFSET5  -1.100000023841858,-0.0316                                            str     [V] set value, measured value
DAC0     15.9998,15.8002                                                       str     [V] set value, measured value
DAC10    26.9998,26.1332                                                       str     [V] set value, measured value
TRIMSECD [2181:4228, 2114:4161]                                                str     Trim section for quadrant D
CLOCK0   3.9999,-4.0002                                                        str     [V] high rail, low rail
CLOCK9   3.0,-7.0002                                                           str     [V] high rail, low rail
CCDSECB  [2049:4096, 1:2048]                                                   str     CCD section for quadrant B
DELAYS   13, 13, 25, 25, 8, 3000, 7, 7, 400, 7                                 str     [10] Delay settings
CLOCK7   6.9999,-2.0001                                                        str     [V] high rail, low rail
CCDCFG   default_sta_20210128.cfg                                              str     CCD configuration file
CLOCK10  3.0,-7.0002                                                           str     [V] high rail, low rail
REQTIME  180.0                                                                 float   [s] Requested exposure time
OBSID    kp4m20210224t062155                                                   str     Unique observation identifier
PROCTYPE RAW                                                                   str     Data processing level
PRODTYPE image                                                                 str     Data product type
CHECKSUM 1Zdj4Ych1Ych1Ych                                                      str     HDU checksum updated 2021-07-08T12:56:13
DATASUM  2770592137                                                            str     data unit checksum updated 2021-07-08T12:56:13
GAINA    1.117                                                                 float   e/ADU (gain applied to image)
SATULEVA 63500.0                                                               float   saturation or non lin. level, in ADU, inc. bias
OVERSCNA 1195.794247115305                                                     float   ADUs (gain not applied)
OBSRDNA  3.032856327436087                                                     float   electrons (gain is applied)
SATUELEA 69593.7978259722                                                      float   saturation or non lin. level, in electrons
GAINB    1.117                                                                 float   e/ADU (gain applied to image)
SATULEVB 63700.0                                                               float   saturation or non lin. level, in ADU, inc. bias
OVERSCNB 1188.874709766999                                                     float   ADUs (gain not applied)
OBSRDNB  2.834090558391209                                                     float   electrons (gain is applied)
SATUELEB 69824.92694919027                                                     float   saturation or non lin. level, in electrons
GAINC    1.127                                                                 float   e/ADU (gain applied to image)
SATULEVC 59000.0                                                               float   saturation or non lin. level, in ADU, inc. bias
OVERSCNC 1193.463564006085                                                     float   ADUs (gain not applied)
OBSRDNC  2.929996330132565                                                     float   electrons (gain is applied)
SATUELEC 65147.96656336514                                                     float   saturation or non lin. level, in electrons
GAIND    1.128                                                                 float   e/ADU (gain applied to image)
SATULEVD 63600.0                                                               float   saturation or non lin. level, in ADU, inc. bias
OVERSCND 1176.893356381423                                                     float   ADUs (gain not applied)
OBSRDND  2.792311084921087                                                     float   electrons (gain is applied)
SATUELED 70413.26429400175                                                     float   saturation or non lin. level, in electrons
FIBERMIN 3500                                                                  int
MODULE   CI                                                                    str
COSMSPLT F                                                                     bool
MAXSPLIT 0                                                                     int
SPLITIDS 77755                                                                 str
OBSTYPE  SCIENCE                                                               str
MANIFEST F                                                                     bool
OBJECT                                                                         str
SEQNUM   1                                                                     int
SEQSTART 2021-02-24T06:19:10.430069                                            str
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
AIRMASS  1.501465                                                              float
PMREADY  T                                                                     bool
PMCOVER  open                                                                  str
PMCOOL   off                                                                   str
DOMSHUTU open                                                                  str
DOMSHUTL open                                                                  str
DOMLIGHH off                                                                   str
DOMLIGHL off                                                                   str
DOMEAZ   347.3                                                                 float
DOMINPOS T                                                                     bool
GUIDOFFR -0.300306                                                             float
GUIDOFFD -0.206036                                                             float
MOONDEC  24.054124                                                             float
MOONRA   119.092751                                                            float
MOONSEP  55.0686276414593                                                      float
INCTRL   T                                                                     bool
INPOS    T                                                                     bool
MNTOFFD  -58.99                                                                float
MNTOFFR  12.19                                                                 float
PARALLAC 147.87483                                                             float
TARGTAZ  352.989038                                                            float
TARGTEL  41.700973                                                             float
TRGTOFFD 0.0                                                                   float
TRGTOFFR 0.0                                                                   float
ZD       48.299027                                                             float
TILERA   110.36                                                                float
TILEDEC  78.76                                                                 float
TCSST    09:12:55.137                                                          str
TCSMJD   59269.265649                                                          float
SKYLEVEL 7.943                                                                 float
PMSEEING 0.94                                                                  float
PMTRANS  100.93                                                                float
ACQCAM   GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                             str
GUIDECAM GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                             str
FOCUSCAM FOCUS1,FOCUS4,FOCUS6,FOCUS9                                           str
SKYCAM   SKYCAM0,SKYCAM1                                                       str
REQADC   109.36,187.96                                                         str
ADCCORR  T                                                                     bool
ADC1PHI  109.360004                                                            float
ADC2PHI  187.960003                                                            float
ADC1HOME F                                                                     bool
ADC2HOME F                                                                     bool
ADC1NREV -1.0                                                                  float
ADC2NREV -1.0                                                                  float
ADC1STAT STOPPED                                                               str
ADC2STAT STOPPED                                                               str
HEXPOS   1117.8,-820.8,-61.4,15.2,30.5,219.3                                   str
RESETROT F                                                                     bool
USEPOS   T                                                                     bool
PETALS   PETAL0,PETAL1,PETAL2,PETAL3,PETAL4,PETAL5,PETAL6,PETAL7,PETAL8,PETAL9 str
POSCYCLE 1                                                                     int
POSONTGT 1540                                                                  int
POSONFRC 0.3704                                                                float
POSDISAB 823                                                                   int
POSENABL 4158                                                                  int
POSRMS   0.0122                                                                float
POSITER  1                                                                     int
POSFRACT 0.95                                                                  float
POSTOLER 0.005                                                                 float
POSMVALL T                                                                     bool
GUIDMODE catalog                                                               str
USEAOS   F                                                                     bool
USESPCTR T                                                                     bool
SPCGRPHS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                               str
ILLSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                               str
CCDSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                               str
TDEWPNT  -19.54                                                                float
TAIRFLOW 0.0                                                                   float
TAIRITMP 12.2                                                                  float
TAIROTMP 13.2                                                                  float
TAIRTEMP 10.655                                                                float
TCASITMP 6.6                                                                   float
TCASOTMP 11.5                                                                  float
TCSITEMP 10.8                                                                  float
TCSOTEMP 11.4                                                                  float
TCIBTEMP 0.0                                                                   float
TCIMTEMP 0.0                                                                   float
TCITTEMP 0.0                                                                   float
TCOSTEMP 0.0                                                                   float
TCOWTEMP 0.0                                                                   float
TDBTEMP  10.5                                                                  float
TFLOWIN  0.0                                                                   float
TFLOWOUT 0.0                                                                   float
TGLYCOLI 12.1                                                                  float
TGLYCOLO 12.0                                                                  float
THINGES  11.6                                                                  float
THINGEW  11.7                                                                  float
TPMAVERT 10.242                                                                float
TPMDESIT 7.0                                                                   float
TPMEIBT  10.1                                                                  float
TPMEITT  10.0                                                                  float
TPMEOBT  10.3                                                                  float
TPMEOTT  10.3                                                                  float
TPMNIBT  9.7                                                                   float
TPMNITT  10.4                                                                  float
TPMNOBT  10.5                                                                  float
TPMNOTT  10.3                                                                  float
TPMRTDT  10.31                                                                 float
TPMSIBT  10.3                                                                  float
TPMSITT  10.0                                                                  float
TPMSOBT  10.0                                                                  float
TPMSOTT  10.4                                                                  float
TPMSTAT  ready                                                                 str
TPMWIBT  9.9                                                                   float
TPMWITT  10.0                                                                  float
TPMWOBT  10.2                                                                  float
TPMWOTT  10.5                                                                  float
TPCITEMP 10.2                                                                  float
TPCOTEMP 10.2                                                                  float
TPR1HUM  0.0                                                                   float
TPR1TEMP 0.0                                                                   float
TPR2HUM  0.0                                                                   float
TPR2TEMP 0.0                                                                   float
TSERVO   40.0                                                                  float
TTRSTEMP 10.7                                                                  float
TTRWTEMP 11.3                                                                  float
TTRUETBT -4.0                                                                  float
TTRUETTT 10.8                                                                  float
TTRUNTBT 11.1                                                                  float
TTRUNTTT 11.0                                                                  float
TTRUSTBT 11.1                                                                  float
TTRUSTST 10.8                                                                  float
TTRUSTTT 11.1                                                                  float
TTRUTSBT 12.0                                                                  float
TTRUTSMT 12.0                                                                  float
TTRUTSTT 11.0                                                                  float
TTRUWTBT 10.9                                                                  float
TTRUWTTT 11.0                                                                  float
ALARM    F                                                                     bool
ALARM-ON F                                                                     bool
BATTERY  100.0                                                                 float
SECLEFT  6444.0                                                                float
UPSSTAT  System Normal - On Line(7)                                            str
INAMPS   71.9                                                                  float
OUTWATTS 5100.0,7300.0,4800.0                                                  str
COMPDEW  -15.0                                                                 float
COMPHUM  5.0                                                                   float
COMPAMB  22.0                                                                  float
COMPTEMP 28.4                                                                  float
DEWPOINT 19.3                                                                  float
HUMIDITY 89.0                                                                  float
PRESSURE 795.0                                                                 float
OUTTEMP  21.2                                                                  float
WINDDIR  323.0                                                                 float
WINDSPD  14.7                                                                  float
GUST     14.7                                                                  float
AMNIENTN 15.9                                                                  float
CFLOOR   10.5                                                                  float
NWALLIN  16.3                                                                  float
NWALLOUT 9.9                                                                   float
WWALLIN  16.4                                                                  float
WWALLOUT 11.3                                                                  float
AMBIENTS 17.2                                                                  float
FLOOR    14.6                                                                  float
EWALLCMP 11.6                                                                  float
EWALLCOU 11.3                                                                  float
ROOF     10.6                                                                  float
ROOFAMB  11.1                                                                  float
DOMEBLOW -99.9                                                                 float
DOMEBUP  -99.9                                                                 float
DOMELLOW -99.9                                                                 float
DOMELUP  -99.9                                                                 float
DOMERLOW -99.9                                                                 float
DOMERUP  -99.9                                                                 float
PLATFORM -99.9                                                                 float
SHACKC   17.3                                                                  float
SHACKW   16.9                                                                  float
STAIRSL  -99.9                                                                 float
STAIRSM  -99.9                                                                 float
STAIRSU  -99.9                                                                 float
TELBASE  10.8                                                                  float
UTILWALL 11.0                                                                  float
UTILROOM 11.1                                                                  float
SP0NIRT  139.99                                                                float
SP0REDT  139.99                                                                float
SP0BLUT  162.97                                                                float
SP0NIRP  8.249e-08                                                             float
SP0REDP  6.155e-08                                                             float
SP0BLUP  8.905e-08                                                             float
SP1NIRT  139.99                                                                float
SP1REDT  139.99                                                                float
SP1BLUT  162.97                                                                float
SP1NIRP  4.38e-08                                                              float
SP1REDP  5.379e-08                                                             float
SP1BLUP  8.005e-08                                                             float
SP2NIRT  139.99                                                                float
SP2REDT  139.99                                                                float
SP2BLUT  163.02                                                                float
SP2NIRP  8.556e-08                                                             float
SP2REDP  8.642e-08                                                             float
SP2BLUP  7.737e-08                                                             float
SP3NIRT  139.99                                                                float
SP3REDT  139.96                                                                float
SP3BLUT  162.99                                                                float
SP3NIRP  3.824e-08                                                             float
SP3REDP  6.739e-08                                                             float
SP3BLUP  9.329e-08                                                             float
SP4NIRT  139.99                                                                float
SP4REDT  140.06                                                                float
SP4BLUT  163.04                                                                float
SP4NIRP  6.3e-08                                                               float
SP4REDP  4.941e-08                                                             float
SP4BLUP  5.325e-08                                                             float
SP5NIRT  139.99                                                                float
SP5REDT  139.99                                                                float
SP5BLUT  163.02                                                                float
SP5NIRP  6.881e-08                                                             float
SP5REDP  6.584e-08                                                             float
SP5BLUP  1.101e-07                                                             float
SP6NIRT  139.99                                                                float
SP6REDT  139.99                                                                float
SP6BLUT  162.97                                                                float
SP6NIRP  2.809e-07                                                             float
SP6REDP  6.053e-08                                                             float
SP6BLUP  7.54e-08                                                              float
SP7NIRT  139.99                                                                float
SP7REDT  139.99                                                                float
SP7BLUT  162.97                                                                float
SP7NIRP  7.49e-08                                                              float
SP7REDP  4.383e-08                                                             float
SP7BLUP  1.018e-07                                                             float
SP8NIRT  139.99                                                                float
SP8REDT  139.99                                                                float
SP8BLUT  162.97                                                                float
SP8NIRP  3.843e-08                                                             float
SP8REDP  5.37e-08                                                              float
SP8BLUP  8.29699999999999e-08                                                  float
SP9NIRT  140.03                                                                float
SP9REDT  140.01                                                                float
SP9BLUT  163.02                                                                float
SP9NIRP  5.706e-08                                                             float
SP9REDP  6.875e-08                                                             float
SP9BLUP  1.206e-07                                                             float
TNFSPROC 8.6995                                                                float
TGFAPROC 9.835                                                                 float
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
FILENAME /exposures/desi/20210223/00077755/desi-00077755.fits.fz               str
EXCLUDED                                                                       str
FVCTIME  2.0                                                                   float
SIMGFACQ F                                                                     bool
TCSKRA   0.3 0.003 0.00003                                                     str
TCSKDEC  0.3 0.003 0.00003                                                     str
TCSGRA   0.3                                                                   float
TCSGDEC  0.3                                                                   float
TCSMFRA  1                                                                     int
TCSMFDEC 1                                                                     int
TCSPIRA  1.0,0.0,0.0,0.0                                                       str
TCSPIDEC 1.0,0.0,0.0,0.0                                                       str
POSCNVGD F                                                                     bool
GUIEXPID 77755                                                                 int
IGFRMNUM 10                                                                    int
FOCEXPID 77755                                                                 int
IFFRMNUM 1                                                                     int
SKYEXPID 77755                                                                 int
ISFRMNUM 1                                                                     int
FGFRMNUM 30                                                                    int
FFFRMNUM 4                                                                     int
FSFRMNUM 3                                                                     int
HELIOCOR 0.9999521148013759                                                    float
NSPEC    500                                                                   int     Number of spectra
WAVEMIN  3600.0                                                                float   First wavelength [Angstroms]
WAVEMAX  5800.0                                                                float   Last wavelength [Angstroms]
WAVESTEP 0.8                                                                   float   Wavelength step size [Angstroms]
SPECTER  0.10.0                                                                str     https://github.com/desihub/specter
IN_PSF   SPECPROD/exposures/20210223/00077755/psf-b7-00077755.fits             str     Input sp
IN_IMG   SPECPROD/preproc/20210223/00077755/preproc-b7-00077755.fits           str
ORIG_PSF SPECPROD/calibnight/20210223/psfnight-b7-20210223.fits                str
BUNIT    electron/Angstrom                                                     str
======== ===================================================================== ======= ===============================================

Data: FITS image [float32, 2751x500]

HDU1
----

EXTNAME = IVAR

Inverse variance of the flux values in HDU0. The unit is 1/(electrons/Angstrom)^2. The noise from neighboring spectral pixels is uncorrelated.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2751             int  Number of wavelengths
NAXIS2   500              int  Number of spectra
CHECKSUM YgRiaZOfTdOfYZOf str  HDU checksum updated 2021-07-08T12:56:13
DATASUM  2402704670       str  data unit checksum updated 2021-07-08T12:56:13
======== ================ ==== ==============================================

Data: FITS image [float32, 2751x500]

HDU2
----

EXTNAME = MASK

Mask of spectral data; 0=good. See the :doc:`bitmask documentation </bitmasks>` page for the definition of the bits.
Prior to desispec/0.24.0 and software release 18.9, the MASK HDU was compressed.


Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2751             int  Number of wavelengths
NAXIS2   500              int  Number of spectra
BSCALE   1                int
BZERO    2147483648       int
CHECKSUM 9GbI9FbG9FbG9FbG str  HDU checksum updated 2021-07-08T12:56:14
DATASUM  688701           str  data unit checksum updated 2021-07-08T12:56:14
======== ================ ==== ==============================================

Data: FITS image [int32, 2751x500]

.. _frame-hdu3-wavelength:

HDU3
----

EXTNAME = WAVELENGTH

1D array of wavelengths in Angstrom, in vacuum (not in air). For science exposures (in opposition to calibration exposures), the wavelength in is the rest frame of the solar system barycenter. The Doppler factor applied to the observed wavelength at the telescope to convert them to the barycentric frame is saved in header keyword HELIOCOR in HDU0. In other words, WAVELENGTH = BARYCENTRIC_FRAME_WAVELENGTH = HELICOR * OBSERVER_FRAME_WAVELENGTH. Note a single factor has been applied to all fibers despite a small difference in pointing.


Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2751             int  Number of wavelengths
BUNIT    Angstrom         str
CHECKSUM 9GQG9DPE9DPE9DPE str  HDU checksum updated 2021-07-08T12:56:14
DATASUM  979185614        str  data unit checksum updated 2021-07-08T12:56:14
======== ================ ==== ==============================================

Data: FITS image [float64, 2751]

.. _frame-hdu4-resolution:

HDU4
----

EXTNAME = RESOLUTION

Resolution matrix stored as a 3D sparse matrix:

Rdata[nspec, ndiag, nwave]

To convert this into sparse matrices for convolving a model that is sampled
at the same wavelengths as the extractions (HDU EXTNAME='WAVELENGTH'):

.. code::

    from scipy.sparse import spdiags
    from astropy.io import fits
    import numpy as np

    #- read a model and its wavelength vector from somewhere
    #- IMPORTANT: cast them to .astype(np.float64) to get native endian

    #- read the resolution data
    resdata = fits.getdata(framefile, 'RESOLUTION').astype(np.float64)

    nspec, nwave = model.shape
    convolvedmodel = np.zeros((nspec, nwave))
    diags = np.arange(10, -11, -1)

    for i in range(nspec):
        R = spdiags(resdata[i], diags, nwave, nwave)
        convolvedmodel[i] = R.dot(model)


Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2751             int
NAXIS2   11               int
NAXIS3   500              int
CHECKSUM YGfeaGcdSGcdYGcd str  HDU checksum updated 2021-07-08T12:56:17
DATASUM  307167897        str  data unit checksum updated 2021-07-08T12:56:17
======== ================ ==== ==============================================

Data: FITS image [float32, 2751x11x500]

HDU5
----

EXTNAME = FIBERMAP

Fibermap information combining fiberassign request with actual fiber locations. See also the :doc:`fibermap documentation </DESI_SPECTRO_REDUX/SPECPROD/preproc/NIGHT/EXPID/fibermap-EXPID>` page.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============================================================================== ======= ==============================================
KEY      Example Value                                                                  Type    Comment
======== ============================================================================== ======= ==============================================
NAXIS1   361                                                                            int     length of dimension 1
NAXIS2   500                                                                            int     length of dimension 2
TILEID   80818                                                                          int
TILERA   110.36                                                                         float
TILEDEC  78.76                                                                          float
FIELDROT 0.59831423612066                                                               float
FA_PLAN  2022-07-01T00:00:00.000                                                        str
FA_HA    0.0                                                                            float
FA_RUN   2021-02-22T00:00:00                                                            str
REQRA    110.36                                                                         float
REQDEC   78.76                                                                          float
FIELDNUM 0                                                                              int
FA_VER   2.1.1.dev2706                                                                  str
FA_SURV  cmx                                                                            str
GFA      /global/cfs/cdirs/desi/target/catalogs/dr9/0.49.0/gfas                         str
SKY      /global/cfs/cdirs/desi/target/catalogs/dr9/0.49.0/skies                        str
SKYSUPP  /global/cfs/cdirs/desi/target/catalogs/gaiadr2/0.49.0/skies-supp               str
TARG     /global/cfs/cdirs/desi/target/catalogs/gaiadr2/0.49.0/targets/cmx/resolve/supp str
FAFLAVOR dithprec                                                                       str
FAOUTDIR ./20210223/                                                                    str
PMTIME   2021-02-23T00:00:00.000                                                        str
RUNDATE  2021-02-22T00:00:00                                                            str
SEED     77                                                                             int
ISDITH   1                                                                              int
OBSCON   DARK|GRAY|BRIGHT                                                               str
BZERO    32768                                                                          int
BSCALE   1                                                                              int
MODULE   CI                                                                             str
EXPID    77755                                                                          int
EXPFRAME 0                                                                              int
FRAMES   None                                                                           Unknown
COSMSPLT F                                                                              bool
MAXSPLIT 0                                                                              int
SPLITIDS 77755                                                                          str
FIBASSGN /data/tiles/SVN_tiles/080/fiberassign-080818.fits.gz                           str
FLAVOR   science                                                                        str
OBSTYPE  SCIENCE                                                                        str
SEQUENCE DESI                                                                           str
MANIFEST F                                                                              bool
OBJECT                                                                                  str
PURPOSE  SV                                                                             str
PROGRAM  Dither fibermode tile 80818 (110.36, 78.76)                                    str
PROPID   2019B-5000                                                                     str
OBSERVER Antonella Palmese                                                              str
LEAD     Ann Elliott                                                                    str
INSTRUME DESI                                                                           str
OBSERVAT KPNO                                                                           str
OBS-LAT  31.96403                                                                       str
OBS-LONG -111.59989                                                                     str
OBS-ELEV 2097.0                                                                         float
TELESCOP KPNO 4.0-m telescope                                                           str
CORRCTOR DESI Corrector                                                                 str
SEQNUM   1                                                                              int
NIGHT    20210223                                                                       int
SEQSTART 2021-02-24T06:19:10.430069                                                     str
TIMESYS  UTC                                                                            str
DATE-OBS 2021-02-24T06:21:55.370842112                                                  str
TIME-OBS 2021-02-23T06:21:55.370842112                                                  str
MJD-OBS  59269.2652242                                                                  float
OPENSHUT None                                                                           Unknown
CAMSHUT  open                                                                           str
ST       09:12:55.688000                                                                str
ACQTIME  15.0                                                                           float
GUIDTIME 5.0                                                                            float
FOCSTIME 60.0                                                                           float
SKYTIME  60.0                                                                           float
WHITESPT F                                                                              bool
ZENITH   F                                                                              bool
SEANNEX  F                                                                              bool
BEYONDP  F                                                                              bool
FIDUCIAL off                                                                            str
BACKLIT  off                                                                            str
AIRMASS  1.501465                                                                       float
FOCUS    1117.7,-820.8,-60.5,15.2,30.4,201.4                                            str
VCCD     ON                                                                             str
TRUSTEMP 11.7                                                                           float
PMIRTEMP 10.225                                                                         float
PMREADY  T                                                                              bool
PMCOVER  open                                                                           str
PMCOOL   off                                                                            str
DOMSHUTU open                                                                           str
DOMSHUTL open                                                                           str
DOMLIGHH off                                                                            str
DOMLIGHL off                                                                            str
DOMEAZ   347.3                                                                          float
DOMINPOS T                                                                              bool
EPOCH    2000.0                                                                         float
GUIDOFFR -0.300306                                                                      float
GUIDOFFD -0.206036                                                                      float
MOONDEC  24.054124                                                                      float
MOONRA   119.092751                                                                     float
MOONSEP  55.0686276414593                                                               float
MOUNTAZ  353.114997                                                                     float
MOUNTDEC 78.77085                                                                       float
MOUNTEL  41.759267                                                                      float
MOUNTHA  27.3357                                                                        float
INCTRL   T                                                                              bool
INPOS    T                                                                              bool
MNTOFFD  -58.99                                                                         float
MNTOFFR  12.19                                                                          float
PARALLAC 147.87483                                                                      float
SKYDEC   78.77085                                                                       float
SKYRA    110.326029                                                                     float
TARGTDEC 78.77085                                                                       float
TARGTRA  110.326029                                                                     float
TARGTAZ  352.989038                                                                     float
TARGTEL  41.700973                                                                      float
TRGTOFFD 0.0                                                                            float
TRGTOFFR 0.0                                                                            float
ZD       48.299027                                                                      float
TCSST    09:12:55.137                                                                   str
TCSMJD   59269.265649                                                                   float
USEETC   F                                                                              bool
SKYLEVEL 7.943                                                                          float
PMSEEING 0.94                                                                           float
PMTRANS  100.93                                                                         float
ACQCAM   GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                                      str
GUIDECAM GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                                      str
FOCUSCAM FOCUS1,FOCUS4,FOCUS6,FOCUS9                                                    str
SKYCAM   SKYCAM0,SKYCAM1                                                                str
REQADC   109.36,187.96                                                                  str
ADCCORR  T                                                                              bool
ADC1PHI  109.360004                                                                     float
ADC2PHI  187.960003                                                                     float
ADC1HOME F                                                                              bool
ADC2HOME F                                                                              bool
ADC1NREV -1.0                                                                           float
ADC2NREV -1.0                                                                           float
ADC1STAT STOPPED                                                                        str
ADC2STAT STOPPED                                                                        str
USESKY   T                                                                              bool
USEFOCUS T                                                                              bool
HEXPOS   1117.8,-820.8,-61.4,15.2,30.5,219.3                                            str
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                                                        str
USEROTAT T                                                                              bool
ROTOFFST 198.4                                                                          float
ROTENBLD T                                                                              bool
ROTRATE  0.0                                                                            float
RESETROT F                                                                              bool
USEPOS   T                                                                              bool
PETALS   PETAL0,PETAL1,PETAL2,PETAL3,PETAL4,PETAL5,PETAL6,PETAL7,PETAL8,PETAL9          str
POSCYCLE 1                                                                              int
POSONTGT 1540                                                                           int
POSONFRC 0.3704                                                                         float
POSDISAB 823                                                                            int
POSENABL 4158                                                                           int
POSRMS   0.0122                                                                         float
POSITER  1                                                                              int
POSFRACT 0.95                                                                           float
POSTOLER 0.005                                                                          float
POSMVALL T                                                                              bool
USEGUIDR T                                                                              bool
GUIDMODE catalog                                                                        str
USEAOS   F                                                                              bool
USEDONUT T                                                                              bool
USESPCTR T                                                                              bool
SPCGRPHS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                                        str
ILLSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                                        str
CCDSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                                        str
TDEWPNT  -19.54                                                                         float
TAIRFLOW 0.0                                                                            float
TAIRITMP 12.2                                                                           float
TAIROTMP 13.2                                                                           float
TAIRTEMP 10.655                                                                         float
TCASITMP 6.6                                                                            float
TCASOTMP 11.5                                                                           float
TCSITEMP 10.8                                                                           float
TCSOTEMP 11.4                                                                           float
TCIBTEMP 0.0                                                                            float
TCIMTEMP 0.0                                                                            float
TCITTEMP 0.0                                                                            float
TCOSTEMP 0.0                                                                            float
TCOWTEMP 0.0                                                                            float
TDBTEMP  10.5                                                                           float
TFLOWIN  0.0                                                                            float
TFLOWOUT 0.0                                                                            float
TGLYCOLI 12.1                                                                           float
TGLYCOLO 12.0                                                                           float
THINGES  11.6                                                                           float
THINGEW  11.7                                                                           float
TPMAVERT 10.242                                                                         float
TPMDESIT 7.0                                                                            float
TPMEIBT  10.1                                                                           float
TPMEITT  10.0                                                                           float
TPMEOBT  10.3                                                                           float
TPMEOTT  10.3                                                                           float
TPMNIBT  9.7                                                                            float
TPMNITT  10.4                                                                           float
TPMNOBT  10.5                                                                           float
TPMNOTT  10.3                                                                           float
TPMRTDT  10.31                                                                          float
TPMSIBT  10.3                                                                           float
TPMSITT  10.0                                                                           float
TPMSOBT  10.0                                                                           float
TPMSOTT  10.4                                                                           float
TPMSTAT  ready                                                                          str
TPMWIBT  9.9                                                                            float
TPMWITT  10.0                                                                           float
TPMWOBT  10.2                                                                           float
TPMWOTT  10.5                                                                           float
TPCITEMP 10.2                                                                           float
TPCOTEMP 10.2                                                                           float
TPR1HUM  0.0                                                                            float
TPR1TEMP 0.0                                                                            float
TPR2HUM  0.0                                                                            float
TPR2TEMP 0.0                                                                            float
TSERVO   40.0                                                                           float
TTRSTEMP 10.7                                                                           float
TTRWTEMP 11.3                                                                           float
TTRUETBT -4.0                                                                           float
TTRUETTT 10.8                                                                           float
TTRUNTBT 11.1                                                                           float
TTRUNTTT 11.0                                                                           float
TTRUSTBT 11.1                                                                           float
TTRUSTST 10.8                                                                           float
TTRUSTTT 11.1                                                                           float
TTRUTSBT 12.0                                                                           float
TTRUTSMT 12.0                                                                           float
TTRUTSTT 11.0                                                                           float
TTRUWTBT 10.9                                                                           float
TTRUWTTT 11.0                                                                           float
ALARM    F                                                                              bool
ALARM-ON F                                                                              bool
BATTERY  100.0                                                                          float
SECLEFT  6444.0                                                                         float
UPSSTAT  System Normal - On Line(7)                                                     str
INAMPS   71.9                                                                           float
OUTWATTS 5100.0,7300.0,4800.0                                                           str
COMPDEW  -15.0                                                                          float
COMPHUM  5.0                                                                            float
COMPAMB  22.0                                                                           float
COMPTEMP 28.4                                                                           float
DEWPOINT 19.3                                                                           float
HUMIDITY 89.0                                                                           float
PRESSURE 795.0                                                                          float
OUTTEMP  21.2                                                                           float
WINDDIR  323.0                                                                          float
WINDSPD  14.7                                                                           float
GUST     14.7                                                                           float
AMNIENTN 15.9                                                                           float
CFLOOR   10.5                                                                           float
NWALLIN  16.3                                                                           float
NWALLOUT 9.9                                                                            float
WWALLIN  16.4                                                                           float
WWALLOUT 11.3                                                                           float
AMBIENTS 17.2                                                                           float
FLOOR    14.6                                                                           float
EWALLCMP 11.6                                                                           float
EWALLCOU 11.3                                                                           float
ROOF     10.6                                                                           float
ROOFAMB  11.1                                                                           float
DOMEBLOW -99.9                                                                          float
DOMEBUP  -99.9                                                                          float
DOMELLOW -99.9                                                                          float
DOMELUP  -99.9                                                                          float
DOMERLOW -99.9                                                                          float
DOMERUP  -99.9                                                                          float
PLATFORM -99.9                                                                          float
SHACKC   17.3                                                                           float
SHACKW   16.9                                                                           float
STAIRSL  -99.9                                                                          float
STAIRSM  -99.9                                                                          float
STAIRSU  -99.9                                                                          float
TELBASE  10.8                                                                           float
UTILWALL 11.0                                                                           float
UTILROOM 11.1                                                                           float
SP0NIRT  139.99                                                                         float
SP0REDT  139.99                                                                         float
SP0BLUT  162.97                                                                         float
SP0NIRP  8.249e-08                                                                      float
SP0REDP  6.155e-08                                                                      float
SP0BLUP  8.905e-08                                                                      float
SP1NIRT  139.99                                                                         float
SP1REDT  139.99                                                                         float
SP1BLUT  162.97                                                                         float
SP1NIRP  4.38e-08                                                                       float
SP1REDP  5.379e-08                                                                      float
SP1BLUP  8.005e-08                                                                      float
SP2NIRT  139.99                                                                         float
SP2REDT  139.99                                                                         float
SP2BLUT  163.02                                                                         float
SP2NIRP  8.556e-08                                                                      float
SP2REDP  8.642e-08                                                                      float
SP2BLUP  7.737e-08                                                                      float
SP3NIRT  139.99                                                                         float
SP3REDT  139.96                                                                         float
SP3BLUT  162.99                                                                         float
SP3NIRP  3.824e-08                                                                      float
SP3REDP  6.739e-08                                                                      float
SP3BLUP  9.329e-08                                                                      float
SP4NIRT  139.99                                                                         float
SP4REDT  140.06                                                                         float
SP4BLUT  163.04                                                                         float
SP4NIRP  6.3e-08                                                                        float
SP4REDP  4.941e-08                                                                      float
SP4BLUP  5.325e-08                                                                      float
SP5NIRT  139.99                                                                         float
SP5REDT  139.99                                                                         float
SP5BLUT  163.02                                                                         float
SP5NIRP  6.881e-08                                                                      float
SP5REDP  6.584e-08                                                                      float
SP5BLUP  1.101e-07                                                                      float
SP6NIRT  139.99                                                                         float
SP6REDT  139.99                                                                         float
SP6BLUT  162.97                                                                         float
SP6NIRP  2.809e-07                                                                      float
SP6REDP  6.053e-08                                                                      float
SP6BLUP  7.54e-08                                                                       float
SP7NIRT  139.99                                                                         float
SP7REDT  139.99                                                                         float
SP7BLUT  162.97                                                                         float
SP7NIRP  7.49e-08                                                                       float
SP7REDP  4.383e-08                                                                      float
SP7BLUP  1.018e-07                                                                      float
SP8NIRT  139.99                                                                         float
SP8REDT  139.99                                                                         float
SP8BLUT  162.97                                                                         float
SP8NIRP  3.843e-08                                                                      float
SP8REDP  5.37e-08                                                                       float
SP8BLUP  8.29699999999999e-08                                                           float
SP9NIRT  140.03                                                                         float
SP9REDT  140.01                                                                         float
SP9BLUT  163.02                                                                         float
SP9NIRP  5.706e-08                                                                      float
SP9REDP  6.875e-08                                                                      float
SP9BLUP  1.206e-07                                                                      float
RADESYS  FK5                                                                            str
TNFSPROC 8.6995                                                                         float
TGFAPROC 9.835                                                                          float
SIMGFAP  F                                                                              bool
USEFVC   T                                                                              bool
USEFID   T                                                                              bool
USEILLUM T                                                                              bool
USEXSRVR T                                                                              bool
USEOPENL T                                                                              bool
STOPGUDR T                                                                              bool
STOPFOCS T                                                                              bool
STOPSKY  T                                                                              bool
KEEPGUDR F                                                                              bool
KEEPFOCS F                                                                              bool
KEEPSKY  F                                                                              bool
REACQUIR F                                                                              bool
FILENAME /exposures/desi/20210223/00077755/desi-00077755.fits.fz                        str
EXCLUDED                                                                                str
DOSVER   trunk                                                                          str
OCSVER   1.2                                                                            float
CONSTVER DESI:CURRENT                                                                   str
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini                               str
REQTIME  180.0                                                                          float
FVCTIME  2.0                                                                            float
SIMGFACQ F                                                                              bool
TCSKRA   0.3 0.003 0.00003                                                              str
TCSKDEC  0.3 0.003 0.00003                                                              str
TCSGRA   0.3                                                                            float
TCSGDEC  0.3                                                                            float
TCSMFRA  1                                                                              int
TCSMFDEC 1                                                                              int
TCSPIRA  1.0,0.0,0.0,0.0                                                                str
TCSPIDEC 1.0,0.0,0.0,0.0                                                                str
POSCNVGD F                                                                              bool
GUIEXPID 77755                                                                          int
IGFRMNUM 10                                                                             int
FOCEXPID 77755                                                                          int
IFFRMNUM 1                                                                              int
SKYEXPID 77755                                                                          int
ISFRMNUM 1                                                                              int
FGFRMNUM 30                                                                             int
FFFRMNUM 4                                                                              int
FSFRMNUM 3                                                                              int
DELTARA  None                                                                           Unknown
DELTADEC None                                                                           Unknown
GSGUIDE0 (518.32,619.56),(973.72,1900.42)                                               str
GSGUIDE2 (891.16,1654.11),(46.08,618.78)                                                str
GSGUIDE3 (714.10,1774.21),(47.68,502.24)                                                str
GSGUIDE5 (287.66,1594.95),(93.01,1750.07)                                               str
GSGUIDE7 (485.09,511.45),(653.67,1607.58)                                               str
GSGUIDE8 (896.83,1786.83),(281.85,267.54)                                               str
ARCHIVE  /exposures/desi/20210223/00077755/guide-00077755.fits.fz                       str
GUIDEFIL guide-00077755.fits.fz                                                         str
COORDFIL coordinates-00077755.fits                                                      str
EXPTIME  180.034                                                                        float
VCCDON   2021-02-12T20:17:35.596905                                                     str
VCCDSEC  986896.6                                                                       float
SPECGRPH 7                                                                              int
SPECID   8                                                                              int
FEEBOX   lbnl067                                                                        str
VESSEL   25                                                                             int
FEEVER   v20160312                                                                      str
FEEPOWER ON                                                                             str
FEEDMASK 2134851391                                                                     int
FEECMASK 1048575                                                                        int
CCDTEMP  850.0                                                                          float
DAC14    0.0,0.7072                                                                     str
DAC6     0.0,-0.0368                                                                    str
DAC11    26.9998,26.7268                                                                str
BIASSECC [2053:2116, 2114:4161]                                                         str
DAC15    19.9997,19.8848                                                                str
DAC5     0.0,-0.0368                                                                    str
CASETEMP 58.3376                                                                        float
AMPSECB  [2049:4096, 2048:1]                                                            str
DAC8     26.9998,26.5784                                                                str
OFFSET3  -1.5,15.8723                                                                   str
DAC9     26.9998,26.3707                                                                str
OFFSET0  -1.5,15.8002                                                                   str
SETTINGS detectors_sm_20210128.json                                                     str
DAC13    -5.0006,-5.0544                                                                str
CLOCK13  3.0,-7.0002                                                                    str
PRESECA  [1:4, 2:2049]                                                                  str
BLDTIME  0.3548                                                                         float
CLOCK8   3.0,-7.0002                                                                    str
ORSECD   [2181:4228, 2082:2113]                                                         str
DAC1     15.9998,15.7899                                                                str
PRRSECA  [5:2052, 1:1]                                                                  str
ORSECB   [2181:4228, 2050:2081]                                                         str
DATASECA [5:2052, 2:2049]                                                               str
DAC3     15.9998,15.862                                                                 str
OFFSET7  -1.100000023841858,-0.0368                                                     str
CRYOTEMP 162.97                                                                         float
TRIMSECC [5:2052, 2114:4161]                                                            str
CPUTEMP  58.1015                                                                        float
TRIMSECB [2181:4228, 2:2049]                                                            str
DETSECD  [2049:4096, 2049:4096]                                                         str
CLOCK1   3.9999,-4.0002                                                                 str
CLOCK5   3.9999,-4.0002                                                                 str
OFFSET2  -1.5,15.8414                                                                   str
CLOCK2   3.9999,-4.0002                                                                 str
DAC16    0.0,63.525                                                                     str
CCDSECD  [2049:4096, 2049:4096]                                                         str
PRESECC  [1:4, 2114:4161]                                                               str
PRRSECC  [5:2052, 4162:4162]                                                            str
DETSECA  [1:2048, 1:2048]                                                               str
DATASECC [5:2052, 2114:4161]                                                            str
DAC17    -0.0,0.0854                                                                    str
OFFSET1  -1.5,15.7899                                                                   str
CLOCK18  3.9999,-4.0002                                                                 str
DAC7     0.0,-0.0316                                                                    str
CLOCK12  3.0,-7.0002                                                                    str
CCDTMING flatdark_sta_timing.txt                                                        str
TRIMSECA [5:2052, 2:2049]                                                               str
PGAGAIN  5                                                                              int
PRESECB  [4229:4232, 2:2049]                                                            str
AMPSECC  [2048:1, 2049:4096]                                                            str
DAC12    4.9997,5.0544                                                                  str
DATASECD [2181:4228, 2114:4161]                                                         str
DATASECB [2181:4228, 2:2049]                                                            str
CCDSECC  [1:2048, 2049:4096]                                                            str
CLOCK4   3.9999,-4.0002                                                                 str
OFFSET4  -1.100000023841858,-0.0263                                                     str
CLOCK11  0.0,0.0                                                                        str
CRYOPRES 1.017e-07                                                                      str
DETSECB  [2049:4096, 1:2048]                                                            str
OFFSET6  -1.100000023841858,-0.0368                                                     str
CCDPREP  purge,clear                                                                    str
ORSECA   [5:2052, 2050:2081]                                                            str
DETECTOR sn22829                                                                        str
BIASSECD [2117:2180, 2114:4161]                                                         str
CLOCK16  0.0,0.0                                                                        str
CLOCK15  0.0,0.0                                                                        str
DIGITIME 54.7765                                                                        float
CCDNAME  CCDSM8B                                                                        str
CDSPARMS 400, 400, 8, 1000                                                              str
DETSECC  [1:2048, 2049:4096]                                                            str
PRRSECD  [2181:4228, 4162:4162]                                                         str
CLOCK17  3.9999,-4.0002                                                                 str
BIASSECB [2117:2180, 2:2049]                                                            str
AMPSECA  [1:2048, 1:2048]                                                               str
DAC4     0.0,-0.021                                                                     str
CCDSECA  [1:2048, 1:2048]                                                               str
CLOCK14  3.0,-7.0002                                                                    str
CAMERA   b7                                                                             str
CLOCK3   6.9999,-2.0001                                                                 str
PRESECD  [4229:4232, 2114:4161]                                                         str
PRRSECB  [2181:4228, 1:1]                                                               str
CCDSIZE  4162,4232                                                                      str
CLOCK6   3.9999,-4.0002                                                                 str
BIASSECA [2053:2116, 2:2049]                                                            str
ORSECC   [5:2052, 2082:2113]                                                            str
DAC2     15.9998,15.8311                                                                str
AMPSECD  [4096:2049, 4096:2049]                                                         str
OFFSET5  -1.100000023841858,-0.0316                                                     str
DAC0     15.9998,15.8002                                                                str
DAC10    26.9998,26.1332                                                                str
TRIMSECD [2181:4228, 2114:4161]                                                         str
CLOCK0   3.9999,-4.0002                                                                 str
CLOCK9   3.0,-7.0002                                                                    str
CCDSECB  [2049:4096, 1:2048]                                                            str
DELAYS   13, 13, 25, 25, 8, 3000, 7, 7, 400, 7                                          str
CLOCK7   6.9999,-2.0001                                                                 str
CCDCFG   default_sta_20210128.cfg                                                       str
CLOCK10  3.0,-7.0002                                                                    str
OBSID    kp4m20210224t062155                                                            str
PROCTYPE RAW                                                                            str
PRODTYPE image                                                                          str
GAINA    1.117                                                                          float
SATULEVA 63500.0                                                                        float
OVERSCNA 1195.794247115305                                                              float
OBSRDNA  3.032856327436087                                                              float
SATUELEA 69593.7978259722                                                               float
GAINB    1.117                                                                          float
SATULEVB 63700.0                                                                        float
OVERSCNB 1188.874709766999                                                              float
OBSRDNB  2.834090558391209                                                              float
SATUELEB 69824.92694919027                                                              float
GAINC    1.127                                                                          float
SATULEVC 59000.0                                                                        float
OVERSCNC 1193.463564006085                                                              float
OBSRDNC  2.929996330132565                                                              float
SATUELEC 65147.96656336514                                                              float
GAIND    1.128                                                                          float
SATULEVD 63600.0                                                                        float
OVERSCND 1176.893356381423                                                              float
OBSRDND  2.792311084921087                                                              float
SATUELED 70413.26429400175                                                              float
FIBERMIN 3500                                                                           int
CHECKSUM a3R3c2O2a2O2a2O2                                                               str     HDU checksum updated 2021-07-08T12:56:17
DATASUM  605678013                                                                      str     data unit checksum updated 2021-07-08T12:56:17
ENCODING ascii                                                                          str
======== ============================================================================== ======= ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

===================== ======= ===== ===========
Name                  Type    Units Description
===================== ======= ===== ===========
TARGETID              int64         Unique target ID
PETAL_LOC             int16         Focal plane petal location 0-9
DEVICE_LOC            int32         Device location 0-5xx
LOCATION              int64         1000*PETAL_LOC + DEVICE_LOC
FIBER                 int32         Fiber number 0-4999
FIBERSTATUS           int32         Fiber status mask; 0=good
TARGET_RA             float64
TARGET_DEC            float64
PMRA                  float32
PMDEC                 float32
REF_EPOCH             float32
LAMBDA_REF            float32
FA_TARGET             int64
FA_TYPE               binary
OBJTYPE               char[3]
FIBERASSIGN_X         float32
FIBERASSIGN_Y         float32
PRIORITY              int32
SUBPRIORITY           float64
OBSCONDITIONS         int32
RELEASE               int16
BRICKID               int32
BRICK_OBJID           int32
MORPHTYPE             char[4]
FLUX_G                float32
FLUX_R                float32
FLUX_Z                float32
FLUX_IVAR_G           float32
FLUX_IVAR_R           float32
FLUX_IVAR_Z           float32
MASKBITS              int16
REF_ID                int64
REF_CAT               char[2]
GAIA_PHOT_G_MEAN_MAG  float32
GAIA_PHOT_BP_MEAN_MAG float32
GAIA_PHOT_RP_MEAN_MAG float32
PARALLAX              float32
BRICKNAME             char[8]
EBV                   float32
FLUX_W1               float32
FLUX_W2               float32
FLUX_IVAR_W1          float32
FLUX_IVAR_W2          float32
FIBERFLUX_G           float32
FIBERFLUX_R           float32
FIBERFLUX_Z           float32
FIBERTOTFLUX_G        float32
FIBERTOTFLUX_R        float32
FIBERTOTFLUX_Z        float32
SERSIC                float32
SHAPE_R               float32
SHAPE_E1              float32
SHAPE_E2              float32
PHOTSYS               char[1]
PRIORITY_INIT         int64
NUMOBS_INIT           int64
CMX_TARGET            int64
DESI_TARGET           int64
BGS_TARGET            int64
MWS_TARGET            int64
PLATE_RA              float64
PLATE_DEC             float64
NUM_ITER              int64
FIBER_X               float64
FIBER_Y               float64
DELTA_X               float64
DELTA_Y               float64
FIBER_RA              float64
FIBER_DEC             float64
EXPTIME               float64
===================== ======= ===== ===========

HDU6
----

EXTNAME = CHI2PIX

:math:`\chi^2` of PSF fit to CCD pixels per spectrum wavelength bin.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2751             int  Number of wavelengths
NAXIS2   500              int  Number of spectra
CHECKSUM SCE8VAB5SAB5SAB5 str  HDU checksum updated 2021-07-08T12:56:18
DATASUM  3693165584       str  data unit checksum updated 2021-07-08T12:56:18
======== ================ ==== ==============================================

Data: FITS image [float32, 2751x500]


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
