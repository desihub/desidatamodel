===========================
fiberflatnight-CAMERA-NIGHT
===========================

:Summary: Relative fiber-to-fiber variations ("fiberflat") as measured by
    continuum lamp calibration spectra, combined across multiple exposures.
    Corrected flux = original flux / fiberflat.
:Naming Convention: ``fiberflatnight-CAMERA-NIGHT.fits``, where ``CAMERA`` is
    *e.g.*, "b0", "r5", etc. and ``NIGHT`` is the observation night in
    YYYYMMDD format.
:Regex: ``fiberflatnight-[brz][0-9]-[0-9]{8}.fits``
:File Type: FITS, 10 MB

Contents
========

====== ========== ======== =================================
Number EXTNAME    Type     Contents
====== ========== ======== =================================
HDU0_  FIBERFLAT  IMAGE    Relative fiber-to-fiber variation
HDU1_  IVAR       IMAGE    Inverse variance of fiberflat
HDU2_  MASK       IMAGE    Mask of fiberflat (0=good)
HDU3_  MEANSPEC   IMAGE    Average spectrum
HDU4_  WAVELENGTH IMAGE    Wavelength
HDU5_  FIBERMAP   BINTABLE fibermap
====== ========== ======== =================================


FITS Header Units
=================

HDU0
----

EXTNAME = FIBERFLAT

Relative fiber-to-fiber variation.  Corrected flux = original flux / fiberflat.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============================================================ ======= ====================================================
KEY      Example Value                                                Type    Comment
======== ============================================================ ======= ====================================================
NAXIS1   2751                                                         int     Number of wavelengths
NAXIS2   500                                                          int     Number of spectra (fibers)
EXPID    68416                                                        int     Exposure number
EXPFRAME 0                                                            int     Frame number
FLAVOR   science                                                      str     Observation type
SEQUENCE Spectrographs                                                str     OCS Sequence name
PURPOSE  Commissioning                                                str     Purpose of observing night
PROGRAM  CALIB DESI-CALIB-00 LEDs only                                str     Program name
PROPID   2019B-5000                                                   str     Proposal ID
OBSERVER DESIObserver                                                 str     Names of observers
LEAD     RunManager                                                   str     Lead observer
INSTRUME DESI                                                         str     Instrument name
OBSERVAT KPNO                                                         str     Observatory name
OBS-LAT  31.96403                                                     str     [deg] Observatory latitude
OBS-LONG -111.59989                                                   str     [deg] Observatory east longitude
OBS-ELEV 2097.0                                                       float   [m] Observatory elevation
TELESCOP KPNO 4.0-m telescope                                         str     Telescope name
CORRCTOR DESI Corrector                                               str     Corrector Identification
NIGHT    20201217                                                     int     Observing night
TIMESYS  UTC                                                          str     Time system used for date-obs
DATE-OBS 2020-12-18T00:44:24.185428                                   str     [UTC] Observation data and start time
TIME-OBS 00:44:24.185428                                              str     [UTC] Observation start time
MJD-OBS  59201.03083548                                               float   Modified Julian Date of observation
ST       23:06:23.210                                                 str     Local Sidereal time at observation start (HH:MM
EXPTIME  120.029                                                      float   [s] Actual exposure time
DELTARA  0.0                                                          float   [arcsec] Offset], right ascension, observer inp
DELTADEC 0.0                                                          float   [arcsec] Offset], declination, observer input
VCCD     ON                                                           str     True (ON) if CCD voltage is on
VCCDON   2020-12-15T23:53:35.750066                                   str     Time when CCD voltage was turned on
VCCDSEC  176016.5                                                     float   [s] CCD on time in seconds
EPOCH    2000.0                                                       float   Epoch of observation
SPECGRPH 7                                                            int     Spectrograph logical name (SP)
SPECID   8                                                            int     Spectrograph serial number (SM)
FEEBOX   lbnl067                                                      str     CCD Controller serial number
VESSEL   25                                                           int     Cryostat serial number
FEEVER   v20160312                                                    str     CCD Controller version
FEEPOWER ON                                                           str     FEE power status
FEEDMASK 2134851391                                                   int     FEE dac mask
FEECMASK 1048575                                                      int     FEE clk mask
CCDTEMP  850.0                                                        float   [deg C] CCD controller CCD temperature
RADESYS  FK5                                                          str     Coordinate reference frame of major/minor axes
FILENAME /exposures/desi/specs/20201217/00068416/sp5-00068416.fits.fz str     Name
DOSVER   trunk                                                        str     DOS software version
OCSVER   1.2                                                          float   OCS software version
CONSTVER DESI:CURRENT                                                 str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini             str     DOS Configuration
ORSECB   [2181:4228, 2050:2081]                                       str     Row overscan section for quadrant B
PRRSECD  [2181:4228, 4162:4162]                                       str     Row prescan section for quadrant D
ORSECA   [5:2052, 2050:2081]                                          str     Row overscan section for quadrant A
DAC13    -5.0006,-5.044                                               str     [V] set value, measured value
PRESECB  [4229:4232, 2:2049]                                          str     Prescan section for quadrant B
CCDTMING default_sta_timing_20180905.txt                              str     CCD timing file
ORSECD   [2181:4228, 2082:2113]                                       str     Row bias section for quadrant D
DAC5     0.0,-0.0316                                                  str     [V] set value, measured value
CCDPREP  purge,clear                                                  str     CCD prep actions
BIASSECC [2053:2116, 2114:4161]                                       str     Bias section for quadrant C
DATASECB [2181:4228, 2:2049]                                          str     Data section for quadrant B
DETSECC  [1:2048, 2049:4096]                                          str     Detector section for quadrant C
CCDSECB  [2049:4096, 1:2048]                                          str     CCD section for quadrant B
AMPSECB  [2049:4096, 2048:1]                                          str     AMP section for quadrant B
OFFSET2  -1.5,15.8414                                                 str     [V] set value, measured value
ORSECC   [5:2052, 2082:2113]                                          str     Row overscan section for quadrant C
OFFSET5  -1.100000023841858,-0.0316                                   str     [V] set value, measured value
CDSPARMS 400, 400, 8, 1000                                            str     CDS parameters
CCDSECC  [1:2048, 2049:4096]                                          str     CCD section for quadrant C
BIASSECD [2117:2180, 2114:4161]                                       str     Bias section for quadrant D
DETSECD  [2049:4096, 2049:4096]                                       str     Detector section for quadrant D
CLOCK9   3.0,-7.0002                                                  str     [V] high rail, low rail
DATASECA [5:2052, 2:2049]                                             str     Data section for quadrant A
DIGITIME 46.0639                                                      float   [s] Time to digitize image
PRESECC  [1:4, 2114:4161]                                             str     Prescan section for quadrant C
DAC17    -0.0,0.0122                                                  str     [V] set value, measured value
BIASSECB [2117:2180, 2:2049]                                          str     Bias section for quadrant B
CLOCK1   3.9999,-4.0002                                               str     [V] high rail, low rail
PRRSECB  [2181:4228, 1:1]                                             str     Row prescan section for quadrant B
CCDSECA  [1:2048, 1:2048]                                             str     CCD section for quadrant A
CCDSIZE  4162,4232                                                    str     CCD size in pixels (rows, columns)
DETECTOR sn22829                                                      str     Detector (ccd) identification
CLOCK14  3.0,-7.0002                                                  str     [V] high rail, low rail
DAC8     26.9998,26.5933                                              str     [V] set value, measured value
DAC15    19.9997,19.8848                                              str     [V] set value, measured value
CCDNAME  CCDSM8B                                                      str     CCD name
DAC1     15.9998,15.7899                                              str     [V] set value, measured value
CRYOTEMP 163.02                                                       float   [deg K] Cryostat CCD temperature
TRIMSECD [2181:4228, 2114:4161]                                       str     Trim section for quadrant D
CLOCK12  3.0,-7.0002                                                  str     [V] high rail, low rail
CLOCK17  3.9999,-4.0002                                               str     [V] high rail, low rail
DAC11    26.9998,26.6972                                              str     [V] set value, measured value
DAC12    4.9997,5.0544                                                str     [V] set value, measured value
OFFSET3  -1.5,15.8723                                                 str     [V] set value, measured value
CLOCK2   3.9999,-4.0002                                               str     [V] high rail, low rail
PRESECD  [4229:4232, 2114:4161]                                       str     Prescan section for quadrant D
PGAGAIN  5                                                            int     Controller gain
BIASSECA [2053:2116, 2:2049]                                          str     Bias section for quadrant A
CLOCK5   3.9999,-4.0002                                               str     [V] high rail, low rail
CLOCK15  0.0,0.0                                                      str     [V] high rail, low rail
CLOCK16  0.0,0.0                                                      str     [V] high rail, low rail
PRRSECA  [5:2052, 1:1]                                                str     Row prescan section for quadrant A
DATASECD [2181:4228, 2114:4161]                                       str     Data section for quadrant D
DELAYS   13, 13, 25, 25, 8, 3000, 7, 7, 7, 7                          str     [10] Delay settings
PRRSECC  [5:2052, 4162:4162]                                          str     Row prescan section for quadrant C
CRYOPRES 1.852e-07                                                    str     [mb] Cryostat pressure (IP)
CLOCK7   6.9999,-2.0001                                               str     [V] high rail, low rail
DAC14    0.0,0.7072                                                   str     [V] set value, measured value
CLOCK13  3.0,-7.0002                                                  str     [V] high rail, low rail
AMPSECA  [1:2048, 1:2048]                                             str     AMP section for quadrant A
OFFSET1  -1.5,15.7899                                                 str     [V] set value, measured value
CCDCFG   default_sta_20190717.cfg                                     str     CCD configuration file
SETTINGS detectors_sm_20191211.json                                   str     Name of DESI CCD settings file
OFFSET7  -1.100000023841858,-0.0368                                   str     [V] set value, measured value
PRESECA  [1:4, 2:2049]                                                str     Prescan section for quadrant A
CCDSECD  [2049:4096, 2049:4096]                                       str     CCD section for quadrant D
CLOCK18  3.9999,-4.0002                                               str     [V] high rail, low rail
TRIMSECC [5:2052, 2114:4161]                                          str     Trim section for quadrant C
DAC7     0.0,-0.0316                                                  str     [V] set value, measured value
DAC0     15.9998,15.8002                                              str     [V] set value, measured value
CLOCK4   3.9999,-4.0002                                               str     [V] high rail, low rail
CPUTEMP  58.5937                                                      float   [deg C] CCD controller CPU temperature
DAC10    26.9998,26.1332                                              str     [V] set value, measured value
AMPSECC  [2048:1, 2049:4096]                                          str     AMP section for quadrant C
DAC9     26.9998,26.4004                                              str     [V] set value, measured value
DATASECC [5:2052, 2114:4161]                                          str     Data section for quadrant C
AMPSECD  [4096:2049, 4096:2049]                                       str     AMP section for quadrant D
CLOCK6   3.9999,-4.0002                                               str     [V] high rail, low rail
DAC4     0.0,-0.0263                                                  str     [V] set value, measured value
OFFSET0  -1.5,15.8002                                                 str     [V] set value, measured value
CASETEMP 58.2146                                                      float   [deg C] CCD controller case temperature
CLOCK8   3.0,-7.0002                                                  str     [V] high rail, low rail
DAC6     0.0,-0.0316                                                  str     [V] set value, measured value
DETSECB  [2049:4096, 1:2048]                                          str     Detector section for quadrant B
CLOCK10  3.0,-7.0002                                                  str     [V] high rail, low rail
TRIMSECB [2181:4228, 2:2049]                                          str     Trim section for quadrant B
DAC16    0.0,65.142                                                   str     [V] set value, measured value
DETSECA  [1:2048, 1:2048]                                             str     Detector section for quadrant A
CLOCK3   6.9999,-2.0001                                               str     [V] high rail, low rail
OFFSET6  -1.100000023841858,-0.0316                                   str     [V] set value, measured value
CLOCK11  0.0,0.0                                                      str     [V] high rail, low rail
DAC3     15.9998,15.8826                                              str     [V] set value, measured value
BLDTIME  0.3523                                                       float   [s] Time to build image
DAC2     15.9998,15.8311                                              str     [V] set value, measured value
OFFSET4  -1.100000023841858,-0.0263                                   str     [V] set value, measured value
CLOCK0   3.9999,-4.0002                                               str     [V] high rail, low rail
TRIMSECA [5:2052, 2:2049]                                             str     Trim section for quadrant A
CAMERA   b7                                                           str     Camera name
REQTIME  120.0                                                        float   [s] Requested exposure time
OBSID    kp4m20201218t004424                                          str     Unique observation identifier
PROCTYPE RAW                                                          str     Data processing level
PRODTYPE image                                                        str     Data product type
CHECKSUM ianalXnWianaiUnW                                             str     HDU checksum updated 2021-07-07T19:21:57
DATASUM  2160869451                                                   str     data unit checksum updated 2021-07-07T19:21:57
GAINA    1.117                                                        float   e/ADU (gain applied to image)
SATULEVA 63500.0                                                      float   saturation or non lin. level, in ADU, inc. bias
OVERSCNA 1206.913359078118                                            float   ADUs (gain not applied)
OBSRDNA  3.558675535780629                                            float   electrons (gain is applied)
SATUELEA 69581.37777790974                                            float   saturation or non lin. level, in electrons
GAINB    1.117                                                        float   e/ADU (gain applied to image)
SATULEVB 63700.0                                                      float   saturation or non lin. level, in ADU, inc. bias
OVERSCNB 1189.350157243735                                            float   ADUs (gain not applied)
OBSRDNB  3.332108295076806                                            float   electrons (gain is applied)
SATUELEB 69824.39587435874                                            float   saturation or non lin. level, in electrons
GAINC    1.127                                                        float   e/ADU (gain applied to image)
SATULEVC 59000.0                                                      float   saturation or non lin. level, in ADU, inc. bias
OVERSCNC 1194.034420281418                                            float   ADUs (gain not applied)
OBSRDNC  3.456268545961142                                            float   electrons (gain is applied)
SATUELEC 65147.32320834284                                            float   saturation or non lin. level, in electrons
GAIND    1.128                                                        float   e/ADU (gain applied to image)
SATULEVD 63600.0                                                      float   saturation or non lin. level, in ADU, inc. bias
OVERSCND 1177.285142184498                                            float   ADUs (gain not applied)
OBSRDND  3.211424022833966                                            float   electrons (gain is applied)
SATUELED 70412.82235961588                                            float   saturation or non lin. level, in electrons
FIBERMIN 3500                                                         int
MODULE   CI                                                           str
FRAMES   None                                                         Unknown
COSMSPLT F                                                            bool
MAXSPLIT 0                                                            int
SPLITIDS 68416                                                        str
OBSTYPE  FLAT                                                         str
MANIFEST F                                                            bool
OBJECT                                                                str
SEQID    3 requests                                                   str
SEQNUM   1                                                            int
SEQTOT   3                                                            int
OPENSHUT None                                                         Unknown
CAMSHUT  open                                                         str
WHITESPT T                                                            bool
ZENITH   F                                                            bool
SEANNEX  F                                                            bool
BEYONDP  F                                                            bool
FIDUCIAL off                                                          str
AIRMASS  1.521296                                                     float
FOCUS    1291.2,-246.0,316.0,-18.0,30.8,-0.0                          str
TRUSTEMP 10.933                                                       float
PMIRTEMP 6.7                                                          float
PMREADY  F                                                            bool
PMCOVER  open                                                         str
PMCOOL   off                                                          str
DOMSHUTU not open                                                     str
DOMSHUTL not open                                                     str
DOMLIGHH off                                                          str
DOMLIGHL off                                                          str
DOMEAZ   254.002                                                      float
DOMINPOS F                                                            bool
GUIDOFFR 0.0                                                          float
GUIDOFFD -0.0                                                         float
MOONDEC  -21.646472                                                   float
MOONRA   313.696312                                                   float
MOUNTAZ  73.495042                                                    float
MOUNTDEC 31.962096                                                    float
MOUNTEL  41.036117                                                    float
MOUNTHA  -58.478889                                                   float
INCTRL   F                                                            bool
INPOS    T                                                            bool
MNTOFFD  -0.0                                                         float
MNTOFFR  -0.0                                                         float
PARALLAC -73.492507                                                   float
SKYDEC   31.962096                                                    float
SKYRA    45.073018                                                    float
TARGTDEC 31.9633                                                      float
TARGTRA  20.027418                                                    float
TARGTAZ  80.966266                                                    float
TARGTEL  61.751074                                                    float
TRGTOFFD 0.0                                                          float
TRGTOFFR 0.0                                                          float
ZD       48.963883                                                    float
TCSST    23:06:22.591                                                 str
TCSMJD   59201.031265                                                 float
ADCCORR  F                                                            bool
ADC1PHI  6.00999300000001                                             float
ADC2PHI  47.240166                                                    float
ADC1HOME F                                                            bool
ADC2HOME F                                                            bool
ADC1NREV -1.0                                                         float
ADC2NREV 0.0                                                          float
ADC1STAT STOPPED                                                      str
ADC2STAT STOPPED                                                      str
HEXPOS   1291.2,-246.0,316.0,-18.0,30.8,-0.0                          str
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                                      str
ROTOFFST 0.0                                                          float
ROTENBLD F                                                            bool
ROTRATE  0.0                                                          float
RESETROT F                                                            bool
GUIDMODE catalog                                                      str
USEAOS   F                                                            bool
SPCGRPHS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                      str
ILLSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                      str
CCDSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                      str
TDEWPNT  -13.417                                                      float
TAIRFLOW 0.0                                                          float
TAIRITMP 10.0                                                         float
TAIROTMP 10.1                                                         float
TAIRTEMP 9.29                                                         float
TCASITMP 0.0                                                          float
TCASOTMP 8.8                                                          float
TCSITEMP 6.8                                                          float
TCSOTEMP 9.0                                                          float
TCIBTEMP 0.0                                                          float
TCIMTEMP 0.0                                                          float
TCITTEMP 0.0                                                          float
TCOSTEMP 0.0                                                          float
TCOWTEMP 0.0                                                          float
TDBTEMP  6.7                                                          float
TFLOWIN  0.0                                                          float
TFLOWOUT 0.0                                                          float
TGLYCOLI 7.9                                                          float
TGLYCOLO 8.6                                                          float
THINGES  10.5                                                         float
THINGEW  9.8                                                          float
TPMAVERT 6.668                                                        float
TPMDESIT 5.0                                                          float
TPMEIBT  6.1                                                          float
TPMEITT  6.2                                                          float
TPMEOBT  6.2                                                          float
TPMEOTT  6.2                                                          float
TPMNIBT  6.4                                                          float
TPMNITT  6.4                                                          float
TPMNOBT  7.1                                                          float
TPMNOTT  7.4                                                          float
TPMRTDT  6.07                                                         float
TPMSIBT  6.3                                                          float
TPMSITT  6.7                                                          float
TPMSOBT  6.4                                                          float
TPMSOTT  6.9                                                          float
TPMSTAT  soft air                                                     str
TPMWIBT  6.3                                                          float
TPMWITT  6.5                                                          float
TPMWOBT  6.7                                                          float
TPMWOTT  7.3                                                          float
TPCITEMP 6.6                                                          float
TPCOTEMP 6.6                                                          float
TPR1HUM  0.0                                                          float
TPR1TEMP 0.0                                                          float
TPR2HUM  0.0                                                          float
TPR2TEMP 0.0                                                          float
TSERVO   40.0                                                         float
TTRSTEMP 10.3                                                         float
TTRWTEMP 10.2                                                         float
TTRUETBT -5.5                                                         float
TTRUETTT 10.7                                                         float
TTRUNTBT 10.1                                                         float
TTRUNTTT 10.9                                                         float
TTRUSTBT 10.2                                                         float
TTRUSTST 10.8                                                         float
TTRUSTTT 10.8                                                         float
TTRUTSBT 10.7                                                         float
TTRUTSMT 10.7                                                         float
TTRUTSTT 11.4                                                         float
TTRUWTBT 10.1                                                         float
TTRUWTTT 11.0                                                         float
ALARM    F                                                            bool
ALARM-ON F                                                            bool
BATTERY  100.0                                                        float
SECLEFT  5238.0                                                       float
UPSSTAT  System Normal - On Line(7)                                   str
INAMPS   69.6                                                         float
OUTWATTS 4500.0,7500.0,4800.0                                         str
COMPDEW  -9.1                                                         float
COMPHUM  10.3                                                         float
COMPAMB  18.8                                                         float
COMPTEMP 24.1                                                         float
DEWPOINT 10.7                                                         float
HUMIDITY 13.0                                                         float
PRESSURE 795.0                                                        float
OUTTEMP  0.0                                                          float
WINDDIR  175.3                                                        float
WINDSPD  42.8                                                         float
GUST     31.4                                                         float
AMNIENTN 12.9                                                         float
CFLOOR   7.9                                                          float
NWALLIN  13.3                                                         float
NWALLOUT 8.1                                                          float
WWALLIN  12.5                                                         float
WWALLOUT 9.0                                                          float
AMBIENTS 14.1                                                         float
FLOOR    12.1                                                         float
EWALLCMP 9.8                                                          float
EWALLCOU 8.9                                                          float
ROOF     9.1                                                          float
ROOFAMB  8.8                                                          float
DOMEBLOW 9.9                                                          float
DOMEBUP  10.0                                                         float
DOMELLOW 9.3                                                          float
DOMELUP  8.9                                                          float
DOMERLOW 9.7                                                          float
DOMERUP  9.5                                                          float
PLATFORM 9.9                                                          float
SHACKC   14.9                                                         float
SHACKW   12.7                                                         float
STAIRSL  9.4                                                          float
STAIRSM  9.5                                                          float
STAIRSU  9.6                                                          float
TELBASE  8.1                                                          float
UTILWALL 10.6                                                         float
UTILROOM 10.6                                                         float
EXCLUDED                                                              str
NSPEC    500                                                          int     Number of spectra
WAVEMIN  3600.0                                                       float   First wavelength [Angstroms]
WAVEMAX  5800.0                                                       float   Last wavelength [Angstroms]
WAVESTEP 0.8                                                          float   Wavelength step size [Angstroms]
SPECTER  0.10.0                                                       str     https://github.com/desihub/specter
IN_PSF   SPECPROD/exposures/20201217/00068416/psf-b7-00068416.fits    str     Input sp
IN_IMG   SPECPROD/preproc/20201217/00068416/preproc-b7-00068416.fits  str
ORIG_PSF SPECPROD/calibnight/20201217/psfnight-b7-20201217.fits       str
CHI2PDF  1.140293710496151                                            float
BUNIT                                                                 str     adimensional quantity to divide to flatfield a frame
======== ============================================================ ======= ====================================================

Data: FITS image [float32, 2751x500]

HDU1
----

EXTNAME = IVAR

Inverse variance of fiberflat.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2751             int
NAXIS2   500              int
BUNIT                     str  inverse variance, adimensional
CHECKSUM 75OIA2LF92LFA2LF str  HDU checksum updated 2021-07-07T19:21:58
DATASUM  2784291411       str  data unit checksum updated 2021-07-07T19:21:58
======== ================ ==== ==============================================

Data: FITS image [float32, 2751x500]

HDU2
----

EXTNAME = MASK

Mask of fiberflat (0=good).

Prior to desispec/0.24.0 and software release 18.9, the MASK HDU was compressed.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2751             int  Number of wavelengths
NAXIS2   500              int  Number of spectra (number of rows)
BSCALE   1                int
BZERO    2147483648       int
CHECKSUM TDeFWDbFTDbFTDbF str  HDU checksum updated 2021-07-07T19:21:58
DATASUM  687822           str  data unit checksum updated 2021-07-07T19:21:58
======== ================ ==== ==============================================

Data: FITS image [int32, 2751x500]

HDU3
----

EXTNAME = MEANSPEC

Average continuum lamp spectrum.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================= ==== ==============================================
KEY      Example Value     Type Comment
======== ================= ==== ==============================================
NAXIS1   2751              int  Number of wavelengths
BUNIT    electron/Angstrom str
CHECKSUM nXJGnXGFnXGFnXGF  str  HDU checksum updated 2021-07-07T19:21:58
DATASUM  2097385325        str  data unit checksum updated 2021-07-07T19:21:58
======== ================= ==== ==============================================

Data: FITS image [float32, 2751]

HDU4
----

EXTNAME = WAVELENGTH

Wavelengths in Angstroms at which the fiberflat is measured.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2751             int  Number of wavelengths
BUNIT    Angstrom         str
CHECKSUM 4nG56kG34kG34kG3 str  HDU checksum updated 2021-07-07T19:21:58
DATASUM  2458411755       str  data unit checksum updated 2021-07-07T19:21:58
======== ================ ==== ==============================================

Data: FITS image [float32, 2751]

HDU5
----

EXTNAME = FIBERMAP

The fibermap HDU copied from other files.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   373              int  length of dimension 1
NAXIS2   500              int  length of dimension 2
ENCODING ascii            str
CHECKSUM 2imG4ZkE2fkE2ZkE str  HDU checksum updated 2021-07-07T19:21:58
DATASUM  508954227        str  data unit checksum updated 2021-07-07T19:21:58
======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

===================== ======= ===== ===========
Name                  Type    Units Description
===================== ======= ===== ===========
TARGETID              int64
DESI_TARGET           int64
BGS_TARGET            int64
MWS_TARGET            int64
SECONDARY_TARGET      int64
TARGET_RA             float64
TARGET_DEC            float64
TARGET_RA_IVAR        float64
TARGET_DEC_IVAR       float64
BRICKID               int64
BRICK_OBJID           int64
MORPHTYPE             char[4]
PRIORITY              int32
SUBPRIORITY           float64
REF_ID                int64
PMRA                  float32
PMDEC                 float32
REF_EPOCH             float32
PMRA_IVAR             float32
PMDEC_IVAR            float32
RELEASE               int16
FLUX_G                float32
FLUX_R                float32
FLUX_Z                float32
FLUX_W1               float32
FLUX_W2               float32
FLUX_IVAR_G           float32
FLUX_IVAR_R           float32
FLUX_IVAR_Z           float32
FLUX_IVAR_W1          float32
FLUX_IVAR_W2          float32
FIBERFLUX_G           float32
FIBERFLUX_R           float32
FIBERFLUX_Z           float32
FIBERFLUX_W1          float32
FIBERFLUX_W2          float32
FIBERTOTFLUX_G        float32
FIBERTOTFLUX_R        float32
FIBERTOTFLUX_Z        float32
FIBERTOTFLUX_W1       float32
FIBERTOTFLUX_W2       float32
GAIA_PHOT_G_MEAN_MAG  float32
GAIA_PHOT_BP_MEAN_MAG float32
GAIA_PHOT_RP_MEAN_MAG float32
MW_TRANSMISSION_G     float32
MW_TRANSMISSION_R     float32
MW_TRANSMISSION_Z     float32
EBV                   float32
PHOTSYS               char[1]
OBSCONDITIONS         int32
NUMOBS_INIT           int64
PRIORITY_INIT         int64
NUMOBS_MORE           int32
HPXPIXEL              int64
FIBER                 int32
PETAL_LOC             int32
DEVICE_LOC            int32
LOCATION              int32
FIBERSTATUS           int32
OBJTYPE               char[3]
LAMBDA_REF            float32
FIBERASSIGN_X         float32
FIBERASSIGN_Y         float32
FA_TARGET             int64
FA_TYPE               binary
NUMTARGET             int16
FIBER_RA              float64
FIBER_DEC             float64
FIBER_RA_IVAR         float32
FIBER_DEC_IVAR        float32
PLATEMAKER_X          float32
PLATEMAKER_Y          float32
PLATEMAKER_RA         float32
PLATEMAKER_DEC        float32
NUM_ITER              int32
SPECTROID             int32
EXPTIME               float32
===================== ======= ===== ===========


Notes and Examples
==================

Corrected flux = original flux / fiberflat.

.. code::

  fiberflat = desispec.fiberflat.compute_fiberflat(flatframe)
  desispec.fiberflat.apply_fiberflat(scienceframe, fiberflat)
