==============
fibermap-EXPID
==============

:Summary: fibermap augmenting the input fiber assignment file with information
          about where the fibers actually ended up from the coordinates file.
:Naming Convention: ``fibermap-{expid}.fits``, where
    ``{expid}`` is the zero-padded 8-digit exposure ID.
:Regex: ``fibermap-[0-9]{8}.fits``
:File Type: FITS, 2 MB 

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

======== ======================================================== ===== =====================
KEY      Example Value                                            Type  Comment
======== ======================================================== ===== =====================
NAXIS1   571                                                      int   length of dimension 1
NAXIS2   5000                                                     int   length of dimension 2
TILERA   170.0                                                    float
FIELDROT 0.0426318411116135                                       float
FA_RUN   2019-09-16T00:00:00                                      str
FA_SURV  cmx                                                      str
FA_HA    0.0                                                      float
REQDEC   60.0                                                     float
TILEID   63227                                                    int
TILEDEC  60.0                                                     float
FIELDNUM 0                                                        int
FA_VER   1.3.0.dev2495                                            str
REQRA    170.0                                                    float
FA_PLAN  2022-07-01T00:00:00.000                                  str
OBSERVAT KPNO                                                     str
OBS-LAT  31.96403                                                 str
OBS-LONG -111.59989                                               str
OBS-ELEV 2097.0                                                   float
TELESCOP KPNO 4.0-m telescope                                     str
INSTRUME DESI                                                     str
CORRCTOR DESI Corrector                                           str
PROGRAM  Dither fibermode tile 63227 (170, 60)                    str
OBSERVER DESIObserver                                             str
LEAD     Luke Tyas                                                str
PROPID   2019B-5000                                               str
MANIFEST F                                                        bool
EXPID    53250                                                    int
FRAMES   24                                                       int
SEQUENCE DESI                                                     str
SEQNUM   1                                                        int
FLAVOR   science                                                  str
OBSTYPE  SCIENCE                                                  str
REQTIME  60.0                                                     float
EXPTIME  15.0                                                     float
OBJECT                                                            str
CAMSHUT  open                                                     str
FIDUCIAL off                                                      str
FOCUS    1144.5,-685.2,277.3,12.3,24.3,0.3                        str
ACQTIME  15.0                                                     float
GUIDTIME 5.0                                                      float
FVCTIME  2.0                                                      float
TIMESYS  UTC                                                      str
RADESYS  FK5                                                      str
EPOCH    2000.0                                                   float
NIGHT    20200305                                                 int
DATE-OBS 2020-03-06T07:35:53.542919                               str
MJD-OBS  58914.31659193                                           float
ST       11:07:28.930                                             str
TARGTRA  170.001079                                               float
TARGTDEC 60.00562                                                 float
TARGTEL  61.880521                                                float
TARGTAZ  3.323334                                                 float
TRGTOFFD 0.0                                                      float
TRGTOFFR 0.0                                                      float
SKYRA    170.001079                                               float
SKYDEC   60.00562                                                 float
ZD       28.119479                                                float
MOUNTHA  -3.13299                                                 float
MOUNTAZ  3.323334                                                 float
MOUNTEL  61.880521                                                float
MOUNTDEC 60.00562                                                 float
INCTRL   T                                                        bool
INPOS    T                                                        bool
WHITESPT F                                                        bool
ZENITH   F                                                        bool
SEANNEX  F                                                        bool
BEYONDP  F                                                        bool
PMREADY  T                                                        bool
PMCOVER  open                                                     str
MNTOFFD  -0.0                                                     float
MNTOFFR  -0.0                                                     float
PARALLAC -174.354122                                              float
DOMEAZ   9.046                                                    float
DOMINPOS T                                                        bool
DOMSHUTU open                                                     str
DOMSHUTL not open                                                 str
DOMLIGHH off                                                      str
DOMLIGHL off                                                      str
TCSKRA   0.15 0.003 0.00003                                       str
TCSKDEC  0.15 0.003 0.00003                                       str
TCSGRA   0.3                                                      float
TCSGDEC  0.3                                                      float
TCSMFRA  1                                                        int
TCSMFDEC 1                                                        int
TCSPIRA  1.0,0.0,0.0,0.0                                          str
TCSPIDEC 1.0,1.0,0.0,0.0                                          str
GUIDOFFR 0.0                                                      float
GUIDOFFD -0.0                                                     float
AIRMASS  1.133533                                                 float
SPCGRPHS SP0,SP1,SP3,SP4,SP5,SP6,SP7,SP8,SP9                      str
TNFSPROC 20.0846                                                  float
MOONRA   121.182164                                               float
MOONDEC  22.382233                                                float
GUIDMODE catalog                                                  str
AOS      F                                                        bool
TCSST    11:07:28.341                                             str
TCSMJD   58914.317018                                             float
TDEWPNT  -5.257                                                   float
TAIRFLOW 0.0                                                      float
TAIRITMP 11.0                                                     float
TAIROTMP 11.3                                                     float
TAIRTEMP 9.315                                                    float
TCASITMP 10.6                                                     float
TCASOTMP 10.4                                                     float
TCSITEMP 8.7                                                      float
TCSOTEMP 10.2                                                     float
TCIBTEMP 21.6                                                     float
TCIMTEMP 21.6                                                     float
TCITTEMP 21.7                                                     float
TCOSTEMP 21.7                                                     float
TCOWTEMP 21.6                                                     float
TDBTEMP  8.9                                                      float
TFLOWIN  0.0                                                      float
TFLOWOUT 0.0                                                      float
TGLYCOLI 11.0                                                     float
TGLYCOLO 10.8                                                     float
THINGES  10.6                                                     float
THINGEW  10.0                                                     float
TPMAVERT 7.89                                                     float
TPMDESIT 6.0                                                      float
TPMEIBT  7.6                                                      float
TPMEITT  7.2                                                      float
TPMEOBT  7.8                                                      float
TPMEOTT  8.4                                                      float
TPMNIBT  7.7                                                      float
TPMNITT  7.4                                                      float
TPMNOBT  8.7                                                      float
TPMNOTT  8.8                                                      float
TPMRTDT  -99.9                                                    float
TPMSIBT  7.5                                                      float
TPMSITT  7.2                                                      float
TPMSOBT  7.4                                                      float
TPMSOTT  8.3                                                      float
TPMSTAT  ready                                                    str
TPMWIBT  7.3                                                      float
TPMWITT  7.2                                                      float
TPMWOBT  7.9                                                      float
TPMWOTT  8.7                                                      float
TPCITEMP 8.2                                                      float
TPCOTEMP 8.2                                                      float
TPR1HUM  -100.0                                                   float
TPR1TEMP -100.0                                                   float
TPR2HUM  -99.99                                                   float
TPR2TEMP -99.99                                                   float
TSERVO   40.0                                                     float
TTRSTEMP 10.1                                                     float
TTRWTEMP 10.0                                                     float
TTRUETBT 10.0                                                     float
TTRUETTT 10.4                                                     float
TTRUNTBT 10.2                                                     float
TTRUNTTT 10.4                                                     float
TTRUSTBT 10.2                                                     float
TTRUSTST 10.9                                                     float
TTRUSTTT 10.3                                                     float
TTRUTSBT 10.7                                                     float
TTRUTSMT 10.7                                                     float
TTRUTSTT 10.7                                                     float
TTRUWTBT 10.1                                                     float
TTRUWTTT 10.4                                                     float
TRUSTEMP 10.7                                                     float
PMIRTEMP 7.9                                                      float
ALARM    F                                                        bool
ALARM-ON F                                                        bool
BATTERY  100.0                                                    float
SECLEFT  5412.0                                                   float
UPSSTAT  System Normal - On Line(7)                               str
INAMPS   69.2                                                     float
OUTWATTS 4700.0,6900.0,4800.0                                     str
COMPDEW  -4.2                                                     float
COMPHUM  19.6                                                     float
COMPAMB  18.4                                                     float
COMPTEMP 19.7                                                     float
DEWPOINT -8.8                                                     float
GUST     117.6                                                    float
HUMIDITY 26.0                                                     float
PRESSURE 793.2                                                    float
OUTTEMP  9.9                                                      float
WINDDIR  111.6                                                    float
WINDSPD  34.0                                                     float
CFLOOR   8.7                                                      float
NWALLIN  13.6                                                     float
NWALLOUT 9.1                                                      float
WWALLIN  13.9                                                     float
WWALLOUT 10.1                                                     float
AMNIENTN 13.3                                                     float
AMBIENTS 14.8                                                     float
FLOOR    13.2                                                     float
EWALLCMP 10.5                                                     float
EWALLCOU 10.1                                                     float
ROOF     9.6                                                      float
ROOFAMB  9.6                                                      float
DOMEBLOW 9.8                                                      float
DOMEBUP  9.9                                                      float
DOMELLOW 9.6                                                      float
DOMELUP  9.4                                                      float
DOMERLOW 9.8                                                      float
DOMERUP  9.4                                                      float
PLATFORM 9.2                                                      float
SHACKC   15.4                                                     float
SHACKW   13.8                                                     float
STAIRSL  9.4                                                      float
STAIRSM  9.3                                                      float
STAIRSU  9.3                                                      float
TELBASE  9.9                                                      float
UTILWALL 9.9                                                      float
UTILROOM 9.9                                                      float
GUIDECAM GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                str
ACQCAM   GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                str
MODULE   GUIDE                                                    str
REQADC   184.59,187.01                                            str
ADC1PHI  184.590061                                               float
ADC2PHI  187.011608                                               float
ADC1HOME F                                                        bool
ADC2HOME F                                                        bool
ADC1NREV 0.0                                                      float
ADC2NREV -2.0                                                     float
ADC1STAT STOPPED                                                  str
ADC2STAT STOPPED                                                  str
ADCCORR  T                                                        bool
HEXPOS   1144.5,-685.2,277.3,12.3,24.3,0.3                        str
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                                  str
ROTOFFST 80.7                                                     float
ROTENBLD T                                                        bool
ROTRATE  0.709                                                    float
EXCLUDED                                                          str
OCSVER   1.2                                                      float
DOSVER   trunk                                                    str
CONSTVER DESI:CURRENT                                             str
USESPCTR T                                                        bool
USEGUIDR T                                                        bool
USEFVC   T                                                        bool
USEFID   T                                                        bool
USEETC   F                                                        bool
USESKY   F                                                        bool
USEFOCUS F                                                        bool
USEDONUT F                                                        bool
USEXSRVR T                                                        bool
USEROTAT T                                                        bool
USEILLUM T                                                        bool
USEPOS   T                                                        bool
SIMGFAP  F                                                        bool
USEOPENL T                                                        bool
RESETROT T                                                        bool
STOPGUDR T                                                        bool
STOPFOCS T                                                        bool
STOPSKY  T                                                        bool
KEEPGUDR T                                                        bool
KEEPFOCS T                                                        bool
KEEPSKY  T                                                        bool
REACQUIR F                                                        bool
INIFILE  /data/msdos/dos_home/architectures/kpno/desi-2.ini       str
OPENSHUT 2020-03-06T07:35:53.542919                               str
GSGUIDE0 (616.11,1662.71),(331.53,973.58)                         str
GSGUIDE2 (38.77,1723.73),(208.88,1145.69)                         str
GSGUIDE3 (357.85,691.55),(248.32,146.62)                          str
GSGUIDE5 (136.72,1802.69),(136.72,1802.69),(127.10,1125.30)       str
GSGUIDE7 (730.18,1227.96)                                         str
GSGUIDE8 (593.31,289.10)                                          str
ARCHIVE  /exposures/desi/20200305/00053250/guide-00053250.fits.fz str
GUIDEFIL guide-00053250.fits.fz                                   str
COORDFIL coordinates-00053250.fits                                str
======== ======================================================== ===== =====================

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
