===================
fibermap-EXPID.fits
===================

:Summary: fibermap augmenting the input fiber assignment file with information
          about where the fibers actually ended up from the coordinates file.
:Naming Convention: ``fibermap-{expid}.fits``, where
    ``{expid}`` is the zero-padded 8-digit exposure ID.
:Regex: ``fibermap-[0-9]{8}\.fits``
:File Type: FITS, 1.8 MB

Contents
========

====== ======== ======== ===================
Number EXTNAME  Type     Contents
====== ======== ======== ===================
HDU0_           IMAGE    *Brief Description*
HDU1_  FIBERMAP BINTABLE *Brief Description*
====== ======== ======== ===================


FITS Header Units
=================

HDU0
----

*Summarize the contents of this HDU.*

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = FIBERMAP

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============================================================================= ======= =====================
KEY      Example Value                                                                 Type    Comment
======== ============================================================================= ======= =====================
NAXIS1   369                                                                           int     length of dimension 1
NAXIS2   5000                                                                          int     length of dimension 2
TILEID   80665                                                                         int
TILERA   198.0                                                                         float
TILEDEC  7.0                                                                           float
FIELDROT -0.0392066758196646                                                           float
FA_PLAN  2022-07-01T00:00:00.000                                                       str
FA_HA    0.0                                                                           float
FA_RUN   2020-03-06T00:00:00                                                           str
REQRA    198.0                                                                         float
REQDEC   7.0                                                                           float
FIELDNUM 0                                                                             int
FA_VER   2.1.0.dev2650                                                                 str
FA_SURV  sv1                                                                           str
GFA      /global/cfs/cdirs/desi/target/catalogs/dr9/0.47.0/gfas                        str
SKY      /global/cfs/cdirs/desi/target/catalogs/dr9/0.47.0/skies                       str
SKYSUPP  /global/cfs/cdirs/desi/target/catalogs/gaiadr2/0.47.0/skies-supp              str
TARG     /global/cfs/cdirs/desi/target/catalogs/dr9/0.47.0/targets/sv1/resolve/bright/ str
FAFLAVOR sv1bgsmws                                                                     str
FAOUTDIR /global/cfs/cdirs/desi/users/raichoor/fiberassign-sv1/20210101/               str
PMTIME   2021-01-02T00:00:00.000                                                       str
RUNDATE  2020-03-06T00:00:00                                                           str
SCTARG   STD_WD,BGS_ANY,MWS_ANY                                                        str
OBSCON   DARK|GRAY|BRIGHT                                                              str
BZERO    32768                                                                         int
BSCALE   1                                                                             int
MODULE   CI                                                                            str
EXPID    81528                                                                         int
EXPFRAME 0                                                                             int
FRAMES   None                                                                          Unknown
COSMSPLT F                                                                             bool
MAXSPLIT 0                                                                             int
SPLITIDS 81528                                                                         str
FIBASSGN /data/tiles/SVN_tiles/080/fiberassign-080665.fits.gz                          str
FLAVOR   science                                                                       str
OBSTYPE  SCIENCE                                                                       str
SEQUENCE DESI                                                                          str
MANIFEST F                                                                             bool
OBJECT                                                                                 str
PURPOSE  Commissioning                                                                 str
PROGRAM  sv1bgsmws                                                                     str
NTSSURVY None                                                                          Unknown
PROPID   2019B-5000                                                                    str
OBSERVER DESIObserver                                                                  str
LEAD     RunManager                                                                    str
INSTRUME DESI                                                                          str
OBSERVAT KPNO                                                                          str
OBS-LAT  31.96403                                                                      str
OBS-LONG -111.59989                                                                    str
OBS-ELEV 2097.0                                                                        float
TELESCOP KPNO 4.0-m telescope                                                          str
CORRCTOR DESI Corrector                                                                str
SEQNUM   1                                                                             int
NIGHT    20210322                                                                      int
SEQSTART 2021-03-23T09:59:11.354796                                                    str
TIMESYS  UTC                                                                           str
DATE-OBS 2021-03-23T10:02:18.466574336                                                 str
TIME-OBS 2021-03-23T10:02:18.466574336                                                 str
MJD-OBS  59296.418269288                                                               float
OPENSHUT None                                                                          Unknown
CAMSHUT  open                                                                          str
ST       14:40:21.920000                                                               str
ACQTIME  15.0                                                                          float
GUIDTIME 5.0                                                                           float
FOCSTIME 60.0                                                                          float
SKYTIME  60.0                                                                          float
WHITESPT F                                                                             bool
ZENITH   F                                                                             bool
SEANNEX  F                                                                             bool
BEYONDP  F                                                                             bool
FIDUCIAL off                                                                           str
BACKLIT  off                                                                           str
AIRMASS  1.209915                                                                      float
FOCUS    1357.4,-270.6,901.3,-16.9,35.2,200.4                                          str
VCCD     ON                                                                            str
TRUSTEMP 5.167                                                                         float
PMIRTEMP 5.463                                                                         float
PMREADY  T                                                                             bool
PMCOVER  open                                                                          str
PMCOOL   off                                                                           str
DOMSHUTU open                                                                          str
DOMSHUTL not open                                                                      str
DOMLIGHH off                                                                           str
DOMLIGHL off                                                                           str
DOMEAZ   224.189                                                                       float
DOMINPOS T                                                                             bool
EPOCH    2000.0                                                                        float
GUIDOFFR 0.0                                                                           float
GUIDOFFD -0.0                                                                          float
SUNRA    2.758766                                                                      float
SUNDEC   1.193628                                                                      float
MOONDEC  24.619659                                                                     float
MOONRA   115.929512                                                                    float
MOONSEP  80.554                                                                        float
MOUNTAZ  223.481125                                                                    float
MOUNTDEC 6.99488                                                                       float
MOUNTEL  57.932743                                                                     float
MOUNTHA  21.596638                                                                     float
INCTRL   T                                                                             bool
INPOS    F                                                                             bool
MNTOFFD  -0.0                                                                          float
MNTOFFR  -0.0                                                                          float
PARALLAC 29.851752                                                                     float
SKYDEC   6.99488                                                                       float
SKYRA    197.996292                                                                    float
TARGTDEC 6.99488                                                                       float
TARGTRA  197.996292                                                                    float
TARGTAZ  216.37784                                                                     float
TARGTEL  55.688951                                                                     float
TRGTOFFD 0.0                                                                           float
TRGTOFFR 0.0                                                                           float
ZD       34.294607                                                                     float
TCSST    14:54:13.400                                                                  str
TCSMJD   59296.428298                                                                  float
USEETC   T                                                                             bool
REQTEFF  150.0                                                                         float
ACTTEFF  335.3705                                                                      float
SEEING   1.0863                                                                        float
SKYLEVEL 1.304                                                                         float
PMSEEING 1.08                                                                          float
PMTRANS  103.75                                                                        float
ACQCAM   GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                                     str
GUIDECAM GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                                     str
FOCUSCAM FOCUS1,FOCUS4,FOCUS6,FOCUS9                                                   str
SKYCAM   SKYCAM0,SKYCAM1                                                               str
REQADC   16.83,54.63                                                                   str
ADCCORR  T                                                                             bool
ADC1PHI  9.03999700000003                                                              float
ADC2PHI  50.939993                                                                     float
ADC1HOME F                                                                             bool
ADC2HOME F                                                                             bool
ADC1NREV -1.0                                                                          float
ADC2NREV -1.0                                                                          float
ADC1STAT STOPPED                                                                       str
ADC2STAT STOPPED                                                                       str
USESKY   T                                                                             bool
USEFOCUS T                                                                             bool
HEXPOS   1327.1,-248.3,862.8,-17.6,32.7,198.1                                          str
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                                                       str
USEROTAT T                                                                             bool
ROTOFFST 194.5                                                                         float
ROTENBLD T                                                                             bool
ROTRATE  0.0                                                                           float
RESETROT F                                                                             bool
USEPOS   T                                                                             bool
PETALS   PETAL0,PETAL1,PETAL2,PETAL3,PETAL4,PETAL5,PETAL7,PETAL8,PETAL9                str
POSCYCLE 1                                                                             int
POSONTGT 720                                                                           int
POSONFRC 0.1709                                                                        float
POSDISAB 766                                                                           int
POSENABL 4213                                                                          int
POSRMS   0.3006                                                                        float
POSITER  1                                                                             int
POSFRACT 0.95                                                                          float
POSTOLER 0.005                                                                         float
POSMVALL T                                                                             bool
USEGUIDR T                                                                             bool
GUIDMODE catalog                                                                       str
USEAOS   F                                                                             bool
USEDONUT T                                                                             bool
USESPCTR T                                                                             bool
SPCGRPHS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                                       str
ILLSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                                       str
CCDSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                                       str
TDEWPNT  -9.88                                                                         float
TAIRFLOW 0.0                                                                           float
TAIRITMP 9.2                                                                           float
TAIROTMP 9.6                                                                           float
TAIRTEMP 3.715                                                                         float
TCASITMP 6.6                                                                           float
TCASOTMP 4.7                                                                           float
TCSITEMP 4.8                                                                           float
TCSOTEMP 4.6                                                                           float
TCIBTEMP 0.0                                                                           float
TCIMTEMP 0.0                                                                           float
TCITTEMP 0.0                                                                           float
TCOSTEMP 0.0                                                                           float
TCOWTEMP 0.0                                                                           float
TDBTEMP  5.6                                                                           float
TFLOWIN  0.0                                                                           float
TFLOWOUT 0.0                                                                           float
TGLYCOLI 9.5                                                                           float
TGLYCOLO 9.3                                                                           float
THINGES  5.0                                                                           float
THINGEW  5.0                                                                           float
TPMAVERT 5.42                                                                          float
TPMDESIT 2.0                                                                           float
TPMEIBT  5.6                                                                           float
TPMEITT  5.5                                                                           float
TPMEOBT  5.6                                                                           float
TPMEOTT  5.4                                                                           float
TPMNIBT  5.5                                                                           float
TPMNITT  5.4                                                                           float
TPMNOBT  5.5                                                                           float
TPMNOTT  5.5                                                                           float
TPMRTDT  5.32                                                                          float
TPMSIBT  5.7                                                                           float
TPMSITT  5.5                                                                           float
TPMSOBT  5.6                                                                           float
TPMSOTT  5.4                                                                           float
TPMSTAT  ready                                                                         str
TPMWIBT  5.5                                                                           float
TPMWITT  5.3                                                                           float
TPMWOBT  5.5                                                                           float
TPMWOTT  5.4                                                                           float
TPCITEMP 4.9                                                                           float
TPCOTEMP 4.8                                                                           float
TPR1HUM  0.0                                                                           float
TPR1TEMP 0.0                                                                           float
TPR2HUM  0.0                                                                           float
TPR2TEMP 0.0                                                                           float
TSERVO   40.0                                                                          float
TTRSTEMP 5.4                                                                           float
TTRWTEMP 3.6                                                                           float
TTRUETBT -11.5                                                                         float
TTRUETTT 4.0                                                                           float
TTRUNTBT 4.1                                                                           float
TTRUNTTT 3.8                                                                           float
TTRUSTBT 4.4                                                                           float
TTRUSTST 10.8                                                                          float
TTRUSTTT 5.4                                                                           float
TTRUTSBT 5.2                                                                           float
TTRUTSMT 5.6                                                                           float
TTRUTSTT 5.5                                                                           float
TTRUWTBT 4.2                                                                           float
TTRUWTTT 3.9                                                                           float
ALARM    F                                                                             bool
ALARM-ON F                                                                             bool
BATTERY  100.0                                                                         float
SECLEFT  5892.0                                                                        float
UPSSTAT  System Normal - On Line(7)                                                    str
INAMPS   71.4                                                                          float
OUTWATTS 5300.0,6900.0,5000.0                                                          str
COMPDEW  -10.4                                                                         float
COMPHUM  13.2                                                                          float
COMPAMB  14.5                                                                          float
COMPTEMP 18.4                                                                          float
DEWPOINT 19.3                                                                          float
HUMIDITY 89.0                                                                          float
PRESSURE 795.0                                                                         float
OUTTEMP  21.2                                                                          float
WINDDIR  323.0                                                                         float
WINDSPD  14.7                                                                          float
GUST     14.7                                                                          float
AMNIENTN 14.8                                                                          float
CFLOOR   4.8                                                                           float
NWALLIN  15.0                                                                          float
NWALLOUT 4.1                                                                           float
WWALLIN  14.0                                                                          float
WWALLOUT 4.6                                                                           float
AMBIENTS 15.6                                                                          float
FLOOR    13.7                                                                          float
EWALLCMP 5.1                                                                           float
EWALLCOU 4.7                                                                           float
ROOF     3.8                                                                           float
ROOFAMB  3.9                                                                           float
DOMEBLOW 3.8                                                                           float
DOMEBUP  3.8                                                                           float
DOMELLOW 3.8                                                                           float
DOMELUP  3.9                                                                           float
DOMERLOW 3.8                                                                           float
DOMERUP  3.4                                                                           float
PLATFORM 3.4                                                                           float
SHACKC   14.4                                                                          float
SHACKW   15.3                                                                          float
STAIRSL  3.8                                                                           float
STAIRSM  3.4                                                                           float
STAIRSU  3.4                                                                           float
TELBASE  5.4                                                                           float
UTILWALL 5.1                                                                           float
UTILROOM 3.7                                                                           float
SP0NIRT  139.99                                                                        float
SP0REDT  140.01                                                                        float
SP0BLUT  162.97                                                                        float
SP0NIRP  5.72e-08                                                                      float
SP0REDP  4.365e-08                                                                     float
SP0BLUP  8.492e-08                                                                     float
SP1NIRT  140.01                                                                        float
SP1REDT  140.01                                                                        float
SP1BLUT  163.02                                                                        float
SP1NIRP  5.763e-08                                                                     float
SP1REDP  5.626e-08                                                                     float
SP1BLUP  8.005e-08                                                                     float
SP2NIRT  140.01                                                                        float
SP2REDT  140.01                                                                        float
SP2BLUT  163.02                                                                        float
SP2NIRP  3.98e-08                                                                      float
SP2REDP  6.595e-08                                                                     float
SP2BLUP  8.106e-08                                                                     float
SP3NIRT  139.96                                                                        float
SP3REDT  140.01                                                                        float
SP3BLUT  162.99                                                                        float
SP3NIRP  3.563e-08                                                                     float
SP3REDP  7.043e-08                                                                     float
SP3BLUP  7.597e-08                                                                     float
SP4NIRT  140.01                                                                        float
SP4REDT  140.06                                                                        float
SP4BLUT  163.04                                                                        float
SP4NIRP  6.909e-08                                                                     float
SP4REDP  4.941e-08                                                                     float
SP4BLUP  4.86e-08                                                                      float
SP5NIRT  140.01                                                                        float
SP5REDT  140.01                                                                        float
SP5BLUT  163.04                                                                        float
SP5NIRP  5.735e-08                                                                     float
SP5REDP  5.483e-08                                                                     float
SP5BLUP  1.123e-07                                                                     float
SP6NIRT  140.06                                                                        float
SP6REDT  140.06                                                                        float
SP6BLUT  163.02                                                                        float
SP6NIRP  2.742e-07                                                                     float
SP6REDP  6.32099999999999e-08                                                          float
SP6BLUP  6.008e-08                                                                     float
SP7NIRT  139.99                                                                        float
SP7REDT  139.99                                                                        float
SP7BLUT  162.99                                                                        float
SP7NIRP  6.38399999999999e-08                                                          float
SP7REDP  4.088e-08                                                                     float
SP7BLUP  9.947e-08                                                                     float
SP8NIRT  140.01                                                                        float
SP8REDT  140.01                                                                        float
SP8BLUT  162.97                                                                        float
SP8NIRP  4.708e-08                                                                     float
SP8REDP  9.897e-08                                                                     float
SP8BLUP  8.28999999999999e-08                                                          float
SP9NIRT  140.01                                                                        float
SP9REDT  140.03                                                                        float
SP9BLUT  163.09                                                                        float
SP9NIRP  5.325e-08                                                                     float
SP9REDP  4.768e-08                                                                     float
SP9BLUP  1.205e-07                                                                     float
RADESYS  FK5                                                                           str
TNFSPROC 8.9552                                                                        float
TGFAPROC 7.1861                                                                        float
SIMGFAP  F                                                                             bool
USEFVC   T                                                                             bool
USEFID   T                                                                             bool
USEILLUM T                                                                             bool
USEXSRVR T                                                                             bool
USEOPENL T                                                                             bool
STOPGUDR T                                                                             bool
STOPFOCS T                                                                             bool
STOPSKY  T                                                                             bool
KEEPGUDR F                                                                             bool
KEEPFOCS F                                                                             bool
KEEPSKY  F                                                                             bool
REACQUIR F                                                                             bool
FILENAME /exposures/desi/20210322/00081528/desi-00081528.fits.fz                       str
EXCLUDED                                                                               str
DOSVER   trunk                                                                         str
OCSVER   1.2                                                                           float
CONSTVER DESI:CURRENT                                                                  str
INIFILE  /data/msdos/dos_home/architectures/kpno/desi_nopetal6.ini                     str
REQTIME  768.478                                                                       float
SIMGFACQ F                                                                             bool
TCSKRA   0.3 0.003 0.00003                                                             str
TCSKDEC  0.3 0.003 0.00003                                                             str
TCSGRA   0.3                                                                           float
TCSGDEC  0.3                                                                           float
TCSMFRA  1                                                                             int
TCSMFDEC 1                                                                             int
TCSPIRA  1.0,0.0,0.0,0.0                                                               str
TCSPIDEC 1.0,0.0,0.0,0.0                                                               str
POSCNVGD F                                                                             bool
GUIEXPID 81528                                                                         int
IGFRMNUM 10                                                                            int
FOCEXPID 81528                                                                         int
IFFRMNUM 1                                                                             int
SKYEXPID 81528                                                                         int
ISFRMNUM 0                                                                             int
FGFRMNUM 104                                                                           int
FFFRMNUM 13                                                                            int
FSFRMNUM 10                                                                            int
SEQID    2 requests                                                                    str
SEQTOT   2                                                                             int
DELTARA  None                                                                          Unknown
DELTADEC None                                                                          Unknown
SHFTFOCS 220.0                                                                         float
GSGUIDE5 (720.13,182.73),(293.93,1434.18)                                              str
GSGUIDE7 (147.69,1766.58),(701.47,941.61)                                              str
GSGUIDE8 (610.21,1369.42),(283.54,513.46)                                              str
FVCTIME  2.0                                                                           float
GSGUIDE0 (834.09,1970.76),(637.93,271.65)                                              str
GSGUIDE2 (193.23,1297.92),(785.62,1926.10)                                             str
GSGUIDE3 (778.02,476.21),(732.69,823.86)                                               str
ARCHIVE  /exposures/desi/20210322/00081528/guide-00081528.fits.fz                      str
GUIDEFIL guide-00081528.fits.fz                                                        str
COORDFIL coordinates-00081528.fits                                                     str
======== ============================================================================= ======= =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

===================== ======= ===== ===========
Name                  Type    Units Description
===================== ======= ===== ===========
TARGETID              int64
PETAL_LOC             int16
DEVICE_LOC            int32
LOCATION              int64
FIBER                 int32
FIBERSTATUS           int32
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


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
