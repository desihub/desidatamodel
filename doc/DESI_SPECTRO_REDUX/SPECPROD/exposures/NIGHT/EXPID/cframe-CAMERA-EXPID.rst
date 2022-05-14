========================
cframe-CAMERA-EXPID.fits
========================

:Summary: This holds the calibrated spectra for a given camera and exposure.
    See the datamodel for :doc:`frame-CAMERA-EXPID.fits <frame-CAMERA-EXPID>`
    files for details of the format.
:Naming Convention: ``cframe-{CAMERA}-{EXPID}.fits``, where ``{CAMERA}`` is
    one of the spectrograph cameras (*e.g.* ``z1``) and ``{EXPID}``
    is the 8-digit exposure ID.
:Regex: ``cframe-[brz][0-9]-[0-9]{8}\.fits``
:File Type: FITS, 82 MB

Contents
========

====== ========== ======== ======================================
Number EXTNAME    Type     Contents
====== ========== ======== ======================================
HDU0_  FLUX       IMAGE    Flux, erg/s/cm2/A
HDU1_  IVAR       IMAGE    Inverse variance, ``(erg/s/cm2/A)^-2``
HDU2_  MASK       IMAGE    Mask (0 = good)
HDU3_  WAVELENGTH IMAGE    wavelength in Angstrom
HDU4_  RESOLUTION IMAGE    Resolution Matrix
HDU5_  FIBERMAP   BINTABLE Fibermap
HDU6_  CHI2PIX    IMAGE    chi2 fit of PSF model to CCD image
HDU7_  SCORES     BINTABLE Quality Assurance scores
====== ========== ======== ======================================


FITS Header Units
=================

HDU0
----

EXTNAME = FLUX

Calibrated spectral flux in 1e-17 erg / (s cm2 Angstrom).

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ===================================================================== ======= ===============================================
    KEY      Example Value                                                         Type    Comment
    ======== ===================================================================== ======= ===============================================
    NAXIS1   2881                                                                  int
    NAXIS2   500                                                                   int
    EXPID    77777                                                                 int     Exposure number
    EXPFRAME 0                                                                     int     Frame number
    FRAMES   None                                                                  Unknown Number of Frames in Archive
    TILEID   80782                                                                 int     DESI Tile ID
    FIBASSGN /data/tiles/SVN_tiles/080/fiberassign-080782.fits.gz                  str     Fiber assign
    FLAVOR   science                                                               str     Observation type
    SEQUENCE DESI                                                                  str     OCS Sequence name
    PURPOSE  SV                                                                    str     Purpose of observing night
    PROGRAM  sv1backup1                                                            str     Program name
    PROPID   2019B-5000                                                            str     Proposal ID
    OBSERVER Adam Myers                                                            str     Names of observers
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
    DATE-OBS 2021-02-24T08:45:48.798053888                                         str     [UTC] Observation data and start tim
    TIME-OBS 2021-02-24T08:45:48.798053888                                         str     [UTC] Observation start time
    MJD-OBS  59269.36514813                                                        float   Modified Julian Date of observation
    OPENSHUT None                                                                  Unknown Time shutter opened
    ST       11:37:12.750000                                                       str     Local Sidereal time at observation start (HH:MM
    EXPTIME  600.079                                                               float   [s] Actual exposure time
    REQRA    168.8                                                                 float   [deg] Requested right ascension (observer input
    REQDEC   71.5                                                                  float   [deg] Requested declination (observer input)
    FOCUS    1117.8,-820.8,10.2,15.2,30.5,462.4                                    str     Telescope focus settings
    VCCD     ON                                                                    str     True (ON) if CCD voltage is on
    VCCDON   2021-02-16T23:21:25.955005                                            str     Time when CCD voltage was turned on
    VCCDSEC  639321.4                                                              float   [s] CCD on time in seconds
    TRUSTEMP 10.533                                                                float   [deg] Average Telescope truss temperature (only
    PMIRTEMP 10.088                                                                float   [deg] Average primary mirror temperature (nit,e
    EPOCH    2000.0                                                                float   Epoch of observation
    MOUNTAZ  357.580192                                                            float   [deg] Mount azimuth angle
    MOUNTDEC 71.50884                                                              float   [deg] Mount declination
    MOUNTEL  50.367086                                                             float   [deg] Mount elevation angle
    MOUNTHA  4.871119                                                              float   [deg] Mount hour angle
    SKYDEC   71.50884                                                              float   [deg] Telescope declination (pointing on sky)
    SKYRA    168.797258                                                            float   [deg] Telescope right ascension (pointing on sk
    TARGTDEC 71.50884                                                              float   [deg] Target declination (to TCS)
    TARGTRA  168.797258                                                            float   [deg] Target right ascension (to TCS)
    USEETC   F                                                                     bool    ETC data available if true
    USESKY   T                                                                     bool    DOS Control: use Sky Monitor
    USEFOCUS T                                                                     bool    DOS Control: use focus
    HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                                               str     Hexapod trim values
    USEROTAT T                                                                     bool    DOS Control: use rotator
    ROTOFFST 461.9                                                                 float   [arcsec] Rotator offset
    ROTENBLD T                                                                     bool    Rotator enabled
    ROTRATE  0.0                                                                   float   [arcsec/min] Rotator rate
    USEGUIDR T                                                                     bool    DOS Control: use guider
    USEDONUT T                                                                     bool    DOS Control: use donuts
    SPECGRPH 9                                                                     int     Spectrograph logical name (SP)
    SPECID   3                                                                     int     Spectrograph serial number (SM)
    FEEBOX   lbnl060                                                               str     CCD Controller serial number
    VESSEL   4                                                                     int     Cryostat serial number
    FEEVER   v20160312                                                             str     CCD Controller version
    FEEPOWER ON                                                                    str     FEE power status
    FEEDMASK 2134851391                                                            int     FEE dac mask
    FEECMASK 1048575                                                               int     FEE clk mask
    CCDTEMP  -136.0659                                                             float   [deg C] CCD controller CCD temperature
    RADESYS  FK5                                                                   str     Coordinate reference frame of major/minor axes
    DOSVER   trunk                                                                 str     DOS software version
    OCSVER   1.2                                                                   float   OCS software version
    CONSTVER DESI:CURRENT                                                          str     Constants version
    INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini                      str     DOS Configuration
    DAC0     -9.0002,-8.9507                                                       str     [V] set value, measured value
    OFFSET3  0.4000000059604645,-8.9713                                            str     [V] set value, measured value
    DAC15    0.0,0.0148                                                            str     [V] set value, measured value
    DAC10    -25.0003,-25.139                                                      str     [V] set value, measured value
    DETSECD  [2058:4114, 2065:4128]                                                str     Detector section for quadrant D
    OFFSET4  2.0,6.049                                                             str     [V] set value, measured value
    PRESECB  [4250:4256, 2:2065]                                                   str     Prescan section for quadrant B
    DAC6     5.9998,6.0437                                                         str     [V] set value, measured value
    ORSECB   [2193:4249, 2066:2097]                                                str     Row overscan section for quadrant B
    CCDCFG   default_lbnl_20210128.cfg                                             str     CCD configuration file
    TRIMSECB [2193:4249, 2:2065]                                                   str     Trim section for quadrant B
    BIASSECD [2129:2192, 2130:4193]                                                str     Bias section for quadrant D
    CRYOPRES 5.973e-08                                                             str     [mb] Cryostat pressure (IP)
    SETTINGS detectors_sm_20210128.json                                            str     Name of DESI CCD settings file
    DETECTOR M1-22                                                                 str     Detector (ccd) identification
    DAC4     5.9998,6.049                                                          str     [V] set value, measured value
    TRIMSECD [2193:4249, 2130:4193]                                                str     Trim section for quadrant D
    CCDSECC  [1:2057, 2065:4128]                                                   str     CCD section for quadrant C
    CCDNAME  CCDSM3Z                                                               str     CCD name
    DAC14    0.0,0.0445                                                            str     [V] set value, measured value
    CLOCK1   9.9999,0.0                                                            str     [V] high rail, low rail
    DAC7     5.9998,6.0122                                                         str     [V] set value, measured value
    DATASECD [2193:4249, 2130:4193]                                                str     Data section for quadrant D
    CLOCK12  9.9992,2.9993                                                         str     [V] high rail, low rail
    DIGITIME 56.4532                                                               float   [s] Time to digitize image
    DAC1     -9.0002,-8.9816                                                       str     [V] set value, measured value
    CDSPARMS 400, 400, 8, 2000                                                     str     CDS parameters
    CPUTEMP  57.8554                                                               float   [deg C] CCD controller CPU temperature
    CLOCK10  9.9992,2.9993                                                         str     [V] high rail, low rail
    AMPSECD  [4114:2058, 4128:2065]                                                str     AMP section for quadrant D
    DAC5     5.9998,6.0227                                                         str     [V] set value, measured value
    ORSECA   [8:2064, 2066:2097]                                                   str     Row overscan section for quadrant A
    CCDPREP  purge,clear                                                           str     CCD prep actions
    CLOCK18  9.0,0.9999                                                            str     [V] high rail, low rail
    ORSECD   [2193:4249, 2098:2129]                                                str     Row bias section for quadrant D
    PRRSECC  [8:2064, 4194:4194]                                                   str     Row prescan section for quadrant C
    CCDTMING flatdark_lbnl_timing.txt                                              str     CCD timing file
    DELAYS   20, 20, 25, 40, 7, 3000, 7, 7, 400, 7                                 str     [10] Delay settings
    DETSECA  [1:2057, 1:2064]                                                      str     Detector section for quadrant A
    PRESECC  [1:7, 2130:4193]                                                      str     Prescan section for quadrant C
    DAC3     -9.0002,-8.9816                                                       str     [V] set value, measured value
    TRIMSECC [8:2064, 2130:4193]                                                   str     Trim section for quadrant C
    CLOCK4   9.9999,0.0                                                            str     [V] high rail, low rail
    PRRSECB  [2193:4249, 1:1]                                                      str     Row prescan section for quadrant B
    CLOCK17  9.0,0.9999                                                            str     [V] high rail, low rail
    OFFSET6  2.0,6.049                                                             str     [V] set value, measured value
    CLOCK5   9.9999,0.0                                                            str     [V] high rail, low rail
    DAC13    0.0,0.0742                                                            str     [V] set value, measured value
    OFFSET1  0.4000000059604645,-8.9816                                            str     [V] set value, measured value
    DAC12    0.0,0.0445                                                            str     [V] set value, measured value
    CLOCK11  9.9992,2.9993                                                         str     [V] high rail, low rail
    DAC16    39.9961,39.501                                                        str     [V] set value, measured value
    BLDTIME  0.3517                                                                float   [s] Time to build image
    BIASSECA [2065:2128, 2:2065]                                                   str     Bias section for quadrant A
    CLOCK7   -2.0001,3.9999                                                        str     [V] high rail, low rail
    DAC11    -25.0003,-24.7383                                                     str     [V] set value, measured value
    DAC8     -25.0003,-25.0796                                                     str     [V] set value, measured value
    ORSECC   [8:2064, 2098:2129]                                                   str     Row overscan section for quadrant C
    DATASECA [8:2064, 2:2065]                                                      str     Data section for quadrant A
    CCDSECD  [2058:4114, 2065:4128]                                                str     CCD section for quadrant D
    CAMERA   z9                                                                    str     Camera name
    CCDSECB  [2058:4114, 1:2064]                                                   str     CCD section for quadrant B
    CRYOTEMP 140.034                                                               float   [deg K] Cryostat CCD temperature
    AMPSECC  [1:2057, 4128:2065]                                                   str     AMP section for quadrant C
    CLOCK16  9.9999,3.0                                                            str     [V] high rail, low rail
    CCDSECA  [1:2057, 1:2064]                                                      str     CCD section for quadrant A
    AMPSECB  [4114:2058, 1:2064]                                                   str     AMP section for quadrant B
    CCDSIZE  4194,4256                                                             str     CCD size in pixels (rows, columns)
    PRESECD  [4250:4256, 2130:4193]                                                str     Prescan section for quadrant D
    DATASECB [2193:4249, 2:2065]                                                   str     Data section for quadrant B
    OFFSET7  2.0,6.0122                                                            str     [V] set value, measured value
    PRRSECD  [2193:4249, 4194:4194]                                                str     Row prescan section for quadrant D
    CLOCK14  9.9992,2.9993                                                         str     [V] high rail, low rail
    DETSECB  [2058:4114, 1:2064]                                                   str     Detector section for quadrant B
    PRESECA  [1:7, 2:2065]                                                         str     Prescan section for quadrant A
    OFFSET2  0.4000000059604645,-8.9507                                            str     [V] set value, measured value
    PRRSECA  [8:2064, 1:1]                                                         str     Row prescan section for quadrant A
    BIASSECB [2129:2192, 2:2065]                                                   str     Bias section for quadrant B
    DAC17    20.0008,12.0048                                                       str     [V] set value, measured value
    PGAGAIN  3                                                                     int     Controller gain
    CLOCK13  9.9992,2.9993                                                         str     [V] high rail, low rail
    DAC2     -9.0002,-8.9507                                                       str     [V] set value, measured value
    CLOCK0   9.9999,0.0                                                            str     [V] high rail, low rail
    CLOCK3   -2.0001,3.9999                                                        str     [V] high rail, low rail
    OFFSET5  2.0,6.0227                                                            str     [V] set value, measured value
    DAC9     -25.0003,-25.3319                                                     str     [V] set value, measured value
    OFFSET0  0.4000000059604645,-8.9507                                            str     [V] set value, measured value
    CLOCK15  9.9992,2.9993                                                         str     [V] high rail, low rail
    DATASECC [8:2064, 2130:4193]                                                   str     Data section for quadrant C
    AMPSECA  [1:2057, 1:2064]                                                      str     AMP section for quadrant A
    BIASSECC [2065:2128, 2130:4193]                                                str     Bias section for quadrant C
    CLOCK9   9.9992,2.9993                                                         str     [V] high rail, low rail
    CASETEMP 57.7224                                                               float   [deg C] CCD controller case temperature
    CLOCK6   9.9999,0.0                                                            str     [V] high rail, low rail
    CLOCK2   9.9999,0.0                                                            str     [V] high rail, low rail
    CLOCK8   9.9992,2.9993                                                         str     [V] high rail, low rail
    TRIMSECA [8:2064, 2:2065]                                                      str     Trim section for quadrant A
    DETSECC  [1:2057, 2065:4128]                                                   str     Detector section for quadrant C
    REQTIME  600.0                                                                 float   [s] Requested exposure time
    OBSID    kp4m20210224t084548                                                   str     Unique observation identifier
    PROCTYPE RAW                                                                   str     Data processing level
    PRODTYPE image                                                                 str     Data product type
    CHECKSUM ZnHEel9DZlEDdl9D                                                      str     HDU checksum updated 2021-07-16T15:54:37
    DATASUM  864071843                                                             str     data unit checksum updated 2021-07-16T15:54:37
    GAINA    1.436                                                                 float   e/ADU (gain applied to image)
    SATULEVA 65535.0                                                               float   saturation or non lin. level, in ADU, inc. bias
    OVERSCNA 1963.327990742693                                                     float   ADUs (gain not applied)
    OBSRDNA  2.357449062157674                                                     float   electrons (gain is applied)
    SATUELEA 91288.9210052935                                                      float   saturation or non lin. level, in electrons
    GAINB    1.496                                                                 float   e/ADU (gain applied to image)
    SATULEVB 65535.0                                                               float   saturation or non lin. level, in ADU, inc. bias
    OVERSCNB 1995.376553613327                                                     float   ADUs (gain not applied)
    OBSRDNB  2.369897651783977                                                     float   electrons (gain is applied)
    SATUELEB 95055.27667579446                                                     float   saturation or non lin. level, in electrons
    GAINC    1.625                                                                 float   e/ADU (gain applied to image)
    SATULEVC 65535.0                                                               float   saturation or non lin. level, in ADU, inc. bias
    OVERSCNC 1985.199477480042                                                     float   ADUs (gain not applied)
    OBSRDNC  2.719195420289723                                                     float   electrons (gain is applied)
    SATUELEC 103268.4258490949                                                     float   saturation or non lin. level, in electrons
    GAIND    1.531                                                                 float   e/ADU (gain applied to image)
    SATULEVD 65535.0                                                               float   saturation or non lin. level, in ADU, inc. bias
    OVERSCND 1991.999315086343                                                     float   ADUs (gain not applied)
    OBSRDND  2.425729158142353                                                     float   electrons (gain is applied)
    SATUELED 97284.3340486028                                                      float   saturation or non lin. level, in electrons
    FIBERMIN 4500                                                                  int
    MODULE   CI                                                                    str
    COSMSPLT F                                                                     bool
    MAXSPLIT 0                                                                     int
    SPLITIDS 77777                                                                 str
    OBSTYPE  SCIENCE                                                               str
    MANIFEST F                                                                     bool
    OBJECT                                                                         str
    SEQNUM   1                                                                     int
    SEQSTART 2021-02-24T08:40:31.036828                                            str
    CAMSHUT  open                                                                  str
    ACQTIME  15                                                                    int
    GUIDTIME 5.0                                                                   float
    FOCSTIME 60.0                                                                  float
    SKYTIME  60                                                                    int
    WHITESPT F                                                                     bool
    ZENITH   F                                                                     bool
    SEANNEX  F                                                                     bool
    BEYONDP  F                                                                     bool
    FIDUCIAL off                                                                   str
    BACKLIT  off                                                                   str
    AIRMASS  1.298085                                                              float
    PMREADY  T                                                                     bool
    PMCOVER  open                                                                  str
    PMCOOL   off                                                                   str
    DOMSHUTU open                                                                  str
    DOMSHUTL open                                                                  str
    DOMLIGHH off                                                                   str
    DOMLIGHL off                                                                   str
    DOMEAZ   351.802                                                               float
    DOMINPOS T                                                                     bool
    GUIDOFFR -0.156998                                                             float
    GUIDOFFD 0.276918                                                              float
    MOONDEC  23.880208                                                             float
    MOONRA   120.516716                                                            float
    MOONSEP  55.183819256517                                                       float
    INCTRL   T                                                                     bool
    INPOS    T                                                                     bool
    MNTOFFD  -60.81                                                                float
    MNTOFFR  11.99                                                                 float
    PARALLAC 172.67464                                                             float
    TARGTAZ  357.267931                                                            float
    TARGTEL  50.342958                                                             float
    TRGTOFFD 0.0                                                                   float
    TRGTOFFR 0.0                                                                   float
    ZD       39.657042                                                             float
    TILERA   168.8                                                                 float
    TILEDEC  71.5                                                                  float
    TCSST    11:37:12.275                                                          str
    TCSMJD   59269.365574                                                          float
    SKYLEVEL 6.346                                                                 float
    PMSEEING 0.97                                                                  float
    PMTRANS  96.38                                                                 float
    ACQCAM   GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                             str
    GUIDECAM GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                             str
    FOCUSCAM FOCUS1,FOCUS4,FOCUS6,FOCUS9                                           str
    SKYCAM   SKYCAM0,SKYCAM1                                                       str
    REQADC   147.76,201.05                                                         str
    ADCCORR  T                                                                     bool
    ADC1PHI  147.759999                                                            float
    ADC2PHI  201.05102                                                             float
    ADC1HOME F                                                                     bool
    ADC2HOME F                                                                     bool
    ADC1NREV -1.0                                                                  float
    ADC2NREV 0.0                                                                   float
    ADC1STAT STOPPED                                                               str
    ADC2STAT STOPPED                                                               str
    HEXPOS   1117.8,-820.8,10.2,15.2,30.5,11.3                                     str
    RESETROT F                                                                     bool
    USEPOS   T                                                                     bool
    PETALS   PETAL0,PETAL1,PETAL2,PETAL3,PETAL4,PETAL5,PETAL6,PETAL7,PETAL8,PETAL9 str
    POSCYCLE 1                                                                     int
    POSONTGT 1338                                                                  int
    POSONFRC 0.3377                                                                float
    POSDISAB 1019                                                                  int
    POSENABL 3962                                                                  int
    POSRMS   0.2291                                                                float
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
    TDEWPNT  -17.083                                                               float
    TAIRFLOW 0.0                                                                   float
    TAIRITMP 11.9                                                                  float
    TAIROTMP 12.6                                                                  float
    TAIRTEMP 9.315                                                                 float
    TCASITMP 6.6                                                                   float
    TCASOTMP 11.2                                                                  float
    TCSITEMP 10.7                                                                  float
    TCSOTEMP 10.7                                                                  float
    TCIBTEMP 0.0                                                                   float
    TCIMTEMP 0.0                                                                   float
    TCITTEMP 0.0                                                                   float
    TCOSTEMP 0.0                                                                   float
    TCOWTEMP 0.0                                                                   float
    TDBTEMP  11.0                                                                  float
    TFLOWIN  0.0                                                                   float
    TFLOWOUT 0.0                                                                   float
    TGLYCOLI 12.2                                                                  float
    TGLYCOLO 12.0                                                                  float
    THINGES  10.4                                                                  float
    THINGEW  11.0                                                                  float
    TPMAVERT 10.103                                                                float
    TPMDESIT 7.0                                                                   float
    TPMEIBT  10.2                                                                  float
    TPMEITT  9.9                                                                   float
    TPMEOBT  10.5                                                                  float
    TPMEOTT  10.2                                                                  float
    TPMNIBT  10.0                                                                  float
    TPMNITT  10.1                                                                  float
    TPMNOBT  10.7                                                                  float
    TPMNOTT  10.2                                                                  float
    TPMRTDT  10.2                                                                  float
    TPMSIBT  10.3                                                                  float
    TPMSITT  9.9                                                                   float
    TPMSOBT  10.2                                                                  float
    TPMSOTT  10.3                                                                  float
    TPMSTAT  ready                                                                 str
    TPMWIBT  10.1                                                                  float
    TPMWITT  9.8                                                                   float
    TPMWOBT  10.5                                                                  float
    TPMWOTT  10.4                                                                  float
    TPCITEMP 10.6                                                                  float
    TPCOTEMP 10.5                                                                  float
    TPR1HUM  0.0                                                                   float
    TPR1TEMP 0.0                                                                   float
    TPR2HUM  0.0                                                                   float
    TPR2TEMP 0.0                                                                   float
    TSERVO   40.0                                                                  float
    TTRSTEMP 9.7                                                                   float
    TTRWTEMP 9.6                                                                   float
    TTRUETBT -4.8                                                                  float
    TTRUETTT 9.8                                                                   float
    TTRUNTBT 10.5                                                                  float
    TTRUNTTT 10.2                                                                  float
    TTRUSTBT 10.4                                                                  float
    TTRUSTST 10.8                                                                  float
    TTRUSTTT 10.1                                                                  float
    TTRUTSBT 10.6                                                                  float
    TTRUTSMT 10.4                                                                  float
    TTRUTSTT 10.3                                                                  float
    TTRUWTBT 10.4                                                                  float
    TTRUWTTT 10.2                                                                  float
    ALARM    F                                                                     bool
    ALARM-ON F                                                                     bool
    BATTERY  100.0                                                                 float
    SECLEFT  6564.0                                                                float
    UPSSTAT  System Normal - On Line(7)                                            str
    INAMPS   71.9                                                                  float
    OUTWATTS 5200.0,7300.0,4900.0                                                  str
    COMPDEW  -14.3                                                                 float
    COMPHUM  5.2                                                                   float
    COMPAMB  22.1                                                                  float
    COMPTEMP 28.7                                                                  float
    DEWPOINT 19.3                                                                  float
    HUMIDITY 89.0                                                                  float
    PRESSURE 795.0                                                                 float
    OUTTEMP  21.2                                                                  float
    WINDDIR  323.0                                                                 float
    WINDSPD  14.7                                                                  float
    GUST     14.7                                                                  float
    AMNIENTN 15.9                                                                  float
    CFLOOR   10.1                                                                  float
    NWALLIN  16.3                                                                  float
    NWALLOUT 9.0                                                                   float
    WWALLIN  16.4                                                                  float
    WWALLOUT 10.6                                                                  float
    AMBIENTS 17.2                                                                  float
    FLOOR    14.7                                                                  float
    EWALLCMP 10.8                                                                  float
    EWALLCOU 10.3                                                                  float
    ROOF     9.4                                                                   float
    ROOFAMB  9.6                                                                   float
    DOMEBLOW 9.6                                                                   float
    DOMEBUP  9.8                                                                   float
    DOMELLOW 9.5                                                                   float
    DOMELUP  9.3                                                                   float
    DOMERLOW 9.6                                                                   float
    DOMERUP  9.2                                                                   float
    PLATFORM 8.9                                                                   float
    SHACKC   17.3                                                                  float
    SHACKW   16.9                                                                  float
    STAIRSL  9.2                                                                   float
    STAIRSM  8.9                                                                   float
    STAIRSU  9.1                                                                   float
    TELBASE  10.6                                                                  float
    UTILWALL 10.1                                                                  float
    UTILROOM 9.9                                                                   float
    SP0NIRT  139.99                                                                float
    SP0REDT  139.99                                                                float
    SP0BLUT  162.97                                                                float
    SP0NIRP  9.032e-08                                                             float
    SP0REDP  6.155e-08                                                             float
    SP0BLUP  9.115e-08                                                             float
    SP1NIRT  139.99                                                                float
    SP1REDT  139.99                                                                float
    SP1BLUT  162.97                                                                float
    SP1NIRP  4.803e-08                                                             float
    SP1REDP  5.631e-08                                                             float
    SP1BLUP  7.999e-08                                                             float
    SP2NIRT  139.99                                                                float
    SP2REDT  139.99                                                                float
    SP2BLUT  163.02                                                                float
    SP2NIRP  1.205e-07                                                             float
    SP2REDP  8.086e-08                                                             float
    SP2BLUP  7.552e-08                                                             float
    SP3NIRT  139.99                                                                float
    SP3REDT  139.96                                                                float
    SP3BLUT  162.99                                                                float
    SP3NIRP  4.194e-08                                                             float
    SP3REDP  6.898e-08                                                             float
    SP3BLUP  7.239e-08                                                             float
    SP4NIRT  139.99                                                                float
    SP4REDT  140.06                                                                float
    SP4BLUT  163.02                                                                float
    SP4NIRP  6.268e-08                                                             float
    SP4REDP  5.049e-08                                                             float
    SP4BLUP  5.575e-08                                                             float
    SP5NIRT  139.99                                                                float
    SP5REDT  139.99                                                                float
    SP5BLUT  163.02                                                                float
    SP5NIRP  7.203e-08                                                             float
    SP5REDP  6.578e-08                                                             float
    SP5BLUP  1.126e-07                                                             float
    SP6NIRT  139.99                                                                float
    SP6REDT  139.99                                                                float
    SP6BLUT  162.97                                                                float
    SP6NIRP  2.807e-07                                                             float
    SP6REDP  6.486e-08                                                             float
    SP6BLUP  6.3e-08                                                               float
    SP7NIRT  140.01                                                                float
    SP7REDT  139.99                                                                float
    SP7BLUT  162.97                                                                float
    SP7NIRP  8.201e-08                                                             float
    SP7REDP  4.282e-08                                                             float
    SP7BLUP  1.018e-07                                                             float
    SP8NIRT  139.99                                                                float
    SP8REDT  139.99                                                                float
    SP8BLUT  162.97                                                                float
    SP8NIRP  3.928e-08                                                             float
    SP8REDP  5.066e-08                                                             float
    SP8BLUP  8.30399999999999e-08                                                  float
    SP9NIRT  140.03                                                                float
    SP9REDT  140.01                                                                float
    SP9BLUT  163.02                                                                float
    SP9NIRP  5.973e-08                                                             float
    SP9REDP  7.546e-08                                                             float
    SP9BLUP  1.232e-07                                                             float
    TNFSPROC 8.6234                                                                float
    TGFAPROC 6.8851                                                                float
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
    FILENAME /exposures/desi/20210223/00077777/desi-00077777.fits.fz               str
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
    POSCNVGD F                                                                     bool
    GUIEXPID 77777                                                                 int
    IGFRMNUM 9                                                                     int
    FOCEXPID 77777                                                                 int
    IFFRMNUM 1                                                                     int
    SKYEXPID 77777                                                                 int
    ISFRMNUM 1                                                                     int
    FGFRMNUM 69                                                                    int
    FFFRMNUM 11                                                                    int
    FSFRMNUM 9                                                                     int
    HELIOCOR 0.9999737629400501                                                    float
    NSPEC    500                                                                   int     Number of spectra
    WAVEMIN  7520.0                                                                float   First wavelength [Angstroms]
    WAVEMAX  9824.0                                                                float   Last wavelength [Angstroms]
    WAVESTEP 0.8                                                                   float   Wavelength step size [Angstroms]
    SPECTER  0.10.0                                                                str     https://github.com/desihub/specter
    IN_PSF   SPECPROD/exposures/20210223/00077777/psf-z9-00077777.fits             str     Input sp
    IN_IMG   SPECPROD/preproc/20210223/00077777/preproc-z9-00077777.fits           str
    ORIG_PSF SPECPROD/calibnight/20210223/psfnight-z9-20210223.fits                str
    BUNIT    10**-17 erg/(s cm2 Angstrom)                                          str
    TSNRALPH 2.77496942906376                                                      float
    IN_FRAME SPECPROD/exposures/20210223/00077777/frame-z9-00077777.fits           str
    FIBERFLT SPECPROD/calibnight/20210223/fiberflatnight-z9-20210223.fits          str
    IN_SKY   SPECPROD/exposures/20210223/00077777/sky-z9-00077777.fits             str
    IN_CALIB SPECPROD/exposures/20210223/00077777/fluxcalib-z9-00077777.fits       str
    ======== ===================================================================== ======= ===============================================

Data: FITS image [float32, 2881x500]

HDU1
----

EXTNAME = IVAR

Inverse variance of flux (*i.e.* ``error**-2``).

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2881             int
    NAXIS2   500              int
    CHECKSUM ZhXFagUETgUEZgUE str  HDU checksum updated 2021-07-16T15:54:37
    DATASUM  1428281379       str  data unit checksum updated 2021-07-16T15:54:37
    ======== ================ ==== ==============================================

Data: FITS image [float32, 2881x500]

HDU2
----

EXTNAME = MASK

Mask of spectra; 0=good.

Prior to desispec/0.24.0 and software release 18.9, the MASK HDU was compressed.

TODO: add documentation link to what bits mean what.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2881             int
    NAXIS2   500              int
    BSCALE   1                int
    BZERO    2147483648       int
    CHECKSUM UA8FU87FUA7FU77F str  HDU checksum updated 2021-07-16T15:54:38
    DATASUM  413756347        str  data unit checksum updated 2021-07-16T15:54:38
    ======== ================ ==== ==============================================

Data: FITS image [int32, 2881x500]

HDU3
----

EXTNAME = WAVELENGTH

Wavelengths at which flux is measured.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2881             int
    BUNIT    Angstrom         str
    CHECKSUM jbdTkaZRjabRjaZR str  HDU checksum updated 2021-07-16T15:54:38
    DATASUM  3106662670       str  data unit checksum updated 2021-07-16T15:54:38
    ======== ================ ==== ==============================================

Data: FITS image [float64, 2881]

HDU4
----

EXTNAME = RESOLUTION

Diagonal elements of convolution matrix describing spectral resolution.

TODO: add code example for using this.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2881             int
    NAXIS2   11               int
    NAXIS3   500              int
    CHECKSUM fiDjhZAiffAifZAi str  HDU checksum updated 2021-07-16T15:54:41
    DATASUM  2514154349       str  data unit checksum updated 2021-07-16T15:54:41
    ======== ================ ==== ==============================================

Data: FITS image [float32, 2881x11x500]

HDU5
----

EXTNAME = FIBERMAP

Fibermap of what targets were assigned to what fibers.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ===================================================================== ======= ==============================================
    KEY      Example Value                                                         Type    Comment
    ======== ===================================================================== ======= ==============================================
    NAXIS1   393                                                                   int     length of dimension 1
    NAXIS2   500                                                                   int     length of dimension 2
    TILEID   80782                                                                 int
    TILERA   168.8                                                                 float
    TILEDEC  71.5                                                                  float
    FIELDROT 0.0750610438669607                                                    float
    FA_PLAN  2022-07-01T00:00:00.000                                               str
    FA_HA    0.0                                                                   float
    FA_RUN   2021-02-22T00:00:00                                                   str
    REQRA    168.8                                                                 float
    REQDEC   71.5                                                                  float
    FIELDNUM 0                                                                     int
    FA_VER   2.1.1.dev2706                                                         str
    FA_SURV  sv1                                                                   str
    DESIROOT /global/cfs/cdirs/desi                                                str
    GFA      DESIROOT/target/catalogs/dr9/0.50.0/gfas                              str
    SCND     DESIROOT/target/catalogs/dr9/0.50.0/targets/sv1/secondary/dark        str
    SKY      DESIROOT/target/catalogs/dr9/0.50.0/skies                             str
    SKYSUPP  DESIROOT/target/catalogs/gaiadr2/0.50.0/skies-supp                    str
    TARG     DESIROOT/target/catalogs/dr9/0.50.0/targets/sv1/resolve/dark          str
    TARG2    DESIROOT/target/catalogs/gaiadr2/0.50.0/targets/sv1/resolve/supp      str
    DR       dr9                                                                   str
    DTVER    0.50.0                                                                str
    FAFLAVOR sv1backup1                                                            str
    M31CEN   n                                                                     str
    FAOUTDIR /global/cfs/cdirs/desi/survey/fiberassign/SV1/20210223/               str
    PMTIME   2021-02-23T00:00:00.000                                               str
    PRIORITY default                                                               str
    RUNDATE  2021-02-22T00:00:00                                                   str
    SCTARG   STD_WD,MWS_MAIN_BROAD,BACKUP_FAINT                                    str
    SCSTD    STD_WD,STD_BRIGHT                                                     str
    OBSCON   DARK|GRAY|BRIGHT                                                      str
    BZERO    32768                                                                 int
    BSCALE   1                                                                     int
    MODULE   CI                                                                    str
    EXPID    77777                                                                 int
    EXPFRAME 0                                                                     int
    FRAMES   None                                                                  Unknown
    COSMSPLT F                                                                     bool
    MAXSPLIT 0                                                                     int
    SPLITIDS 77777                                                                 str
    FIBASSGN /data/tiles/SVN_tiles/080/fiberassign-080782.fits.gz                  str
    FLAVOR   science                                                               str
    OBSTYPE  SCIENCE                                                               str
    SEQUENCE DESI                                                                  str
    MANIFEST F                                                                     bool
    OBJECT                                                                         str
    PURPOSE  SV                                                                    str
    PROGRAM  sv1backup1                                                            str
    PROPID   2019B-5000                                                            str
    OBSERVER Adam Myers                                                            str
    LEAD     Ann Elliott                                                           str
    INSTRUME DESI                                                                  str
    OBSERVAT KPNO                                                                  str
    OBS-LAT  31.96403                                                              str
    OBS-LONG -111.59989                                                            str
    OBS-ELEV 2097.0                                                                float
    TELESCOP KPNO 4.0-m telescope                                                  str
    CORRCTOR DESI Corrector                                                        str
    SEQNUM   1                                                                     int
    NIGHT    20210223                                                              int
    SEQSTART 2021-02-24T08:40:31.036828                                            str
    TIMESYS  UTC                                                                   str
    DATE-OBS 2021-02-24T08:45:48.792386816                                         str
    TIME-OBS 2021-02-24T08:45:48.792386816                                         str
    MJD-OBS  59269.36514806                                                        float
    OPENSHUT None                                                                  Unknown
    CAMSHUT  open                                                                  str
    ST       11:37:12.748000                                                       str
    ACQTIME  15                                                                    int
    GUIDTIME 5.0                                                                   float
    FOCSTIME 60.0                                                                  float
    SKYTIME  60                                                                    int
    WHITESPT F                                                                     bool
    ZENITH   F                                                                     bool
    SEANNEX  F                                                                     bool
    BEYONDP  F                                                                     bool
    FIDUCIAL off                                                                   str
    BACKLIT  off                                                                   str
    AIRMASS  1.298085                                                              float
    FOCUS    1117.8,-820.8,10.2,15.2,30.5,462.4                                    str
    VCCD     ON                                                                    str
    TRUSTEMP 10.533                                                                float
    PMIRTEMP 10.088                                                                float
    PMREADY  T                                                                     bool
    PMCOVER  open                                                                  str
    PMCOOL   off                                                                   str
    DOMSHUTU open                                                                  str
    DOMSHUTL open                                                                  str
    DOMLIGHH off                                                                   str
    DOMLIGHL off                                                                   str
    DOMEAZ   351.802                                                               float
    DOMINPOS T                                                                     bool
    EPOCH    2000.0                                                                float
    GUIDOFFR -0.156998                                                             float
    GUIDOFFD 0.276918                                                              float
    MOONDEC  23.880208                                                             float
    MOONRA   120.516716                                                            float
    MOONSEP  55.183819256517                                                       float
    MOUNTAZ  357.580192                                                            float
    MOUNTDEC 71.50884                                                              float
    MOUNTEL  50.367086                                                             float
    MOUNTHA  4.871119                                                              float
    INCTRL   T                                                                     bool
    INPOS    T                                                                     bool
    MNTOFFD  -60.81                                                                float
    MNTOFFR  11.99                                                                 float
    PARALLAC 172.67464                                                             float
    SKYDEC   71.50884                                                              float
    SKYRA    168.797258                                                            float
    TARGTDEC 71.50884                                                              float
    TARGTRA  168.797258                                                            float
    TARGTAZ  357.267931                                                            float
    TARGTEL  50.342958                                                             float
    TRGTOFFD 0.0                                                                   float
    TRGTOFFR 0.0                                                                   float
    ZD       39.657042                                                             float
    TCSST    11:37:12.275                                                          str
    TCSMJD   59269.365574                                                          float
    USEETC   F                                                                     bool
    SKYLEVEL 6.346                                                                 float
    PMSEEING 0.97                                                                  float
    PMTRANS  96.38                                                                 float
    ACQCAM   GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                             str
    GUIDECAM GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                             str
    FOCUSCAM FOCUS1,FOCUS4,FOCUS6,FOCUS9                                           str
    SKYCAM   SKYCAM0,SKYCAM1                                                       str
    REQADC   147.76,201.05                                                         str
    ADCCORR  T                                                                     bool
    ADC1PHI  147.759999                                                            float
    ADC2PHI  201.05102                                                             float
    ADC1HOME F                                                                     bool
    ADC2HOME F                                                                     bool
    ADC1NREV -1.0                                                                  float
    ADC2NREV 0.0                                                                   float
    ADC1STAT STOPPED                                                               str
    ADC2STAT STOPPED                                                               str
    USESKY   T                                                                     bool
    USEFOCUS T                                                                     bool
    HEXPOS   1117.8,-820.8,10.2,15.2,30.5,11.3                                     str
    HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                                               str
    USEROTAT T                                                                     bool
    ROTOFFST 461.9                                                                 float
    ROTENBLD T                                                                     bool
    ROTRATE  0.0                                                                   float
    RESETROT F                                                                     bool
    USEPOS   T                                                                     bool
    PETALS   PETAL0,PETAL1,PETAL2,PETAL3,PETAL4,PETAL5,PETAL6,PETAL7,PETAL8,PETAL9 str
    POSCYCLE 1                                                                     int
    POSONTGT 1338                                                                  int
    POSONFRC 0.3377                                                                float
    POSDISAB 1019                                                                  int
    POSENABL 3962                                                                  int
    POSRMS   0.2291                                                                float
    POSITER  1                                                                     int
    POSFRACT 0.95                                                                  float
    POSTOLER 0.005                                                                 float
    POSMVALL T                                                                     bool
    USEGUIDR T                                                                     bool
    GUIDMODE catalog                                                               str
    USEAOS   F                                                                     bool
    USEDONUT T                                                                     bool
    USESPCTR T                                                                     bool
    SPCGRPHS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                               str
    ILLSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                               str
    CCDSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                               str
    TDEWPNT  -17.083                                                               float
    TAIRFLOW 0.0                                                                   float
    TAIRITMP 11.9                                                                  float
    TAIROTMP 12.6                                                                  float
    TAIRTEMP 9.315                                                                 float
    TCASITMP 6.6                                                                   float
    TCASOTMP 11.2                                                                  float
    TCSITEMP 10.7                                                                  float
    TCSOTEMP 10.7                                                                  float
    TCIBTEMP 0.0                                                                   float
    TCIMTEMP 0.0                                                                   float
    TCITTEMP 0.0                                                                   float
    TCOSTEMP 0.0                                                                   float
    TCOWTEMP 0.0                                                                   float
    TDBTEMP  11.0                                                                  float
    TFLOWIN  0.0                                                                   float
    TFLOWOUT 0.0                                                                   float
    TGLYCOLI 12.2                                                                  float
    TGLYCOLO 12.0                                                                  float
    THINGES  10.4                                                                  float
    THINGEW  11.0                                                                  float
    TPMAVERT 10.103                                                                float
    TPMDESIT 7.0                                                                   float
    TPMEIBT  10.2                                                                  float
    TPMEITT  9.9                                                                   float
    TPMEOBT  10.5                                                                  float
    TPMEOTT  10.2                                                                  float
    TPMNIBT  10.0                                                                  float
    TPMNITT  10.1                                                                  float
    TPMNOBT  10.7                                                                  float
    TPMNOTT  10.2                                                                  float
    TPMRTDT  10.2                                                                  float
    TPMSIBT  10.3                                                                  float
    TPMSITT  9.9                                                                   float
    TPMSOBT  10.2                                                                  float
    TPMSOTT  10.3                                                                  float
    TPMSTAT  ready                                                                 str
    TPMWIBT  10.1                                                                  float
    TPMWITT  9.8                                                                   float
    TPMWOBT  10.5                                                                  float
    TPMWOTT  10.4                                                                  float
    TPCITEMP 10.6                                                                  float
    TPCOTEMP 10.5                                                                  float
    TPR1HUM  0.0                                                                   float
    TPR1TEMP 0.0                                                                   float
    TPR2HUM  0.0                                                                   float
    TPR2TEMP 0.0                                                                   float
    TSERVO   40.0                                                                  float
    TTRSTEMP 9.7                                                                   float
    TTRWTEMP 9.6                                                                   float
    TTRUETBT -4.8                                                                  float
    TTRUETTT 9.8                                                                   float
    TTRUNTBT 10.5                                                                  float
    TTRUNTTT 10.2                                                                  float
    TTRUSTBT 10.4                                                                  float
    TTRUSTST 10.8                                                                  float
    TTRUSTTT 10.1                                                                  float
    TTRUTSBT 10.6                                                                  float
    TTRUTSMT 10.4                                                                  float
    TTRUTSTT 10.3                                                                  float
    TTRUWTBT 10.4                                                                  float
    TTRUWTTT 10.2                                                                  float
    ALARM    F                                                                     bool
    ALARM-ON F                                                                     bool
    BATTERY  100.0                                                                 float
    SECLEFT  6564.0                                                                float
    UPSSTAT  System Normal - On Line(7)                                            str
    INAMPS   71.9                                                                  float
    OUTWATTS 5200.0,7300.0,4900.0                                                  str
    COMPDEW  -14.3                                                                 float
    COMPHUM  5.2                                                                   float
    COMPAMB  22.1                                                                  float
    COMPTEMP 28.7                                                                  float
    DEWPOINT 19.3                                                                  float
    HUMIDITY 89.0                                                                  float
    PRESSURE 795.0                                                                 float
    OUTTEMP  21.2                                                                  float
    WINDDIR  323.0                                                                 float
    WINDSPD  14.7                                                                  float
    GUST     14.7                                                                  float
    AMNIENTN 15.9                                                                  float
    CFLOOR   10.1                                                                  float
    NWALLIN  16.3                                                                  float
    NWALLOUT 9.0                                                                   float
    WWALLIN  16.4                                                                  float
    WWALLOUT 10.6                                                                  float
    AMBIENTS 17.2                                                                  float
    FLOOR    14.7                                                                  float
    EWALLCMP 10.8                                                                  float
    EWALLCOU 10.3                                                                  float
    ROOF     9.4                                                                   float
    ROOFAMB  9.6                                                                   float
    DOMEBLOW 9.6                                                                   float
    DOMEBUP  9.8                                                                   float
    DOMELLOW 9.5                                                                   float
    DOMELUP  9.3                                                                   float
    DOMERLOW 9.6                                                                   float
    DOMERUP  9.2                                                                   float
    PLATFORM 8.9                                                                   float
    SHACKC   17.3                                                                  float
    SHACKW   16.9                                                                  float
    STAIRSL  9.2                                                                   float
    STAIRSM  8.9                                                                   float
    STAIRSU  9.1                                                                   float
    TELBASE  10.6                                                                  float
    UTILWALL 10.1                                                                  float
    UTILROOM 9.9                                                                   float
    SP0NIRT  139.99                                                                float
    SP0REDT  139.99                                                                float
    SP0BLUT  162.97                                                                float
    SP0NIRP  9.032e-08                                                             float
    SP0REDP  6.155e-08                                                             float
    SP0BLUP  9.115e-08                                                             float
    SP1NIRT  139.99                                                                float
    SP1REDT  139.99                                                                float
    SP1BLUT  162.97                                                                float
    SP1NIRP  4.803e-08                                                             float
    SP1REDP  5.631e-08                                                             float
    SP1BLUP  7.999e-08                                                             float
    SP2NIRT  139.99                                                                float
    SP2REDT  139.99                                                                float
    SP2BLUT  163.02                                                                float
    SP2NIRP  1.205e-07                                                             float
    SP2REDP  8.086e-08                                                             float
    SP2BLUP  7.552e-08                                                             float
    SP3NIRT  139.99                                                                float
    SP3REDT  139.96                                                                float
    SP3BLUT  162.99                                                                float
    SP3NIRP  4.194e-08                                                             float
    SP3REDP  6.898e-08                                                             float
    SP3BLUP  7.239e-08                                                             float
    SP4NIRT  139.99                                                                float
    SP4REDT  140.06                                                                float
    SP4BLUT  163.02                                                                float
    SP4NIRP  6.268e-08                                                             float
    SP4REDP  5.049e-08                                                             float
    SP4BLUP  5.575e-08                                                             float
    SP5NIRT  139.99                                                                float
    SP5REDT  139.99                                                                float
    SP5BLUT  163.02                                                                float
    SP5NIRP  7.203e-08                                                             float
    SP5REDP  6.578e-08                                                             float
    SP5BLUP  1.126e-07                                                             float
    SP6NIRT  139.99                                                                float
    SP6REDT  139.99                                                                float
    SP6BLUT  162.97                                                                float
    SP6NIRP  2.807e-07                                                             float
    SP6REDP  6.486e-08                                                             float
    SP6BLUP  6.3e-08                                                               float
    SP7NIRT  140.01                                                                float
    SP7REDT  139.99                                                                float
    SP7BLUT  162.97                                                                float
    SP7NIRP  8.201e-08                                                             float
    SP7REDP  4.282e-08                                                             float
    SP7BLUP  1.018e-07                                                             float
    SP8NIRT  139.99                                                                float
    SP8REDT  139.99                                                                float
    SP8BLUT  162.97                                                                float
    SP8NIRP  3.928e-08                                                             float
    SP8REDP  5.066e-08                                                             float
    SP8BLUP  8.30399999999999e-08                                                  float
    SP9NIRT  140.03                                                                float
    SP9REDT  140.01                                                                float
    SP9BLUT  163.02                                                                float
    SP9NIRP  5.973e-08                                                             float
    SP9REDP  7.546e-08                                                             float
    SP9BLUP  1.232e-07                                                             float
    RADESYS  FK5                                                                   str
    TNFSPROC 8.6234                                                                float
    TGFAPROC 6.8851                                                                float
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
    FILENAME /exposures/desi/20210223/00077777/desi-00077777.fits.fz               str
    EXCLUDED                                                                       str
    DOSVER   trunk                                                                 str
    OCSVER   1.2                                                                   float
    CONSTVER DESI:CURRENT                                                          str
    INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini                      str
    REQTIME  600.0                                                                 float
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
    GUIEXPID 77777                                                                 int
    IGFRMNUM 9                                                                     int
    FOCEXPID 77777                                                                 int
    IFFRMNUM 1                                                                     int
    SKYEXPID 77777                                                                 int
    ISFRMNUM 1                                                                     int
    FGFRMNUM 69                                                                    int
    FFFRMNUM 11                                                                    int
    FSFRMNUM 9                                                                     int
    DELTARA  None                                                                  Unknown
    DELTADEC None                                                                  Unknown
    FVCTIME  2.0                                                                   float
    GSGUIDE0 (991.24,839.27),(845.05,1414.39)                                      str
    GSGUIDE2 (826.78,1039.48),(605.01,881.95)                                      str
    GSGUIDE3 (411.70,760.03),(210.35,1664.90)                                      str
    GSGUIDE5 (689.08,1584.37),(427.94,922.92)                                      str
    GSGUIDE7 (256.50,569.43),(619.84,959.25)                                       str
    GSGUIDE8 (780.97,1486.45),(811.23,376.06)                                      str
    ARCHIVE  /exposures/desi/20210223/00077777/guide-00077777.fits.fz              str
    GUIDEFIL guide-00077777.fits.fz                                                str
    COORDFIL coordinates-00077777.fits                                             str
    EXPTIME  600.079                                                               float
    VCCDON   2021-02-16T23:21:25.955005                                            str
    VCCDSEC  639321.4                                                              float
    SPECGRPH 9                                                                     int
    SPECID   3                                                                     int
    FEEBOX   lbnl060                                                               str
    VESSEL   4                                                                     int
    FEEVER   v20160312                                                             str
    FEEPOWER ON                                                                    str
    FEEDMASK 2134851391                                                            int
    FEECMASK 1048575                                                               int
    CCDTEMP  -136.0659                                                             float
    DAC0     -9.0002,-8.9507                                                       str
    OFFSET3  0.4000000059604645,-8.9713                                            str
    DAC15    0.0,0.0148                                                            str
    DAC10    -25.0003,-25.139                                                      str
    DETSECD  [2058:4114, 2065:4128]                                                str
    OFFSET4  2.0,6.049                                                             str
    PRESECB  [4250:4256, 2:2065]                                                   str
    DAC6     5.9998,6.0437                                                         str
    ORSECB   [2193:4249, 2066:2097]                                                str
    CCDCFG   default_lbnl_20210128.cfg                                             str
    TRIMSECB [2193:4249, 2:2065]                                                   str
    BIASSECD [2129:2192, 2130:4193]                                                str
    CRYOPRES 5.973e-08                                                             str
    SETTINGS detectors_sm_20210128.json                                            str
    DETECTOR M1-22                                                                 str
    DAC4     5.9998,6.049                                                          str
    TRIMSECD [2193:4249, 2130:4193]                                                str
    CCDSECC  [1:2057, 2065:4128]                                                   str
    CCDNAME  CCDSM3Z                                                               str
    DAC14    0.0,0.0445                                                            str
    CLOCK1   9.9999,0.0                                                            str
    DAC7     5.9998,6.0122                                                         str
    DATASECD [2193:4249, 2130:4193]                                                str
    CLOCK12  9.9992,2.9993                                                         str
    DIGITIME 56.4532                                                               float
    DAC1     -9.0002,-8.9816                                                       str
    CDSPARMS 400, 400, 8, 2000                                                     str
    CPUTEMP  57.8554                                                               float
    CLOCK10  9.9992,2.9993                                                         str
    AMPSECD  [4114:2058, 4128:2065]                                                str
    DAC5     5.9998,6.0227                                                         str
    ORSECA   [8:2064, 2066:2097]                                                   str
    CCDPREP  purge,clear                                                           str
    CLOCK18  9.0,0.9999                                                            str
    ORSECD   [2193:4249, 2098:2129]                                                str
    PRRSECC  [8:2064, 4194:4194]                                                   str
    CCDTMING flatdark_lbnl_timing.txt                                              str
    DELAYS   20, 20, 25, 40, 7, 3000, 7, 7, 400, 7                                 str
    DETSECA  [1:2057, 1:2064]                                                      str
    PRESECC  [1:7, 2130:4193]                                                      str
    DAC3     -9.0002,-8.9816                                                       str
    TRIMSECC [8:2064, 2130:4193]                                                   str
    CLOCK4   9.9999,0.0                                                            str
    PRRSECB  [2193:4249, 1:1]                                                      str
    CLOCK17  9.0,0.9999                                                            str
    OFFSET6  2.0,6.049                                                             str
    CLOCK5   9.9999,0.0                                                            str
    DAC13    0.0,0.0742                                                            str
    OFFSET1  0.4000000059604645,-8.9816                                            str
    DAC12    0.0,0.0445                                                            str
    CLOCK11  9.9992,2.9993                                                         str
    DAC16    39.9961,39.501                                                        str
    BLDTIME  0.3517                                                                float
    BIASSECA [2065:2128, 2:2065]                                                   str
    CLOCK7   -2.0001,3.9999                                                        str
    DAC11    -25.0003,-24.7383                                                     str
    DAC8     -25.0003,-25.0796                                                     str
    ORSECC   [8:2064, 2098:2129]                                                   str
    DATASECA [8:2064, 2:2065]                                                      str
    CCDSECD  [2058:4114, 2065:4128]                                                str
    CAMERA   z9                                                                    str
    CCDSECB  [2058:4114, 1:2064]                                                   str
    CRYOTEMP 140.034                                                               float
    AMPSECC  [1:2057, 4128:2065]                                                   str
    CLOCK16  9.9999,3.0                                                            str
    CCDSECA  [1:2057, 1:2064]                                                      str
    AMPSECB  [4114:2058, 1:2064]                                                   str
    CCDSIZE  4194,4256                                                             str
    PRESECD  [4250:4256, 2130:4193]                                                str
    DATASECB [2193:4249, 2:2065]                                                   str
    OFFSET7  2.0,6.0122                                                            str
    PRRSECD  [2193:4249, 4194:4194]                                                str
    CLOCK14  9.9992,2.9993                                                         str
    DETSECB  [2058:4114, 1:2064]                                                   str
    PRESECA  [1:7, 2:2065]                                                         str
    OFFSET2  0.4000000059604645,-8.9507                                            str
    PRRSECA  [8:2064, 1:1]                                                         str
    BIASSECB [2129:2192, 2:2065]                                                   str
    DAC17    20.0008,12.0048                                                       str
    PGAGAIN  3                                                                     int
    CLOCK13  9.9992,2.9993                                                         str
    DAC2     -9.0002,-8.9507                                                       str
    CLOCK0   9.9999,0.0                                                            str
    CLOCK3   -2.0001,3.9999                                                        str
    OFFSET5  2.0,6.0227                                                            str
    DAC9     -25.0003,-25.3319                                                     str
    OFFSET0  0.4000000059604645,-8.9507                                            str
    CLOCK15  9.9992,2.9993                                                         str
    DATASECC [8:2064, 2130:4193]                                                   str
    AMPSECA  [1:2057, 1:2064]                                                      str
    BIASSECC [2065:2128, 2130:4193]                                                str
    CLOCK9   9.9992,2.9993                                                         str
    CASETEMP 57.7224                                                               float
    CLOCK6   9.9999,0.0                                                            str
    CLOCK2   9.9999,0.0                                                            str
    CLOCK8   9.9992,2.9993                                                         str
    TRIMSECA [8:2064, 2:2065]                                                      str
    DETSECC  [1:2057, 2065:4128]                                                   str
    OBSID    kp4m20210224t084548                                                   str
    PROCTYPE RAW                                                                   str
    PRODTYPE image                                                                 str
    GAINA    1.436                                                                 float
    SATULEVA 65535.0                                                               float
    OVERSCNA 1963.327990742693                                                     float
    OBSRDNA  2.357449062157674                                                     float
    SATUELEA 91288.9210052935                                                      float
    GAINB    1.496                                                                 float
    SATULEVB 65535.0                                                               float
    OVERSCNB 1995.376553613327                                                     float
    OBSRDNB  2.369897651783977                                                     float
    SATUELEB 95055.27667579446                                                     float
    GAINC    1.625                                                                 float
    SATULEVC 65535.0                                                               float
    OVERSCNC 1985.199477480042                                                     float
    OBSRDNC  2.719195420289723                                                     float
    SATUELEC 103268.4258490949                                                     float
    GAIND    1.531                                                                 float
    SATULEVD 65535.0                                                               float
    OVERSCND 1991.999315086343                                                     float
    OBSRDND  2.425729158142353                                                     float
    SATUELED 97284.3340486028                                                      float
    FIBERMIN 4500                                                                  int
    CHECKSUM kNA3lN60kNA0kN50                                                      str     HDU checksum updated 2021-07-16T15:54:42
    DATASUM  2789833251                                                            str     data unit checksum updated 2021-07-16T15:54:42
    ENCODING ascii                                                                 str
    ======== ===================================================================== ======= ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

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
SV1_DESI_TARGET [1]_  int64
SV1_BGS_TARGET [1]_   int64
SV1_MWS_TARGET [1]_   int64
SV1_SCND_TARGET [1]_  int64
DESI_TARGET           int64
BGS_TARGET            int64
MWS_TARGET            int64
SCND_TARGET           int64
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
PSF_TO_FIBER_SPECFLUX float64
===================== ======= ===== ===========

.. [1] Optional

HDU6
----

EXTNAME = CHI2PIX

:math:`chi^2` of PSF fit to CCD data per flux bin.  Large values indicate poor fits,
*e.g.* due to unmasked cosmics or other CCD defects.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2881             int  Number of wavelengths
    NAXIS2   500              int  Number of spectra
    CHECKSUM cBAJe94GcAAGc93G str  HDU checksum updated 2021-07-16T15:54:42
    DATASUM  3947425746       str  data unit checksum updated 2021-07-16T15:54:42
    ======== ================ ==== ==============================================

Data: FITS image [float32, 2881x500]

HDU7
----

EXTNAME = SCORES

Scores / metrics measured from the spectra for use in QA and systematics
studies.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   160              int  length of dimension 1
    NAXIS2   500              int  length of dimension 2
    ENCODING ascii            str
    CHECKSUM YanYbZkXZakXaYkX str  HDU checksum updated 2021-07-16T15:54:42
    DATASUM  3675881366       str  data unit checksum updated 2021-07-16T15:54:42
    ======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Note: the ``_C`` in the column names refers to the camera for this particular
frame, *e.g.* ``_B``, ``_R``, or ``_Z``.  These are designed such that the
SCORES tables from individual frames can be later combined into a summary
table for the exposure.

TODO: document wavelength ranges covered per camera.

.. rst-class:: columns

===================== ======= ===== ============================================
Name                  Type    Units Description
===================== ======= ===== ============================================
SUM_RAW_COUNT_Z       float64       sum counts in wave. range 7600,9800A
MEDIAN_RAW_COUNT_Z    float64       median counts/A in wave. range 7600,9800A
MEDIAN_RAW_SNR_Z      float64       median SNR/sqrt(A) in wave. range 7600,9800A
SUM_FFLAT_COUNT_Z     float64       sum counts in wave. range 7600,9800A
MEDIAN_FFLAT_COUNT_Z  float64       median counts/A in wave. range 7600,9800A
MEDIAN_FFLAT_SNR_Z    float64       median SNR/sqrt(A) in wave. range 7600,9800A
SUM_SKYSUB_COUNT_Z    float64       sum counts in wave. range 7600,9800A
MEDIAN_SKYSUB_COUNT_Z float64       median counts/A in wave. range 7600,9800A
MEDIAN_SKYSUB_SNR_Z   float64       median SNR/sqrt(A) in wave. range 7600,9800A
SUM_CALIB_COUNT_Z     float64       sum counts in wave. range 7600,9800A
MEDIAN_CALIB_COUNT_Z  float64       median counts/A in wave. range 7600,9800A
MEDIAN_CALIB_SNR_Z    float64       median SNR/sqrt(A) in wave. range 7600,9800A
TSNR2_GPBDARK_Z       float64       from calc_frame_tsnr
TSNR2_ELG_Z           float64       from calc_frame_tsnr
TSNR2_GPBBRIGHT_Z     float64       from calc_frame_tsnr
TSNR2_LYA_Z           float64       from calc_frame_tsnr
TSNR2_BGS_Z           float64       from calc_frame_tsnr
TSNR2_GPBBACKUP_Z     float64       from calc_frame_tsnr
TSNR2_QSO_Z           float64       from calc_frame_tsnr
TSNR2_LRG_Z           float64       from calc_frame_tsnr
===================== ======= ===== ============================================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
