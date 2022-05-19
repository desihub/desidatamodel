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
HDU0_           IMAGE    Keywords only
HDU1_  FIBERMAP BINTABLE *Brief Description*
====== ======== ======== ===================


FITS Header Units
=================

HDU0
----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    CHECKSUM C6gEC3Z9C3dCC3Z9 str  HDU checksum updated 2022-02-14T05:35:59
    DATASUM  0                str  data unit checksum updated 2022-02-14T05:35:59
    ======== ================ ==== ==============================================

Empty HDU.

HDU1
----

EXTNAME = FIBERMAP

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ======================================================================== ======= ===============================================
    KEY      Example Value                                                            Type    Comment
    ======== ======================================================================== ======= ===============================================
    NAXIS1   385                                                                      int     length of dimension 1
    NAXIS2   5000                                                                     int     length of dimension 2
    TILEID   80616                                                                    int
    TILERA   356.0                                                                    float
    TILEDEC  29.0                                                                     float
    FIELDROT -0.00962199210064233                                                     float
    FA_PLAN  2022-07-01T00:00:00.000                                                  str
    FA_HA    0.0                                                                      float
    FA_RUN   2020-03-06T00:00:00                                                      str
    REQRA    356.0                                                                    float
    REQDEC   29.0                                                                     float
    FIELDNUM 0                                                                        int
    FA_VER   2.0.0.dev2618                                                            str
    FA_SURV  sv1                                                                      str
    LONGSTRN OGIP 1.0                                                                 str     The OGIP Long String Convention may be used.
    GFA      /data/target/catalogs/dr9/0.47.0/gfas                                    str
    SKY      /data/target/catalogs/dr9/0.47.0/skies                                   str
    SKYSUPP  /data/target/catalogs/gaiadr2/0.47.0/skies-supp                          str
    TARG     /data/target/catalogs/dr9/0.47.0/targets/sv1/resolve/bright/             str
    FAFLAVOR sv1bgsmws                                                                str
    FAOUTDIR /software/datasystems/users/raichoor/fiberassign-test/desi-sv1-20201218/ str
    PMTIME   2020-12-18T00:00:00.000                                                  str
    RUNDATE  2020-03-06T00:00:00                                                      str
    SCTARG   STD_WD,BGS_ANY,MWS_ANY                                                   str
    OBSCON   DARK|GRAY|BRIGHT                                                         str
    MODULE   CI                                                                       str     Image Sources/Component
    EXPID    69022                                                                    int     Exposure number
    EXPFRAME 0                                                                        int     Frame number
    COSMSPLT F                                                                        bool    Cosmics split exposure if true
    MAXSPLIT 0                                                                        int     Number of allowed exposure splits
    SPLITIDS 69022                                                                    str     List of expids for split exposures
    FIBASSGN /data/tiles/SVN_tiles/080/fiberassign-080616.fits                        str     Fiber assign fil
    FLAVOR   science                                                                  str     Observation type
    OBSTYPE  SCIENCE                                                                  str     Spectrograph observation type
    SEQUENCE DESI                                                                     str     OCS Sequence name
    MANIFEST F                                                                        bool    DOS exposure manifest
    OBJECT                                                                            str     Object name
    PURPOSE  Commissioning                                                            str     Purpose of observing night
    PROGRAM  SV1 BGS+MWS tile 80616                                                   str     Program name
    PROPID   2019B-5000                                                               str     Proposal ID
    OBSERVER DESIObserver                                                             str     Names of observers
    LEAD     RunManager                                                               str     Lead observer
    INSTRUME DESI                                                                     str     Instrument name
    OBSERVAT KPNO                                                                     str     Observatory name
    OBS-LAT  31.96403                                                                 str     [deg] Observatory latitude
    OBS-LONG -111.59989                                                               str     [deg] Observatory east longitude
    OBS-ELEV 2097.0                                                                   float   [m] Observatory elevation
    TELESCOP KPNO 4.0-m telescope                                                     str     Telescope name
    CORRCTOR DESI Corrector                                                           str     Corrector Identification
    SEQNUM   1                                                                        int     Number of exposure in sequence
    NIGHT    20201220                                                                 int     Observing night
    TIMESYS  UTC                                                                      str     Time system used for date-obs
    DATE-OBS 2020-12-21T02:36:32.099838                                               str     [UTC] Observation data and start time
    MJD-OBS  59204.10870486                                                           float   Modified Julian Date of observation
    OPENSHUT 2020-12-21T02:36:32.099838                                               str     Time shutter opened
    CAMSHUT  open                                                                     str     Shutter status during observation
    ST       01:10:39.210                                                             str     Local Sidereal time at observation start (HH:MM
    ACQTIME  15.0                                                                     float   [s] acqusition image exposure time
    GUIDTIME 5.0                                                                      float   [s] guider GFA exposure time
    FOCSTIME 60.0                                                                     float   [s] focus GFA exposure time
    SKYTIME  60.0                                                                     float   [s] sky camera exposure time (acquisition)
    WHITESPT F                                                                        bool    Telescope is at whitespot
    ZENITH   F                                                                        bool    Telescope is at zenith
    SEANNEX  F                                                                        bool    Telescope is at SE annex
    BEYONDP  F                                                                        bool    Telescope is beyond pole
    FIDUCIAL off                                                                      str     Fiducials status during observation
    BACKLIT  off                                                                      str     Fibers are backlit if True
    AIRMASS  1.060311                                                                 float   Airmass
    FOCUS    1426.5,-501.4,81.0,-2.6,42.3,169.2                                       str     Telescope focus settings
    VCCD     ON                                                                       str     True (ON) if CCD voltage is on
    TRUSTEMP 11.767                                                                   float   [deg] Average Telescope truss temperature (only
    PMIRTEMP 8.925                                                                    float   [deg] Average primary mirror temperature (nit,e
    PMREADY  T                                                                        bool    Primary mirror ready
    PMCOVER  open                                                                     str     Primary mirror cover
    PMCOOL   off                                                                      str     Primary mirror cooling
    DOMSHUTU open                                                                     str     Upper dome shutter
    DOMSHUTL open                                                                     str     Lower dome shutter
    DOMLIGHH off                                                                      str     High dome lights
    DOMLIGHL off                                                                      str     Low dome lights
    DOMEAZ   255.166                                                                  float   [deg] Dome azimuth angle
    DOMINPOS T                                                                        bool    Dome is in position
    EQUINOX  2000.0                                                                   float   Epoch of observation
    GUIDOFFR -0.052283                                                                float   [arcsec] Cummulative guider offset (RA)
    GUIDOFFD 0.136634                                                                 float   [arcsec] Cummulative guider offset (dec)
    MOONDEC  -8.975162                                                                float   [deg] Moon declination at start of exposure
    MOONRA   352.538429                                                               float   [deg] Moon RA at start of exposure
    MOUNTAZ  266.70224                                                                float   [deg] Mount azimuth angle
    MOUNTDEC 28.999221                                                                float   [deg] Mount declination
    MOUNTEL  71.039837                                                                float   [deg] Mount elevation angle
    MOUNTHA  21.769281                                                                float   [deg] Mount hour angle
    INCTRL   T                                                                        bool    DESI in control
    INPOS    T                                                                        bool    Mount in position
    MNTOFFD  -15.76                                                                   float   [arcsec] Mount offset (dec)
    MNTOFFR  29.32                                                                    float   [arcsec] Mount offset (RA)
    PARALLAC 75.635085                                                                float   [deg] Parallactic angle
    SKYDEC   28.999221                                                                float   [deg] Telescope declination (pointing on sky)
    SKYRA    355.996551                                                               float   [deg] Telescope right ascension (pointing on sk
    TARGTDEC 28.999221                                                                float   [deg] Target declination (to TCS)
    TARGTRA  355.996551                                                               float   [deg] Target right ascension (to TCS)
    TARGTAZ  267.074049                                                               float   [deg] Target azimuth
    TARGTEL  70.563787                                                                float   [deg] Target elevation
    TRGTOFFD 0.0                                                                      float   [arcsec] Telescope target offset (dec)
    TRGTOFFR 0.0                                                                      float   [arcsec] Telescope target offset (RA)
    ZD       19.436213                                                                float   [deg] Telescope zenith distance
    TCSST    01:13:18.668                                                             str     Local Sidereal time reported by TCS (HH:MM:SS)
    TCSMJD   59204.110981                                                             float   MJD reported by TCS
    USEETC   F                                                                        bool    ETC data available if true
    ACQCAM   GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                                str     Acquisition cameras used
    GUIDECAM GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                                str     Guide cameras used for t
    FOCUSCAM FOCUS1,FOCUS4,FOCUS6,FOCUS9                                              str     Focus cameras used for this exposure
    SKYCAM   SKYCAM0,SKYCAM1                                                          str     Sky cameras used for this exposure
    REQADC   65.78,85.28                                                              str     [deg] requested ADC angles
    ADCCORR  T                                                                        bool    Correct pointing for ADC setting if True
    ADC1PHI  65.780005                                                                float   [deg] ADC 1 angle
    ADC2PHI  85.279991                                                                float   [deg] ADC 2 angle
    ADC1HOME F                                                                        bool    ADC 1 at home position if True
    ADC2HOME F                                                                        bool    ADC 2 at home position if True
    ADC1NREV -1.0                                                                     float   ADC 1 number of revs
    ADC2NREV 0.0                                                                      float   ADC 2 number of revs
    ADC1STAT STOPPED                                                                  str     ADC 1 status
    ADC2STAT STOPPED                                                                  str     ADC 2 status
    USESKY   T                                                                        bool    DOS Control: use Sky Monitor
    USEFOCUS T                                                                        bool    DOS Control: use focus
    HEXPOS   1426.5,-501.3,81.0,-2.6,42.3,171.9                                       str     Hexapod position
    HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                                                  str     Hexapod trim values
    USEROTAT T                                                                        bool    DOS Control: use rotator
    ROTOFFST 167.1                                                                    float   [arcsec] Rotator offset
    ROTENBLD T                                                                        bool    Rotator enabled
    ROTRATE  0.0                                                                      float   [arcsec/min] Rotator rate
    RESETROT F                                                                        bool    DOS Control: reset hex rotator
    USEPOS   T                                                                        bool    Fiber positioner data available if true
    PETALS   PETAL0,PETAL1,PETAL2,PETAL3,PETAL4,PETAL5,PETAL6,PETAL7,PETAL8,PETAL9    str     Participating petals
    POSCYCLE 1                                                                        int     Number of current iteration
    POSONTGT 3626                                                                     int     Number of positioners on target
    POSONFRC 0.8613                                                                   float   Fraction of positioners on target
    POSDISAB 37                                                                       int     Number of disabled positioners
    POSENABL 4210                                                                     int     Number of enabled positioners
    POSRMS   0.0171                                                                   float   [micron] RMS of positioner accuracy
    POSITER  1                                                                        int     Positioning Control: max. number of pos. cycles
    POSFRACT 0.95                                                                     float
    POSTOLER 0.01                                                                     float   Positioning Control: in_position tolerance (mm)
    POSMVALL T                                                                        bool    Positioning Control: move all positioners
    USEGUIDR T                                                                        bool    DOS Control: use guider
    GUIDMODE catalog                                                                  str     Guider mode
    USEAOS   F                                                                        bool    DOS Control: AOS data available if true
    USEDONUT T                                                                        bool    DOS Control: use donuts
    USESPCTR T                                                                        bool    DOS Control: use spectrographs
    SPCGRPHS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                                  str     Participating spectrograph
    ILLSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                                  str     Participating illuminate s
    CCDSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                                  str     Participating ccd spectrog
    TDEWPNT  -16.043                                                                  float   Telescope air dew point
    TAIRFLOW 0.0                                                                      float   Telescope air flow
    TAIRITMP 11.8                                                                     float   [deg] Telescope air in temperature
    TAIROTMP 11.7                                                                     float   [deg] Telescope air out temperature
    TAIRTEMP 10.65                                                                    float   [deg] Telescope air temperature
    TCASITMP 0.0                                                                      float   [deg] Telescope Cass Cage in temperature
    TCASOTMP 10.8                                                                     float   [deg] Telescope Cass Cage out temperature
    TCSITEMP 9.3                                                                      float   [deg] Telescope center section in temperature
    TCSOTEMP 10.8                                                                     float   [deg] Telescope center section out temperature
    TCIBTEMP 0.0                                                                      float   [deg] Telescope chimney IB temperature
    TCIMTEMP 0.0                                                                      float   [deg] Telescope chimney IM temperature
    TCITTEMP 0.0                                                                      float   [deg] Telescope chimney IT temperature
    TCOSTEMP 0.0                                                                      float   [deg] Telescope chimney OS temperature
    TCOWTEMP 0.0                                                                      float   [deg] Telescope chimney OW temperature
    TDBTEMP  9.3                                                                      float   [deg] Telescope dec bore temperature
    TFLOWIN  0.0                                                                      float   Telescope flow rate in
    TFLOWOUT 0.0                                                                      float   Telescope flow rate out
    TGLYCOLI 9.9                                                                      float   [deg] Telescope glycol in temperature
    TGLYCOLO 9.8                                                                      float   [deg] Telescope glycol out temperature
    THINGES  11.4                                                                     float   [deg] Telescope hinge S temperature
    THINGEW  11.2                                                                     float   [deg] Telescope hinge W temperature
    TPMAVERT 8.931                                                                    float   [deg] Telescope mirror averagetemperature
    TPMDESIT 7.0                                                                      float   [deg] Telescope mirror desired temperature
    TPMEIBT  8.6                                                                      float   [deg] Telescope mirror EIB temperature
    TPMEITT  8.6                                                                      float   [deg] Telescope mirror EIT temperature
    TPMEOBT  8.5                                                                      float   [deg] Telescope mirror EOB temperature
    TPMEOTT  9.0                                                                      float   [deg] Telescope mirror EOT temperature
    TPMNIBT  8.4                                                                      float   [deg] Telescope mirror NIB temperature
    TPMNITT  8.9                                                                      float   [deg] Telescope mirror NIT temperature
    TPMNOBT  8.8                                                                      float   [deg] Telescope mirror NOB temperature
    TPMNOTT  9.1                                                                      float   [deg] Telescope mirror NOT temperature
    TPMRTDT  9.0                                                                      float   [deg] Telescope mirror RTD temperature
    TPMSIBT  8.6                                                                      float   [deg] Telescope mirror SIB temperature
    TPMSITT  8.8                                                                      float   [deg] Telescope mirror SIT temperature
    TPMSOBT  8.2                                                                      float   [deg] Telescope mirror SOB temperature
    TPMSOTT  8.9                                                                      float   [deg] Telescope mirror SOT temperature
    TPMSTAT  ready                                                                    str     Telescope mirror status
    TPMWIBT  8.2                                                                      float   [deg] Telescope mirror WIB temperature
    TPMWITT  9.1                                                                      float   [deg] Telescope mirror WIT temperature
    TPMWOBT  8.3                                                                      float   [deg] Telescope mirror WOB temperature
    TPMWOTT  8.9                                                                      float   [deg] Telescope mirror WOT temperature
    TPCITEMP 8.5                                                                      float   [deg] Telescope primary cell in temperature
    TPCOTEMP 8.6                                                                      float   [deg] Telescope primary cell out temperature
    TPR1HUM  0.0                                                                      float   Telescope probe 1 humidity
    TPR1TEMP 0.0                                                                      float   [deg] Telescope probe1 temperature
    TPR2HUM  0.0                                                                      float   Telescope probe 2 humidity
    TPR2TEMP 0.0                                                                      float   [deg] Telescope probe2 temperature
    TSERVO   40.0                                                                     float   Telescope servo setpoint
    TTRSTEMP 11.4                                                                     float   [deg] Telescope top ring S temperature
    TTRWTEMP 11.0                                                                     float   [deg] Telescope top ring W temperature
    TTRUETBT -4.2                                                                     float   [deg] Telescope truss ETB temperature
    TTRUETTT 11.2                                                                     float   [deg] Telescope truss ETT temperature
    TTRUNTBT 10.9                                                                     float   [deg] Telescope truss NTB temperature
    TTRUNTTT 11.2                                                                     float   [deg] Telescope truss NTT temperature
    TTRUSTBT 10.7                                                                     float   [deg] Telescope truss STB temperature
    TTRUSTST 10.8                                                                     float   [deg] Telescope truss STS temperature
    TTRUSTTT 11.1                                                                     float   [deg] Telescope truss STT temperature
    TTRUTSBT 11.8                                                                     float   [deg] Telescope truss TSB temperature
    TTRUTSMT 11.8                                                                     float   [deg] Telescope truss TSM temperature
    TTRUTSTT 11.8                                                                     float   [deg] Telescope truss TST temperature
    TTRUWTBT 10.5                                                                     float   [deg] Telescope truss WTB temperature
    TTRUWTTT 10.9                                                                     float   [deg] Telescope truss WTT temperature
    ALARM    F                                                                        bool    UPS major alarm or check battery
    ALARM-ON F                                                                        bool    UPS active alarm condition
    BATTERY  100.0                                                                    float   [%] UPS Battery left
    SECLEFT  5178.0                                                                   float   [s] UPS Seconds left
    UPSSTAT  System Normal - On Line(7)                                               str     UPS Status
    INAMPS   70.4                                                                     float   [A] UPS total input current
    OUTWATTS 5000.0,7200.0,4800.0                                                     str     [W] UPS Phase A, B, C output watts
    COMPDEW  -12.9                                                                    float   [deg C] Computer room dewpoint
    COMPHUM  7.4                                                                      float   [%] Computer room humidity
    COMPAMB  19.5                                                                     float   [deg C] Computer room ambient temperature
    COMPTEMP 24.5                                                                     float   [deg C] Computer room hygrometer temperature
    DEWPOINT 11.5                                                                     float   [deg C] (outside) dewpoint
    HUMIDITY 10.0                                                                     float   [%] (outside) humidity
    PRESSURE 795.0                                                                    float   [torr] (outside) air pressure
    OUTTEMP  0.0                                                                      float   [deg C] outside temperature
    WINDDIR  55.0                                                                     float   [deg] wind direction
    WINDSPD  27.3                                                                     float   [m/s] wind speed
    GUST     20.6                                                                     float   [m/s] Wind gusts speed
    AMNIENTN 13.5                                                                     float   [deg C] ambient temperature north
    CFLOOR   8.9                                                                      float   [deg C] temperature on C floor
    NWALLIN  13.9                                                                     float   [deg C] temperature at north wall inside
    NWALLOUT 9.6                                                                      float   [deg C] temperature at north wall outside
    WWALLIN  12.9                                                                     float   [deg C] temperature at west wall inside
    WWALLOUT 10.6                                                                     float   [deg C] temperature at west wall outside
    AMBIENTS 14.8                                                                     float   [deg C] ambient temperature south
    FLOOR    12.6                                                                     float   [deg C] temperature at floor (LCR)
    EWALLCMP 10.8                                                                     float   [deg C] temperature at east wall, computer room
    EWALLCOU 10.6                                                                     float   [deg C] temperature at east wall, Coude room
    ROOF     10.3                                                                     float   [deg C] temperature on roof
    ROOFAMB  10.6                                                                     float   [deg C] ambient temperature on roof
    DOMEBLOW 10.4                                                                     float   [deg C] temperature at dome back, lower
    DOMEBUP  10.7                                                                     float   [deg C] temperature at dome back, upper
    DOMELLOW 10.8                                                                     float   [deg C] temperature at dome left, lower
    DOMELUP  10.8                                                                     float   [deg C] temperature at dome left, upper
    DOMERLOW 10.6                                                                     float   [deg C] temperature at dome right, lower
    DOMERUP  10.5                                                                     float   [deg C] temperature at dome right, upper
    PLATFORM 10.4                                                                     float   [deg C] temperature at platform
    SHACKC   14.4                                                                     float   [deg C] temperature at shack ceiling
    SHACKW   13.7                                                                     float   [deg C] temperature at shack wall
    STAIRSL  10.5                                                                     float   [deg C] temperature at stairs, lower
    STAIRSM  10.4                                                                     float   [deg C] temperature at stairs, mid
    STAIRSU  10.6                                                                     float   [deg C] temperature at stairs, upper
    TELBASE  9.6                                                                      float   [deg C] temperature at telescope base
    UTILWALL 11.1                                                                     float   [deg C] temperature at utility room wall
    UTILROOM 10.9                                                                     float   [deg C] temperature in utilitiy room
    RADESYS  FK5                                                                      str     Coordinate reference frame of major/minor axes
    TNFSPROC 8.1963                                                                   float   [s] PlateMaker NFSPROC processing time
    TGFAPROC 7.9212                                                                   float   [s] PlateMaker GFAPROC processing time
    SIMGFAP  F                                                                        bool    DOS Control: simulate GFAPROC
    USEFVC   T                                                                        bool    DOS Control: use fvc
    USEFID   T                                                                        bool    DOS Control: use fiducials
    USEILLUM T                                                                        bool    DOS Control: use illuminator
    USEXSRVR T                                                                        bool    DOS Control: use exposure server
    USEOPENL T                                                                        bool    DOS Control: use open loop move
    STOPGUDR T                                                                        bool    DOS Control: stop guider
    STOPFOCS T                                                                        bool    DOS Control: stop focus
    STOPSKY  T                                                                        bool    DOS Control: stop sky monitor
    KEEPGUDR F                                                                        bool    DOS Control: keep guider running
    KEEPFOCS F                                                                        bool    DOS Control: keep focus running
    KEEPSKY  F                                                                        bool    DOS Control: keep sky mon. running
    REACQUIR F                                                                        bool    DOS Control: reacquire same files
    FILENAME /exposures/desi/20201220/00069022/desi-00069022.fits.fz                  str     Name of (F
    EXCLUDED                                                                          str     Components excluded from this exposure
    DOSVER   trunk                                                                    str     DOS software version
    OCSVER   1.2                                                                      float   OCS software version
    CONSTVER DESI:CURRENT                                                             str     Constants version
    INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini                         str     DOS Configuration
    REQTIME  300.0                                                                    float   [s] Requested exposure time
    FVCTIME  2.0                                                                      float   [s] FVC exposure time
    SIMGFACQ F                                                                        bool
    POSCNVGD F                                                                        bool
    GUIEXPID 69022                                                                    int     Guider exposure id at start of spectro exp.
    IGFRMNUM 12                                                                       int     Guider frame number at start of spectro exp.
    FOCEXPID 69022                                                                    int     Focus exposure id at start of spectro exp.
    IFFRMNUM 1                                                                        int     Focus frame number at start of spectro exp.
    SKYEXPID 69022                                                                    int     Sky exposure id at start of spectro exp.
    ISFRMNUM 1                                                                        int     Sky frame number at start of spectro exp.
    FGFRMNUM 46                                                                       int     Guider frame number at end of spectro exp.
    FFFRMNUM 6                                                                        int     Focus frame number at end of spectro exp.
    FSFRMNUM 5                                                                        int     Sky frame number at end of spectro exp.
    CHECKSUM IHcZL9cYIGcYI9cY                                                         str     HDU checksum updated 2022-02-14T05:35:59
    DATASUM  1766599107                                                               str     data unit checksum updated 2022-02-14T05:35:59
    FRAMES   47                                                                       int     Number of Frames in Archive
    DELTARA  None                                                                     Unknown [arcsec] Offset], right ascension, observer inp
    DELTADEC None                                                                     Unknown [arcsec] Offset], declination, observer input
    GSGUIDE0 (980.05,685.98),(878.97,731.68)                                          str
    GSGUIDE2 (372.65,939.43),(784.50,1529.96)                                         str
    GSGUIDE3 (365.22,1423.83),(249.12,411.52)                                         str
    GSGUIDE5 (848.52,78.26),(516.16,1410.54)                                          str
    GSGUIDE7 (540.95,1848.95),(504.68,831.62)                                         str
    GSGUIDE8 (720.29,552.69),(499.80,465.13)                                          str
    ARCHIVE  /exposures/desi/20201220/00069022/guide-00069022.fits.fz                 str
    GUIDEFIL guide-00069022.fits.fz                                                   str
    COORDFIL coordinates-00069022.fits                                                str
    ======== ======================================================================== ======= ===============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

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
BRICKNAME             char[8]
BRICKID               int32
BRICK_OBJID           int32
MORPHTYPE             char[4]
EBV                   float32
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
FIBERTOTFLUX_G        float32
FIBERTOTFLUX_R        float32
FIBERTOTFLUX_Z        float32
MASKBITS              int16
SERSIC                float32
SHAPE_R               float32
SHAPE_E1              float32
SHAPE_E2              float32
REF_ID                int64
REF_CAT               char[2]
GAIA_PHOT_G_MEAN_MAG  float32
GAIA_PHOT_BP_MEAN_MAG float32
GAIA_PHOT_RP_MEAN_MAG float32
PARALLAX              float32
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
===================== ======= ===== ===========

.. [1] Optional

Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
