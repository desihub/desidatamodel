==========
desi-EXPID
==========

:Summary: Raw data from the DESI spectrographs, with one fpack-compressed
    HDU per spectrograph camera
:Naming Convention: ``desi-EXPID.fits.fz``, where EXPID is the zero-padded
    8-digit exposure ID.
:Regex: ``desi-[0-9]{8}\.fits\.fz``
:File Type: FITS, 500 MB

Contents
========

There is one HDU per spectrograph camera with EXTNAMEs like
B0, B1, ... R0, R1, ... Z8, Z9.  The structure of each of these is
the same; only one is explicitly documented below.  These could appear
in any order and individual cameras could be missing from a data file
depending upon the state of the hardware and the ICS configuration.

================= ========= ================ ====================================
Number            EXTNAME   Type             Contents
================= ========= ================ ====================================
HDU00_                      IMAGE            Empty HDU
HDU01_            SPEC      Compressed IMAGE *Brief Description*
HDU02_            Z0        Compressed IMAGE Raw data from the Z0 spectrograph
`HDU03 -- HDU31`_ various   Compressed IMAGE Raw data similar to Z0 spectrograph.
HDU32_            SPECTCONS BINTABLE         Telemetry data
================= ========= ================ ====================================

FITS Header Units
=================

HDU00
-----

This HDU has no non-standard required keywords.

Empty HDU.

Early commissioning data and simulated data may have had ``EXTNAME = SPS`` as
well as header keywords that now appear in HDU01_.

HDU01
-----

EXTNAME = SPEC

*Description needed.*

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ===================================================================== ======= ===============================================
    KEY      Example Value                                                         Type    Comment
    ======== ===================================================================== ======= ===============================================
    NAXIS1   8                                                                     int     width of table in bytes
    NAXIS2   1                                                                     int     number of rows in table
    BZERO    32768                                                                 int     offset data range to that of unsigned short
    BSCALE   1                                                                     int     default scaling factor
    MODULE   CI                                                                    str     Image Sources/Component
    EXPID    118526                                                                int     Exposure number
    EXPFRAME 0                                                                     int     Frame number
    FRAMES   None                                                                  Unknown Number of Frames in Archive
    COSMSPLT T                                                                     bool    Cosmics split exposure if true
    MAXSPLIT 0                                                                     int     Number of allowed exposure splits
    VISITIDS 118524,118525,118526                                                  str     List of expids for a visit (same tile)
    TILEID   4403                                                                  int     DESI Tile ID
    FIBASSGN /data/tiles/SVN_tiles/004/fiberassign-004403.fits.gz                  str     Fiber assign
    FLAVOR   science                                                               str     Observation type
    OBSTYPE  SCIENCE                                                               str     Spectrograph observation type
    SEQUENCE _Split                                                                str     OCS Sequence name
    MANIFEST F                                                                     bool    DOS exposure manifest
    OBJECT                                                                         str     Object name
    PURPOSE  Main Survey                                                           str     Purpose of observing night
    PROGRAM  DARK                                                                  str     Program name
    NTSSURVY main                                                                  str     NTS survey name
    NTSPROG  DARK                                                                  str     NTS program name
    SBPROF   ELG                                                                   str     Profile used by ETC
    MAXTIME  5400.0                                                                float   [s] Maximum exposure time for entire visit (fro
    ESTTIME  3705.79                                                               float   [s] Estimated exposure time for visit (from ETC
    MINTIME  300.0                                                                 float   [s] Minimum exposure time (from NTS, used by ET
    MIDTIME  915.0                                                                 float   [s] Exposure midpoint time used by PlateMaker
    PROPID   2020B-5000                                                            str     Proposal ID
    OBSERVER Jessica Chellino, Corentin Ravoux                                     str     Names of observers
    LEAD     Martin Landriau                                                       str     Lead observer
    INSTRUME DESI                                                                  str     Instrument name
    OBSERVAT KPNO                                                                  str     Observatory name
    OBS-LAT  31.96403                                                              str     [deg] Observatory latitude
    OBS-LONG -111.59989                                                            str     [deg] Observatory east longitude
    OBS-ELEV 2097.0                                                                float   [m] Observatory elevation
    TELESCOP KPNO 4.0-m telescope                                                  str     Telescope name
    CORRCTOR DESI Corrector                                                        str     Corrector Identification
    SEQNUM   1                                                                     int     Number of exposure in sequence
    NIGHT    20220113                                                              int     Observing night
    SEQSTART 2022-01-14T11:03:08.447408                                            str     Start time of sequence processing
    TIMESYS  UTC                                                                   str     Time system used for date-obs
    DATE-OBS 2022-01-14T11:04:17.830044160                                         str     [UTC] Observation data and start tim
    TIME-OBS 2022-01-14T11:04:17.830044160                                         str     [UTC] Observation start time
    MJD-OBS  59593.461317476                                                       float   Modified Julian Date of observation
    STARTADJ 2022-01-14T11:03:22.140652                                            str     Time sequence starts adjusting the inst
    OPENSHUT 2022-01-14T11:04:18.577390                                            str     Time shutter opened
    CAMSHUT  open                                                                  str     Shutter status during observation
    ST       11:13:28.582000                                                       str     Local Sidereal time at observation start (HH:MM
    EXPTIME  579.1588                                                              float   [s] Actual exposure time
    DELTARA  0.                                                                    float   [arcsec] Offset], right ascension, observer inp
    DELTADEC 0.                                                                    float   [arcsec] Offset], declination, observer input
    ACQTIME  15.0                                                                  float   [s] acqusition image exposure time
    GUIDTIME 5.0                                                                   float   [s] guider GFA exposure time
    FOCSTIME 60.0                                                                  float   [s] focus GFA exposure time
    SKYTIME  60.0                                                                  float   [s] sky camera exposure time (acquisition)
    REQRA    170.239                                                               float   [deg] Requested right ascension (observer input
    REQDEC   -7.093                                                                float   [deg] Requested declination (observer input)
    WHITESPT F                                                                     bool    Telescope is at whitespot
    ZENITH   F                                                                     bool    Telescope is at zenith
    SEANNEX  F                                                                     bool    Telescope is at SE annex
    BEYONDP  F                                                                     bool    Telescope is beyond pole
    FIDUCIAL off                                                                   str     Fiducials status during observation
    BACKLIT  off                                                                   str     Fibers are backlit if True
    AIRMASS  1.287912                                                              float   Airmass
    FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                                    str     Telescope focus settings
    VCCD     ON                                                                    str     True (ON) if CCD voltage is on
    TRUSTEMP 12.267                                                                float   [deg] Average Telescope truss temperature (only
    PMIRTEMP 11.675                                                                float   [deg] Average primary mirror temperature (nit,e
    PMREADY  T                                                                     bool    Primary mirror ready
    PMCOVER  open                                                                  str     Primary mirror cover
    PMCOOL   off                                                                   str     Primary mirror cooling
    DOMSHUTU open                                                                  str     Upper dome shutter
    DOMSHUTL open                                                                  str     Lower dome shutter
    DOMLIGHH off                                                                   str     High dome lights
    DOMLIGHL off                                                                   str     Low dome lights
    DOMEAZ   180.062                                                               float   [deg] Dome azimuth angle
    DOMINPOS T                                                                     bool    Dome is in position
    EPOCH    2000.0                                                                float   Epoch of observation
    GUIDOFFR -0.659376                                                             float   [arcsec] Cummulative guider offset (RA)
    GUIDOFFD 0.003783                                                              float   [arcsec] Cummulative guider offset (dec)
    SUNRA    296.151203                                                            float   [deg] Sun RA at start of exposure
    SUNDEC   -21.264137                                                            float   [deg] Sun declination at start of exposure
    MOONDEC  23.960888                                                             float   [deg] Moon declination at start of exposure
    MOONRA   73.944051                                                             float   [deg] Moon RA at start of exposure
    MOONSEP  99.032                                                                float   [deg] Moon Separation
    MOUNTAZ  176.725567                                                            float   [deg] Mount azimuth angle
    MOUNTDEC -7.102329                                                             float   [deg] Mount declination
    MOUNTEL  50.883914                                                             float   [deg] Mount elevation angle
    MOUNTHA  -2.081118                                                             float   [deg] Mount hour angle
    INCTRL   T                                                                     bool    DESI in control
    INPOS    T                                                                     bool    Mount in position
    MNTOFFD  75.86                                                                 float   [arcsec] Mount offset (dec)
    MNTOFFR  -31.1                                                                 float   [arcsec] Mount offset (RA)
    PARALLAC -2.510103                                                             float   [deg] Parallactic angle
    SKYDEC   -7.102329                                                             float   [deg] Telescope declination (pointing on sky)
    SKYRA    170.24163                                                             float   [deg] Telescope right ascension (pointing on sk
    TARGTDEC -7.102329                                                             float   [deg] Target declination (to TCS)
    TARGTRA  170.24163                                                             float   [deg] Target right ascension (to TCS)
    TARGTAZ  177.063681                                                            float   [deg] Target azimuth
    TARGTEL  50.893802                                                             float   [deg] Target elevation
    TRGTOFFD 0.0                                                                   float   [arcsec] Telescope target offset (dec)
    TRGTOFFR 0.0                                                                   float   [arcsec] Telescope target offset (RA)
    ZD       39.106198                                                             float   [deg] Telescope zenith distance
    TILERA   170.239                                                               float   RA of tile given in fiberassign file
    TILEDEC  -7.093                                                                float   DEC of tile given in fiberassign file
    TCSST    11:13:30.164                                                          str     Local Sidereal time reported by TCS (HH:MM:SS)
    TCSMJD   59593.461771                                                          float   MJD reported by TCS
    USETURB  T                                                                     bool    Turbulence corrections are applied if true
    USEETC   T                                                                     bool    ETC data available if true
    REQTEFF  1000.0                                                                float   [s] Requested effective exposure time
    ACTTEFF  1.113899                                                              float   [s] Actual effective exposure time
    TOTTEFF  936.3194                                                              float   [s] Total effective exposure time for visit
    SEEING   None                                                                  Unknown [arcsec] ETC/PM seeing
    TRANSPAR None                                                                  Unknown ETC/PM transparency
    SKYLEVEL 7.516                                                                 float   [unit?] PM/ETC sky level
    PMSEEING None                                                                  Unknown [arcsec] PlateMaker GFAPROC seeing
    PMTRANSP None                                                                  Unknown [%] PlateMaker GFAPROC transparency
    ETCSEENG 1.1695                                                                float   [arcsec] ETC seeing
    ETCTEFF  1.113899                                                              float   [s] ETC effective exposure time
    ETCREAL  580.104492                                                            float   [s] ETC real open shutter time
    ETCPREV  454.940948                                                            float   [s] ETC cummulative t_eff for visit
    ETCSPLIT 3                                                                     int     ETC split sequence number for this visit
    ETCPROF  ELG                                                                   str     ETC source brightness profile
    ETCTRANS 0.10543                                                               float   ETC avg. TRANSP normalized to 1
    ETCTHRUP 0.10793                                                               float   ETC avg. thruput (PSF profile)
    ETCTHRUE 0.10457                                                               float   ETC avg. thruput (ELG profile)
    ETCTHRUB 0.101061                                                              float   ETC avg. thruput (BGS profile)
    ETCFRACP 0.575305                                                              float   ETC transp. weighted avg. FFRAC (PSF)
    ETCFRACE 0.408837                                                              float   ETC transp. weighted avg. FFRAC (ELG)
    ETCFRACB 0.181983                                                              float   ETC transp. weighted avg. FFRAC (BGS)
    ETCSKY   6.882767                                                              float   ETC averaged, normalized sky camera flux
    ACQFWHM  1.169528                                                              float   [arcsec] FWHM of guide star PSF in acq. image
    ACQCAM   GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                             str     Acquisition cameras used
    GUIDECAM GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                             str     Guide cameras used for t
    FOCUSCAM FOCUS1,FOCUS4,FOCUS6,FOCUS9                                           str     Focus cameras used for this exposure
    SKYCAM   SKYCAM0,SKYCAM1                                                       str     Sky cameras used for this exposure
    REQADC   334.05,26.06                                                          str     [deg] requested ADC angles
    ADCCORR  T                                                                     bool    Correct pointing for ADC setting if True
    ADC1PHI  334.049995                                                            float   [deg] ADC 1 angle
    ADC2PHI  26.058728                                                             float   [deg] ADC 2 angle
    ADC1HOME F                                                                     bool    ADC 1 at home position if True
    ADC2HOME F                                                                     bool    ADC 2 at home position if True
    ADC1NREV -1.0                                                                  float   ADC 1 number of revs
    ADC2NREV 1.0                                                                   float   ADC 2 number of revs
    ADC1STAT STOPPED                                                               str     ADC 1 status
    ADC2STAT STOPPED                                                               str     ADC 2 status
    USESKY   T                                                                     bool    DOS Control: use Sky Monitor
    USEFOCUS T                                                                     bool    DOS Control: use focus
    HEXPOS   946.7,-231.6,-83.4,-18.3,9.9,138.8                                    str     Hexapod position
    HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                                               str     Hexapod trim values
    USEROTAT T                                                                     bool    DOS Control: use rotator
    ROTOFFST 138.8                                                                 float   [arcsec] Rotator offset
    ROTENBLD T                                                                     bool    Rotator enabled
    ROTRATE  0.513                                                                 float   [arcsec/min] Rotator rate
    RESETROT F                                                                     bool    DOS Control: reset hex rotator
    SPLITEXP T                                                                     bool    Split exposure part of a visit
    USESPLIT T                                                                     bool    Exposure splits are allowed
    USEPOS   T                                                                     bool    Fiber positioner data available if true
    PETALS   PETAL0,PETAL1,PETAL2,PETAL3,PETAL4,PETAL5,PETAL6,PETAL7,PETAL8,PETAL9 str     Participating petals
    POSCYCLE None                                                                  Unknown Number of current iteration
    POSONTGT None                                                                  Unknown Number of positioners on target
    POSONFRC None                                                                  Unknown Fraction of positioners on target
    POSDISAB None                                                                  Unknown Number of disabled positioners
    POSENABL None                                                                  Unknown Number of enabled positioners
    POSRMS   None                                                                  Unknown [mm] RMS of positioner accuracy
    POSITER  1                                                                     int     Positioning Control: max. number of pos. cycles
    POSFRACT 0.95                                                                  float
    POSTOLER 0.005                                                                 float   Positioning Control: in_position tolerance (mm)
    POSMVALL T                                                                     bool    Positioning Control: move all positioners
    USEGUIDR T                                                                     bool    DOS Control: use guider
    GUIDMODE catalog                                                               str     Guider mode
    USEAOS   T                                                                     bool    DOS Control: AOS data available if true
    USEDONUT T                                                                     bool    DOS Control: use donuts
    USESPCTR T                                                                     bool    DOS Control: use spectrographs
    SPCGRPHS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                               str     Participating spectrograph
    ILLSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                               str     Participating illuminate s
    CCDSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                               str     Participating ccd spectrog
    TDEWPNT  -32.86                                                                float   Telescope air dew point
    TAIRFLOW 0.0                                                                   float   Telescope air flow
    TAIRITMP 12.5                                                                  float   [deg] Telescope air in temperature
    TAIROTMP 12.7                                                                  float   [deg] Telescope air out temperature
    TAIRTEMP 11.05                                                                 float   [deg] Telescope air temperature
    TCASITMP 6.6                                                                   float   [deg] Telescope Cass Cage in temperature
    TCASOTMP 12.2                                                                  float   [deg] Telescope Cass Cage out temperature
    TCSITEMP 12.1                                                                  float   [deg] Telescope center section in temperature
    TCSOTEMP 12.3                                                                  float   [deg] Telescope center section out temperature
    TCIBTEMP 0.0                                                                   float   [deg] Telescope chimney IB temperature
    TCIMTEMP 0.0                                                                   float   [deg] Telescope chimney IM temperature
    TCITTEMP 0.0                                                                   float   [deg] Telescope chimney IT temperature
    TCOSTEMP 0.0                                                                   float   [deg] Telescope chimney OS temperature
    TCOWTEMP 0.0                                                                   float   [deg] Telescope chimney OW temperature
    TDBTEMP  12.4                                                                  float   [deg] Telescope dec bore temperature
    TFLOWIN  0.0                                                                   float   Telescope flow rate in
    TFLOWOUT 0.0                                                                   float   Telescope flow rate out
    TGLYCOLI 12.8                                                                  float   [deg] Telescope glycol in temperature
    TGLYCOLO 12.6                                                                  float   [deg] Telescope glycol out temperature
    THINGES  12.1                                                                  float   [deg] Telescope hinge S temperature
    THINGEW  22.3                                                                  float   [deg] Telescope hinge W temperature
    TPMAVERT 11.658                                                                float   [deg] Telescope mirror averagetemperature
    TPMDESIT 6.0                                                                   float   [deg] Telescope mirror desired temperature
    TPMEIBT  12.1                                                                  float   [deg] Telescope mirror EIB temperature
    TPMEITT  11.5                                                                  float   [deg] Telescope mirror EIT temperature
    TPMEOBT  12.3                                                                  float   [deg] Telescope mirror EOB temperature
    TPMEOTT  12.0                                                                  float   [deg] Telescope mirror EOT temperature
    TPMNIBT  11.9                                                                  float   [deg] Telescope mirror NIB temperature
    TPMNITT  11.4                                                                  float   [deg] Telescope mirror NIT temperature
    TPMNOBT  12.3                                                                  float   [deg] Telescope mirror NOB temperature
    TPMNOTT  12.0                                                                  float   [deg] Telescope mirror NOT temperature
    TPMRTDT  11.67                                                                 float   [deg] Telescope mirror RTD temperature
    TPMSIBT  12.1                                                                  float   [deg] Telescope mirror SIB temperature
    TPMSITT  11.5                                                                  float   [deg] Telescope mirror SIT temperature
    TPMSOBT  12.0                                                                  float   [deg] Telescope mirror SOB temperature
    TPMSOTT  11.7                                                                  float   [deg] Telescope mirror SOT temperature
    TPMSTAT  ready                                                                 str     Telescope mirror status
    TPMWIBT  11.9                                                                  float   [deg] Telescope mirror WIB temperature
    TPMWITT  11.3                                                                  float   [deg] Telescope mirror WIT temperature
    TPMWOBT  11.9                                                                  float   [deg] Telescope mirror WOB temperature
    TPMWOTT  11.8                                                                  float   [deg] Telescope mirror WOT temperature
    TPCITEMP 12.1                                                                  float   [deg] Telescope primary cell in temperature
    TPCOTEMP 12.0                                                                  float   [deg] Telescope primary cell out temperature
    TPR1HUM  0.0                                                                   float   Telescope probe 1 humidity
    TPR1TEMP 0.0                                                                   float   [deg] Telescope probe1 temperature
    TPR2HUM  0.0                                                                   float   Telescope probe 2 humidity
    TPR2TEMP 0.0                                                                   float   [deg] Telescope probe2 temperature
    TSERVO   40.0                                                                  float   Telescope servo setpoint
    TTRSTEMP 11.9                                                                  float   [deg] Telescope top ring S temperature
    TTRWTEMP 11.7                                                                  float   [deg] Telescope top ring W temperature
    TTRUETBT -1.5                                                                  float   [deg] Telescope truss ETB temperature
    TTRUETTT 11.6                                                                  float   [deg] Telescope truss ETT temperature
    TTRUNTBT 11.7                                                                  float   [deg] Telescope truss NTB temperature
    TTRUNTTT 11.6                                                                  float   [deg] Telescope truss NTT temperature
    TTRUSTBT 11.7                                                                  float   [deg] Telescope truss STB temperature
    TTRUSTST 10.8                                                                  float   [deg] Telescope truss STS temperature
    TTRUSTTT 11.7                                                                  float   [deg] Telescope truss STT temperature
    TTRUTSBT 12.2                                                                  float   [deg] Telescope truss TSB temperature
    TTRUTSMT 12.2                                                                  float   [deg] Telescope truss TSM temperature
    TTRUTSTT 12.2                                                                  float   [deg] Telescope truss TST temperature
    TTRUWTBT 11.6                                                                  float   [deg] Telescope truss WTB temperature
    TTRUWTTT 11.6                                                                  float   [deg] Telescope truss WTT temperature
    ALARM    F                                                                     bool    UPS major alarm or check battery
    ALARM-ON F                                                                     bool    UPS active alarm condition
    BATTERY  100.0                                                                 float   [%] UPS Battery left
    SECLEFT  6312.0                                                                float   [s] UPS Seconds left
    UPSSTAT  System Normal - On Line(7)                                            str     UPS Status
    INAMPS   68.3                                                                  float   [A] UPS total input current
    OUTWATTS 4800.0,7200.0,4500.0                                                  str     [W] UPS Phase A, B, C output watts
    COMPDEW  -10.3                                                                 float   [deg C] Computer room dewpoint
    COMPHUM  13.9                                                                  float   [%] Computer room humidity
    COMPAMB  25.2                                                                  float   [deg C] Computer room ambient temperature
    COMPTEMP 17.6                                                                  float   [deg C] Computer room hygrometer temperature
    DEWPOINT -36.9                                                                 float   [deg C] (outside) dewpoint
    HUMIDITY 2.0                                                                   float   [%] (outside) humidity
    PRESSURE 793.2                                                                 float   [torr] (outside) air pressure
    OUTTEMP  11.0                                                                  float   [deg C] outside temperature
    WINDDIR  264.5                                                                 float   [deg] wind direction
    WINDSPD  11.7                                                                  float   [m/s] wind speed
    GUST     10.8                                                                  float   [m/s] Wind gusts speed
    AMNIENTN 16.8                                                                  float   [deg C] ambient temperature north
    CFLOOR   11.6                                                                  float   [deg C] temperature on C floor
    NWALLIN  17.3                                                                  float   [deg C] temperature at north wall inside
    NWALLOUT 11.1                                                                  float   [deg C] temperature at north wall outside
    WWALLIN  16.5                                                                  float   [deg C] temperature at west wall inside
    WWALLOUT 11.5                                                                  float   [deg C] temperature at west wall outside
    AMBIENTS 17.6                                                                  float   [deg C] ambient temperature south
    FLOOR    15.7                                                                  float   [deg C] temperature at floor (LCR)
    EWALLCMP 11.9                                                                  float   [deg C] temperature at east wall, computer room
    EWALLCOU 11.6                                                                  float   [deg C] temperature at east wall, Coude room
    ROOF     10.9                                                                  float   [deg C] temperature on roof
    ROOFAMB  11.1                                                                  float   [deg C] ambient temperature on roof
    DOMEBLOW 11.2                                                                  float   [deg C] temperature at dome back, lower
    DOMEBUP  11.3                                                                  float   [deg C] temperature at dome back, upper
    DOMELLOW 11.1                                                                  float   [deg C] temperature at dome left, lower
    DOMELUP  10.9                                                                  float   [deg C] temperature at dome left, upper
    DOMERLOW 11.1                                                                  float   [deg C] temperature at dome right, lower
    DOMERUP  10.7                                                                  float   [deg C] temperature at dome right, upper
    PLATFORM 10.6                                                                  float   [deg C] temperature at platform
    SHACKC   16.7                                                                  float   [deg C] temperature at shack ceiling
    SHACKW   16.6                                                                  float   [deg C] temperature at shack wall
    STAIRSL  10.9                                                                  float   [deg C] temperature at stairs, lower
    STAIRSM  10.7                                                                  float   [deg C] temperature at stairs, mid
    STAIRSU  10.9                                                                  float   [deg C] temperature at stairs, upper
    TELBASE  11.6                                                                  float   [deg C] temperature at telescope base
    UTILWALL 11.4                                                                  float   [deg C] temperature at utility room wall
    UTILROOM 10.1                                                                  float   [deg C] temperature in utilitiy room
    SP0NIRT  139.96                                                                float   [K] SP0 NIR temperature
    SP0REDT  139.99                                                                float   [K] SP0 red temperature
    SP0BLUT  163.02                                                                float   [K] SP0 blue temperature
    SP0NIRP  7.36e-08                                                              float   [mb] SP0 NIR pressure
    SP0REDP  5.492e-08                                                             float   [mb] SP0 red pressure
    SP0BLUP  1.001e-07                                                             float   [mb] SP0 blue pressure
    SP1NIRT  139.96                                                                float   [K] SP1 NIR temperature
    SP1REDT  139.96                                                                float   [K] SP1 red temperature
    SP1BLUT  163.02                                                                float   [K] SP1 blue temperature
    SP1NIRP  6.622e-08                                                             float   [mb] SP1 NIR pressure
    SP1REDP  6.033e-08                                                             float   [mb] SP1 red pressure
    SP1BLUP  8.599e-08                                                             float   [mb] SP1 blue pressure
    SP2NIRT  139.96                                                                float   [K] SP2 NIR temperature
    SP2REDT  139.96                                                                float   [K] SP2 red temperature
    SP2BLUT  163.02                                                                float   [K] SP2 blue temperature
    SP2NIRP  5.556e-08                                                             float   [mb] SP2 NIR pressure
    SP2REDP  6.013e-08                                                             float   [mb] SP2 red pressure
    SP2BLUP  8.897e-08                                                             float   [mb] SP2 blue pressure
    SP3NIRT  140.03                                                                float   [K] SP3 NIR temperature
    SP3REDT  139.96                                                                float   [K] SP3 red temperature
    SP3BLUT  163.04                                                                float   [K] SP3 blue temperature
    SP3NIRP  4.3e-08                                                               float   [mb] SP3 NIR pressure
    SP3REDP  7.066e-08                                                             float   [mb] SP3 red pressure
    SP3BLUP  8.324e-08                                                             float   [mb] SP3 blue pressure
    SP4NIRT  139.96                                                                float   [K] SP4 NIR temperature
    SP4REDT  139.99                                                                float   [K] SP4 red temperature
    SP4BLUT  163.04                                                                float   [K] SP4 blue temperature
    SP4NIRP  6.921e-08                                                             float   [mb] SP4 NIR pressure
    SP4REDP  4.505e-08                                                             float   [mb] SP4 red pressure
    SP4BLUP  6.846e-08                                                             float   [mb] SP4 blue pressure
    SP5NIRT  139.99                                                                float   [K] SP5 NIR temperature
    SP5REDT  139.99                                                                float   [K] SP5 red temperature
    SP5BLUT  163.02                                                                float   [K] SP5 blue temperature
    SP5NIRP  7.886e-08                                                             float   [mb] SP5 NIR pressure
    SP5REDP  4.383e-08                                                             float   [mb] SP5 red pressure
    SP5BLUP  1.003e-07                                                             float   [mb] SP5 blue pressure
    SP6NIRT  139.96                                                                float   [K] SP6 NIR temperature
    SP6REDT  139.96                                                                float   [K] SP6 red temperature
    SP6BLUT  163.04                                                                float   [K] SP6 blue temperature
    SP6NIRP  2.688e-07                                                             float   [mb] SP6 NIR pressure
    SP6REDP  6.65e-08                                                              float   [mb] SP6 red pressure
    SP6BLUP  9.062e-08                                                             float   [mb] SP6 blue pressure
    SP7NIRT  139.96                                                                float   [K] SP7 NIR temperature
    SP7REDT  140.03                                                                float   [K] SP7 red temperature
    SP7BLUT  162.97                                                                float   [K] SP7 blue temperature
    SP7NIRP  6.073e-08                                                             float   [mb] SP7 NIR pressure
    SP7REDP  4.807e-08                                                             float   [mb] SP7 red pressure
    SP7BLUP  1.066e-07                                                             float   [mb] SP7 blue pressure
    SP8NIRT  139.96                                                                float   [K] SP8 NIR temperature
    SP8REDT  139.96                                                                float   [K] SP8 red temperature
    SP8BLUT  163.04                                                                float   [K] SP8 blue temperature
    SP8NIRP  1.257e-07                                                             float   [mb] SP8 NIR pressure
    SP8REDP  4.635e-08                                                             float   [mb] SP8 red pressure
    SP8BLUP  8.912e-08                                                             float   [mb] SP8 blue pressure
    SP9NIRT  139.96                                                                float   [K] SP9 NIR temperature
    SP9REDT  139.96                                                                float   [K] SP9 red temperature
    SP9BLUT  163.02                                                                float   [K] SP9 blue temperature
    SP9NIRP  5.325e-08                                                             float   [mb] SP9 NIR pressure
    SP9REDP  6.124e-08                                                             float   [mb] SP9 red pressure
    SP9BLUP  1.236e-07                                                             float   [mb] SP9 blue pressure
    RADESYS  FK5                                                                   str     Coordinate reference frame of major/minor axes
    SIMGFAP  F                                                                     bool    DOS Control: simulate GFAPROC
    USEFVC   T                                                                     bool    DOS Control: use fvc
    USEFID   T                                                                     bool    DOS Control: use fiducials
    USEILLUM T                                                                     bool    DOS Control: use illuminator
    USEXSRVR T                                                                     bool    DOS Control: use exposure server
    USEOPENL T                                                                     bool    DOS Control: use open loop move
    USEMIDPT T                                                                     bool    Use exposure midpoint if true
    STOPGUDR T                                                                     bool    DOS Control: stop guider
    STOPFOCS T                                                                     bool    DOS Control: stop focus
    STOPSKY  T                                                                     bool    DOS Control: stop sky monitor
    KEEPGUDR F                                                                     bool    DOS Control: keep guider running
    KEEPFOCS F                                                                     bool    DOS Control: keep focus running
    KEEPSKY  F                                                                     bool    DOS Control: keep sky mon. running
    REACQUIR F                                                                     bool    DOS Control: reacquire same files
    FILENAME /exposures/desi/20220113/00118526/desi-00118526.fits.fz               str     Name of (F
    EXCLUDED                                                                       str     Components excluded from this exposure
    DOSVER   trunk                                                                 str     DOS software version
    OCSVER   1.2                                                                   float   OCS software version
    PMVER    desi-138368                                                           str     PlateMaker/Dervish version
    ETCVERS  0.1.14                                                                str     ETC version
    CONSTVER DESI:CURRENT                                                          str     Constants version
    INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini                      str     DOS Configuration
    REQTIME  1860.0                                                                float   [s] Requested exposure time
    SIMGFACQ F                                                                     bool
    TCSKRA   0.01 0.04 0.01                                                        str     TCS Kalman (RA)
    TCSKDEC  0.01 0.04 0.01                                                        str     TCS Kalman (dec)
    TCSGRA   0.15                                                                  float   TCS simple gain (RA)
    TCSGDEC  0.15                                                                  float   TCS simple gain (dec)
    TCSMFRA  2                                                                     int     TCS moving filter length (RA)
    TCSMFDEC 2                                                                     int     TCS moving filter length (dec)
    TCSPIRA  0.9,0.0,0.0,0.0                                                       str     TCS PI settings (P, I (gain, error window, satu
    TCSPIDEC 0.9,0.0,0.0,0.0                                                       str     TCS PI settings (P, I (gain, error window, satu
    GUIEXPID 118526                                                                int     Guider exposure id at start of spectro exp.
    IGFRMNUM 2                                                                     int     Guider frame number at start of spectro exp.
    FOCEXPID 118526                                                                int     Focus exposure id at start of spectro exp.
    IFFRMNUM 0                                                                     int     Focus frame number at start of spectro exp.
    SKYEXPID 118526                                                                int     Sky exposure id at start of spectro exp.
    ISFRMNUM 0                                                                     int     Sky frame number at start of spectro exp.
    FGFRMNUM 72                                                                    int     Guider frame number at end of spectro exp.
    FFFRMNUM 9                                                                     int     Focus frame number at end of spectro exp.
    FSFRMNUM 7                                                                     int     Sky frame number at end of spectro exp.
    ETCSKYLV 7.8081                                                                float   [unit?] ETC skylevel
    CHECKSUM OlYZPlXZOlXZOlXZ                                                      str     HDU checksum updated 2022-01-14T11:15:03
    DATASUM  306780459                                                             str     data unit checksum updated 2022-01-14T11:15:03
    ======== ===================================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 10]

HDU02
-----

EXTNAME = Z0

Unprocessed spectrograph raw data, including overscans, from camera Z0.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ============= ==================================================== ======= ===============================================
    KEY           Example Value                                        Type    Comment
    ============= ==================================================== ======= ===============================================
    NAXIS1        8                                                    int     width of table in bytes
    NAXIS2        4194                                                 int     number of rows in table
    BZERO         32768                                                int     offset data range to that of unsigned short
    BSCALE        1                                                    int     default scaling factor
    EXPID         118526                                               int     Exposure number
    EXPFRAME      0                                                    int     Frame number
    FRAMES [1]_   None                                                 Unknown Number of Frames in Archive
    TILEID        4403                                                 int     DESI Tile ID
    FIBASSGN [1]_ /data/tiles/SVN_tiles/004/fiberassign-004403.fits.gz str     Fiber assign
    FLAVOR        science                                              str     Observation type
    SEQUENCE      _Split                                               str     OCS Sequence name
    PURPOSE       Main Survey                                          str     Purpose of observing night
    PROGRAM       DARK                                                 str     Program name
    PROPID        2020B-5000                                           str     Proposal ID
    OBSERVER      Jessica Chellino, Corentin Ravoux                    str     Names of observers
    LEAD          Martin Landriau                                      str     Lead observer
    INSTRUME      DESI                                                 str     Instrument name
    OBSERVAT      KPNO                                                 str     Observatory name
    OBS-LAT       31.96403                                             str     [deg] Observatory latitude
    OBS-LONG      -111.59989                                           str     [deg] Observatory east longitude
    OBS-ELEV      2097.0                                               float   [m] Observatory elevation
    TELESCOP      KPNO 4.0-m telescope                                 str     Telescope name
    CORRCTOR      DESI Corrector                                       str     Corrector Identification
    NIGHT         20220113                                             int     Observing night
    TIMESYS       UTC                                                  str     Time system used for date-obs
    DATE-OBS      2022-01-14T11:04:17.790636032                        str     [UTC] Observation data and start tim
    TIME-OBS      2022-01-14T11:04:17.790636032                        str     [UTC] Observation start time
    MJD-OBS       59593.46131702                                       float   Modified Julian Date of observation
    OPENSHUT      2022-01-14T11:04:18.577390                           str     Time shutter opened
    ST            11:13:28.540000                                      str     Local Sidereal time at observation start (HH:MM
    EXPTIME       579.193                                              float   [s] Actual exposure time
    DELTARA       0.                                                   float   [arcsec] Offset], right ascension, observer inp
    DELTADEC      0.                                                   float   [arcsec] Offset], declination, observer input
    REQRA [1]_    170.239                                              float   [deg] Requested right ascension (observer input
    REQDEC [1]_   -7.093                                               float   [deg] Requested declination (observer input)
    FOCUS [1]_    946.6,-231.6,-83.4,-18.3,9.8,139.4                   str     Telescope focus settings
    VCCD          ON                                                   str     True (ON) if CCD voltage is on
    VCCDON        2022-01-10T20:55:43.758808                           str     Time when CCD voltage was turned on
    VCCDSEC       310751.8                                             float   [s] CCD on time in seconds
    TRUSTEMP [1]_ 12.267                                               float   [deg] Average Telescope truss temperature (only
    PMIRTEMP [1]_ 11.675                                               float   [deg] Average primary mirror temperature (nit,e
    EPOCH         2000.0                                               float   Epoch of observation
    MOUNTAZ [1]_  176.725567                                           float   [deg] Mount azimuth angle
    MOUNTDEC [1]_ -7.102329                                            float   [deg] Mount declination
    MOUNTEL [1]_  50.883914                                            float   [deg] Mount elevation angle
    MOUNTHA [1]_  -2.081118                                            float   [deg] Mount hour angle
    SKYDEC [1]_   -7.102329                                            float   [deg] Telescope declination (pointing on sky)
    SKYRA [1]_    170.24163                                            float   [deg] Telescope right ascension (pointing on sk
    TARGTDEC [1]_ -7.102329                                            float   [deg] Target declination (to TCS)
    TARGTRA [1]_  170.24163                                            float   [deg] Target right ascension (to TCS)
    USEETC [1]_   T                                                    bool    ETC data available if true
    USESKY [1]_   T                                                    bool    DOS Control: use Sky Monitor
    USEFOCUS [1]_ T                                                    bool    DOS Control: use focus
    HEXTRIM [1]_  0.0,0.0,0.0,0.0,0.0,0.0                              str     Hexapod trim values
    USEROTAT [1]_ T                                                    bool    DOS Control: use rotator
    ROTOFFST [1]_ 138.8                                                float   [arcsec] Rotator offset
    ROTENBLD [1]_ T                                                    bool    Rotator enabled
    ROTRATE [1]_  0.513                                                float   [arcsec/min] Rotator rate
    USEGUIDR [1]_ T                                                    bool    DOS Control: use guider
    USEDONUT [1]_ T                                                    bool    DOS Control: use donuts
    SPECGRPH      0                                                    int     Spectrograph logical name (SP)
    SPECID        4                                                    int     Spectrograph serial number (SM)
    FEEBOX        lbnl082                                              str     CCD Controller serial number
    VESSEL        17                                                   int     Cryostat serial number
    FEEVER        v20160312                                            str     CCD Controller version
    DETFLVER      FAILED: invalid argument for get command             str     CCD Controller detector f
    FEEPOWER      ON                                                   str     FEE power status
    FEEDMASK      2134851391                                           int     FEE dac mask
    FEECMASK      1048575                                              int     FEE clk mask
    CCDTEMP       -137.5647                                            float   [deg C] CCD controller CCD temperature
    RADESYS       FK5                                                  str     Coordinate reference frame of major/minor axes
    DOSVER        trunk                                                str     DOS software version
    OCSVER        1.2                                                  float   OCS software version
    CONSTVER      DESI:CURRENT                                         str     Constants version
    INIFILE       /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
    CAMERA        z0                                                   str     Camera name
    DAC2          -9.0002,-8.8271                                      str     [V] set value, measured value
    DATASECA      [8:2064, 2:2065]                                     str     Data section for quadrant A
    CLOCK6        9.9999,0.0                                           str     [V] high rail, low rail
    DIGITIME      56.4524                                              float   [s] Time to digitize image
    DAC17         20.0008,11.834                                       str     [V] set value, measured value
    CLOCK15       9.9992,2.9993                                        str     [V] high rail, low rail
    DETSECB       [2058:4114, 1:2064]                                  str     Detector section for quadrant B
    CLOCK0        9.9999,0.0                                           str     [V] high rail, low rail
    CRYOPRES      7.360e-08                                            str     [mb] Cryostat pressure (IP)
    AMPSECC       [1:2057, 4128:2065]                                  str     AMP section for quadrant C
    CCDTMING      flatdark_lbnl_timing.txt                             str     CCD timing file
    CLOCK8        9.9992,2.9993                                        str     [V] high rail, low rail
    CLOCK4        9.9999,0.0                                           str     [V] high rail, low rail
    PRESECB       [4250:4256, 2:2065]                                  str     Prescan section for quadrant B
    DAC1          -9.0002,-8.8683                                      str     [V] set value, measured value
    PRRSECC       [8:2064, 4194:4194]                                  str     Row prescan section for quadrant C
    DAC10         -25.0003,-24.7976                                    str     [V] set value, measured value
    OFFSET2       0.4000000059604645,-8.8271                           str     [V] set value, measured value
    CLOCK14       9.9992,2.9993                                        str     [V] high rail, low rail
    DAC16         39.9961,39.039                                       str     [V] set value, measured value
    ORSECB        [2193:4249, 2066:2097]                               str     Row overscan section for quadrant B
    AMPSECA       [1:2057, 1:2064]                                     str     AMP section for quadrant A
    DAC14         0.0,0.1039                                           str     [V] set value, measured value
    DAC11         -25.0003,-24.0556                                    str     [V] set value, measured value
    CLOCK7        -2.0001,3.9999                                       str     [V] high rail, low rail
    PGAGAIN       3                                                    int     Controller gain
    ORSECA        [8:2064, 2066:2097]                                  str     Row overscan section for quadrant A
    DAC15         0.0,0.089                                            str     [V] set value, measured value
    DETSECD       [2058:4114, 2065:4128]                               str     Detector section for quadrant D
    ORSECD        [2193:4249, 2098:2129]                               str     Row bias section for quadrant D
    OFFSET0       0.4000000059604645,-8.7962                           str     [V] set value, measured value
    OFFSET6       2.0,6.0911                                           str     [V] set value, measured value
    PRRSECD       [2193:4249, 4194:4194]                               str     Row prescan section for quadrant D
    DAC13         0.0,0.1187                                           str     [V] set value, measured value
    OFFSET3       0.4000000059604645,-8.8786                           str     [V] set value, measured value
    AMPSECD       [4114:2058, 4128:2065]                               str     AMP section for quadrant D
    DAC9          -25.0003,-24.946                                     str     [V] set value, measured value
    DELAYS        20, 20, 25, 40, 7, 3000, 7, 7, 400, 7                str     [10] Delay settings
    SETTINGS      detectors_sm_20210128.json                           str     Name of DESI CCD settings file
    DETSECA       [1:2057, 1:2064]                                     str     Detector section for quadrant A
    CLOCK5        9.9999,0.0                                           str     [V] high rail, low rail
    PRRSECB       [2193:4249, 1:1]                                     str     Row prescan section for quadrant B
    DETECTOR      M1-53                                                str     Detector (ccd) identification
    CLOCK12       9.9992,2.9993                                        str     [V] high rail, low rail
    DAC12         0.0,0.1039                                           str     [V] set value, measured value
    TRIMSECA      [8:2064, 2:2065]                                     str     Trim section for quadrant A
    DATASECB      [2193:4249, 2:2065]                                  str     Data section for quadrant B
    CDSPARMS      400, 400, 8, 2000                                    str     CDS parameters
    TRIMSECC      [8:2064, 2130:4193]                                  str     Trim section for quadrant C
    DAC3          -9.0002,-8.8683                                      str     [V] set value, measured value
    BIASSECA      [2065:2128, 2:2065]                                  str     Bias section for quadrant A
    TRIMSECB      [2193:4249, 2:2065]                                  str     Trim section for quadrant B
    CASETEMP      60.1833                                              float   [deg C] CCD controller case temperature
    CPUTEMP       59.5781                                              float   [deg C] CCD controller CPU temperature
    OFFSET5       2.0,6.0806                                           str     [V] set value, measured value
    CCDSECD       [2058:4114, 2065:4128]                               str     CCD section for quadrant D
    CCDNAME       CCDSM4Z                                              str     CCD name
    DAC4          5.9998,6.0648                                        str     [V] set value, measured value
    BLDTIME       0.3529                                               float   [s] Time to build image
    CLOCK13       9.9992,2.9993                                        str     [V] high rail, low rail
    CLOCK1        9.9999,0.0                                           str     [V] high rail, low rail
    PRESECA       [1:7, 2:2065]                                        str     Prescan section for quadrant A
    CCDSIZE       4194,4256                                            str     CCD size in pixels (rows, columns)
    DATASECC      [8:2064, 2130:4193]                                  str     Data section for quadrant C
    CLOCK18       9.0,0.9999                                           str     [V] high rail, low rail
    CLOCK10       9.9992,2.9993                                        str     [V] high rail, low rail
    CRYOTEMP      139.962                                              float   [deg K] Cryostat CCD temperature
    CLOCK3        -2.0001,3.9999                                       str     [V] high rail, low rail
    DAC0          -9.0002,-8.7962                                      str     [V] set value, measured value
    CCDSECA       [1:2057, 1:2064]                                     str     CCD section for quadrant A
    CLOCK11       9.9992,2.9993                                        str     [V] high rail, low rail
    CLOCK2        9.9999,0.0                                           str     [V] high rail, low rail
    CLOCK9        9.9992,2.9993                                        str     [V] high rail, low rail
    CLOCK17       9.0,0.9999                                           str     [V] high rail, low rail
    ORSECC        [8:2064, 2098:2129]                                  str     Row overscan section for quadrant C
    CCDSECC       [1:2057, 2065:4128]                                  str     CCD section for quadrant C
    PRESECD       [4250:4256, 2130:4193]                               str     Prescan section for quadrant D
    BIASSECD      [2129:2192, 2130:4193]                               str     Bias section for quadrant D
    AMPSECB       [4114:2058, 1:2064]                                  str     AMP section for quadrant B
    CCDCFG        default_lbnl_20210128.cfg                            str     CCD configuration file
    BIASSECB      [2129:2192, 2:2065]                                  str     Bias section for quadrant B
    BIASSECC      [2065:2128, 2130:4193]                               str     Bias section for quadrant C
    CLOCK16       9.9999,3.0                                           str     [V] high rail, low rail
    CCDPREP       purge,clear                                          str     CCD prep actions
    DAC8          -25.0003,-24.8273                                    str     [V] set value, measured value
    PRRSECA       [8:2064, 1:1]                                        str     Row prescan section for quadrant A
    DATASECD      [2193:4249, 2130:4193]                               str     Data section for quadrant D
    DAC5          5.9998,6.0806                                        str     [V] set value, measured value
    PRESECC       [1:7, 2130:4193]                                     str     Prescan section for quadrant C
    OFFSET1       0.4000000059604645,-8.8786                           str     [V] set value, measured value
    OFFSET4       2.0,6.0595                                           str     [V] set value, measured value
    DAC7          5.9998,5.9964                                        str     [V] set value, measured value
    DAC6          5.9998,6.0963                                        str     [V] set value, measured value
    OFFSET7       2.0,5.9911                                           str     [V] set value, measured value
    DETSECC       [1:2057, 2065:4128]                                  str     Detector section for quadrant C
    TRIMSECD      [2193:4249, 2130:4193]                               str     Trim section for quadrant D
    CCDSECB       [2058:4114, 1:2064]                                  str     CCD section for quadrant B
    REQTIME       1860.0                                               float   [s] Requested exposure time
    OBSID         kp4m20220114t110417                                  str     Unique observation identifier
    PROCTYPE      RAW                                                  str     Data processing level
    PRODTYPE      image                                                str     Data product type
    CHECKSUM      mqJSonIQmnIQmnIQ                                     str     HDU checksum updated 2022-01-14T11:15:05
    DATASUM       3453799606                                           str     data unit checksum updated 2022-01-14T11:15:05
    ============= ==================================================== ======= ===============================================

    .. [1] Optional

Data: FITS image [int16 (compressed), 4256x4194]

HDU03 -- HDU31
--------------

EXTNAME = B0, R0, B1, R1, Z1, B2, R2, Z2, B3, R3, Z3, B4, R4, Z4, B5, R5, Z5, B6, R6, Z6, B7, R7, Z7, B8, R8, Z8, B9, R9, Z9

Data: See Z0.

Note: any combination of B0..Z9 could exist in any order.

HDU32
-----

EXTNAME = SPECTCONS

This is a telemetry table. This table contains variable-length arrays, whose
length depends on the exact number of HDUs included in this file.

Note: this is the last HDU, but its exact number will depend upon the number of
cameras in included in the file.


Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ========== ============================================================================================================ ======= ===============================================
    KEY        Example Value                                                                                                Type    Comment
    ========== ============================================================================================================ ======= ===============================================
    NAXIS1     352                                                                                                          int     width of table in bytes
    NAXIS2     10                                                                                                           int     number of rows in table
    EXPID      118526                                                                                                       int     Exposure number
    EXPFRAME   0                                                                                                            int     Frame number
    FRAMES     None                                                                                                         Unknown Number of Frames in Archive
    TILEID     4403                                                                                                         int     DESI Tile ID
    FIBASSGN   /data/tiles/SVN_tiles/004/fiberassign-004403.fits.gz                                                         str     Fiber assign
    FLAVOR     science                                                                                                      str     Observation type
    SEQUENCE   _Split                                                                                                       str     OCS Sequence name
    PURPOSE    Main Survey                                                                                                  str     Purpose of observing night
    PROGRAM    DARK                                                                                                         str     Program name
    PROPID     2020B-5000                                                                                                   str     Proposal ID
    OBSERVER   Jessica Chellino, Corentin Ravoux                                                                            str     Names of observers
    LEAD       Martin Landriau                                                                                              str     Lead observer
    INSTRUME   DESI                                                                                                         str     Instrument name
    OBSERVAT   KPNO                                                                                                         str     Observatory name
    OBS-LAT    31.96403                                                                                                     str     [deg] Observatory latitude
    OBS-LONG   -111.59989                                                                                                   str     [deg] Observatory east longitude
    OBS-ELEV   2097.0                                                                                                       float   [m] Observatory elevation
    TELESCOP   KPNO 4.0-m telescope                                                                                         str     Telescope name
    CORRCTOR   DESI Corrector                                                                                               str     Corrector Identification
    NIGHT      20220113                                                                                                     int     Observing night
    TIMESYS    UTC                                                                                                          str     Time system used for date-obs
    DELTARA    0.                                                                                                           float   [arcsec] Offset], right ascension, observer inp
    DELTADEC   0.                                                                                                           float   [arcsec] Offset], declination, observer input
    REQRA      170.239                                                                                                      float   [deg] Requested right ascension (observer input
    REQDEC     -7.093                                                                                                       float   [deg] Requested declination (observer input)
    FOCUS      946.6,-231.6,-83.4,-18.3,9.8,139.4                                                                           str     Telescope focus settings
    TRUSTEMP   12.267                                                                                                       float   [deg] Average Telescope truss temperature (only
    PMIRTEMP   11.675                                                                                                       float   [deg] Average primary mirror temperature (nit,e
    EPOCH      2000.0                                                                                                       float   Epoch of observation
    MOUNTAZ    176.725567                                                                                                   float   [deg] Mount azimuth angle
    MOUNTDEC   -7.102329                                                                                                    float   [deg] Mount declination
    MOUNTEL    50.883914                                                                                                    float   [deg] Mount elevation angle
    MOUNTHA    -2.081118                                                                                                    float   [deg] Mount hour angle
    SKYDEC     -7.102329                                                                                                    float   [deg] Telescope declination (pointing on sky)
    SKYRA [1]_ 170.24163                                                                                                    float   [deg] Telescope right ascension (pointing on sk
    TARGTDEC   -7.102329                                                                                                    float   [deg] Target declination (to TCS)
    TARGTRA    170.24163                                                                                                    float   [deg] Target right ascension (to TCS)
    USEETC     T                                                                                                            bool    ETC data available if true
    USESKY     T                                                                                                            bool    DOS Control: use Sky Monitor
    USEFOCUS   T                                                                                                            bool    DOS Control: use focus
    HEXTRIM    0.0,0.0,0.0,0.0,0.0,0.0                                                                                      str     Hexapod trim values
    USEROTAT   T                                                                                                            bool    DOS Control: use rotator
    ROTOFFST   138.8                                                                                                        float   [arcsec] Rotator offset
    ROTENBLD   T                                                                                                            bool    Rotator enabled
    ROTRATE    0.513                                                                                                        float   [arcsec/min] Rotator rate
    USEGUIDR   T                                                                                                            bool    DOS Control: use guider
    USEDONUT   T                                                                                                            bool    DOS Control: use donuts
    SPCGRPHS   SP4, SP9, SP8, SP2, SP0, SP5, SP7, SP6, SP1, SP3                                                             str     Participating spe
    DEVICES    SPECTCON4, SPECTCON9, SPECTCON8, SPECTCON2, SPECTCON0, SPECTCON5, SPECTCON7, SPECTCON6, SPECTCON1, SPECTCON3 str     Participating devices (spectro controller)
    RADESYS    FK5                                                                                                          str     Coordinate reference frame of major/minor axes
    DOSVER     trunk                                                                                                        str     DOS software version
    OCSVER     1.2                                                                                                          float   OCS software version
    CONSTVER   DESI:CURRENT                                                                                                 str     Constants version
    INIFILE    /data/msdos/dos_home/architectures/kpno/desi.ini                                                             str     DOS Configuration
    REQTIME    1860.0                                                                                                       float   [s] Requested exposure time
    OBSID      kp4m20220114t110417                                                                                          str     Unique observation identifier
    PROCTYPE   RAW                                                                                                          str     Data processing level
    PRODTYPE   image                                                                                                        str     Data product type
    CHECKSUM   0YhA1VZ30VfA0VZ3                                                                                             str     HDU checksum updated 2022-01-14T11:15:09
    DATASUM    2915472531                                                                                                   str     data unit checksum updated 2022-01-14T11:15:09
    ========== ============================================================================================================ ======= ===============================================

    .. [1] Optional

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

======== =========== ===== ===================
Name     Type        Units Description
======== =========== ===== ===================
unit     int64             label for field   1
specid   int64             label for field   2
EXPTIME  float64           label for field   3
DATE-OBS char stream       label for field   4
TIME-OBS char stream       label for field   5
MJD-OBS  float64           label for field   6
ST       char stream       label for field   7
OPENSHUT char stream       label for field   8
OBSID    char stream       label for field   9
STATUS   char stream       label for field  10
HARTL    char stream       label for field  11
HARTLP   char stream       label for field  12
HARTR    char stream       label for field  13
HARTRP   char stream       label for field  14
WAGO     char stream       label for field  15
NIRSHUT  char stream       label for field  16
NIRSEAL  char stream       label for field  17
NIRPOW   char stream       label for field  18
EXPSHUT  char stream       label for field  19
EXPSEAL  char stream       label for field  20
EXPPOW   char stream       label for field  21
ILLUM    char stream       label for field  22
ZTEMP    float64           label for field  23
ZHUMID   float64           label for field  24
BTEMP    float64           label for field  25
BHUMID   float64           label for field  26
RTEMP    float64           label for field  27
RHUMID   float64           label for field  28
IEBTEMP  float64           label for field  29
COLLTEMP float64           label for field  30
CRYOTEMP float64           label for field  31
BZTEMP   float64           label for field  32
MIRROR   char stream       label for field  33
MOUNT    char stream       label for field  34
EXPMEC   char stream       label for field  35
ZDICHR   char stream       label for field  36
NIRMEC   char stream       label for field  37
RDICHR   char stream       label for field  38
BVPHG    char stream       label for field  39
ZVPHG    char stream       label for field  40
RVPHG    char stream       label for field  41
BCAM     char stream       label for field  42
ZCAM     char stream       label for field  43
RCAM     char stream       label for field  44
======== =========== ===== ===================


Notes and Examples
==================

Provenance
----------

* 2019-02-21: Revised based on headers from spectrograph functional verification files.
* 2019-04-03: Revised based on raw data files created from spectrograph functional verification files.
* 2023-03-21: Revised in preparation for first public data release.

Known Issues
------------

* The compressed ``SPEC`` HDU contains the ``ZSIMPLE`` keyword. This would
  be appropriate in a compressed *primary* HDU but not in a compressed extension.
* Does ``MJD-OBS`` save sufficient decimal precision to actually reconstruct ``DATE-OBS`` to microsecond precision?
* Some header keywords contain empty values. These will produce
  warnings when files of this type are examined with ``fitsverify``.

Expected Changes
----------------

* Coordinate with ICS for header keywords (*e.g.* ``FLAVOR`` -> ``PROGRAM``).
