=================
fvc-primary-EXPID
=================

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``fvc-primary-EXPID.fits``, where EXPID is the zero-padded
    8-digit exposure ID.
:Regex: ``fvc-primary-[0-9]{8}\.fits``
:File Type: FITS, 19 KB

Contents
========

====== ======= ===== ===================
Number EXTNAME Type  Contents
====== ======= ===== ===================
HDU0_  fvc     IMAGE *Brief Description*
====== ======= ===== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = fvc

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================================================ ======= =======
    KEY      Example Value                                    Type    Comment
    ======== ================================================ ======= =======
    FVCTIME  2.0                                              float
    EXPTIME  None                                             Unknown
    REQTIME  2.0                                              float
    IMAGECAM FVC                                              str
    EXPID    51406                                            int
    OBSERVER DESIObserver                                     str
    PROPID   2019B-5000                                       str
    PROGRAM  FVC alt-az dome closed                           str
    LEAD     RunManager                                       str
    RADESYS  FK5                                              str
    TIMESYS  UTC                                              str
    EPOCH    2000.0                                           float
    DOSVER   trunk                                            str
    OCSVER   1.2                                              float
    INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini str
    INSTRUME DESI                                             str
    CONSTVER DESI:CURRENT                                     str
    CORRCTOR DESI Corrector                                   str
    TELESCOP KPNO 4.0-m telescope                             str
    OBSERVAT KPNO                                             str
    OBS-ELEV 2097.0                                           float
    OBS-LAT  31.96403                                         str
    OBS-LONG -111.59989                                       str
    NIGHT    20200220                                         int
    DATE-OBS 2020-02-21T11:04:11.878701                       str
    MJD-OBS  58900.4612486                                    float
    OPENSHUT 2020-02-21T11:04:11.878701                       str
    ST       13:41:09.750                                     str
    SEQUENCE FVC                                              str
    FLAVOR   science                                          str
    DELTARA  0.0                                              float
    DELTADEC 0.0                                              float
    EXCLUDED                                                  str
    GUIDMODE catalog                                          str
    MANIFEST F                                                bool
    OBJECT                                                    str
    SEQID    20 requests                                      str
    SEQTOT   20                                               int
    SEQNUM   5                                                int
    CAMSHUT  open                                             str
    INPOS    T                                                bool
    INCTRL   T                                                bool
    DOMINPOS T                                                bool
    WHITESPT F                                                bool
    ZENITH   F                                                bool
    SEANNEX  F                                                bool
    BEYONDP  F                                                bool
    SKYRA    205.295743                                       float
    SKYDEC   -28.030359                                       float
    TARGTRA  204.369079                                       float
    TARGTDEC -28.0367                                         float
    TARGTAZ  180.937824                                       float
    TARGTEL  29.993611                                        float
    TRGTOFFR 0.0                                              float
    TRGTOFFD 0.0                                              float
    GUIDOFFR 0.0                                              float
    GUIDOFFD -0.0                                             float
    MNTOFFR  -0.0                                             float
    MNTOFFD  -0.0                                             float
    AIRMASS  1.994121                                         float
    MOUNTHA  -0.006443                                        float
    MOUNTAZ  179.993433                                       float
    MOUNTEL  30.006341                                        float
    MOUNTDEC -28.030359                                       float
    PARALLAC -0.006312                                        float
    ZD       59.993659                                        float
    TCSST    13:41:09.432                                     str
    TCSMJD   58900.461678                                     float
    DOMEAZ   184.424                                          float
    PMREADY  T                                                bool
    MOONRA   310.75149                                        float
    MOONDEC  -20.881956                                       float
    TCSKRA   0.15 0.003 0.00003                               str
    TCSKDEC  0.15 0.003 0.00003                               str
    TCSGRA   0.3                                              float
    TCSGDEC  0.3                                              float
    TCSMFRA  1                                                int
    TCSMFDEC 1                                                int
    TCSPIRA  1.0,0.0,0.0,0.0                                  str
    TCSPIDEC 1.0,1.0,0.0,0.0                                  str
    ADC1PHI  359.999931                                       float
    ADC2PHI  0.000101                                         float
    ADC1HOME F                                                bool
    ADC2HOME F                                                bool
    ADC1NREV 0.0                                              float
    ADC2NREV 0.0                                              float
    ADC1STAT STOPPED                                          str
    ADC2STAT STOPPED                                          str
    HEXPOS   1139.5,-480.5,61.0,-3.1,25.0,-0.0                str
    HEXTRIM  0.0,0.0,-46.0,0.0,0.0,0.0                        str
    ROTENBLD T                                                bool
    ROTOFFST 153.1                                            float
    ROTRATE  0.496                                            float
    UPSSTAT  System Normal - On Line(7)                       str
    FIDUCIAL off                                              str
    FOCUS    1139.5,-480.5,61.0,-3.1,25.0,-0.0                str
    COMPAMB  19.6                                             float
    COMPTEMP 20.4                                             float
    COMPDEW  -2.0                                             float
    COMPHUM  22.1                                             float
    ALARM    F                                                bool
    ALARM-ON F                                                bool
    SECLEFT  5922.0                                           float
    BATTERY  100.0                                            float
    INAMPS   65.6                                             float
    OUTWATTS 4500.0,6600.0,4400.0                             str
    TPMAVERT 10.927                                           float
    TPMDESIT 8.0                                              float
    TSERVO   40.0                                             float
    TAIRTEMP 11.068                                           float
    TDEWPNT  -3.42                                            float
    TAIRFLOW 0.0                                              float
    TPR1HUM  -100.0                                           float
    TPR1TEMP -100.0                                           float
    TPR2HUM  -99.99                                           float
    TPR2TEMP -99.99                                           float
    TFLOWIN  0.0                                              float
    TFLOWOUT 0.0                                              float
    TPMRTDT  -99.9                                            float
    TPMNIBT  10.6                                             float
    TPMEIBT  10.7                                             float
    TPMSIBT  10.7                                             float
    TPMWIBT  10.5                                             float
    TPMNOBT  11.0                                             float
    TPMEOBT  10.6                                             float
    TPMSOBT  10.7                                             float
    TPMWOBT  10.6                                             float
    TPMNITT  10.7                                             float
    TPMEITT  10.7                                             float
    TPMSITT  10.8                                             float
    TPMWITT  10.7                                             float
    TPMNOTT  11.2                                             float
    TPMEOTT  11.1                                             float
    TPMSOTT  11.0                                             float
    TPMWOTT  11.0                                             float
    TGLYCOLI 12.3                                             float
    TGLYCOLO 12.1                                             float
    TAIRITMP 12.2                                             float
    TAIROTMP 12.2                                             float
    TTRUNTTT 11.7                                             float
    TTRUETTT 11.7                                             float
    TTRUSTTT 11.7                                             float
    TTRUWTTT 11.7                                             float
    TTRUNTBT 11.6                                             float
    TTRUETBT 11.5                                             float
    TTRUSTBT 11.7                                             float
    TTRUWTBT 11.4                                             float
    TTRUSTST 12.3                                             float
    TTRUTSBT 12.4                                             float
    TTRUTSMT 12.5                                             float
    TTRUTSTT 12.3                                             float
    TTRSTEMP 12.1                                             float
    TTRWTEMP 11.9                                             float
    THINGES  12.3                                             float
    THINGEW  11.8                                             float
    TCOSTEMP 21.7                                             float
    TCOWTEMP 21.6                                             float
    TCIBTEMP 21.6                                             float
    TCIMTEMP 21.6                                             float
    TCITTEMP 21.7                                             float
    TCSITEMP 11.5                                             float
    TCSOTEMP 11.9                                             float
    TPCITEMP 11.0                                             float
    TPCOTEMP 11.0                                             float
    TCASITMP 10.6                                             float
    TCASOTMP 11.9                                             float
    TDBTEMP  11.3                                             float
    TPMSTAT  ready                                            str
    TRUSTEMP 12.4                                             float
    PMIRTEMP 10.9                                             float
    PLATFORM 11.0                                             float
    STAIRSU  11.1                                             float
    STAIRSM  11.0                                             float
    STAIRSL  11.1                                             float
    DOMELUP  10.9                                             float
    DOMELLOW 11.3                                             float
    DOMEBUP  11.0                                             float
    DOMEBLOW 11.1                                             float
    DOMERUP  10.8                                             float
    DOMERLOW 11.2                                             float
    NWALLIN  15.1                                             float
    WWALLIN  14.1                                             float
    FLOOR    13.7                                             float
    SHACKC   16.0                                             float
    SHACKW   14.3                                             float
    AMNIENTN 14.3                                             float
    AMBIENTS 15.7                                             float
    NWALLOUT 10.2                                             float
    WWALLOUT 11.1                                             float
    CFLOOR   10.2                                             float
    TELBASE  10.9                                             float
    UTILROOM 11.3                                             float
    UTILWALL 11.4                                             float
    EWALLCOU 11.1                                             float
    EWALLCMP 11.7                                             float
    ROOF     11.1                                             float
    ROOFAMB  10.9                                             float
    DOMSHUTU not open                                         str
    DOMSHUTL not open                                         str
    DOMLIGHH off                                              str
    DOMLIGHL off                                              str
    PMCOVER  open                                             str
    WINDSPD  11.2                                             float
    WINDDIR  209.6                                            float
    HUMIDITY 31.0                                             float
    PRESSURE 793.5                                            float
    OUTTEMP  11.7                                             float
    DEWPOINT -4.9                                             float
    GUST     117.6                                            float
    AOS      F                                                bool
    ======== ================================================ ======= =======

Empty HDU.


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
