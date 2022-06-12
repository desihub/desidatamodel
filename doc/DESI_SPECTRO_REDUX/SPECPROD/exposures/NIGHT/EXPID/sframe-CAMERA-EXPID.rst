========================
sframe-CAMERA-EXPID.fits
========================

:Summary: fiber-flatfielded and sky-subtracted but not flux calibrated
          per-camera spectra.
:Naming Convention: ``sframe-{CAMERA}-{EXPID}.fits``, where ``{CAMERA}`` is
    one of the spectrograph cameras (*e.g.* ``z1``) and ``{EXPID}``
    is the 8-digit exposure ID.
:Regex: ``sframe-[brz][0-9]-[0-9]{8}\.fits``
:File Type: FITS, 70 MB

Contents
========

====== ========== ======== ===================
Number EXTNAME    Type     Contents
====== ========== ======== ===================
HDU0_  FLUX       IMAGE    flatfielded sky subtracted photons
HDU1_  IVAR       IMAGE    Inverse variance of FLUX
HDU2_  MASK       IMAGE    Bad value mask; 0=good
HDU3_  WAVELENGTH IMAGE    Wavelength grid of the extraction
HDU3_  RESOLUTION IMAGE    Resolution matrix
HDU5_  FIBERMAP   BINTABLE Fibermap
HDU6_  CHI2PIX    IMAGE    chi2 of PSF fit to CCD pixels
====== ========== ======== ===================

FITS Header Units
=================

HDU0
----

EXTNAME = FLUX

2D array of fiber flat-fielded and sky subtracted flux of dimension [nspec, nwave] in units of electrons per Angstrom. nspec is the number of fibers per camera. nwave in the length of the wavelength array. The spectra of all fibers share the same
wavelength grid (given in HDU WAVELENGTH). sframe.flux = frame.flux / flatfield - sky .

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============================================================== ======= ===============================================
KEY      Example Value                                                  Type    Comment
======== ============================================================== ======= ===============================================
NAXIS1   2326                                                           int     Number of wavelength samples
NAXIS2   500                                                            int     Number of extracted spectra
EXPID    82471                                                          int     Exposure number
EXPFRAME 0                                                              int     Frame number
FRAMES   None                                                           Unknown Number of Frames in Archive
TILEID   80618                                                          int     DESI Tile ID
FIBASSGN /data/tiles/SVN_tiles/080/fiberassign-080618.fits.gz           str     Fiber assign
FLAVOR   science                                                        str     Observation type
SEQUENCE DESI                                                           str     OCS Sequence name
PURPOSE  Commissioning                                                  str     Purpose of observing night
PROGRAM  etc split test                                                 str     Program name
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
NIGHT    20210327                                                       int     Observing night
TIMESYS  UTC                                                            str     Time system used for date-obs
DATE-OBS 2021-03-28T03:27:30.439315968                                  str     [UTC] Observation data and start tim
TIME-OBS 2021-03-27T03:27:30.439315968                                  str     [UTC] Observation start time
MJD-OBS  59301.14410231                                                 float   Modified Julian Date of observation
OPENSHUT None                                                           Unknown Time shutter opened
ST       08:24:11.800000                                                str     Local Sidereal time at observation start (HH:MM
EXPTIME  404.901                                                        float   [s] Actual exposure time
REQRA    114.221                                                        float   [deg] Requested right ascension (observer input
REQDEC   38.469                                                         float   [deg] Requested declination (observer input)
FOCUS    1344.4,-698.4,733.8,4.4,45.2,197.4                             str     Telescope focus settings
VCCD     ON                                                             str     True (ON) if CCD voltage is on
VCCDON   2021-03-03T22:41:13.333510                                     str     Time when CCD voltage was turned on
VCCDSEC  2091240.6                                                      float   [s] CCD on time in seconds
TRUSTEMP 6.8                                                            float   [deg] Average Telescope truss temperature (only
PMIRTEMP 4.263                                                          float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                                         float   Epoch of observation
MOUNTAZ  308.277504                                                     float   [deg] Mount azimuth angle
MOUNTDEC 38.469911                                                      float   [deg] Mount declination
MOUNTEL  78.698607                                                      float   [deg] Mount elevation angle
MOUNTHA  11.331883                                                      float   [deg] Mount hour angle
SKYDEC   38.469911                                                      float   [deg] Telescope declination (pointing on sky)
SKYRA    114.219192                                                     float   [deg] Telescope right ascension (pointing on sk
TARGTDEC 38.469911                                                      float   [deg] Target declination (to TCS)
TARGTRA  114.219192                                                     float   [deg] Target right ascension (to TCS)
USEETC   T                                                              bool    ETC data available if true
USESKY   T                                                              bool    DOS Control: use Sky Monitor
USEFOCUS T                                                              bool    DOS Control: use focus
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                                        str     Hexapod trim values
USEROTAT T                                                              bool    DOS Control: use rotator
ROTOFFST 194.8                                                          float   [arcsec] Rotator offset
ROTENBLD T                                                              bool    Rotator enabled
ROTRATE  0.0                                                            float   [arcsec/min] Rotator rate
USEGUIDR T                                                              bool    DOS Control: use guider
USEDONUT T                                                              bool    DOS Control: use donuts
SPECGRPH 9                                                              int     Spectrograph logical name (SP)
SPECID   3                                                              int     Spectrograph serial number (SM)
FEEBOX   lbnl086                                                        str     CCD Controller serial number
VESSEL   6                                                              int     Cryostat serial number
FEEVER   v20160312                                                      str     CCD Controller version
FEEPOWER ON                                                             str     FEE power status
FEEDMASK 2134851391                                                     int     FEE dac mask
FEECMASK 1048575                                                        int     FEE clk mask
CCDTEMP  -136.9963                                                      float   [deg C] CCD controller CCD temperature
RADESYS  FK5                                                            str     Coordinate reference frame of major/minor axes
DOSVER   trunk                                                          str     DOS software version
OCSVER   1.2                                                            float   OCS software version
CONSTVER DESI:CURRENT                                                   str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi_nopetal6.ini      str     DOS Conf
CLOCK10  9.9992,2.9993                                                  str     [V] high rail, low rail
CPUTEMP  56.748                                                         float   [deg C] CCD controller CPU temperature
CLOCK5   9.9999,0.0                                                     str     [V] high rail, low rail
PGAGAIN  3                                                              int     Controller gain
CLOCK3   -2.0001,3.9999                                                 str     [V] high rail, low rail
DATASECA [8:2064, 2:2065]                                               str     Data section for quadrant A
DAC4     5.9998,6.0227                                                  str     [V] set value, measured value
DATASECB [2193:4249, 2:2065]                                            str     Data section for quadrant B
CLOCK4   9.9999,0.0                                                     str     [V] high rail, low rail
CLOCK1   9.9999,0.0                                                     str     [V] high rail, low rail
CCDSECA  [1:2057, 1:2064]                                               str     CCD section for quadrant A
DAC6     5.9998,6.028                                                   str     [V] set value, measured value
CLOCK17  9.0,0.9999                                                     str     [V] high rail, low rail
PRESECA  [1:7, 2:2065]                                                  str     Prescan section for quadrant A
CAMERA   r9                                                             str     Camera name
DETSECD  [2058:4114, 2065:4128]                                         str     Detector section for quadrant D
BIASSECC [2065:2128, 2130:4193]                                         str     Bias section for quadrant C
CCDTMING flatdark_lbnl_timing.txt                                       str     CCD timing file
AMPSECD  [4114:2058, 4128:2065]                                         str     AMP section for quadrant D
CLOCK15  9.9992,2.9993                                                  str     [V] high rail, low rail
CCDSIZE  4194,4256                                                      str     CCD size in pixels (rows, columns)
CLOCK18  9.0,0.9999                                                     str     [V] high rail, low rail
CLOCK12  9.9992,2.9993                                                  str     [V] high rail, low rail
CLOCK6   9.9999,0.0                                                     str     [V] high rail, low rail
CCDSECD  [2058:4114, 2065:4128]                                         str     CCD section for quadrant D
CLOCK2   9.9999,0.0                                                     str     [V] high rail, low rail
OFFSET6  2.0,6.028                                                      str     [V] set value, measured value
CLOCK8   9.9992,2.9993                                                  str     [V] high rail, low rail
DAC9     -25.0003,-24.6938                                              str     [V] set value, measured value
ORSECD   [2193:4249, 2098:2129]                                         str     Row bias section for quadrant D
AMPSECC  [1:2057, 4128:2065]                                            str     AMP section for quadrant C
CCDSECC  [1:2057, 2065:4128]                                            str     CCD section for quadrant C
DAC12    0.0,0.0445                                                     str     [V] set value, measured value
CLOCK13  9.9992,2.9993                                                  str     [V] high rail, low rail
OFFSET3  0.4000000059604645,-8.8889                                     str     [V] set value, measured value
CLOCK16  9.9999,3.0                                                     str     [V] high rail, low rail
DAC15    0.0,0.0594                                                     str     [V] set value, measured value
CLOCK11  9.9992,2.9993                                                  str     [V] high rail, low rail
PRRSECA  [8:2064, 1:1]                                                  str     Row prescan section for quadrant A
CRYOPRES 1.232e-07                                                      str     [mb] Cryostat pressure (IP)
DAC13    0.0,0.0594                                                     str     [V] set value, measured value
ORSECC   [8:2064, 2098:2129]                                            str     Row overscan section for quadrant C
DETSECC  [1:2057, 2065:4128]                                            str     Detector section for quadrant C
PRESECC  [1:7, 2130:4193]                                               str     Prescan section for quadrant C
DELAYS   20, 20, 25, 40, 7, 3000, 7, 7, 400, 7                          str     [10] Delay settings
DAC3     -9.0002,-8.8889                                                str     [V] set value, measured value
DETSECA  [1:2057, 1:2064]                                               str     Detector section for quadrant A
DAC11    -25.0003,-24.9906                                              str     [V] set value, measured value
BIASSECD [2129:2192, 2130:4193]                                         str     Bias section for quadrant D
OFFSET7  2.0,5.9228                                                     str     [V] set value, measured value
PRRSECC  [8:2064, 4194:4194]                                            str     Row prescan section for quadrant C
CLOCK9   9.9992,2.9993                                                  str     [V] high rail, low rail
DETECTOR M1-12                                                          str     Detector (ccd) identification
OFFSET0  0.4000000059604645,-8.8683                                     str     [V] set value, measured value
AMPSECB  [4114:2058, 1:2064]                                            str     AMP section for quadrant B
DATASECC [8:2064, 2130:4193]                                            str     Data section for quadrant C
SETTINGS detectors_sm_20210128.json                                     str     Name of DESI CCD settings file
DAC0     -9.0002,-8.8683                                                str     [V] set value, measured value
CCDCFG   default_lbnl_20210128.cfg                                      str     CCD configuration file
CLOCK14  9.9992,2.9993                                                  str     [V] high rail, low rail
DIGITIME 56.4659                                                        float   [s] Time to digitize image
BIASSECB [2129:2192, 2:2065]                                            str     Bias section for quadrant B
TRIMSECB [2193:4249, 2:2065]                                            str     Trim section for quadrant B
BIASSECA [2065:2128, 2:2065]                                            str     Bias section for quadrant A
DAC2     -9.0002,-8.9198                                                str     [V] set value, measured value
PRESECB  [4250:4256, 2:2065]                                            str     Prescan section for quadrant B
TRIMSECA [8:2064, 2:2065]                                               str     Trim section for quadrant A
ORSECB   [2193:4249, 2066:2097]                                         str     Row overscan section for quadrant B
DAC17    20.0008,11.9438                                                str     [V] set value, measured value
DAC8     -25.0003,-25.0351                                              str     [V] set value, measured value
OFFSET2  0.4000000059604645,-8.9198                                     str     [V] set value, measured value
DAC5     5.9998,6.049                                                   str     [V] set value, measured value
OFFSET4  2.0,6.0227                                                     str     [V] set value, measured value
DAC7     5.9998,5.9228                                                  str     [V] set value, measured value
CRYOTEMP 163.069                                                        float   [deg K] Cryostat CCD temperature
CDSPARMS 400, 400, 8, 2000                                              str     CDS parameters
PRESECD  [4250:4256, 2130:4193]                                         str     Prescan section for quadrant D
PRRSECB  [2193:4249, 1:1]                                               str     Row prescan section for quadrant B
CLOCK0   9.9999,0.0                                                     str     [V] high rail, low rail
TRIMSECC [8:2064, 2130:4193]                                            str     Trim section for quadrant C
DAC16    39.9961,39.5934                                                str     [V] set value, measured value
BLDTIME  0.3537                                                         float   [s] Time to build image
OFFSET5  2.0,6.0437                                                     str     [V] set value, measured value
DETSECB  [2058:4114, 1:2064]                                            str     Detector section for quadrant B
DAC14    0.0,0.0594                                                     str     [V] set value, measured value
CCDNAME  CCDSM3R                                                        str     CCD name
CCDSECB  [2058:4114, 1:2064]                                            str     CCD section for quadrant B
ORSECA   [8:2064, 2066:2097]                                            str     Row overscan section for quadrant A
DAC10    -25.0003,-24.7976                                              str     [V] set value, measured value
DAC1     -9.0002,-8.8683                                                str     [V] set value, measured value
PRRSECD  [2193:4249, 4194:4194]                                         str     Row prescan section for quadrant D
CASETEMP 56.3689                                                        float   [deg C] CCD controller case temperature
CLOCK7   -2.0001,3.9999                                                 str     [V] high rail, low rail
DATASECD [2193:4249, 2130:4193]                                         str     Data section for quadrant D
CCDPREP  purge,clear                                                    str     CCD prep actions
OFFSET1  0.4000000059604645,-8.8683                                     str     [V] set value, measured value
TRIMSECD [2193:4249, 2130:4193]                                         str     Trim section for quadrant D
AMPSECA  [1:2057, 1:2064]                                               str     AMP section for quadrant A
REQTIME  1200.0                                                         float   [s] Requested exposure time
OBSID    kp4m20210328t032730                                            str     Unique observation identifier
PROCTYPE RAW                                                            str     Data processing level
PRODTYPE image                                                          str     Data product type
CHECKSUM eAqle6okeAoke5ok                                               str     HDU checksum updated 2021-07-08T15:52:36
DATASUM  1502571638                                                     str     data unit checksum updated 2021-07-08T15:52:36
GAINA    1.753                                                          float   e/ADU (gain applied to image)
SATULEVA 65535.0                                                        float   saturation or non lin. level, in ADU, inc. bias
OVERSCNA 1969.097510928673                                              float   ADUs (gain not applied)
OBSRDNA  2.991258329885281                                              float   electrons (gain is applied)
SATUELEA 111431.027063342                                               float   saturation or non lin. level, in electrons
GAINB    1.641                                                          float   e/ADU (gain applied to image)
SATULEVB 65535.0                                                        float   saturation or non lin. level, in ADU, inc. bias
OVERSCNB 1985.789879724296                                              float   ADUs (gain not applied)
OBSRDNB  2.780391208524129                                              float   electrons (gain is applied)
SATUELEB 104284.2538073724                                              float   saturation or non lin. level, in electrons
GAINC    1.493                                                          float   e/ADU (gain applied to image)
SATULEVC 65535.0                                                        float   saturation or non lin. level, in ADU, inc. bias
OVERSCNC 1956.35457860547                                               float   ADUs (gain not applied)
OBSRDNC  2.592391786703571                                              float   electrons (gain is applied)
SATUELEC 94922.91761414205                                              float   saturation or non lin. level, in electrons
GAIND    1.506                                                          float   e/ADU (gain applied to image)
SATULEVD 65535.0                                                        float   saturation or non lin. level, in ADU, inc. bias
OVERSCND 1997.967299224445                                              float   ADUs (gain not applied)
OBSRDND  2.497454822632709                                              float   electrons (gain is applied)
SATUELED 95686.77124736799                                              float   saturation or non lin. level, in electrons
FIBERMIN 4500                                                           int
MODULE   CI                                                             str
COSMSPLT F                                                              bool
MAXSPLIT 2                                                              int
SPLITIDS 82471,82472,82473                                              str
OBSTYPE  SCIENCE                                                        str
MANIFEST F                                                              bool
OBJECT                                                                  str
NTSSURVY na                                                             str
SEQNUM   1                                                              int
SEQSTART 2021-03-28T03:23:59.954509                                     str
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
AIRMASS  1.026162                                                       float
PMREADY  T                                                              bool
PMCOVER  open                                                           str
PMCOOL   off                                                            str
DOMSHUTU open                                                           str
DOMSHUTL open                                                           str
DOMLIGHH off                                                            str
DOMLIGHL off                                                            str
DOMEAZ   308.654                                                        float
DOMINPOS T                                                              bool
GUIDOFFR 0.72293                                                        float
GUIDOFFD 0.50558                                                        float
SUNRA    7.051836                                                       float
SUNDEC   3.046169                                                       float
MOONDEC  5.013778                                                       float
MOONRA   180.657804                                                     float
MOONSEP  69.575                                                         float
INCTRL   T                                                              bool
INPOS    T                                                              bool
MNTOFFD  -11.73                                                         float
MNTOFFR  25.84                                                          float
PARALLAC 115.913494                                                     float
TARGTAZ  303.894822                                                     float
TARGTEL  77.022352                                                      float
TRGTOFFD 0.0                                                            float
TRGTOFFR 0.0                                                            float
ZD       12.977648                                                      float
TILERA   114.221                                                        float
TILEDEC  38.469                                                         float
TCSST    08:31:58.308                                                   str
TCSMJD   59301.149918                                                   float
REQTEFF  378.0                                                          float
ACTTEFF  43.4371                                                        float
SEEING   1.4601                                                         float
SKYLEVEL 9.516                                                          float
PMSEEING 1.46                                                           float
PMTRANS  100.0                                                          float
ACQCAM   GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                      str
GUIDECAM GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                      str
FOCUSCAM FOCUS1,FOCUS4,FOCUS6,FOCUS9                                    str
SKYCAM   SKYCAM0,SKYCAM1                                                str
REQADC   116.97,128.42                                                  str
ADCCORR  T                                                              bool
ADC1PHI  116.969998                                                     float
ADC2PHI  128.419999                                                     float
ADC1HOME F                                                              bool
ADC2HOME F                                                              bool
ADC1NREV -1.0                                                           float
ADC2NREV 0.0                                                            float
ADC1STAT STOPPED                                                        str
ADC2STAT STOPPED                                                        str
HEXPOS   1344.3,-698.3,733.8,4.4,45.3,181.8                             str
RESETROT F                                                              bool
USEPOS   T                                                              bool
PETALS   PETAL0,PETAL1,PETAL2,PETAL3,PETAL4,PETAL5,PETAL7,PETAL8,PETAL9 str
POSCYCLE 1                                                              int
POSONTGT 852                                                            int
POSONFRC 0.1981                                                         float
POSDISAB 680                                                            int
POSENABL 4301                                                           int
POSRMS   0.2989                                                         float
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
TDEWPNT  -2.11                                                          float
TAIRFLOW 0.0                                                            float
TAIRITMP 6.9                                                            float
TAIROTMP 6.8                                                            float
TAIRTEMP 5.27                                                           float
TCASITMP 6.6                                                            float
TCASOTMP 5.3                                                            float
TCSITEMP 4.4                                                            float
TCSOTEMP 5.7                                                            float
TCIBTEMP 0.0                                                            float
TCIMTEMP 0.0                                                            float
TCITTEMP 0.0                                                            float
TCOSTEMP 0.0                                                            float
TCOWTEMP 0.0                                                            float
TDBTEMP  4.3                                                            float
TFLOWIN  0.0                                                            float
TFLOWOUT 0.0                                                            float
TGLYCOLI 4.8                                                            float
TGLYCOLO 5.0                                                            float
THINGES  6.3                                                            float
THINGEW  5.5                                                            float
TPMAVERT 4.278                                                          float
TPMDESIT 1.0                                                            float
TPMEIBT  3.9                                                            float
TPMEITT  4.4                                                            float
TPMEOBT  3.7                                                            float
TPMEOTT  4.0                                                            float
TPMNIBT  3.8                                                            float
TPMNITT  4.3                                                            float
TPMNOBT  3.9                                                            float
TPMNOTT  4.3                                                            float
TPMRTDT  4.11                                                           float
TPMSIBT  4.2                                                            float
TPMSITT  4.3                                                            float
TPMSOBT  3.5                                                            float
TPMSOTT  4.3                                                            float
TPMSTAT  ready                                                          str
TPMWIBT  3.8                                                            float
TPMWITT  4.2                                                            float
TPMWOBT  3.6                                                            float
TPMWOTT  4.4                                                            float
TPCITEMP 3.3                                                            float
TPCOTEMP 3.2                                                            float
TPR1HUM  0.0                                                            float
TPR1TEMP 0.0                                                            float
TPR2HUM  0.0                                                            float
TPR2TEMP 0.0                                                            float
TSERVO   40.0                                                           float
TTRSTEMP 6.0                                                            float
TTRWTEMP 5.5                                                            float
TTRUETBT -10.0                                                          float
TTRUETTT 6.3                                                            float
TTRUNTBT 5.7                                                            float
TTRUNTTT 6.1                                                            float
TTRUSTBT 5.9                                                            float
TTRUSTST 10.8                                                           float
TTRUSTTT 6.2                                                            float
TTRUTSBT 6.7                                                            float
TTRUTSMT 6.7                                                            float
TTRUTSTT 6.7                                                            float
TTRUWTBT 5.3                                                            float
TTRUWTTT 6.1                                                            float
ALARM    F                                                              bool
ALARM-ON F                                                              bool
BATTERY  100.0                                                          float
SECLEFT  6624.0                                                         float
UPSSTAT  System Normal - On Line(7)                                     str
INAMPS   69.7                                                           float
OUTWATTS 5200.0,6800.0,4900.0                                           str
COMPDEW  -2.5                                                           float
COMPHUM  21.4                                                           float
COMPAMB  15.1                                                           float
COMPTEMP 20.3                                                           float
DEWPOINT 19.3                                                           float
HUMIDITY 89.0                                                           float
PRESSURE 795.0                                                          float
OUTTEMP  21.2                                                           float
WINDDIR  323.0                                                          float
WINDSPD  14.7                                                           float
GUST     14.7                                                           float
AMNIENTN 13.1                                                           float
CFLOOR   4.8                                                            float
NWALLIN  13.3                                                           float
NWALLOUT 4.9                                                            float
WWALLIN  13.2                                                           float
WWALLOUT 5.8                                                            float
AMBIENTS 14.5                                                           float
FLOOR    12.1                                                           float
EWALLCMP 6.1                                                            float
EWALLCOU 5.9                                                            float
ROOF     5.4                                                            float
ROOFAMB  5.8                                                            float
DOMEBLOW 6.1                                                            float
DOMEBUP  6.3                                                            float
DOMELLOW 5.6                                                            float
DOMELUP  5.7                                                            float
DOMERLOW 5.7                                                            float
DOMERUP  5.5                                                            float
PLATFORM 5.2                                                            float
SHACKC   14.9                                                           float
SHACKW   13.6                                                           float
STAIRSL  5.4                                                            float
STAIRSM  5.2                                                            float
STAIRSU  5.4                                                            float
TELBASE  5.1                                                            float
UTILWALL 6.1                                                            float
UTILROOM 5.7                                                            float
SP0NIRT  139.99                                                         float
SP0REDT  140.01                                                         float
SP0BLUT  162.97                                                         float
SP0NIRP  5.455e-08                                                      float
SP0REDP  4.362e-08                                                      float
SP0BLUP  7.73e-08                                                       float
SP1NIRT  140.01                                                         float
SP1REDT  140.01                                                         float
SP1BLUT  163.02                                                         float
SP1NIRP  6.18e-08                                                       float
SP1REDP  7.73e-08                                                       float
SP1BLUP  8.18e-08                                                       float
SP2NIRT  139.99                                                         float
SP2REDT  140.01                                                         float
SP2BLUT  163.02                                                         float
SP2NIRP  3.888e-08                                                      float
SP2REDP  5.598e-08                                                      float
SP2BLUP  9.51e-08                                                       float
SP3NIRT  139.96                                                         float
SP3REDT  139.99                                                         float
SP3BLUT  162.97                                                         float
SP3NIRP  4e-08                                                          float
SP3REDP  6.289e-08                                                      float
SP3BLUP  6.464e-08                                                      float
SP4NIRT  140.01                                                         float
SP4REDT  140.06                                                         float
SP4BLUT  163.04                                                         float
SP4NIRP  6.739e-08                                                      float
SP4REDP  4.72e-08                                                       float
SP4BLUP  6.513e-08                                                      float
SP5NIRT  140.01                                                         float
SP5REDT  140.01                                                         float
SP5BLUT  162.99                                                         float
SP5NIRP  6.728e-08                                                      float
SP5REDP  5.87e-08                                                       float
SP5BLUP  1.102e-07                                                      float
SP6NIRT  140.06                                                         float
SP6REDT  140.06                                                         float
SP6BLUT  163.02                                                         float
SP6NIRP  2.807e-07                                                      float
SP6REDP  6.491e-08                                                      float
SP6BLUP  7.886e-08                                                      float
SP7NIRT  139.99                                                         float
SP7REDT  139.99                                                         float
SP7BLUT  162.99                                                         float
SP7NIRP  7.71799999999999e-08                                           float
SP7REDP  3.724e-08                                                      float
SP7BLUP  9.947e-08                                                      float
SP8NIRT  140.01                                                         float
SP8REDT  140.01                                                         float
SP8BLUT  162.99                                                         float
SP8NIRP  4.819e-08                                                      float
SP8REDP  3.96e-08                                                       float
SP8BLUP  8.106e-08                                                      float
SP9NIRT  140.01                                                         float
SP9REDT  140.06                                                         float
SP9BLUT  163.07                                                         float
SP9NIRP  5.321e-08                                                      float
SP9REDP  4.347e-08                                                      float
SP9BLUP  1.204e-07                                                      float
TNFSPROC 8.6137                                                         float
TGFAPROC 8.6911                                                         float
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
FILENAME /exposures/desi/20210327/00082471/desi-00082471.fits.fz        str
EXCLUDED                                                                str
SIMGFACQ F                                                              bool
TCSKRA   0.3 0.003 0.00003                                              str
TCSKDEC  0.3 0.003 0.00003                                              str
TCSGRA   0.3                                                            float
TCSGDEC  0.3                                                            float
TCSMFRA  1                                                              int
TCSMFDEC 1                                                              int
TCSPIRA  1.0,0.0,0.0,0.0                                                str
TCSPIDEC 1.0,0.0,0.0,0.0                                                str
POSCNVGD F                                                              bool
GUIEXPID 82471                                                          int
IGFRMNUM 10                                                             int
FOCEXPID 82471                                                          int
IFFRMNUM 1                                                              int
SKYEXPID 82471                                                          int
ISFRMNUM 0                                                              int
FGFRMNUM 60                                                             int
FFFRMNUM 7                                                              int
FSFRMNUM 5                                                              int
HELIOCOR 0.9999069545810282                                             float
NSPEC    500                                                            int     Number of spectra
WAVEMIN  5760.0                                                         float   First wavelength [Angstroms]
WAVEMAX  7620.0                                                         float   Last wavelength [Angstroms]
WAVESTEP 0.8                                                            float   Wavelength step size [Angstroms]
SPECTER  0.10.0                                                         str     https://github.com/desihub/specter
IN_PSF   SPECPROD/exposures/20210327/00082471/psf-r9-00082471.fits      str     Input sp
IN_IMG   SPECPROD/preproc/20210327/00082471/preproc-r9-00082471.fits    str
ORIG_PSF SPECPROD/calibnight/20210327/psfnight-r9-20210327.fits         str
BUNIT    electron/Angstrom                                              str
IN_SKY   SPECPROD/exposures/20210327/00082471/sky-r9-00082471.fits      str
FIBERFLT SPECPROD/calibnight/20210327/fiberflatnight-r9-20210327.fits   str
======== ============================================================== ======= ===============================================

Data: FITS image [float32, 2326x500]

HDU1
----

EXTNAME = IVAR

Inverse variance of the flux in HDU0. The unit is 1/(electrons/Angstrom)^2. The noise from neighboring spectral pixels is uncorrelated.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2326             int  Number of wavelengths
NAXIS2   500              int  Number of spectra
CHECKSUM 9UJ3CTG29TG2ATG2 str  HDU checksum updated 2021-07-08T15:52:36
DATASUM  3074959512       str  data unit checksum updated 2021-07-08T15:52:36
======== ================ ==== ==============================================

Data: FITS image [float32, 2326x500]

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
NAXIS1   2326             int  Number of wavelengths
NAXIS2   500              int  Number of spectra
BSCALE   1                int
BZERO    2147483648       int
CHECKSUM ZGp6dDn5ZDn5bDn5 str  HDU checksum updated 2021-07-08T15:52:36
DATASUM  47035306         str  data unit checksum updated 2021-07-08T15:52:36
======== ================ ==== ==============================================

Data: FITS image [int32, 2326x500]

HDU3
----

EXTNAME = WAVELENGTH

1D array of wavelengths. See the frame :ref:`WAVELENGTH documentation <frame-hdu3-wavelength>` for more details.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2326             int  Number of wavelengths
BUNIT    Angstrom         str
CHECKSUM 9MZDCMZA9MZAAMZA str  HDU checksum updated 2021-07-08T15:52:37
DATASUM  456732359        str  data unit checksum updated 2021-07-08T15:52:37
======== ================ ==== ==============================================

Data: FITS image [float64, 2326]

HDU4
----

EXTNAME = RESOLUTION

Resolution matrix stored as a 3D sparse matrix. the frame :ref:`RESOLUTION documentation <frame-hdu4-resolution>` for more details.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2326             int
NAXIS2   11               int
NAXIS3   500              int
CHECKSUM LiPqNgMnLgMnLgMn str  HDU checksum updated 2021-07-08T15:52:39
DATASUM  2191513558       str  data unit checksum updated 2021-07-08T15:52:39
======== ================ ==== ==============================================

Data: FITS image [float32, 2326x11x500]

HDU5
----

EXTNAME = FIBERMAP

Fibermap information combining fiberassign request with actual fiber locations. See also the :doc:`fibermap documentation </DESI_SPECTRO_REDUX/SPECPROD/preproc/NIGHT/EXPID/fibermap-EXPID>` page.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================================================================== ======= ==============================================
KEY      Example Value                                                            Type    Comment
======== ======================================================================== ======= ==============================================
NAXIS1   369                                                                      int     length of dimension 1
NAXIS2   500                                                                      int     length of dimension 2
TILEID   80618                                                                    int
TILERA   114.221                                                                  float
TILEDEC  38.469                                                                   float
FIELDROT 0.145323276256189                                                        float
FA_PLAN  2022-07-01T00:00:00.000                                                  str
FA_HA    0.0                                                                      float
FA_RUN   2020-03-06T00:00:00                                                      str
REQRA    114.221                                                                  float
REQDEC   38.469                                                                   float
FIELDNUM 0                                                                        int
FA_VER   2.0.0.dev2618                                                            str
FA_SURV  sv1                                                                      str
GFA      /data/target/catalogs/dr9/0.47.0/gfas                                    str
SKY      /data/target/catalogs/dr9/0.47.0/skies                                   str
SKYSUPP  /data/target/catalogs/gaiadr2/0.47.0/skies-supp                          str
TARG     /data/target/catalogs/dr9/0.47.0/targets/sv1/resolve/bright/             str
FAFLAVOR sv1bgsmws                                                                str
FAOUTDIR /software/datasystems/users/raichoor/fiberassign-test/desi-sv1-20201218/ str
PMTIME   2020-12-19T00:00:00.000                                                  str
RUNDATE  2020-03-06T00:00:00                                                      str
SCTARG   STD_WD,BGS_ANY,MWS_ANY                                                   str
OBSCON   DARK|GRAY|BRIGHT                                                         str
BZERO    32768                                                                    int
BSCALE   1                                                                        int
MODULE   CI                                                                       str
EXPID    82471                                                                    int
EXPFRAME 0                                                                        int
FRAMES   None                                                                     Unknown
COSMSPLT F                                                                        bool
MAXSPLIT 2                                                                        int
SPLITIDS 82471,82472,82473                                                        str
FIBASSGN /data/tiles/SVN_tiles/080/fiberassign-080618.fits.gz                     str
FLAVOR   science                                                                  str
OBSTYPE  SCIENCE                                                                  str
SEQUENCE DESI                                                                     str
MANIFEST F                                                                        bool
OBJECT                                                                            str
PURPOSE  Commissioning                                                            str
PROGRAM  etc split test                                                           str
NTSSURVY na                                                                       str
PROPID   2019B-5000                                                               str
OBSERVER DESIObserver                                                             str
LEAD     RunManager                                                               str
INSTRUME DESI                                                                     str
OBSERVAT KPNO                                                                     str
OBS-LAT  31.96403                                                                 str
OBS-LONG -111.59989                                                               str
OBS-ELEV 2097.0                                                                   float
TELESCOP KPNO 4.0-m telescope                                                     str
CORRCTOR DESI Corrector                                                           str
SEQNUM   1                                                                        int
NIGHT    20210327                                                                 int
SEQSTART 2021-03-28T03:23:59.954509                                               str
TIMESYS  UTC                                                                      str
DATE-OBS 2021-03-28T03:27:30.435958784                                            str
TIME-OBS 2021-03-27T03:27:30.435958784                                            str
MJD-OBS  59301.144102268                                                          float
OPENSHUT None                                                                     Unknown
CAMSHUT  open                                                                     str
ST       08:24:11.795000                                                          str
ACQTIME  15                                                                       int
GUIDTIME 5.0                                                                      float
FOCSTIME 60.0                                                                     float
SKYTIME  60.0                                                                     float
WHITESPT F                                                                        bool
ZENITH   F                                                                        bool
SEANNEX  F                                                                        bool
BEYONDP  F                                                                        bool
FIDUCIAL off                                                                      str
BACKLIT  off                                                                      str
AIRMASS  1.026162                                                                 float
FOCUS    1344.4,-698.4,733.8,4.4,45.2,197.4                                       str
VCCD     ON                                                                       str
TRUSTEMP 6.8                                                                      float
PMIRTEMP 4.263                                                                    float
PMREADY  T                                                                        bool
PMCOVER  open                                                                     str
PMCOOL   off                                                                      str
DOMSHUTU open                                                                     str
DOMSHUTL open                                                                     str
DOMLIGHH off                                                                      str
DOMLIGHL off                                                                      str
DOMEAZ   308.654                                                                  float
DOMINPOS T                                                                        bool
EPOCH    2000.0                                                                   float
GUIDOFFR 0.72293                                                                  float
GUIDOFFD 0.50558                                                                  float
SUNRA    7.051836                                                                 float
SUNDEC   3.046169                                                                 float
MOONDEC  5.013778                                                                 float
MOONRA   180.657804                                                               float
MOONSEP  69.575                                                                   float
MOUNTAZ  308.277504                                                               float
MOUNTDEC 38.469911                                                                float
MOUNTEL  78.698607                                                                float
MOUNTHA  11.331883                                                                float
INCTRL   T                                                                        bool
INPOS    T                                                                        bool
MNTOFFD  -11.73                                                                   float
MNTOFFR  25.84                                                                    float
PARALLAC 115.913494                                                               float
SKYDEC   38.469911                                                                float
SKYRA    114.219192                                                               float
TARGTDEC 38.469911                                                                float
TARGTRA  114.219192                                                               float
TARGTAZ  303.894822                                                               float
TARGTEL  77.022352                                                                float
TRGTOFFD 0.0                                                                      float
TRGTOFFR 0.0                                                                      float
ZD       12.977648                                                                float
TCSST    08:31:58.308                                                             str
TCSMJD   59301.149918                                                             float
USEETC   T                                                                        bool
REQTEFF  378.0                                                                    float
ACTTEFF  43.4371                                                                  float
SEEING   1.4601                                                                   float
SKYLEVEL 9.516                                                                    float
PMSEEING 1.46                                                                     float
PMTRANS  100.0                                                                    float
ACQCAM   GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                                str
GUIDECAM GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                                str
FOCUSCAM FOCUS1,FOCUS4,FOCUS6,FOCUS9                                              str
SKYCAM   SKYCAM0,SKYCAM1                                                          str
REQADC   116.97,128.42                                                            str
ADCCORR  T                                                                        bool
ADC1PHI  116.969998                                                               float
ADC2PHI  128.419999                                                               float
ADC1HOME F                                                                        bool
ADC2HOME F                                                                        bool
ADC1NREV -1.0                                                                     float
ADC2NREV 0.0                                                                      float
ADC1STAT STOPPED                                                                  str
ADC2STAT STOPPED                                                                  str
USESKY   T                                                                        bool
USEFOCUS T                                                                        bool
HEXPOS   1344.3,-698.3,733.8,4.4,45.3,181.8                                       str
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                                                  str
USEROTAT T                                                                        bool
ROTOFFST 194.8                                                                    float
ROTENBLD T                                                                        bool
ROTRATE  0.0                                                                      float
RESETROT F                                                                        bool
USEPOS   T                                                                        bool
PETALS   PETAL0,PETAL1,PETAL2,PETAL3,PETAL4,PETAL5,PETAL7,PETAL8,PETAL9           str
POSCYCLE 1                                                                        int
POSONTGT 852                                                                      int
POSONFRC 0.1981                                                                   float
POSDISAB 680                                                                      int
POSENABL 4301                                                                     int
POSRMS   0.2989                                                                   float
POSITER  1                                                                        int
POSFRACT 0.95                                                                     float
POSTOLER 0.005                                                                    float
POSMVALL T                                                                        bool
USEGUIDR T                                                                        bool
GUIDMODE catalog                                                                  str
USEAOS   F                                                                        bool
USEDONUT T                                                                        bool
USESPCTR T                                                                        bool
SPCGRPHS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                                  str
ILLSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                                  str
CCDSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                                  str
TDEWPNT  -2.11                                                                    float
TAIRFLOW 0.0                                                                      float
TAIRITMP 6.9                                                                      float
TAIROTMP 6.8                                                                      float
TAIRTEMP 5.27                                                                     float
TCASITMP 6.6                                                                      float
TCASOTMP 5.3                                                                      float
TCSITEMP 4.4                                                                      float
TCSOTEMP 5.7                                                                      float
TCIBTEMP 0.0                                                                      float
TCIMTEMP 0.0                                                                      float
TCITTEMP 0.0                                                                      float
TCOSTEMP 0.0                                                                      float
TCOWTEMP 0.0                                                                      float
TDBTEMP  4.3                                                                      float
TFLOWIN  0.0                                                                      float
TFLOWOUT 0.0                                                                      float
TGLYCOLI 4.8                                                                      float
TGLYCOLO 5.0                                                                      float
THINGES  6.3                                                                      float
THINGEW  5.5                                                                      float
TPMAVERT 4.278                                                                    float
TPMDESIT 1.0                                                                      float
TPMEIBT  3.9                                                                      float
TPMEITT  4.4                                                                      float
TPMEOBT  3.7                                                                      float
TPMEOTT  4.0                                                                      float
TPMNIBT  3.8                                                                      float
TPMNITT  4.3                                                                      float
TPMNOBT  3.9                                                                      float
TPMNOTT  4.3                                                                      float
TPMRTDT  4.11                                                                     float
TPMSIBT  4.2                                                                      float
TPMSITT  4.3                                                                      float
TPMSOBT  3.5                                                                      float
TPMSOTT  4.3                                                                      float
TPMSTAT  ready                                                                    str
TPMWIBT  3.8                                                                      float
TPMWITT  4.2                                                                      float
TPMWOBT  3.6                                                                      float
TPMWOTT  4.4                                                                      float
TPCITEMP 3.3                                                                      float
TPCOTEMP 3.2                                                                      float
TPR1HUM  0.0                                                                      float
TPR1TEMP 0.0                                                                      float
TPR2HUM  0.0                                                                      float
TPR2TEMP 0.0                                                                      float
TSERVO   40.0                                                                     float
TTRSTEMP 6.0                                                                      float
TTRWTEMP 5.5                                                                      float
TTRUETBT -10.0                                                                    float
TTRUETTT 6.3                                                                      float
TTRUNTBT 5.7                                                                      float
TTRUNTTT 6.1                                                                      float
TTRUSTBT 5.9                                                                      float
TTRUSTST 10.8                                                                     float
TTRUSTTT 6.2                                                                      float
TTRUTSBT 6.7                                                                      float
TTRUTSMT 6.7                                                                      float
TTRUTSTT 6.7                                                                      float
TTRUWTBT 5.3                                                                      float
TTRUWTTT 6.1                                                                      float
ALARM    F                                                                        bool
ALARM-ON F                                                                        bool
BATTERY  100.0                                                                    float
SECLEFT  6624.0                                                                   float
UPSSTAT  System Normal - On Line(7)                                               str
INAMPS   69.7                                                                     float
OUTWATTS 5200.0,6800.0,4900.0                                                     str
COMPDEW  -2.5                                                                     float
COMPHUM  21.4                                                                     float
COMPAMB  15.1                                                                     float
COMPTEMP 20.3                                                                     float
DEWPOINT 19.3                                                                     float
HUMIDITY 89.0                                                                     float
PRESSURE 795.0                                                                    float
OUTTEMP  21.2                                                                     float
WINDDIR  323.0                                                                    float
WINDSPD  14.7                                                                     float
GUST     14.7                                                                     float
AMNIENTN 13.1                                                                     float
CFLOOR   4.8                                                                      float
NWALLIN  13.3                                                                     float
NWALLOUT 4.9                                                                      float
WWALLIN  13.2                                                                     float
WWALLOUT 5.8                                                                      float
AMBIENTS 14.5                                                                     float
FLOOR    12.1                                                                     float
EWALLCMP 6.1                                                                      float
EWALLCOU 5.9                                                                      float
ROOF     5.4                                                                      float
ROOFAMB  5.8                                                                      float
DOMEBLOW 6.1                                                                      float
DOMEBUP  6.3                                                                      float
DOMELLOW 5.6                                                                      float
DOMELUP  5.7                                                                      float
DOMERLOW 5.7                                                                      float
DOMERUP  5.5                                                                      float
PLATFORM 5.2                                                                      float
SHACKC   14.9                                                                     float
SHACKW   13.6                                                                     float
STAIRSL  5.4                                                                      float
STAIRSM  5.2                                                                      float
STAIRSU  5.4                                                                      float
TELBASE  5.1                                                                      float
UTILWALL 6.1                                                                      float
UTILROOM 5.7                                                                      float
SP0NIRT  139.99                                                                   float
SP0REDT  140.01                                                                   float
SP0BLUT  162.97                                                                   float
SP0NIRP  5.455e-08                                                                float
SP0REDP  4.362e-08                                                                float
SP0BLUP  7.73e-08                                                                 float
SP1NIRT  140.01                                                                   float
SP1REDT  140.01                                                                   float
SP1BLUT  163.02                                                                   float
SP1NIRP  6.18e-08                                                                 float
SP1REDP  7.73e-08                                                                 float
SP1BLUP  8.18e-08                                                                 float
SP2NIRT  139.99                                                                   float
SP2REDT  140.01                                                                   float
SP2BLUT  163.02                                                                   float
SP2NIRP  3.888e-08                                                                float
SP2REDP  5.598e-08                                                                float
SP2BLUP  9.51e-08                                                                 float
SP3NIRT  139.96                                                                   float
SP3REDT  139.99                                                                   float
SP3BLUT  162.97                                                                   float
SP3NIRP  4e-08                                                                    float
SP3REDP  6.289e-08                                                                float
SP3BLUP  6.464e-08                                                                float
SP4NIRT  140.01                                                                   float
SP4REDT  140.06                                                                   float
SP4BLUT  163.04                                                                   float
SP4NIRP  6.739e-08                                                                float
SP4REDP  4.72e-08                                                                 float
SP4BLUP  6.513e-08                                                                float
SP5NIRT  140.01                                                                   float
SP5REDT  140.01                                                                   float
SP5BLUT  162.99                                                                   float
SP5NIRP  6.728e-08                                                                float
SP5REDP  5.87e-08                                                                 float
SP5BLUP  1.102e-07                                                                float
SP6NIRT  140.06                                                                   float
SP6REDT  140.06                                                                   float
SP6BLUT  163.02                                                                   float
SP6NIRP  2.807e-07                                                                float
SP6REDP  6.491e-08                                                                float
SP6BLUP  7.886e-08                                                                float
SP7NIRT  139.99                                                                   float
SP7REDT  139.99                                                                   float
SP7BLUT  162.99                                                                   float
SP7NIRP  7.71799999999999e-08                                                     float
SP7REDP  3.724e-08                                                                float
SP7BLUP  9.947e-08                                                                float
SP8NIRT  140.01                                                                   float
SP8REDT  140.01                                                                   float
SP8BLUT  162.99                                                                   float
SP8NIRP  4.819e-08                                                                float
SP8REDP  3.96e-08                                                                 float
SP8BLUP  8.106e-08                                                                float
SP9NIRT  140.01                                                                   float
SP9REDT  140.06                                                                   float
SP9BLUT  163.07                                                                   float
SP9NIRP  5.321e-08                                                                float
SP9REDP  4.347e-08                                                                float
SP9BLUP  1.204e-07                                                                float
RADESYS  FK5                                                                      str
TNFSPROC 8.6137                                                                   float
TGFAPROC 8.6911                                                                   float
SIMGFAP  F                                                                        bool
USEFVC   T                                                                        bool
USEFID   T                                                                        bool
USEILLUM T                                                                        bool
USEXSRVR T                                                                        bool
USEOPENL T                                                                        bool
STOPGUDR T                                                                        bool
STOPFOCS T                                                                        bool
STOPSKY  T                                                                        bool
KEEPGUDR F                                                                        bool
KEEPFOCS F                                                                        bool
KEEPSKY  F                                                                        bool
REACQUIR F                                                                        bool
FILENAME /exposures/desi/20210327/00082471/desi-00082471.fits.fz                  str
EXCLUDED                                                                          str
DOSVER   trunk                                                                    str
OCSVER   1.2                                                                      float
CONSTVER DESI:CURRENT                                                             str
INIFILE  /data/msdos/dos_home/architectures/kpno/desi_nopetal6.ini                str
REQTIME  1200.0                                                                   float
SIMGFACQ F                                                                        bool
TCSKRA   0.3 0.003 0.00003                                                        str
TCSKDEC  0.3 0.003 0.00003                                                        str
TCSGRA   0.3                                                                      float
TCSGDEC  0.3                                                                      float
TCSMFRA  1                                                                        int
TCSMFDEC 1                                                                        int
TCSPIRA  1.0,0.0,0.0,0.0                                                          str
TCSPIDEC 1.0,0.0,0.0,0.0                                                          str
POSCNVGD F                                                                        bool
GUIEXPID 82471                                                                    int
IGFRMNUM 10                                                                       int
FOCEXPID 82471                                                                    int
IFFRMNUM 1                                                                        int
SKYEXPID 82471                                                                    int
ISFRMNUM 0                                                                        int
FGFRMNUM 60                                                                       int
FFFRMNUM 7                                                                        int
FSFRMNUM 5                                                                        int
SEQID    2 requests                                                               str
SEQTOT   2                                                                        int
DELTARA  None                                                                     Unknown
DELTADEC None                                                                     Unknown
GSGUIDE5 (926.39,1827.49),(896.85,895.27)                                         str
GSGUIDE7 (707.79,1894.75),(408.78,1321.69)                                        str
GSGUIDE8 (210.36,1109.18),(739.80,665.39)                                         str
GSGUIDE0 (205.82,1419.31),(826.45,1151.95)                                        str
GSGUIDE2 (399.48,787.77),(572.35,1748.42)                                         str
GSGUIDE3 (826.20,829.60),(309.14,227.34)                                          str
ARCHIVE  /exposures/desi/20210327/00082471/guide-00082471.fits.fz                 str
GUIDEFIL guide-00082471.fits.fz                                                   str
COORDFIL coordinates-00082471.fits                                                str
EXPTIME  404.901                                                                  float
VCCDON   2021-03-03T22:41:13.333510                                               str
VCCDSEC  2091240.6                                                                float
SPECGRPH 9                                                                        int
SPECID   3                                                                        int
FEEBOX   lbnl086                                                                  str
VESSEL   6                                                                        int
FEEVER   v20160312                                                                str
FEEPOWER ON                                                                       str
FEEDMASK 2134851391                                                               int
FEECMASK 1048575                                                                  int
CCDTEMP  -136.9963                                                                float
CLOCK10  9.9992,2.9993                                                            str
CPUTEMP  56.748                                                                   float
CLOCK5   9.9999,0.0                                                               str
PGAGAIN  3                                                                        int
CLOCK3   -2.0001,3.9999                                                           str
DATASECA [8:2064, 2:2065]                                                         str
DAC4     5.9998,6.0227                                                            str
DATASECB [2193:4249, 2:2065]                                                      str
CLOCK4   9.9999,0.0                                                               str
CLOCK1   9.9999,0.0                                                               str
CCDSECA  [1:2057, 1:2064]                                                         str
DAC6     5.9998,6.028                                                             str
CLOCK17  9.0,0.9999                                                               str
PRESECA  [1:7, 2:2065]                                                            str
CAMERA   r9                                                                       str
DETSECD  [2058:4114, 2065:4128]                                                   str
BIASSECC [2065:2128, 2130:4193]                                                   str
CCDTMING flatdark_lbnl_timing.txt                                                 str
AMPSECD  [4114:2058, 4128:2065]                                                   str
CLOCK15  9.9992,2.9993                                                            str
CCDSIZE  4194,4256                                                                str
CLOCK18  9.0,0.9999                                                               str
CLOCK12  9.9992,2.9993                                                            str
CLOCK6   9.9999,0.0                                                               str
CCDSECD  [2058:4114, 2065:4128]                                                   str
CLOCK2   9.9999,0.0                                                               str
OFFSET6  2.0,6.028                                                                str
CLOCK8   9.9992,2.9993                                                            str
DAC9     -25.0003,-24.6938                                                        str
ORSECD   [2193:4249, 2098:2129]                                                   str
AMPSECC  [1:2057, 4128:2065]                                                      str
CCDSECC  [1:2057, 2065:4128]                                                      str
DAC12    0.0,0.0445                                                               str
CLOCK13  9.9992,2.9993                                                            str
OFFSET3  0.4000000059604645,-8.8889                                               str
CLOCK16  9.9999,3.0                                                               str
DAC15    0.0,0.0594                                                               str
CLOCK11  9.9992,2.9993                                                            str
PRRSECA  [8:2064, 1:1]                                                            str
CRYOPRES 1.232e-07                                                                str
DAC13    0.0,0.0594                                                               str
ORSECC   [8:2064, 2098:2129]                                                      str
DETSECC  [1:2057, 2065:4128]                                                      str
PRESECC  [1:7, 2130:4193]                                                         str
DELAYS   20, 20, 25, 40, 7, 3000, 7, 7, 400, 7                                    str
DAC3     -9.0002,-8.8889                                                          str
DETSECA  [1:2057, 1:2064]                                                         str
DAC11    -25.0003,-24.9906                                                        str
BIASSECD [2129:2192, 2130:4193]                                                   str
OFFSET7  2.0,5.9228                                                               str
PRRSECC  [8:2064, 4194:4194]                                                      str
CLOCK9   9.9992,2.9993                                                            str
DETECTOR M1-12                                                                    str
OFFSET0  0.4000000059604645,-8.8683                                               str
AMPSECB  [4114:2058, 1:2064]                                                      str
DATASECC [8:2064, 2130:4193]                                                      str
SETTINGS detectors_sm_20210128.json                                               str
DAC0     -9.0002,-8.8683                                                          str
CCDCFG   default_lbnl_20210128.cfg                                                str
CLOCK14  9.9992,2.9993                                                            str
DIGITIME 56.4659                                                                  float
BIASSECB [2129:2192, 2:2065]                                                      str
TRIMSECB [2193:4249, 2:2065]                                                      str
BIASSECA [2065:2128, 2:2065]                                                      str
DAC2     -9.0002,-8.9198                                                          str
PRESECB  [4250:4256, 2:2065]                                                      str
TRIMSECA [8:2064, 2:2065]                                                         str
ORSECB   [2193:4249, 2066:2097]                                                   str
DAC17    20.0008,11.9438                                                          str
DAC8     -25.0003,-25.0351                                                        str
OFFSET2  0.4000000059604645,-8.9198                                               str
DAC5     5.9998,6.049                                                             str
OFFSET4  2.0,6.0227                                                               str
DAC7     5.9998,5.9228                                                            str
CRYOTEMP 163.069                                                                  float
CDSPARMS 400, 400, 8, 2000                                                        str
PRESECD  [4250:4256, 2130:4193]                                                   str
PRRSECB  [2193:4249, 1:1]                                                         str
CLOCK0   9.9999,0.0                                                               str
TRIMSECC [8:2064, 2130:4193]                                                      str
DAC16    39.9961,39.5934                                                          str
BLDTIME  0.3537                                                                   float
OFFSET5  2.0,6.0437                                                               str
DETSECB  [2058:4114, 1:2064]                                                      str
DAC14    0.0,0.0594                                                               str
CCDNAME  CCDSM3R                                                                  str
CCDSECB  [2058:4114, 1:2064]                                                      str
ORSECA   [8:2064, 2066:2097]                                                      str
DAC10    -25.0003,-24.7976                                                        str
DAC1     -9.0002,-8.8683                                                          str
PRRSECD  [2193:4249, 4194:4194]                                                   str
CASETEMP 56.3689                                                                  float
CLOCK7   -2.0001,3.9999                                                           str
DATASECD [2193:4249, 2130:4193]                                                   str
CCDPREP  purge,clear                                                              str
OFFSET1  0.4000000059604645,-8.8683                                               str
TRIMSECD [2193:4249, 2130:4193]                                                   str
AMPSECA  [1:2057, 1:2064]                                                         str
OBSID    kp4m20210328t032730                                                      str
PROCTYPE RAW                                                                      str
PRODTYPE image                                                                    str
GAINA    1.753                                                                    float
SATULEVA 65535.0                                                                  float
OVERSCNA 1969.097510928673                                                        float
OBSRDNA  2.991258329885281                                                        float
SATUELEA 111431.027063342                                                         float
GAINB    1.641                                                                    float
SATULEVB 65535.0                                                                  float
OVERSCNB 1985.789879724296                                                        float
OBSRDNB  2.780391208524129                                                        float
SATUELEB 104284.2538073724                                                        float
GAINC    1.493                                                                    float
SATULEVC 65535.0                                                                  float
OVERSCNC 1956.35457860547                                                         float
OBSRDNC  2.592391786703571                                                        float
SATUELEC 94922.91761414205                                                        float
GAIND    1.506                                                                    float
SATULEVD 65535.0                                                                  float
OVERSCND 1997.967299224445                                                        float
OBSRDND  2.497454822632709                                                        float
SATUELED 95686.77124736799                                                        float
FIBERMIN 4500                                                                     int
CHECKSUM 9HCPH99N9GCNE99N                                                         str     HDU checksum updated 2021-07-08T15:52:40
DATASUM  955623005                                                                str     data unit checksum updated 2021-07-08T15:52:40
ENCODING ascii                                                                    str
======== ======================================================================== ======= ==============================================

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
FIBERFLUX_G           float32
FIBERFLUX_R           float32
FIBERFLUX_Z           float32
FIBERTOTFLUX_G        float32
FIBERTOTFLUX_R        float32
FIBERTOTFLUX_Z        float32
MASKBITS              int16
SERSIC                float32
SHAPE_R               float32
SHAPE_E1              float32
SHAPE_E2              float32
PHOTSYS               char[1]
PRIORITY_INIT         int64
NUMOBS_INIT           int64
SV1_DESI_TARGET       int64
SV1_BGS_TARGET        int64
SV1_MWS_TARGET        int64
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
NAXIS1   2326             int  Number of wavelengths
NAXIS2   500              int  Number of spectra
CHECKSUM WY6VaW3VZW3VaW3V str  HDU checksum updated 2021-07-08T15:52:40
DATASUM  2321269489       str  data unit checksum updated 2021-07-08T15:52:40
======== ================ ==== ==============================================

Data: FITS image [float32, 2326x500]


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
