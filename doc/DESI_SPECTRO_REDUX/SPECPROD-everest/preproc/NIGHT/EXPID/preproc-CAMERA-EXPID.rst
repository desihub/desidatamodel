=========================
preproc-CAMERA-EXPID.fits
=========================

:Summary: Pre-processed spectrograph CCD raw data.
:Naming Convention: ``preproc-{camera}-{expid}.fits``, where
    ``{camera}`` is the spectrograph camera (e.g. "b0", "r1", "z9"),
    and ``{expid}`` is the zero-padded 8-digit exposure ID.
:Regex: ``preproc-[brz][0-9]-[0-9]{8}\.fits``
:File Type: FITS, 194 MB

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

======== ======================================================= ======= ===============================================
KEY      Example Value                                           Type    Comment
======== ======================================================= ======= ===============================================
NAXIS1   4096                                                    int
NAXIS2   4096                                                    int
EXPID    95882                                                   int     Exposure number
EXPFRAME 0                                                       int     Frame number
FLAVOR   science                                                 str     Observation type
SEQUENCE Spectrographs                                           str     OCS Sequence name
PURPOSE  Main Survey                                             str     Purpose of observing night
PROGRAM  CALIB LED gain sequence                                 str     Program name
PROPID   2020B-5000                                              str     Proposal ID
OBSERVER DESIObserver                                            str     Names of observers
LEAD     RunManager                                              str     Lead observer
INSTRUME DESI                                                    str     Instrument name
OBSERVAT KPNO                                                    str     Observatory name
OBS-LAT  31.96403                                                str     [deg] Observatory latitude
OBS-LONG -111.59989                                              str     [deg] Observatory east longitude
OBS-ELEV 2097.0                                                  float   [m] Observatory elevation
TELESCOP KPNO 4.0-m telescope                                    str     Telescope name
CORRCTOR DESI Corrector                                          str     Corrector Identification
NIGHT    20210624                                                int     Observing night
TIMESYS  UTC                                                     str     Time system used for date-obs
DATE-OBS 2021-06-25T00:51:56.775584                              str     [UTC] Observation data and start time
TIME-OBS 2021-06-24T00:51:56.775584                              str     [UTC] Observation start time
MJD-OBS  59390.03607379                                          float   Modified Julian Date of observation
OPENSHUT 2021-06-25T00:51:57.382712                              str     Time shutter opened
ST       11:39:06.070000                                         str     Local Sidereal time at observation start (HH:MM
EXPTIME  100.099                                                 float   [s] Actual exposure time
DELTARA  0.0                                                     float   [arcsec] Offset], right ascension, observer inp
DELTADEC 0.0                                                     float   [arcsec] Offset], declination, observer input
VCCD     ON                                                      str     True (ON) if CCD voltage is on
VCCDON   2021-06-24T12:53:18.351674                              str     Time when CCD voltage was turned on
VCCDSEC  43270.1                                                 float   [s] CCD on time in seconds
EPOCH    2000.0                                                  float   Epoch of observation
SPECGRPH 1                                                       int     Spectrograph logical name (SP)
SPECID   10                                                      int     Spectrograph serial number (SM)
FEEBOX   lbnl088                                                 str     CCD Controller serial number
VESSEL   29                                                      int     Cryostat serial number
FEEVER   v20160312                                               str     CCD Controller version
FEEPOWER ON                                                      str     FEE power status
FEEDMASK 2134851391                                              int     FEE dac mask
FEECMASK 1048575                                                 int     FEE clk mask
CCDTEMP  850.0                                                   float   [deg C] CCD controller CCD temperature
RADESYS  FK5                                                     str     Coordinate reference frame of major/minor axes
DOSVER   trunk                                                   str     DOS software version
OCSVER   1.2                                                     float   OCS software version
CONSTVER DESI:CURRENT                                            str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini        str     DOS Configuration
BIASSECC [2053:2116, 2114:4161]                                  str     Bias section for quadrant C
PGAGAIN  5                                                       int     Controller gain
CCDPREP  purge,clear                                             str     CCD prep actions
DAC7     0.0,-0.0158                                             str     [V] set value, measured value
CASETEMP 58.0915                                                 float   [deg C] CCD controller case temperature
PRESECB  [4229:4232, 2:2049]                                     str     Prescan section for quadrant B
DAC5     0.0,-0.0158                                             str     [V] set value, measured value
CCDCFG   CMV_22805_sta_revd_tuned-may2018_20210128.cfg           str     CCD configuration fi
DAC9     26.9998,27.0236                                         str     [V] set value, measured value
ORSECA   [5:2052, 2050:2081]                                     str     Row overscan section for quadrant A
CCDSECD  [2049:4096, 2049:4096]                                  str     CCD section for quadrant D
CRYOTEMP 162.97                                                  float   [deg K] Cryostat CCD temperature
DATASECC [5:2052, 2114:4161]                                     str     Data section for quadrant C
DAC14    0.0,0.7904                                              str     [V] set value, measured value
TRIMSECD [2181:4228, 2114:4161]                                  str     Trim section for quadrant D
CLOCK4   3.9999,-4.0002                                          str     [V] high rail, low rail
CLOCK12  3.0,-8.0001                                             str     [V] high rail, low rail
OFFSET1  -1.5,15.7796                                            str     [V] set value, measured value
BIASSECD [2117:2180, 2114:4161]                                  str     Bias section for quadrant D
ORSECC   [5:2052, 2082:2113]                                     str     Row overscan section for quadrant C
CLOCK6   3.9999,-4.0002                                          str     [V] high rail, low rail
PRESECA  [1:4, 2:2049]                                           str     Prescan section for quadrant A
CLOCK8   3.0,-8.0001                                             str     [V] high rail, low rail
DELAYS   13, 13, 25, 25, 8, 3000, 7, 7, 400, 7                   str     [10] Delay settings
DATASECB [2181:4228, 2:2049]                                     str     Data section for quadrant B
DAC10    26.9998,27.0682                                         str     [V] set value, measured value
DATASECD [2181:4228, 2114:4161]                                  str     Data section for quadrant D
DAC6     0.0,-0.0105                                             str     [V] set value, measured value
BIASSECB [2117:2180, 2:2049]                                     str     Bias section for quadrant B
ORSECB   [2181:4228, 2050:2081]                                  str     Row overscan section for quadrant B
DAC11    26.9998,26.5191                                         str     [V] set value, measured value
AMPSECD  [4096:2049, 4096:2049]                                  str     AMP section for quadrant D
DETSECA  [1:2048, 1:2048]                                        str     Detector section for quadrant A
CLOCK13  3.0,-8.0001                                             str     [V] high rail, low rail
CCDNAME  CCDSM10B                                                str     CCD name
AMPSECA  [1:2048, 1:2048]                                        str     AMP section for quadrant A
CPUTEMP  57.9785                                                 float   [deg C] CCD controller CPU temperature
CAMERA   b1                                                      str     Camera name
PRESECD  [4229:4232, 2114:4161]                                  str     Prescan section for quadrant D
PRESECC  [1:4, 2114:4161]                                        str     Prescan section for quadrant C
CLOCK16  0.0,0.0                                                 str     [V] high rail, low rail
DETSECD  [2049:4096, 2049:4096]                                  str     Detector section for quadrant D
AMPSECC  [2048:1, 2049:4096]                                     str     AMP section for quadrant C
ORSECD   [2181:4228, 2082:2113]                                  str     Row bias section for quadrant D
TRIMSECC [5:2052, 2114:4161]                                     str     Trim section for quadrant C
CLOCK18  3.9999,-4.0002                                          str     [V] high rail, low rail
DETSECB  [2049:4096, 1:2048]                                     str     Detector section for quadrant B
CLOCK17  3.9999,-4.0002                                          str     [V] high rail, low rail
CLOCK5   3.9999,-4.0002                                          str     [V] high rail, low rail
DAC3     15.9998,15.9444                                         str     [V] set value, measured value
PRRSECB  [2181:4228, 1:1]                                        str     Row prescan section for quadrant B
DAC1     15.9998,15.7796                                         str     [V] set value, measured value
DAC0     15.9998,15.9547                                         str     [V] set value, measured value
PRRSECD  [2181:4228, 4162:4162]                                  str     Row prescan section for quadrant D
DAC8     26.9998,27.0088                                         str     [V] set value, measured value
BLDTIME  0.3551                                                  float   [s] Time to build image
CLOCK14  3.0,-8.0001                                             str     [V] high rail, low rail
OFFSET3  -1.5,15.9341                                            str     [V] set value, measured value
DAC16    0.0,0.2772                                              str     [V] set value, measured value
TRIMSECB [2181:4228, 2:2049]                                     str     Trim section for quadrant B
DAC4     0.0,-0.0105                                             str     [V] set value, measured value
CCDSECC  [1:2048, 2049:4096]                                     str     CCD section for quadrant C
PRRSECC  [5:2052, 4162:4162]                                     str     Row prescan section for quadrant C
CLOCK1   3.9999,-4.0002                                          str     [V] high rail, low rail
PRRSECA  [5:2052, 1:1]                                           str     Row prescan section for quadrant A
DAC17    -0.0,0.061                                              str     [V] set value, measured value
CLOCK7   6.9999,-2.0001                                          str     [V] high rail, low rail
DAC12    0.0,5.0752                                              str     [V] set value, measured value
CDSPARMS 350, 350, 8, 1000                                       str     CDS parameters
CCDSIZE  4162,4232                                               str     CCD size in pixels (rows, columns)
CCDTMING flatdark_sta_timing.txt                                 str     CCD timing file
OFFSET4  -1.2599999904632568,-0.0053                             str     [V] set value, measured value
DIGITIME 49.545                                                  float   [s] Time to digitize image
DETSECC  [1:2048, 2049:4096]                                     str     Detector section for quadrant C
CCDSECB  [2049:4096, 1:2048]                                     str     CCD section for quadrant B
CCDSECA  [1:2048, 1:2048]                                        str     CCD section for quadrant A
OFFSET7  -1.4700000286102295,-0.0263                             str     [V] set value, measured value
CLOCK0   3.9999,-4.0002                                          str     [V] high rail, low rail
DAC15    19.9997,19.812                                          str     [V] set value, measured value
BIASSECA [2053:2116, 2:2049]                                     str     Bias section for quadrant A
CLOCK9   3.0,-8.0001                                             str     [V] high rail, low rail
OFFSET2  -1.5,15.8208                                            str     [V] set value, measured value
TRIMSECA [5:2052, 2:2049]                                        str     Trim section for quadrant A
OFFSET0  -1.5,15.965                                             str     [V] set value, measured value
CRYOPRES 8.794e-08                                               str     [mb] Cryostat pressure (IP)
OFFSET5  -1.309999942779541,-0.021                               str     [V] set value, measured value
DETECTOR sn22822                                                 str     Detector (ccd) identification
SETTINGS detectors_sm_20210128.json                              str     Name of DESI CCD settings file
DATASECA [5:2052, 2:2049]                                        str     Data section for quadrant A
CLOCK15  0.0,0.0                                                 str     [V] high rail, low rail
AMPSECB  [2049:4096, 2048:1]                                     str     AMP section for quadrant B
DAC13    0.0,-5.0232                                             str     [V] set value, measured value
CLOCK10  3.0,-8.0001                                             str     [V] high rail, low rail
OFFSET6  -1.5199999809265137,-0.0158                             str     [V] set value, measured value
DAC2     15.9998,15.8105                                         str     [V] set value, measured value
CLOCK11  0.0,0.0                                                 str     [V] high rail, low rail
CLOCK2   3.9999,-4.0002                                          str     [V] high rail, low rail
CLOCK3   6.9999,-2.0001                                          str     [V] high rail, low rail
REQTIME  100.0                                                   float   [s] Requested exposure time
OBSID    kp4m20210625t005156                                     str     Unique observation identifier
PROCTYPE RAW                                                     str     Data processing level
PRODTYPE image                                                   str     Data product type
CHECKSUM 66jQ66gQ66gQ66gQ                                        str     HDU checksum updated 2021-07-07T16:47:31
DATASUM  1002884070                                              str     data unit checksum updated 2021-07-07T16:47:31
GAINA    1.308                                                   float   e/ADU (gain applied to image)
SATULEVA 35000.0                                                 float   saturation or non lin. level, in ADU, inc. bias
OVERSCNA 1208.720593091835                                       float   ADUs (gain not applied)
OBSRDNA  5.319229645440016                                       float   electrons (gain is applied)
SATUELEA 44198.99346423588                                       float   saturation or non lin. level, in electrons
GAINB    1.286                                                   float   e/ADU (gain applied to image)
SATULEVB 36000.0                                                 float   saturation or non lin. level, in ADU, inc. bias
OVERSCNB 1206.300288531992                                       float   ADUs (gain not applied)
OBSRDNB  3.250851570254362                                       float   electrons (gain is applied)
SATUELEB 44744.69782894786                                       float   saturation or non lin. level, in electrons
GAINC    1.288                                                   float   e/ADU (gain applied to image)
SATULEVC 45000.0                                                 float   saturation or non lin. level, in ADU, inc. bias
OVERSCNC 1192.14201160539                                        float   ADUs (gain not applied)
OBSRDNC  4.31948644183243                                        float   electrons (gain is applied)
SATUELEC 56424.52108905226                                       float   saturation or non lin. level, in electrons
GAIND    1.304                                                   float   e/ADU (gain applied to image)
SATULEVD 36000.0                                                 float   saturation or non lin. level, in ADU, inc. bias
OVERSCND 1180.660787266955                                       float   ADUs (gain not applied)
OBSRDND  3.202120109933047                                       float   electrons (gain is applied)
SATUELED 45404.41833340389                                       float   saturation or non lin. level, in electrons
FIBERMIN 500                                                     int
MODULE   CI                                                      str
FRAMES   None                                                    Unknown
COSMSPLT F                                                       bool
MAXSPLIT 0                                                       int
OBSTYPE  FLAT                                                    str
MANIFEST F                                                       bool
OBJECT                                                           str
NTSSURVY na                                                      str
SEQID    2 requests                                              str
SEQNUM   1                                                       int
SEQTOT   2                                                       int
SEQSTART 2021-06-25T00:51:53.096588                              str
CAMSHUT  open                                                    str
WHITESPT T                                                       bool
ZENITH   F                                                       bool
SEANNEX  F                                                       bool
BEYONDP  F                                                       bool
FIDUCIAL off                                                     str
AIRMASS  1.521257                                                float
FOCUS    868.0,-522.3,-1055.0,-1.7,11.9,0.0                      str
PMREADY  F                                                       bool
DOMEAZ   106.727                                                 float
DOMINPOS F                                                       bool
GUIDOFFR 0.0                                                     float
GUIDOFFD -0.0                                                    float
SUNRA    94.038905                                               float
SUNDEC   23.384181                                               float
MOONDEC  -25.604587                                              float
MOONRA   277.758043                                              float
MOONSEP  163.761                                                 float
MOUNTAZ  286.506498                                              float
MOUNTDEC 31.96357                                                float
MOUNTEL  41.037384                                               float
MOUNTHA  58.477846                                               float
INCTRL   F                                                       bool
INPOS    T                                                       bool
MNTOFFD  -0.0                                                    float
MNTOFFR  -0.0                                                    float
PARALLAC 73.49407                                                float
SKYDEC   31.96357                                                float
SKYRA    116.298974                                              float
TARGTDEC 31.963305                                               float
TARGTRA  89.002025                                               float
TARGTAZ  296.183791                                              float
TARGTEL  19.467294                                               float
TRGTOFFD 0.0                                                     float
TRGTOFFR 0.0                                                     float
ZD       48.962616                                               float
TCSST    11:39:06.437                                            str
TCSMJD   59390.036509                                            float
SEEING   None                                                    Unknown
TRANSPAR None                                                    Unknown
ADCCORR  F                                                       bool
ADC1PHI  8.50000000127693e-05                                    float
ADC2PHI  0.000176                                                float
ADC1HOME F                                                       bool
ADC2HOME F                                                       bool
ADC1NREV 0.0                                                     float
ADC2NREV 0.0                                                     float
ADC1STAT STOPPED                                                 str
ADC2STAT STOPPED                                                 str
HEXPOS   868.0,-522.3,-1055.0,-1.7,11.9,0.0                      str
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                                 str
ROTOFFST 0.0                                                     float
ROTENBLD F                                                       bool
ROTRATE  0.0                                                     float
RESETROT F                                                       bool
GUIDMODE catalog                                                 str
SPCGRPHS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                 str
ILLSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                 str
CCDSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                 str
UPSSTAT  SUCCESS                                                 str
FILENAME /exposures/desi/20210624/00095882/desi-00095882.fits.fz str
EXCLUDED                                                         str
TCSKRA   0.3 0.003 0.00003                                       str
TCSKDEC  0.3 0.003 0.00003                                       str
TCSGRA   0.3                                                     float
TCSGDEC  0.3                                                     float
TCSMFRA  1                                                       int
TCSMFDEC 1                                                       int
TCSPIRA  1.0,0.0,0.0,0.0                                         str
TCSPIDEC 1.0,0.0,0.0,0.0                                         str
======== ======================================================= ======= ===============================================

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
CHECKSUM 9Sia9ShZ9Sha9ShW str  HDU checksum updated 2021-07-07T16:47:35
DATASUM  2730518959       str  data unit checksum updated 2021-07-07T16:47:35
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
CHECKSUM FA7pG74nFA4nF74n str  HDU checksum updated 2021-07-07T16:47:39
DATASUM  3723652597       str  data unit checksum updated 2021-07-07T16:47:39
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
CHECKSUM lP5BmM59lM5AlM57 str  HDU checksum updated 2021-07-07T16:47:43
DATASUM  2589967241       str  data unit checksum updated 2021-07-07T16:47:43
======== ================ ==== ==============================================

Data: FITS image [float32, 4096x4096]

HDU4
----

EXTNAME = FIBERMAP

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================================================= ======= ==============================================
KEY      Example Value                                           Type    Comment
======== ======================================================= ======= ==============================================
NAXIS1   373                                                     int     length of dimension 1
NAXIS2   500                                                     int     length of dimension 2
EXPID    95882                                                   int
EXPFRAME 0                                                       int
FLAVOR   science                                                 str
SEQUENCE Spectrographs                                           str
PURPOSE  Main Survey                                             str
PROGRAM  CALIB LED gain sequence                                 str
PROPID   2020B-5000                                              str
OBSERVER DESIObserver                                            str
LEAD     RunManager                                              str
INSTRUME DESI                                                    str
OBSERVAT KPNO                                                    str
OBS-LAT  31.96403                                                str
OBS-LONG -111.59989                                              str
OBS-ELEV 2097.0                                                  float
TELESCOP KPNO 4.0-m telescope                                    str
CORRCTOR DESI Corrector                                          str
NIGHT    20210624                                                int
TIMESYS  UTC                                                     str
DATE-OBS 2021-06-25T00:51:56.775584                              str
TIME-OBS 2021-06-24T00:51:56.775584                              str
MJD-OBS  59390.03607379                                          float
OPENSHUT 2021-06-25T00:51:57.382712                              str
ST       11:39:06.070000                                         str
EXPTIME  100.099                                                 float
DELTARA  0.0                                                     float
DELTADEC 0.0                                                     float
VCCD     ON                                                      str
VCCDON   2021-06-24T12:53:18.351674                              str
VCCDSEC  43270.1                                                 float
EPOCH    2000.0                                                  float
SPECGRPH 1                                                       int
SPECID   10                                                      int
FEEBOX   lbnl088                                                 str
VESSEL   29                                                      int
FEEVER   v20160312                                               str
FEEPOWER ON                                                      str
FEEDMASK 2134851391                                              int
FEECMASK 1048575                                                 int
CCDTEMP  850.0                                                   float
RADESYS  FK5                                                     str
DOSVER   trunk                                                   str
OCSVER   1.2                                                     float
CONSTVER DESI:CURRENT                                            str
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini        str
BIASSECC [2053:2116, 2114:4161]                                  str
PGAGAIN  5                                                       int
CCDPREP  purge,clear                                             str
DAC7     0.0,-0.0158                                             str
CASETEMP 58.0915                                                 float
PRESECB  [4229:4232, 2:2049]                                     str
DAC5     0.0,-0.0158                                             str
CCDCFG   CMV_22805_sta_revd_tuned-may2018_20210128.cfg           str
DAC9     26.9998,27.0236                                         str
ORSECA   [5:2052, 2050:2081]                                     str
CCDSECD  [2049:4096, 2049:4096]                                  str
CRYOTEMP 162.97                                                  float
DATASECC [5:2052, 2114:4161]                                     str
DAC14    0.0,0.7904                                              str
TRIMSECD [2181:4228, 2114:4161]                                  str
CLOCK4   3.9999,-4.0002                                          str
CLOCK12  3.0,-8.0001                                             str
OFFSET1  -1.5,15.7796                                            str
BIASSECD [2117:2180, 2114:4161]                                  str
ORSECC   [5:2052, 2082:2113]                                     str
CLOCK6   3.9999,-4.0002                                          str
PRESECA  [1:4, 2:2049]                                           str
CLOCK8   3.0,-8.0001                                             str
DELAYS   13, 13, 25, 25, 8, 3000, 7, 7, 400, 7                   str
DATASECB [2181:4228, 2:2049]                                     str
DAC10    26.9998,27.0682                                         str
DATASECD [2181:4228, 2114:4161]                                  str
DAC6     0.0,-0.0105                                             str
BIASSECB [2117:2180, 2:2049]                                     str
ORSECB   [2181:4228, 2050:2081]                                  str
DAC11    26.9998,26.5191                                         str
AMPSECD  [4096:2049, 4096:2049]                                  str
DETSECA  [1:2048, 1:2048]                                        str
CLOCK13  3.0,-8.0001                                             str
CCDNAME  CCDSM10B                                                str
AMPSECA  [1:2048, 1:2048]                                        str
CPUTEMP  57.9785                                                 float
CAMERA   b1                                                      str
PRESECD  [4229:4232, 2114:4161]                                  str
PRESECC  [1:4, 2114:4161]                                        str
CLOCK16  0.0,0.0                                                 str
DETSECD  [2049:4096, 2049:4096]                                  str
AMPSECC  [2048:1, 2049:4096]                                     str
ORSECD   [2181:4228, 2082:2113]                                  str
TRIMSECC [5:2052, 2114:4161]                                     str
CLOCK18  3.9999,-4.0002                                          str
DETSECB  [2049:4096, 1:2048]                                     str
CLOCK17  3.9999,-4.0002                                          str
CLOCK5   3.9999,-4.0002                                          str
DAC3     15.9998,15.9444                                         str
PRRSECB  [2181:4228, 1:1]                                        str
DAC1     15.9998,15.7796                                         str
DAC0     15.9998,15.9547                                         str
PRRSECD  [2181:4228, 4162:4162]                                  str
DAC8     26.9998,27.0088                                         str
BLDTIME  0.3551                                                  float
CLOCK14  3.0,-8.0001                                             str
OFFSET3  -1.5,15.9341                                            str
DAC16    0.0,0.2772                                              str
TRIMSECB [2181:4228, 2:2049]                                     str
DAC4     0.0,-0.0105                                             str
CCDSECC  [1:2048, 2049:4096]                                     str
PRRSECC  [5:2052, 4162:4162]                                     str
CLOCK1   3.9999,-4.0002                                          str
PRRSECA  [5:2052, 1:1]                                           str
DAC17    -0.0,0.061                                              str
CLOCK7   6.9999,-2.0001                                          str
DAC12    0.0,5.0752                                              str
CDSPARMS 350, 350, 8, 1000                                       str
CCDSIZE  4162,4232                                               str
CCDTMING flatdark_sta_timing.txt                                 str
OFFSET4  -1.2599999904632568,-0.0053                             str
DIGITIME 49.545                                                  float
DETSECC  [1:2048, 2049:4096]                                     str
CCDSECB  [2049:4096, 1:2048]                                     str
CCDSECA  [1:2048, 1:2048]                                        str
OFFSET7  -1.4700000286102295,-0.0263                             str
CLOCK0   3.9999,-4.0002                                          str
DAC15    19.9997,19.812                                          str
BIASSECA [2053:2116, 2:2049]                                     str
CLOCK9   3.0,-8.0001                                             str
OFFSET2  -1.5,15.8208                                            str
TRIMSECA [5:2052, 2:2049]                                        str
OFFSET0  -1.5,15.965                                             str
CRYOPRES 8.794e-08                                               str
OFFSET5  -1.309999942779541,-0.021                               str
DETECTOR sn22822                                                 str
SETTINGS detectors_sm_20210128.json                              str
DATASECA [5:2052, 2:2049]                                        str
CLOCK15  0.0,0.0                                                 str
AMPSECB  [2049:4096, 2048:1]                                     str
DAC13    0.0,-5.0232                                             str
CLOCK10  3.0,-8.0001                                             str
OFFSET6  -1.5199999809265137,-0.0158                             str
DAC2     15.9998,15.8105                                         str
CLOCK11  0.0,0.0                                                 str
CLOCK2   3.9999,-4.0002                                          str
CLOCK3   6.9999,-2.0001                                          str
REQTIME  100.0                                                   float
OBSID    kp4m20210625t005156                                     str
PROCTYPE RAW                                                     str
PRODTYPE image                                                   str
GAINA    1.308                                                   float
SATULEVA 35000.0                                                 float
OVERSCNA 1208.720593091835                                       float
OBSRDNA  5.319229645440016                                       float
SATUELEA 44198.99346423588                                       float
GAINB    1.286                                                   float
SATULEVB 36000.0                                                 float
OVERSCNB 1206.300288531992                                       float
OBSRDNB  3.250851570254362                                       float
SATUELEB 44744.69782894786                                       float
GAINC    1.288                                                   float
SATULEVC 45000.0                                                 float
OVERSCNC 1192.14201160539                                        float
OBSRDNC  4.31948644183243                                        float
SATUELEC 56424.52108905226                                       float
GAIND    1.304                                                   float
SATULEVD 36000.0                                                 float
OVERSCND 1180.660787266955                                       float
OBSRDND  3.202120109933047                                       float
SATUELED 45404.41833340389                                       float
FIBERMIN 500                                                     int
BZERO    32768                                                   int
BSCALE   1                                                       int
MODULE   CI                                                      str
FRAMES   None                                                    Unknown
COSMSPLT F                                                       bool
MAXSPLIT 0                                                       int
OBSTYPE  FLAT                                                    str
MANIFEST F                                                       bool
OBJECT                                                           str
NTSSURVY na                                                      str
SEQID    2 requests                                              str
SEQNUM   1                                                       int
SEQTOT   2                                                       int
SEQSTART 2021-06-25T00:51:53.096588                              str
CAMSHUT  open                                                    str
WHITESPT T                                                       bool
ZENITH   F                                                       bool
SEANNEX  F                                                       bool
BEYONDP  F                                                       bool
FIDUCIAL off                                                     str
AIRMASS  1.521257                                                float
FOCUS    868.0,-522.3,-1055.0,-1.7,11.9,0.0                      str
PMREADY  F                                                       bool
DOMEAZ   106.727                                                 float
DOMINPOS F                                                       bool
GUIDOFFR 0.0                                                     float
GUIDOFFD -0.0                                                    float
SUNRA    94.038905                                               float
SUNDEC   23.384181                                               float
MOONDEC  -25.604587                                              float
MOONRA   277.758043                                              float
MOONSEP  163.761                                                 float
MOUNTAZ  286.506498                                              float
MOUNTDEC 31.96357                                                float
MOUNTEL  41.037384                                               float
MOUNTHA  58.477846                                               float
INCTRL   F                                                       bool
INPOS    T                                                       bool
MNTOFFD  -0.0                                                    float
MNTOFFR  -0.0                                                    float
PARALLAC 73.49407                                                float
SKYDEC   31.96357                                                float
SKYRA    116.298974                                              float
TARGTDEC 31.963305                                               float
TARGTRA  89.002025                                               float
TARGTAZ  296.183791                                              float
TARGTEL  19.467294                                               float
TRGTOFFD 0.0                                                     float
TRGTOFFR 0.0                                                     float
ZD       48.962616                                               float
TCSST    11:39:06.437                                            str
TCSMJD   59390.036509                                            float
SEEING   None                                                    Unknown
TRANSPAR None                                                    Unknown
ADCCORR  F                                                       bool
ADC1PHI  8.50000000127693e-05                                    float
ADC2PHI  0.000176                                                float
ADC1HOME F                                                       bool
ADC2HOME F                                                       bool
ADC1NREV 0.0                                                     float
ADC2NREV 0.0                                                     float
ADC1STAT STOPPED                                                 str
ADC2STAT STOPPED                                                 str
HEXPOS   868.0,-522.3,-1055.0,-1.7,11.9,0.0                      str
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                                 str
ROTOFFST 0.0                                                     float
ROTENBLD F                                                       bool
ROTRATE  0.0                                                     float
RESETROT F                                                       bool
GUIDMODE catalog                                                 str
SPCGRPHS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                 str
ILLSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                 str
CCDSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                 str
UPSSTAT  SUCCESS                                                 str
FILENAME /exposures/desi/20210624/00095882/desi-00095882.fits.fz str
EXCLUDED                                                         str
TCSKRA   0.3 0.003 0.00003                                       str
TCSKDEC  0.3 0.003 0.00003                                       str
TCSGRA   0.3                                                     float
TCSGDEC  0.3                                                     float
TCSMFRA  1                                                       int
TCSMFDEC 1                                                       int
TCSPIRA  1.0,0.0,0.0,0.0                                         str
TCSPIDEC 1.0,0.0,0.0,0.0                                         str
CHECKSUM OCAAO986OCAAO975                                        str     HDU checksum updated 2021-07-07T16:47:44
DATASUM  3603410927                                              str     data unit checksum updated 2021-07-07T16:47:44
======== ======================================================= ======= ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

===================== ======= ================== ===========
Name                  Type    Units              Description
===================== ======= ================== ===========
TARGETID              int64
DESI_TARGET           int64
BGS_TARGET            int64
MWS_TARGET            int64
SECONDARY_TARGET      int64
TARGET_RA             float64 deg
TARGET_DEC            float64 deg
TARGET_RA_IVAR        float64 deg-2
TARGET_DEC_IVAR       float64 deg-2
BRICKID               int64
BRICK_OBJID           int64
MORPHTYPE             char[4]
PRIORITY              int32
SUBPRIORITY           float64
REF_ID                int64
PMRA                  float32 10**-3 arcsec yr-1
PMDEC                 float32 10**-3 arcsec yr-1
REF_EPOCH             float32
PMRA_IVAR             float32 10**6 arcsec-2 yr2
PMDEC_IVAR            float32 10**6 arcsec-2 yr2
RELEASE               int16
FLUX_G                float32 nanomaggies
FLUX_R                float32 nanomaggies
FLUX_Z                float32 nanomaggies
FLUX_W1               float32 nanomaggies
FLUX_W2               float32 nanomaggies
FLUX_IVAR_G           float32 1/nanomaggies**2
FLUX_IVAR_R           float32 1/nanomaggies**2
FLUX_IVAR_Z           float32 1/nanomaggies**2
FLUX_IVAR_W1          float32 1/nanomaggies**2
FLUX_IVAR_W2          float32 1/nanomaggies**2
FIBERFLUX_G           float32 nanomaggies
FIBERFLUX_R           float32 nanomaggies
FIBERFLUX_Z           float32 nanomaggies
FIBERFLUX_W1          float32 nanomaggies
FIBERFLUX_W2          float32 nanomaggies
FIBERTOTFLUX_G        float32 nanomaggies
FIBERTOTFLUX_R        float32 nanomaggies
FIBERTOTFLUX_Z        float32 nanomaggies
FIBERTOTFLUX_W1       float32 nanomaggies
FIBERTOTFLUX_W2       float32 nanomaggies
GAIA_PHOT_G_MEAN_MAG  float32 mag
GAIA_PHOT_BP_MEAN_MAG float32 mag
GAIA_PHOT_RP_MEAN_MAG float32 mag
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
LAMBDA_REF            float32 Angstrom
FIBERASSIGN_X         float32 mm
FIBERASSIGN_Y         float32 mm
FA_TARGET             int64
FA_TYPE               binary
NUMTARGET             int16
FIBER_RA              float64 deg
FIBER_DEC             float64 deg
FIBER_RA_IVAR         float32 deg-2
FIBER_DEC_IVAR        float32 deg-2
PLATEMAKER_X          float32 mm
PLATEMAKER_Y          float32 mm
PLATEMAKER_RA         float32 deg
PLATEMAKER_DEC        float32 deg
NUM_ITER              int32
SPECTROID             int32
EXPTIME               float32 s
===================== ======= ================== ===========


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
