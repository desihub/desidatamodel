===========================
fiberflat-CAMERA-EXPID.fits
===========================

:Summary: This file contains the fiberflat such that newflux = rawflux/fiberflat.
:Naming Convention: ``fiberflat-{CAMERA}-{EXPID}.fits``, where ``{camera}`` is the camera
    name (*e.g.* b0, r1, z9) and ``{EXPID}`` is the zero padded 8-digit exposure ID.
:Regex: ``fiberflat-[brz][0-9]-[0-9]{8}\.fits``
:File Type: FITS, 16 MB

Contents
========

====== ================ ======== ===================================
Number EXTNAME          Type     Contents
====== ================ ======== ===================================
HDU0_  FIBERFLAT        IMAGE    fiberflat[nspec, nwave]
HDU1_  IVAR             IMAGE    inverse variance of fiberflat
HDU2_  MASK             IMAGE    bitmask of fiberflat (0=good)
HDU3_  MEANSPEC         IMAGE    average spectrum[nwave]
HDU4_  WAVELENGTH       IMAGE    wavelength grid[nwave] in Angstroms
HDU5_  STDSTAR_FIBERMAP BINTABLE fibermap
====== ================ ======== ===================================

Note: the FIBERMAP HDU may be dropped from future versions


FITS Header Units
=================

HDU0
----

EXTNAME = FIBERFLAT

Fiber flat field correction to homogeneize the response among fibers of the same camera, for each wavelength. 2D array of dimension [nspec, nwave]. nspec is the number of fibers per camera. nwave in the length of the wavelength array. The fiber flat field of all fibers share the same wavelength grid (given in HDU WAVELENGTH). This file is the fiber flat derived for the flat exposure EXPID. It is an intermediate file used as input for the nightly fiber flat.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

Header keywords are inherited from the input Frame file.

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== =========================================================== ======= ====================================================
    KEY      Example Value                                               Type    Comment
    ======== =========================================================== ======= ====================================================
    NAXIS1   2881                                                        int
    NAXIS2   500                                                         int
    EXPID    70882                                                       int     Exposure number
    EXPFRAME 0                                                           int     Frame number
    FLAVOR   science                                                     str     Observation type
    SEQUENCE Spectrographs                                               str     OCS Sequence name
    PURPOSE  Commissioning                                               str     Purpose of observing night
    PROGRAM  CALIB DESI-CALIB-00 LEDs only                               str     Program name
    PROPID   2019B-5000                                                  str     Proposal ID
    OBSERVER DESIObserver                                                str     Names of observers
    LEAD     RunManager                                                  str     Lead observer
    INSTRUME DESI                                                        str     Instrument name
    OBSERVAT KPNO                                                        str     Observatory name
    OBS-LAT  31.96403                                                    str     [deg] Observatory latitude
    OBS-LONG -111.59989                                                  str     [deg] Observatory east longitude
    OBS-ELEV 2097.0                                                      float   [m] Observatory elevation
    TELESCOP KPNO 4.0-m telescope                                        str     Telescope name
    CORRCTOR DESI Corrector                                              str     Corrector Identification
    NIGHT    20210105                                                    int     Observing night
    TIMESYS  UTC                                                         str     Time system used for date-obs
    DATE-OBS 2021-01-06T00:14:34.487889920                               str     [UTC] Observation data and start tim
    TIME-OBS 2021-01-05T00:14:34.487889920                               str     [UTC] Observation start time
    MJD-OBS  59220.01012139                                              float   Modified Julian Date of observation
    ST       23:51:23.200000                                             str     Local Sidereal time at observation start (HH:MM
    EXPTIME  120.035                                                     float   [s] Actual exposure time
    DELTARA  0.0                                                         float   [arcsec] Offset], right ascension, observer inp
    DELTADEC 0.0                                                         float   [arcsec] Offset], declination, observer input
    VCCD     ON                                                          str     True (ON) if CCD voltage is on
    VCCDON   2020-12-09T21:23:25.450662                                  str     Time when CCD voltage was turned on
    VCCDSEC  2343238.6                                                   float   [s] CCD on time in seconds
    EPOCH    2000.0                                                      float   Epoch of observation
    SPECGRPH 9                                                           int     Spectrograph logical name (SP)
    SPECID   3                                                           int     Spectrograph serial number (SM)
    FEEBOX   lbnl060                                                     str     CCD Controller serial number
    VESSEL   4                                                           int     Cryostat serial number
    FEEVER   v20160312                                                   str     CCD Controller version
    FEEPOWER ON                                                          str     FEE power status
    FEEDMASK 2134851391                                                  int     FEE dac mask
    FEECMASK 1048575                                                     int     FEE clk mask
    CCDTEMP  -136.0969                                                   float   [deg C] CCD controller CCD temperature
    RADESYS  FK5                                                         str     Coordinate reference frame of major/minor axes
    DOSVER   trunk                                                       str     DOS software version
    OCSVER   1.2                                                         float   OCS software version
    CONSTVER DESI:CURRENT                                                str     Constants version
    INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini            str     DOS Configuration
    CLOCK12  9.9992,2.9993                                               str     [V] high rail, low rail
    PGAGAIN  3                                                           int     Controller gain
    DAC10    -25.0003,-25.139                                            str     [V] set value, measured value
    BIASSECA [2065:2128, 2:2065]                                         str     Bias section for quadrant A
    CCDNAME  CCDSM3Z                                                     str     CCD name
    CASETEMP 57.8454                                                     float   [deg C] CCD controller case temperature
    TRIMSECC [8:2064, 2130:4193]                                         str     Trim section for quadrant C
    DAC0     -9.0002,-8.9507                                             str     [V] set value, measured value
    BIASSECC [2065:2128, 2130:4193]                                      str     Bias section for quadrant C
    CLOCK5   9.9999,0.0                                                  str     [V] high rail, low rail
    CLOCK0   9.9999,0.0                                                  str     [V] high rail, low rail
    CRYOPRES 5.083e-08                                                   str     [mb] Cryostat pressure (IP)
    DAC17    20.0008,12.0292                                             str     [V] set value, measured value
    CCDSECC  [1:2057, 2065:4128]                                         str     CCD section for quadrant C
    DATASECB [2193:4249, 2:2065]                                         str     Data section for quadrant B
    AMPSECC  [1:2057, 4128:2065]                                         str     AMP section for quadrant C
    AMPSECD  [4114:2058, 4128:2065]                                      str     AMP section for quadrant D
    DAC13    0.0,0.0594                                                  str     [V] set value, measured value
    CCDSECD  [2058:4114, 2065:4128]                                      str     CCD section for quadrant D
    PRRSECC  [8:2064, 4194:4194]                                         str     Row prescan section for quadrant C
    ORSECC   [8:2064, 2098:2129]                                         str     Row overscan section for quadrant C
    CCDTMING default_lbnl_timing_20180905.txt                            str     CCD timing file
    CPUTEMP  57.7324                                                     float   [deg C] CCD controller CPU temperature
    OFFSET7  2.0,6.0174                                                  str     [V] set value, measured value
    TRIMSECA [8:2064, 2:2065]                                            str     Trim section for quadrant A
    DAC2     -9.0002,-8.9507                                             str     [V] set value, measured value
    PRRSECA  [8:2064, 1:1]                                               str     Row prescan section for quadrant A
    OFFSET2  0.4000000059604645,-8.9507                                  str     [V] set value, measured value
    CLOCK8   9.9992,2.9993                                               str     [V] high rail, low rail
    AMPSECA  [1:2057, 1:2064]                                            str     AMP section for quadrant A
    TRIMSECD [2193:4249, 2130:4193]                                      str     Trim section for quadrant D
    TRIMSECB [2193:4249, 2:2065]                                         str     Trim section for quadrant B
    CLOCK16  9.9999,3.0                                                  str     [V] high rail, low rail
    CLOCK17  9.0,0.9999                                                  str     [V] high rail, low rail
    PRESECC  [1:7, 2130:4193]                                            str     Prescan section for quadrant C
    DATASECD [2193:4249, 2130:4193]                                      str     Data section for quadrant D
    CLOCK1   9.9999,0.0                                                  str     [V] high rail, low rail
    OFFSET5  2.0,6.0227                                                  str     [V] set value, measured value
    DETSECA  [1:2057, 1:2064]                                            str     Detector section for quadrant A
    OFFSET3  0.4000000059604645,-8.9713                                  str     [V] set value, measured value
    OFFSET1  0.4000000059604645,-8.9816                                  str     [V] set value, measured value
    CLOCK3   -2.0001,3.9999                                              str     [V] high rail, low rail
    CLOCK10  9.9992,2.9993                                               str     [V] high rail, low rail
    AMPSECB  [4114:2058, 1:2064]                                         str     AMP section for quadrant B
    CDSPARMS 400, 400, 8, 2000                                           str     CDS parameters
    PRRSECB  [2193:4249, 1:1]                                            str     Row prescan section for quadrant B
    PRESECB  [4250:4256, 2:2065]                                         str     Prescan section for quadrant B
    CLOCK4   9.9999,0.0                                                  str     [V] high rail, low rail
    DAC1     -9.0002,-8.9919                                             str     [V] set value, measured value
    CLOCK7   -2.0001,3.9999                                              str     [V] high rail, low rail
    DETSECB  [2058:4114, 1:2064]                                         str     Detector section for quadrant B
    PRRSECD  [2193:4249, 4194:4194]                                      str     Row prescan section for quadrant D
    OFFSET6  2.0,6.049                                                   str     [V] set value, measured value
    DAC15    0.0,0.0148                                                  str     [V] set value, measured value
    CAMERA   z9                                                          str     Camera name
    ORSECA   [8:2064, 2066:2097]                                         str     Row overscan section for quadrant A
    DAC12    0.0,0.0445                                                  str     [V] set value, measured value
    DAC3     -9.0002,-8.9816                                             str     [V] set value, measured value
    DETSECC  [1:2057, 2065:4128]                                         str     Detector section for quadrant C
    CLOCK13  9.9992,2.9993                                               str     [V] high rail, low rail
    ORSECB   [2193:4249, 2066:2097]                                      str     Row overscan section for quadrant B
    BIASSECD [2129:2192, 2130:4193]                                      str     Bias section for quadrant D
    DAC4     5.9998,6.049                                                str     [V] set value, measured value
    DAC14    0.0,0.0445                                                  str     [V] set value, measured value
    CCDCFG   default_lbnl_20190717.cfg                                   str     CCD configuration file
    DAC9     -25.0003,-25.3467                                           str     [V] set value, measured value
    OFFSET4  2.0,6.049                                                   str     [V] set value, measured value
    DAC11    -25.0003,-24.7531                                           str     [V] set value, measured value
    DAC8     -25.0003,-25.0944                                           str     [V] set value, measured value
    CCDSIZE  4194,4256                                                   str     CCD size in pixels (rows, columns)
    OFFSET0  0.4000000059604645,-8.9507                                  str     [V] set value, measured value
    SETTINGS detectors_sm_20191211.json                                  str     Name of DESI CCD settings file
    DAC5     5.9998,6.0227                                               str     [V] set value, measured value
    CLOCK2   9.9999,0.0                                                  str     [V] high rail, low rail
    CLOCK11  9.9992,2.9993                                               str     [V] high rail, low rail
    DETECTOR M1-22                                                       str     Detector (ccd) identification
    ORSECD   [2193:4249, 2098:2129]                                      str     Row bias section for quadrant D
    CLOCK6   9.9999,0.0                                                  str     [V] high rail, low rail
    DATASECA [8:2064, 2:2065]                                            str     Data section for quadrant A
    CCDSECA  [1:2057, 1:2064]                                            str     CCD section for quadrant A
    DIGITIME 47.5395                                                     float   [s] Time to digitize image
    CLOCK15  9.9992,2.9993                                               str     [V] high rail, low rail
    DAC6     5.9998,6.049                                                str     [V] set value, measured value
    CLOCK18  9.0,0.9999                                                  str     [V] high rail, low rail
    BLDTIME  0.3498                                                      float   [s] Time to build image
    PRESECD  [4250:4256, 2130:4193]                                      str     Prescan section for quadrant D
    BIASSECB [2129:2192, 2:2065]                                         str     Bias section for quadrant B
    PRESECA  [1:7, 2:2065]                                               str     Prescan section for quadrant A
    DELAYS   20, 20, 25, 40, 7, 3000, 7, 7, 7, 7                         str     [10] Delay settings
    CRYOTEMP 139.986                                                     float   [deg K] Cryostat CCD temperature
    DETSECD  [2058:4114, 2065:4128]                                      str     Detector section for quadrant D
    CCDPREP  purge,clear                                                 str     CCD prep actions
    CCDSECB  [2058:4114, 1:2064]                                         str     CCD section for quadrant B
    DAC16    39.9961,39.501                                              str     [V] set value, measured value
    CLOCK14  9.9992,2.9993                                               str     [V] high rail, low rail
    DAC7     5.9998,6.0122                                               str     [V] set value, measured value
    DATASECC [8:2064, 2130:4193]                                         str     Data section for quadrant C
    CLOCK9   9.9992,2.9993                                               str     [V] high rail, low rail
    REQTIME  120.0                                                       float   [s] Requested exposure time
    OBSID    kp4m20210106t001434                                         str     Unique observation identifier
    PROCTYPE RAW                                                         str     Data processing level
    PRODTYPE image                                                       str     Data product type
    CHECKSUM UqlnaojkXojkaojk                                            str     HDU checksum updated 2021-07-07T18:12:11
    DATASUM  1567259519                                                  str     data unit checksum updated 2021-07-07T18:12:11
    GAINA    1.436                                                       float   e/ADU (gain applied to image)
    SATULEVA 65535.0                                                     float   saturation or non lin. level, in ADU, inc. bias
    OVERSCNA 1963.048097897937                                           float   ADUs (gain not applied)
    OBSRDNA  2.336835385267745                                           float   electrons (gain is applied)
    SATUELEA 91289.32293141856                                           float   saturation or non lin. level, in electrons
    GAINB    1.496                                                       float   e/ADU (gain applied to image)
    SATULEVB 65535.0                                                     float   saturation or non lin. level, in ADU, inc. bias
    OVERSCNB 1995.813471569851                                           float   ADUs (gain not applied)
    OBSRDNB  2.246041713363053                                           float   electrons (gain is applied)
    SATUELEB 95054.6230465315                                            float   saturation or non lin. level, in electrons
    GAINC    1.625                                                       float   e/ADU (gain applied to image)
    SATULEVC 65535.0                                                     float   saturation or non lin. level, in ADU, inc. bias
    OVERSCNC 1985.122045687638                                           float   ADUs (gain not applied)
    OBSRDNC  2.774140398679661                                           float   electrons (gain is applied)
    SATUELEC 103268.5516757576                                           float   saturation or non lin. level, in electrons
    GAIND    1.531                                                       float   e/ADU (gain applied to image)
    SATULEVD 65535.0                                                     float   saturation or non lin. level, in ADU, inc. bias
    OVERSCND 1991.892730300213                                           float   ADUs (gain not applied)
    OBSRDND  2.414067469938595                                           float   electrons (gain is applied)
    SATUELED 97284.49722991037                                           float   saturation or non lin. level, in electrons
    FIBERMIN 4500                                                        int
    MODULE   CI                                                          str
    FRAMES   None                                                        Unknown
    COSMSPLT F                                                           bool
    MAXSPLIT 0                                                           int
    SPLITIDS 70882                                                       str
    OBSTYPE  FLAT                                                        str
    MANIFEST F                                                           bool
    OBJECT                                                               str
    SEQID    3 requests                                                  str
    SEQNUM   1                                                           int
    SEQTOT   3                                                           int
    OPENSHUT None                                                        Unknown
    CAMSHUT  open                                                        str
    WHITESPT T                                                           bool
    ZENITH   F                                                           bool
    SEANNEX  F                                                           bool
    BEYONDP  F                                                           bool
    FIDUCIAL off                                                         str
    AIRMASS  1.521297                                                    float
    FOCUS    847.7,32.5,105.5,-41.6,-1.7,0.0                             str
    TRUSTEMP 11.7                                                        float
    PMIRTEMP 6.713                                                       float
    PMREADY  F                                                           bool
    PMCOVER  open                                                        str
    PMCOOL   on                                                          str
    DOMSHUTU not open                                                    str
    DOMSHUTL not open                                                    str
    DOMLIGHH off                                                         str
    DOMLIGHL off                                                         str
    DOMEAZ   252.961                                                     float
    DOMINPOS F                                                           bool
    GUIDOFFR -0.0                                                        float
    GUIDOFFD -0.0                                                        float
    MOONDEC  0.341691                                                    float
    MOONRA   191.56549                                                   float
    MOONSEP  127.286531908392                                            float
    MOUNTAZ  73.493885                                                   float
    MOUNTDEC 31.962924                                                   float
    MOUNTEL  41.036086                                                   float
    MOUNTHA  -58.479216                                                  float
    INCTRL   F                                                           bool
    INPOS    T                                                           bool
    MNTOFFD  -0.0                                                        float
    MNTOFFR  -0.0                                                        float
    PARALLAC -73.493093                                                  float
    SKYDEC   31.962924                                                   float
    SKYRA    56.322324                                                   float
    TARGTDEC 31.9633                                                     float
    TARGTRA  36.803577                                                   float
    TARGTAZ  79.393831                                                   float
    TARGTEL  57.130693                                                   float
    TRGTOFFD 0.0                                                         float
    TRGTOFFR 0.0                                                         float
    ZD       48.963914                                                   float
    TCSST    23:51:22.346                                                str
    TCSMJD   59220.010548                                                float
    ADCCORR  F                                                           bool
    ADC1PHI  16.910154                                                   float
    ADC2PHI  125.239081                                                  float
    ADC1HOME F                                                           bool
    ADC2HOME F                                                           bool
    ADC1NREV -1.0                                                        float
    ADC2NREV 0.0                                                         float
    ADC1STAT STOPPED                                                     str
    ADC2STAT STOPPED                                                     str
    HEXPOS   847.7,32.5,105.5,-41.6,-1.7,0.0                             str
    HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                                     str
    ROTOFFST 0.0                                                         float
    ROTENBLD F                                                           bool
    ROTRATE  0.0                                                         float
    RESETROT F                                                           bool
    GUIDMODE catalog                                                     str
    USEAOS   F                                                           bool
    SPCGRPHS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                     str
    ILLSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                     str
    CCDSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                     str
    TDEWPNT  -21.193                                                     float
    TAIRFLOW 1.104                                                       float
    TAIRITMP 10.4                                                        float
    TAIROTMP 4.5                                                         float
    TAIRTEMP 10.375                                                      float
    TCASITMP 0.0                                                         float
    TCASOTMP 9.1                                                         float
    TCSITEMP 6.5                                                         float
    TCSOTEMP 9.2                                                         float
    TCIBTEMP 0.0                                                         float
    TCIMTEMP 0.0                                                         float
    TCITTEMP 0.0                                                         float
    TCOSTEMP 0.0                                                         float
    TCOWTEMP 0.0                                                         float
    TDBTEMP  -7.9                                                        float
    TFLOWIN  19.5                                                        float
    TFLOWOUT 18.9                                                        float
    TGLYCOLI -1.8                                                        float
    TGLYCOLO -0.9                                                        float
    THINGES  11.4                                                        float
    THINGEW  11.1                                                        float
    TPMAVERT 6.722                                                       float
    TPMDESIT 5.6                                                         float
    TPMEIBT  6.4                                                         float
    TPMEITT  6.2                                                         float
    TPMEOBT  6.4                                                         float
    TPMEOTT  6.3                                                         float
    TPMNIBT  7.0                                                         float
    TPMNITT  6.4                                                         float
    TPMNOBT  8.3                                                         float
    TPMNOTT  7.7                                                         float
    TPMRTDT  6.11                                                        float
    TPMSIBT  6.4                                                         float
    TPMSITT  5.8                                                         float
    TPMSOBT  6.4                                                         float
    TPMSOTT  6.2                                                         float
    TPMSTAT  soft air                                                    str
    TPMWIBT  6.6                                                         float
    TPMWITT  6.5                                                         float
    TPMWOBT  8.3                                                         float
    TPMWOTT  8.6                                                         float
    TPCITEMP 7.1                                                         float
    TPCOTEMP 7.2                                                         float
    TPR1HUM  0.0                                                         float
    TPR1TEMP 0.0                                                         float
    TPR2HUM  0.0                                                         float
    TPR2TEMP 0.0                                                         float
    TSERVO   5.6                                                         float
    TTRSTEMP 11.6                                                        float
    TTRWTEMP 11.5                                                        float
    TTRUETBT -6.2                                                        float
    TTRUETTT 10.2                                                        float
    TTRUNTBT 10.2                                                        float
    TTRUNTTT 10.5                                                        float
    TTRUSTBT 10.2                                                        float
    TTRUSTST 10.8                                                        float
    TTRUSTTT 11.4                                                        float
    TTRUTSBT 11.9                                                        float
    TTRUTSMT 12.0                                                        float
    TTRUTSTT 11.2                                                        float
    TTRUWTBT 10.5                                                        float
    TTRUWTTT 10.6                                                        float
    ALARM    F                                                           bool
    ALARM-ON F                                                           bool
    BATTERY  100.0                                                       float
    SECLEFT  5736.0                                                      float
    UPSSTAT  System Normal - On Line(7)                                  str
    INAMPS   64.9                                                        float
    OUTWATTS 4500.0,6800.0,4200.0                                        str
    COMPDEW  -11.2                                                       float
    COMPHUM  9.4                                                         float
    COMPAMB  16.8                                                        float
    COMPTEMP 22.9                                                        float
    DEWPOINT 8.8                                                         float
    HUMIDITY 9.0                                                         float
    PRESSURE 795.0                                                       float
    OUTTEMP  0.0                                                         float
    WINDDIR  325.1                                                       float
    WINDSPD  24.7                                                        float
    GUST     18.8                                                        float
    AMNIENTN 12.3                                                        float
    CFLOOR   9.4                                                         float
    NWALLIN  12.7                                                        float
    NWALLOUT 8.9                                                         float
    WWALLIN  13.0                                                        float
    WWALLOUT 9.6                                                         float
    AMBIENTS 14.1                                                        float
    FLOOR    12.6                                                        float
    EWALLCMP 10.4                                                        float
    EWALLCOU 9.4                                                         float
    ROOF     9.8                                                         float
    ROOFAMB  9.7                                                         float
    DOMEBLOW 11.2                                                        float
    DOMEBUP  11.2                                                        float
    DOMELLOW 12.4                                                        float
    DOMELUP  16.6                                                        float
    DOMERLOW 10.6                                                        float
    DOMERUP  11.1                                                        float
    PLATFORM 12.4                                                        float
    SHACKC   14.5                                                        float
    SHACKW   13.4                                                        float
    STAIRSL  11.0                                                        float
    STAIRSM  11.3                                                        float
    STAIRSU  11.5                                                        float
    TELBASE  8.9                                                         float
    UTILWALL 10.5                                                        float
    UTILROOM 11.1                                                        float
    FILENAME /exposures/desi/20210105/00070882/desi-00070882.fits.fz     str
    EXCLUDED                                                             str
    NSPEC    500                                                         int     Number of spectra
    WAVEMIN  7520.0                                                      float   First wavelength [Angstroms]
    WAVEMAX  9824.0                                                      float   Last wavelength [Angstroms]
    WAVESTEP 0.8                                                         float   Wavelength step size [Angstroms]
    SPECTER  0.10.0                                                      str     https://github.com/desihub/specter
    IN_PSF   SPECPROD/exposures/20210105/00070882/psf-z9-00070882.fits   str     Input sp
    IN_IMG   SPECPROD/preproc/20210105/00070882/preproc-z9-00070882.fits str
    ORIG_PSF SPECPROD/calibnight/20210105/psfnight-z9-20210105.fits      str
    CHI2PDF  1.118104247799276                                           float
    BUNIT                                                                str     adimensional quantity to divide to flatfield a frame
    ======== =========================================================== ======= ====================================================

Data: FITS image [float32, 2881x500]

HDU1
----

EXTNAME = IVAR

Inverse variance (1/sigma^2) of the fiber flat field in HDU0.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2881             int
    NAXIS2   500              int
    BUNIT                     str  inverse variance, adimensional
    CHECKSUM 9PWhCOTZ9OTfAOTZ str  HDU checksum updated 2021-07-07T18:12:11
    DATASUM  1188137300       str  data unit checksum updated 2021-07-07T18:12:11
    ======== ================ ==== ==============================================

Data: FITS image [float32, 2881x500]

HDU2
----

EXTNAME = MASK

Mask of the fiberflat; 0=good. See the :doc:`bitmask documentation </bitmasks>` page for the definition of the bits.
Prior to desispec/0.24.0 and software release 18.9, the MASK HDU was compressed.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2881             int  Number of wavelengths
    NAXIS2   500              int  Number of spectra
    BSCALE   1                int
    BZERO    2147483648       int
    CHECKSUM EGfjGGdhEGdhEGdh str  HDU checksum updated 2021-07-07T18:12:11
    DATASUM  722182           str  data unit checksum updated 2021-07-07T18:12:11
    ======== ================ ==== ==============================================

Data: FITS image [int32, 2881x500]

HDU3
----

EXTNAME = MEANSPEC

Average flat lamp spectrum of fibers in this camera frame. The fiber flat field is in first approximation the ratio of the measured spectra to this mean spectrum (in practice we use a deconvolved mean spectrum and reconvolve it with the resolution of each fiber). The units are electrons per Angstrom.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================= ==== ==============================================
    KEY      Example Value     Type Comment
    ======== ================= ==== ==============================================
    NAXIS1   2881              int  Number of wavelengths
    BUNIT    electron/Angstrom str
    CHECKSUM CcfOCceNCceNCceN  str  HDU checksum updated 2021-07-07T18:12:12
    DATASUM  1452506388        str  data unit checksum updated 2021-07-07T18:12:12
    ======== ================= ==== ==============================================

Data: FITS image [float32, 2881]

HDU4
----

EXTNAME = WAVELENGTH

Wavelength grid in Angstrom used by this fiber flat field. Note that contrary to the science frame, this wavelength array is in the observer frame. In consequence, one has to first convert its wavelength to the solar barycenter frame before using this data to flat field a science exposure. See the frame :ref:`WAVELENGTH documentation <frame-hdu3-wavelength>` for more details.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2881             int
    BUNIT    Angstrom         str
    CHECKSUM kRaDlRa9kRaCkRa9 str  HDU checksum updated 2021-07-07T18:12:12
    DATASUM  153633556        str  data unit checksum updated 2021-07-07T18:12:12
    ======== ================ ==== ==============================================

Data: FITS image [float32, 2881]

HDU5
----

EXTNAME = FIBERMAP

Fibermap with information about the fiber status.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ======================================================= ======= ==============================================
    KEY      Example Value                                           Type    Comment
    ======== ======================================================= ======= ==============================================
    NAXIS1   373                                                     int     length of dimension 1
    NAXIS2   500                                                     int     length of dimension 2
    EXPID    70882                                                   int
    EXPFRAME 0                                                       int
    FLAVOR   science                                                 str
    SEQUENCE Spectrographs                                           str
    PURPOSE  Commissioning                                           str
    PROGRAM  CALIB DESI-CALIB-00 LEDs only                           str
    PROPID   2019B-5000                                              str
    OBSERVER DESIObserver                                            str
    LEAD     RunManager                                              str
    INSTRUME DESI                                                    str
    OBSERVAT KPNO                                                    str
    OBS-LAT  31.96403                                                str
    OBS-LONG -111.59989                                              str
    OBS-ELEV 2097.0                                                  float
    TELESCOP KPNO 4.0-m telescope                                    str
    CORRCTOR DESI Corrector                                          str
    NIGHT    20210105                                                int
    TIMESYS  UTC                                                     str
    DATE-OBS 2021-01-06T00:14:34.487889920                           str
    TIME-OBS 2021-01-05T00:14:34.487889920                           str
    MJD-OBS  59220.01012139                                          float
    ST       23:51:23.200000                                         str
    EXPTIME  120.035                                                 float
    DELTARA  0.0                                                     float
    DELTADEC 0.0                                                     float
    VCCD     ON                                                      str
    VCCDON   2020-12-09T21:23:25.450662                              str
    VCCDSEC  2343238.6                                               float
    EPOCH    2000.0                                                  float
    SPECGRPH 9                                                       int
    SPECID   3                                                       int
    FEEBOX   lbnl060                                                 str
    VESSEL   4                                                       int
    FEEVER   v20160312                                               str
    FEEPOWER ON                                                      str
    FEEDMASK 2134851391                                              int
    FEECMASK 1048575                                                 int
    CCDTEMP  -136.0969                                               float
    RADESYS  FK5                                                     str
    DOSVER   trunk                                                   str
    OCSVER   1.2                                                     float
    CONSTVER DESI:CURRENT                                            str
    INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini        str
    CLOCK12  9.9992,2.9993                                           str
    PGAGAIN  3                                                       int
    DAC10    -25.0003,-25.139                                        str
    BIASSECA [2065:2128, 2:2065]                                     str
    CCDNAME  CCDSM3Z                                                 str
    CASETEMP 57.8454                                                 float
    TRIMSECC [8:2064, 2130:4193]                                     str
    DAC0     -9.0002,-8.9507                                         str
    BIASSECC [2065:2128, 2130:4193]                                  str
    CLOCK5   9.9999,0.0                                              str
    CLOCK0   9.9999,0.0                                              str
    CRYOPRES 5.083e-08                                               str
    DAC17    20.0008,12.0292                                         str
    CCDSECC  [1:2057, 2065:4128]                                     str
    DATASECB [2193:4249, 2:2065]                                     str
    AMPSECC  [1:2057, 4128:2065]                                     str
    AMPSECD  [4114:2058, 4128:2065]                                  str
    DAC13    0.0,0.0594                                              str
    CCDSECD  [2058:4114, 2065:4128]                                  str
    PRRSECC  [8:2064, 4194:4194]                                     str
    ORSECC   [8:2064, 2098:2129]                                     str
    CCDTMING default_lbnl_timing_20180905.txt                        str
    CPUTEMP  57.7324                                                 float
    OFFSET7  2.0,6.0174                                              str
    TRIMSECA [8:2064, 2:2065]                                        str
    DAC2     -9.0002,-8.9507                                         str
    PRRSECA  [8:2064, 1:1]                                           str
    OFFSET2  0.4000000059604645,-8.9507                              str
    CLOCK8   9.9992,2.9993                                           str
    AMPSECA  [1:2057, 1:2064]                                        str
    TRIMSECD [2193:4249, 2130:4193]                                  str
    TRIMSECB [2193:4249, 2:2065]                                     str
    CLOCK16  9.9999,3.0                                              str
    CLOCK17  9.0,0.9999                                              str
    PRESECC  [1:7, 2130:4193]                                        str
    DATASECD [2193:4249, 2130:4193]                                  str
    CLOCK1   9.9999,0.0                                              str
    OFFSET5  2.0,6.0227                                              str
    DETSECA  [1:2057, 1:2064]                                        str
    OFFSET3  0.4000000059604645,-8.9713                              str
    OFFSET1  0.4000000059604645,-8.9816                              str
    CLOCK3   -2.0001,3.9999                                          str
    CLOCK10  9.9992,2.9993                                           str
    AMPSECB  [4114:2058, 1:2064]                                     str
    CDSPARMS 400, 400, 8, 2000                                       str
    PRRSECB  [2193:4249, 1:1]                                        str
    PRESECB  [4250:4256, 2:2065]                                     str
    CLOCK4   9.9999,0.0                                              str
    DAC1     -9.0002,-8.9919                                         str
    CLOCK7   -2.0001,3.9999                                          str
    DETSECB  [2058:4114, 1:2064]                                     str
    PRRSECD  [2193:4249, 4194:4194]                                  str
    OFFSET6  2.0,6.049                                               str
    DAC15    0.0,0.0148                                              str
    CAMERA   z9                                                      str
    ORSECA   [8:2064, 2066:2097]                                     str
    DAC12    0.0,0.0445                                              str
    DAC3     -9.0002,-8.9816                                         str
    DETSECC  [1:2057, 2065:4128]                                     str
    CLOCK13  9.9992,2.9993                                           str
    ORSECB   [2193:4249, 2066:2097]                                  str
    BIASSECD [2129:2192, 2130:4193]                                  str
    DAC4     5.9998,6.049                                            str
    DAC14    0.0,0.0445                                              str
    CCDCFG   default_lbnl_20190717.cfg                               str
    DAC9     -25.0003,-25.3467                                       str
    OFFSET4  2.0,6.049                                               str
    DAC11    -25.0003,-24.7531                                       str
    DAC8     -25.0003,-25.0944                                       str
    CCDSIZE  4194,4256                                               str
    OFFSET0  0.4000000059604645,-8.9507                              str
    SETTINGS detectors_sm_20191211.json                              str
    DAC5     5.9998,6.0227                                           str
    CLOCK2   9.9999,0.0                                              str
    CLOCK11  9.9992,2.9993                                           str
    DETECTOR M1-22                                                   str
    ORSECD   [2193:4249, 2098:2129]                                  str
    CLOCK6   9.9999,0.0                                              str
    DATASECA [8:2064, 2:2065]                                        str
    CCDSECA  [1:2057, 1:2064]                                        str
    DIGITIME 47.5395                                                 float
    CLOCK15  9.9992,2.9993                                           str
    DAC6     5.9998,6.049                                            str
    CLOCK18  9.0,0.9999                                              str
    BLDTIME  0.3498                                                  float
    PRESECD  [4250:4256, 2130:4193]                                  str
    BIASSECB [2129:2192, 2:2065]                                     str
    PRESECA  [1:7, 2:2065]                                           str
    DELAYS   20, 20, 25, 40, 7, 3000, 7, 7, 7, 7                     str
    CRYOTEMP 139.986                                                 float
    DETSECD  [2058:4114, 2065:4128]                                  str
    CCDPREP  purge,clear                                             str
    CCDSECB  [2058:4114, 1:2064]                                     str
    DAC16    39.9961,39.501                                          str
    CLOCK14  9.9992,2.9993                                           str
    DAC7     5.9998,6.0122                                           str
    DATASECC [8:2064, 2130:4193]                                     str
    CLOCK9   9.9992,2.9993                                           str
    REQTIME  120.0                                                   float
    OBSID    kp4m20210106t001434                                     str
    PROCTYPE RAW                                                     str
    PRODTYPE image                                                   str
    GAINA    1.436                                                   float
    SATULEVA 65535.0                                                 float
    OVERSCNA 1963.048097897937                                       float
    OBSRDNA  2.336835385267745                                       float
    SATUELEA 91289.32293141856                                       float
    GAINB    1.496                                                   float
    SATULEVB 65535.0                                                 float
    OVERSCNB 1995.813471569851                                       float
    OBSRDNB  2.246041713363053                                       float
    SATUELEB 95054.6230465315                                        float
    GAINC    1.625                                                   float
    SATULEVC 65535.0                                                 float
    OVERSCNC 1985.122045687638                                       float
    OBSRDNC  2.774140398679661                                       float
    SATUELEC 103268.5516757576                                       float
    GAIND    1.531                                                   float
    SATULEVD 65535.0                                                 float
    OVERSCND 1991.892730300213                                       float
    OBSRDND  2.414067469938595                                       float
    SATUELED 97284.49722991037                                       float
    FIBERMIN 4500                                                    int
    BZERO    32768                                                   int
    BSCALE   1                                                       int
    MODULE   CI                                                      str
    FRAMES   None                                                    Unknown
    COSMSPLT F                                                       bool
    MAXSPLIT 0                                                       int
    SPLITIDS 70882                                                   str
    OBSTYPE  FLAT                                                    str
    MANIFEST F                                                       bool
    OBJECT                                                           str
    SEQID    3 requests                                              str
    SEQNUM   1                                                       int
    SEQTOT   3                                                       int
    OPENSHUT None                                                    Unknown
    CAMSHUT  open                                                    str
    WHITESPT T                                                       bool
    ZENITH   F                                                       bool
    SEANNEX  F                                                       bool
    BEYONDP  F                                                       bool
    FIDUCIAL off                                                     str
    AIRMASS  1.521297                                                float
    FOCUS    847.7,32.5,105.5,-41.6,-1.7,0.0                         str
    TRUSTEMP 11.7                                                    float
    PMIRTEMP 6.713                                                   float
    PMREADY  F                                                       bool
    PMCOVER  open                                                    str
    PMCOOL   on                                                      str
    DOMSHUTU not open                                                str
    DOMSHUTL not open                                                str
    DOMLIGHH off                                                     str
    DOMLIGHL off                                                     str
    DOMEAZ   252.961                                                 float
    DOMINPOS F                                                       bool
    GUIDOFFR -0.0                                                    float
    GUIDOFFD -0.0                                                    float
    MOONDEC  0.341691                                                float
    MOONRA   191.56549                                               float
    MOONSEP  127.286531908392                                        float
    MOUNTAZ  73.493885                                               float
    MOUNTDEC 31.962924                                               float
    MOUNTEL  41.036086                                               float
    MOUNTHA  -58.479216                                              float
    INCTRL   F                                                       bool
    INPOS    T                                                       bool
    MNTOFFD  -0.0                                                    float
    MNTOFFR  -0.0                                                    float
    PARALLAC -73.493093                                              float
    SKYDEC   31.962924                                               float
    SKYRA    56.322324                                               float
    TARGTDEC 31.9633                                                 float
    TARGTRA  36.803577                                               float
    TARGTAZ  79.393831                                               float
    TARGTEL  57.130693                                               float
    TRGTOFFD 0.0                                                     float
    TRGTOFFR 0.0                                                     float
    ZD       48.963914                                               float
    TCSST    23:51:22.346                                            str
    TCSMJD   59220.010548                                            float
    ADCCORR  F                                                       bool
    ADC1PHI  16.910154                                               float
    ADC2PHI  125.239081                                              float
    ADC1HOME F                                                       bool
    ADC2HOME F                                                       bool
    ADC1NREV -1.0                                                    float
    ADC2NREV 0.0                                                     float
    ADC1STAT STOPPED                                                 str
    ADC2STAT STOPPED                                                 str
    HEXPOS   847.7,32.5,105.5,-41.6,-1.7,0.0                         str
    HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                                 str
    ROTOFFST 0.0                                                     float
    ROTENBLD F                                                       bool
    ROTRATE  0.0                                                     float
    RESETROT F                                                       bool
    GUIDMODE catalog                                                 str
    USEAOS   F                                                       bool
    SPCGRPHS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                 str
    ILLSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                 str
    CCDSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                 str
    TDEWPNT  -21.193                                                 float
    TAIRFLOW 1.104                                                   float
    TAIRITMP 10.4                                                    float
    TAIROTMP 4.5                                                     float
    TAIRTEMP 10.375                                                  float
    TCASITMP 0.0                                                     float
    TCASOTMP 9.1                                                     float
    TCSITEMP 6.5                                                     float
    TCSOTEMP 9.2                                                     float
    TCIBTEMP 0.0                                                     float
    TCIMTEMP 0.0                                                     float
    TCITTEMP 0.0                                                     float
    TCOSTEMP 0.0                                                     float
    TCOWTEMP 0.0                                                     float
    TDBTEMP  -7.9                                                    float
    TFLOWIN  19.5                                                    float
    TFLOWOUT 18.9                                                    float
    TGLYCOLI -1.8                                                    float
    TGLYCOLO -0.9                                                    float
    THINGES  11.4                                                    float
    THINGEW  11.1                                                    float
    TPMAVERT 6.722                                                   float
    TPMDESIT 5.6                                                     float
    TPMEIBT  6.4                                                     float
    TPMEITT  6.2                                                     float
    TPMEOBT  6.4                                                     float
    TPMEOTT  6.3                                                     float
    TPMNIBT  7.0                                                     float
    TPMNITT  6.4                                                     float
    TPMNOBT  8.3                                                     float
    TPMNOTT  7.7                                                     float
    TPMRTDT  6.11                                                    float
    TPMSIBT  6.4                                                     float
    TPMSITT  5.8                                                     float
    TPMSOBT  6.4                                                     float
    TPMSOTT  6.2                                                     float
    TPMSTAT  soft air                                                str
    TPMWIBT  6.6                                                     float
    TPMWITT  6.5                                                     float
    TPMWOBT  8.3                                                     float
    TPMWOTT  8.6                                                     float
    TPCITEMP 7.1                                                     float
    TPCOTEMP 7.2                                                     float
    TPR1HUM  0.0                                                     float
    TPR1TEMP 0.0                                                     float
    TPR2HUM  0.0                                                     float
    TPR2TEMP 0.0                                                     float
    TSERVO   5.6                                                     float
    TTRSTEMP 11.6                                                    float
    TTRWTEMP 11.5                                                    float
    TTRUETBT -6.2                                                    float
    TTRUETTT 10.2                                                    float
    TTRUNTBT 10.2                                                    float
    TTRUNTTT 10.5                                                    float
    TTRUSTBT 10.2                                                    float
    TTRUSTST 10.8                                                    float
    TTRUSTTT 11.4                                                    float
    TTRUTSBT 11.9                                                    float
    TTRUTSMT 12.0                                                    float
    TTRUTSTT 11.2                                                    float
    TTRUWTBT 10.5                                                    float
    TTRUWTTT 10.6                                                    float
    ALARM    F                                                       bool
    ALARM-ON F                                                       bool
    BATTERY  100.0                                                   float
    SECLEFT  5736.0                                                  float
    UPSSTAT  System Normal - On Line(7)                              str
    INAMPS   64.9                                                    float
    OUTWATTS 4500.0,6800.0,4200.0                                    str
    COMPDEW  -11.2                                                   float
    COMPHUM  9.4                                                     float
    COMPAMB  16.8                                                    float
    COMPTEMP 22.9                                                    float
    DEWPOINT 8.8                                                     float
    HUMIDITY 9.0                                                     float
    PRESSURE 795.0                                                   float
    OUTTEMP  0.0                                                     float
    WINDDIR  325.1                                                   float
    WINDSPD  24.7                                                    float
    GUST     18.8                                                    float
    AMNIENTN 12.3                                                    float
    CFLOOR   9.4                                                     float
    NWALLIN  12.7                                                    float
    NWALLOUT 8.9                                                     float
    WWALLIN  13.0                                                    float
    WWALLOUT 9.6                                                     float
    AMBIENTS 14.1                                                    float
    FLOOR    12.6                                                    float
    EWALLCMP 10.4                                                    float
    EWALLCOU 9.4                                                     float
    ROOF     9.8                                                     float
    ROOFAMB  9.7                                                     float
    DOMEBLOW 11.2                                                    float
    DOMEBUP  11.2                                                    float
    DOMELLOW 12.4                                                    float
    DOMELUP  16.6                                                    float
    DOMERLOW 10.6                                                    float
    DOMERUP  11.1                                                    float
    PLATFORM 12.4                                                    float
    SHACKC   14.5                                                    float
    SHACKW   13.4                                                    float
    STAIRSL  11.0                                                    float
    STAIRSM  11.3                                                    float
    STAIRSU  11.5                                                    float
    TELBASE  8.9                                                     float
    UTILWALL 10.5                                                    float
    UTILROOM 11.1                                                    float
    FILENAME /exposures/desi/20210105/00070882/desi-00070882.fits.fz str
    EXCLUDED                                                         str
    CHECKSUM SCdQU9ZOSAdOS9ZO                                        str     HDU checksum updated 2021-07-07T18:12:12
    DATASUM  3473499039                                              str     data unit checksum updated 2021-07-07T18:12:12
    ENCODING ascii                                                   str
    ======== ======================================================= ======= ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

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

*Add notes and examples here.  You can also create links to example files.*
