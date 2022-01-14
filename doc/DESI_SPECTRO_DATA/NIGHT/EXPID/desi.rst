====
desi
====

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``desi-00118526.fits.fz``, where ... *Give a human readable
    description of the filename, e.g. ``blat-{EXPID}`` where ``{EXPID}``
    is the 8-digit exposure ID.*
:Regex: ``desi-00118526.fits.fz`` *Give a regular expression for this filename.
    For example, a six-digit number would correspond to ``[0-9]{6}``.*
:File Type: FITS, 394 MB  *This section gives the type of the file
    and its approximate size.*

Contents
========

====== ========= ======== ===================
Number EXTNAME   Type     Contents
====== ========= ======== ===================
HDU00_           IMAGE    *Brief Description*
HDU01_ SPEC      BINTABLE *Brief Description*
HDU02_ Z4        BINTABLE *Brief Description*
HDU03_ R4        BINTABLE *Brief Description*
HDU04_ B4        BINTABLE *Brief Description*
HDU05_ Z9        BINTABLE *Brief Description*
HDU06_ R9        BINTABLE *Brief Description*
HDU07_ B9        BINTABLE *Brief Description*
HDU08_ Z8        BINTABLE *Brief Description*
HDU09_ R8        BINTABLE *Brief Description*
HDU10_ B8        BINTABLE *Brief Description*
HDU11_ Z2        BINTABLE *Brief Description*
HDU12_ R2        BINTABLE *Brief Description*
HDU13_ B2        BINTABLE *Brief Description*
HDU14_ Z0        BINTABLE *Brief Description*
HDU15_ R0        BINTABLE *Brief Description*
HDU16_ B0        BINTABLE *Brief Description*
HDU17_ Z5        BINTABLE *Brief Description*
HDU18_ R5        BINTABLE *Brief Description*
HDU19_ B5        BINTABLE *Brief Description*
HDU20_ Z7        BINTABLE *Brief Description*
HDU21_ R7        BINTABLE *Brief Description*
HDU22_ B7        BINTABLE *Brief Description*
HDU23_ Z6        BINTABLE *Brief Description*
HDU24_ R6        BINTABLE *Brief Description*
HDU25_ B6        BINTABLE *Brief Description*
HDU26_ Z1        BINTABLE *Brief Description*
HDU27_ R1        BINTABLE *Brief Description*
HDU28_ B1        BINTABLE *Brief Description*
HDU29_ Z3        BINTABLE *Brief Description*
HDU30_ R3        BINTABLE *Brief Description*
HDU31_ B3        BINTABLE *Brief Description*
HDU32_ SPECTCONS BINTABLE *Brief Description*
====== ========= ======== ===================


FITS Header Units
=================

HDU00
-----

*Summarize the contents of this HDU.*

This HDU has no non-standard required keywords.

Empty HDU.

HDU01
-----

EXTNAME = SPEC

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

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

EXTNAME = Z4

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   4194                                                 int     number of rows in table
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
EXPID    118526                                               int     Exposure number
EXPFRAME 0                                                    int     Frame number
FRAMES   None                                                 Unknown Number of Frames in Archive
TILEID   4403                                                 int     DESI Tile ID
FIBASSGN /data/tiles/SVN_tiles/004/fiberassign-004403.fits.gz str     Fiber assign
FLAVOR   science                                              str     Observation type
SEQUENCE _Split                                               str     OCS Sequence name
PURPOSE  Main Survey                                          str     Purpose of observing night
PROGRAM  DARK                                                 str     Program name
PROPID   2020B-5000                                           str     Proposal ID
OBSERVER Jessica Chellino, Corentin Ravoux                    str     Names of observers
LEAD     Martin Landriau                                      str     Lead observer
INSTRUME DESI                                                 str     Instrument name
OBSERVAT KPNO                                                 str     Observatory name
OBS-LAT  31.96403                                             str     [deg] Observatory latitude
OBS-LONG -111.59989                                           str     [deg] Observatory east longitude
OBS-ELEV 2097.0                                               float   [m] Observatory elevation
TELESCOP KPNO 4.0-m telescope                                 str     Telescope name
CORRCTOR DESI Corrector                                       str     Corrector Identification
NIGHT    20220113                                             int     Observing night
TIMESYS  UTC                                                  str     Time system used for date-obs
DATE-OBS 2022-01-14T11:04:17.824419072                        str     [UTC] Observation data and start tim
TIME-OBS 2022-01-14T11:04:17.824419072                        str     [UTC] Observation start time
MJD-OBS  59593.46131741                                       float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:04:18.610806                           str     Time shutter opened
ST       11:13:28.580000                                      str     Local Sidereal time at observation start (HH:MM
EXPTIME  579.164                                              float   [s] Actual exposure time
REQRA    170.239                                              float   [deg] Requested right ascension (observer input
REQDEC   -7.093                                               float   [deg] Requested declination (observer input)
FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                   str     Telescope focus settings
VCCD     ON                                                   str     True (ON) if CCD voltage is on
VCCDON   2022-01-10T20:55:43.770055                           str     Time when CCD voltage was turned on
VCCDSEC  310751.8                                             float   [s] CCD on time in seconds
TRUSTEMP 12.267                                               float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.675                                               float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                               float   Epoch of observation
MOUNTAZ  176.725567                                           float   [deg] Mount azimuth angle
MOUNTDEC -7.102329                                            float   [deg] Mount declination
MOUNTEL  50.883914                                            float   [deg] Mount elevation angle
MOUNTHA  -2.081118                                            float   [deg] Mount hour angle
SKYDEC   -7.102329                                            float   [deg] Telescope declination (pointing on sky)
SKYRA    170.24163                                            float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.102329                                            float   [deg] Target declination (to TCS)
TARGTRA  170.24163                                            float   [deg] Target right ascension (to TCS)
USEETC   T                                                    bool    ETC data available if true
USESKY   T                                                    bool    DOS Control: use Sky Monitor
USEFOCUS T                                                    bool    DOS Control: use focus
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                              str     Hexapod trim values
USEROTAT T                                                    bool    DOS Control: use rotator
ROTOFFST 138.8                                                float   [arcsec] Rotator offset
ROTENBLD T                                                    bool    Rotator enabled
ROTRATE  0.513                                                float   [arcsec/min] Rotator rate
USEGUIDR T                                                    bool    DOS Control: use guider
USEDONUT T                                                    bool    DOS Control: use donuts
SPECGRPH 4                                                    int     Spectrograph logical name (SP)
SPECID   1                                                    int     Spectrograph serial number (SM)
FEEBOX   lbnl053                                              str     CCD Controller serial number
VESSEL   2                                                    int     Cryostat serial number
FEEVER   v20160312                                            str     CCD Controller version
DETFLVER FAILED: invalid argument for get command             str     CCD Controller detector f
FEEPOWER ON                                                   str     FEE power status
FEEDMASK 2134851391                                           int     FEE dac mask
FEECMASK 1048575                                              int     FEE clk mask
CCDTEMP  -134.6382                                            float   [deg C] CCD controller CCD temperature
RADESYS  FK5                                                  str     Coordinate reference frame of major/minor axes
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
CCDSIZE  4194,4256                                            str     CCD size in pixels (rows, columns)
DATASECA [8:2064, 2:2065]                                     str     Data section for quadrant A
OFFSET4  2.0,5.9806                                           str     [V] set value, measured value
PRESECC  [1:7, 2130:4193]                                     str     Prescan section for quadrant C
OFFSET7  2.0,6.0437                                           str     [V] set value, measured value
OFFSET1  0.4000000059604645,-8.8683                           str     [V] set value, measured value
DAC6     5.9998,6.0227                                        str     [V] set value, measured value
DAC15    0.0,0.0742                                           str     [V] set value, measured value
DETSECB  [2058:4114, 1:2064]                                  str     Detector section for quadrant B
TRIMSECB [2193:4249, 2:2065]                                  str     Trim section for quadrant B
OFFSET3  0.4000000059604645,-8.8786                           str     [V] set value, measured value
ORSECA   [8:2064, 2066:2097]                                  str     Row overscan section for quadrant A
AMPSECC  [1:2057, 4128:2065]                                  str     AMP section for quadrant C
CCDPREP  purge,clear                                          str     CCD prep actions
CPUTEMP  61.7929                                              float   [deg C] CCD controller CPU temperature
CCDSECA  [1:2057, 1:2064]                                     str     CCD section for quadrant A
CLOCK18  9.0,0.9999                                           str     [V] high rail, low rail
ORSECD   [2193:4249, 2098:2129]                               str     Row bias section for quadrant D
CAMERA   z4                                                   str     Camera name
CLOCK0   9.9999,0.0                                           str     [V] high rail, low rail
BIASSECD [2129:2192, 2130:4193]                               str     Bias section for quadrant D
PRESECD  [4250:4256, 2130:4193]                               str     Prescan section for quadrant D
PRRSECC  [8:2064, 4194:4194]                                  str     Row prescan section for quadrant C
DAC16    39.9961,39.4086                                      str     [V] set value, measured value
DAC14    0.0,0.0742                                           str     [V] set value, measured value
DAC17    20.0008,11.8828                                      str     [V] set value, measured value
TRIMSECA [8:2064, 2:2065]                                     str     Trim section for quadrant A
DAC12    0.0,0.089                                            str     [V] set value, measured value
PRRSECD  [2193:4249, 4194:4194]                               str     Row prescan section for quadrant D
CCDNAME  CCDSM1Z                                              str     CCD name
CLOCK13  9.9992,2.9993                                        str     [V] high rail, low rail
PRRSECB  [2193:4249, 1:1]                                     str     Row prescan section for quadrant B
DAC8     -25.0003,-24.6047                                    str     [V] set value, measured value
BIASSECB [2129:2192, 2:2065]                                  str     Bias section for quadrant B
CLOCK2   9.9999,0.0                                           str     [V] high rail, low rail
CLOCK15  9.9992,2.9993                                        str     [V] high rail, low rail
AMPSECB  [4114:2058, 1:2064]                                  str     AMP section for quadrant B
CCDSECC  [1:2057, 2065:4128]                                  str     CCD section for quadrant C
CCDSECD  [2058:4114, 2065:4128]                               str     CCD section for quadrant D
TRIMSECD [2193:4249, 2130:4193]                               str     Trim section for quadrant D
CLOCK12  9.9992,2.9993                                        str     [V] high rail, low rail
DELAYS   20, 20, 25, 40, 7, 3000, 7, 7, 400, 7                str     [10] Delay settings
CLOCK11  9.9992,2.9993                                        str     [V] high rail, low rail
ORSECC   [8:2064, 2098:2129]                                  str     Row overscan section for quadrant C
CLOCK14  9.9992,2.9993                                        str     [V] high rail, low rail
CDSPARMS 400, 400, 8, 2000                                    str     CDS parameters
CLOCK7   -2.0001,3.9999                                       str     [V] high rail, low rail
DAC10    -25.0003,-24.8125                                    str     [V] set value, measured value
DATASECD [2193:4249, 2130:4193]                               str     Data section for quadrant D
OFFSET5  2.0,6.0648                                           str     [V] set value, measured value
CLOCK4   9.9999,0.0                                           str     [V] high rail, low rail
DATASECB [2193:4249, 2:2065]                                  str     Data section for quadrant B
CASETEMP 61.6599                                              float   [deg C] CCD controller case temperature
CLOCK3   -2.0001,3.9999                                       str     [V] high rail, low rail
DETSECA  [1:2057, 1:2064]                                     str     Detector section for quadrant A
PRESECA  [1:7, 2:2065]                                        str     Prescan section for quadrant A
DAC2     -9.0002,-8.8477                                      str     [V] set value, measured value
DAC1     -9.0002,-8.8683                                      str     [V] set value, measured value
CLOCK9   9.9992,2.9993                                        str     [V] high rail, low rail
BLDTIME  0.3518                                               float   [s] Time to build image
AMPSECD  [4114:2058, 4128:2065]                               str     AMP section for quadrant D
PGAGAIN  3                                                    int     Controller gain
CLOCK6   9.9999,0.0                                           str     [V] high rail, low rail
DETSECD  [2058:4114, 2065:4128]                               str     Detector section for quadrant D
ORSECB   [2193:4249, 2066:2097]                               str     Row overscan section for quadrant B
SETTINGS detectors_sm_20210128.json                           str     Name of DESI CCD settings file
OFFSET6  2.0,6.0174                                           str     [V] set value, measured value
DETECTOR M1-20                                                str     Detector (ccd) identification
DAC11    -25.0003,-24.3376                                    str     [V] set value, measured value
BIASSECC [2065:2128, 2130:4193]                               str     Bias section for quadrant C
DETSECC  [1:2057, 2065:4128]                                  str     Detector section for quadrant C
PRRSECA  [8:2064, 1:1]                                        str     Row prescan section for quadrant A
CLOCK8   9.9992,2.9993                                        str     [V] high rail, low rail
OFFSET0  0.4000000059604645,-8.8683                           str     [V] set value, measured value
CRYOPRES 6.606e-08                                            str     [mb] Cryostat pressure (IP)
DIGITIME 56.4552                                              float   [s] Time to digitize image
PRESECB  [4250:4256, 2:2065]                                  str     Prescan section for quadrant B
CLOCK17  9.0,0.9999                                           str     [V] high rail, low rail
CLOCK5   9.9999,0.0                                           str     [V] high rail, low rail
DAC0     -9.0002,-8.8786                                      str     [V] set value, measured value
DAC3     -9.0002,-8.8786                                      str     [V] set value, measured value
CCDSECB  [2058:4114, 1:2064]                                  str     CCD section for quadrant B
CCDCFG   default_lbnl_20210128.cfg                            str     CCD configuration file
DAC4     5.9998,5.9806                                        str     [V] set value, measured value
DAC9     -25.0003,-24.6641                                    str     [V] set value, measured value
AMPSECA  [1:2057, 1:2064]                                     str     AMP section for quadrant A
DAC13    0.0,0.0594                                           str     [V] set value, measured value
DAC7     5.9998,6.0385                                        str     [V] set value, measured value
CLOCK1   9.9999,0.0                                           str     [V] high rail, low rail
OFFSET2  0.4000000059604645,-8.8374                           str     [V] set value, measured value
CLOCK16  9.9999,3.0                                           str     [V] high rail, low rail
DAC5     5.9998,6.0648                                        str     [V] set value, measured value
CLOCK10  9.9992,2.9993                                        str     [V] high rail, low rail
CRYOTEMP 139.937                                              float   [deg K] Cryostat CCD temperature
DATASECC [8:2064, 2130:4193]                                  str     Data section for quadrant C
BIASSECA [2065:2128, 2:2065]                                  str     Bias section for quadrant A
CCDTMING flatdark_lbnl_timing.txt                             str     CCD timing file
TRIMSECC [8:2064, 2130:4193]                                  str     Trim section for quadrant C
REQTIME  1860.0                                               float   [s] Requested exposure time
OBSID    kp4m20220114t110417                                  str     Unique observation identifier
PROCTYPE RAW                                                  str     Data processing level
PRODTYPE image                                                str     Data product type
CHECKSUM 33ma50mY30ma30mY                                     str     HDU checksum updated 2022-01-14T11:15:03
DATASUM  3812990342                                           str     data unit checksum updated 2022-01-14T11:15:03
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 4256x4194]

HDU03
-----

EXTNAME = R4

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   4194                                                 int     number of rows in table
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
EXPID    118526                                               int     Exposure number
EXPFRAME 0                                                    int     Frame number
FRAMES   None                                                 Unknown Number of Frames in Archive
TILEID   4403                                                 int     DESI Tile ID
FIBASSGN /data/tiles/SVN_tiles/004/fiberassign-004403.fits.gz str     Fiber assign
FLAVOR   science                                              str     Observation type
SEQUENCE _Split                                               str     OCS Sequence name
PURPOSE  Main Survey                                          str     Purpose of observing night
PROGRAM  DARK                                                 str     Program name
PROPID   2020B-5000                                           str     Proposal ID
OBSERVER Jessica Chellino, Corentin Ravoux                    str     Names of observers
LEAD     Martin Landriau                                      str     Lead observer
INSTRUME DESI                                                 str     Instrument name
OBSERVAT KPNO                                                 str     Observatory name
OBS-LAT  31.96403                                             str     [deg] Observatory latitude
OBS-LONG -111.59989                                           str     [deg] Observatory east longitude
OBS-ELEV 2097.0                                               float   [m] Observatory elevation
TELESCOP KPNO 4.0-m telescope                                 str     Telescope name
CORRCTOR DESI Corrector                                       str     Corrector Identification
NIGHT    20220113                                             int     Observing night
TIMESYS  UTC                                                  str     Time system used for date-obs
DATE-OBS 2022-01-14T11:04:17.824419072                        str     [UTC] Observation data and start tim
TIME-OBS 2022-01-14T11:04:17.824419072                        str     [UTC] Observation start time
MJD-OBS  59593.46131741                                       float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:04:18.610806                           str     Time shutter opened
ST       11:13:28.580000                                      str     Local Sidereal time at observation start (HH:MM
EXPTIME  579.164                                              float   [s] Actual exposure time
REQRA    170.239                                              float   [deg] Requested right ascension (observer input
REQDEC   -7.093                                               float   [deg] Requested declination (observer input)
FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                   str     Telescope focus settings
VCCD     ON                                                   str     True (ON) if CCD voltage is on
VCCDON   2022-01-10T20:55:36.957452                           str     Time when CCD voltage was turned on
VCCDSEC  310758.6                                             float   [s] CCD on time in seconds
TRUSTEMP 12.267                                               float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.675                                               float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                               float   Epoch of observation
MOUNTAZ  176.725567                                           float   [deg] Mount azimuth angle
MOUNTDEC -7.102329                                            float   [deg] Mount declination
MOUNTEL  50.883914                                            float   [deg] Mount elevation angle
MOUNTHA  -2.081118                                            float   [deg] Mount hour angle
SKYDEC   -7.102329                                            float   [deg] Telescope declination (pointing on sky)
SKYRA    170.24163                                            float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.102329                                            float   [deg] Target declination (to TCS)
TARGTRA  170.24163                                            float   [deg] Target right ascension (to TCS)
USEETC   T                                                    bool    ETC data available if true
USESKY   T                                                    bool    DOS Control: use Sky Monitor
USEFOCUS T                                                    bool    DOS Control: use focus
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                              str     Hexapod trim values
USEROTAT T                                                    bool    DOS Control: use rotator
ROTOFFST 138.8                                                float   [arcsec] Rotator offset
ROTENBLD T                                                    bool    Rotator enabled
ROTRATE  0.513                                                float   [arcsec/min] Rotator rate
USEGUIDR T                                                    bool    DOS Control: use guider
USEDONUT T                                                    bool    DOS Control: use donuts
SPECGRPH 4                                                    int     Spectrograph logical name (SP)
SPECID   1                                                    int     Spectrograph serial number (SM)
FEEBOX   lbnl065                                              str     CCD Controller serial number
VESSEL   1                                                    int     Cryostat serial number
FEEVER   v20160312                                            str     CCD Controller version
DETFLVER FAILED: invalid argument for get command             str     CCD Controller detector f
FEEPOWER ON                                                   str     FEE power status
FEEDMASK 2134851391                                           int     FEE dac mask
FEECMASK 1048575                                              int     FEE clk mask
CCDTEMP  -134.0275                                            float   [deg C] CCD controller CCD temperature
RADESYS  FK5                                                  str     Coordinate reference frame of major/minor axes
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
CCDCFG   LBNL-PE-21-20211015.cfg                              str     CCD configuration file
CLOCK14  9.9992,2.9993                                        str     [V] high rail, low rail
CCDSECC  [1:2057, 2065:4128]                                  str     CCD section for quadrant C
PRRSECA  [8:2064, 1:1]                                        str     Row prescan section for quadrant A
CLOCK18  7.9998,0.0                                           str     [V] high rail, low rail
CCDPREP  purge,clear                                          str     CCD prep actions
CLOCK4   9.9999,-2.0001                                       str     [V] high rail, low rail
PRESECD  [4250:4256, 2130:4193]                               str     Prescan section for quadrant D
DAC2     -10.6006,-10.4442                                    str     [V] set value, measured value
DAC16    39.9961,39.4086                                      str     [V] set value, measured value
CCDTMING flatdark_lbnl_timing.txt                             str     CCD timing file
DAC10    -25.0003,-25.0944                                    str     [V] set value, measured value
DIGITIME 56.4569                                              float   [s] Time to digitize image
DAC13    0.0,0.0742                                           str     [V] set value, measured value
DETSECD  [2058:4114, 2065:4128]                               str     Detector section for quadrant D
CLOCK2   9.9999,-2.0001                                       str     [V] high rail, low rail
CLOCK1   9.9999,-2.0001                                       str     [V] high rail, low rail
CLOCK8   9.9992,2.9993                                        str     [V] high rail, low rail
OFFSET7  2.0,6.0648                                           str     [V] set value, measured value
CLOCK13  9.9992,2.9993                                        str     [V] high rail, low rail
TRIMSECB [2193:4249, 2:2065]                                  str     Trim section for quadrant B
CLOCK10  9.9992,2.9993                                        str     [V] high rail, low rail
TRIMSECA [8:2064, 2:2065]                                     str     Trim section for quadrant A
DETSECB  [2058:4114, 1:2064]                                  str     Detector section for quadrant B
DATASECC [8:2064, 2130:4193]                                  str     Data section for quadrant C
CRYOTEMP 163.044                                              float   [deg K] Cryostat CCD temperature
CCDNAME  CCDSM1R                                              str     CCD name
PRRSECB  [2193:4249, 1:1]                                     str     Row prescan section for quadrant B
PRRSECD  [2193:4249, 4194:4194]                               str     Row prescan section for quadrant D
DAC9     -25.0003,-24.7234                                    str     [V] set value, measured value
DAC8     -25.0003,-24.7828                                    str     [V] set value, measured value
CCDSECD  [2058:4114, 2065:4128]                               str     CCD section for quadrant D
CCDSIZE  4194,4256                                            str     CCD size in pixels (rows, columns)
BLDTIME  0.3518                                               float   [s] Time to build image
DAC6     3.9999,4.0397                                        str     [V] set value, measured value
CLOCK5   9.9999,-2.0001                                       str     [V] high rail, low rail
BIASSECD [2129:2192, 2130:4193]                               str     Bias section for quadrant D
TRIMSECD [2193:4249, 2130:4193]                               str     Trim section for quadrant D
CLOCK16  9.9999,3.0                                           str     [V] high rail, low rail
CLOCK12  9.9992,2.9993                                        str     [V] high rail, low rail
CCDSECB  [2058:4114, 1:2064]                                  str     CCD section for quadrant B
OFFSET2  0.4000000059604645,-10.4442                          str     [V] set value, measured value
DETSECA  [1:2057, 1:2064]                                     str     Detector section for quadrant A
DAC15    0.0,0.0445                                           str     [V] set value, measured value
OFFSET3  0.4000000059604645,-8.8889                           str     [V] set value, measured value
AMPSECD  [4114:2058, 4128:2065]                               str     AMP section for quadrant D
BIASSECA [2065:2128, 2:2065]                                  str     Bias section for quadrant A
DAC1     -9.0002,-8.9816                                      str     [V] set value, measured value
ORSECC   [8:2064, 2098:2129]                                  str     Row overscan section for quadrant C
DAC12    0.0,0.0594                                           str     [V] set value, measured value
CLOCK9   9.9992,2.9993                                        str     [V] high rail, low rail
CLOCK0   9.9999,-2.0001                                       str     [V] high rail, low rail
DAC7     5.9998,6.0648                                        str     [V] set value, measured value
ORSECB   [2193:4249, 2066:2097]                               str     Row overscan section for quadrant B
DATASECB [2193:4249, 2:2065]                                  str     Data section for quadrant B
DAC14    0.0,0.0742                                           str     [V] set value, measured value
CAMERA   r4                                                   str     Camera name
PRESECA  [1:7, 2:2065]                                        str     Prescan section for quadrant A
CLOCK6   9.9999,-2.0001                                       str     [V] high rail, low rail
CDSPARMS 400, 400, 8, 2000                                    str     CDS parameters
DAC17    20.0008,12.1024                                      str     [V] set value, measured value
DELAYS   20, 20, 25, 40, 7, 3000, 7, 7, 400, 7                str     [10] Delay settings
CLOCK11  9.9992,2.9993                                        str     [V] high rail, low rail
CASETEMP 55.1384                                              float   [deg C] CCD controller case temperature
CCDSECA  [1:2057, 1:2064]                                     str     CCD section for quadrant A
DAC3     -9.0002,-8.8889                                      str     [V] set value, measured value
AMPSECB  [4114:2058, 1:2064]                                  str     AMP section for quadrant B
OFFSET6  2.0,4.0397                                           str     [V] set value, measured value
CLOCK15  9.9992,2.9993                                        str     [V] high rail, low rail
CLOCK7   -2.0001,3.9999                                       str     [V] high rail, low rail
DATASECA [8:2064, 2:2065]                                     str     Data section for quadrant A
SETTINGS detectors_sm_20211015.json                           str     Name of DESI CCD settings file
OFFSET5  2.0,6.049                                            str     [V] set value, measured value
OFFSET4  2.0,6.0437                                           str     [V] set value, measured value
BIASSECC [2065:2128, 2130:4193]                               str     Bias section for quadrant C
DAC0     -9.0002,-8.961                                       str     [V] set value, measured value
DAC4     5.9998,6.0437                                        str     [V] set value, measured value
CLOCK3   -2.0001,3.9999                                       str     [V] high rail, low rail
OFFSET0  0.4000000059604645,-8.961                            str     [V] set value, measured value
DETSECC  [1:2057, 2065:4128]                                  str     Detector section for quadrant C
PRRSECC  [8:2064, 4194:4194]                                  str     Row prescan section for quadrant C
DAC11    -25.0003,-24.9312                                    str     [V] set value, measured value
DAC5     5.9998,6.0543                                        str     [V] set value, measured value
ORSECD   [2193:4249, 2098:2129]                               str     Row bias section for quadrant D
PGAGAIN  3                                                    int     Controller gain
AMPSECA  [1:2057, 1:2064]                                     str     AMP section for quadrant A
OFFSET1  0.4000000059604645,-8.9816                           str     [V] set value, measured value
PRESECC  [1:7, 2130:4193]                                     str     Prescan section for quadrant C
CLOCK17  7.9998,0.0                                           str     [V] high rail, low rail
CPUTEMP  54.4101                                              float   [deg C] CCD controller CPU temperature
TRIMSECC [8:2064, 2130:4193]                                  str     Trim section for quadrant C
PRESECB  [4250:4256, 2:2065]                                  str     Prescan section for quadrant B
DATASECD [2193:4249, 2130:4193]                               str     Data section for quadrant D
BIASSECB [2129:2192, 2:2065]                                  str     Bias section for quadrant B
AMPSECC  [1:2057, 4128:2065]                                  str     AMP section for quadrant C
DETECTOR LBNL-PE-21                                           str     Detector (ccd) identification
CRYOPRES 7.008e-08                                            str     [mb] Cryostat pressure (IP)
ORSECA   [8:2064, 2066:2097]                                  str     Row overscan section for quadrant A
REQTIME  1860.0                                               float   [s] Requested exposure time
OBSID    kp4m20220114t110417                                  str     Unique observation identifier
PROCTYPE RAW                                                  str     Data processing level
PRODTYPE image                                                str     Data product type
CHECKSUM 3W9aAU7W3U7aAU7W                                     str     HDU checksum updated 2022-01-14T11:15:03
DATASUM  2583478185                                           str     data unit checksum updated 2022-01-14T11:15:03
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 4256x4194]

HDU04
-----

EXTNAME = B4

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   4162                                                 int     number of rows in table
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
EXPID    118526                                               int     Exposure number
EXPFRAME 0                                                    int     Frame number
FRAMES   None                                                 Unknown Number of Frames in Archive
TILEID   4403                                                 int     DESI Tile ID
FIBASSGN /data/tiles/SVN_tiles/004/fiberassign-004403.fits.gz str     Fiber assign
FLAVOR   science                                              str     Observation type
SEQUENCE _Split                                               str     OCS Sequence name
PURPOSE  Main Survey                                          str     Purpose of observing night
PROGRAM  DARK                                                 str     Program name
PROPID   2020B-5000                                           str     Proposal ID
OBSERVER Jessica Chellino, Corentin Ravoux                    str     Names of observers
LEAD     Martin Landriau                                      str     Lead observer
INSTRUME DESI                                                 str     Instrument name
OBSERVAT KPNO                                                 str     Observatory name
OBS-LAT  31.96403                                             str     [deg] Observatory latitude
OBS-LONG -111.59989                                           str     [deg] Observatory east longitude
OBS-ELEV 2097.0                                               float   [m] Observatory elevation
TELESCOP KPNO 4.0-m telescope                                 str     Telescope name
CORRCTOR DESI Corrector                                       str     Corrector Identification
NIGHT    20220113                                             int     Observing night
TIMESYS  UTC                                                  str     Time system used for date-obs
DATE-OBS 2022-01-14T11:04:17.824419072                        str     [UTC] Observation data and start tim
TIME-OBS 2022-01-14T11:04:17.824419072                        str     [UTC] Observation start time
MJD-OBS  59593.46131741                                       float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:04:18.610806                           str     Time shutter opened
ST       11:13:28.580000                                      str     Local Sidereal time at observation start (HH:MM
EXPTIME  579.164                                              float   [s] Actual exposure time
REQRA    170.239                                              float   [deg] Requested right ascension (observer input
REQDEC   -7.093                                               float   [deg] Requested declination (observer input)
FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                   str     Telescope focus settings
VCCD     ON                                                   str     True (ON) if CCD voltage is on
VCCDON   2022-01-10T20:55:39.335356                           str     Time when CCD voltage was turned on
VCCDSEC  310754.5                                             float   [s] CCD on time in seconds
TRUSTEMP 12.267                                               float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.675                                               float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                               float   Epoch of observation
MOUNTAZ  176.725567                                           float   [deg] Mount azimuth angle
MOUNTDEC -7.102329                                            float   [deg] Mount declination
MOUNTEL  50.883914                                            float   [deg] Mount elevation angle
MOUNTHA  -2.081118                                            float   [deg] Mount hour angle
SKYDEC   -7.102329                                            float   [deg] Telescope declination (pointing on sky)
SKYRA    170.24163                                            float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.102329                                            float   [deg] Target declination (to TCS)
TARGTRA  170.24163                                            float   [deg] Target right ascension (to TCS)
USEETC   T                                                    bool    ETC data available if true
USESKY   T                                                    bool    DOS Control: use Sky Monitor
USEFOCUS T                                                    bool    DOS Control: use focus
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                              str     Hexapod trim values
USEROTAT T                                                    bool    DOS Control: use rotator
ROTOFFST 138.8                                                float   [arcsec] Rotator offset
ROTENBLD T                                                    bool    Rotator enabled
ROTRATE  0.513                                                float   [arcsec/min] Rotator rate
USEGUIDR T                                                    bool    DOS Control: use guider
USEDONUT T                                                    bool    DOS Control: use donuts
SPECGRPH 4                                                    int     Spectrograph logical name (SP)
SPECID   1                                                    int     Spectrograph serial number (SM)
FEEBOX   lbnl066                                              str     CCD Controller serial number
VESSEL   3                                                    int     Cryostat serial number
FEEVER   v20160312                                            str     CCD Controller version
DETFLVER FAILED: invalid argument for get command             str     CCD Controller detector f
FEEPOWER ON                                                   str     FEE power status
FEEDMASK 2134851391                                           int     FEE dac mask
FEECMASK 1048575                                              int     FEE clk mask
CCDTEMP  850.0                                                float   [deg C] CCD controller CCD temperature
RADESYS  FK5                                                  str     Coordinate reference frame of major/minor axes
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
CLOCK7   6.9999,-2.0001                                       str     [V] high rail, low rail
PGAGAIN  5                                                    int     Controller gain
DAC17    -0.0,0.1098                                          str     [V] set value, measured value
DAC7     0.0,-0.0263                                          str     [V] set value, measured value
DAC5     0.0,0.0105                                           str     [V] set value, measured value
DETSECD  [2049:4096, 2049:4096]                               str     Detector section for quadrant D
CLOCK1   3.9999,-4.0002                                       str     [V] high rail, low rail
DAC13    -5.0006,-5.0232                                      str     [V] set value, measured value
DAC4     0.0,-0.0263                                          str     [V] set value, measured value
CASETEMP 56.4919                                              float   [deg C] CCD controller case temperature
TRIMSECA [5:2052, 2:2049]                                     str     Trim section for quadrant A
DETSECB  [2049:4096, 1:2048]                                  str     Detector section for quadrant B
CCDPREP  purge,clear                                          str     CCD prep actions
AMPSECB  [2049:4096, 2048:1]                                  str     AMP section for quadrant B
BIASSECA [2053:2116, 2:2049]                                  str     Bias section for quadrant A
CLOCK3   6.9999,-2.0001                                       str     [V] high rail, low rail
DAC0     15.9998,15.7693                                      str     [V] set value, measured value
DAC3     15.9998,15.965                                       str     [V] set value, measured value
CLOCK2   3.9999,-4.0002                                       str     [V] high rail, low rail
DETSECA  [1:2048, 1:2048]                                     str     Detector section for quadrant A
BIASSECB [2117:2180, 2:2049]                                  str     Bias section for quadrant B
PRESECC  [1:4, 2114:4161]                                     str     Prescan section for quadrant C
CCDSECA  [1:2048, 1:2048]                                     str     CCD section for quadrant A
PRRSECA  [5:2052, 1:1]                                        str     Row prescan section for quadrant A
ORSECD   [2181:4228, 2082:2113]                               str     Row bias section for quadrant D
PRRSECC  [5:2052, 4162:4162]                                  str     Row prescan section for quadrant C
PRESECA  [1:4, 2:2049]                                        str     Prescan section for quadrant A
DATASECC [5:2052, 2114:4161]                                  str     Data section for quadrant C
CLOCK8   3.0,-7.0002                                          str     [V] high rail, low rail
CCDNAME  CCDSM1B                                              str     CCD name
DATASECB [2181:4228, 2:2049]                                  str     Data section for quadrant B
CRYOPRES 7.008e-08                                            str     [mb] Cryostat pressure (IP)
CRYOTEMP 163.044                                              float   [deg K] Cryostat CCD temperature
OFFSET2  -1.5,15.8414                                         str     [V] set value, measured value
CLOCK10  3.0,-7.0002                                          str     [V] high rail, low rail
TRIMSECB [2181:4228, 2:2049]                                  str     Trim section for quadrant B
AMPSECD  [4096:2049, 4096:2049]                               str     AMP section for quadrant D
CLOCK4   3.9999,-4.0002                                       str     [V] high rail, low rail
DAC10    26.9998,26.3707                                      str     [V] set value, measured value
OFFSET1  -1.5,15.8002                                         str     [V] set value, measured value
DAC15    19.9997,19.9888                                      str     [V] set value, measured value
BIASSECC [2053:2116, 2114:4161]                               str     Bias section for quadrant C
SETTINGS detectors_sm_20210128.json                           str     Name of DESI CCD settings file
CLOCK6   3.9999,-4.0002                                       str     [V] high rail, low rail
CLOCK14  3.0,-7.0002                                          str     [V] high rail, low rail
TRIMSECD [2181:4228, 2114:4161]                               str     Trim section for quadrant D
DAC11    26.9998,26.7417                                      str     [V] set value, measured value
OFFSET4  -1.100000023841858,-0.021                            str     [V] set value, measured value
PRRSECB  [2181:4228, 1:1]                                     str     Row prescan section for quadrant B
CAMERA   b4                                                   str     Camera name
AMPSECC  [2048:1, 2049:4096]                                  str     AMP section for quadrant C
CPUTEMP  56.2558                                              float   [deg C] CCD controller CPU temperature
CLOCK9   3.0,-7.0002                                          str     [V] high rail, low rail
CCDCFG   default_sta_20210128.cfg                             str     CCD configuration file
OFFSET5  -1.100000023841858,0.0105                            str     [V] set value, measured value
BIASSECD [2117:2180, 2114:4161]                               str     Bias section for quadrant D
DAC16    0.0,65.0496                                          str     [V] set value, measured value
DAC9     26.9998,27.0236                                      str     [V] set value, measured value
DAC12    4.9997,5.0336                                        str     [V] set value, measured value
AMPSECA  [1:2048, 1:2048]                                     str     AMP section for quadrant A
DAC6     0.0,-0.021                                           str     [V] set value, measured value
DETECTOR sn17986                                              str     Detector (ccd) identification
DAC1     15.9998,15.8002                                      str     [V] set value, measured value
CLOCK18  3.9999,-4.0002                                       str     [V] high rail, low rail
CCDSIZE  4162,4232                                            str     CCD size in pixels (rows, columns)
CLOCK15  0.0,0.0                                              str     [V] high rail, low rail
CCDTMING flatdark_sta_timing.txt                              str     CCD timing file
PRESECB  [4229:4232, 2:2049]                                  str     Prescan section for quadrant B
DIGITIME 54.7853                                              float   [s] Time to digitize image
CCDSECD  [2049:4096, 2049:4096]                               str     CCD section for quadrant D
OFFSET0  -1.5,15.7796                                         str     [V] set value, measured value
DAC2     15.9998,15.8517                                      str     [V] set value, measured value
OFFSET3  -1.5,15.9444                                         str     [V] set value, measured value
PRESECD  [4229:4232, 2114:4161]                               str     Prescan section for quadrant D
OFFSET7  -1.100000023841858,-0.021                            str     [V] set value, measured value
CLOCK17  3.9999,-4.0002                                       str     [V] high rail, low rail
CLOCK11  0.0,0.0                                              str     [V] high rail, low rail
OFFSET6  -1.100000023841858,-0.0316                           str     [V] set value, measured value
TRIMSECC [5:2052, 2114:4161]                                  str     Trim section for quadrant C
CLOCK12  3.0,-7.0002                                          str     [V] high rail, low rail
DELAYS   13, 13, 25, 25, 8, 3000, 7, 7, 400, 7                str     [10] Delay settings
CLOCK0   3.9999,-4.0002                                       str     [V] high rail, low rail
CLOCK5   3.9999,-4.0002                                       str     [V] high rail, low rail
CDSPARMS 400, 400, 8, 1000                                    str     CDS parameters
CCDSECC  [1:2048, 2049:4096]                                  str     CCD section for quadrant C
CCDSECB  [2049:4096, 1:2048]                                  str     CCD section for quadrant B
ORSECA   [5:2052, 2050:2081]                                  str     Row overscan section for quadrant A
DATASECD [2181:4228, 2114:4161]                               str     Data section for quadrant D
DETSECC  [1:2048, 2049:4096]                                  str     Detector section for quadrant C
DATASECA [5:2052, 2:2049]                                     str     Data section for quadrant A
BLDTIME  0.3529                                               float   [s] Time to build image
DAC14    0.0,0.78                                             str     [V] set value, measured value
ORSECC   [5:2052, 2082:2113]                                  str     Row overscan section for quadrant C
PRRSECD  [2181:4228, 4162:4162]                               str     Row prescan section for quadrant D
CLOCK16  0.0,0.0                                              str     [V] high rail, low rail
CLOCK13  3.0,-7.0002                                          str     [V] high rail, low rail
ORSECB   [2181:4228, 2050:2081]                               str     Row overscan section for quadrant B
DAC8     26.9998,26.8752                                      str     [V] set value, measured value
REQTIME  1860.0                                               float   [s] Requested exposure time
OBSID    kp4m20220114t110417                                  str     Unique observation identifier
PROCTYPE RAW                                                  str     Data processing level
PRODTYPE image                                                str     Data product type
CHECKSUM 9aAPGS6O9YAOGY5O                                     str     HDU checksum updated 2022-01-14T11:15:04
DATASUM  808617780                                            str     data unit checksum updated 2022-01-14T11:15:04
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 4232x4162]

HDU05
-----

EXTNAME = Z9

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   4194                                                 int     number of rows in table
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
EXPID    118526                                               int     Exposure number
EXPFRAME 0                                                    int     Frame number
FRAMES   None                                                 Unknown Number of Frames in Archive
TILEID   4403                                                 int     DESI Tile ID
FIBASSGN /data/tiles/SVN_tiles/004/fiberassign-004403.fits.gz str     Fiber assign
FLAVOR   science                                              str     Observation type
SEQUENCE _Split                                               str     OCS Sequence name
PURPOSE  Main Survey                                          str     Purpose of observing night
PROGRAM  DARK                                                 str     Program name
PROPID   2020B-5000                                           str     Proposal ID
OBSERVER Jessica Chellino, Corentin Ravoux                    str     Names of observers
LEAD     Martin Landriau                                      str     Lead observer
INSTRUME DESI                                                 str     Instrument name
OBSERVAT KPNO                                                 str     Observatory name
OBS-LAT  31.96403                                             str     [deg] Observatory latitude
OBS-LONG -111.59989                                           str     [deg] Observatory east longitude
OBS-ELEV 2097.0                                               float   [m] Observatory elevation
TELESCOP KPNO 4.0-m telescope                                 str     Telescope name
CORRCTOR DESI Corrector                                       str     Corrector Identification
NIGHT    20220113                                             int     Observing night
TIMESYS  UTC                                                  str     Time system used for date-obs
DATE-OBS 2022-01-14T11:04:17.858990080                        str     [UTC] Observation data and start tim
TIME-OBS 2022-01-14T11:04:17.858990080                        str     [UTC] Observation start time
MJD-OBS  59593.46131781                                       float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:04:18.624533                           str     Time shutter opened
ST       11:13:28.609999                                      str     Local Sidereal time at observation start (HH:MM
EXPTIME  579.103                                              float   [s] Actual exposure time
REQRA    170.239                                              float   [deg] Requested right ascension (observer input
REQDEC   -7.093                                               float   [deg] Requested declination (observer input)
FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                   str     Telescope focus settings
VCCD     ON                                                   str     True (ON) if CCD voltage is on
VCCDON   2022-01-10T20:55:43.758381                           str     Time when CCD voltage was turned on
VCCDSEC  310751.8                                             float   [s] CCD on time in seconds
TRUSTEMP 12.267                                               float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.675                                               float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                               float   Epoch of observation
MOUNTAZ  176.725567                                           float   [deg] Mount azimuth angle
MOUNTDEC -7.102329                                            float   [deg] Mount declination
MOUNTEL  50.883914                                            float   [deg] Mount elevation angle
MOUNTHA  -2.081118                                            float   [deg] Mount hour angle
SKYDEC   -7.102329                                            float   [deg] Telescope declination (pointing on sky)
SKYRA    170.24163                                            float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.102329                                            float   [deg] Target declination (to TCS)
TARGTRA  170.24163                                            float   [deg] Target right ascension (to TCS)
USEETC   T                                                    bool    ETC data available if true
USESKY   T                                                    bool    DOS Control: use Sky Monitor
USEFOCUS T                                                    bool    DOS Control: use focus
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                              str     Hexapod trim values
USEROTAT T                                                    bool    DOS Control: use rotator
ROTOFFST 138.8                                                float   [arcsec] Rotator offset
ROTENBLD T                                                    bool    Rotator enabled
ROTRATE  0.513                                                float   [arcsec/min] Rotator rate
USEGUIDR T                                                    bool    DOS Control: use guider
USEDONUT T                                                    bool    DOS Control: use donuts
SPECGRPH 9                                                    int     Spectrograph logical name (SP)
SPECID   3                                                    int     Spectrograph serial number (SM)
FEEBOX   lbnl060                                              str     CCD Controller serial number
VESSEL   4                                                    int     Cryostat serial number
FEEVER   v20160312                                            str     CCD Controller version
DETFLVER FAILED: invalid argument for get command             str     CCD Controller detector f
FEEPOWER ON                                                   str     FEE power status
FEEDMASK 2134851391                                           int     FEE dac mask
FEECMASK 1048575                                              int     FEE clk mask
CCDTEMP  -136.0762                                            float   [deg C] CCD controller CCD temperature
RADESYS  FK5                                                  str     Coordinate reference frame of major/minor axes
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
CDSPARMS 400, 400, 8, 2000                                    str     CDS parameters
CLOCK1   9.9999,0.0                                           str     [V] high rail, low rail
CLOCK3   -2.0001,3.9999                                       str     [V] high rail, low rail
BIASSECC [2065:2128, 2130:4193]                               str     Bias section for quadrant C
AMPSECA  [1:2057, 1:2064]                                     str     AMP section for quadrant A
DAC4     5.9998,6.0437                                        str     [V] set value, measured value
DETECTOR M1-22                                                str     Detector (ccd) identification
CLOCK2   9.9999,0.0                                           str     [V] high rail, low rail
OFFSET6  2.0,6.0437                                           str     [V] set value, measured value
DAC3     -9.0002,-8.9713                                      str     [V] set value, measured value
ORSECC   [8:2064, 2098:2129]                                  str     Row overscan section for quadrant C
CLOCK10  9.9992,2.9993                                        str     [V] high rail, low rail
DETSECA  [1:2057, 1:2064]                                     str     Detector section for quadrant A
CCDTMING flatdark_lbnl_timing.txt                             str     CCD timing file
PRRSECD  [2193:4249, 4194:4194]                               str     Row prescan section for quadrant D
PRRSECB  [2193:4249, 1:1]                                     str     Row prescan section for quadrant B
OFFSET4  2.0,6.0437                                           str     [V] set value, measured value
CCDCFG   default_lbnl_20210128.cfg                            str     CCD configuration file
DETSECB  [2058:4114, 1:2064]                                  str     Detector section for quadrant B
ORSECA   [8:2064, 2066:2097]                                  str     Row overscan section for quadrant A
DAC2     -9.0002,-8.9507                                      str     [V] set value, measured value
CLOCK8   9.9992,2.9993                                        str     [V] high rail, low rail
DELAYS   20, 20, 25, 40, 7, 3000, 7, 7, 400, 7                str     [10] Delay settings
DAC0     -9.0002,-8.9507                                      str     [V] set value, measured value
DAC11    -25.0003,-24.7383                                    str     [V] set value, measured value
CCDSECC  [1:2057, 2065:4128]                                  str     CCD section for quadrant C
PGAGAIN  3                                                    int     Controller gain
DAC7     5.9998,6.0122                                        str     [V] set value, measured value
CPUTEMP  58.2246                                              float   [deg C] CCD controller CPU temperature
PRESECC  [1:7, 2130:4193]                                     str     Prescan section for quadrant C
TRIMSECB [2193:4249, 2:2065]                                  str     Trim section for quadrant B
DAC6     5.9998,6.049                                         str     [V] set value, measured value
SETTINGS detectors_sm_20210128.json                           str     Name of DESI CCD settings file
CCDSECB  [2058:4114, 1:2064]                                  str     CCD section for quadrant B
BIASSECA [2065:2128, 2:2065]                                  str     Bias section for quadrant A
CLOCK17  9.0,0.9999                                           str     [V] high rail, low rail
CLOCK0   9.9999,0.0                                           str     [V] high rail, low rail
ORSECB   [2193:4249, 2066:2097]                               str     Row overscan section for quadrant B
TRIMSECA [8:2064, 2:2065]                                     str     Trim section for quadrant A
CLOCK16  9.9999,3.0                                           str     [V] high rail, low rail
DETSECC  [1:2057, 2065:4128]                                  str     Detector section for quadrant C
CLOCK4   9.9999,0.0                                           str     [V] high rail, low rail
BIASSECB [2129:2192, 2:2065]                                  str     Bias section for quadrant B
CLOCK5   9.9999,0.0                                           str     [V] high rail, low rail
AMPSECC  [1:2057, 4128:2065]                                  str     AMP section for quadrant C
ORSECD   [2193:4249, 2098:2129]                               str     Row bias section for quadrant D
CLOCK12  9.9992,2.9993                                        str     [V] high rail, low rail
CCDPREP  purge,clear                                          str     CCD prep actions
DAC1     -9.0002,-8.9919                                      str     [V] set value, measured value
DAC5     5.9998,6.0227                                        str     [V] set value, measured value
DATASECA [8:2064, 2:2065]                                     str     Data section for quadrant A
OFFSET5  2.0,6.0227                                           str     [V] set value, measured value
DAC16    39.9961,39.501                                       str     [V] set value, measured value
CLOCK18  9.0,0.9999                                           str     [V] high rail, low rail
CCDSECD  [2058:4114, 2065:4128]                               str     CCD section for quadrant D
DIGITIME 56.4486                                              float   [s] Time to digitize image
OFFSET7  2.0,6.0122                                           str     [V] set value, measured value
BIASSECD [2129:2192, 2130:4193]                               str     Bias section for quadrant D
CLOCK15  9.9992,2.9993                                        str     [V] high rail, low rail
CLOCK13  9.9992,2.9993                                        str     [V] high rail, low rail
CCDNAME  CCDSM3Z                                              str     CCD name
PRRSECA  [8:2064, 1:1]                                        str     Row prescan section for quadrant A
CAMERA   z9                                                   str     Camera name
TRIMSECC [8:2064, 2130:4193]                                  str     Trim section for quadrant C
PRRSECC  [8:2064, 4194:4194]                                  str     Row prescan section for quadrant C
OFFSET2  0.4000000059604645,-8.9507                           str     [V] set value, measured value
CLOCK7   -2.0001,3.9999                                       str     [V] high rail, low rail
DATASECC [8:2064, 2130:4193]                                  str     Data section for quadrant C
CASETEMP 58.0915                                              float   [deg C] CCD controller case temperature
PRESECD  [4250:4256, 2130:4193]                               str     Prescan section for quadrant D
DETSECD  [2058:4114, 2065:4128]                               str     Detector section for quadrant D
CCDSECA  [1:2057, 1:2064]                                     str     CCD section for quadrant A
CRYOTEMP 139.962                                              float   [deg K] Cryostat CCD temperature
DAC13    0.0,0.0594                                           str     [V] set value, measured value
TRIMSECD [2193:4249, 2130:4193]                               str     Trim section for quadrant D
DAC9     -25.0003,-25.3319                                    str     [V] set value, measured value
CCDSIZE  4194,4256                                            str     CCD size in pixels (rows, columns)
DAC8     -25.0003,-25.0944                                    str     [V] set value, measured value
AMPSECB  [4114:2058, 1:2064]                                  str     AMP section for quadrant B
DATASECB [2193:4249, 2:2065]                                  str     Data section for quadrant B
OFFSET3  0.4000000059604645,-8.9816                           str     [V] set value, measured value
DATASECD [2193:4249, 2130:4193]                               str     Data section for quadrant D
BLDTIME  0.3535                                               float   [s] Time to build image
CLOCK9   9.9992,2.9993                                        str     [V] high rail, low rail
CRYOPRES 5.451e-08                                            str     [mb] Cryostat pressure (IP)
PRESECA  [1:7, 2:2065]                                        str     Prescan section for quadrant A
OFFSET0  0.4000000059604645,-8.9507                           str     [V] set value, measured value
PRESECB  [4250:4256, 2:2065]                                  str     Prescan section for quadrant B
DAC12    0.0,0.0445                                           str     [V] set value, measured value
DAC10    -25.0003,-25.139                                     str     [V] set value, measured value
AMPSECD  [4114:2058, 4128:2065]                               str     AMP section for quadrant D
DAC17    20.0008,12.017                                       str     [V] set value, measured value
CLOCK6   9.9999,0.0                                           str     [V] high rail, low rail
OFFSET1  0.4000000059604645,-8.9919                           str     [V] set value, measured value
CLOCK14  9.9992,2.9993                                        str     [V] high rail, low rail
CLOCK11  9.9992,2.9993                                        str     [V] high rail, low rail
DAC15    0.0,0.0148                                           str     [V] set value, measured value
DAC14    0.0,0.0445                                           str     [V] set value, measured value
REQTIME  1860.0                                               float   [s] Requested exposure time
OBSID    kp4m20220114t110417                                  str     Unique observation identifier
PROCTYPE RAW                                                  str     Data processing level
PRODTYPE image                                                str     Data product type
CHECKSUM 8AaOAAXL1AaL8AUL                                     str     HDU checksum updated 2022-01-14T11:15:04
DATASUM  2861097645                                           str     data unit checksum updated 2022-01-14T11:15:04
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 4256x4194]

HDU06
-----

EXTNAME = R9

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   4194                                                 int     number of rows in table
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
EXPID    118526                                               int     Exposure number
EXPFRAME 0                                                    int     Frame number
FRAMES   None                                                 Unknown Number of Frames in Archive
TILEID   4403                                                 int     DESI Tile ID
FIBASSGN /data/tiles/SVN_tiles/004/fiberassign-004403.fits.gz str     Fiber assign
FLAVOR   science                                              str     Observation type
SEQUENCE _Split                                               str     OCS Sequence name
PURPOSE  Main Survey                                          str     Purpose of observing night
PROGRAM  DARK                                                 str     Program name
PROPID   2020B-5000                                           str     Proposal ID
OBSERVER Jessica Chellino, Corentin Ravoux                    str     Names of observers
LEAD     Martin Landriau                                      str     Lead observer
INSTRUME DESI                                                 str     Instrument name
OBSERVAT KPNO                                                 str     Observatory name
OBS-LAT  31.96403                                             str     [deg] Observatory latitude
OBS-LONG -111.59989                                           str     [deg] Observatory east longitude
OBS-ELEV 2097.0                                               float   [m] Observatory elevation
TELESCOP KPNO 4.0-m telescope                                 str     Telescope name
CORRCTOR DESI Corrector                                       str     Corrector Identification
NIGHT    20220113                                             int     Observing night
TIMESYS  UTC                                                  str     Time system used for date-obs
DATE-OBS 2022-01-14T11:04:17.858990080                        str     [UTC] Observation data and start tim
TIME-OBS 2022-01-14T11:04:17.858990080                        str     [UTC] Observation start time
MJD-OBS  59593.46131781                                       float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:04:18.624533                           str     Time shutter opened
ST       11:13:28.609999                                      str     Local Sidereal time at observation start (HH:MM
EXPTIME  579.103                                              float   [s] Actual exposure time
REQRA    170.239                                              float   [deg] Requested right ascension (observer input
REQDEC   -7.093                                               float   [deg] Requested declination (observer input)
FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                   str     Telescope focus settings
VCCD     ON                                                   str     True (ON) if CCD voltage is on
VCCDON   2022-01-10T20:55:36.973983                           str     Time when CCD voltage was turned on
VCCDSEC  310758.6                                             float   [s] CCD on time in seconds
TRUSTEMP 12.267                                               float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.675                                               float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                               float   Epoch of observation
MOUNTAZ  176.725567                                           float   [deg] Mount azimuth angle
MOUNTDEC -7.102329                                            float   [deg] Mount declination
MOUNTEL  50.883914                                            float   [deg] Mount elevation angle
MOUNTHA  -2.081118                                            float   [deg] Mount hour angle
SKYDEC   -7.102329                                            float   [deg] Telescope declination (pointing on sky)
SKYRA    170.24163                                            float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.102329                                            float   [deg] Target declination (to TCS)
TARGTRA  170.24163                                            float   [deg] Target right ascension (to TCS)
USEETC   T                                                    bool    ETC data available if true
USESKY   T                                                    bool    DOS Control: use Sky Monitor
USEFOCUS T                                                    bool    DOS Control: use focus
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                              str     Hexapod trim values
USEROTAT T                                                    bool    DOS Control: use rotator
ROTOFFST 138.8                                                float   [arcsec] Rotator offset
ROTENBLD T                                                    bool    Rotator enabled
ROTRATE  0.513                                                float   [arcsec/min] Rotator rate
USEGUIDR T                                                    bool    DOS Control: use guider
USEDONUT T                                                    bool    DOS Control: use donuts
SPECGRPH 9                                                    int     Spectrograph logical name (SP)
SPECID   3                                                    int     Spectrograph serial number (SM)
FEEBOX   lbnl086                                              str     CCD Controller serial number
VESSEL   6                                                    int     Cryostat serial number
FEEVER   v20160312                                            str     CCD Controller version
DETFLVER FAILED: invalid argument for get command             str     CCD Controller detector f
FEEPOWER ON                                                   str     FEE power status
FEEDMASK 2134851391                                           int     FEE dac mask
FEECMASK 1048575                                              int     FEE clk mask
CCDTEMP  -134.2345                                            float   [deg C] CCD controller CCD temperature
RADESYS  FK5                                                  str     Coordinate reference frame of major/minor axes
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
DATASECC [8:2064, 2130:4193]                                  str     Data section for quadrant C
CLOCK18  9.0,0.9999                                           str     [V] high rail, low rail
DAC2     -9.0002,-8.9198                                      str     [V] set value, measured value
OFFSET0  0.4000000059604645,-8.8477                           str     [V] set value, measured value
CCDPREP  purge,clear                                          str     CCD prep actions
PRRSECA  [8:2064, 1:1]                                        str     Row prescan section for quadrant A
OFFSET1  0.4000000059604645,-8.9404                           str     [V] set value, measured value
CCDCFG   default_lbnl_20210128.cfg                            str     CCD configuration file
OFFSET3  0.4000000059604645,-8.9198                           str     [V] set value, measured value
DATASECD [2193:4249, 2130:4193]                               str     Data section for quadrant D
CLOCK17  9.0,0.9999                                           str     [V] high rail, low rail
CLOCK10  9.9992,2.9993                                        str     [V] high rail, low rail
PRESECB  [4250:4256, 2:2065]                                  str     Prescan section for quadrant B
CCDNAME  CCDSM3R                                              str     CCD name
DATASECA [8:2064, 2:2065]                                     str     Data section for quadrant A
DETECTOR M1-22-1                                              str     Detector (ccd) identification
ORSECB   [2193:4249, 2066:2097]                               str     Row overscan section for quadrant B
CLOCK14  9.9992,2.9993                                        str     [V] high rail, low rail
PRRSECC  [8:2064, 4194:4194]                                  str     Row prescan section for quadrant C
CLOCK13  9.9992,2.9993                                        str     [V] high rail, low rail
DAC1     -9.0002,-8.9404                                      str     [V] set value, measured value
CRYOPRES 1.265e-07                                            str     [mb] Cryostat pressure (IP)
OFFSET4  2.0,6.0437                                           str     [V] set value, measured value
AMPSECC  [1:2057, 4128:2065]                                  str     AMP section for quadrant C
CLOCK3   -2.0001,3.9999                                       str     [V] high rail, low rail
DETSECA  [1:2057, 1:2064]                                     str     Detector section for quadrant A
AMPSECD  [4114:2058, 4128:2065]                               str     AMP section for quadrant D
DAC0     -9.0002,-8.8477                                      str     [V] set value, measured value
CPUTEMP  57.9785                                              float   [deg C] CCD controller CPU temperature
CLOCK4   9.9999,0.0                                           str     [V] high rail, low rail
DAC13    0.0,-0.0148                                          str     [V] set value, measured value
CAMERA   r9                                                   str     Camera name
BLDTIME  0.3519                                               float   [s] Time to build image
CCDSECB  [2058:4114, 1:2064]                                  str     CCD section for quadrant B
DAC5     5.9998,6.0437                                        str     [V] set value, measured value
CLOCK6   9.9999,0.0                                           str     [V] high rail, low rail
TRIMSECC [8:2064, 2130:4193]                                  str     Trim section for quadrant C
CLOCK5   9.9999,0.0                                           str     [V] high rail, low rail
BIASSECD [2129:2192, 2130:4193]                               str     Bias section for quadrant D
DATASECB [2193:4249, 2:2065]                                  str     Data section for quadrant B
PRRSECD  [2193:4249, 4194:4194]                               str     Row prescan section for quadrant D
CRYOTEMP 163.02                                               float   [deg K] Cryostat CCD temperature
DETSECC  [1:2057, 2065:4128]                                  str     Detector section for quadrant C
DIGITIME 56.4529                                              float   [s] Time to digitize image
DAC7     5.9998,6.0332                                        str     [V] set value, measured value
CCDSECA  [1:2057, 1:2064]                                     str     CCD section for quadrant A
DAC14    0.0,-0.0148                                          str     [V] set value, measured value
ORSECC   [8:2064, 2098:2129]                                  str     Row overscan section for quadrant C
DAC8     -25.0003,-25.0499                                    str     [V] set value, measured value
ORSECA   [8:2064, 2066:2097]                                  str     Row overscan section for quadrant A
CLOCK0   9.9999,0.0                                           str     [V] high rail, low rail
CCDSIZE  4194,4256                                            str     CCD size in pixels (rows, columns)
DAC9     -25.0003,-24.8125                                    str     [V] set value, measured value
DETSECB  [2058:4114, 1:2064]                                  str     Detector section for quadrant B
SETTINGS detectors_sm_20210616.json                           str     Name of DESI CCD settings file
CASETEMP 58.8298                                              float   [deg C] CCD controller case temperature
DELAYS   20, 20, 25, 40, 7, 3000, 7, 7, 400, 7                str     [10] Delay settings
DAC3     -9.0002,-8.9095                                      str     [V] set value, measured value
DAC6     5.9998,6.0385                                        str     [V] set value, measured value
OFFSET7  2.0,6.0385                                           str     [V] set value, measured value
DAC11    -25.0003,-24.9757                                    str     [V] set value, measured value
CLOCK11  9.9992,2.9993                                        str     [V] high rail, low rail
PRRSECB  [2193:4249, 1:1]                                     str     Row prescan section for quadrant B
PGAGAIN  3                                                    int     Controller gain
CCDSECD  [2058:4114, 2065:4128]                               str     CCD section for quadrant D
AMPSECB  [4114:2058, 1:2064]                                  str     AMP section for quadrant B
BIASSECA [2065:2128, 2:2065]                                  str     Bias section for quadrant A
TRIMSECA [8:2064, 2:2065]                                     str     Trim section for quadrant A
CLOCK16  9.9999,3.0                                           str     [V] high rail, low rail
CLOCK8   9.9992,2.9993                                        str     [V] high rail, low rail
CLOCK12  9.9992,2.9993                                        str     [V] high rail, low rail
BIASSECB [2129:2192, 2:2065]                                  str     Bias section for quadrant B
TRIMSECD [2193:4249, 2130:4193]                               str     Trim section for quadrant D
ORSECD   [2193:4249, 2098:2129]                               str     Row bias section for quadrant D
CCDSECC  [1:2057, 2065:4128]                                  str     CCD section for quadrant C
DAC16    39.9961,39.5934                                      str     [V] set value, measured value
CCDTMING flatdark_lbnl_timing.txt                             str     CCD timing file
CLOCK9   9.9992,2.9993                                        str     [V] high rail, low rail
PRESECC  [1:7, 2130:4193]                                     str     Prescan section for quadrant C
CDSPARMS 400, 400, 8, 2000                                    str     CDS parameters
PRESECA  [1:7, 2:2065]                                        str     Prescan section for quadrant A
OFFSET6  2.0,6.0385                                           str     [V] set value, measured value
DAC17    20.0008,12.3464                                      str     [V] set value, measured value
DETSECD  [2058:4114, 2065:4128]                               str     Detector section for quadrant D
DAC15    0.0,-0.0445                                          str     [V] set value, measured value
OFFSET5  2.0,6.0437                                           str     [V] set value, measured value
CLOCK1   9.9999,0.0                                           str     [V] high rail, low rail
PRESECD  [4250:4256, 2130:4193]                               str     Prescan section for quadrant D
DAC10    -25.0003,-24.946                                     str     [V] set value, measured value
BIASSECC [2065:2128, 2130:4193]                               str     Bias section for quadrant C
DAC12    0.0,-0.0297                                          str     [V] set value, measured value
AMPSECA  [1:2057, 1:2064]                                     str     AMP section for quadrant A
OFFSET2  0.4000000059604645,-8.9301                           str     [V] set value, measured value
CLOCK15  9.9992,2.9993                                        str     [V] high rail, low rail
CLOCK2   9.9999,0.0                                           str     [V] high rail, low rail
DAC4     5.9998,6.0437                                        str     [V] set value, measured value
TRIMSECB [2193:4249, 2:2065]                                  str     Trim section for quadrant B
CLOCK7   -2.0001,3.9999                                       str     [V] high rail, low rail
REQTIME  1860.0                                               float   [s] Requested exposure time
OBSID    kp4m20220114t110417                                  str     Unique observation identifier
PROCTYPE RAW                                                  str     Data processing level
PRODTYPE image                                                str     Data product type
CHECKSUM ToFnUm9lTmElTm9l                                     str     HDU checksum updated 2022-01-14T11:15:04
DATASUM  3398252125                                           str     data unit checksum updated 2022-01-14T11:15:04
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 4256x4194]

HDU07
-----

EXTNAME = B9

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   4162                                                 int     number of rows in table
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
EXPID    118526                                               int     Exposure number
EXPFRAME 0                                                    int     Frame number
FRAMES   None                                                 Unknown Number of Frames in Archive
TILEID   4403                                                 int     DESI Tile ID
FIBASSGN /data/tiles/SVN_tiles/004/fiberassign-004403.fits.gz str     Fiber assign
FLAVOR   science                                              str     Observation type
SEQUENCE _Split                                               str     OCS Sequence name
PURPOSE  Main Survey                                          str     Purpose of observing night
PROGRAM  DARK                                                 str     Program name
PROPID   2020B-5000                                           str     Proposal ID
OBSERVER Jessica Chellino, Corentin Ravoux                    str     Names of observers
LEAD     Martin Landriau                                      str     Lead observer
INSTRUME DESI                                                 str     Instrument name
OBSERVAT KPNO                                                 str     Observatory name
OBS-LAT  31.96403                                             str     [deg] Observatory latitude
OBS-LONG -111.59989                                           str     [deg] Observatory east longitude
OBS-ELEV 2097.0                                               float   [m] Observatory elevation
TELESCOP KPNO 4.0-m telescope                                 str     Telescope name
CORRCTOR DESI Corrector                                       str     Corrector Identification
NIGHT    20220113                                             int     Observing night
TIMESYS  UTC                                                  str     Time system used for date-obs
DATE-OBS 2022-01-14T11:04:17.858990080                        str     [UTC] Observation data and start tim
TIME-OBS 2022-01-14T11:04:17.858990080                        str     [UTC] Observation start time
MJD-OBS  59593.46131781                                       float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:04:18.624533                           str     Time shutter opened
ST       11:13:28.609999                                      str     Local Sidereal time at observation start (HH:MM
EXPTIME  579.103                                              float   [s] Actual exposure time
REQRA    170.239                                              float   [deg] Requested right ascension (observer input
REQDEC   -7.093                                               float   [deg] Requested declination (observer input)
FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                   str     Telescope focus settings
VCCD     ON                                                   str     True (ON) if CCD voltage is on
VCCDON   2022-01-10T20:55:39.344921                           str     Time when CCD voltage was turned on
VCCDSEC  310754.5                                             float   [s] CCD on time in seconds
TRUSTEMP 12.267                                               float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.675                                               float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                               float   Epoch of observation
MOUNTAZ  176.725567                                           float   [deg] Mount azimuth angle
MOUNTDEC -7.102329                                            float   [deg] Mount declination
MOUNTEL  50.883914                                            float   [deg] Mount elevation angle
MOUNTHA  -2.081118                                            float   [deg] Mount hour angle
SKYDEC   -7.102329                                            float   [deg] Telescope declination (pointing on sky)
SKYRA    170.24163                                            float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.102329                                            float   [deg] Target declination (to TCS)
TARGTRA  170.24163                                            float   [deg] Target right ascension (to TCS)
USEETC   T                                                    bool    ETC data available if true
USESKY   T                                                    bool    DOS Control: use Sky Monitor
USEFOCUS T                                                    bool    DOS Control: use focus
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                              str     Hexapod trim values
USEROTAT T                                                    bool    DOS Control: use rotator
ROTOFFST 138.8                                                float   [arcsec] Rotator offset
ROTENBLD T                                                    bool    Rotator enabled
ROTRATE  0.513                                                float   [arcsec/min] Rotator rate
USEGUIDR T                                                    bool    DOS Control: use guider
USEDONUT T                                                    bool    DOS Control: use donuts
SPECGRPH 9                                                    int     Spectrograph logical name (SP)
SPECID   3                                                    int     Spectrograph serial number (SM)
FEEBOX   lbnl068                                              str     CCD Controller serial number
VESSEL   7                                                    int     Cryostat serial number
FEEVER   v20160312                                            str     CCD Controller version
DETFLVER FAILED: invalid argument for get command             str     CCD Controller detector f
FEEPOWER ON                                                   str     FEE power status
FEEDMASK 2134851391                                           int     FEE dac mask
FEECMASK 1048575                                              int     FEE clk mask
CCDTEMP  850.0                                                float   [deg C] CCD controller CCD temperature
RADESYS  FK5                                                  str     Coordinate reference frame of major/minor axes
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
CLOCK6   3.9999,-4.0002                                       str     [V] high rail, low rail
CLOCK9   3.0,-7.0002                                          str     [V] high rail, low rail
DAC13    -5.0006,-5.3872                                      str     [V] set value, measured value
DATASECD [2181:4228, 2114:4161]                               str     Data section for quadrant D
CLOCK7   6.9999,-2.0001                                       str     [V] high rail, low rail
OFFSET6  -1.100000023841858,-0.0736                           str     [V] set value, measured value
DETECTOR sn22794                                              str     Detector (ccd) identification
DIGITIME 54.7849                                              float   [s] Time to digitize image
TRIMSECC [5:2052, 2114:4161]                                  str     Trim section for quadrant C
PRESECC  [1:4, 2114:4161]                                     str     Prescan section for quadrant C
CLOCK14  3.0,-7.0002                                          str     [V] high rail, low rail
CLOCK4   3.9999,-4.0002                                       str     [V] high rail, low rail
DETSECC  [1:2048, 2049:4096]                                  str     Detector section for quadrant C
AMPSECD  [4096:2049, 4096:2049]                               str     AMP section for quadrant D
CCDCFG   default_sta_20210128.cfg                             str     CCD configuration file
DAC8     26.9998,26.8752                                      str     [V] set value, measured value
CLOCK15  0.0,0.0                                              str     [V] high rail, low rail
CCDSECD  [2049:4096, 2049:4096]                               str     CCD section for quadrant D
CCDSECB  [2049:4096, 1:2048]                                  str     CCD section for quadrant B
CDSPARMS 400, 400, 8, 1000                                    str     CDS parameters
CLOCK18  3.9999,-4.0002                                       str     [V] high rail, low rail
PRRSECA  [5:2052, 1:1]                                        str     Row prescan section for quadrant A
BIASSECB [2117:2180, 2:2049]                                  str     Bias section for quadrant B
PRRSECB  [2181:4228, 1:1]                                     str     Row prescan section for quadrant B
DAC16    0.0,64.4028                                          str     [V] set value, measured value
DAC0     15.9998,16.0989                                      str     [V] set value, measured value
CCDTMING flatdark_sta_timing.txt                              str     CCD timing file
DETSECD  [2049:4096, 2049:4096]                               str     Detector section for quadrant D
DAC10    26.9998,26.9198                                      str     [V] set value, measured value
CASETEMP 59.9372                                              float   [deg C] CCD controller case temperature
CCDNAME  CCDSM3B                                              str     CCD name
CLOCK2   3.9999,-4.0002                                       str     [V] high rail, low rail
DAC6     0.0,-0.0684                                          str     [V] set value, measured value
OFFSET3  -1.5,16.2946                                         str     [V] set value, measured value
CCDSECA  [1:2048, 1:2048]                                     str     CCD section for quadrant A
ORSECD   [2181:4228, 2082:2113]                               str     Row bias section for quadrant D
CLOCK5   3.9999,-4.0002                                       str     [V] high rail, low rail
CAMERA   b9                                                   str     Camera name
CLOCK3   6.9999,-2.0001                                       str     [V] high rail, low rail
CLOCK1   3.9999,-4.0002                                       str     [V] high rail, low rail
DAC2     15.9998,16.2843                                      str     [V] set value, measured value
CPUTEMP  60.4394                                              float   [deg C] CCD controller CPU temperature
CLOCK13  3.0,-7.0002                                          str     [V] high rail, low rail
CCDSECC  [1:2048, 2049:4096]                                  str     CCD section for quadrant C
PRESECA  [1:4, 2:2049]                                        str     Prescan section for quadrant A
AMPSECB  [2049:4096, 2048:1]                                  str     AMP section for quadrant B
PRESECB  [4229:4232, 2:2049]                                  str     Prescan section for quadrant B
PRESECD  [4229:4232, 2114:4161]                               str     Prescan section for quadrant D
CLOCK8   3.0,-7.0002                                          str     [V] high rail, low rail
OFFSET1  -1.5,16.3358                                         str     [V] set value, measured value
PGAGAIN  5                                                    int     Controller gain
CLOCK11  0.0,0.0                                              str     [V] high rail, low rail
DAC15    19.9997,20.6648                                      str     [V] set value, measured value
DAC5     0.0,-0.0842                                          str     [V] set value, measured value
DATASECA [5:2052, 2:2049]                                     str     Data section for quadrant A
SETTINGS detectors_sm_20210128.json                           str     Name of DESI CCD settings file
DAC9     26.9998,26.623                                       str     [V] set value, measured value
OFFSET0  -1.5,16.1092                                         str     [V] set value, measured value
DAC1     15.9998,16.3358                                      str     [V] set value, measured value
DAC4     0.0,-0.0842                                          str     [V] set value, measured value
OFFSET7  -1.100000023841858,-0.0736                           str     [V] set value, measured value
CCDSIZE  4162,4232                                            str     CCD size in pixels (rows, columns)
DETSECB  [2049:4096, 1:2048]                                  str     Detector section for quadrant B
DAC7     0.0,-0.0736                                          str     [V] set value, measured value
CRYOTEMP 163.02                                               float   [deg K] Cryostat CCD temperature
CLOCK17  3.9999,-4.0002                                       str     [V] high rail, low rail
BIASSECC [2053:2116, 2114:4161]                               str     Bias section for quadrant C
PRRSECD  [2181:4228, 4162:4162]                               str     Row prescan section for quadrant D
BLDTIME  0.3516                                               float   [s] Time to build image
CCDPREP  purge,clear                                          str     CCD prep actions
DATASECC [5:2052, 2114:4161]                                  str     Data section for quadrant C
DAC12    4.9997,5.0128                                        str     [V] set value, measured value
CLOCK12  3.0,-7.0002                                          str     [V] high rail, low rail
DAC11    26.9998,26.7268                                      str     [V] set value, measured value
OFFSET5  -1.100000023841858,-0.0842                           str     [V] set value, measured value
AMPSECA  [1:2048, 1:2048]                                     str     AMP section for quadrant A
BIASSECD [2117:2180, 2114:4161]                               str     Bias section for quadrant D
DETSECA  [1:2048, 1:2048]                                     str     Detector section for quadrant A
CLOCK0   3.9999,-4.0002                                       str     [V] high rail, low rail
ORSECB   [2181:4228, 2050:2081]                               str     Row overscan section for quadrant B
DAC17    -0.0,0.0854                                          str     [V] set value, measured value
OFFSET4  -1.100000023841858,-0.0789                           str     [V] set value, measured value
AMPSECC  [2048:1, 2049:4096]                                  str     AMP section for quadrant C
DAC3     15.9998,16.2946                                      str     [V] set value, measured value
BIASSECA [2053:2116, 2:2049]                                  str     Bias section for quadrant A
TRIMSECD [2181:4228, 2114:4161]                               str     Trim section for quadrant D
DAC14    0.0,0.7904                                           str     [V] set value, measured value
ORSECC   [5:2052, 2082:2113]                                  str     Row overscan section for quadrant C
CLOCK10  3.0,-7.0002                                          str     [V] high rail, low rail
PRRSECC  [5:2052, 4162:4162]                                  str     Row prescan section for quadrant C
TRIMSECB [2181:4228, 2:2049]                                  str     Trim section for quadrant B
CRYOPRES 1.265e-07                                            str     [mb] Cryostat pressure (IP)
TRIMSECA [5:2052, 2:2049]                                     str     Trim section for quadrant A
CLOCK16  0.0,0.0                                              str     [V] high rail, low rail
ORSECA   [5:2052, 2050:2081]                                  str     Row overscan section for quadrant A
DATASECB [2181:4228, 2:2049]                                  str     Data section for quadrant B
DELAYS   13, 13, 25, 25, 8, 3000, 7, 7, 400, 7                str     [10] Delay settings
OFFSET2  -1.5,16.3152                                         str     [V] set value, measured value
REQTIME  1860.0                                               float   [s] Requested exposure time
OBSID    kp4m20220114t110417                                  str     Unique observation identifier
PROCTYPE RAW                                                  str     Data processing level
PRODTYPE image                                                str     Data product type
CHECKSUM GGDIH9DIGGDIG9DI                                     str     HDU checksum updated 2022-01-14T11:15:04
DATASUM  1851142029                                           str     data unit checksum updated 2022-01-14T11:15:04
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 4232x4162]

HDU08
-----

EXTNAME = Z8

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   4194                                                 int     number of rows in table
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
EXPID    118526                                               int     Exposure number
EXPFRAME 0                                                    int     Frame number
FRAMES   None                                                 Unknown Number of Frames in Archive
TILEID   4403                                                 int     DESI Tile ID
FIBASSGN /data/tiles/SVN_tiles/004/fiberassign-004403.fits.gz str     Fiber assign
FLAVOR   science                                              str     Observation type
SEQUENCE _Split                                               str     OCS Sequence name
PURPOSE  Main Survey                                          str     Purpose of observing night
PROGRAM  DARK                                                 str     Program name
PROPID   2020B-5000                                           str     Proposal ID
OBSERVER Jessica Chellino, Corentin Ravoux                    str     Names of observers
LEAD     Martin Landriau                                      str     Lead observer
INSTRUME DESI                                                 str     Instrument name
OBSERVAT KPNO                                                 str     Observatory name
OBS-LAT  31.96403                                             str     [deg] Observatory latitude
OBS-LONG -111.59989                                           str     [deg] Observatory east longitude
OBS-ELEV 2097.0                                               float   [m] Observatory elevation
TELESCOP KPNO 4.0-m telescope                                 str     Telescope name
CORRCTOR DESI Corrector                                       str     Corrector Identification
NIGHT    20220113                                             int     Observing night
TIMESYS  UTC                                                  str     Time system used for date-obs
DATE-OBS 2022-01-14T11:04:18.005188096                        str     [UTC] Observation data and start tim
TIME-OBS 2022-01-14T11:04:18.005188096                        str     [UTC] Observation start time
MJD-OBS  59593.4613195                                        float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:04:18.788872                           str     Time shutter opened
ST       11:13:28.760000                                      str     Local Sidereal time at observation start (HH:MM
EXPTIME  578.988                                              float   [s] Actual exposure time
REQRA    170.239                                              float   [deg] Requested right ascension (observer input
REQDEC   -7.093                                               float   [deg] Requested declination (observer input)
FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                   str     Telescope focus settings
VCCD     ON                                                   str     True (ON) if CCD voltage is on
VCCDON   2022-01-10T20:55:43.750210                           str     Time when CCD voltage was turned on
VCCDSEC  310751.8                                             float   [s] CCD on time in seconds
TRUSTEMP 12.267                                               float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.675                                               float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                               float   Epoch of observation
MOUNTAZ  176.725567                                           float   [deg] Mount azimuth angle
MOUNTDEC -7.102329                                            float   [deg] Mount declination
MOUNTEL  50.883914                                            float   [deg] Mount elevation angle
MOUNTHA  -2.081118                                            float   [deg] Mount hour angle
SKYDEC   -7.102329                                            float   [deg] Telescope declination (pointing on sky)
SKYRA    170.24163                                            float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.102329                                            float   [deg] Target declination (to TCS)
TARGTRA  170.24163                                            float   [deg] Target right ascension (to TCS)
USEETC   T                                                    bool    ETC data available if true
USESKY   T                                                    bool    DOS Control: use Sky Monitor
USEFOCUS T                                                    bool    DOS Control: use focus
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                              str     Hexapod trim values
USEROTAT T                                                    bool    DOS Control: use rotator
ROTOFFST 138.8                                                float   [arcsec] Rotator offset
ROTENBLD T                                                    bool    Rotator enabled
ROTRATE  0.513                                                float   [arcsec/min] Rotator rate
USEGUIDR T                                                    bool    DOS Control: use guider
USEDONUT T                                                    bool    DOS Control: use donuts
SPECGRPH 8                                                    int     Spectrograph logical name (SP)
SPECID   2                                                    int     Spectrograph serial number (SM)
FEEBOX   lbnl055                                              str     CCD Controller serial number
VESSEL   9                                                    int     Cryostat serial number
FEEVER   v20160312                                            str     CCD Controller version
DETFLVER FAILED: invalid argument for get command             str     CCD Controller detector f
FEEPOWER ON                                                   str     FEE power status
FEEDMASK 2134851391                                           int     FEE dac mask
FEECMASK 1048575                                              int     FEE clk mask
CCDTEMP  -136.1383                                            float   [deg C] CCD controller CCD temperature
RADESYS  FK5                                                  str     Coordinate reference frame of major/minor axes
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
CLOCK8   9.9992,2.9993                                        str     [V] high rail, low rail
OFFSET1  0.4000000059604645,-8.9713                           str     [V] set value, measured value
DAC7     5.9998,6.0069                                        str     [V] set value, measured value
DAC6     5.9998,5.9964                                        str     [V] set value, measured value
PRESECC  [1:7, 2130:4193]                                     str     Prescan section for quadrant C
CLOCK2   9.9999,0.0                                           str     [V] high rail, low rail
PRESECD  [4250:4256, 2130:4193]                               str     Prescan section for quadrant D
DELAYS   20, 20, 25, 40, 7, 3000, 7, 7, 400, 7                str     [10] Delay settings
CLOCK5   9.9999,0.0                                           str     [V] high rail, low rail
DAC12    0.0,-0.0148                                          str     [V] set value, measured value
ORSECA   [8:2064, 2066:2097]                                  str     Row overscan section for quadrant A
DAC8     -25.0003,-25.0796                                    str     [V] set value, measured value
CLOCK18  9.0,0.9999                                           str     [V] high rail, low rail
CLOCK14  9.9992,2.9993                                        str     [V] high rail, low rail
ORSECD   [2193:4249, 2098:2129]                               str     Row bias section for quadrant D
DATASECB [2193:4249, 2:2065]                                  str     Data section for quadrant B
PRESECB  [4250:4256, 2:2065]                                  str     Prescan section for quadrant B
OFFSET0  0.4000000059604645,-9.0331                           str     [V] set value, measured value
CRYOTEMP 139.937                                              float   [deg K] Cryostat CCD temperature
CLOCK6   9.9999,0.0                                           str     [V] high rail, low rail
AMPSECA  [1:2057, 1:2064]                                     str     AMP section for quadrant A
CCDTMING flatdark_lbnl_timing.txt                             str     CCD timing file
PRRSECA  [8:2064, 1:1]                                        str     Row prescan section for quadrant A
CLOCK16  9.9999,3.0                                           str     [V] high rail, low rail
OFFSET7  2.0,6.0017                                           str     [V] set value, measured value
CRYOPRES 1.377e-07                                            str     [mb] Cryostat pressure (IP)
CLOCK13  9.9992,2.9993                                        str     [V] high rail, low rail
DETSECA  [1:2057, 1:2064]                                     str     Detector section for quadrant A
DAC14    0.0,-0.0297                                          str     [V] set value, measured value
CLOCK10  9.9992,2.9993                                        str     [V] high rail, low rail
DAC13    0.0,-0.0297                                          str     [V] set value, measured value
DIGITIME 56.4552                                              float   [s] Time to digitize image
DATASECD [2193:4249, 2130:4193]                               str     Data section for quadrant D
CCDSIZE  4194,4256                                            str     CCD size in pixels (rows, columns)
AMPSECC  [1:2057, 4128:2065]                                  str     AMP section for quadrant C
CLOCK9   9.9992,2.9993                                        str     [V] high rail, low rail
DAC16    39.9961,39.4548                                      str     [V] set value, measured value
DAC4     5.9998,6.0437                                        str     [V] set value, measured value
CLOCK12  9.9992,2.9993                                        str     [V] high rail, low rail
PGAGAIN  3                                                    int     Controller gain
DAC10    -25.0003,-25.0648                                    str     [V] set value, measured value
ORSECC   [8:2064, 2098:2129]                                  str     Row overscan section for quadrant C
DETSECB  [2058:4114, 1:2064]                                  str     Detector section for quadrant B
PRRSECD  [2193:4249, 4194:4194]                               str     Row prescan section for quadrant D
DAC1     -9.0002,-8.9816                                      str     [V] set value, measured value
DAC3     -9.0002,-8.9816                                      str     [V] set value, measured value
DAC5     5.9998,6.0595                                        str     [V] set value, measured value
CCDSECC  [1:2057, 2065:4128]                                  str     CCD section for quadrant C
CLOCK1   9.9999,0.0                                           str     [V] high rail, low rail
CLOCK4   9.9999,0.0                                           str     [V] high rail, low rail
CLOCK17  9.0,0.9999                                           str     [V] high rail, low rail
CLOCK3   -2.0001,3.9999                                       str     [V] high rail, low rail
CCDCFG   default_lbnl_20210128.cfg                            str     CCD configuration file
DAC0     -9.0002,-9.0434                                      str     [V] set value, measured value
CDSPARMS 400, 400, 8, 2000                                    str     CDS parameters
DATASECA [8:2064, 2:2065]                                     str     Data section for quadrant A
BIASSECD [2129:2192, 2130:4193]                               str     Bias section for quadrant D
DETSECC  [1:2057, 2065:4128]                                  str     Detector section for quadrant C
OFFSET6  2.0,6.0017                                           str     [V] set value, measured value
PRRSECC  [8:2064, 4194:4194]                                  str     Row prescan section for quadrant C
BIASSECB [2129:2192, 2:2065]                                  str     Bias section for quadrant B
DETECTOR M1-42                                                str     Detector (ccd) identification
CCDNAME  CCDSM2Z                                              str     CCD name
AMPSECD  [4114:2058, 4128:2065]                               str     AMP section for quadrant D
TRIMSECD [2193:4249, 2130:4193]                               str     Trim section for quadrant D
DAC11    -25.0003,-25.3616                                    str     [V] set value, measured value
CPUTEMP  56.748                                               float   [deg C] CCD controller CPU temperature
DAC9     -25.0003,-25.3467                                    str     [V] set value, measured value
CLOCK11  9.9992,2.9993                                        str     [V] high rail, low rail
BIASSECA [2065:2128, 2:2065]                                  str     Bias section for quadrant A
AMPSECB  [4114:2058, 1:2064]                                  str     AMP section for quadrant B
DETSECD  [2058:4114, 2065:4128]                               str     Detector section for quadrant D
TRIMSECA [8:2064, 2:2065]                                     str     Trim section for quadrant A
OFFSET3  0.4000000059604645,-8.9713                           str     [V] set value, measured value
OFFSET4  2.0,6.0437                                           str     [V] set value, measured value
CLOCK15  9.9992,2.9993                                        str     [V] high rail, low rail
DAC2     -9.0002,-8.961                                       str     [V] set value, measured value
BIASSECC [2065:2128, 2130:4193]                               str     Bias section for quadrant C
DAC15    0.0,0.0                                              str     [V] set value, measured value
DATASECC [8:2064, 2130:4193]                                  str     Data section for quadrant C
SETTINGS detectors_sm_20210128.json                           str     Name of DESI CCD settings file
PRRSECB  [2193:4249, 1:1]                                     str     Row prescan section for quadrant B
TRIMSECC [8:2064, 2130:4193]                                  str     Trim section for quadrant C
OFFSET2  0.4000000059604645,-8.961                            str     [V] set value, measured value
BLDTIME  0.3523                                               float   [s] Time to build image
TRIMSECB [2193:4249, 2:2065]                                  str     Trim section for quadrant B
OFFSET5  2.0,6.0595                                           str     [V] set value, measured value
CCDSECA  [1:2057, 1:2064]                                     str     CCD section for quadrant A
CCDSECB  [2058:4114, 1:2064]                                  str     CCD section for quadrant B
CCDPREP  purge,clear                                          str     CCD prep actions
ORSECB   [2193:4249, 2066:2097]                               str     Row overscan section for quadrant B
CLOCK0   9.9999,0.0                                           str     [V] high rail, low rail
CAMERA   z8                                                   str     Camera name
DAC17    20.0008,12.2854                                      str     [V] set value, measured value
PRESECA  [1:7, 2:2065]                                        str     Prescan section for quadrant A
CLOCK7   -2.0001,3.9999                                       str     [V] high rail, low rail
CCDSECD  [2058:4114, 2065:4128]                               str     CCD section for quadrant D
CASETEMP 57.1072                                              float   [deg C] CCD controller case temperature
REQTIME  1860.0                                               float   [s] Requested exposure time
OBSID    kp4m20220114t110417                                  str     Unique observation identifier
PROCTYPE RAW                                                  str     Data processing level
PRODTYPE image                                                str     Data product type
CHECKSUM 2beY5ZdY2adY2YdY                                     str     HDU checksum updated 2022-01-14T11:15:04
DATASUM  1343001440                                           str     data unit checksum updated 2022-01-14T11:15:04
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 4256x4194]

HDU09
-----

EXTNAME = R8

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   4194                                                 int     number of rows in table
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
EXPID    118526                                               int     Exposure number
EXPFRAME 0                                                    int     Frame number
FRAMES   None                                                 Unknown Number of Frames in Archive
TILEID   4403                                                 int     DESI Tile ID
FIBASSGN /data/tiles/SVN_tiles/004/fiberassign-004403.fits.gz str     Fiber assign
FLAVOR   science                                              str     Observation type
SEQUENCE _Split                                               str     OCS Sequence name
PURPOSE  Main Survey                                          str     Purpose of observing night
PROGRAM  DARK                                                 str     Program name
PROPID   2020B-5000                                           str     Proposal ID
OBSERVER Jessica Chellino, Corentin Ravoux                    str     Names of observers
LEAD     Martin Landriau                                      str     Lead observer
INSTRUME DESI                                                 str     Instrument name
OBSERVAT KPNO                                                 str     Observatory name
OBS-LAT  31.96403                                             str     [deg] Observatory latitude
OBS-LONG -111.59989                                           str     [deg] Observatory east longitude
OBS-ELEV 2097.0                                               float   [m] Observatory elevation
TELESCOP KPNO 4.0-m telescope                                 str     Telescope name
CORRCTOR DESI Corrector                                       str     Corrector Identification
NIGHT    20220113                                             int     Observing night
TIMESYS  UTC                                                  str     Time system used for date-obs
DATE-OBS 2022-01-14T11:04:18.005188096                        str     [UTC] Observation data and start tim
TIME-OBS 2022-01-14T11:04:18.005188096                        str     [UTC] Observation start time
MJD-OBS  59593.4613195                                        float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:04:18.788872                           str     Time shutter opened
ST       11:13:28.760000                                      str     Local Sidereal time at observation start (HH:MM
EXPTIME  578.988                                              float   [s] Actual exposure time
REQRA    170.239                                              float   [deg] Requested right ascension (observer input
REQDEC   -7.093                                               float   [deg] Requested declination (observer input)
FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                   str     Telescope focus settings
VCCD     ON                                                   str     True (ON) if CCD voltage is on
VCCDON   2022-01-10T20:55:36.876421                           str     Time when CCD voltage was turned on
VCCDSEC  310758.3                                             float   [s] CCD on time in seconds
TRUSTEMP 12.267                                               float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.675                                               float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                               float   Epoch of observation
MOUNTAZ  176.725567                                           float   [deg] Mount azimuth angle
MOUNTDEC -7.102329                                            float   [deg] Mount declination
MOUNTEL  50.883914                                            float   [deg] Mount elevation angle
MOUNTHA  -2.081118                                            float   [deg] Mount hour angle
SKYDEC   -7.102329                                            float   [deg] Telescope declination (pointing on sky)
SKYRA    170.24163                                            float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.102329                                            float   [deg] Target declination (to TCS)
TARGTRA  170.24163                                            float   [deg] Target right ascension (to TCS)
USEETC   T                                                    bool    ETC data available if true
USESKY   T                                                    bool    DOS Control: use Sky Monitor
USEFOCUS T                                                    bool    DOS Control: use focus
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                              str     Hexapod trim values
USEROTAT T                                                    bool    DOS Control: use rotator
ROTOFFST 138.8                                                float   [arcsec] Rotator offset
ROTENBLD T                                                    bool    Rotator enabled
ROTRATE  0.513                                                float   [arcsec/min] Rotator rate
USEGUIDR T                                                    bool    DOS Control: use guider
USEDONUT T                                                    bool    DOS Control: use donuts
SPECGRPH 8                                                    int     Spectrograph logical name (SP)
SPECID   2                                                    int     Spectrograph serial number (SM)
FEEBOX   lbnl050                                              str     CCD Controller serial number
VESSEL   8                                                    int     Cryostat serial number
FEEVER   v20160312                                            str     CCD Controller version
DETFLVER FAILED: invalid argument for get command             str     CCD Controller detector f
FEEPOWER ON                                                   str     FEE power status
FEEDMASK 2134851391                                           int     FEE dac mask
FEECMASK 1048575                                              int     FEE clk mask
CCDTEMP  -135.2694                                            float   [deg C] CCD controller CCD temperature
RADESYS  FK5                                                  str     Coordinate reference frame of major/minor axes
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
DAC15    0.0,0.0148                                           str     [V] set value, measured value
CPUTEMP  60.4394                                              float   [deg C] CCD controller CPU temperature
CCDCFG   M1-46_lbnl_20211019.cfg                              str     CCD configuration file
CLOCK15  9.9992,2.9993                                        str     [V] high rail, low rail
BIASSECA [2065:2128, 2:2065]                                  str     Bias section for quadrant A
PRESECC  [1:7, 2130:4193]                                     str     Prescan section for quadrant C
DAC7     5.9998,6.0332                                        str     [V] set value, measured value
DETSECC  [1:2057, 2065:4128]                                  str     Detector section for quadrant C
CLOCK0   9.9999,0.0                                           str     [V] high rail, low rail
CCDTMING flatdark_lbnl_timing.txt                             str     CCD timing file
CAMERA   r8                                                   str     Camera name
ORSECD   [2193:4249, 2098:2129]                               str     Row bias section for quadrant D
CCDSECD  [2058:4114, 2065:4128]                               str     CCD section for quadrant D
PRRSECD  [2193:4249, 4194:4194]                               str     Row prescan section for quadrant D
OFFSET1  0.4000000059604645,-8.9198                           str     [V] set value, measured value
CLOCK11  9.9992,2.9993                                        str     [V] high rail, low rail
DATASECC [8:2064, 2130:4193]                                  str     Data section for quadrant C
TRIMSECB [2193:4249, 2:2065]                                  str     Trim section for quadrant B
CLOCK6   9.9999,0.0                                           str     [V] high rail, low rail
PRESECA  [1:7, 2:2065]                                        str     Prescan section for quadrant A
CCDSECC  [1:2057, 2065:4128]                                  str     CCD section for quadrant C
OFFSET2  0.4000000059604645,-8.9198                           str     [V] set value, measured value
CRYOPRES 8.920e-08                                            str     [mb] Cryostat pressure (IP)
TRIMSECA [8:2064, 2:2065]                                     str     Trim section for quadrant A
PRRSECA  [8:2064, 1:1]                                        str     Row prescan section for quadrant A
DIGITIME 56.1202                                              float   [s] Time to digitize image
CLOCK9   9.9992,2.9993                                        str     [V] high rail, low rail
DAC13    0.0,0.0148                                           str     [V] set value, measured value
DETSECA  [1:2057, 1:2064]                                     str     Detector section for quadrant A
CLOCK4   9.9999,0.0                                           str     [V] high rail, low rail
CRYOTEMP 163.044                                              float   [deg K] Cryostat CCD temperature
CLOCK7   -2.0001,3.9999                                       str     [V] high rail, low rail
CLOCK12  9.9992,2.9993                                        str     [V] high rail, low rail
AMPSECD  [4114:2058, 4128:2065]                               str     AMP section for quadrant D
DAC0     -9.0002,-8.9507                                      str     [V] set value, measured value
OFFSET0  0.4000000059604645,-8.9507                           str     [V] set value, measured value
PGAGAIN  3                                                    int     Controller gain
CLOCK14  9.9992,2.9993                                        str     [V] high rail, low rail
CCDSIZE  4194,4256                                            str     CCD size in pixels (rows, columns)
CASETEMP 60.4294                                              float   [deg C] CCD controller case temperature
CCDSECA  [1:2057, 1:2064]                                     str     CCD section for quadrant A
DAC4     5.9998,6.0332                                        str     [V] set value, measured value
CLOCK16  9.9999,3.0                                           str     [V] high rail, low rail
AMPSECA  [1:2057, 1:2064]                                     str     AMP section for quadrant A
DETECTOR M1-46                                                str     Detector (ccd) identification
OFFSET3  0.4000000059604645,-8.9095                           str     [V] set value, measured value
ORSECA   [8:2064, 2066:2097]                                  str     Row overscan section for quadrant A
CLOCK3   -2.0001,3.9999                                       str     [V] high rail, low rail
SETTINGS detectors_sm_20211015.json                           str     Name of DESI CCD settings file
DAC14    0.0,0.0594                                           str     [V] set value, measured value
PRRSECC  [8:2064, 4194:4194]                                  str     Row prescan section for quadrant C
ORSECC   [8:2064, 2098:2129]                                  str     Row overscan section for quadrant C
TRIMSECD [2193:4249, 2130:4193]                               str     Trim section for quadrant D
BIASSECD [2129:2192, 2130:4193]                               str     Bias section for quadrant D
CCDSECB  [2058:4114, 1:2064]                                  str     CCD section for quadrant B
BLDTIME  0.3519                                               float   [s] Time to build image
DAC10    -25.0003,-24.6938                                    str     [V] set value, measured value
DAC8     -25.0003,-24.9312                                    str     [V] set value, measured value
DAC3     -9.0002,-8.9095                                      str     [V] set value, measured value
PRESECD  [4250:4256, 2130:4193]                               str     Prescan section for quadrant D
CLOCK5   9.9999,0.0                                           str     [V] high rail, low rail
CLOCK18  9.0,0.9999                                           str     [V] high rail, low rail
DETSECB  [2058:4114, 1:2064]                                  str     Detector section for quadrant B
DAC17    20.0008,12.261                                       str     [V] set value, measured value
BIASSECC [2065:2128, 2130:4193]                               str     Bias section for quadrant C
CCDNAME  CCDSM2R                                              str     CCD name
AMPSECC  [1:2057, 4128:2065]                                  str     AMP section for quadrant C
DATASECA [8:2064, 2:2065]                                     str     Data section for quadrant A
CDSPARMS 400, 400, 8, 2000                                    str     CDS parameters
CLOCK10  9.9992,2.9993                                        str     [V] high rail, low rail
DATASECD [2193:4249, 2130:4193]                               str     Data section for quadrant D
DAC5     5.9998,6.0543                                        str     [V] set value, measured value
OFFSET7  2.0,6.028                                            str     [V] set value, measured value
OFFSET6  2.0,6.0385                                           str     [V] set value, measured value
DATASECB [2193:4249, 2:2065]                                  str     Data section for quadrant B
OFFSET5  2.0,6.0543                                           str     [V] set value, measured value
DAC12    0.0,0.0297                                           str     [V] set value, measured value
TRIMSECC [8:2064, 2130:4193]                                  str     Trim section for quadrant C
CLOCK2   9.9999,0.0                                           str     [V] high rail, low rail
PRESECB  [4250:4256, 2:2065]                                  str     Prescan section for quadrant B
AMPSECB  [4114:2058, 1:2064]                                  str     AMP section for quadrant B
DELAYS   20, 20, 25, 25, 15, 3000, 7, 7, 400, 7               str     [10] Delay settings
DAC9     -25.0003,-24.768                                     str     [V] set value, measured value
PRRSECB  [2193:4249, 1:1]                                     str     Row prescan section for quadrant B
ORSECB   [2193:4249, 2066:2097]                               str     Row overscan section for quadrant B
DAC16    39.9961,39.3162                                      str     [V] set value, measured value
DAC2     -9.0002,-8.9198                                      str     [V] set value, measured value
CLOCK1   9.9999,0.0                                           str     [V] high rail, low rail
CLOCK8   9.9992,2.9993                                        str     [V] high rail, low rail
BIASSECB [2129:2192, 2:2065]                                  str     Bias section for quadrant B
DETSECD  [2058:4114, 2065:4128]                               str     Detector section for quadrant D
DAC11    -25.0003,-24.8422                                    str     [V] set value, measured value
OFFSET4  2.0,6.028                                            str     [V] set value, measured value
CLOCK17  9.0,0.9999                                           str     [V] high rail, low rail
DAC1     -9.0002,-8.9198                                      str     [V] set value, measured value
CLOCK13  9.9992,2.9993                                        str     [V] high rail, low rail
DAC6     5.9998,6.0437                                        str     [V] set value, measured value
CCDPREP  purge,clear                                          str     CCD prep actions
REQTIME  1860.0                                               float   [s] Requested exposure time
OBSID    kp4m20220114t110417                                  str     Unique observation identifier
PROCTYPE RAW                                                  str     Data processing level
PRODTYPE image                                                str     Data product type
CHECKSUM J6j6M6j5J6j5J6j5                                     str     HDU checksum updated 2022-01-14T11:15:04
DATASUM  3618169380                                           str     data unit checksum updated 2022-01-14T11:15:04
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 4256x4194]

HDU10
-----

EXTNAME = B8

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   4162                                                 int     number of rows in table
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
EXPID    118526                                               int     Exposure number
EXPFRAME 0                                                    int     Frame number
FRAMES   None                                                 Unknown Number of Frames in Archive
TILEID   4403                                                 int     DESI Tile ID
FIBASSGN /data/tiles/SVN_tiles/004/fiberassign-004403.fits.gz str     Fiber assign
FLAVOR   science                                              str     Observation type
SEQUENCE _Split                                               str     OCS Sequence name
PURPOSE  Main Survey                                          str     Purpose of observing night
PROGRAM  DARK                                                 str     Program name
PROPID   2020B-5000                                           str     Proposal ID
OBSERVER Jessica Chellino, Corentin Ravoux                    str     Names of observers
LEAD     Martin Landriau                                      str     Lead observer
INSTRUME DESI                                                 str     Instrument name
OBSERVAT KPNO                                                 str     Observatory name
OBS-LAT  31.96403                                             str     [deg] Observatory latitude
OBS-LONG -111.59989                                           str     [deg] Observatory east longitude
OBS-ELEV 2097.0                                               float   [m] Observatory elevation
TELESCOP KPNO 4.0-m telescope                                 str     Telescope name
CORRCTOR DESI Corrector                                       str     Corrector Identification
NIGHT    20220113                                             int     Observing night
TIMESYS  UTC                                                  str     Time system used for date-obs
DATE-OBS 2022-01-14T11:04:18.005188096                        str     [UTC] Observation data and start tim
TIME-OBS 2022-01-14T11:04:18.005188096                        str     [UTC] Observation start time
MJD-OBS  59593.4613195                                        float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:04:18.788872                           str     Time shutter opened
ST       11:13:28.760000                                      str     Local Sidereal time at observation start (HH:MM
EXPTIME  578.988                                              float   [s] Actual exposure time
REQRA    170.239                                              float   [deg] Requested right ascension (observer input
REQDEC   -7.093                                               float   [deg] Requested declination (observer input)
FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                   str     Telescope focus settings
VCCD     ON                                                   str     True (ON) if CCD voltage is on
VCCDON   2022-01-10T20:55:39.339764                           str     Time when CCD voltage was turned on
VCCDSEC  310754.6                                             float   [s] CCD on time in seconds
TRUSTEMP 12.267                                               float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.675                                               float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                               float   Epoch of observation
MOUNTAZ  176.725567                                           float   [deg] Mount azimuth angle
MOUNTDEC -7.102329                                            float   [deg] Mount declination
MOUNTEL  50.883914                                            float   [deg] Mount elevation angle
MOUNTHA  -2.081118                                            float   [deg] Mount hour angle
SKYDEC   -7.102329                                            float   [deg] Telescope declination (pointing on sky)
SKYRA    170.24163                                            float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.102329                                            float   [deg] Target declination (to TCS)
TARGTRA  170.24163                                            float   [deg] Target right ascension (to TCS)
USEETC   T                                                    bool    ETC data available if true
USESKY   T                                                    bool    DOS Control: use Sky Monitor
USEFOCUS T                                                    bool    DOS Control: use focus
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                              str     Hexapod trim values
USEROTAT T                                                    bool    DOS Control: use rotator
ROTOFFST 138.8                                                float   [arcsec] Rotator offset
ROTENBLD T                                                    bool    Rotator enabled
ROTRATE  0.513                                                float   [arcsec/min] Rotator rate
USEGUIDR T                                                    bool    DOS Control: use guider
USEDONUT T                                                    bool    DOS Control: use donuts
SPECGRPH 8                                                    int     Spectrograph logical name (SP)
SPECID   2                                                    int     Spectrograph serial number (SM)
FEEBOX   lbnl063                                              str     CCD Controller serial number
VESSEL   5                                                    int     Cryostat serial number
FEEVER   v20160312                                            str     CCD Controller version
DETFLVER FAILED: invalid argument for get command             str     CCD Controller detector f
FEEPOWER ON                                                   str     FEE power status
FEEDMASK 2134851391                                           int     FEE dac mask
FEECMASK 1048575                                              int     FEE clk mask
CCDTEMP  850.0                                                float   [deg C] CCD controller CCD temperature
RADESYS  FK5                                                  str     Coordinate reference frame of major/minor axes
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
CCDNAME  CCDSM2B                                              str     CCD name
DETSECD  [2049:4096, 2049:4096]                               str     Detector section for quadrant D
DAC3     15.9998,15.8311                                      str     [V] set value, measured value
BIASSECD [2117:2180, 2114:4161]                               str     Bias section for quadrant D
DAC12    4.9997,5.0544                                        str     [V] set value, measured value
PRESECA  [1:4, 2:2049]                                        str     Prescan section for quadrant A
CLOCK18  3.9999,-4.0002                                       str     [V] high rail, low rail
CCDSECA  [1:2048, 1:2048]                                     str     CCD section for quadrant A
DAC17    -0.0,0.0122                                          str     [V] set value, measured value
PGAGAIN  5                                                    int     Controller gain
CAMERA   b8                                                   str     Camera name
OFFSET0  -1.5,15.7075                                         str     [V] set value, measured value
CLOCK1   3.9999,-4.0002                                       str     [V] high rail, low rail
AMPSECA  [1:2048, 1:2048]                                     str     AMP section for quadrant A
ORSECA   [5:2052, 2050:2081]                                  str     Row overscan section for quadrant A
CLOCK17  3.9999,-4.0002                                       str     [V] high rail, low rail
CCDTMING flatdark_sta_timing.txt                              str     CCD timing file
CDSPARMS 400, 400, 8, 1000                                    str     CDS parameters
PRESECC  [1:4, 2114:4161]                                     str     Prescan section for quadrant C
CLOCK13  3.0,-7.0002                                          str     [V] high rail, low rail
CLOCK15  0.0,0.0                                              str     [V] high rail, low rail
OFFSET6  -1.100000023841858,-0.0053                           str     [V] set value, measured value
TRIMSECD [2181:4228, 2114:4161]                               str     Trim section for quadrant D
DAC4     0.0,-0.0158                                          str     [V] set value, measured value
CLOCK16  0.0,0.0                                              str     [V] high rail, low rail
ORSECD   [2181:4228, 2082:2113]                               str     Row bias section for quadrant D
DATASECD [2181:4228, 2114:4161]                               str     Data section for quadrant D
CLOCK0   3.9999,-4.0002                                       str     [V] high rail, low rail
TRIMSECC [5:2052, 2114:4161]                                  str     Trim section for quadrant C
ORSECB   [2181:4228, 2050:2081]                               str     Row overscan section for quadrant B
CCDPREP  purge,clear                                          str     CCD prep actions
PRRSECB  [2181:4228, 1:1]                                     str     Row prescan section for quadrant B
TRIMSECB [2181:4228, 2:2049]                                  str     Trim section for quadrant B
AMPSECB  [2049:4096, 2048:1]                                  str     AMP section for quadrant B
PRRSECD  [2181:4228, 4162:4162]                               str     Row prescan section for quadrant D
OFFSET2  -1.5,15.8723                                         str     [V] set value, measured value
PRRSECC  [5:2052, 4162:4162]                                  str     Row prescan section for quadrant C
OFFSET5  -1.100000023841858,-0.0158                           str     [V] set value, measured value
DETECTOR sn22802                                              str     Detector (ccd) identification
AMPSECC  [2048:1, 2049:4096]                                  str     AMP section for quadrant C
DAC5     0.0,-0.0105                                          str     [V] set value, measured value
PRESECB  [4229:4232, 2:2049]                                  str     Prescan section for quadrant B
CPUTEMP  60.9316                                              float   [deg C] CCD controller CPU temperature
DAC2     15.9998,15.8929                                      str     [V] set value, measured value
AMPSECD  [4096:2049, 4096:2049]                               str     AMP section for quadrant D
CLOCK8   3.0,-7.0002                                          str     [V] high rail, low rail
BLDTIME  0.3517                                               float   [s] Time to build image
OFFSET1  -1.5,15.8929                                         str     [V] set value, measured value
DAC14    0.0,0.8424                                           str     [V] set value, measured value
SETTINGS detectors_sm_20210128.json                           str     Name of DESI CCD settings file
DAC9     26.9998,26.5636                                      str     [V] set value, measured value
CLOCK3   6.9999,-2.0001                                       str     [V] high rail, low rail
CRYOTEMP 163.044                                              float   [deg K] Cryostat CCD temperature
CLOCK5   3.9999,-4.0002                                       str     [V] high rail, low rail
CCDSECC  [1:2048, 2049:4096]                                  str     CCD section for quadrant C
OFFSET4  -1.100000023841858,-0.021                            str     [V] set value, measured value
DAC0     15.9998,15.6869                                      str     [V] set value, measured value
CLOCK14  3.0,-7.0002                                          str     [V] high rail, low rail
PRRSECA  [5:2052, 1:1]                                        str     Row prescan section for quadrant A
DELAYS   13, 13, 25, 25, 8, 3000, 7, 7, 400, 7                str     [10] Delay settings
DAC13    -5.0006,-5.0544                                      str     [V] set value, measured value
CLOCK9   3.0,-7.0002                                          str     [V] high rail, low rail
CCDSECB  [2049:4096, 1:2048]                                  str     CCD section for quadrant B
CLOCK10  3.0,-7.0002                                          str     [V] high rail, low rail
DAC10    26.9998,27.0385                                      str     [V] set value, measured value
CLOCK12  3.0,-7.0002                                          str     [V] high rail, low rail
DETSECC  [1:2048, 2049:4096]                                  str     Detector section for quadrant C
CCDCFG   default_sta_20210128.cfg                             str     CCD configuration file
BIASSECC [2053:2116, 2114:4161]                               str     Bias section for quadrant C
OFFSET3  -1.5,15.8414                                         str     [V] set value, measured value
DIGITIME 54.8188                                              float   [s] Time to digitize image
DAC6     0.0,0.0                                              str     [V] set value, measured value
DATASECA [5:2052, 2:2049]                                     str     Data section for quadrant A
OFFSET7  -1.100000023841858,-0.0053                           str     [V] set value, measured value
CLOCK4   3.9999,-4.0002                                       str     [V] high rail, low rail
CASETEMP 60.5525                                              float   [deg C] CCD controller case temperature
DAC11    26.9998,27.0385                                      str     [V] set value, measured value
PRESECD  [4229:4232, 2114:4161]                               str     Prescan section for quadrant D
CCDSECD  [2049:4096, 2049:4096]                               str     CCD section for quadrant D
DATASECC [5:2052, 2114:4161]                                  str     Data section for quadrant C
DAC7     0.0,0.0                                              str     [V] set value, measured value
DETSECB  [2049:4096, 1:2048]                                  str     Detector section for quadrant B
CRYOPRES 8.920e-08                                            str     [mb] Cryostat pressure (IP)
CLOCK6   3.9999,-4.0002                                       str     [V] high rail, low rail
ORSECC   [5:2052, 2082:2113]                                  str     Row overscan section for quadrant C
CLOCK7   6.9999,-2.0001                                       str     [V] high rail, low rail
BIASSECA [2053:2116, 2:2049]                                  str     Bias section for quadrant A
DATASECB [2181:4228, 2:2049]                                  str     Data section for quadrant B
DAC1     15.9998,15.8929                                      str     [V] set value, measured value
DAC15    19.9997,19.9264                                      str     [V] set value, measured value
DAC8     26.9998,26.6378                                      str     [V] set value, measured value
CCDSIZE  4162,4232                                            str     CCD size in pixels (rows, columns)
CLOCK2   3.9999,-4.0002                                       str     [V] high rail, low rail
BIASSECB [2117:2180, 2:2049]                                  str     Bias section for quadrant B
TRIMSECA [5:2052, 2:2049]                                     str     Trim section for quadrant A
DAC16    0.0,63.3402                                          str     [V] set value, measured value
DETSECA  [1:2048, 1:2048]                                     str     Detector section for quadrant A
CLOCK11  0.0,0.0                                              str     [V] high rail, low rail
REQTIME  1860.0                                               float   [s] Requested exposure time
OBSID    kp4m20220114t110417                                  str     Unique observation identifier
PROCTYPE RAW                                                  str     Data processing level
PRODTYPE image                                                str     Data product type
CHECKSUM R9OAU9LAR9LAR9LA                                     str     HDU checksum updated 2022-01-14T11:15:05
DATASUM  3625345256                                           str     data unit checksum updated 2022-01-14T11:15:05
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 4232x4162]

HDU11
-----

EXTNAME = Z2

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   4194                                                 int     number of rows in table
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
EXPID    118526                                               int     Exposure number
EXPFRAME 0                                                    int     Frame number
FRAMES   None                                                 Unknown Number of Frames in Archive
TILEID   4403                                                 int     DESI Tile ID
FIBASSGN /data/tiles/SVN_tiles/004/fiberassign-004403.fits.gz str     Fiber assign
FLAVOR   science                                              str     Observation type
SEQUENCE _Split                                               str     OCS Sequence name
PURPOSE  Main Survey                                          str     Purpose of observing night
PROGRAM  DARK                                                 str     Program name
PROPID   2020B-5000                                           str     Proposal ID
OBSERVER Jessica Chellino, Corentin Ravoux                    str     Names of observers
LEAD     Martin Landriau                                      str     Lead observer
INSTRUME DESI                                                 str     Instrument name
OBSERVAT KPNO                                                 str     Observatory name
OBS-LAT  31.96403                                             str     [deg] Observatory latitude
OBS-LONG -111.59989                                           str     [deg] Observatory east longitude
OBS-ELEV 2097.0                                               float   [m] Observatory elevation
TELESCOP KPNO 4.0-m telescope                                 str     Telescope name
CORRCTOR DESI Corrector                                       str     Corrector Identification
NIGHT    20220113                                             int     Observing night
TIMESYS  UTC                                                  str     Time system used for date-obs
DATE-OBS 2022-01-14T11:04:17.824615936                        str     [UTC] Observation data and start tim
TIME-OBS 2022-01-14T11:04:17.824615936                        str     [UTC] Observation start time
MJD-OBS  59593.46131741                                       float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:04:18.612278                           str     Time shutter opened
ST       11:13:28.580000                                      str     Local Sidereal time at observation start (HH:MM
EXPTIME  579.17                                               float   [s] Actual exposure time
REQRA    170.239                                              float   [deg] Requested right ascension (observer input
REQDEC   -7.093                                               float   [deg] Requested declination (observer input)
FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                   str     Telescope focus settings
VCCD     ON                                                   str     True (ON) if CCD voltage is on
VCCDON   2022-01-10T20:55:43.745954                           str     Time when CCD voltage was turned on
VCCDSEC  310751.8                                             float   [s] CCD on time in seconds
TRUSTEMP 12.267                                               float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.675                                               float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                               float   Epoch of observation
MOUNTAZ  176.725567                                           float   [deg] Mount azimuth angle
MOUNTDEC -7.102329                                            float   [deg] Mount declination
MOUNTEL  50.883914                                            float   [deg] Mount elevation angle
MOUNTHA  -2.081118                                            float   [deg] Mount hour angle
SKYDEC   -7.102329                                            float   [deg] Telescope declination (pointing on sky)
SKYRA    170.24163                                            float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.102329                                            float   [deg] Target declination (to TCS)
TARGTRA  170.24163                                            float   [deg] Target right ascension (to TCS)
USEETC   T                                                    bool    ETC data available if true
USESKY   T                                                    bool    DOS Control: use Sky Monitor
USEFOCUS T                                                    bool    DOS Control: use focus
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                              str     Hexapod trim values
USEROTAT T                                                    bool    DOS Control: use rotator
ROTOFFST 138.8                                                float   [arcsec] Rotator offset
ROTENBLD T                                                    bool    Rotator enabled
ROTRATE  0.513                                                float   [arcsec/min] Rotator rate
USEGUIDR T                                                    bool    DOS Control: use guider
USEDONUT T                                                    bool    DOS Control: use donuts
SPECGRPH 2                                                    int     Spectrograph logical name (SP)
SPECID   5                                                    int     Spectrograph serial number (SM)
FEEBOX   lbnl054                                              str     CCD Controller serial number
VESSEL   13                                                   int     Cryostat serial number
FEEVER   v20160312                                            str     CCD Controller version
DETFLVER FAILED: invalid argument for get command             str     CCD Controller detector f
FEEPOWER ON                                                   str     FEE power status
FEEDMASK 2134851391                                           int     FEE dac mask
FEECMASK 1048575                                              int     FEE clk mask
CCDTEMP  -132.9814                                            float   [deg C] CCD controller CCD temperature
RADESYS  FK5                                                  str     Coordinate reference frame of major/minor axes
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
CCDPREP  purge,clear                                          str     CCD prep actions
DATASECC [8:2064, 2130:4193]                                  str     Data section for quadrant C
CRYOPRES 5.584e-08                                            str     [mb] Cryostat pressure (IP)
CCDNAME  CCDSM5Z                                              str     CCD name
DAC3     -9.0002,-8.961                                       str     [V] set value, measured value
AMPSECD  [4114:2058, 4128:2065]                               str     AMP section for quadrant D
DETSECC  [1:2057, 2065:4128]                                  str     Detector section for quadrant C
TRIMSECA [8:2064, 2:2065]                                     str     Trim section for quadrant A
CLOCK12  9.9992,2.9993                                        str     [V] high rail, low rail
AMPSECB  [4114:2058, 1:2064]                                  str     AMP section for quadrant B
DAC7     5.9998,6.0332                                        str     [V] set value, measured value
CRYOTEMP 139.962                                              float   [deg K] Cryostat CCD temperature
DAC13    0.0,-0.0445                                          str     [V] set value, measured value
BLDTIME  0.3516                                               float   [s] Time to build image
DETSECD  [2058:4114, 2065:4128]                               str     Detector section for quadrant D
CLOCK8   9.9992,2.9993                                        str     [V] high rail, low rail
DELAYS   20, 20, 25, 40, 7, 3000, 7, 7, 400, 7                str     [10] Delay settings
CCDSIZE  4194,4256                                            str     CCD size in pixels (rows, columns)
CCDSECD  [2058:4114, 2065:4128]                               str     CCD section for quadrant D
OFFSET0  0.4000000059604645,-8.9713                           str     [V] set value, measured value
CLOCK11  9.9992,2.9993                                        str     [V] high rail, low rail
PRRSECC  [8:2064, 4194:4194]                                  str     Row prescan section for quadrant C
CLOCK16  9.9999,3.0                                           str     [V] high rail, low rail
PRESECC  [1:7, 2130:4193]                                     str     Prescan section for quadrant C
CLOCK14  9.9992,2.9993                                        str     [V] high rail, low rail
PRESECD  [4250:4256, 2130:4193]                               str     Prescan section for quadrant D
CLOCK10  9.9992,2.9993                                        str     [V] high rail, low rail
CLOCK9   9.9992,2.9993                                        str     [V] high rail, low rail
AMPSECC  [1:2057, 4128:2065]                                  str     AMP section for quadrant C
DAC15    0.0,-0.0445                                          str     [V] set value, measured value
DETECTOR M1-59                                                str     Detector (ccd) identification
DETSECB  [2058:4114, 1:2064]                                  str     Detector section for quadrant B
DETSECA  [1:2057, 1:2064]                                     str     Detector section for quadrant A
TRIMSECC [8:2064, 2130:4193]                                  str     Trim section for quadrant C
DATASECB [2193:4249, 2:2065]                                  str     Data section for quadrant B
DAC8     -25.0003,-24.7086                                    str     [V] set value, measured value
OFFSET5  2.0,6.0069                                           str     [V] set value, measured value
OFFSET2  0.4000000059604645,-9.0228                           str     [V] set value, measured value
CCDSECC  [1:2057, 2065:4128]                                  str     CCD section for quadrant C
PRESECA  [1:7, 2:2065]                                        str     Prescan section for quadrant A
DAC6     5.9998,6.0122                                        str     [V] set value, measured value
DAC2     -9.0002,-9.0228                                      str     [V] set value, measured value
ORSECC   [8:2064, 2098:2129]                                  str     Row overscan section for quadrant C
CLOCK6   9.9999,0.0                                           str     [V] high rail, low rail
ORSECB   [2193:4249, 2066:2097]                               str     Row overscan section for quadrant B
CLOCK3   -2.0001,3.9999                                       str     [V] high rail, low rail
CLOCK5   9.9999,0.0                                           str     [V] high rail, low rail
CLOCK7   -2.0001,3.9999                                       str     [V] high rail, low rail
DIGITIME 56.4579                                              float   [s] Time to digitize image
BIASSECD [2129:2192, 2130:4193]                               str     Bias section for quadrant D
DAC4     5.9998,6.0437                                        str     [V] set value, measured value
CAMERA   z2                                                   str     Camera name
PRESECB  [4250:4256, 2:2065]                                  str     Prescan section for quadrant B
BIASSECB [2129:2192, 2:2065]                                  str     Bias section for quadrant B
CLOCK2   9.9999,0.0                                           str     [V] high rail, low rail
AMPSECA  [1:2057, 1:2064]                                     str     AMP section for quadrant A
OFFSET1  0.4000000059604645,-8.9816                           str     [V] set value, measured value
CCDTMING flatdark_lbnl_timing.txt                             str     CCD timing file
DAC5     5.9998,6.0069                                        str     [V] set value, measured value
ORSECA   [8:2064, 2066:2097]                                  str     Row overscan section for quadrant A
CLOCK4   9.9999,0.0                                           str     [V] high rail, low rail
CDSPARMS 400, 400, 8, 2000                                    str     CDS parameters
DAC9     -25.0003,-24.6641                                    str     [V] set value, measured value
DATASECD [2193:4249, 2130:4193]                               str     Data section for quadrant D
CCDSECB  [2058:4114, 1:2064]                                  str     CCD section for quadrant B
DAC14    0.0,-0.0445                                          str     [V] set value, measured value
PRRSECA  [8:2064, 1:1]                                        str     Row prescan section for quadrant A
CCDCFG   default_lbnl_20210128.cfg                            str     CCD configuration file
PRRSECD  [2193:4249, 4194:4194]                               str     Row prescan section for quadrant D
DAC17    20.0008,12.1146                                      str     [V] set value, measured value
CLOCK13  9.9992,2.9993                                        str     [V] high rail, low rail
DAC1     -9.0002,-8.9816                                      str     [V] set value, measured value
PRRSECB  [2193:4249, 1:1]                                     str     Row prescan section for quadrant B
CLOCK1   9.9999,0.0                                           str     [V] high rail, low rail
TRIMSECB [2193:4249, 2:2065]                                  str     Trim section for quadrant B
DAC0     -9.0002,-8.9713                                      str     [V] set value, measured value
CASETEMP 55.7537                                              float   [deg C] CCD controller case temperature
OFFSET3  0.4000000059604645,-8.9713                           str     [V] set value, measured value
DATASECA [8:2064, 2:2065]                                     str     Data section for quadrant A
TRIMSECD [2193:4249, 2130:4193]                               str     Trim section for quadrant D
CPUTEMP  55.3945                                              float   [deg C] CCD controller CPU temperature
ORSECD   [2193:4249, 2098:2129]                               str     Row bias section for quadrant D
DAC11    -25.0003,-25.0202                                    str     [V] set value, measured value
BIASSECC [2065:2128, 2130:4193]                               str     Bias section for quadrant C
BIASSECA [2065:2128, 2:2065]                                  str     Bias section for quadrant A
SETTINGS detectors_sm_20210128.json                           str     Name of DESI CCD settings file
PGAGAIN  3                                                    int     Controller gain
DAC16    39.9961,39.4548                                      str     [V] set value, measured value
DAC12    0.0,-0.0445                                          str     [V] set value, measured value
OFFSET6  2.0,6.0122                                           str     [V] set value, measured value
OFFSET4  2.0,6.0437                                           str     [V] set value, measured value
CCDSECA  [1:2057, 1:2064]                                     str     CCD section for quadrant A
CLOCK17  9.0,0.9999                                           str     [V] high rail, low rail
CLOCK0   9.9999,0.0                                           str     [V] high rail, low rail
DAC10    -25.0003,-25.1686                                    str     [V] set value, measured value
OFFSET7  2.0,6.0332                                           str     [V] set value, measured value
CLOCK15  9.9992,2.9993                                        str     [V] high rail, low rail
CLOCK18  9.0,0.9999                                           str     [V] high rail, low rail
REQTIME  1860.0                                               float   [s] Requested exposure time
OBSID    kp4m20220114t110417                                  str     Unique observation identifier
PROCTYPE RAW                                                  str     Data processing level
PRODTYPE image                                                str     Data product type
CHECKSUM 3qiIAog93ogGAog9                                     str     HDU checksum updated 2022-01-14T11:15:05
DATASUM  254671777                                            str     data unit checksum updated 2022-01-14T11:15:05
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 4256x4194]

HDU12
-----

EXTNAME = R2

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   4194                                                 int     number of rows in table
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
EXPID    118526                                               int     Exposure number
EXPFRAME 0                                                    int     Frame number
FRAMES   None                                                 Unknown Number of Frames in Archive
TILEID   4403                                                 int     DESI Tile ID
FIBASSGN /data/tiles/SVN_tiles/004/fiberassign-004403.fits.gz str     Fiber assign
FLAVOR   science                                              str     Observation type
SEQUENCE _Split                                               str     OCS Sequence name
PURPOSE  Main Survey                                          str     Purpose of observing night
PROGRAM  DARK                                                 str     Program name
PROPID   2020B-5000                                           str     Proposal ID
OBSERVER Jessica Chellino, Corentin Ravoux                    str     Names of observers
LEAD     Martin Landriau                                      str     Lead observer
INSTRUME DESI                                                 str     Instrument name
OBSERVAT KPNO                                                 str     Observatory name
OBS-LAT  31.96403                                             str     [deg] Observatory latitude
OBS-LONG -111.59989                                           str     [deg] Observatory east longitude
OBS-ELEV 2097.0                                               float   [m] Observatory elevation
TELESCOP KPNO 4.0-m telescope                                 str     Telescope name
CORRCTOR DESI Corrector                                       str     Corrector Identification
NIGHT    20220113                                             int     Observing night
TIMESYS  UTC                                                  str     Time system used for date-obs
DATE-OBS 2022-01-14T11:04:17.824615936                        str     [UTC] Observation data and start tim
TIME-OBS 2022-01-14T11:04:17.824615936                        str     [UTC] Observation start time
MJD-OBS  59593.46131741                                       float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:04:18.612278                           str     Time shutter opened
ST       11:13:28.580000                                      str     Local Sidereal time at observation start (HH:MM
EXPTIME  579.17                                               float   [s] Actual exposure time
REQRA    170.239                                              float   [deg] Requested right ascension (observer input
REQDEC   -7.093                                               float   [deg] Requested declination (observer input)
FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                   str     Telescope focus settings
VCCD     ON                                                   str     True (ON) if CCD voltage is on
VCCDON   2022-01-10T20:55:36.956324                           str     Time when CCD voltage was turned on
VCCDSEC  310758.6                                             float   [s] CCD on time in seconds
TRUSTEMP 12.267                                               float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.675                                               float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                               float   Epoch of observation
MOUNTAZ  176.725567                                           float   [deg] Mount azimuth angle
MOUNTDEC -7.102329                                            float   [deg] Mount declination
MOUNTEL  50.883914                                            float   [deg] Mount elevation angle
MOUNTHA  -2.081118                                            float   [deg] Mount hour angle
SKYDEC   -7.102329                                            float   [deg] Telescope declination (pointing on sky)
SKYRA    170.24163                                            float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.102329                                            float   [deg] Target declination (to TCS)
TARGTRA  170.24163                                            float   [deg] Target right ascension (to TCS)
USEETC   T                                                    bool    ETC data available if true
USESKY   T                                                    bool    DOS Control: use Sky Monitor
USEFOCUS T                                                    bool    DOS Control: use focus
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                              str     Hexapod trim values
USEROTAT T                                                    bool    DOS Control: use rotator
ROTOFFST 138.8                                                float   [arcsec] Rotator offset
ROTENBLD T                                                    bool    Rotator enabled
ROTRATE  0.513                                                float   [arcsec/min] Rotator rate
USEGUIDR T                                                    bool    DOS Control: use guider
USEDONUT T                                                    bool    DOS Control: use donuts
SPECGRPH 2                                                    int     Spectrograph logical name (SP)
SPECID   5                                                    int     Spectrograph serial number (SM)
FEEBOX   lbnl051                                              str     CCD Controller serial number
VESSEL   10                                                   int     Cryostat serial number
FEEVER   v20160312                                            str     CCD Controller version
DETFLVER FAILED: invalid argument for get command             str     CCD Controller detector f
FEEPOWER ON                                                   str     FEE power status
FEEDMASK 2134851391                                           int     FEE dac mask
FEECMASK 1048575                                              int     FEE clk mask
CCDTEMP  -136.5932                                            float   [deg C] CCD controller CCD temperature
RADESYS  FK5                                                  str     Coordinate reference frame of major/minor axes
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
CLOCK17  9.0,0.9999                                           str     [V] high rail, low rail
CLOCK3   -2.0001,3.9999                                       str     [V] high rail, low rail
ORSECC   [8:2064, 2098:2129]                                  str     Row overscan section for quadrant C
DAC14    0.0,-0.0297                                          str     [V] set value, measured value
CCDSECD  [2058:4114, 2065:4128]                               str     CCD section for quadrant D
AMPSECA  [1:2057, 1:2064]                                     str     AMP section for quadrant A
CPUTEMP  57.7324                                              float   [deg C] CCD controller CPU temperature
DAC8     -25.0003,-24.946                                     str     [V] set value, measured value
DAC11    -25.0003,-24.575                                     str     [V] set value, measured value
BIASSECB [2129:2192, 2:2065]                                  str     Bias section for quadrant B
OFFSET1  0.4000000059604645,-8.9713                           str     [V] set value, measured value
CLOCK8   9.9992,2.9993                                        str     [V] high rail, low rail
DAC9     -25.0003,-25.0499                                    str     [V] set value, measured value
DAC12    0.0,-0.0297                                          str     [V] set value, measured value
CLOCK6   9.9999,0.0                                           str     [V] high rail, low rail
CCDTMING flatdark_lbnl_timing.txt                             str     CCD timing file
DETSECA  [1:2057, 1:2064]                                     str     Detector section for quadrant A
CLOCK9   9.9992,2.9993                                        str     [V] high rail, low rail
CCDCFG   default_lbnl_20210128.cfg                            str     CCD configuration file
CLOCK5   9.9999,0.0                                           str     [V] high rail, low rail
CCDSECB  [2058:4114, 1:2064]                                  str     CCD section for quadrant B
PRRSECB  [2193:4249, 1:1]                                     str     Row prescan section for quadrant B
DATASECA [8:2064, 2:2065]                                     str     Data section for quadrant A
DAC15    0.0,-0.0297                                          str     [V] set value, measured value
CLOCK1   9.9999,0.0                                           str     [V] high rail, low rail
CLOCK10  9.9992,2.9993                                        str     [V] high rail, low rail
DAC16    39.9961,39.0852                                      str     [V] set value, measured value
PRRSECA  [8:2064, 1:1]                                        str     Row prescan section for quadrant A
CLOCK11  9.9992,2.9993                                        str     [V] high rail, low rail
TRIMSECC [8:2064, 2130:4193]                                  str     Trim section for quadrant C
OFFSET2  0.4000000059604645,-9.0537                           str     [V] set value, measured value
CCDNAME  CCDSM5R                                              str     CCD name
DETSECC  [1:2057, 2065:4128]                                  str     Detector section for quadrant C
DAC6     5.9998,6.0174                                        str     [V] set value, measured value
CRYOTEMP 162.995                                              float   [deg K] Cryostat CCD temperature
DAC2     -9.0002,-9.064                                       str     [V] set value, measured value
DAC3     -9.0002,-8.9713                                      str     [V] set value, measured value
DETSECB  [2058:4114, 1:2064]                                  str     Detector section for quadrant B
PRESECA  [1:7, 2:2065]                                        str     Prescan section for quadrant A
OFFSET5  2.0,6.0069                                           str     [V] set value, measured value
CRYOPRES 9.517e-08                                            str     [mb] Cryostat pressure (IP)
DATASECD [2193:4249, 2130:4193]                               str     Data section for quadrant D
TRIMSECB [2193:4249, 2:2065]                                  str     Trim section for quadrant B
AMPSECC  [1:2057, 4128:2065]                                  str     AMP section for quadrant C
AMPSECD  [4114:2058, 4128:2065]                               str     AMP section for quadrant D
OFFSET7  2.0,6.0122                                           str     [V] set value, measured value
CCDSECC  [1:2057, 2065:4128]                                  str     CCD section for quadrant C
PRRSECD  [2193:4249, 4194:4194]                               str     Row prescan section for quadrant D
CCDSECA  [1:2057, 1:2064]                                     str     CCD section for quadrant A
ORSECD   [2193:4249, 2098:2129]                               str     Row bias section for quadrant D
CLOCK0   9.9999,0.0                                           str     [V] high rail, low rail
AMPSECB  [4114:2058, 1:2064]                                  str     AMP section for quadrant B
ORSECB   [2193:4249, 2066:2097]                               str     Row overscan section for quadrant B
OFFSET6  2.0,6.0174                                           str     [V] set value, measured value
ORSECA   [8:2064, 2066:2097]                                  str     Row overscan section for quadrant A
PRRSECC  [8:2064, 4194:4194]                                  str     Row prescan section for quadrant C
CLOCK12  9.9992,2.9993                                        str     [V] high rail, low rail
CLOCK4   9.9999,0.0                                           str     [V] high rail, low rail
PRESECD  [4250:4256, 2130:4193]                               str     Prescan section for quadrant D
BIASSECD [2129:2192, 2130:4193]                               str     Bias section for quadrant D
OFFSET3  0.4000000059604645,-8.9713                           str     [V] set value, measured value
DATASECC [8:2064, 2130:4193]                                  str     Data section for quadrant C
BIASSECA [2065:2128, 2:2065]                                  str     Bias section for quadrant A
DAC5     5.9998,6.0069                                        str     [V] set value, measured value
CLOCK7   -2.0001,3.9999                                       str     [V] high rail, low rail
DAC10    -25.0003,-25.228                                     str     [V] set value, measured value
DETSECD  [2058:4114, 2065:4128]                               str     Detector section for quadrant D
SETTINGS detectors_sm_20210128.json                           str     Name of DESI CCD settings file
OFFSET4  2.0,5.9806                                           str     [V] set value, measured value
DAC1     -9.0002,-8.9713                                      str     [V] set value, measured value
CLOCK14  9.9992,2.9993                                        str     [V] high rail, low rail
BLDTIME  0.3521                                               float   [s] Time to build image
CAMERA   r2                                                   str     Camera name
CDSPARMS 400, 400, 8, 2000                                    str     CDS parameters
DETECTOR M1-28                                                str     Detector (ccd) identification
PRESECC  [1:7, 2130:4193]                                     str     Prescan section for quadrant C
TRIMSECA [8:2064, 2:2065]                                     str     Trim section for quadrant A
CLOCK13  9.9992,2.9993                                        str     [V] high rail, low rail
DAC7     5.9998,6.0069                                        str     [V] set value, measured value
PRESECB  [4250:4256, 2:2065]                                  str     Prescan section for quadrant B
CCDSIZE  4194,4256                                            str     CCD size in pixels (rows, columns)
DAC17    20.0008,12.0048                                      str     [V] set value, measured value
CLOCK16  9.9999,3.0                                           str     [V] high rail, low rail
TRIMSECD [2193:4249, 2130:4193]                               str     Trim section for quadrant D
DATASECB [2193:4249, 2:2065]                                  str     Data section for quadrant B
CLOCK18  9.0,0.9999                                           str     [V] high rail, low rail
CLOCK2   9.9999,0.0                                           str     [V] high rail, low rail
DIGITIME 56.4895                                              float   [s] Time to digitize image
CLOCK15  9.9992,2.9993                                        str     [V] high rail, low rail
DAC13    0.0,-0.0445                                          str     [V] set value, measured value
PGAGAIN  3                                                    int     Controller gain
BIASSECC [2065:2128, 2130:4193]                               str     Bias section for quadrant C
CASETEMP 57.3533                                              float   [deg C] CCD controller case temperature
DAC4     5.9998,5.9806                                        str     [V] set value, measured value
DELAYS   20, 20, 25, 40, 7, 3000, 7, 7, 400, 7                str     [10] Delay settings
DAC0     -9.0002,-9.0434                                      str     [V] set value, measured value
OFFSET0  0.4000000059604645,-9.0331                           str     [V] set value, measured value
CCDPREP  purge,clear                                          str     CCD prep actions
REQTIME  1860.0                                               float   [s] Requested exposure time
OBSID    kp4m20220114t110417                                  str     Unique observation identifier
PROCTYPE RAW                                                  str     Data processing level
PRODTYPE image                                                str     Data product type
CHECKSUM gHEOg9CMgGCMg9CM                                     str     HDU checksum updated 2022-01-14T11:15:05
DATASUM  2748375834                                           str     data unit checksum updated 2022-01-14T11:15:05
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 4256x4194]

HDU13
-----

EXTNAME = B2

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   4162                                                 int     number of rows in table
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
EXPID    118526                                               int     Exposure number
EXPFRAME 0                                                    int     Frame number
FRAMES   None                                                 Unknown Number of Frames in Archive
TILEID   4403                                                 int     DESI Tile ID
FIBASSGN /data/tiles/SVN_tiles/004/fiberassign-004403.fits.gz str     Fiber assign
FLAVOR   science                                              str     Observation type
SEQUENCE _Split                                               str     OCS Sequence name
PURPOSE  Main Survey                                          str     Purpose of observing night
PROGRAM  DARK                                                 str     Program name
PROPID   2020B-5000                                           str     Proposal ID
OBSERVER Jessica Chellino, Corentin Ravoux                    str     Names of observers
LEAD     Martin Landriau                                      str     Lead observer
INSTRUME DESI                                                 str     Instrument name
OBSERVAT KPNO                                                 str     Observatory name
OBS-LAT  31.96403                                             str     [deg] Observatory latitude
OBS-LONG -111.59989                                           str     [deg] Observatory east longitude
OBS-ELEV 2097.0                                               float   [m] Observatory elevation
TELESCOP KPNO 4.0-m telescope                                 str     Telescope name
CORRCTOR DESI Corrector                                       str     Corrector Identification
NIGHT    20220113                                             int     Observing night
TIMESYS  UTC                                                  str     Time system used for date-obs
DATE-OBS 2022-01-14T11:04:17.824615936                        str     [UTC] Observation data and start tim
TIME-OBS 2022-01-14T11:04:17.824615936                        str     [UTC] Observation start time
MJD-OBS  59593.46131741                                       float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:04:18.612278                           str     Time shutter opened
ST       11:13:28.580000                                      str     Local Sidereal time at observation start (HH:MM
EXPTIME  579.17                                               float   [s] Actual exposure time
REQRA    170.239                                              float   [deg] Requested right ascension (observer input
REQDEC   -7.093                                               float   [deg] Requested declination (observer input)
FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                   str     Telescope focus settings
VCCD     ON                                                   str     True (ON) if CCD voltage is on
VCCDON   2022-01-10T20:55:39.334558                           str     Time when CCD voltage was turned on
VCCDSEC  310754.5                                             float   [s] CCD on time in seconds
TRUSTEMP 12.267                                               float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.675                                               float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                               float   Epoch of observation
MOUNTAZ  176.725567                                           float   [deg] Mount azimuth angle
MOUNTDEC -7.102329                                            float   [deg] Mount declination
MOUNTEL  50.883914                                            float   [deg] Mount elevation angle
MOUNTHA  -2.081118                                            float   [deg] Mount hour angle
SKYDEC   -7.102329                                            float   [deg] Telescope declination (pointing on sky)
SKYRA    170.24163                                            float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.102329                                            float   [deg] Target declination (to TCS)
TARGTRA  170.24163                                            float   [deg] Target right ascension (to TCS)
USEETC   T                                                    bool    ETC data available if true
USESKY   T                                                    bool    DOS Control: use Sky Monitor
USEFOCUS T                                                    bool    DOS Control: use focus
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                              str     Hexapod trim values
USEROTAT T                                                    bool    DOS Control: use rotator
ROTOFFST 138.8                                                float   [arcsec] Rotator offset
ROTENBLD T                                                    bool    Rotator enabled
ROTRATE  0.513                                                float   [arcsec/min] Rotator rate
USEGUIDR T                                                    bool    DOS Control: use guider
USEDONUT T                                                    bool    DOS Control: use donuts
SPECGRPH 2                                                    int     Spectrograph logical name (SP)
SPECID   5                                                    int     Spectrograph serial number (SM)
FEEBOX   lbnl056                                              str     CCD Controller serial number
VESSEL   12                                                   int     Cryostat serial number
FEEVER   v20160312                                            str     CCD Controller version
DETFLVER FAILED: invalid argument for get command             str     CCD Controller detector f
FEEPOWER ON                                                   str     FEE power status
FEEDMASK 2134851391                                           int     FEE dac mask
FEECMASK 1048575                                              int     FEE clk mask
CCDTEMP  850.0                                                float   [deg C] CCD controller CCD temperature
RADESYS  FK5                                                  str     Coordinate reference frame of major/minor axes
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
OFFSET0  -1.5,15.8517                                         str     [V] set value, measured value
DETSECC  [1:2048, 2049:4096]                                  str     Detector section for quadrant C
BIASSECA [2053:2116, 2:2049]                                  str     Bias section for quadrant A
DATASECB [2181:4228, 2:2049]                                  str     Data section for quadrant B
CLOCK1   3.9999,-4.0002                                       str     [V] high rail, low rail
DETSECB  [2049:4096, 1:2048]                                  str     Detector section for quadrant B
DAC16    0.0,64.0332                                          str     [V] set value, measured value
CCDPREP  purge,clear                                          str     CCD prep actions
PRRSECB  [2181:4228, 1:1]                                     str     Row prescan section for quadrant B
AMPSECA  [1:2048, 1:2048]                                     str     AMP section for quadrant A
DAC15    19.9997,19.968                                       str     [V] set value, measured value
DAC8     26.9998,26.7862                                      str     [V] set value, measured value
DAC1     15.9998,15.862                                       str     [V] set value, measured value
PRESECA  [1:4, 2:2049]                                        str     Prescan section for quadrant A
CLOCK2   3.9999,-4.0002                                       str     [V] high rail, low rail
OFFSET7  -1.100000023841858,0.0                               str     [V] set value, measured value
CASETEMP 54.154                                               float   [deg C] CCD controller case temperature
ORSECA   [5:2052, 2050:2081]                                  str     Row overscan section for quadrant A
CRYOTEMP 162.995                                              float   [deg K] Cryostat CCD temperature
DIGITIME 54.777                                               float   [s] Time to digitize image
DAC14    0.0,0.8008                                           str     [V] set value, measured value
CLOCK12  3.0,-7.0002                                          str     [V] high rail, low rail
ORSECD   [2181:4228, 2082:2113]                               str     Row bias section for quadrant D
PRESECD  [4229:4232, 2114:4161]                               str     Prescan section for quadrant D
TRIMSECB [2181:4228, 2:2049]                                  str     Trim section for quadrant B
CAMERA   b2                                                   str     Camera name
CLOCK18  3.9999,-4.0002                                       str     [V] high rail, low rail
DAC17    -0.0,0.0732                                          str     [V] set value, measured value
DELAYS   13, 13, 25, 25, 8, 3000, 7, 7, 400, 7                str     [10] Delay settings
DAC7     0.0,0.0                                              str     [V] set value, measured value
PRESECB  [4229:4232, 2:2049]                                  str     Prescan section for quadrant B
DAC5     0.0,0.0                                              str     [V] set value, measured value
DETSECD  [2049:4096, 2049:4096]                               str     Detector section for quadrant D
CCDSECD  [2049:4096, 2049:4096]                               str     CCD section for quadrant D
CLOCK0   3.9999,-4.0002                                       str     [V] high rail, low rail
PRRSECC  [5:2052, 4162:4162]                                  str     Row prescan section for quadrant C
TRIMSECD [2181:4228, 2114:4161]                               str     Trim section for quadrant D
DAC6     0.0,-0.0053                                          str     [V] set value, measured value
DETECTOR sn22801                                              str     Detector (ccd) identification
CCDNAME  CCDSM5B                                              str     CCD name
CLOCK14  3.0,-7.0002                                          str     [V] high rail, low rail
CLOCK4   3.9999,-4.0002                                       str     [V] high rail, low rail
CLOCK17  3.9999,-4.0002                                       str     [V] high rail, low rail
OFFSET5  -1.100000023841858,0.0                               str     [V] set value, measured value
CPUTEMP  54.5332                                              float   [deg C] CCD controller CPU temperature
CLOCK7   6.9999,-2.0001                                       str     [V] high rail, low rail
ORSECB   [2181:4228, 2050:2081]                               str     Row overscan section for quadrant B
CLOCK8   3.0,-7.0002                                          str     [V] high rail, low rail
CLOCK11  0.0,0.0                                              str     [V] high rail, low rail
OFFSET1  -1.5,15.862                                          str     [V] set value, measured value
CLOCK9   3.0,-7.0002                                          str     [V] high rail, low rail
BIASSECC [2053:2116, 2114:4161]                               str     Bias section for quadrant C
DAC13    -5.0006,-5.0232                                      str     [V] set value, measured value
BIASSECB [2117:2180, 2:2049]                                  str     Bias section for quadrant B
CCDTMING flatdark_sta_timing.txt                              str     CCD timing file
PRRSECD  [2181:4228, 4162:4162]                               str     Row prescan section for quadrant D
CLOCK5   3.9999,-4.0002                                       str     [V] high rail, low rail
CLOCK6   3.9999,-4.0002                                       str     [V] high rail, low rail
DATASECA [5:2052, 2:2049]                                     str     Data section for quadrant A
TRIMSECC [5:2052, 2114:4161]                                  str     Trim section for quadrant C
CLOCK15  0.0,0.0                                              str     [V] high rail, low rail
CLOCK13  3.0,-7.0002                                          str     [V] high rail, low rail
BIASSECD [2117:2180, 2114:4161]                               str     Bias section for quadrant D
DAC3     15.9998,15.9547                                      str     [V] set value, measured value
DAC4     0.0,0.0053                                           str     [V] set value, measured value
PGAGAIN  5                                                    int     Controller gain
DAC11    26.9998,26.5042                                      str     [V] set value, measured value
CCDSECC  [1:2048, 2049:4096]                                  str     CCD section for quadrant C
AMPSECC  [2048:1, 2049:4096]                                  str     AMP section for quadrant C
DAC2     15.9998,15.7693                                      str     [V] set value, measured value
AMPSECB  [2049:4096, 2048:1]                                  str     AMP section for quadrant B
ORSECC   [5:2052, 2082:2113]                                  str     Row overscan section for quadrant C
DAC12    4.9997,5.0856                                        str     [V] set value, measured value
BLDTIME  0.3518                                               float   [s] Time to build image
OFFSET4  -1.100000023841858,0.0                               str     [V] set value, measured value
CRYOPRES 9.517e-08                                            str     [mb] Cryostat pressure (IP)
CLOCK10  3.0,-7.0002                                          str     [V] high rail, low rail
CLOCK3   6.9999,-2.0001                                       str     [V] high rail, low rail
CCDSECA  [1:2048, 1:2048]                                     str     CCD section for quadrant A
DETSECA  [1:2048, 1:2048]                                     str     Detector section for quadrant A
CDSPARMS 400, 400, 8, 1000                                    str     CDS parameters
CCDSIZE  4162,4232                                            str     CCD size in pixels (rows, columns)
OFFSET3  -1.5,15.965                                          str     [V] set value, measured value
PRRSECA  [5:2052, 1:1]                                        str     Row prescan section for quadrant A
DAC9     26.9998,26.623                                       str     [V] set value, measured value
CLOCK16  0.0,0.0                                              str     [V] high rail, low rail
DAC10    26.9998,26.2816                                      str     [V] set value, measured value
DATASECD [2181:4228, 2114:4161]                               str     Data section for quadrant D
TRIMSECA [5:2052, 2:2049]                                     str     Trim section for quadrant A
DATASECC [5:2052, 2114:4161]                                  str     Data section for quadrant C
CCDSECB  [2049:4096, 1:2048]                                  str     CCD section for quadrant B
PRESECC  [1:4, 2114:4161]                                     str     Prescan section for quadrant C
OFFSET2  -1.5,15.7693                                         str     [V] set value, measured value
OFFSET6  -1.100000023841858,0.0                               str     [V] set value, measured value
AMPSECD  [4096:2049, 4096:2049]                               str     AMP section for quadrant D
SETTINGS detectors_sm_20210128.json                           str     Name of DESI CCD settings file
DAC0     15.9998,15.862                                       str     [V] set value, measured value
CCDCFG   default_sta_20210128.cfg                             str     CCD configuration file
REQTIME  1860.0                                               float   [s] Requested exposure time
OBSID    kp4m20220114t110417                                  str     Unique observation identifier
PROCTYPE RAW                                                  str     Data processing level
PRODTYPE image                                                str     Data product type
CHECKSUM Wa42aX20Xa20aW20                                     str     HDU checksum updated 2022-01-14T11:15:05
DATASUM  2050978499                                           str     data unit checksum updated 2022-01-14T11:15:05
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 4232x4162]

HDU14
-----

EXTNAME = Z0

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   4194                                                 int     number of rows in table
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
EXPID    118526                                               int     Exposure number
EXPFRAME 0                                                    int     Frame number
FRAMES   None                                                 Unknown Number of Frames in Archive
TILEID   4403                                                 int     DESI Tile ID
FIBASSGN /data/tiles/SVN_tiles/004/fiberassign-004403.fits.gz str     Fiber assign
FLAVOR   science                                              str     Observation type
SEQUENCE _Split                                               str     OCS Sequence name
PURPOSE  Main Survey                                          str     Purpose of observing night
PROGRAM  DARK                                                 str     Program name
PROPID   2020B-5000                                           str     Proposal ID
OBSERVER Jessica Chellino, Corentin Ravoux                    str     Names of observers
LEAD     Martin Landriau                                      str     Lead observer
INSTRUME DESI                                                 str     Instrument name
OBSERVAT KPNO                                                 str     Observatory name
OBS-LAT  31.96403                                             str     [deg] Observatory latitude
OBS-LONG -111.59989                                           str     [deg] Observatory east longitude
OBS-ELEV 2097.0                                               float   [m] Observatory elevation
TELESCOP KPNO 4.0-m telescope                                 str     Telescope name
CORRCTOR DESI Corrector                                       str     Corrector Identification
NIGHT    20220113                                             int     Observing night
TIMESYS  UTC                                                  str     Time system used for date-obs
DATE-OBS 2022-01-14T11:04:17.790636032                        str     [UTC] Observation data and start tim
TIME-OBS 2022-01-14T11:04:17.790636032                        str     [UTC] Observation start time
MJD-OBS  59593.46131702                                       float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:04:18.577390                           str     Time shutter opened
ST       11:13:28.540000                                      str     Local Sidereal time at observation start (HH:MM
EXPTIME  579.193                                              float   [s] Actual exposure time
REQRA    170.239                                              float   [deg] Requested right ascension (observer input
REQDEC   -7.093                                               float   [deg] Requested declination (observer input)
FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                   str     Telescope focus settings
VCCD     ON                                                   str     True (ON) if CCD voltage is on
VCCDON   2022-01-10T20:55:43.758808                           str     Time when CCD voltage was turned on
VCCDSEC  310751.8                                             float   [s] CCD on time in seconds
TRUSTEMP 12.267                                               float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.675                                               float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                               float   Epoch of observation
MOUNTAZ  176.725567                                           float   [deg] Mount azimuth angle
MOUNTDEC -7.102329                                            float   [deg] Mount declination
MOUNTEL  50.883914                                            float   [deg] Mount elevation angle
MOUNTHA  -2.081118                                            float   [deg] Mount hour angle
SKYDEC   -7.102329                                            float   [deg] Telescope declination (pointing on sky)
SKYRA    170.24163                                            float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.102329                                            float   [deg] Target declination (to TCS)
TARGTRA  170.24163                                            float   [deg] Target right ascension (to TCS)
USEETC   T                                                    bool    ETC data available if true
USESKY   T                                                    bool    DOS Control: use Sky Monitor
USEFOCUS T                                                    bool    DOS Control: use focus
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                              str     Hexapod trim values
USEROTAT T                                                    bool    DOS Control: use rotator
ROTOFFST 138.8                                                float   [arcsec] Rotator offset
ROTENBLD T                                                    bool    Rotator enabled
ROTRATE  0.513                                                float   [arcsec/min] Rotator rate
USEGUIDR T                                                    bool    DOS Control: use guider
USEDONUT T                                                    bool    DOS Control: use donuts
SPECGRPH 0                                                    int     Spectrograph logical name (SP)
SPECID   4                                                    int     Spectrograph serial number (SM)
FEEBOX   lbnl082                                              str     CCD Controller serial number
VESSEL   17                                                   int     Cryostat serial number
FEEVER   v20160312                                            str     CCD Controller version
DETFLVER FAILED: invalid argument for get command             str     CCD Controller detector f
FEEPOWER ON                                                   str     FEE power status
FEEDMASK 2134851391                                           int     FEE dac mask
FEECMASK 1048575                                              int     FEE clk mask
CCDTEMP  -137.5647                                            float   [deg C] CCD controller CCD temperature
RADESYS  FK5                                                  str     Coordinate reference frame of major/minor axes
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
CAMERA   z0                                                   str     Camera name
DAC2     -9.0002,-8.8271                                      str     [V] set value, measured value
DATASECA [8:2064, 2:2065]                                     str     Data section for quadrant A
CLOCK6   9.9999,0.0                                           str     [V] high rail, low rail
DIGITIME 56.4524                                              float   [s] Time to digitize image
DAC17    20.0008,11.834                                       str     [V] set value, measured value
CLOCK15  9.9992,2.9993                                        str     [V] high rail, low rail
DETSECB  [2058:4114, 1:2064]                                  str     Detector section for quadrant B
CLOCK0   9.9999,0.0                                           str     [V] high rail, low rail
CRYOPRES 7.360e-08                                            str     [mb] Cryostat pressure (IP)
AMPSECC  [1:2057, 4128:2065]                                  str     AMP section for quadrant C
CCDTMING flatdark_lbnl_timing.txt                             str     CCD timing file
CLOCK8   9.9992,2.9993                                        str     [V] high rail, low rail
CLOCK4   9.9999,0.0                                           str     [V] high rail, low rail
PRESECB  [4250:4256, 2:2065]                                  str     Prescan section for quadrant B
DAC1     -9.0002,-8.8683                                      str     [V] set value, measured value
PRRSECC  [8:2064, 4194:4194]                                  str     Row prescan section for quadrant C
DAC10    -25.0003,-24.7976                                    str     [V] set value, measured value
OFFSET2  0.4000000059604645,-8.8271                           str     [V] set value, measured value
CLOCK14  9.9992,2.9993                                        str     [V] high rail, low rail
DAC16    39.9961,39.039                                       str     [V] set value, measured value
ORSECB   [2193:4249, 2066:2097]                               str     Row overscan section for quadrant B
AMPSECA  [1:2057, 1:2064]                                     str     AMP section for quadrant A
DAC14    0.0,0.1039                                           str     [V] set value, measured value
DAC11    -25.0003,-24.0556                                    str     [V] set value, measured value
CLOCK7   -2.0001,3.9999                                       str     [V] high rail, low rail
PGAGAIN  3                                                    int     Controller gain
ORSECA   [8:2064, 2066:2097]                                  str     Row overscan section for quadrant A
DAC15    0.0,0.089                                            str     [V] set value, measured value
DETSECD  [2058:4114, 2065:4128]                               str     Detector section for quadrant D
ORSECD   [2193:4249, 2098:2129]                               str     Row bias section for quadrant D
OFFSET0  0.4000000059604645,-8.7962                           str     [V] set value, measured value
OFFSET6  2.0,6.0911                                           str     [V] set value, measured value
PRRSECD  [2193:4249, 4194:4194]                               str     Row prescan section for quadrant D
DAC13    0.0,0.1187                                           str     [V] set value, measured value
OFFSET3  0.4000000059604645,-8.8786                           str     [V] set value, measured value
AMPSECD  [4114:2058, 4128:2065]                               str     AMP section for quadrant D
DAC9     -25.0003,-24.946                                     str     [V] set value, measured value
DELAYS   20, 20, 25, 40, 7, 3000, 7, 7, 400, 7                str     [10] Delay settings
SETTINGS detectors_sm_20210128.json                           str     Name of DESI CCD settings file
DETSECA  [1:2057, 1:2064]                                     str     Detector section for quadrant A
CLOCK5   9.9999,0.0                                           str     [V] high rail, low rail
PRRSECB  [2193:4249, 1:1]                                     str     Row prescan section for quadrant B
DETECTOR M1-53                                                str     Detector (ccd) identification
CLOCK12  9.9992,2.9993                                        str     [V] high rail, low rail
DAC12    0.0,0.1039                                           str     [V] set value, measured value
TRIMSECA [8:2064, 2:2065]                                     str     Trim section for quadrant A
DATASECB [2193:4249, 2:2065]                                  str     Data section for quadrant B
CDSPARMS 400, 400, 8, 2000                                    str     CDS parameters
TRIMSECC [8:2064, 2130:4193]                                  str     Trim section for quadrant C
DAC3     -9.0002,-8.8683                                      str     [V] set value, measured value
BIASSECA [2065:2128, 2:2065]                                  str     Bias section for quadrant A
TRIMSECB [2193:4249, 2:2065]                                  str     Trim section for quadrant B
CASETEMP 60.1833                                              float   [deg C] CCD controller case temperature
CPUTEMP  59.5781                                              float   [deg C] CCD controller CPU temperature
OFFSET5  2.0,6.0806                                           str     [V] set value, measured value
CCDSECD  [2058:4114, 2065:4128]                               str     CCD section for quadrant D
CCDNAME  CCDSM4Z                                              str     CCD name
DAC4     5.9998,6.0648                                        str     [V] set value, measured value
BLDTIME  0.3529                                               float   [s] Time to build image
CLOCK13  9.9992,2.9993                                        str     [V] high rail, low rail
CLOCK1   9.9999,0.0                                           str     [V] high rail, low rail
PRESECA  [1:7, 2:2065]                                        str     Prescan section for quadrant A
CCDSIZE  4194,4256                                            str     CCD size in pixels (rows, columns)
DATASECC [8:2064, 2130:4193]                                  str     Data section for quadrant C
CLOCK18  9.0,0.9999                                           str     [V] high rail, low rail
CLOCK10  9.9992,2.9993                                        str     [V] high rail, low rail
CRYOTEMP 139.962                                              float   [deg K] Cryostat CCD temperature
CLOCK3   -2.0001,3.9999                                       str     [V] high rail, low rail
DAC0     -9.0002,-8.7962                                      str     [V] set value, measured value
CCDSECA  [1:2057, 1:2064]                                     str     CCD section for quadrant A
CLOCK11  9.9992,2.9993                                        str     [V] high rail, low rail
CLOCK2   9.9999,0.0                                           str     [V] high rail, low rail
CLOCK9   9.9992,2.9993                                        str     [V] high rail, low rail
CLOCK17  9.0,0.9999                                           str     [V] high rail, low rail
ORSECC   [8:2064, 2098:2129]                                  str     Row overscan section for quadrant C
CCDSECC  [1:2057, 2065:4128]                                  str     CCD section for quadrant C
PRESECD  [4250:4256, 2130:4193]                               str     Prescan section for quadrant D
BIASSECD [2129:2192, 2130:4193]                               str     Bias section for quadrant D
AMPSECB  [4114:2058, 1:2064]                                  str     AMP section for quadrant B
CCDCFG   default_lbnl_20210128.cfg                            str     CCD configuration file
BIASSECB [2129:2192, 2:2065]                                  str     Bias section for quadrant B
BIASSECC [2065:2128, 2130:4193]                               str     Bias section for quadrant C
CLOCK16  9.9999,3.0                                           str     [V] high rail, low rail
CCDPREP  purge,clear                                          str     CCD prep actions
DAC8     -25.0003,-24.8273                                    str     [V] set value, measured value
PRRSECA  [8:2064, 1:1]                                        str     Row prescan section for quadrant A
DATASECD [2193:4249, 2130:4193]                               str     Data section for quadrant D
DAC5     5.9998,6.0806                                        str     [V] set value, measured value
PRESECC  [1:7, 2130:4193]                                     str     Prescan section for quadrant C
OFFSET1  0.4000000059604645,-8.8786                           str     [V] set value, measured value
OFFSET4  2.0,6.0595                                           str     [V] set value, measured value
DAC7     5.9998,5.9964                                        str     [V] set value, measured value
DAC6     5.9998,6.0963                                        str     [V] set value, measured value
OFFSET7  2.0,5.9911                                           str     [V] set value, measured value
DETSECC  [1:2057, 2065:4128]                                  str     Detector section for quadrant C
TRIMSECD [2193:4249, 2130:4193]                               str     Trim section for quadrant D
CCDSECB  [2058:4114, 1:2064]                                  str     CCD section for quadrant B
REQTIME  1860.0                                               float   [s] Requested exposure time
OBSID    kp4m20220114t110417                                  str     Unique observation identifier
PROCTYPE RAW                                                  str     Data processing level
PRODTYPE image                                                str     Data product type
CHECKSUM mqJSonIQmnIQmnIQ                                     str     HDU checksum updated 2022-01-14T11:15:05
DATASUM  3453799606                                           str     data unit checksum updated 2022-01-14T11:15:05
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 4256x4194]

HDU15
-----

EXTNAME = R0

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   4194                                                 int     number of rows in table
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
EXPID    118526                                               int     Exposure number
EXPFRAME 0                                                    int     Frame number
FRAMES   None                                                 Unknown Number of Frames in Archive
TILEID   4403                                                 int     DESI Tile ID
FIBASSGN /data/tiles/SVN_tiles/004/fiberassign-004403.fits.gz str     Fiber assign
FLAVOR   science                                              str     Observation type
SEQUENCE _Split                                               str     OCS Sequence name
PURPOSE  Main Survey                                          str     Purpose of observing night
PROGRAM  DARK                                                 str     Program name
PROPID   2020B-5000                                           str     Proposal ID
OBSERVER Jessica Chellino, Corentin Ravoux                    str     Names of observers
LEAD     Martin Landriau                                      str     Lead observer
INSTRUME DESI                                                 str     Instrument name
OBSERVAT KPNO                                                 str     Observatory name
OBS-LAT  31.96403                                             str     [deg] Observatory latitude
OBS-LONG -111.59989                                           str     [deg] Observatory east longitude
OBS-ELEV 2097.0                                               float   [m] Observatory elevation
TELESCOP KPNO 4.0-m telescope                                 str     Telescope name
CORRCTOR DESI Corrector                                       str     Corrector Identification
NIGHT    20220113                                             int     Observing night
TIMESYS  UTC                                                  str     Time system used for date-obs
DATE-OBS 2022-01-14T11:04:17.790636032                        str     [UTC] Observation data and start tim
TIME-OBS 2022-01-14T11:04:17.790636032                        str     [UTC] Observation start time
MJD-OBS  59593.46131702                                       float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:04:18.577390                           str     Time shutter opened
ST       11:13:28.540000                                      str     Local Sidereal time at observation start (HH:MM
EXPTIME  579.193                                              float   [s] Actual exposure time
REQRA    170.239                                              float   [deg] Requested right ascension (observer input
REQDEC   -7.093                                               float   [deg] Requested declination (observer input)
FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                   str     Telescope focus settings
VCCD     ON                                                   str     True (ON) if CCD voltage is on
VCCDON   2022-01-10T20:55:36.972453                           str     Time when CCD voltage was turned on
VCCDSEC  310758.6                                             float   [s] CCD on time in seconds
TRUSTEMP 12.267                                               float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.675                                               float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                               float   Epoch of observation
MOUNTAZ  176.725567                                           float   [deg] Mount azimuth angle
MOUNTDEC -7.102329                                            float   [deg] Mount declination
MOUNTEL  50.883914                                            float   [deg] Mount elevation angle
MOUNTHA  -2.081118                                            float   [deg] Mount hour angle
SKYDEC   -7.102329                                            float   [deg] Telescope declination (pointing on sky)
SKYRA    170.24163                                            float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.102329                                            float   [deg] Target declination (to TCS)
TARGTRA  170.24163                                            float   [deg] Target right ascension (to TCS)
USEETC   T                                                    bool    ETC data available if true
USESKY   T                                                    bool    DOS Control: use Sky Monitor
USEFOCUS T                                                    bool    DOS Control: use focus
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                              str     Hexapod trim values
USEROTAT T                                                    bool    DOS Control: use rotator
ROTOFFST 138.8                                                float   [arcsec] Rotator offset
ROTENBLD T                                                    bool    Rotator enabled
ROTRATE  0.513                                                float   [arcsec/min] Rotator rate
USEGUIDR T                                                    bool    DOS Control: use guider
USEDONUT T                                                    bool    DOS Control: use donuts
SPECGRPH 0                                                    int     Spectrograph logical name (SP)
SPECID   4                                                    int     Spectrograph serial number (SM)
FEEBOX   lbnl078                                              str     CCD Controller serial number
VESSEL   14                                                   int     Cryostat serial number
FEEVER   v20160312                                            str     CCD Controller version
DETFLVER FAILED: invalid argument for get command             str     CCD Controller detector f
FEEPOWER ON                                                   str     FEE power status
FEEDMASK 2134851391                                           int     FEE dac mask
FEECMASK 1048575                                              int     FEE clk mask
CCDTEMP  -142.1871                                            float   [deg C] CCD controller CCD temperature
RADESYS  FK5                                                  str     Coordinate reference frame of major/minor axes
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
CLOCK14  9.9992,2.9993                                        str     [V] high rail, low rail
DETSECD  [2058:4114, 2065:4128]                               str     Detector section for quadrant D
DETSECC  [1:2057, 2065:4128]                                  str     Detector section for quadrant C
TRIMSECB [2193:4249, 2:2065]                                  str     Trim section for quadrant B
DAC5     5.9998,6.028                                         str     [V] set value, measured value
CCDSIZE  4194,4256                                            str     CCD size in pixels (rows, columns)
DAC3     -9.0002,-8.9095                                      str     [V] set value, measured value
PRESECC  [1:7, 2130:4193]                                     str     Prescan section for quadrant C
CLOCK18  9.0,0.9999                                           str     [V] high rail, low rail
CLOCK7   -2.0001,3.9999                                       str     [V] high rail, low rail
DAC6     5.9998,5.9911                                        str     [V] set value, measured value
TRIMSECD [2193:4249, 2130:4193]                               str     Trim section for quadrant D
DAC11    -25.0003,-24.3673                                    str     [V] set value, measured value
DAC10    -25.0003,-24.3524                                    str     [V] set value, measured value
DAC4     5.9998,6.0174                                        str     [V] set value, measured value
CLOCK10  9.9992,2.9993                                        str     [V] high rail, low rail
ORSECD   [2193:4249, 2098:2129]                               str     Row bias section for quadrant D
CCDSECD  [2058:4114, 2065:4128]                               str     CCD section for quadrant D
CLOCK11  9.9992,2.9993                                        str     [V] high rail, low rail
CLOCK5   9.9999,0.0                                           str     [V] high rail, low rail
PRRSECA  [8:2064, 1:1]                                        str     Row prescan section for quadrant A
DETSECA  [1:2057, 1:2064]                                     str     Detector section for quadrant A
CDSPARMS 400, 400, 8, 2000                                    str     CDS parameters
DAC15    0.0,-0.0148                                          str     [V] set value, measured value
AMPSECA  [1:2057, 1:2064]                                     str     AMP section for quadrant A
CLOCK4   9.9999,0.0                                           str     [V] high rail, low rail
CCDSECA  [1:2057, 1:2064]                                     str     CCD section for quadrant A
DAC17    20.0008,11.9316                                      str     [V] set value, measured value
BIASSECA [2065:2128, 2:2065]                                  str     Bias section for quadrant A
CCDTMING flatdark_lbnl_timing.txt                             str     CCD timing file
ORSECC   [8:2064, 2098:2129]                                  str     Row overscan section for quadrant C
DAC2     -9.0002,-8.9301                                      str     [V] set value, measured value
DATASECD [2193:4249, 2130:4193]                               str     Data section for quadrant D
CLOCK15  9.9992,2.9993                                        str     [V] high rail, low rail
CLOCK16  9.9999,3.0                                           str     [V] high rail, low rail
CLOCK17  9.0,0.9999                                           str     [V] high rail, low rail
ORSECB   [2193:4249, 2066:2097]                               str     Row overscan section for quadrant B
CLOCK13  9.9992,2.9993                                        str     [V] high rail, low rail
PGAGAIN  3                                                    int     Controller gain
TRIMSECA [8:2064, 2:2065]                                     str     Trim section for quadrant A
CLOCK8   9.9992,2.9993                                        str     [V] high rail, low rail
PRRSECB  [2193:4249, 1:1]                                     str     Row prescan section for quadrant B
AMPSECB  [4114:2058, 1:2064]                                  str     AMP section for quadrant B
CAMERA   r0                                                   str     Camera name
ORSECA   [8:2064, 2066:2097]                                  str     Row overscan section for quadrant A
DAC12    0.0,0.0                                              str     [V] set value, measured value
AMPSECC  [1:2057, 4128:2065]                                  str     AMP section for quadrant C
PRRSECC  [8:2064, 4194:4194]                                  str     Row prescan section for quadrant C
DATASECC [8:2064, 2130:4193]                                  str     Data section for quadrant C
CLOCK2   9.9999,0.0                                           str     [V] high rail, low rail
DETECTOR M1-49                                                str     Detector (ccd) identification
OFFSET0  0.4000000059604645,-8.9198                           str     [V] set value, measured value
BIASSECC [2065:2128, 2130:4193]                               str     Bias section for quadrant C
BIASSECB [2129:2192, 2:2065]                                  str     Bias section for quadrant B
DAC1     -9.0002,-8.858                                       str     [V] set value, measured value
AMPSECD  [4114:2058, 4128:2065]                               str     AMP section for quadrant D
OFFSET4  2.0,6.0174                                           str     [V] set value, measured value
TRIMSECC [8:2064, 2130:4193]                                  str     Trim section for quadrant C
DATASECB [2193:4249, 2:2065]                                  str     Data section for quadrant B
CCDPREP  purge,clear                                          str     CCD prep actions
DAC0     -9.0002,-8.9198                                      str     [V] set value, measured value
OFFSET3  0.4000000059604645,-8.9095                           str     [V] set value, measured value
PRESECA  [1:7, 2:2065]                                        str     Prescan section for quadrant A
CASETEMP 56.8611                                              float   [deg C] CCD controller case temperature
DAC7     5.9998,6.028                                         str     [V] set value, measured value
CRYOTEMP 163.02                                               float   [deg K] Cryostat CCD temperature
OFFSET5  2.0,6.028                                            str     [V] set value, measured value
SETTINGS detectors_sm_20210128.json                           str     Name of DESI CCD settings file
CLOCK3   -2.0001,3.9999                                       str     [V] high rail, low rail
CCDCFG   default_lbnl_20210128.cfg                            str     CCD configuration file
DETSECB  [2058:4114, 1:2064]                                  str     Detector section for quadrant B
DAC13    0.0,0.0148                                           str     [V] set value, measured value
DIGITIME 56.4576                                              float   [s] Time to digitize image
CPUTEMP  58.2246                                              float   [deg C] CCD controller CPU temperature
PRRSECD  [2193:4249, 4194:4194]                               str     Row prescan section for quadrant D
DAC9     -25.0003,-24.5305                                    str     [V] set value, measured value
CRYOPRES 1.001e-07                                            str     [mb] Cryostat pressure (IP)
CCDSECC  [1:2057, 2065:4128]                                  str     CCD section for quadrant C
DELAYS   20, 20, 25, 40, 7, 3000, 7, 7, 400, 7                str     [10] Delay settings
CLOCK1   9.9999,0.0                                           str     [V] high rail, low rail
CLOCK6   9.9999,0.0                                           str     [V] high rail, low rail
CLOCK9   9.9992,2.9993                                        str     [V] high rail, low rail
CLOCK12  9.9992,2.9993                                        str     [V] high rail, low rail
CCDNAME  CCDSM4R                                              str     CCD name
DAC8     -25.0003,-24.9312                                    str     [V] set value, measured value
OFFSET1  0.4000000059604645,-8.858                            str     [V] set value, measured value
BLDTIME  0.3524                                               float   [s] Time to build image
OFFSET2  0.4000000059604645,-8.9301                           str     [V] set value, measured value
PRESECB  [4250:4256, 2:2065]                                  str     Prescan section for quadrant B
DAC16    39.9961,39.5934                                      str     [V] set value, measured value
CLOCK0   9.9999,0.0                                           str     [V] high rail, low rail
DAC14    0.0,-0.0148                                          str     [V] set value, measured value
OFFSET6  2.0,5.9911                                           str     [V] set value, measured value
OFFSET7  2.0,6.0332                                           str     [V] set value, measured value
CCDSECB  [2058:4114, 1:2064]                                  str     CCD section for quadrant B
PRESECD  [4250:4256, 2130:4193]                               str     Prescan section for quadrant D
DATASECA [8:2064, 2:2065]                                     str     Data section for quadrant A
BIASSECD [2129:2192, 2130:4193]                               str     Bias section for quadrant D
REQTIME  1860.0                                               float   [s] Requested exposure time
OBSID    kp4m20220114t110417                                  str     Unique observation identifier
PROCTYPE RAW                                                  str     Data processing level
PRODTYPE image                                                str     Data product type
CHECKSUM 1Lmb3JkZ1Jkb1JkZ                                     str     HDU checksum updated 2022-01-14T11:15:06
DATASUM  2569830282                                           str     data unit checksum updated 2022-01-14T11:15:06
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 4256x4194]

HDU16
-----

EXTNAME = B0

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   4162                                                 int     number of rows in table
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
EXPID    118526                                               int     Exposure number
EXPFRAME 0                                                    int     Frame number
FRAMES   None                                                 Unknown Number of Frames in Archive
TILEID   4403                                                 int     DESI Tile ID
FIBASSGN /data/tiles/SVN_tiles/004/fiberassign-004403.fits.gz str     Fiber assign
FLAVOR   science                                              str     Observation type
SEQUENCE _Split                                               str     OCS Sequence name
PURPOSE  Main Survey                                          str     Purpose of observing night
PROGRAM  DARK                                                 str     Program name
PROPID   2020B-5000                                           str     Proposal ID
OBSERVER Jessica Chellino, Corentin Ravoux                    str     Names of observers
LEAD     Martin Landriau                                      str     Lead observer
INSTRUME DESI                                                 str     Instrument name
OBSERVAT KPNO                                                 str     Observatory name
OBS-LAT  31.96403                                             str     [deg] Observatory latitude
OBS-LONG -111.59989                                           str     [deg] Observatory east longitude
OBS-ELEV 2097.0                                               float   [m] Observatory elevation
TELESCOP KPNO 4.0-m telescope                                 str     Telescope name
CORRCTOR DESI Corrector                                       str     Corrector Identification
NIGHT    20220113                                             int     Observing night
TIMESYS  UTC                                                  str     Time system used for date-obs
DATE-OBS 2022-01-14T11:04:17.790636032                        str     [UTC] Observation data and start tim
TIME-OBS 2022-01-14T11:04:17.790636032                        str     [UTC] Observation start time
MJD-OBS  59593.46131702                                       float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:04:18.577390                           str     Time shutter opened
ST       11:13:28.540000                                      str     Local Sidereal time at observation start (HH:MM
EXPTIME  579.193                                              float   [s] Actual exposure time
REQRA    170.239                                              float   [deg] Requested right ascension (observer input
REQDEC   -7.093                                               float   [deg] Requested declination (observer input)
FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                   str     Telescope focus settings
VCCD     ON                                                   str     True (ON) if CCD voltage is on
VCCDON   2022-01-10T20:55:39.335418                           str     Time when CCD voltage was turned on
VCCDSEC  310754.5                                             float   [s] CCD on time in seconds
TRUSTEMP 12.267                                               float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.675                                               float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                               float   Epoch of observation
MOUNTAZ  176.725567                                           float   [deg] Mount azimuth angle
MOUNTDEC -7.102329                                            float   [deg] Mount declination
MOUNTEL  50.883914                                            float   [deg] Mount elevation angle
MOUNTHA  -2.081118                                            float   [deg] Mount hour angle
SKYDEC   -7.102329                                            float   [deg] Telescope declination (pointing on sky)
SKYRA    170.24163                                            float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.102329                                            float   [deg] Target declination (to TCS)
TARGTRA  170.24163                                            float   [deg] Target right ascension (to TCS)
USEETC   T                                                    bool    ETC data available if true
USESKY   T                                                    bool    DOS Control: use Sky Monitor
USEFOCUS T                                                    bool    DOS Control: use focus
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                              str     Hexapod trim values
USEROTAT T                                                    bool    DOS Control: use rotator
ROTOFFST 138.8                                                float   [arcsec] Rotator offset
ROTENBLD T                                                    bool    Rotator enabled
ROTRATE  0.513                                                float   [arcsec/min] Rotator rate
USEGUIDR T                                                    bool    DOS Control: use guider
USEDONUT T                                                    bool    DOS Control: use donuts
SPECGRPH 0                                                    int     Spectrograph logical name (SP)
SPECID   4                                                    int     Spectrograph serial number (SM)
FEEBOX   lbnl081                                              str     CCD Controller serial number
VESSEL   15                                                   int     Cryostat serial number
FEEVER   v20160312                                            str     CCD Controller version
DETFLVER FAILED: invalid argument for get command             str     CCD Controller detector f
FEEPOWER ON                                                   str     FEE power status
FEEDMASK 2134851391                                           int     FEE dac mask
FEECMASK 1048575                                              int     FEE clk mask
CCDTEMP  850.0                                                float   [deg C] CCD controller CCD temperature
RADESYS  FK5                                                  str     Coordinate reference frame of major/minor axes
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
CLOCK7   6.9999,-2.0001                                       str     [V] high rail, low rail
CLOCK1   3.9999,-4.0002                                       str     [V] high rail, low rail
CAMERA   b0                                                   str     Camera name
AMPSECC  [2048:1, 2049:4096]                                  str     AMP section for quadrant C
DAC9     26.9998,26.9346                                      str     [V] set value, measured value
DAC4     0.0,0.0105                                           str     [V] set value, measured value
PRESECD  [4229:4232, 2114:4161]                               str     Prescan section for quadrant D
CCDNAME  CCDSM4B                                              str     CCD name
OFFSET3  -1.5,15.9547                                         str     [V] set value, measured value
DELAYS   13, 13, 25, 25, 8, 3000, 7, 7, 400, 7                str     [10] Delay settings
DAC12    4.9997,22.62                                         str     [V] set value, measured value
PGAGAIN  5                                                    int     Controller gain
OFFSET6  -1.100000023841858,0.0158                            str     [V] set value, measured value
CLOCK10  3.0,-7.0002                                          str     [V] high rail, low rail
CCDCFG   default_sta_20210128.cfg                             str     CCD configuration file
AMPSECB  [2049:4096, 2048:1]                                  str     AMP section for quadrant B
DAC16    0.0,65.5116                                          str     [V] set value, measured value
DIGITIME 54.7878                                              float   [s] Time to digitize image
CLOCK6   3.9999,-4.0002                                       str     [V] high rail, low rail
DAC15    19.9997,20.072                                       str     [V] set value, measured value
OFFSET5  -1.100000023841858,0.0105                            str     [V] set value, measured value
PRESECB  [4229:4232, 2:2049]                                  str     Prescan section for quadrant B
PRESECA  [1:4, 2:2049]                                        str     Prescan section for quadrant A
CCDSIZE  4162,4232                                            str     CCD size in pixels (rows, columns)
CCDSECA  [1:2048, 1:2048]                                     str     CCD section for quadrant A
AMPSECA  [1:2048, 1:2048]                                     str     AMP section for quadrant A
DAC10    26.9998,26.8307                                      str     [V] set value, measured value
OFFSET4  -1.100000023841858,0.0053                            str     [V] set value, measured value
PRRSECC  [5:2052, 4162:4162]                                  str     Row prescan section for quadrant C
PRRSECD  [2181:4228, 4162:4162]                               str     Row prescan section for quadrant D
CLOCK16  0.0,0.0                                              str     [V] high rail, low rail
CCDSECB  [2049:4096, 1:2048]                                  str     CCD section for quadrant B
DATASECB [2181:4228, 2:2049]                                  str     Data section for quadrant B
CLOCK8   3.0,-7.0002                                          str     [V] high rail, low rail
SETTINGS detectors_sm_20210128.json                           str     Name of DESI CCD settings file
BIASSECB [2117:2180, 2:2049]                                  str     Bias section for quadrant B
CLOCK11  0.0,0.0                                              str     [V] high rail, low rail
DATASECC [5:2052, 2114:4161]                                  str     Data section for quadrant C
DAC5     0.0,0.0105                                           str     [V] set value, measured value
PRESECC  [1:4, 2114:4161]                                     str     Prescan section for quadrant C
CLOCK12  3.0,-7.0002                                          str     [V] high rail, low rail
BLDTIME  0.3514                                               float   [s] Time to build image
CASETEMP 56.4919                                              float   [deg C] CCD controller case temperature
OFFSET7  -1.100000023841858,0.0105                            str     [V] set value, measured value
DAC1     15.9998,15.8105                                      str     [V] set value, measured value
CCDSECD  [2049:4096, 2049:4096]                               str     CCD section for quadrant D
DATASECA [5:2052, 2:2049]                                     str     Data section for quadrant A
CLOCK15  0.0,0.0                                              str     [V] high rail, low rail
CLOCK13  3.0,-7.0002                                          str     [V] high rail, low rail
CLOCK2   3.9999,-4.0002                                       str     [V] high rail, low rail
DAC8     26.9998,26.6081                                      str     [V] set value, measured value
CPUTEMP  56.5019                                              float   [deg C] CCD controller CPU temperature
CDSPARMS 400, 400, 8, 1000                                    str     CDS parameters
PRRSECB  [2181:4228, 1:1]                                     str     Row prescan section for quadrant B
DATASECD [2181:4228, 2114:4161]                               str     Data section for quadrant D
DAC11    26.9998,26.9049                                      str     [V] set value, measured value
ORSECB   [2181:4228, 2050:2081]                               str     Row overscan section for quadrant B
DAC0     15.9998,15.965                                       str     [V] set value, measured value
DETSECD  [2049:4096, 2049:4096]                               str     Detector section for quadrant D
ORSECC   [5:2052, 2082:2113]                                  str     Row overscan section for quadrant C
DETSECC  [1:2048, 2049:4096]                                  str     Detector section for quadrant C
DETSECA  [1:2048, 1:2048]                                     str     Detector section for quadrant A
DAC3     15.9998,15.965                                       str     [V] set value, measured value
CRYOPRES 1.001e-07                                            str     [mb] Cryostat pressure (IP)
DAC6     0.0,0.0158                                           str     [V] set value, measured value
CLOCK0   3.9999,-4.0002                                       str     [V] high rail, low rail
OFFSET2  -1.5,15.8311                                         str     [V] set value, measured value
PRRSECA  [5:2052, 1:1]                                        str     Row prescan section for quadrant A
CLOCK4   3.9999,-4.0002                                       str     [V] high rail, low rail
TRIMSECB [2181:4228, 2:2049]                                  str     Trim section for quadrant B
TRIMSECC [5:2052, 2114:4161]                                  str     Trim section for quadrant C
CRYOTEMP 163.02                                               float   [deg K] Cryostat CCD temperature
CLOCK17  3.9999,-4.0002                                       str     [V] high rail, low rail
TRIMSECA [5:2052, 2:2049]                                     str     Trim section for quadrant A
CCDPREP  purge,clear                                          str     CCD prep actions
BIASSECC [2053:2116, 2114:4161]                               str     Bias section for quadrant C
CLOCK5   3.9999,-4.0002                                       str     [V] high rail, low rail
TRIMSECD [2181:4228, 2114:4161]                               str     Trim section for quadrant D
CCDTMING flatdark_sta_timing.txt                              str     CCD timing file
DETSECB  [2049:4096, 1:2048]                                  str     Detector section for quadrant B
DAC14    0.0,0.8216                                           str     [V] set value, measured value
DAC2     15.9998,15.8208                                      str     [V] set value, measured value
CLOCK3   6.9999,-2.0001                                       str     [V] high rail, low rail
ORSECA   [5:2052, 2050:2081]                                  str     Row overscan section for quadrant A
CLOCK14  3.0,-7.0002                                          str     [V] high rail, low rail
DAC7     0.0,0.0053                                           str     [V] set value, measured value
CLOCK9   3.0,-7.0002                                          str     [V] high rail, low rail
BIASSECD [2117:2180, 2114:4161]                               str     Bias section for quadrant D
CLOCK18  3.9999,-4.0002                                       str     [V] high rail, low rail
CCDSECC  [1:2048, 2049:4096]                                  str     CCD section for quadrant C
AMPSECD  [4096:2049, 4096:2049]                               str     AMP section for quadrant D
DAC13    -5.0006,-4.9816                                      str     [V] set value, measured value
DETECTOR sn22797                                              str     Detector (ccd) identification
OFFSET1  -1.5,15.8208                                         str     [V] set value, measured value
ORSECD   [2181:4228, 2082:2113]                               str     Row bias section for quadrant D
DAC17    -0.0,0.0366                                          str     [V] set value, measured value
BIASSECA [2053:2116, 2:2049]                                  str     Bias section for quadrant A
OFFSET0  -1.5,15.965                                          str     [V] set value, measured value
REQTIME  1860.0                                               float   [s] Requested exposure time
OBSID    kp4m20220114t110417                                  str     Unique observation identifier
PROCTYPE RAW                                                  str     Data processing level
PRODTYPE image                                                str     Data product type
CHECKSUM ZgkehdkbZdkbfdkb                                     str     HDU checksum updated 2022-01-14T11:15:06
DATASUM  4200929096                                           str     data unit checksum updated 2022-01-14T11:15:06
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 4232x4162]

HDU17
-----

EXTNAME = Z5

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   4194                                                 int     number of rows in table
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
EXPID    118526                                               int     Exposure number
EXPFRAME 0                                                    int     Frame number
FRAMES   None                                                 Unknown Number of Frames in Archive
TILEID   4403                                                 int     DESI Tile ID
FIBASSGN /data/tiles/SVN_tiles/004/fiberassign-004403.fits.gz str     Fiber assign
FLAVOR   science                                              str     Observation type
SEQUENCE _Split                                               str     OCS Sequence name
PURPOSE  Main Survey                                          str     Purpose of observing night
PROGRAM  DARK                                                 str     Program name
PROPID   2020B-5000                                           str     Proposal ID
OBSERVER Jessica Chellino, Corentin Ravoux                    str     Names of observers
LEAD     Martin Landriau                                      str     Lead observer
INSTRUME DESI                                                 str     Instrument name
OBSERVAT KPNO                                                 str     Observatory name
OBS-LAT  31.96403                                             str     [deg] Observatory latitude
OBS-LONG -111.59989                                           str     [deg] Observatory east longitude
OBS-ELEV 2097.0                                               float   [m] Observatory elevation
TELESCOP KPNO 4.0-m telescope                                 str     Telescope name
CORRCTOR DESI Corrector                                       str     Corrector Identification
NIGHT    20220113                                             int     Observing night
TIMESYS  UTC                                                  str     Time system used for date-obs
DATE-OBS 2022-01-14T11:04:17.831962880                        str     [UTC] Observation data and start tim
TIME-OBS 2022-01-14T11:04:17.831962880                        str     [UTC] Observation start time
MJD-OBS  59593.4613175                                        float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:04:18.619392                           str     Time shutter opened
ST       11:13:28.580000                                      str     Local Sidereal time at observation start (HH:MM
EXPTIME  579.101                                              float   [s] Actual exposure time
REQRA    170.239                                              float   [deg] Requested right ascension (observer input
REQDEC   -7.093                                               float   [deg] Requested declination (observer input)
FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                   str     Telescope focus settings
VCCD     ON                                                   str     True (ON) if CCD voltage is on
VCCDON   2022-01-10T20:55:43.742514                           str     Time when CCD voltage was turned on
VCCDSEC  310751.8                                             float   [s] CCD on time in seconds
TRUSTEMP 12.267                                               float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.675                                               float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                               float   Epoch of observation
MOUNTAZ  176.725567                                           float   [deg] Mount azimuth angle
MOUNTDEC -7.102329                                            float   [deg] Mount declination
MOUNTEL  50.883914                                            float   [deg] Mount elevation angle
MOUNTHA  -2.081118                                            float   [deg] Mount hour angle
SKYDEC   -7.102329                                            float   [deg] Telescope declination (pointing on sky)
SKYRA    170.24163                                            float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.102329                                            float   [deg] Target declination (to TCS)
TARGTRA  170.24163                                            float   [deg] Target right ascension (to TCS)
USEETC   T                                                    bool    ETC data available if true
USESKY   T                                                    bool    DOS Control: use Sky Monitor
USEFOCUS T                                                    bool    DOS Control: use focus
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                              str     Hexapod trim values
USEROTAT T                                                    bool    DOS Control: use rotator
ROTOFFST 138.8                                                float   [arcsec] Rotator offset
ROTENBLD T                                                    bool    Rotator enabled
ROTRATE  0.513                                                float   [arcsec/min] Rotator rate
USEGUIDR T                                                    bool    DOS Control: use guider
USEDONUT T                                                    bool    DOS Control: use donuts
SPECGRPH 5                                                    int     Spectrograph logical name (SP)
SPECID   9                                                    int     Spectrograph serial number (SM)
FEEBOX   lbnl058                                              str     CCD Controller serial number
VESSEL   28                                                   int     Cryostat serial number
FEEVER   v20160312                                            str     CCD Controller version
DETFLVER FAILED: invalid argument for get command             str     CCD Controller detector f
FEEPOWER ON                                                   str     FEE power status
FEEDMASK 2134851391                                           int     FEE dac mask
FEECMASK 1048575                                              int     FEE clk mask
CCDTEMP  -134.1621                                            float   [deg C] CCD controller CCD temperature
RADESYS  FK5                                                  str     Coordinate reference frame of major/minor axes
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
DAC13    0.0,0.0445                                           str     [V] set value, measured value
DAC0     -9.0002,-8.961                                       str     [V] set value, measured value
DAC16    39.9961,39.1776                                      str     [V] set value, measured value
TRIMSECD [2193:4249, 2130:4193]                               str     Trim section for quadrant D
CLOCK2   9.9999,0.0                                           str     [V] high rail, low rail
CLOCK11  9.9992,2.9993                                        str     [V] high rail, low rail
DATASECD [2193:4249, 2130:4193]                               str     Data section for quadrant D
OFFSET0  0.4000000059604645,-8.961                            str     [V] set value, measured value
OFFSET4  2.0,6.049                                            str     [V] set value, measured value
TRIMSECC [8:2064, 2130:4193]                                  str     Trim section for quadrant C
DAC12    0.0,0.0742                                           str     [V] set value, measured value
PRESECB  [4250:4256, 2:2065]                                  str     Prescan section for quadrant B
CLOCK0   9.9999,0.0                                           str     [V] high rail, low rail
CLOCK13  9.9992,2.9993                                        str     [V] high rail, low rail
PRRSECA  [8:2064, 1:1]                                        str     Row prescan section for quadrant A
CLOCK14  9.9992,2.9993                                        str     [V] high rail, low rail
PRESECA  [1:7, 2:2065]                                        str     Prescan section for quadrant A
OFFSET5  2.0,6.049                                            str     [V] set value, measured value
PRRSECC  [8:2064, 4194:4194]                                  str     Row prescan section for quadrant C
ORSECB   [2193:4249, 2066:2097]                               str     Row overscan section for quadrant B
AMPSECB  [4114:2058, 1:2064]                                  str     AMP section for quadrant B
CRYOTEMP 139.986                                              float   [deg K] Cryostat CCD temperature
CCDTMING flatdark_lbnl_timing.txt                             str     CCD timing file
CLOCK5   9.9999,0.0                                           str     [V] high rail, low rail
CLOCK12  9.9992,2.9993                                        str     [V] high rail, low rail
DAC1     -9.0002,-8.9507                                      str     [V] set value, measured value
DAC2     -9.0002,-8.8992                                      str     [V] set value, measured value
TRIMSECB [2193:4249, 2:2065]                                  str     Trim section for quadrant B
DIGITIME 56.4569                                              float   [s] Time to digitize image
DAC3     -9.0002,-8.961                                       str     [V] set value, measured value
BIASSECC [2065:2128, 2130:4193]                               str     Bias section for quadrant C
CCDNAME  CCDSM9Z                                              str     CCD name
PRESECC  [1:7, 2130:4193]                                     str     Prescan section for quadrant C
CCDPREP  purge,clear                                          str     CCD prep actions
DAC17    20.0008,12.1634                                      str     [V] set value, measured value
PRESECD  [4250:4256, 2130:4193]                               str     Prescan section for quadrant D
DETSECC  [1:2057, 2065:4128]                                  str     Detector section for quadrant C
CLOCK4   9.9999,0.0                                           str     [V] high rail, low rail
BIASSECD [2129:2192, 2130:4193]                               str     Bias section for quadrant D
CLOCK16  9.9999,3.0                                           str     [V] high rail, low rail
AMPSECA  [1:2057, 1:2064]                                     str     AMP section for quadrant A
AMPSECD  [4114:2058, 4128:2065]                               str     AMP section for quadrant D
CLOCK7   -2.0001,3.9999                                       str     [V] high rail, low rail
DELAYS   20, 20, 25, 40, 7, 3000, 7, 7, 400, 7                str     [10] Delay settings
DAC10    -25.0003,-25.1538                                    str     [V] set value, measured value
CLOCK1   9.9999,0.0                                           str     [V] high rail, low rail
CLOCK6   9.9999,0.0                                           str     [V] high rail, low rail
DATASECB [2193:4249, 2:2065]                                  str     Data section for quadrant B
CLOCK3   -2.0001,3.9999                                       str     [V] high rail, low rail
DAC14    0.0,0.0297                                           str     [V] set value, measured value
DETECTOR M1-45C                                               str     Detector (ccd) identification
DETSECA  [1:2057, 1:2064]                                     str     Detector section for quadrant A
PRRSECD  [2193:4249, 4194:4194]                               str     Row prescan section for quadrant D
DAC8     -25.0003,-25.1983                                    str     [V] set value, measured value
CLOCK8   9.9992,2.9993                                        str     [V] high rail, low rail
CRYOPRES 8.072e-08                                            str     [mb] Cryostat pressure (IP)
OFFSET7  2.0,6.0227                                           str     [V] set value, measured value
OFFSET6  2.0,6.028                                            str     [V] set value, measured value
CCDSECA  [1:2057, 1:2064]                                     str     CCD section for quadrant A
CCDSECB  [2058:4114, 1:2064]                                  str     CCD section for quadrant B
CASETEMP 59.9372                                              float   [deg C] CCD controller case temperature
DETSECB  [2058:4114, 1:2064]                                  str     Detector section for quadrant B
CCDSECD  [2058:4114, 2065:4128]                               str     CCD section for quadrant D
BIASSECA [2065:2128, 2:2065]                                  str     Bias section for quadrant A
ORSECA   [8:2064, 2066:2097]                                  str     Row overscan section for quadrant A
CDSPARMS 400, 400, 8, 2000                                    str     CDS parameters
DAC5     5.9998,6.049                                         str     [V] set value, measured value
CCDSIZE  4194,4256                                            str     CCD size in pixels (rows, columns)
BIASSECB [2129:2192, 2:2065]                                  str     Bias section for quadrant B
CLOCK15  9.9992,2.9993                                        str     [V] high rail, low rail
CAMERA   z5                                                   str     Camera name
OFFSET1  0.4000000059604645,-8.961                            str     [V] set value, measured value
DATASECA [8:2064, 2:2065]                                     str     Data section for quadrant A
DETSECD  [2058:4114, 2065:4128]                               str     Detector section for quadrant D
SETTINGS detectors_sm_20210128.json                           str     Name of DESI CCD settings file
OFFSET3  0.4000000059604645,-8.9713                           str     [V] set value, measured value
CCDSECC  [1:2057, 2065:4128]                                  str     CCD section for quadrant C
DAC4     5.9998,6.049                                         str     [V] set value, measured value
DAC6     5.9998,6.028                                         str     [V] set value, measured value
PGAGAIN  3                                                    int     Controller gain
CPUTEMP  59.9472                                              float   [deg C] CCD controller CPU temperature
ORSECD   [2193:4249, 2098:2129]                               str     Row bias section for quadrant D
PRRSECB  [2193:4249, 1:1]                                     str     Row prescan section for quadrant B
CLOCK10  9.9992,2.9993                                        str     [V] high rail, low rail
DATASECC [8:2064, 2130:4193]                                  str     Data section for quadrant C
DAC7     5.9998,6.028                                         str     [V] set value, measured value
ORSECC   [8:2064, 2098:2129]                                  str     Row overscan section for quadrant C
CLOCK9   9.9992,2.9993                                        str     [V] high rail, low rail
DAC11    -25.0003,-24.6196                                    str     [V] set value, measured value
BLDTIME  0.3573                                               float   [s] Time to build image
DAC9     -25.0003,-24.946                                     str     [V] set value, measured value
CLOCK18  9.0,0.9999                                           str     [V] high rail, low rail
CCDCFG   default_lbnl_20210128.cfg                            str     CCD configuration file
DAC15    0.0,0.0148                                           str     [V] set value, measured value
CLOCK17  9.0,0.9999                                           str     [V] high rail, low rail
OFFSET2  0.4000000059604645,-8.9095                           str     [V] set value, measured value
TRIMSECA [8:2064, 2:2065]                                     str     Trim section for quadrant A
AMPSECC  [1:2057, 4128:2065]                                  str     AMP section for quadrant C
REQTIME  1860.0                                               float   [s] Requested exposure time
OBSID    kp4m20220114t110417                                  str     Unique observation identifier
PROCTYPE RAW                                                  str     Data processing level
PRODTYPE image                                                str     Data product type
CHECKSUM Y1Ana09nT0AnY09n                                     str     HDU checksum updated 2022-01-14T11:15:06
DATASUM  449430340                                            str     data unit checksum updated 2022-01-14T11:15:06
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 4256x4194]

HDU18
-----

EXTNAME = R5

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   4194                                                 int     number of rows in table
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
EXPID    118526                                               int     Exposure number
EXPFRAME 0                                                    int     Frame number
FRAMES   None                                                 Unknown Number of Frames in Archive
TILEID   4403                                                 int     DESI Tile ID
FIBASSGN /data/tiles/SVN_tiles/004/fiberassign-004403.fits.gz str     Fiber assign
FLAVOR   science                                              str     Observation type
SEQUENCE _Split                                               str     OCS Sequence name
PURPOSE  Main Survey                                          str     Purpose of observing night
PROGRAM  DARK                                                 str     Program name
PROPID   2020B-5000                                           str     Proposal ID
OBSERVER Jessica Chellino, Corentin Ravoux                    str     Names of observers
LEAD     Martin Landriau                                      str     Lead observer
INSTRUME DESI                                                 str     Instrument name
OBSERVAT KPNO                                                 str     Observatory name
OBS-LAT  31.96403                                             str     [deg] Observatory latitude
OBS-LONG -111.59989                                           str     [deg] Observatory east longitude
OBS-ELEV 2097.0                                               float   [m] Observatory elevation
TELESCOP KPNO 4.0-m telescope                                 str     Telescope name
CORRCTOR DESI Corrector                                       str     Corrector Identification
NIGHT    20220113                                             int     Observing night
TIMESYS  UTC                                                  str     Time system used for date-obs
DATE-OBS 2022-01-14T11:04:17.831962880                        str     [UTC] Observation data and start tim
TIME-OBS 2022-01-14T11:04:17.831962880                        str     [UTC] Observation start time
MJD-OBS  59593.4613175                                        float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:04:18.619392                           str     Time shutter opened
ST       11:13:28.580000                                      str     Local Sidereal time at observation start (HH:MM
EXPTIME  579.101                                              float   [s] Actual exposure time
REQRA    170.239                                              float   [deg] Requested right ascension (observer input
REQDEC   -7.093                                               float   [deg] Requested declination (observer input)
FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                   str     Telescope focus settings
VCCD     ON                                                   str     True (ON) if CCD voltage is on
VCCDON   2022-01-10T20:55:36.978232                           str     Time when CCD voltage was turned on
VCCDSEC  310758.6                                             float   [s] CCD on time in seconds
TRUSTEMP 12.267                                               float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.675                                               float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                               float   Epoch of observation
MOUNTAZ  176.725567                                           float   [deg] Mount azimuth angle
MOUNTDEC -7.102329                                            float   [deg] Mount declination
MOUNTEL  50.883914                                            float   [deg] Mount elevation angle
MOUNTHA  -2.081118                                            float   [deg] Mount hour angle
SKYDEC   -7.102329                                            float   [deg] Telescope declination (pointing on sky)
SKYRA    170.24163                                            float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.102329                                            float   [deg] Target declination (to TCS)
TARGTRA  170.24163                                            float   [deg] Target right ascension (to TCS)
USEETC   T                                                    bool    ETC data available if true
USESKY   T                                                    bool    DOS Control: use Sky Monitor
USEFOCUS T                                                    bool    DOS Control: use focus
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                              str     Hexapod trim values
USEROTAT T                                                    bool    DOS Control: use rotator
ROTOFFST 138.8                                                float   [arcsec] Rotator offset
ROTENBLD T                                                    bool    Rotator enabled
ROTRATE  0.513                                                float   [arcsec/min] Rotator rate
USEGUIDR T                                                    bool    DOS Control: use guider
USEDONUT T                                                    bool    DOS Control: use donuts
SPECGRPH 5                                                    int     Spectrograph logical name (SP)
SPECID   9                                                    int     Spectrograph serial number (SM)
FEEBOX   lbnl057                                              str     CCD Controller serial number
VESSEL   26                                                   int     Cryostat serial number
FEEVER   v20160312                                            str     CCD Controller version
DETFLVER FAILED: invalid argument for get command             str     CCD Controller detector f
FEEPOWER ON                                                   str     FEE power status
FEEDMASK 2134851391                                           int     FEE dac mask
FEECMASK 1048575                                              int     FEE clk mask
CCDTEMP  -135.8177                                            float   [deg C] CCD controller CCD temperature
RADESYS  FK5                                                  str     Coordinate reference frame of major/minor axes
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
ORSECB   [2193:4249, 2066:2097]                               str     Row overscan section for quadrant B
DAC12    0.0,0.0148                                           str     [V] set value, measured value
CLOCK3   -2.0001,3.9999                                       str     [V] high rail, low rail
CLOCK2   9.9999,0.0                                           str     [V] high rail, low rail
DAC13    0.0,0.0                                              str     [V] set value, measured value
DAC11    -25.0003,-24.5305                                    str     [V] set value, measured value
TRIMSECA [8:2064, 2:2065]                                     str     Trim section for quadrant A
BLDTIME  0.3512                                               float   [s] Time to build image
CLOCK6   9.9999,0.0                                           str     [V] high rail, low rail
OFFSET0  0.4000000059604645,-8.755                            str     [V] set value, measured value
OFFSET7  2.0,6.0069                                           str     [V] set value, measured value
CCDSECD  [2058:4114, 2065:4128]                               str     CCD section for quadrant D
DAC4     5.9998,6.0595                                        str     [V] set value, measured value
AMPSECB  [4114:2058, 1:2064]                                  str     AMP section for quadrant B
PRRSECC  [8:2064, 4194:4194]                                  str     Row prescan section for quadrant C
CCDTMING flatdark_lbnl_timing.txt                             str     CCD timing file
TRIMSECD [2193:4249, 2130:4193]                               str     Trim section for quadrant D
BIASSECC [2065:2128, 2130:4193]                               str     Bias section for quadrant C
DAC6     5.9998,6.0437                                        str     [V] set value, measured value
CLOCK17  9.0,0.9999                                           str     [V] high rail, low rail
CCDSIZE  4194,4256                                            str     CCD size in pixels (rows, columns)
CLOCK4   9.9999,0.0                                           str     [V] high rail, low rail
CAMERA   r5                                                   str     Camera name
CLOCK1   9.9999,0.0                                           str     [V] high rail, low rail
DETECTOR M1-52                                                str     Detector (ccd) identification
PRRSECD  [2193:4249, 4194:4194]                               str     Row prescan section for quadrant D
CCDSECB  [2058:4114, 1:2064]                                  str     CCD section for quadrant B
PRRSECA  [8:2064, 1:1]                                        str     Row prescan section for quadrant A
ORSECC   [8:2064, 2098:2129]                                  str     Row overscan section for quadrant C
PRESECB  [4250:4256, 2:2065]                                  str     Prescan section for quadrant B
PGAGAIN  3                                                    int     Controller gain
CCDSECC  [1:2057, 2065:4128]                                  str     CCD section for quadrant C
DAC7     5.9998,6.0122                                        str     [V] set value, measured value
CCDPREP  purge,clear                                          str     CCD prep actions
AMPSECD  [4114:2058, 4128:2065]                               str     AMP section for quadrant D
OFFSET1  0.4000000059604645,-8.9507                           str     [V] set value, measured value
DAC14    0.0,-0.0148                                          str     [V] set value, measured value
DAC1     -9.0002,-8.9507                                      str     [V] set value, measured value
CLOCK7   -2.0001,3.9999                                       str     [V] high rail, low rail
CLOCK10  9.9992,2.9993                                        str     [V] high rail, low rail
ORSECD   [2193:4249, 2098:2129]                               str     Row bias section for quadrant D
CLOCK16  9.9999,3.0                                           str     [V] high rail, low rail
CLOCK14  9.9992,2.9993                                        str     [V] high rail, low rail
CLOCK5   9.9999,0.0                                           str     [V] high rail, low rail
PRESECA  [1:7, 2:2065]                                        str     Prescan section for quadrant A
CDSPARMS 400, 400, 8, 2000                                    str     CDS parameters
CASETEMP 59.8142                                              float   [deg C] CCD controller case temperature
CLOCK15  9.9992,2.9993                                        str     [V] high rail, low rail
OFFSET6  2.0,6.0437                                           str     [V] set value, measured value
CLOCK8   9.9992,2.9993                                        str     [V] high rail, low rail
DATASECC [8:2064, 2130:4193]                                  str     Data section for quadrant C
DAC16    39.9961,39.8706                                      str     [V] set value, measured value
OFFSET3  0.4000000059604645,-8.9919                           str     [V] set value, measured value
BIASSECD [2129:2192, 2130:4193]                               str     Bias section for quadrant D
CLOCK11  9.9992,2.9993                                        str     [V] high rail, low rail
DAC0     -9.0002,-8.755                                       str     [V] set value, measured value
DETSECA  [1:2057, 1:2064]                                     str     Detector section for quadrant A
TRIMSECC [8:2064, 2130:4193]                                  str     Trim section for quadrant C
BIASSECB [2129:2192, 2:2065]                                  str     Bias section for quadrant B
SETTINGS detectors_sm_20210128.json                           str     Name of DESI CCD settings file
DATASECB [2193:4249, 2:2065]                                  str     Data section for quadrant B
BIASSECA [2065:2128, 2:2065]                                  str     Bias section for quadrant A
CPUTEMP  59.4551                                              float   [deg C] CCD controller CPU temperature
DAC3     -9.0002,-8.9919                                      str     [V] set value, measured value
DIGITIME 56.4629                                              float   [s] Time to digitize image
DELAYS   20, 20, 25, 40, 7, 3000, 7, 7, 400, 7                str     [10] Delay settings
DAC8     -25.0003,-24.946                                     str     [V] set value, measured value
DETSECC  [1:2057, 2065:4128]                                  str     Detector section for quadrant C
AMPSECA  [1:2057, 1:2064]                                     str     AMP section for quadrant A
CCDSECA  [1:2057, 1:2064]                                     str     CCD section for quadrant A
OFFSET4  2.0,6.0595                                           str     [V] set value, measured value
CLOCK9   9.9992,2.9993                                        str     [V] high rail, low rail
CLOCK18  9.0,0.9999                                           str     [V] high rail, low rail
CRYOTEMP 163.02                                               float   [deg K] Cryostat CCD temperature
DATASECA [8:2064, 2:2065]                                     str     Data section for quadrant A
DAC17    20.0008,12.322                                       str     [V] set value, measured value
DAC9     -25.0003,-24.6492                                    str     [V] set value, measured value
PRRSECB  [2193:4249, 1:1]                                     str     Row prescan section for quadrant B
CCDNAME  CCDSM9R                                              str     CCD name
ORSECA   [8:2064, 2066:2097]                                  str     Row overscan section for quadrant A
DETSECB  [2058:4114, 1:2064]                                  str     Detector section for quadrant B
PRESECD  [4250:4256, 2130:4193]                               str     Prescan section for quadrant D
DAC2     -9.0002,-8.9404                                      str     [V] set value, measured value
DAC5     5.9998,5.9911                                        str     [V] set value, measured value
DAC10    -25.0003,-25.0054                                    str     [V] set value, measured value
OFFSET2  0.4000000059604645,-8.9404                           str     [V] set value, measured value
CLOCK13  9.9992,2.9993                                        str     [V] high rail, low rail
CCDCFG   default_lbnl_20210128.cfg                            str     CCD configuration file
CLOCK0   9.9999,0.0                                           str     [V] high rail, low rail
DAC15    0.0,-0.0148                                          str     [V] set value, measured value
CRYOPRES 1.004e-07                                            str     [mb] Cryostat pressure (IP)
DATASECD [2193:4249, 2130:4193]                               str     Data section for quadrant D
AMPSECC  [1:2057, 4128:2065]                                  str     AMP section for quadrant C
TRIMSECB [2193:4249, 2:2065]                                  str     Trim section for quadrant B
DETSECD  [2058:4114, 2065:4128]                               str     Detector section for quadrant D
PRESECC  [1:7, 2130:4193]                                     str     Prescan section for quadrant C
OFFSET5  2.0,5.9911                                           str     [V] set value, measured value
CLOCK12  9.9992,2.9993                                        str     [V] high rail, low rail
REQTIME  1860.0                                               float   [s] Requested exposure time
OBSID    kp4m20220114t110417                                  str     Unique observation identifier
PROCTYPE RAW                                                  str     Data processing level
PRODTYPE image                                                str     Data product type
CHECKSUM 9aDRARAP3XAP9XAP                                     str     HDU checksum updated 2022-01-14T11:15:06
DATASUM  1638309244                                           str     data unit checksum updated 2022-01-14T11:15:06
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 4256x4194]

HDU19
-----

EXTNAME = B5

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   4162                                                 int     number of rows in table
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
EXPID    118526                                               int     Exposure number
EXPFRAME 0                                                    int     Frame number
FRAMES   None                                                 Unknown Number of Frames in Archive
TILEID   4403                                                 int     DESI Tile ID
FIBASSGN /data/tiles/SVN_tiles/004/fiberassign-004403.fits.gz str     Fiber assign
FLAVOR   science                                              str     Observation type
SEQUENCE _Split                                               str     OCS Sequence name
PURPOSE  Main Survey                                          str     Purpose of observing night
PROGRAM  DARK                                                 str     Program name
PROPID   2020B-5000                                           str     Proposal ID
OBSERVER Jessica Chellino, Corentin Ravoux                    str     Names of observers
LEAD     Martin Landriau                                      str     Lead observer
INSTRUME DESI                                                 str     Instrument name
OBSERVAT KPNO                                                 str     Observatory name
OBS-LAT  31.96403                                             str     [deg] Observatory latitude
OBS-LONG -111.59989                                           str     [deg] Observatory east longitude
OBS-ELEV 2097.0                                               float   [m] Observatory elevation
TELESCOP KPNO 4.0-m telescope                                 str     Telescope name
CORRCTOR DESI Corrector                                       str     Corrector Identification
NIGHT    20220113                                             int     Observing night
TIMESYS  UTC                                                  str     Time system used for date-obs
DATE-OBS 2022-01-14T11:04:17.831962880                        str     [UTC] Observation data and start tim
TIME-OBS 2022-01-14T11:04:17.831962880                        str     [UTC] Observation start time
MJD-OBS  59593.4613175                                        float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:04:18.619392                           str     Time shutter opened
ST       11:13:28.580000                                      str     Local Sidereal time at observation start (HH:MM
EXPTIME  579.101                                              float   [s] Actual exposure time
REQRA    170.239                                              float   [deg] Requested right ascension (observer input
REQDEC   -7.093                                               float   [deg] Requested declination (observer input)
FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                   str     Telescope focus settings
VCCD     ON                                                   str     True (ON) if CCD voltage is on
VCCDON   2022-01-10T20:55:39.332434                           str     Time when CCD voltage was turned on
VCCDSEC  310754.6                                             float   [s] CCD on time in seconds
TRUSTEMP 12.267                                               float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.675                                               float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                               float   Epoch of observation
MOUNTAZ  176.725567                                           float   [deg] Mount azimuth angle
MOUNTDEC -7.102329                                            float   [deg] Mount declination
MOUNTEL  50.883914                                            float   [deg] Mount elevation angle
MOUNTHA  -2.081118                                            float   [deg] Mount hour angle
SKYDEC   -7.102329                                            float   [deg] Telescope declination (pointing on sky)
SKYRA    170.24163                                            float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.102329                                            float   [deg] Target declination (to TCS)
TARGTRA  170.24163                                            float   [deg] Target right ascension (to TCS)
USEETC   T                                                    bool    ETC data available if true
USESKY   T                                                    bool    DOS Control: use Sky Monitor
USEFOCUS T                                                    bool    DOS Control: use focus
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                              str     Hexapod trim values
USEROTAT T                                                    bool    DOS Control: use rotator
ROTOFFST 138.8                                                float   [arcsec] Rotator offset
ROTENBLD T                                                    bool    Rotator enabled
ROTRATE  0.513                                                float   [arcsec/min] Rotator rate
USEGUIDR T                                                    bool    DOS Control: use guider
USEDONUT T                                                    bool    DOS Control: use donuts
SPECGRPH 5                                                    int     Spectrograph logical name (SP)
SPECID   9                                                    int     Spectrograph serial number (SM)
FEEBOX   lbnl088                                              str     CCD Controller serial number
VESSEL   32                                                   int     Cryostat serial number
FEEVER   v20160312                                            str     CCD Controller version
DETFLVER FAILED: invalid argument for get command             str     CCD Controller detector f
FEEPOWER ON                                                   str     FEE power status
FEEDMASK 2134851391                                           int     FEE dac mask
FEECMASK 1048575                                              int     FEE clk mask
CCDTEMP  850.0                                                float   [deg C] CCD controller CCD temperature
RADESYS  FK5                                                  str     Coordinate reference frame of major/minor axes
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
ORSECC   [5:2052, 2082:2113]                                  str     Row overscan section for quadrant C
PRESECC  [1:4, 2114:4161]                                     str     Prescan section for quadrant C
DAC10    26.9998,26.8752                                      str     [V] set value, measured value
AMPSECA  [1:2048, 1:2048]                                     str     AMP section for quadrant A
CLOCK0   3.9999,-4.0002                                       str     [V] high rail, low rail
CLOCK6   3.9999,-4.0002                                       str     [V] high rail, low rail
DAC17    -0.0,0.0366                                          str     [V] set value, measured value
OFFSET0  -1.5,15.8517                                         str     [V] set value, measured value
PRRSECC  [5:2052, 4162:4162]                                  str     Row prescan section for quadrant C
DAC11    26.9998,26.059                                       str     [V] set value, measured value
CLOCK8   3.0,-7.0002                                          str     [V] high rail, low rail
CLOCK12  3.0,-7.0002                                          str     [V] high rail, low rail
DETSECC  [1:2048, 2049:4096]                                  str     Detector section for quadrant C
DAC1     15.9998,15.9444                                      str     [V] set value, measured value
OFFSET4  -1.100000023841858,-0.0368                           str     [V] set value, measured value
DAC6     0.0,-0.0368                                          str     [V] set value, measured value
AMPSECC  [2048:1, 2049:4096]                                  str     AMP section for quadrant C
CCDNAME  CCDSM9B                                              str     CCD name
DAC14    0.0,0.7384                                           str     [V] set value, measured value
ORSECD   [2181:4228, 2082:2113]                               str     Row bias section for quadrant D
DAC15    19.9997,19.9784                                      str     [V] set value, measured value
CLOCK7   6.9999,-2.0001                                       str     [V] high rail, low rail
DETSECD  [2049:4096, 2049:4096]                               str     Detector section for quadrant D
BIASSECA [2053:2116, 2:2049]                                  str     Bias section for quadrant A
PRESECB  [4229:4232, 2:2049]                                  str     Prescan section for quadrant B
CCDSECA  [1:2048, 1:2048]                                     str     CCD section for quadrant A
CLOCK14  3.0,-7.0002                                          str     [V] high rail, low rail
CLOCK1   3.9999,-4.0002                                       str     [V] high rail, low rail
DAC0     15.9998,15.862                                       str     [V] set value, measured value
BIASSECC [2053:2116, 2114:4161]                               str     Bias section for quadrant C
DAC7     0.0,-0.0263                                          str     [V] set value, measured value
DATASECD [2181:4228, 2114:4161]                               str     Data section for quadrant D
DIGITIME 54.7914                                              float   [s] Time to digitize image
CCDSIZE  4162,4232                                            str     CCD size in pixels (rows, columns)
TRIMSECA [5:2052, 2:2049]                                     str     Trim section for quadrant A
DAC12    4.9997,5.0232                                        str     [V] set value, measured value
SETTINGS detectors_sm_20210623.json                           str     Name of DESI CCD settings file
CLOCK5   3.9999,-4.0002                                       str     [V] high rail, low rail
DAC3     15.9998,15.8414                                      str     [V] set value, measured value
OFFSET6  -1.100000023841858,-0.0316                           str     [V] set value, measured value
AMPSECB  [2049:4096, 2048:1]                                  str     AMP section for quadrant B
DAC16    0.0,63.2016                                          str     [V] set value, measured value
PRRSECB  [2181:4228, 1:1]                                     str     Row prescan section for quadrant B
OFFSET7  -1.100000023841858,-0.0263                           str     [V] set value, measured value
CCDTMING flatdark_sta_timing.txt                              str     CCD timing file
BLDTIME  0.3516                                               float   [s] Time to build image
DATASECB [2181:4228, 2:2049]                                  str     Data section for quadrant B
DETSECB  [2049:4096, 1:2048]                                  str     Detector section for quadrant B
DAC2     15.9998,15.9032                                      str     [V] set value, measured value
CRYOTEMP 163.02                                               float   [deg K] Cryostat CCD temperature
CLOCK13  3.0,-7.0002                                          str     [V] high rail, low rail
CCDCFG   default_sta_20210128.cfg                             str     CCD configuration file
TRIMSECD [2181:4228, 2114:4161]                               str     Trim section for quadrant D
CLOCK4   3.9999,-4.0002                                       str     [V] high rail, low rail
CDSPARMS 400, 400, 8, 1000                                    str     CDS parameters
OFFSET5  -1.100000023841858,-0.0263                           str     [V] set value, measured value
OFFSET1  -1.5,15.9547                                         str     [V] set value, measured value
CRYOPRES 1.004e-07                                            str     [mb] Cryostat pressure (IP)
DAC9     26.9998,26.5636                                      str     [V] set value, measured value
CLOCK2   3.9999,-4.0002                                       str     [V] high rail, low rail
PRESECD  [4229:4232, 2114:4161]                               str     Prescan section for quadrant D
CCDSECC  [1:2048, 2049:4096]                                  str     CCD section for quadrant C
TRIMSECB [2181:4228, 2:2049]                                  str     Trim section for quadrant B
DATASECC [5:2052, 2114:4161]                                  str     Data section for quadrant C
BIASSECD [2117:2180, 2114:4161]                               str     Bias section for quadrant D
TRIMSECC [5:2052, 2114:4161]                                  str     Trim section for quadrant C
CLOCK11  0.0,0.0                                              str     [V] high rail, low rail
CLOCK15  0.0,0.0                                              str     [V] high rail, low rail
CASETEMP 58.3376                                              float   [deg C] CCD controller case temperature
CLOCK17  3.9999,-4.0002                                       str     [V] high rail, low rail
CCDSECD  [2049:4096, 2049:4096]                               str     CCD section for quadrant D
CPUTEMP  58.5937                                              float   [deg C] CCD controller CPU temperature
CCDPREP  purge,clear                                          str     CCD prep actions
PRRSECA  [5:2052, 1:1]                                        str     Row prescan section for quadrant A
CAMERA   b5                                                   str     Camera name
CLOCK10  3.0,-7.0002                                          str     [V] high rail, low rail
ORSECB   [2181:4228, 2050:2081]                               str     Row overscan section for quadrant B
DELAYS   13, 13, 25, 25, 8, 3000, 7, 7, 400, 7                str     [10] Delay settings
DETECTOR sn22817                                              str     Detector (ccd) identification
PGAGAIN  5                                                    int     Controller gain
CCDSECB  [2049:4096, 1:2048]                                  str     CCD section for quadrant B
CLOCK16  0.0,0.0                                              str     [V] high rail, low rail
CLOCK9   3.0,-7.0002                                          str     [V] high rail, low rail
DAC13    -5.0006,-5.0856                                      str     [V] set value, measured value
ORSECA   [5:2052, 2050:2081]                                  str     Row overscan section for quadrant A
BIASSECB [2117:2180, 2:2049]                                  str     Bias section for quadrant B
DAC5     0.0,-0.0263                                          str     [V] set value, measured value
OFFSET3  -1.5,15.8311                                         str     [V] set value, measured value
DAC8     26.9998,26.9346                                      str     [V] set value, measured value
CLOCK3   6.9999,-2.0001                                       str     [V] high rail, low rail
PRESECA  [1:4, 2:2049]                                        str     Prescan section for quadrant A
PRRSECD  [2181:4228, 4162:4162]                               str     Row prescan section for quadrant D
AMPSECD  [4096:2049, 4096:2049]                               str     AMP section for quadrant D
DAC4     0.0,-0.0368                                          str     [V] set value, measured value
CLOCK18  3.9999,-4.0002                                       str     [V] high rail, low rail
OFFSET2  -1.5,15.9135                                         str     [V] set value, measured value
DATASECA [5:2052, 2:2049]                                     str     Data section for quadrant A
DETSECA  [1:2048, 1:2048]                                     str     Detector section for quadrant A
REQTIME  1860.0                                               float   [s] Requested exposure time
OBSID    kp4m20220114t110417                                  str     Unique observation identifier
PROCTYPE RAW                                                  str     Data processing level
PRODTYPE image                                                str     Data product type
CHECKSUM aYnAbWk8aWkAaWk5                                     str     HDU checksum updated 2022-01-14T11:15:06
DATASUM  868972578                                            str     data unit checksum updated 2022-01-14T11:15:06
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 4232x4162]

HDU20
-----

EXTNAME = Z7

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   4194                                                 int     number of rows in table
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
EXPID    118526                                               int     Exposure number
EXPFRAME 0                                                    int     Frame number
FRAMES   None                                                 Unknown Number of Frames in Archive
TILEID   4403                                                 int     DESI Tile ID
FIBASSGN /data/tiles/SVN_tiles/004/fiberassign-004403.fits.gz str     Fiber assign
FLAVOR   science                                              str     Observation type
SEQUENCE _Split                                               str     OCS Sequence name
PURPOSE  Main Survey                                          str     Purpose of observing night
PROGRAM  DARK                                                 str     Program name
PROPID   2020B-5000                                           str     Proposal ID
OBSERVER Jessica Chellino, Corentin Ravoux                    str     Names of observers
LEAD     Martin Landriau                                      str     Lead observer
INSTRUME DESI                                                 str     Instrument name
OBSERVAT KPNO                                                 str     Observatory name
OBS-LAT  31.96403                                             str     [deg] Observatory latitude
OBS-LONG -111.59989                                           str     [deg] Observatory east longitude
OBS-ELEV 2097.0                                               float   [m] Observatory elevation
TELESCOP KPNO 4.0-m telescope                                 str     Telescope name
CORRCTOR DESI Corrector                                       str     Corrector Identification
NIGHT    20220113                                             int     Observing night
TIMESYS  UTC                                                  str     Time system used for date-obs
DATE-OBS 2022-01-14T11:04:17.827120128                        str     [UTC] Observation data and start tim
TIME-OBS 2022-01-14T11:04:17.827120128                        str     [UTC] Observation start time
MJD-OBS  59593.46131744                                       float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:04:18.593524                           str     Time shutter opened
ST       11:13:28.580000                                      str     Local Sidereal time at observation start (HH:MM
EXPTIME  579.202                                              float   [s] Actual exposure time
REQRA    170.239                                              float   [deg] Requested right ascension (observer input
REQDEC   -7.093                                               float   [deg] Requested declination (observer input)
FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                   str     Telescope focus settings
VCCD     ON                                                   str     True (ON) if CCD voltage is on
VCCDON   2022-01-13T17:59:51.044913                           str     Time when CCD voltage was turned on
VCCDSEC  62104.5                                              float   [s] CCD on time in seconds
TRUSTEMP 12.267                                               float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.675                                               float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                               float   Epoch of observation
MOUNTAZ  176.725567                                           float   [deg] Mount azimuth angle
MOUNTDEC -7.102329                                            float   [deg] Mount declination
MOUNTEL  50.883914                                            float   [deg] Mount elevation angle
MOUNTHA  -2.081118                                            float   [deg] Mount hour angle
SKYDEC   -7.102329                                            float   [deg] Telescope declination (pointing on sky)
SKYRA    170.24163                                            float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.102329                                            float   [deg] Target declination (to TCS)
TARGTRA  170.24163                                            float   [deg] Target right ascension (to TCS)
USEETC   T                                                    bool    ETC data available if true
USESKY   T                                                    bool    DOS Control: use Sky Monitor
USEFOCUS T                                                    bool    DOS Control: use focus
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                              str     Hexapod trim values
USEROTAT T                                                    bool    DOS Control: use rotator
ROTOFFST 138.8                                                float   [arcsec] Rotator offset
ROTENBLD T                                                    bool    Rotator enabled
ROTRATE  0.513                                                float   [arcsec/min] Rotator rate
USEGUIDR T                                                    bool    DOS Control: use guider
USEDONUT T                                                    bool    DOS Control: use donuts
SPECGRPH 7                                                    int     Spectrograph logical name (SP)
SPECID   8                                                    int     Spectrograph serial number (SM)
FEEBOX   lbnl085                                              str     CCD Controller serial number
VESSEL   20                                                   int     Cryostat serial number
FEEVER   v20160312                                            str     CCD Controller version
DETFLVER FAILED: invalid argument for get command             str     CCD Controller detector f
FEEPOWER ON                                                   str     FEE power status
FEEDMASK 2134851391                                           int     FEE dac mask
FEECMASK 1048575                                              int     FEE clk mask
CCDTEMP  -133.8515                                            float   [deg C] CCD controller CCD temperature
RADESYS  FK5                                                  str     Coordinate reference frame of major/minor axes
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
OFFSET2  0.4000000059604645,-8.9301                           str     [V] set value, measured value
PRRSECD  [2193:4249, 4194:4194]                               str     Row prescan section for quadrant D
DAC17    20.0008,12.0048                                      str     [V] set value, measured value
ORSECA   [8:2064, 2066:2097]                                  str     Row overscan section for quadrant A
DAC13    0.0,0.0148                                           str     [V] set value, measured value
CASETEMP 57.5994                                              float   [deg C] CCD controller case temperature
DAC0     -9.0002,-9.0228                                      str     [V] set value, measured value
CLOCK13  9.9992,2.9993                                        str     [V] high rail, low rail
ORSECD   [2193:4249, 2098:2129]                               str     Row bias section for quadrant D
CLOCK1   9.9999,0.0                                           str     [V] high rail, low rail
BIASSECC [2065:2128, 2130:4193]                               str     Bias section for quadrant C
DAC15    0.0,0.0148                                           str     [V] set value, measured value
CLOCK6   9.9999,0.0                                           str     [V] high rail, low rail
CCDSECB  [2058:4114, 1:2064]                                  str     CCD section for quadrant B
DETSECA  [1:2057, 1:2064]                                     str     Detector section for quadrant A
DETSECC  [1:2057, 2065:4128]                                  str     Detector section for quadrant C
DAC6     5.9998,6.0385                                        str     [V] set value, measured value
DAC4     5.9998,6.0437                                        str     [V] set value, measured value
CCDTMING flatdark_lbnl_timing.txt                             str     CCD timing file
DIGITIME 56.4599                                              float   [s] Time to digitize image
CCDSECC  [1:2057, 2065:4128]                                  str     CCD section for quadrant C
DETSECB  [2058:4114, 1:2064]                                  str     Detector section for quadrant B
CLOCK7   -2.0001,3.9999                                       str     [V] high rail, low rail
DATASECC [8:2064, 2130:4193]                                  str     Data section for quadrant C
SETTINGS detectors_sm_20210128.json                           str     Name of DESI CCD settings file
CLOCK16  9.9999,3.0                                           str     [V] high rail, low rail
DAC11    -25.0003,-24.9164                                    str     [V] set value, measured value
AMPSECC  [1:2057, 4128:2065]                                  str     AMP section for quadrant C
CLOCK5   9.9999,0.0                                           str     [V] high rail, low rail
CLOCK14  9.9992,2.9993                                        str     [V] high rail, low rail
DATASECD [2193:4249, 2130:4193]                               str     Data section for quadrant D
CCDNAME  CCDSM8Z                                              str     CCD name
CLOCK2   9.9999,0.0                                           str     [V] high rail, low rail
DAC1     -9.0002,-8.9816                                      str     [V] set value, measured value
OFFSET7  2.0,6.0385                                           str     [V] set value, measured value
OFFSET3  0.4000000059604645,-9.0434                           str     [V] set value, measured value
CCDSIZE  4194,4256                                            str     CCD size in pixels (rows, columns)
AMPSECD  [4114:2058, 4128:2065]                               str     AMP section for quadrant D
CRYOTEMP 139.962                                              float   [deg K] Cryostat CCD temperature
OFFSET6  2.0,6.0332                                           str     [V] set value, measured value
DAC12    0.0,0.0148                                           str     [V] set value, measured value
PRESECC  [1:7, 2130:4193]                                     str     Prescan section for quadrant C
PRRSECA  [8:2064, 1:1]                                        str     Row prescan section for quadrant A
BIASSECB [2129:2192, 2:2065]                                  str     Bias section for quadrant B
PRESECA  [1:7, 2:2065]                                        str     Prescan section for quadrant A
PRRSECB  [2193:4249, 1:1]                                     str     Row prescan section for quadrant B
CCDSECD  [2058:4114, 2065:4128]                               str     CCD section for quadrant D
CLOCK9   9.9992,2.9993                                        str     [V] high rail, low rail
OFFSET1  0.4000000059604645,-8.9816                           str     [V] set value, measured value
DATASECB [2193:4249, 2:2065]                                  str     Data section for quadrant B
AMPSECB  [4114:2058, 1:2064]                                  str     AMP section for quadrant B
CLOCK15  9.9992,2.9993                                        str     [V] high rail, low rail
TRIMSECD [2193:4249, 2130:4193]                               str     Trim section for quadrant D
DAC3     -9.0002,-9.0434                                      str     [V] set value, measured value
AMPSECA  [1:2057, 1:2064]                                     str     AMP section for quadrant A
DAC14    0.0,0.0148                                           str     [V] set value, measured value
PGAGAIN  3                                                    int     Controller gain
CLOCK10  9.9992,2.9993                                        str     [V] high rail, low rail
DAC7     5.9998,6.0385                                        str     [V] set value, measured value
CAMERA   z7                                                   str     Camera name
OFFSET0  0.4000000059604645,-9.0228                           str     [V] set value, measured value
BLDTIME  0.3515                                               float   [s] Time to build image
CLOCK17  9.0,0.9999                                           str     [V] high rail, low rail
DELAYS   20, 20, 25, 40, 7, 3000, 7, 7, 400, 7                str     [10] Delay settings
TRIMSECA [8:2064, 2:2065]                                     str     Trim section for quadrant A
DETECTOR M1-40                                                str     Detector (ccd) identification
DAC10    -25.0003,-25.0796                                    str     [V] set value, measured value
CRYOPRES 6.073e-08                                            str     [mb] Cryostat pressure (IP)
CCDSECA  [1:2057, 1:2064]                                     str     CCD section for quadrant A
OFFSET4  2.0,6.0385                                           str     [V] set value, measured value
BIASSECA [2065:2128, 2:2065]                                  str     Bias section for quadrant A
CLOCK11  9.9992,2.9993                                        str     [V] high rail, low rail
OFFSET5  2.0,6.0543                                           str     [V] set value, measured value
ORSECC   [8:2064, 2098:2129]                                  str     Row overscan section for quadrant C
DAC2     -9.0002,-8.9198                                      str     [V] set value, measured value
DAC5     5.9998,6.0543                                        str     [V] set value, measured value
CDSPARMS 400, 400, 8, 2000                                    str     CDS parameters
CLOCK18  9.0,0.9999                                           str     [V] high rail, low rail
TRIMSECC [8:2064, 2130:4193]                                  str     Trim section for quadrant C
DETSECD  [2058:4114, 2065:4128]                               str     Detector section for quadrant D
CLOCK0   9.9999,0.0                                           str     [V] high rail, low rail
DAC9     -25.0003,-24.6344                                    str     [V] set value, measured value
PRESECB  [4250:4256, 2:2065]                                  str     Prescan section for quadrant B
CCDPREP  purge,clear                                          str     CCD prep actions
CLOCK8   9.9992,2.9993                                        str     [V] high rail, low rail
ORSECB   [2193:4249, 2066:2097]                               str     Row overscan section for quadrant B
TRIMSECB [2193:4249, 2:2065]                                  str     Trim section for quadrant B
BIASSECD [2129:2192, 2130:4193]                               str     Bias section for quadrant D
CLOCK4   9.9999,0.0                                           str     [V] high rail, low rail
PRESECD  [4250:4256, 2130:4193]                               str     Prescan section for quadrant D
CCDCFG   default_lbnl_20210128.cfg                            str     CCD configuration file
CLOCK3   -2.0001,3.9999                                       str     [V] high rail, low rail
DAC16    39.9961,39.6396                                      str     [V] set value, measured value
PRRSECC  [8:2064, 4194:4194]                                  str     Row prescan section for quadrant C
DATASECA [8:2064, 2:2065]                                     str     Data section for quadrant A
CPUTEMP  58.5937                                              float   [deg C] CCD controller CPU temperature
DAC8     -25.0003,-24.7531                                    str     [V] set value, measured value
CLOCK12  9.9992,2.9993                                        str     [V] high rail, low rail
REQTIME  1860.0                                               float   [s] Requested exposure time
OBSID    kp4m20220114t110417                                  str     Unique observation identifier
PROCTYPE RAW                                                  str     Data processing level
PRODTYPE image                                                str     Data product type
CHECKSUM 83IZ93FX83FX83FX                                     str     HDU checksum updated 2022-01-14T11:15:07
DATASUM  2865487509                                           str     data unit checksum updated 2022-01-14T11:15:07
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 4256x4194]

HDU21
-----

EXTNAME = R7

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   4194                                                 int     number of rows in table
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
EXPID    118526                                               int     Exposure number
EXPFRAME 0                                                    int     Frame number
FRAMES   None                                                 Unknown Number of Frames in Archive
TILEID   4403                                                 int     DESI Tile ID
FIBASSGN /data/tiles/SVN_tiles/004/fiberassign-004403.fits.gz str     Fiber assign
FLAVOR   science                                              str     Observation type
SEQUENCE _Split                                               str     OCS Sequence name
PURPOSE  Main Survey                                          str     Purpose of observing night
PROGRAM  DARK                                                 str     Program name
PROPID   2020B-5000                                           str     Proposal ID
OBSERVER Jessica Chellino, Corentin Ravoux                    str     Names of observers
LEAD     Martin Landriau                                      str     Lead observer
INSTRUME DESI                                                 str     Instrument name
OBSERVAT KPNO                                                 str     Observatory name
OBS-LAT  31.96403                                             str     [deg] Observatory latitude
OBS-LONG -111.59989                                           str     [deg] Observatory east longitude
OBS-ELEV 2097.0                                               float   [m] Observatory elevation
TELESCOP KPNO 4.0-m telescope                                 str     Telescope name
CORRCTOR DESI Corrector                                       str     Corrector Identification
NIGHT    20220113                                             int     Observing night
TIMESYS  UTC                                                  str     Time system used for date-obs
DATE-OBS 2022-01-14T11:04:17.827120128                        str     [UTC] Observation data and start tim
TIME-OBS 2022-01-14T11:04:17.827120128                        str     [UTC] Observation start time
MJD-OBS  59593.46131744                                       float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:04:18.593524                           str     Time shutter opened
ST       11:13:28.580000                                      str     Local Sidereal time at observation start (HH:MM
EXPTIME  579.202                                              float   [s] Actual exposure time
REQRA    170.239                                              float   [deg] Requested right ascension (observer input
REQDEC   -7.093                                               float   [deg] Requested declination (observer input)
FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                   str     Telescope focus settings
VCCD     ON                                                   str     True (ON) if CCD voltage is on
VCCDON   2022-01-13T17:59:44.268250                           str     Time when CCD voltage was turned on
VCCDSEC  62111.3                                              float   [s] CCD on time in seconds
TRUSTEMP 12.267                                               float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.675                                               float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                               float   Epoch of observation
MOUNTAZ  176.725567                                           float   [deg] Mount azimuth angle
MOUNTDEC -7.102329                                            float   [deg] Mount declination
MOUNTEL  50.883914                                            float   [deg] Mount elevation angle
MOUNTHA  -2.081118                                            float   [deg] Mount hour angle
SKYDEC   -7.102329                                            float   [deg] Telescope declination (pointing on sky)
SKYRA    170.24163                                            float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.102329                                            float   [deg] Target declination (to TCS)
TARGTRA  170.24163                                            float   [deg] Target right ascension (to TCS)
USEETC   T                                                    bool    ETC data available if true
USESKY   T                                                    bool    DOS Control: use Sky Monitor
USEFOCUS T                                                    bool    DOS Control: use focus
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                              str     Hexapod trim values
USEROTAT T                                                    bool    DOS Control: use rotator
ROTOFFST 138.8                                                float   [arcsec] Rotator offset
ROTENBLD T                                                    bool    Rotator enabled
ROTRATE  0.513                                                float   [arcsec/min] Rotator rate
USEGUIDR T                                                    bool    DOS Control: use guider
USEDONUT T                                                    bool    DOS Control: use donuts
SPECGRPH 7                                                    int     Spectrograph logical name (SP)
SPECID   8                                                    int     Spectrograph serial number (SM)
FEEBOX   lbnl070                                              str     CCD Controller serial number
VESSEL   19                                                   int     Cryostat serial number
FEEVER   v20160312                                            str     CCD Controller version
DETFLVER FAILED: invalid argument for get command             str     CCD Controller detector f
FEEPOWER ON                                                   str     FEE power status
FEEDMASK 2134851391                                           int     FEE dac mask
FEECMASK 1048575                                              int     FEE clk mask
CCDTEMP  -133.9861                                            float   [deg C] CCD controller CCD temperature
RADESYS  FK5                                                  str     Coordinate reference frame of major/minor axes
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
DATASECB [2193:4249, 2:2065]                                  str     Data section for quadrant B
PRRSECB  [2193:4249, 1:1]                                     str     Row prescan section for quadrant B
CLOCK8   9.9992,2.9993                                        str     [V] high rail, low rail
CLOCK14  9.9992,2.9993                                        str     [V] high rail, low rail
DAC10    -25.0003,-25.0499                                    str     [V] set value, measured value
OFFSET3  0.4000000059604645,-8.961                            str     [V] set value, measured value
CLOCK11  9.9992,2.9993                                        str     [V] high rail, low rail
DAC8     -25.0003,-24.8422                                    str     [V] set value, measured value
DAC12    0.0,-0.0148                                          str     [V] set value, measured value
CCDPREP  purge,clear                                          str     CCD prep actions
CLOCK3   -2.0001,3.9999                                       str     [V] high rail, low rail
DAC9     -25.0003,-24.9164                                    str     [V] set value, measured value
TRIMSECC [8:2064, 2130:4193]                                  str     Trim section for quadrant C
CLOCK13  9.9992,2.9993                                        str     [V] high rail, low rail
DAC2     -9.0002,-8.9919                                      str     [V] set value, measured value
CRYOPRES 1.066e-07                                            str     [mb] Cryostat pressure (IP)
PRRSECA  [8:2064, 1:1]                                        str     Row prescan section for quadrant A
CLOCK9   9.9992,2.9993                                        str     [V] high rail, low rail
DETSECC  [1:2057, 2065:4128]                                  str     Detector section for quadrant C
OFFSET6  2.0,6.0437                                           str     [V] set value, measured value
CCDSECB  [2058:4114, 1:2064]                                  str     CCD section for quadrant B
OFFSET2  0.4000000059604645,-8.9919                           str     [V] set value, measured value
CLOCK2   9.9999,0.0                                           str     [V] high rail, low rail
CCDNAME  CCDSM8R                                              str     CCD name
ORSECC   [8:2064, 2098:2129]                                  str     Row overscan section for quadrant C
CLOCK4   9.9999,0.0                                           str     [V] high rail, low rail
AMPSECD  [4114:2058, 4128:2065]                               str     AMP section for quadrant D
DETECTOR M1-02-1                                              str     Detector (ccd) identification
SETTINGS detectors_sm_20210128.json                           str     Name of DESI CCD settings file
OFFSET4  2.0,6.0385                                           str     [V] set value, measured value
DETSECD  [2058:4114, 2065:4128]                               str     Detector section for quadrant D
TRIMSECD [2193:4249, 2130:4193]                               str     Trim section for quadrant D
CCDSECD  [2058:4114, 2065:4128]                               str     CCD section for quadrant D
CLOCK10  9.9992,2.9993                                        str     [V] high rail, low rail
CCDSECC  [1:2057, 2065:4128]                                  str     CCD section for quadrant C
DAC13    0.0,-0.0297                                          str     [V] set value, measured value
CLOCK12  9.9992,2.9993                                        str     [V] high rail, low rail
OFFSET5  2.0,6.0174                                           str     [V] set value, measured value
ORSECA   [8:2064, 2066:2097]                                  str     Row overscan section for quadrant A
CCDSECA  [1:2057, 1:2064]                                     str     CCD section for quadrant A
CCDSIZE  4194,4256                                            str     CCD size in pixels (rows, columns)
CASETEMP 55.2615                                              float   [deg C] CCD controller case temperature
BIASSECC [2065:2128, 2130:4193]                               str     Bias section for quadrant C
CLOCK16  9.9999,3.0                                           str     [V] high rail, low rail
CCDTMING flatdark_lbnl_timing.txt                             str     CCD timing file
CRYOTEMP 162.97                                               float   [deg K] Cryostat CCD temperature
DAC14    0.0,-0.0148                                          str     [V] set value, measured value
PRESECD  [4250:4256, 2130:4193]                               str     Prescan section for quadrant D
TRIMSECA [8:2064, 2:2065]                                     str     Trim section for quadrant A
CLOCK0   9.9999,0.0                                           str     [V] high rail, low rail
AMPSECC  [1:2057, 4128:2065]                                  str     AMP section for quadrant C
AMPSECB  [4114:2058, 1:2064]                                  str     AMP section for quadrant B
DETSECA  [1:2057, 1:2064]                                     str     Detector section for quadrant A
CDSPARMS 400, 400, 8, 2000                                    str     CDS parameters
PRRSECD  [2193:4249, 4194:4194]                               str     Row prescan section for quadrant D
DIGITIME 56.4523                                              float   [s] Time to digitize image
AMPSECA  [1:2057, 1:2064]                                     str     AMP section for quadrant A
CPUTEMP  55.5176                                              float   [deg C] CCD controller CPU temperature
OFFSET0  0.4000000059604645,-8.961                            str     [V] set value, measured value
PRESECB  [4250:4256, 2:2065]                                  str     Prescan section for quadrant B
CLOCK6   9.9999,0.0                                           str     [V] high rail, low rail
DAC16    39.9961,39.1314                                      str     [V] set value, measured value
OFFSET1  0.4000000059604645,-8.8889                           str     [V] set value, measured value
CAMERA   r7                                                   str     Camera name
DAC3     -9.0002,-8.961                                       str     [V] set value, measured value
CLOCK7   -2.0001,3.9999                                       str     [V] high rail, low rail
BIASSECA [2065:2128, 2:2065]                                  str     Bias section for quadrant A
PRRSECC  [8:2064, 4194:4194]                                  str     Row prescan section for quadrant C
PRESECC  [1:7, 2130:4193]                                     str     Prescan section for quadrant C
CLOCK1   9.9999,0.0                                           str     [V] high rail, low rail
DELAYS   20, 20, 25, 40, 7, 3000, 7, 7, 400, 7                str     [10] Delay settings
DAC11    -25.0003,-24.6641                                    str     [V] set value, measured value
DAC17    20.0008,12.2854                                      str     [V] set value, measured value
TRIMSECB [2193:4249, 2:2065]                                  str     Trim section for quadrant B
CLOCK5   9.9999,0.0                                           str     [V] high rail, low rail
ORSECD   [2193:4249, 2098:2129]                               str     Row bias section for quadrant D
OFFSET7  2.0,6.028                                            str     [V] set value, measured value
CLOCK18  9.0,0.9999                                           str     [V] high rail, low rail
CCDCFG   default_lbnl_20210128.cfg                            str     CCD configuration file
BLDTIME  0.3515                                               float   [s] Time to build image
BIASSECB [2129:2192, 2:2065]                                  str     Bias section for quadrant B
DATASECC [8:2064, 2130:4193]                                  str     Data section for quadrant C
ORSECB   [2193:4249, 2066:2097]                               str     Row overscan section for quadrant B
BIASSECD [2129:2192, 2130:4193]                               str     Bias section for quadrant D
DATASECA [8:2064, 2:2065]                                     str     Data section for quadrant A
DAC7     5.9998,6.0227                                        str     [V] set value, measured value
DAC1     -9.0002,-8.8889                                      str     [V] set value, measured value
DAC6     5.9998,6.0437                                        str     [V] set value, measured value
DAC5     5.9998,6.0122                                        str     [V] set value, measured value
PRESECA  [1:7, 2:2065]                                        str     Prescan section for quadrant A
DAC15    0.0,-0.0148                                          str     [V] set value, measured value
CLOCK17  9.0,0.9999                                           str     [V] high rail, low rail
DETSECB  [2058:4114, 1:2064]                                  str     Detector section for quadrant B
DATASECD [2193:4249, 2130:4193]                               str     Data section for quadrant D
CLOCK15  9.9992,2.9993                                        str     [V] high rail, low rail
DAC4     5.9998,6.0332                                        str     [V] set value, measured value
DAC0     -9.0002,-8.961                                       str     [V] set value, measured value
PGAGAIN  3                                                    int     Controller gain
REQTIME  1860.0                                               float   [s] Requested exposure time
OBSID    kp4m20220114t110417                                  str     Unique observation identifier
PROCTYPE RAW                                                  str     Data processing level
PRODTYPE image                                                str     Data product type
CHECKSUM 8Egc99Za8Eda89Za                                     str     HDU checksum updated 2022-01-14T11:15:07
DATASUM  2465349317                                           str     data unit checksum updated 2022-01-14T11:15:07
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 4256x4194]

HDU22
-----

EXTNAME = B7

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   4162                                                 int     number of rows in table
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
EXPID    118526                                               int     Exposure number
EXPFRAME 0                                                    int     Frame number
FRAMES   None                                                 Unknown Number of Frames in Archive
TILEID   4403                                                 int     DESI Tile ID
FIBASSGN /data/tiles/SVN_tiles/004/fiberassign-004403.fits.gz str     Fiber assign
FLAVOR   science                                              str     Observation type
SEQUENCE _Split                                               str     OCS Sequence name
PURPOSE  Main Survey                                          str     Purpose of observing night
PROGRAM  DARK                                                 str     Program name
PROPID   2020B-5000                                           str     Proposal ID
OBSERVER Jessica Chellino, Corentin Ravoux                    str     Names of observers
LEAD     Martin Landriau                                      str     Lead observer
INSTRUME DESI                                                 str     Instrument name
OBSERVAT KPNO                                                 str     Observatory name
OBS-LAT  31.96403                                             str     [deg] Observatory latitude
OBS-LONG -111.59989                                           str     [deg] Observatory east longitude
OBS-ELEV 2097.0                                               float   [m] Observatory elevation
TELESCOP KPNO 4.0-m telescope                                 str     Telescope name
CORRCTOR DESI Corrector                                       str     Corrector Identification
NIGHT    20220113                                             int     Observing night
TIMESYS  UTC                                                  str     Time system used for date-obs
DATE-OBS 2022-01-14T11:04:17.827120128                        str     [UTC] Observation data and start tim
TIME-OBS 2022-01-14T11:04:17.827120128                        str     [UTC] Observation start time
MJD-OBS  59593.46131744                                       float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:04:18.593524                           str     Time shutter opened
ST       11:13:28.580000                                      str     Local Sidereal time at observation start (HH:MM
EXPTIME  579.202                                              float   [s] Actual exposure time
REQRA    170.239                                              float   [deg] Requested right ascension (observer input
REQDEC   -7.093                                               float   [deg] Requested declination (observer input)
FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                   str     Telescope focus settings
VCCD     ON                                                   str     True (ON) if CCD voltage is on
VCCDON   2022-01-13T17:59:46.644381                           str     Time when CCD voltage was turned on
VCCDSEC  62107.2                                              float   [s] CCD on time in seconds
TRUSTEMP 12.267                                               float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.675                                               float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                               float   Epoch of observation
MOUNTAZ  176.725567                                           float   [deg] Mount azimuth angle
MOUNTDEC -7.102329                                            float   [deg] Mount declination
MOUNTEL  50.883914                                            float   [deg] Mount elevation angle
MOUNTHA  -2.081118                                            float   [deg] Mount hour angle
SKYDEC   -7.102329                                            float   [deg] Telescope declination (pointing on sky)
SKYRA    170.24163                                            float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.102329                                            float   [deg] Target declination (to TCS)
TARGTRA  170.24163                                            float   [deg] Target right ascension (to TCS)
USEETC   T                                                    bool    ETC data available if true
USESKY   T                                                    bool    DOS Control: use Sky Monitor
USEFOCUS T                                                    bool    DOS Control: use focus
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                              str     Hexapod trim values
USEROTAT T                                                    bool    DOS Control: use rotator
ROTOFFST 138.8                                                float   [arcsec] Rotator offset
ROTENBLD T                                                    bool    Rotator enabled
ROTRATE  0.513                                                float   [arcsec/min] Rotator rate
USEGUIDR T                                                    bool    DOS Control: use guider
USEDONUT T                                                    bool    DOS Control: use donuts
SPECGRPH 7                                                    int     Spectrograph logical name (SP)
SPECID   8                                                    int     Spectrograph serial number (SM)
FEEBOX   lbnl067                                              str     CCD Controller serial number
VESSEL   25                                                   int     Cryostat serial number
FEEVER   v20160312                                            str     CCD Controller version
DETFLVER FAILED: invalid argument for get command             str     CCD Controller detector f
FEEPOWER ON                                                   str     FEE power status
FEEDMASK 2134851391                                           int     FEE dac mask
FEECMASK 1048575                                              int     FEE clk mask
CCDTEMP  850.0                                                float   [deg C] CCD controller CCD temperature
RADESYS  FK5                                                  str     Coordinate reference frame of major/minor axes
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
CLOCK2   3.9999,-4.0002                                       str     [V] high rail, low rail
TRIMSECD [2181:4228, 2114:4161]                               str     Trim section for quadrant D
BIASSECA [2053:2116, 2:2049]                                  str     Bias section for quadrant A
PRESECB  [4229:4232, 2:2049]                                  str     Prescan section for quadrant B
OFFSET2  -1.5,15.8208                                         str     [V] set value, measured value
DAC6     0.0,-0.0316                                          str     [V] set value, measured value
DETSECB  [2049:4096, 1:2048]                                  str     Detector section for quadrant B
CLOCK7   6.9999,-2.0001                                       str     [V] high rail, low rail
CLOCK8   3.0,-7.0002                                          str     [V] high rail, low rail
DELAYS   13, 13, 25, 25, 8, 3000, 7, 7, 400, 7                str     [10] Delay settings
OFFSET7  -1.100000023841858,-0.0368                           str     [V] set value, measured value
DIGITIME 54.7863                                              float   [s] Time to digitize image
BIASSECC [2053:2116, 2114:4161]                               str     Bias section for quadrant C
TRIMSECA [5:2052, 2:2049]                                     str     Trim section for quadrant A
PRESECA  [1:4, 2:2049]                                        str     Prescan section for quadrant A
DAC5     0.0,-0.0316                                          str     [V] set value, measured value
ORSECB   [2181:4228, 2050:2081]                               str     Row overscan section for quadrant B
PRRSECC  [5:2052, 4162:4162]                                  str     Row prescan section for quadrant C
CDSPARMS 400, 400, 8, 1000                                    str     CDS parameters
ORSECC   [5:2052, 2082:2113]                                  str     Row overscan section for quadrant C
AMPSECA  [1:2048, 1:2048]                                     str     AMP section for quadrant A
DAC0     15.9998,15.8105                                      str     [V] set value, measured value
PRRSECD  [2181:4228, 4162:4162]                               str     Row prescan section for quadrant D
SETTINGS detectors_sm_20210128.json                           str     Name of DESI CCD settings file
CLOCK5   3.9999,-4.0002                                       str     [V] high rail, low rail
AMPSECD  [4096:2049, 4096:2049]                               str     AMP section for quadrant D
OFFSET4  -1.100000023841858,-0.0263                           str     [V] set value, measured value
DATASECA [5:2052, 2:2049]                                     str     Data section for quadrant A
CLOCK13  3.0,-7.0002                                          str     [V] high rail, low rail
CRYOPRES 1.066e-07                                            str     [mb] Cryostat pressure (IP)
BIASSECB [2117:2180, 2:2049]                                  str     Bias section for quadrant B
DATASECC [5:2052, 2114:4161]                                  str     Data section for quadrant C
DAC17    -0.0,0.0854                                          str     [V] set value, measured value
BIASSECD [2117:2180, 2114:4161]                               str     Bias section for quadrant D
CPUTEMP  57.9785                                              float   [deg C] CCD controller CPU temperature
DAC14    0.0,0.7072                                           str     [V] set value, measured value
CLOCK17  3.9999,-4.0002                                       str     [V] high rail, low rail
DATASECD [2181:4228, 2114:4161]                               str     Data section for quadrant D
DETSECC  [1:2048, 2049:4096]                                  str     Detector section for quadrant C
CLOCK6   3.9999,-4.0002                                       str     [V] high rail, low rail
PRESECC  [1:4, 2114:4161]                                     str     Prescan section for quadrant C
TRIMSECB [2181:4228, 2:2049]                                  str     Trim section for quadrant B
CLOCK18  3.9999,-4.0002                                       str     [V] high rail, low rail
CLOCK15  0.0,0.0                                              str     [V] high rail, low rail
DAC7     0.0,-0.0316                                          str     [V] set value, measured value
OFFSET3  -1.5,15.8723                                         str     [V] set value, measured value
AMPSECB  [2049:4096, 2048:1]                                  str     AMP section for quadrant B
CLOCK4   3.9999,-4.0002                                       str     [V] high rail, low rail
DAC4     0.0,-0.0316                                          str     [V] set value, measured value
CCDSIZE  4162,4232                                            str     CCD size in pixels (rows, columns)
OFFSET6  -1.100000023841858,-0.0316                           str     [V] set value, measured value
CRYOTEMP 162.97                                               float   [deg K] Cryostat CCD temperature
CLOCK3   6.9999,-2.0001                                       str     [V] high rail, low rail
DAC1     15.9998,15.8002                                      str     [V] set value, measured value
DETSECD  [2049:4096, 2049:4096]                               str     Detector section for quadrant D
DAC2     15.9998,15.8414                                      str     [V] set value, measured value
DAC11    26.9998,26.7417                                      str     [V] set value, measured value
OFFSET1  -1.5,15.7899                                         str     [V] set value, measured value
CCDTMING flatdark_sta_timing.txt                              str     CCD timing file
OFFSET5  -1.100000023841858,-0.0316                           str     [V] set value, measured value
TRIMSECC [5:2052, 2114:4161]                                  str     Trim section for quadrant C
CLOCK16  0.0,0.0                                              str     [V] high rail, low rail
CAMERA   b7                                                   str     Camera name
PRESECD  [4229:4232, 2114:4161]                               str     Prescan section for quadrant D
ORSECA   [5:2052, 2050:2081]                                  str     Row overscan section for quadrant A
DETSECA  [1:2048, 1:2048]                                     str     Detector section for quadrant A
CCDPREP  purge,clear                                          str     CCD prep actions
CLOCK1   3.9999,-4.0002                                       str     [V] high rail, low rail
DAC9     26.9998,26.3707                                      str     [V] set value, measured value
CLOCK0   3.9999,-4.0002                                       str     [V] high rail, low rail
DAC16    0.0,64.8648                                          str     [V] set value, measured value
DAC3     15.9998,15.8723                                      str     [V] set value, measured value
ORSECD   [2181:4228, 2082:2113]                               str     Row bias section for quadrant D
PRRSECA  [5:2052, 1:1]                                        str     Row prescan section for quadrant A
DETECTOR sn22829                                              str     Detector (ccd) identification
PGAGAIN  5                                                    int     Controller gain
CLOCK14  3.0,-7.0002                                          str     [V] high rail, low rail
CASETEMP 58.0915                                              float   [deg C] CCD controller case temperature
CCDCFG   default_sta_20210128.cfg                             str     CCD configuration file
PRRSECB  [2181:4228, 1:1]                                     str     Row prescan section for quadrant B
DAC10    26.9998,26.1332                                      str     [V] set value, measured value
CLOCK10  3.0,-7.0002                                          str     [V] high rail, low rail
CCDNAME  CCDSM8B                                              str     CCD name
CLOCK12  3.0,-7.0002                                          str     [V] high rail, low rail
CCDSECA  [1:2048, 1:2048]                                     str     CCD section for quadrant A
DAC8     26.9998,26.5784                                      str     [V] set value, measured value
DAC15    19.9997,19.8848                                      str     [V] set value, measured value
CCDSECC  [1:2048, 2049:4096]                                  str     CCD section for quadrant C
DAC12    4.9997,5.044                                         str     [V] set value, measured value
OFFSET0  -1.5,15.8002                                         str     [V] set value, measured value
CLOCK9   3.0,-7.0002                                          str     [V] high rail, low rail
CCDSECD  [2049:4096, 2049:4096]                               str     CCD section for quadrant D
DATASECB [2181:4228, 2:2049]                                  str     Data section for quadrant B
AMPSECC  [2048:1, 2049:4096]                                  str     AMP section for quadrant C
CCDSECB  [2049:4096, 1:2048]                                  str     CCD section for quadrant B
BLDTIME  0.3517                                               float   [s] Time to build image
DAC13    -5.0006,-5.0336                                      str     [V] set value, measured value
CLOCK11  0.0,0.0                                              str     [V] high rail, low rail
REQTIME  1860.0                                               float   [s] Requested exposure time
OBSID    kp4m20220114t110417                                  str     Unique observation identifier
PROCTYPE RAW                                                  str     Data processing level
PRODTYPE image                                                str     Data product type
CHECKSUM cHDJeGCGcGCGcGCG                                     str     HDU checksum updated 2022-01-14T11:15:07
DATASUM  1700097806                                           str     data unit checksum updated 2022-01-14T11:15:07
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 4232x4162]

HDU23
-----

EXTNAME = Z6

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   4194                                                 int     number of rows in table
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
EXPID    118526                                               int     Exposure number
EXPFRAME 0                                                    int     Frame number
FRAMES   None                                                 Unknown Number of Frames in Archive
TILEID   4403                                                 int     DESI Tile ID
FIBASSGN /data/tiles/SVN_tiles/004/fiberassign-004403.fits.gz str     Fiber assign
FLAVOR   science                                              str     Observation type
SEQUENCE _Split                                               str     OCS Sequence name
PURPOSE  Main Survey                                          str     Purpose of observing night
PROGRAM  DARK                                                 str     Program name
PROPID   2020B-5000                                           str     Proposal ID
OBSERVER Jessica Chellino, Corentin Ravoux                    str     Names of observers
LEAD     Martin Landriau                                      str     Lead observer
INSTRUME DESI                                                 str     Instrument name
OBSERVAT KPNO                                                 str     Observatory name
OBS-LAT  31.96403                                             str     [deg] Observatory latitude
OBS-LONG -111.59989                                           str     [deg] Observatory east longitude
OBS-ELEV 2097.0                                               float   [m] Observatory elevation
TELESCOP KPNO 4.0-m telescope                                 str     Telescope name
CORRCTOR DESI Corrector                                       str     Corrector Identification
NIGHT    20220113                                             int     Observing night
TIMESYS  UTC                                                  str     Time system used for date-obs
DATE-OBS 2022-01-14T11:04:17.764723968                        str     [UTC] Observation data and start tim
TIME-OBS 2022-01-14T11:04:17.764723968                        str     [UTC] Observation start time
MJD-OBS  59593.46131672                                       float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:04:18.551089                           str     Time shutter opened
ST       11:13:28.520000                                      str     Local Sidereal time at observation start (HH:MM
EXPTIME  579.174                                              float   [s] Actual exposure time
REQRA    170.239                                              float   [deg] Requested right ascension (observer input
REQDEC   -7.093                                               float   [deg] Requested declination (observer input)
FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                   str     Telescope focus settings
VCCD     ON                                                   str     True (ON) if CCD voltage is on
VCCDON   2022-01-10T20:55:43.755442                           str     Time when CCD voltage was turned on
VCCDSEC  310751.8                                             float   [s] CCD on time in seconds
TRUSTEMP 12.267                                               float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.675                                               float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                               float   Epoch of observation
MOUNTAZ  176.725567                                           float   [deg] Mount azimuth angle
MOUNTDEC -7.102329                                            float   [deg] Mount declination
MOUNTEL  50.883914                                            float   [deg] Mount elevation angle
MOUNTHA  -2.081118                                            float   [deg] Mount hour angle
SKYDEC   -7.102329                                            float   [deg] Telescope declination (pointing on sky)
SKYRA    170.24163                                            float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.102329                                            float   [deg] Target declination (to TCS)
TARGTRA  170.24163                                            float   [deg] Target right ascension (to TCS)
USEETC   T                                                    bool    ETC data available if true
USESKY   T                                                    bool    DOS Control: use Sky Monitor
USEFOCUS T                                                    bool    DOS Control: use focus
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                              str     Hexapod trim values
USEROTAT T                                                    bool    DOS Control: use rotator
ROTOFFST 138.8                                                float   [arcsec] Rotator offset
ROTENBLD T                                                    bool    Rotator enabled
ROTRATE  0.513                                                float   [arcsec/min] Rotator rate
USEGUIDR T                                                    bool    DOS Control: use guider
USEDONUT T                                                    bool    DOS Control: use donuts
SPECGRPH 6                                                    int     Spectrograph logical name (SP)
SPECID   7                                                    int     Spectrograph serial number (SM)
FEEBOX   lbnl061                                              str     CCD Controller serial number
VESSEL   21                                                   int     Cryostat serial number
FEEVER   v20160312                                            str     CCD Controller version
DETFLVER FAILED: invalid argument for get command             str     CCD Controller detector f
FEEPOWER ON                                                   str     FEE power status
FEEDMASK 2134851391                                           int     FEE dac mask
FEECMASK 1048575                                              int     FEE clk mask
CCDTEMP  -134.131                                             float   [deg C] CCD controller CCD temperature
RADESYS  FK5                                                  str     Coordinate reference frame of major/minor axes
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
OFFSET7  2.0,6.0017                                           str     [V] set value, measured value
DAC7     5.9998,6.0017                                        str     [V] set value, measured value
CASETEMP 58.9529                                              float   [deg C] CCD controller case temperature
DATASECC [8:2064, 2130:4193]                                  str     Data section for quadrant C
OFFSET1  0.4000000059604645,-8.9507                           str     [V] set value, measured value
OFFSET6  2.0,6.049                                            str     [V] set value, measured value
CLOCK17  9.0,0.9999                                           str     [V] high rail, low rail
DAC15    0.0,0.0                                              str     [V] set value, measured value
BIASSECA [2065:2128, 2:2065]                                  str     Bias section for quadrant A
TRIMSECC [8:2064, 2130:4193]                                  str     Trim section for quadrant C
CDSPARMS 400, 400, 8, 2000                                    str     CDS parameters
PRRSECD  [2193:4249, 4194:4194]                               str     Row prescan section for quadrant D
DAC1     -9.0002,-8.9507                                      str     [V] set value, measured value
DAC4     5.9998,6.049                                         str     [V] set value, measured value
PRRSECB  [2193:4249, 1:1]                                     str     Row prescan section for quadrant B
CLOCK6   9.9999,0.0                                           str     [V] high rail, low rail
CLOCK7   -2.0001,3.9999                                       str     [V] high rail, low rail
CLOCK11  9.9992,2.9993                                        str     [V] high rail, low rail
CLOCK8   9.9992,2.9993                                        str     [V] high rail, low rail
CCDSECC  [1:2057, 2065:4128]                                  str     CCD section for quadrant C
CCDCFG   default_lbnl_20210128.cfg                            str     CCD configuration file
CLOCK1   9.9999,0.0                                           str     [V] high rail, low rail
DETECTOR M1-51                                                str     Detector (ccd) identification
DIGITIME 56.4537                                              float   [s] Time to digitize image
CCDSECA  [1:2057, 1:2064]                                     str     CCD section for quadrant A
ORSECB   [2193:4249, 2066:2097]                               str     Row overscan section for quadrant B
CLOCK0   9.9999,0.0                                           str     [V] high rail, low rail
DAC14    0.0,-0.0297                                          str     [V] set value, measured value
DAC5     5.9998,6.0174                                        str     [V] set value, measured value
CLOCK18  9.0,0.9999                                           str     [V] high rail, low rail
PRRSECA  [8:2064, 1:1]                                        str     Row prescan section for quadrant A
ORSECA   [8:2064, 2066:2097]                                  str     Row overscan section for quadrant A
CLOCK5   9.9999,0.0                                           str     [V] high rail, low rail
DAC13    0.0,-0.0297                                          str     [V] set value, measured value
CAMERA   z6                                                   str     Camera name
PRESECA  [1:7, 2:2065]                                        str     Prescan section for quadrant A
DAC9     -25.0003,-25.0499                                    str     [V] set value, measured value
DETSECC  [1:2057, 2065:4128]                                  str     Detector section for quadrant C
CRYOTEMP 139.986                                              float   [deg K] Cryostat CCD temperature
CLOCK15  9.9992,2.9993                                        str     [V] high rail, low rail
DATASECB [2193:4249, 2:2065]                                  str     Data section for quadrant B
CLOCK2   9.9999,0.0                                           str     [V] high rail, low rail
CCDSIZE  4194,4256                                            str     CCD size in pixels (rows, columns)
CCDNAME  CCDSM7Z                                              str     CCD name
ORSECD   [2193:4249, 2098:2129]                               str     Row bias section for quadrant D
CLOCK14  9.9992,2.9993                                        str     [V] high rail, low rail
OFFSET0  0.4000000059604645,-8.9713                           str     [V] set value, measured value
ORSECC   [8:2064, 2098:2129]                                  str     Row overscan section for quadrant C
DETSECA  [1:2057, 1:2064]                                     str     Detector section for quadrant A
DAC3     -9.0002,-8.8889                                      str     [V] set value, measured value
BIASSECD [2129:2192, 2130:4193]                               str     Bias section for quadrant D
OFFSET3  0.4000000059604645,-8.8889                           str     [V] set value, measured value
DAC11    -25.0003,-25.0351                                    str     [V] set value, measured value
CLOCK13  9.9992,2.9993                                        str     [V] high rail, low rail
AMPSECC  [1:2057, 4128:2065]                                  str     AMP section for quadrant C
DATASECA [8:2064, 2:2065]                                     str     Data section for quadrant A
TRIMSECA [8:2064, 2:2065]                                     str     Trim section for quadrant A
DAC8     -25.0003,-24.6196                                    str     [V] set value, measured value
CPUTEMP  58.2246                                              float   [deg C] CCD controller CPU temperature
DAC10    -25.0003,-24.8422                                    str     [V] set value, measured value
CCDPREP  purge,clear                                          str     CCD prep actions
CLOCK10  9.9992,2.9993                                        str     [V] high rail, low rail
DAC6     5.9998,6.049                                         str     [V] set value, measured value
CLOCK12  9.9992,2.9993                                        str     [V] high rail, low rail
OFFSET2  0.4000000059604645,-8.961                            str     [V] set value, measured value
CLOCK3   -2.0001,3.9999                                       str     [V] high rail, low rail
PRESECC  [1:7, 2130:4193]                                     str     Prescan section for quadrant C
DAC12    0.0,-0.0297                                          str     [V] set value, measured value
TRIMSECD [2193:4249, 2130:4193]                               str     Trim section for quadrant D
AMPSECD  [4114:2058, 4128:2065]                               str     AMP section for quadrant D
PGAGAIN  3                                                    int     Controller gain
BIASSECB [2129:2192, 2:2065]                                  str     Bias section for quadrant B
BIASSECC [2065:2128, 2130:4193]                               str     Bias section for quadrant C
CCDSECD  [2058:4114, 2065:4128]                               str     CCD section for quadrant D
PRESECB  [4250:4256, 2:2065]                                  str     Prescan section for quadrant B
CLOCK9   9.9992,2.9993                                        str     [V] high rail, low rail
DATASECD [2193:4249, 2130:4193]                               str     Data section for quadrant D
CLOCK4   9.9999,0.0                                           str     [V] high rail, low rail
TRIMSECB [2193:4249, 2:2065]                                  str     Trim section for quadrant B
DAC17    20.0008,11.834                                       str     [V] set value, measured value
CRYOPRES 2.749e-07                                            str     [mb] Cryostat pressure (IP)
PRRSECC  [8:2064, 4194:4194]                                  str     Row prescan section for quadrant C
CCDTMING flatdark_lbnl_timing.txt                             str     CCD timing file
OFFSET5  2.0,6.0174                                           str     [V] set value, measured value
DELAYS   20, 20, 25, 40, 7, 3000, 7, 7, 400, 7                str     [10] Delay settings
CCDSECB  [2058:4114, 1:2064]                                  str     CCD section for quadrant B
OFFSET4  2.0,6.049                                            str     [V] set value, measured value
DAC16    39.9961,39.5472                                      str     [V] set value, measured value
BLDTIME  0.3518                                               float   [s] Time to build image
DAC0     -9.0002,-8.9713                                      str     [V] set value, measured value
DAC2     -9.0002,-8.961                                       str     [V] set value, measured value
DETSECD  [2058:4114, 2065:4128]                               str     Detector section for quadrant D
SETTINGS detectors_sm_20210128.json                           str     Name of DESI CCD settings file
PRESECD  [4250:4256, 2130:4193]                               str     Prescan section for quadrant D
DETSECB  [2058:4114, 1:2064]                                  str     Detector section for quadrant B
AMPSECB  [4114:2058, 1:2064]                                  str     AMP section for quadrant B
CLOCK16  9.9999,3.0                                           str     [V] high rail, low rail
AMPSECA  [1:2057, 1:2064]                                     str     AMP section for quadrant A
REQTIME  1860.0                                               float   [s] Requested exposure time
OBSID    kp4m20220114t110417                                  str     Unique observation identifier
PROCTYPE RAW                                                  str     Data processing level
PRODTYPE image                                                str     Data product type
CHECKSUM Tpa9UoV7ToZ7ToZ7                                     str     HDU checksum updated 2022-01-14T11:15:07
DATASUM  291832533                                            str     data unit checksum updated 2022-01-14T11:15:07
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 4256x4194]

HDU24
-----

EXTNAME = R6

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   4194                                                 int     number of rows in table
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
EXPID    118526                                               int     Exposure number
EXPFRAME 0                                                    int     Frame number
FRAMES   None                                                 Unknown Number of Frames in Archive
TILEID   4403                                                 int     DESI Tile ID
FIBASSGN /data/tiles/SVN_tiles/004/fiberassign-004403.fits.gz str     Fiber assign
FLAVOR   science                                              str     Observation type
SEQUENCE _Split                                               str     OCS Sequence name
PURPOSE  Main Survey                                          str     Purpose of observing night
PROGRAM  DARK                                                 str     Program name
PROPID   2020B-5000                                           str     Proposal ID
OBSERVER Jessica Chellino, Corentin Ravoux                    str     Names of observers
LEAD     Martin Landriau                                      str     Lead observer
INSTRUME DESI                                                 str     Instrument name
OBSERVAT KPNO                                                 str     Observatory name
OBS-LAT  31.96403                                             str     [deg] Observatory latitude
OBS-LONG -111.59989                                           str     [deg] Observatory east longitude
OBS-ELEV 2097.0                                               float   [m] Observatory elevation
TELESCOP KPNO 4.0-m telescope                                 str     Telescope name
CORRCTOR DESI Corrector                                       str     Corrector Identification
NIGHT    20220113                                             int     Observing night
TIMESYS  UTC                                                  str     Time system used for date-obs
DATE-OBS 2022-01-14T11:04:17.764723968                        str     [UTC] Observation data and start tim
TIME-OBS 2022-01-14T11:04:17.764723968                        str     [UTC] Observation start time
MJD-OBS  59593.46131672                                       float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:04:18.551089                           str     Time shutter opened
ST       11:13:28.520000                                      str     Local Sidereal time at observation start (HH:MM
EXPTIME  579.174                                              float   [s] Actual exposure time
REQRA    170.239                                              float   [deg] Requested right ascension (observer input
REQDEC   -7.093                                               float   [deg] Requested declination (observer input)
FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                   str     Telescope focus settings
VCCD     ON                                                   str     True (ON) if CCD voltage is on
VCCDON   2022-01-10T20:55:36.975335                           str     Time when CCD voltage was turned on
VCCDSEC  310758.6                                             float   [s] CCD on time in seconds
TRUSTEMP 12.267                                               float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.675                                               float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                               float   Epoch of observation
MOUNTAZ  176.725567                                           float   [deg] Mount azimuth angle
MOUNTDEC -7.102329                                            float   [deg] Mount declination
MOUNTEL  50.883914                                            float   [deg] Mount elevation angle
MOUNTHA  -2.081118                                            float   [deg] Mount hour angle
SKYDEC   -7.102329                                            float   [deg] Telescope declination (pointing on sky)
SKYRA    170.24163                                            float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.102329                                            float   [deg] Target declination (to TCS)
TARGTRA  170.24163                                            float   [deg] Target right ascension (to TCS)
USEETC   T                                                    bool    ETC data available if true
USESKY   T                                                    bool    DOS Control: use Sky Monitor
USEFOCUS T                                                    bool    DOS Control: use focus
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                              str     Hexapod trim values
USEROTAT T                                                    bool    DOS Control: use rotator
ROTOFFST 138.8                                                float   [arcsec] Rotator offset
ROTENBLD T                                                    bool    Rotator enabled
ROTRATE  0.513                                                float   [arcsec/min] Rotator rate
USEGUIDR T                                                    bool    DOS Control: use guider
USEDONUT T                                                    bool    DOS Control: use donuts
SPECGRPH 6                                                    int     Spectrograph logical name (SP)
SPECID   7                                                    int     Spectrograph serial number (SM)
FEEBOX   lbnl084                                              str     CCD Controller serial number
VESSEL   24                                                   int     Cryostat serial number
FEEVER   v20160312                                            str     CCD Controller version
DETFLVER FAILED: invalid argument for get command             str     CCD Controller detector f
FEEPOWER ON                                                   str     FEE power status
FEEDMASK 2134851391                                           int     FEE dac mask
FEECMASK 1048575                                              int     FEE clk mask
CCDTEMP  -133.7375                                            float   [deg C] CCD controller CCD temperature
RADESYS  FK5                                                  str     Coordinate reference frame of major/minor axes
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
CCDSECB  [2058:4114, 1:2064]                                  str     CCD section for quadrant B
ORSECA   [8:2064, 2066:2097]                                  str     Row overscan section for quadrant A
DAC10    -25.0003,-24.6196                                    str     [V] set value, measured value
CPUTEMP  58.9629                                              float   [deg C] CCD controller CPU temperature
AMPSECC  [1:2057, 4128:2065]                                  str     AMP section for quadrant C
DAC8     -25.0003,-24.5157                                    str     [V] set value, measured value
CLOCK0   9.9999,0.0                                           str     [V] high rail, low rail
TRIMSECD [2193:4249, 2130:4193]                               str     Trim section for quadrant D
TRIMSECB [2193:4249, 2:2065]                                  str     Trim section for quadrant B
CCDPREP  purge,clear                                          str     CCD prep actions
DAC5     5.9998,6.0385                                        str     [V] set value, measured value
DAC6     5.9998,6.0122                                        str     [V] set value, measured value
DATASECC [8:2064, 2130:4193]                                  str     Data section for quadrant C
PRESECC  [1:7, 2130:4193]                                     str     Prescan section for quadrant C
TRIMSECA [8:2064, 2:2065]                                     str     Trim section for quadrant A
OFFSET0  0.4000000059604645,-9.0125                           str     [V] set value, measured value
CDSPARMS 400, 400, 8, 2000                                    str     CDS parameters
PRRSECB  [2193:4249, 1:1]                                     str     Row prescan section for quadrant B
CLOCK10  9.9992,2.9993                                        str     [V] high rail, low rail
BIASSECA [2065:2128, 2:2065]                                  str     Bias section for quadrant A
CCDCFG   default_lbnl_20210128.cfg                            str     CCD configuration file
OFFSET3  0.4000000059604645,-8.9507                           str     [V] set value, measured value
PRRSECA  [8:2064, 1:1]                                        str     Row prescan section for quadrant A
AMPSECD  [4114:2058, 4128:2065]                               str     AMP section for quadrant D
CLOCK6   9.9999,0.0                                           str     [V] high rail, low rail
OFFSET4  2.0,6.0122                                           str     [V] set value, measured value
DAC9     -25.0003,-24.8718                                    str     [V] set value, measured value
CLOCK17  9.0,0.9999                                           str     [V] high rail, low rail
DETSECB  [2058:4114, 1:2064]                                  str     Detector section for quadrant B
AMPSECA  [1:2057, 1:2064]                                     str     AMP section for quadrant A
CLOCK1   9.9999,0.0                                           str     [V] high rail, low rail
DAC0     -9.0002,-9.0125                                      str     [V] set value, measured value
CLOCK14  9.9992,2.9993                                        str     [V] high rail, low rail
DATASECD [2193:4249, 2130:4193]                               str     Data section for quadrant D
CLOCK5   9.9999,0.0                                           str     [V] high rail, low rail
OFFSET7  2.0,6.0069                                           str     [V] set value, measured value
CLOCK13  9.9992,2.9993                                        str     [V] high rail, low rail
DELAYS   20, 20, 25, 40, 7, 3000, 7, 7, 400, 7                str     [10] Delay settings
DETSECA  [1:2057, 1:2064]                                     str     Detector section for quadrant A
DATASECA [8:2064, 2:2065]                                     str     Data section for quadrant A
PGAGAIN  3                                                    int     Controller gain
OFFSET6  2.0,6.0122                                           str     [V] set value, measured value
CCDSIZE  4194,4256                                            str     CCD size in pixels (rows, columns)
DAC16    39.9961,39.4548                                      str     [V] set value, measured value
DAC7     5.9998,6.0122                                        str     [V] set value, measured value
CLOCK11  9.9992,2.9993                                        str     [V] high rail, low rail
AMPSECB  [4114:2058, 1:2064]                                  str     AMP section for quadrant B
PRESECB  [4250:4256, 2:2065]                                  str     Prescan section for quadrant B
CLOCK18  9.0,0.9999                                           str     [V] high rail, low rail
DAC14    0.0,-0.0594                                          str     [V] set value, measured value
BLDTIME  0.3565                                               float   [s] Time to build image
PRESECA  [1:7, 2:2065]                                        str     Prescan section for quadrant A
DETECTOR M1-15                                                str     Detector (ccd) identification
CLOCK2   9.9999,0.0                                           str     [V] high rail, low rail
PRESECD  [4250:4256, 2130:4193]                               str     Prescan section for quadrant D
DAC1     -9.0002,-9.0434                                      str     [V] set value, measured value
PRRSECC  [8:2064, 4194:4194]                                  str     Row prescan section for quadrant C
SETTINGS detectors_sm_20210128.json                           str     Name of DESI CCD settings file
DAC11    -25.0003,-24.8125                                    str     [V] set value, measured value
BIASSECD [2129:2192, 2130:4193]                               str     Bias section for quadrant D
CRYOTEMP 163.044                                              float   [deg K] Cryostat CCD temperature
DAC4     5.9998,6.0122                                        str     [V] set value, measured value
CLOCK3   -2.0001,3.9999                                       str     [V] high rail, low rail
CCDTMING flatdark_lbnl_timing.txt                             str     CCD timing file
CLOCK4   9.9999,0.0                                           str     [V] high rail, low rail
OFFSET5  2.0,6.0385                                           str     [V] set value, measured value
DAC3     -9.0002,-8.9507                                      str     [V] set value, measured value
CRYOPRES 1.014e-07                                            str     [mb] Cryostat pressure (IP)
OFFSET1  0.4000000059604645,-9.0434                           str     [V] set value, measured value
CLOCK8   9.9992,2.9993                                        str     [V] high rail, low rail
CLOCK9   9.9992,2.9993                                        str     [V] high rail, low rail
BIASSECC [2065:2128, 2130:4193]                               str     Bias section for quadrant C
DAC2     -9.0002,-8.9095                                      str     [V] set value, measured value
DAC13    0.0,-0.0594                                          str     [V] set value, measured value
PRRSECD  [2193:4249, 4194:4194]                               str     Row prescan section for quadrant D
ORSECD   [2193:4249, 2098:2129]                               str     Row bias section for quadrant D
CASETEMP 58.9529                                              float   [deg C] CCD controller case temperature
OFFSET2  0.4000000059604645,-8.9095                           str     [V] set value, measured value
DETSECC  [1:2057, 2065:4128]                                  str     Detector section for quadrant C
DETSECD  [2058:4114, 2065:4128]                               str     Detector section for quadrant D
CCDSECD  [2058:4114, 2065:4128]                               str     CCD section for quadrant D
ORSECC   [8:2064, 2098:2129]                                  str     Row overscan section for quadrant C
CLOCK16  9.9999,3.0                                           str     [V] high rail, low rail
CAMERA   r6                                                   str     Camera name
CCDSECC  [1:2057, 2065:4128]                                  str     CCD section for quadrant C
CCDSECA  [1:2057, 1:2064]                                     str     CCD section for quadrant A
ORSECB   [2193:4249, 2066:2097]                               str     Row overscan section for quadrant B
CLOCK15  9.9992,2.9993                                        str     [V] high rail, low rail
TRIMSECC [8:2064, 2130:4193]                                  str     Trim section for quadrant C
CCDNAME  CCDSM7R                                              str     CCD name
DAC15    0.0,-0.0445                                          str     [V] set value, measured value
CLOCK12  9.9992,2.9993                                        str     [V] high rail, low rail
DAC17    20.0008,11.4558                                      str     [V] set value, measured value
DIGITIME 56.4617                                              float   [s] Time to digitize image
BIASSECB [2129:2192, 2:2065]                                  str     Bias section for quadrant B
CLOCK7   -2.0001,3.9999                                       str     [V] high rail, low rail
DAC12    0.0,-0.0594                                          str     [V] set value, measured value
DATASECB [2193:4249, 2:2065]                                  str     Data section for quadrant B
REQTIME  1860.0                                               float   [s] Requested exposure time
OBSID    kp4m20220114t110417                                  str     Unique observation identifier
PROCTYPE RAW                                                  str     Data processing level
PRODTYPE image                                                str     Data product type
CHECKSUM Z6gja4ZiU4diZ4Zi                                     str     HDU checksum updated 2022-01-14T11:15:07
DATASUM  2455340579                                           str     data unit checksum updated 2022-01-14T11:15:07
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 4256x4194]

HDU25
-----

EXTNAME = B6

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   4162                                                 int     number of rows in table
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
EXPID    118526                                               int     Exposure number
EXPFRAME 0                                                    int     Frame number
FRAMES   None                                                 Unknown Number of Frames in Archive
TILEID   4403                                                 int     DESI Tile ID
FIBASSGN /data/tiles/SVN_tiles/004/fiberassign-004403.fits.gz str     Fiber assign
FLAVOR   science                                              str     Observation type
SEQUENCE _Split                                               str     OCS Sequence name
PURPOSE  Main Survey                                          str     Purpose of observing night
PROGRAM  DARK                                                 str     Program name
PROPID   2020B-5000                                           str     Proposal ID
OBSERVER Jessica Chellino, Corentin Ravoux                    str     Names of observers
LEAD     Martin Landriau                                      str     Lead observer
INSTRUME DESI                                                 str     Instrument name
OBSERVAT KPNO                                                 str     Observatory name
OBS-LAT  31.96403                                             str     [deg] Observatory latitude
OBS-LONG -111.59989                                           str     [deg] Observatory east longitude
OBS-ELEV 2097.0                                               float   [m] Observatory elevation
TELESCOP KPNO 4.0-m telescope                                 str     Telescope name
CORRCTOR DESI Corrector                                       str     Corrector Identification
NIGHT    20220113                                             int     Observing night
TIMESYS  UTC                                                  str     Time system used for date-obs
DATE-OBS 2022-01-14T11:04:17.764723968                        str     [UTC] Observation data and start tim
TIME-OBS 2022-01-14T11:04:17.764723968                        str     [UTC] Observation start time
MJD-OBS  59593.46131672                                       float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:04:18.551089                           str     Time shutter opened
ST       11:13:28.520000                                      str     Local Sidereal time at observation start (HH:MM
EXPTIME  579.174                                              float   [s] Actual exposure time
REQRA    170.239                                              float   [deg] Requested right ascension (observer input
REQDEC   -7.093                                               float   [deg] Requested declination (observer input)
FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                   str     Telescope focus settings
VCCD     ON                                                   str     True (ON) if CCD voltage is on
VCCDON   2022-01-10T20:55:39.353866                           str     Time when CCD voltage was turned on
VCCDSEC  310749.3                                             float   [s] CCD on time in seconds
TRUSTEMP 12.267                                               float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.675                                               float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                               float   Epoch of observation
MOUNTAZ  176.725567                                           float   [deg] Mount azimuth angle
MOUNTDEC -7.102329                                            float   [deg] Mount declination
MOUNTEL  50.883914                                            float   [deg] Mount elevation angle
MOUNTHA  -2.081118                                            float   [deg] Mount hour angle
SKYDEC   -7.102329                                            float   [deg] Telescope declination (pointing on sky)
SKYRA    170.24163                                            float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.102329                                            float   [deg] Target declination (to TCS)
TARGTRA  170.24163                                            float   [deg] Target right ascension (to TCS)
USEETC   T                                                    bool    ETC data available if true
USESKY   T                                                    bool    DOS Control: use Sky Monitor
USEFOCUS T                                                    bool    DOS Control: use focus
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                              str     Hexapod trim values
USEROTAT T                                                    bool    DOS Control: use rotator
ROTOFFST 138.8                                                float   [arcsec] Rotator offset
ROTENBLD T                                                    bool    Rotator enabled
ROTRATE  0.513                                                float   [arcsec/min] Rotator rate
USEGUIDR T                                                    bool    DOS Control: use guider
USEDONUT T                                                    bool    DOS Control: use donuts
SPECGRPH 6                                                    int     Spectrograph logical name (SP)
SPECID   7                                                    int     Spectrograph serial number (SM)
FEEBOX   lbnl075                                              str     CCD Controller serial number
VESSEL   22                                                   int     Cryostat serial number
FEEVER   v20160312                                            str     CCD Controller version
DETFLVER FAILED: invalid argument for get command             str     CCD Controller detector f
FEEPOWER ON                                                   str     FEE power status
FEEDMASK 2134851391                                           int     FEE dac mask
FEECMASK 1048575                                              int     FEE clk mask
CCDTEMP  850.0                                                float   [deg C] CCD controller CCD temperature
RADESYS  FK5                                                  str     Coordinate reference frame of major/minor axes
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
CLOCK6   3.9999,-4.0002                                       str     [V] high rail, low rail
ORSECB   [2181:4228, 2050:2081]                               str     Row overscan section for quadrant B
DAC5     0.0,-0.0053                                          str     [V] set value, measured value
ORSECD   [2181:4228, 2082:2113]                               str     Row bias section for quadrant D
CLOCK11  0.0,0.0                                              str     [V] high rail, low rail
DETSECB  [2049:4096, 1:2048]                                  str     Detector section for quadrant B
CDSPARMS 350, 350, 8, 1000                                    str     CDS parameters
BIASSECB [2117:2180, 2:2049]                                  str     Bias section for quadrant B
SETTINGS detectors_sm_20210128.json                           str     Name of DESI CCD settings file
CCDCFG   sn22813_sta_20210128.cfg                             str     CCD configuration file
PRESECB  [4229:4232, 2:2049]                                  str     Prescan section for quadrant B
CLOCK12  3.0,-8.0001                                          str     [V] high rail, low rail
PRESECD  [4229:4232, 2114:4161]                               str     Prescan section for quadrant D
OFFSET5  -1.100000023841858,-0.0053                           str     [V] set value, measured value
DAC7     0.0,0.0                                              str     [V] set value, measured value
CPUTEMP  52.9336                                              float   [deg C] CCD controller CPU temperature
CLOCK8   3.0,-8.0001                                          str     [V] high rail, low rail
AMPSECD  [4096:2049, 4096:2049]                               str     AMP section for quadrant D
ORSECA   [5:2052, 2050:2081]                                  str     Row overscan section for quadrant A
CAMERA   b6                                                   str     Camera name
CLOCK1   3.9999,-4.0002                                       str     [V] high rail, low rail
DAC16    0.0,64.449                                           str     [V] set value, measured value
CCDTMING flatdark_sta_timing.txt                              str     CCD timing file
OFFSET1  -1.5,15.8105                                         str     [V] set value, measured value
BIASSECA [2053:2116, 2:2049]                                  str     Bias section for quadrant A
DETECTOR sn22813                                              str     Detector (ccd) identification
CLOCK18  3.9999,-4.0002                                       str     [V] high rail, low rail
CLOCK3   6.9999,-2.0001                                       str     [V] high rail, low rail
OFFSET3  -1.5,15.8311                                         str     [V] set value, measured value
OFFSET2  -1.5,15.9032                                         str     [V] set value, measured value
AMPSECC  [2048:1, 2049:4096]                                  str     AMP section for quadrant C
DAC4     0.0,0.0053                                           str     [V] set value, measured value
DAC17    -0.0,0.1098                                          str     [V] set value, measured value
CLOCK10  3.0,-8.0001                                          str     [V] high rail, low rail
CLOCK7   6.9999,-2.0001                                       str     [V] high rail, low rail
AMPSECB  [2049:4096, 2048:1]                                  str     AMP section for quadrant B
DATASECA [5:2052, 2:2049]                                     str     Data section for quadrant A
CLOCK16  0.0,0.0                                              str     [V] high rail, low rail
CCDSECB  [2049:4096, 1:2048]                                  str     CCD section for quadrant B
DATASECC [5:2052, 2114:4161]                                  str     Data section for quadrant C
CLOCK13  3.0,-8.0001                                          str     [V] high rail, low rail
TRIMSECB [2181:4228, 2:2049]                                  str     Trim section for quadrant B
CCDSECC  [1:2048, 2049:4096]                                  str     CCD section for quadrant C
OFFSET0  -1.5,15.8414                                         str     [V] set value, measured value
DETSECD  [2049:4096, 2049:4096]                               str     Detector section for quadrant D
DAC8     26.9998,26.0294                                      str     [V] set value, measured value
DAC10    26.9998,26.9049                                      str     [V] set value, measured value
TRIMSECA [5:2052, 2:2049]                                     str     Trim section for quadrant A
CCDNAME  CCDSM7B                                              str     CCD name
DAC2     15.9998,15.9135                                      str     [V] set value, measured value
DAC1     15.9998,15.8311                                      str     [V] set value, measured value
BIASSECC [2053:2116, 2114:4161]                               str     Bias section for quadrant C
PRRSECB  [2181:4228, 1:1]                                     str     Row prescan section for quadrant B
PRRSECD  [2181:4228, 4162:4162]                               str     Row prescan section for quadrant D
DELAYS   13, 13, 25, 25, 8, 3000, 7, 7, 400, 7                str     [10] Delay settings
DETSECC  [1:2048, 2049:4096]                                  str     Detector section for quadrant C
DATASECB [2181:4228, 2:2049]                                  str     Data section for quadrant B
DAC13    0.0,-5.044                                           str     [V] set value, measured value
DAC3     15.9998,15.8517                                      str     [V] set value, measured value
CRYOTEMP 163.044                                              float   [deg K] Cryostat CCD temperature
CLOCK0   3.9999,-4.0002                                       str     [V] high rail, low rail
DIGITIME 49.5331                                              float   [s] Time to digitize image
DAC0     15.9998,15.8414                                      str     [V] set value, measured value
PRESECC  [1:4, 2114:4161]                                     str     Prescan section for quadrant C
DAC6     0.0,0.0105                                           str     [V] set value, measured value
TRIMSECD [2181:4228, 2114:4161]                               str     Trim section for quadrant D
CCDSIZE  4162,4232                                            str     CCD size in pixels (rows, columns)
CLOCK5   3.9999,-4.0002                                       str     [V] high rail, low rail
DAC12    0.0,5.044                                            str     [V] set value, measured value
CLOCK2   3.9999,-4.0002                                       str     [V] high rail, low rail
PGAGAIN  5                                                    int     Controller gain
CLOCK14  3.0,-8.0001                                          str     [V] high rail, low rail
CRYOPRES 1.014e-07                                            str     [mb] Cryostat pressure (IP)
PRESECA  [1:4, 2:2049]                                        str     Prescan section for quadrant A
CCDSECA  [1:2048, 1:2048]                                     str     CCD section for quadrant A
TRIMSECC [5:2052, 2114:4161]                                  str     Trim section for quadrant C
DAC9     26.9998,26.252                                       str     [V] set value, measured value
OFFSET6  -1.100000023841858,0.0053                            str     [V] set value, measured value
CCDSECD  [2049:4096, 2049:4096]                               str     CCD section for quadrant D
CLOCK15  0.0,0.0                                              str     [V] high rail, low rail
DAC11    26.9998,26.9346                                      str     [V] set value, measured value
CLOCK9   3.0,-8.0001                                          str     [V] high rail, low rail
OFFSET4  -1.100000023841858,0.0053                            str     [V] set value, measured value
DETSECA  [1:2048, 1:2048]                                     str     Detector section for quadrant A
ORSECC   [5:2052, 2082:2113]                                  str     Row overscan section for quadrant C
CLOCK17  3.9999,-4.0002                                       str     [V] high rail, low rail
PRRSECA  [5:2052, 1:1]                                        str     Row prescan section for quadrant A
AMPSECA  [1:2048, 1:2048]                                     str     AMP section for quadrant A
CCDPREP  purge,clear                                          str     CCD prep actions
DAC14    0.0,0.8112                                           str     [V] set value, measured value
BIASSECD [2117:2180, 2114:4161]                               str     Bias section for quadrant D
DAC15    19.9997,19.6872                                      str     [V] set value, measured value
PRRSECC  [5:2052, 4162:4162]                                  str     Row prescan section for quadrant C
OFFSET7  -1.100000023841858,0.0                               str     [V] set value, measured value
DATASECD [2181:4228, 2114:4161]                               str     Data section for quadrant D
BLDTIME  0.3516                                               float   [s] Time to build image
CASETEMP 52.3083                                              float   [deg C] CCD controller case temperature
CLOCK4   3.9999,-4.0002                                       str     [V] high rail, low rail
REQTIME  1860.0                                               float   [s] Requested exposure time
OBSID    kp4m20220114t110417                                  str     Unique observation identifier
PROCTYPE RAW                                                  str     Data processing level
PRODTYPE image                                                str     Data product type
CHECKSUM gJROiJPLgJPLgJPL                                     str     HDU checksum updated 2022-01-14T11:15:07
DATASUM  3185992570                                           str     data unit checksum updated 2022-01-14T11:15:07
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 4232x4162]

HDU26
-----

EXTNAME = Z1

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   4194                                                 int     number of rows in table
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
EXPID    118526                                               int     Exposure number
EXPFRAME 0                                                    int     Frame number
FRAMES   None                                                 Unknown Number of Frames in Archive
TILEID   4403                                                 int     DESI Tile ID
FIBASSGN /data/tiles/SVN_tiles/004/fiberassign-004403.fits.gz str     Fiber assign
FLAVOR   science                                              str     Observation type
SEQUENCE _Split                                               str     OCS Sequence name
PURPOSE  Main Survey                                          str     Purpose of observing night
PROGRAM  DARK                                                 str     Program name
PROPID   2020B-5000                                           str     Proposal ID
OBSERVER Jessica Chellino, Corentin Ravoux                    str     Names of observers
LEAD     Martin Landriau                                      str     Lead observer
INSTRUME DESI                                                 str     Instrument name
OBSERVAT KPNO                                                 str     Observatory name
OBS-LAT  31.96403                                             str     [deg] Observatory latitude
OBS-LONG -111.59989                                           str     [deg] Observatory east longitude
OBS-ELEV 2097.0                                               float   [m] Observatory elevation
TELESCOP KPNO 4.0-m telescope                                 str     Telescope name
CORRCTOR DESI Corrector                                       str     Corrector Identification
NIGHT    20220113                                             int     Observing night
TIMESYS  UTC                                                  str     Time system used for date-obs
DATE-OBS 2022-01-14T11:04:17.770361088                        str     [UTC] Observation data and start tim
TIME-OBS 2022-01-14T11:04:17.770361088                        str     [UTC] Observation start time
MJD-OBS  59593.46131679                                       float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:04:18.378370                           str     Time shutter opened
ST       11:13:28.520000                                      str     Local Sidereal time at observation start (HH:MM
EXPTIME  579.377                                              float   [s] Actual exposure time
REQRA    170.239                                              float   [deg] Requested right ascension (observer input
REQDEC   -7.093                                               float   [deg] Requested declination (observer input)
FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                   str     Telescope focus settings
VCCD     ON                                                   str     True (ON) if CCD voltage is on
VCCDON   2022-01-10T20:55:43.760937                           str     Time when CCD voltage was turned on
VCCDSEC  310751.8                                             float   [s] CCD on time in seconds
TRUSTEMP 12.267                                               float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.675                                               float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                               float   Epoch of observation
MOUNTAZ  176.725567                                           float   [deg] Mount azimuth angle
MOUNTDEC -7.102329                                            float   [deg] Mount declination
MOUNTEL  50.883914                                            float   [deg] Mount elevation angle
MOUNTHA  -2.081118                                            float   [deg] Mount hour angle
SKYDEC   -7.102329                                            float   [deg] Telescope declination (pointing on sky)
SKYRA    170.24163                                            float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.102329                                            float   [deg] Target declination (to TCS)
TARGTRA  170.24163                                            float   [deg] Target right ascension (to TCS)
USEETC   T                                                    bool    ETC data available if true
USESKY   T                                                    bool    DOS Control: use Sky Monitor
USEFOCUS T                                                    bool    DOS Control: use focus
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                              str     Hexapod trim values
USEROTAT T                                                    bool    DOS Control: use rotator
ROTOFFST 138.8                                                float   [arcsec] Rotator offset
ROTENBLD T                                                    bool    Rotator enabled
ROTRATE  0.513                                                float   [arcsec/min] Rotator rate
USEGUIDR T                                                    bool    DOS Control: use guider
USEDONUT T                                                    bool    DOS Control: use donuts
SPECGRPH 1                                                    int     Spectrograph logical name (SP)
SPECID   10                                                   int     Spectrograph serial number (SM)
FEEBOX   lbnl077                                              str     CCD Controller serial number
VESSEL   30                                                   int     Cryostat serial number
FEEVER   v20160312                                            str     CCD Controller version
DETFLVER FAILED: invalid argument for get command             str     CCD Controller detector f
FEEPOWER ON                                                   str     FEE power status
FEEDMASK 2134851391                                           int     FEE dac mask
FEECMASK 1048575                                              int     FEE clk mask
CCDTEMP  -134.338                                             float   [deg C] CCD controller CCD temperature
RADESYS  FK5                                                  str     Coordinate reference frame of major/minor axes
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
CLOCK8   9.9992,2.9993                                        str     [V] high rail, low rail
DAC12    0.0,0.1039                                           str     [V] set value, measured value
OFFSET4  2.0,6.0543                                           str     [V] set value, measured value
CLOCK2   9.9999,-1.0002                                       str     [V] high rail, low rail
BIASSECA [2065:2128, 2:2065]                                  str     Bias section for quadrant A
CLOCK13  9.9992,2.9993                                        str     [V] high rail, low rail
OFFSET5  2.0,6.07                                             str     [V] set value, measured value
PRESECD  [4250:4256, 2130:4193]                               str     Prescan section for quadrant D
DAC14    0.0,0.089                                            str     [V] set value, measured value
OFFSET7  2.0,6.0648                                           str     [V] set value, measured value
TRIMSECA [8:2064, 2:2065]                                     str     Trim section for quadrant A
DAC3     -9.0002,-8.7962                                      str     [V] set value, measured value
CRYOPRES 6.628e-08                                            str     [mb] Cryostat pressure (IP)
CPUTEMP  57.7324                                              float   [deg C] CCD controller CPU temperature
OFFSET3  0.4000000059604645,-8.7962                           str     [V] set value, measured value
ORSECD   [2193:4249, 2098:2129]                               str     Row bias section for quadrant D
CAMERA   z1                                                   str     Camera name
CLOCK5   9.9999,-1.0002                                       str     [V] high rail, low rail
DAC13    0.0,0.1039                                           str     [V] set value, measured value
DETSECB  [2058:4114, 1:2064]                                  str     Detector section for quadrant B
DAC15    0.0,0.089                                            str     [V] set value, measured value
BIASSECB [2129:2192, 2:2065]                                  str     Bias section for quadrant B
OFFSET6  2.0,6.0437                                           str     [V] set value, measured value
DETSECD  [2058:4114, 2065:4128]                               str     Detector section for quadrant D
SETTINGS detectors.json                                       str     Name of DESI CCD settings file
CCDPREP  purge,clear                                          str     CCD prep actions
PRRSECC  [8:2064, 4194:4194]                                  str     Row prescan section for quadrant C
DAC6     5.9998,6.0437                                        str     [V] set value, measured value
BLDTIME  0.3531                                               float   [s] Time to build image
CLOCK0   9.9999,-1.0002                                       str     [V] high rail, low rail
AMPSECC  [1:2057, 4128:2065]                                  str     AMP section for quadrant C
TRIMSECD [2193:4249, 2130:4193]                               str     Trim section for quadrant D
CLOCK1   9.9999,-1.0002                                       str     [V] high rail, low rail
DATASECA [8:2064, 2:2065]                                     str     Data section for quadrant A
OFFSET1  0.4000000059604645,-8.8374                           str     [V] set value, measured value
DAC2     -9.0002,-8.8786                                      str     [V] set value, measured value
DATASECD [2193:4249, 2130:4193]                               str     Data section for quadrant D
CDSPARMS 400, 400, 8, 2000                                    str     CDS parameters
OFFSET2  0.4000000059604645,-8.8786                           str     [V] set value, measured value
CLOCK4   9.9999,-1.0002                                       str     [V] high rail, low rail
DAC11    -25.0003,-24.3821                                    str     [V] set value, measured value
DETSECC  [1:2057, 2065:4128]                                  str     Detector section for quadrant C
CCDSECA  [1:2057, 1:2064]                                     str     CCD section for quadrant A
DETECTOR M1-35                                                str     Detector (ccd) identification
DAC1     -9.0002,-8.8374                                      str     [V] set value, measured value
CCDNAME  CCDSM10Z                                             str     CCD name
CLOCK17  9.0,0.9999                                           str     [V] high rail, low rail
ORSECA   [8:2064, 2066:2097]                                  str     Row overscan section for quadrant A
DAC17    20.0008,12.0658                                      str     [V] set value, measured value
TRIMSECB [2193:4249, 2:2065]                                  str     Trim section for quadrant B
DAC0     -9.0002,-8.8992                                      str     [V] set value, measured value
DAC8     -25.0003,-24.6344                                    str     [V] set value, measured value
PRRSECD  [2193:4249, 4194:4194]                               str     Row prescan section for quadrant D
PRESECB  [4250:4256, 2:2065]                                  str     Prescan section for quadrant B
TRIMSECC [8:2064, 2130:4193]                                  str     Trim section for quadrant C
CCDSECB  [2058:4114, 1:2064]                                  str     CCD section for quadrant B
AMPSECA  [1:2057, 1:2064]                                     str     AMP section for quadrant A
DAC16    39.9961,39.27                                        str     [V] set value, measured value
CLOCK12  9.9992,2.9993                                        str     [V] high rail, low rail
DAC9     -25.0003,-25.0351                                    str     [V] set value, measured value
CCDTMING flatdark_lbnl_timing.txt                             str     CCD timing file
CLOCK9   9.9992,2.9993                                        str     [V] high rail, low rail
CLOCK16  9.9999,3.0                                           str     [V] high rail, low rail
CLOCK3   -2.0001,3.9999                                       str     [V] high rail, low rail
DIGITIME 56.4639                                              float   [s] Time to digitize image
CLOCK10  9.9992,2.9993                                        str     [V] high rail, low rail
CCDCFG   M1-35_lbnl_20220107.cfg                              str     CCD configuration file
BIASSECC [2065:2128, 2130:4193]                               str     Bias section for quadrant C
AMPSECB  [4114:2058, 1:2064]                                  str     AMP section for quadrant B
CCDSIZE  4194,4256                                            str     CCD size in pixels (rows, columns)
PGAGAIN  3                                                    int     Controller gain
BIASSECD [2129:2192, 2130:4193]                               str     Bias section for quadrant D
CRYOTEMP 139.962                                              float   [deg K] Cryostat CCD temperature
PRRSECB  [2193:4249, 1:1]                                     str     Row prescan section for quadrant B
ORSECB   [2193:4249, 2066:2097]                               str     Row overscan section for quadrant B
DAC4     5.9998,6.0595                                        str     [V] set value, measured value
CLOCK14  9.9992,2.9993                                        str     [V] high rail, low rail
PRRSECA  [8:2064, 1:1]                                        str     Row prescan section for quadrant A
PRESECC  [1:7, 2130:4193]                                     str     Prescan section for quadrant C
CLOCK6   9.9999,-1.0002                                       str     [V] high rail, low rail
CLOCK18  9.0,0.9999                                           str     [V] high rail, low rail
CCDSECC  [1:2057, 2065:4128]                                  str     CCD section for quadrant C
DATASECC [8:2064, 2130:4193]                                  str     Data section for quadrant C
DAC10    -25.0003,-24.204                                     str     [V] set value, measured value
CASETEMP 56.9841                                              float   [deg C] CCD controller case temperature
PRESECA  [1:7, 2:2065]                                        str     Prescan section for quadrant A
OFFSET0  0.4000000059604645,-8.8992                           str     [V] set value, measured value
DAC5     5.9998,6.07                                          str     [V] set value, measured value
AMPSECD  [4114:2058, 4128:2065]                               str     AMP section for quadrant D
DELAYS   20, 20, 25, 40, 7, 3000, 7, 7, 400, 7                str     [10] Delay settings
CLOCK11  9.9992,2.9993                                        str     [V] high rail, low rail
CCDSECD  [2058:4114, 2065:4128]                               str     CCD section for quadrant D
DETSECA  [1:2057, 1:2064]                                     str     Detector section for quadrant A
DATASECB [2193:4249, 2:2065]                                  str     Data section for quadrant B
CLOCK15  9.9992,2.9993                                        str     [V] high rail, low rail
CLOCK7   -2.0001,3.9999                                       str     [V] high rail, low rail
DAC7     5.9998,6.0648                                        str     [V] set value, measured value
ORSECC   [8:2064, 2098:2129]                                  str     Row overscan section for quadrant C
REQTIME  1860.0                                               float   [s] Requested exposure time
OBSID    kp4m20220114t110417                                  str     Unique observation identifier
PROCTYPE RAW                                                  str     Data processing level
PRODTYPE image                                                str     Data product type
CHECKSUM PGJaPD9XPDGaPD9W                                     str     HDU checksum updated 2022-01-14T11:15:08
DATASUM  14361011                                             str     data unit checksum updated 2022-01-14T11:15:08
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 4256x4194]

HDU27
-----

EXTNAME = R1

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   4194                                                 int     number of rows in table
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
EXPID    118526                                               int     Exposure number
EXPFRAME 0                                                    int     Frame number
FRAMES   None                                                 Unknown Number of Frames in Archive
TILEID   4403                                                 int     DESI Tile ID
FIBASSGN /data/tiles/SVN_tiles/004/fiberassign-004403.fits.gz str     Fiber assign
FLAVOR   science                                              str     Observation type
SEQUENCE _Split                                               str     OCS Sequence name
PURPOSE  Main Survey                                          str     Purpose of observing night
PROGRAM  DARK                                                 str     Program name
PROPID   2020B-5000                                           str     Proposal ID
OBSERVER Jessica Chellino, Corentin Ravoux                    str     Names of observers
LEAD     Martin Landriau                                      str     Lead observer
INSTRUME DESI                                                 str     Instrument name
OBSERVAT KPNO                                                 str     Observatory name
OBS-LAT  31.96403                                             str     [deg] Observatory latitude
OBS-LONG -111.59989                                           str     [deg] Observatory east longitude
OBS-ELEV 2097.0                                               float   [m] Observatory elevation
TELESCOP KPNO 4.0-m telescope                                 str     Telescope name
CORRCTOR DESI Corrector                                       str     Corrector Identification
NIGHT    20220113                                             int     Observing night
TIMESYS  UTC                                                  str     Time system used for date-obs
DATE-OBS 2022-01-14T11:04:17.770361088                        str     [UTC] Observation data and start tim
TIME-OBS 2022-01-14T11:04:17.770361088                        str     [UTC] Observation start time
MJD-OBS  59593.46131679                                       float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:04:18.378370                           str     Time shutter opened
ST       11:13:28.520000                                      str     Local Sidereal time at observation start (HH:MM
EXPTIME  579.377                                              float   [s] Actual exposure time
REQRA    170.239                                              float   [deg] Requested right ascension (observer input
REQDEC   -7.093                                               float   [deg] Requested declination (observer input)
FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                   str     Telescope focus settings
VCCD     ON                                                   str     True (ON) if CCD voltage is on
VCCDON   2022-01-10T20:55:36.986559                           str     Time when CCD voltage was turned on
VCCDSEC  310758.6                                             float   [s] CCD on time in seconds
TRUSTEMP 12.267                                               float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.675                                               float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                               float   Epoch of observation
MOUNTAZ  176.725567                                           float   [deg] Mount azimuth angle
MOUNTDEC -7.102329                                            float   [deg] Mount declination
MOUNTEL  50.883914                                            float   [deg] Mount elevation angle
MOUNTHA  -2.081118                                            float   [deg] Mount hour angle
SKYDEC   -7.102329                                            float   [deg] Telescope declination (pointing on sky)
SKYRA    170.24163                                            float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.102329                                            float   [deg] Target declination (to TCS)
TARGTRA  170.24163                                            float   [deg] Target right ascension (to TCS)
USEETC   T                                                    bool    ETC data available if true
USESKY   T                                                    bool    DOS Control: use Sky Monitor
USEFOCUS T                                                    bool    DOS Control: use focus
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                              str     Hexapod trim values
USEROTAT T                                                    bool    DOS Control: use rotator
ROTOFFST 138.8                                                float   [arcsec] Rotator offset
ROTENBLD T                                                    bool    Rotator enabled
ROTRATE  0.513                                                float   [arcsec/min] Rotator rate
USEGUIDR T                                                    bool    DOS Control: use guider
USEDONUT T                                                    bool    DOS Control: use donuts
SPECGRPH 1                                                    int     Spectrograph logical name (SP)
SPECID   10                                                   int     Spectrograph serial number (SM)
FEEBOX   lbnl052                                              str     CCD Controller serial number
VESSEL   23                                                   int     Cryostat serial number
FEEVER   v20160312                                            str     CCD Controller version
DETFLVER FAILED: invalid argument for get command             str     CCD Controller detector f
FEEPOWER ON                                                   str     FEE power status
FEEDMASK 2134851391                                           int     FEE dac mask
FEECMASK 1048575                                              int     FEE clk mask
CCDTEMP  -134.483                                             float   [deg C] CCD controller CCD temperature
RADESYS  FK5                                                  str     Coordinate reference frame of major/minor axes
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
CLOCK0   9.9999,-3.0003                                       str     [V] high rail, low rail
DAC14    0.0,0.0445                                           str     [V] set value, measured value
CLOCK10  9.9992,2.9993                                        str     [V] high rail, low rail
CLOCK7   -2.0001,3.9999                                       str     [V] high rail, low rail
AMPSECD  [4114:2058, 4128:2065]                               str     AMP section for quadrant D
CASETEMP 58.8298                                              float   [deg C] CCD controller case temperature
PRESECB  [4250:4256, 2:2065]                                  str     Prescan section for quadrant B
CCDSECD  [2058:4114, 2065:4128]                               str     CCD section for quadrant D
TRIMSECC [8:2064, 2130:4193]                                  str     Trim section for quadrant C
DAC16    39.9961,39.039                                       str     [V] set value, measured value
CLOCK14  9.9992,2.9993                                        str     [V] high rail, low rail
ORSECD   [2193:4249, 2098:2129]                               str     Row bias section for quadrant D
DAC6     5.9998,6.0437                                        str     [V] set value, measured value
DETSECA  [1:2057, 1:2064]                                     str     Detector section for quadrant A
PRRSECB  [2193:4249, 1:1]                                     str     Row prescan section for quadrant B
OFFSET6  2.0,6.0437                                           str     [V] set value, measured value
DAC8     -25.0003,-24.7383                                    str     [V] set value, measured value
DAC13    0.0,0.0297                                           str     [V] set value, measured value
DELAYS   20, 20, 25, 40, 7, 3000, 7, 7, 400, 7                str     [10] Delay settings
TRIMSECA [8:2064, 2:2065]                                     str     Trim section for quadrant A
CAMERA   r1                                                   str     Camera name
CLOCK15  9.9992,2.9993                                        str     [V] high rail, low rail
TRIMSECD [2193:4249, 2130:4193]                               str     Trim section for quadrant D
CLOCK12  9.9992,2.9993                                        str     [V] high rail, low rail
CCDTMING flatdark_lbnl_timing.txt                             str     CCD timing file
CRYOPRES 8.794e-08                                            str     [mb] Cryostat pressure (IP)
DAC15    0.0,0.0148                                           str     [V] set value, measured value
OFFSET2  0.4000000059604645,-8.9301                           str     [V] set value, measured value
CLOCK9   9.9992,2.9993                                        str     [V] high rail, low rail
CLOCK3   -2.0001,3.9999                                       str     [V] high rail, low rail
CCDNAME  CCDSM10R                                             str     CCD name
CLOCK17  9.0,0.9999                                           str     [V] high rail, low rail
DAC11    -25.0003,-24.8867                                    str     [V] set value, measured value
BIASSECD [2129:2192, 2130:4193]                               str     Bias section for quadrant D
ORSECC   [8:2064, 2098:2129]                                  str     Row overscan section for quadrant C
BIASSECB [2129:2192, 2:2065]                                  str     Bias section for quadrant B
CLOCK8   9.9992,2.9993                                        str     [V] high rail, low rail
CLOCK4   9.9999,-3.0003                                       str     [V] high rail, low rail
CCDPREP  purge,clear                                          str     CCD prep actions
CCDSECB  [2058:4114, 1:2064]                                  str     CCD section for quadrant B
PRRSECA  [8:2064, 1:1]                                        str     Row prescan section for quadrant A
DAC2     -9.0002,-8.9301                                      str     [V] set value, measured value
PRESECC  [1:7, 2130:4193]                                     str     Prescan section for quadrant C
CLOCK18  9.0,0.9999                                           str     [V] high rail, low rail
DAC12    0.0,0.0297                                           str     [V] set value, measured value
OFFSET7  2.0,6.028                                            str     [V] set value, measured value
CLOCK13  9.9992,2.9993                                        str     [V] high rail, low rail
DAC9     -25.0003,-24.4563                                    str     [V] set value, measured value
DATASECB [2193:4249, 2:2065]                                  str     Data section for quadrant B
CLOCK2   9.9999,-3.0003                                       str     [V] high rail, low rail
CPUTEMP  58.5937                                              float   [deg C] CCD controller CPU temperature
OFFSET5  2.0,5.9806                                           str     [V] set value, measured value
DAC3     -9.0002,-8.9816                                      str     [V] set value, measured value
CLOCK11  9.9992,2.9993                                        str     [V] high rail, low rail
OFFSET0  0.4000000059604645,-8.8889                           str     [V] set value, measured value
ORSECA   [8:2064, 2066:2097]                                  str     Row overscan section for quadrant A
DETSECC  [1:2057, 2065:4128]                                  str     Detector section for quadrant C
TRIMSECB [2193:4249, 2:2065]                                  str     Trim section for quadrant B
DETECTOR M1-26                                                str     Detector (ccd) identification
DAC1     -9.0002,-8.9301                                      str     [V] set value, measured value
AMPSECA  [1:2057, 1:2064]                                     str     AMP section for quadrant A
CLOCK16  9.9999,3.0                                           str     [V] high rail, low rail
DAC5     5.9998,5.9806                                        str     [V] set value, measured value
CCDSIZE  4194,4256                                            str     CCD size in pixels (rows, columns)
CLOCK1   9.9999,-3.0003                                       str     [V] high rail, low rail
BIASSECC [2065:2128, 2130:4193]                               str     Bias section for quadrant C
SETTINGS detectors.json                                       str     Name of DESI CCD settings file
OFFSET4  2.0,6.028                                            str     [V] set value, measured value
CCDSECC  [1:2057, 2065:4128]                                  str     CCD section for quadrant C
PRRSECC  [8:2064, 4194:4194]                                  str     Row prescan section for quadrant C
DATASECA [8:2064, 2:2065]                                     str     Data section for quadrant A
BLDTIME  0.3514                                               float   [s] Time to build image
CLOCK5   9.9999,-3.0003                                       str     [V] high rail, low rail
DATASECC [8:2064, 2130:4193]                                  str     Data section for quadrant C
PGAGAIN  3                                                    int     Controller gain
PRRSECD  [2193:4249, 4194:4194]                               str     Row prescan section for quadrant D
AMPSECB  [4114:2058, 1:2064]                                  str     AMP section for quadrant B
DETSECB  [2058:4114, 1:2064]                                  str     Detector section for quadrant B
AMPSECC  [1:2057, 4128:2065]                                  str     AMP section for quadrant C
DAC0     -9.0002,-8.8992                                      str     [V] set value, measured value
CCDCFG   M1-26_lbnl_20220104.cfg                              str     CCD configuration file
DATASECD [2193:4249, 2130:4193]                               str     Data section for quadrant D
DAC10    -25.0003,-24.1892                                    str     [V] set value, measured value
OFFSET1  0.4000000059604645,-8.9301                           str     [V] set value, measured value
DETSECD  [2058:4114, 2065:4128]                               str     Detector section for quadrant D
BIASSECA [2065:2128, 2:2065]                                  str     Bias section for quadrant A
DAC7     5.9998,6.0227                                        str     [V] set value, measured value
ORSECB   [2193:4249, 2066:2097]                               str     Row overscan section for quadrant B
CLOCK6   9.9999,-3.0003                                       str     [V] high rail, low rail
DAC17    20.0008,13.8836                                      str     [V] set value, measured value
CCDSECA  [1:2057, 1:2064]                                     str     CCD section for quadrant A
PRESECD  [4250:4256, 2130:4193]                               str     Prescan section for quadrant D
DIGITIME 56.451                                               float   [s] Time to digitize image
PRESECA  [1:7, 2:2065]                                        str     Prescan section for quadrant A
OFFSET3  0.4000000059604645,-8.9816                           str     [V] set value, measured value
DAC4     5.9998,6.028                                         str     [V] set value, measured value
CDSPARMS 400, 400, 8, 2000                                    str     CDS parameters
CRYOTEMP 163.02                                               float   [deg K] Cryostat CCD temperature
REQTIME  1860.0                                               float   [s] Requested exposure time
OBSID    kp4m20220114t110417                                  str     Unique observation identifier
PROCTYPE RAW                                                  str     Data processing level
PRODTYPE image                                                str     Data product type
CHECKSUM onaYrlYVolaVolYV                                     str     HDU checksum updated 2022-01-14T11:15:08
DATASUM  373504067                                            str     data unit checksum updated 2022-01-14T11:15:08
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 4256x4194]

HDU28
-----

EXTNAME = B1

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   4162                                                 int     number of rows in table
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
EXPID    118526                                               int     Exposure number
EXPFRAME 0                                                    int     Frame number
FRAMES   None                                                 Unknown Number of Frames in Archive
TILEID   4403                                                 int     DESI Tile ID
FIBASSGN /data/tiles/SVN_tiles/004/fiberassign-004403.fits.gz str     Fiber assign
FLAVOR   science                                              str     Observation type
SEQUENCE _Split                                               str     OCS Sequence name
PURPOSE  Main Survey                                          str     Purpose of observing night
PROGRAM  DARK                                                 str     Program name
PROPID   2020B-5000                                           str     Proposal ID
OBSERVER Jessica Chellino, Corentin Ravoux                    str     Names of observers
LEAD     Martin Landriau                                      str     Lead observer
INSTRUME DESI                                                 str     Instrument name
OBSERVAT KPNO                                                 str     Observatory name
OBS-LAT  31.96403                                             str     [deg] Observatory latitude
OBS-LONG -111.59989                                           str     [deg] Observatory east longitude
OBS-ELEV 2097.0                                               float   [m] Observatory elevation
TELESCOP KPNO 4.0-m telescope                                 str     Telescope name
CORRCTOR DESI Corrector                                       str     Corrector Identification
NIGHT    20220113                                             int     Observing night
TIMESYS  UTC                                                  str     Time system used for date-obs
DATE-OBS 2022-01-14T11:04:17.770361088                        str     [UTC] Observation data and start tim
TIME-OBS 2022-01-14T11:04:17.770361088                        str     [UTC] Observation start time
MJD-OBS  59593.46131679                                       float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:04:18.378370                           str     Time shutter opened
ST       11:13:28.520000                                      str     Local Sidereal time at observation start (HH:MM
EXPTIME  579.377                                              float   [s] Actual exposure time
REQRA    170.239                                              float   [deg] Requested right ascension (observer input
REQDEC   -7.093                                               float   [deg] Requested declination (observer input)
FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                   str     Telescope focus settings
VCCD     ON                                                   str     True (ON) if CCD voltage is on
VCCDON   2022-01-10T20:55:39.351803                           str     Time when CCD voltage was turned on
VCCDSEC  310749.3                                             float   [s] CCD on time in seconds
TRUSTEMP 12.267                                               float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.675                                               float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                               float   Epoch of observation
MOUNTAZ  176.725567                                           float   [deg] Mount azimuth angle
MOUNTDEC -7.102329                                            float   [deg] Mount declination
MOUNTEL  50.883914                                            float   [deg] Mount elevation angle
MOUNTHA  -2.081118                                            float   [deg] Mount hour angle
SKYDEC   -7.102329                                            float   [deg] Telescope declination (pointing on sky)
SKYRA    170.24163                                            float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.102329                                            float   [deg] Target declination (to TCS)
TARGTRA  170.24163                                            float   [deg] Target right ascension (to TCS)
USEETC   T                                                    bool    ETC data available if true
USESKY   T                                                    bool    DOS Control: use Sky Monitor
USEFOCUS T                                                    bool    DOS Control: use focus
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                              str     Hexapod trim values
USEROTAT T                                                    bool    DOS Control: use rotator
ROTOFFST 138.8                                                float   [arcsec] Rotator offset
ROTENBLD T                                                    bool    Rotator enabled
ROTRATE  0.513                                                float   [arcsec/min] Rotator rate
USEGUIDR T                                                    bool    DOS Control: use guider
USEDONUT T                                                    bool    DOS Control: use donuts
SPECGRPH 1                                                    int     Spectrograph logical name (SP)
SPECID   10                                                   int     Spectrograph serial number (SM)
FEEBOX   lbnl088                                              str     CCD Controller serial number
VESSEL   29                                                   int     Cryostat serial number
FEEVER   v20160312                                            str     CCD Controller version
DETFLVER FAILED: invalid argument for get command             str     CCD Controller detector f
FEEPOWER ON                                                   str     FEE power status
FEEDMASK 2134851391                                           int     FEE dac mask
FEECMASK 1048575                                              int     FEE clk mask
CCDTEMP  850.0                                                float   [deg C] CCD controller CCD temperature
RADESYS  FK5                                                  str     Coordinate reference frame of major/minor axes
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
OFFSET3  -1.5,15.9444                                         str     [V] set value, measured value
CLOCK1   3.9999,-4.0002                                       str     [V] high rail, low rail
OFFSET2  -1.5,15.8002                                         str     [V] set value, measured value
CCDPREP  purge,clear                                          str     CCD prep actions
BIASSECA [2053:2116, 2:2049]                                  str     Bias section for quadrant A
OFFSET7  -1.4700000286102295,-0.021                           str     [V] set value, measured value
OFFSET5  -1.309999942779541,-0.021                            str     [V] set value, measured value
OFFSET6  -1.5199999809265137,-0.0158                          str     [V] set value, measured value
ORSECA   [5:2052, 2050:2081]                                  str     Row overscan section for quadrant A
CLOCK10  3.0,-8.0001                                          str     [V] high rail, low rail
CLOCK9   3.0,-8.0001                                          str     [V] high rail, low rail
PRRSECA  [5:2052, 1:1]                                        str     Row prescan section for quadrant A
DAC10    26.9998,27.0385                                      str     [V] set value, measured value
CCDSIZE  4162,4232                                            str     CCD size in pixels (rows, columns)
DAC15    19.9997,19.8224                                      str     [V] set value, measured value
DATASECD [2181:4228, 2114:4161]                               str     Data section for quadrant D
CLOCK18  3.9999,-4.0002                                       str     [V] high rail, low rail
PRESECC  [1:4, 2114:4161]                                     str     Prescan section for quadrant C
OFFSET4  -1.2599999904632568,-0.0105                          str     [V] set value, measured value
PRRSECB  [2181:4228, 1:1]                                     str     Row prescan section for quadrant B
TRIMSECA [5:2052, 2:2049]                                     str     Trim section for quadrant A
CCDSECC  [1:2048, 2049:4096]                                  str     CCD section for quadrant C
ORSECD   [2181:4228, 2082:2113]                               str     Row bias section for quadrant D
AMPSECD  [4096:2049, 4096:2049]                               str     AMP section for quadrant D
DATASECC [5:2052, 2114:4161]                                  str     Data section for quadrant C
CLOCK12  3.0,-8.0001                                          str     [V] high rail, low rail
CLOCK15  0.0,0.0                                              str     [V] high rail, low rail
CPUTEMP  58.8398                                              float   [deg C] CCD controller CPU temperature
DAC14    0.0,0.78                                             str     [V] set value, measured value
CCDTMING flatdark_sta_timing.txt                              str     CCD timing file
CCDSECB  [2049:4096, 1:2048]                                  str     CCD section for quadrant B
CASETEMP 57.7224                                              float   [deg C] CCD controller case temperature
CCDCFG   CMV_22805_sta_revd_tuned-may2018_20210128.cfg        str     CCD configuration fi
DATASECB [2181:4228, 2:2049]                                  str     Data section for quadrant B
CLOCK2   3.9999,-4.0002                                       str     [V] high rail, low rail
PRRSECC  [5:2052, 4162:4162]                                  str     Row prescan section for quadrant C
DELAYS   13, 13, 25, 25, 8, 3000, 7, 7, 400, 7                str     [10] Delay settings
CLOCK7   6.9999,-2.0001                                       str     [V] high rail, low rail
DAC3     15.9998,15.9341                                      str     [V] set value, measured value
CLOCK16  0.0,0.0                                              str     [V] high rail, low rail
OFFSET0  -1.5,15.9547                                         str     [V] set value, measured value
PRESECB  [4229:4232, 2:2049]                                  str     Prescan section for quadrant B
BIASSECC [2053:2116, 2114:4161]                               str     Bias section for quadrant C
DAC6     0.0,-0.0158                                          str     [V] set value, measured value
TRIMSECB [2181:4228, 2:2049]                                  str     Trim section for quadrant B
SETTINGS detectors_sm_20210128.json                           str     Name of DESI CCD settings file
DAC9     26.9998,27.0236                                      str     [V] set value, measured value
CCDNAME  CCDSM10B                                             str     CCD name
ORSECB   [2181:4228, 2050:2081]                               str     Row overscan section for quadrant B
DAC13    0.0,-5.0232                                          str     [V] set value, measured value
DATASECA [5:2052, 2:2049]                                     str     Data section for quadrant A
BIASSECB [2117:2180, 2:2049]                                  str     Bias section for quadrant B
CRYOTEMP 163.02                                               float   [deg K] Cryostat CCD temperature
CRYOPRES 8.794e-08                                            str     [mb] Cryostat pressure (IP)
BIASSECD [2117:2180, 2114:4161]                               str     Bias section for quadrant D
DAC4     0.0,-0.0053                                          str     [V] set value, measured value
CDSPARMS 350, 350, 8, 1000                                    str     CDS parameters
DAC8     26.9998,27.0088                                      str     [V] set value, measured value
CCDSECD  [2049:4096, 2049:4096]                               str     CCD section for quadrant D
CLOCK6   3.9999,-4.0002                                       str     [V] high rail, low rail
DIGITIME 49.5351                                              float   [s] Time to digitize image
PRESECD  [4229:4232, 2114:4161]                               str     Prescan section for quadrant D
DAC11    26.9998,26.5042                                      str     [V] set value, measured value
DAC5     0.0,-0.0158                                          str     [V] set value, measured value
OFFSET1  -1.5,15.759                                          str     [V] set value, measured value
DAC16    0.0,0.231                                            str     [V] set value, measured value
CLOCK0   3.9999,-4.0002                                       str     [V] high rail, low rail
CCDSECA  [1:2048, 1:2048]                                     str     CCD section for quadrant A
DAC2     15.9998,15.8208                                      str     [V] set value, measured value
AMPSECA  [1:2048, 1:2048]                                     str     AMP section for quadrant A
CLOCK13  3.0,-8.0001                                          str     [V] high rail, low rail
DETSECD  [2049:4096, 2049:4096]                               str     Detector section for quadrant D
CLOCK8   3.0,-8.0001                                          str     [V] high rail, low rail
CLOCK3   6.9999,-2.0001                                       str     [V] high rail, low rail
CLOCK5   3.9999,-4.0002                                       str     [V] high rail, low rail
DETSECC  [1:2048, 2049:4096]                                  str     Detector section for quadrant C
DAC7     0.0,-0.021                                           str     [V] set value, measured value
DETECTOR sn22822                                              str     Detector (ccd) identification
CAMERA   b1                                                   str     Camera name
DAC17    -0.0,0.0976                                          str     [V] set value, measured value
PGAGAIN  5                                                    int     Controller gain
ORSECC   [5:2052, 2082:2113]                                  str     Row overscan section for quadrant C
DAC12    0.0,5.0752                                           str     [V] set value, measured value
DAC1     15.9998,15.7693                                      str     [V] set value, measured value
CLOCK14  3.0,-8.0001                                          str     [V] high rail, low rail
DETSECA  [1:2048, 1:2048]                                     str     Detector section for quadrant A
CLOCK4   3.9999,-4.0002                                       str     [V] high rail, low rail
PRRSECD  [2181:4228, 4162:4162]                               str     Row prescan section for quadrant D
DAC0     15.9998,15.9547                                      str     [V] set value, measured value
AMPSECB  [2049:4096, 2048:1]                                  str     AMP section for quadrant B
BLDTIME  0.354                                                float   [s] Time to build image
TRIMSECC [5:2052, 2114:4161]                                  str     Trim section for quadrant C
DETSECB  [2049:4096, 1:2048]                                  str     Detector section for quadrant B
CLOCK11  0.0,0.0                                              str     [V] high rail, low rail
CLOCK17  3.9999,-4.0002                                       str     [V] high rail, low rail
AMPSECC  [2048:1, 2049:4096]                                  str     AMP section for quadrant C
PRESECA  [1:4, 2:2049]                                        str     Prescan section for quadrant A
TRIMSECD [2181:4228, 2114:4161]                               str     Trim section for quadrant D
REQTIME  1860.0                                               float   [s] Requested exposure time
OBSID    kp4m20220114t110417                                  str     Unique observation identifier
PROCTYPE RAW                                                  str     Data processing level
PRODTYPE image                                                str     Data product type
CHECKSUM 7i3eAf2e9f2eAf2e                                     str     HDU checksum updated 2022-01-14T11:15:08
DATASUM  1626912123                                           str     data unit checksum updated 2022-01-14T11:15:08
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 4232x4162]

HDU29
-----

EXTNAME = Z3

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   4194                                                 int     number of rows in table
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
EXPID    118526                                               int     Exposure number
EXPFRAME 0                                                    int     Frame number
FRAMES   None                                                 Unknown Number of Frames in Archive
TILEID   4403                                                 int     DESI Tile ID
FIBASSGN /data/tiles/SVN_tiles/004/fiberassign-004403.fits.gz str     Fiber assign
FLAVOR   science                                              str     Observation type
SEQUENCE _Split                                               str     OCS Sequence name
PURPOSE  Main Survey                                          str     Purpose of observing night
PROGRAM  DARK                                                 str     Program name
PROPID   2020B-5000                                           str     Proposal ID
OBSERVER Jessica Chellino, Corentin Ravoux                    str     Names of observers
LEAD     Martin Landriau                                      str     Lead observer
INSTRUME DESI                                                 str     Instrument name
OBSERVAT KPNO                                                 str     Observatory name
OBS-LAT  31.96403                                             str     [deg] Observatory latitude
OBS-LONG -111.59989                                           str     [deg] Observatory east longitude
OBS-ELEV 2097.0                                               float   [m] Observatory elevation
TELESCOP KPNO 4.0-m telescope                                 str     Telescope name
CORRCTOR DESI Corrector                                       str     Corrector Identification
NIGHT    20220113                                             int     Observing night
TIMESYS  UTC                                                  str     Time system used for date-obs
DATE-OBS 2022-01-14T11:04:17.802424064                        str     [UTC] Observation data and start tim
TIME-OBS 2022-01-14T11:04:17.802424064                        str     [UTC] Observation start time
MJD-OBS  59593.46131716                                       float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:04:18.589818                           str     Time shutter opened
ST       11:13:28.550000                                      str     Local Sidereal time at observation start (HH:MM
EXPTIME  579.116                                              float   [s] Actual exposure time
REQRA    170.239                                              float   [deg] Requested right ascension (observer input
REQDEC   -7.093                                               float   [deg] Requested declination (observer input)
FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                   str     Telescope focus settings
VCCD     ON                                                   str     True (ON) if CCD voltage is on
VCCDON   2022-01-10T20:55:43.764530                           str     Time when CCD voltage was turned on
VCCDSEC  310751.8                                             float   [s] CCD on time in seconds
TRUSTEMP 12.267                                               float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.675                                               float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                               float   Epoch of observation
MOUNTAZ  176.725567                                           float   [deg] Mount azimuth angle
MOUNTDEC -7.102329                                            float   [deg] Mount declination
MOUNTEL  50.883914                                            float   [deg] Mount elevation angle
MOUNTHA  -2.081118                                            float   [deg] Mount hour angle
SKYDEC   -7.102329                                            float   [deg] Telescope declination (pointing on sky)
SKYRA    170.24163                                            float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.102329                                            float   [deg] Target declination (to TCS)
TARGTRA  170.24163                                            float   [deg] Target right ascension (to TCS)
USEETC   T                                                    bool    ETC data available if true
USESKY   T                                                    bool    DOS Control: use Sky Monitor
USEFOCUS T                                                    bool    DOS Control: use focus
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                              str     Hexapod trim values
USEROTAT T                                                    bool    DOS Control: use rotator
ROTOFFST 138.8                                                float   [arcsec] Rotator offset
ROTENBLD T                                                    bool    Rotator enabled
ROTRATE  0.513                                                float   [arcsec/min] Rotator rate
USEGUIDR T                                                    bool    DOS Control: use guider
USEDONUT T                                                    bool    DOS Control: use donuts
SPECGRPH 3                                                    int     Spectrograph logical name (SP)
SPECID   6                                                    int     Spectrograph serial number (SM)
FEEBOX   lbnl083                                              str     CCD Controller serial number
VESSEL   18                                                   int     Cryostat serial number
FEEVER   v20160312                                            str     CCD Controller version
DETFLVER 20211202                                             str     CCD Controller detector file version
FEEPOWER ON                                                   str     FEE power status
FEEDMASK 2134851391                                           int     FEE dac mask
FEECMASK 1048575                                              int     FEE clk mask
CCDTEMP  -140.2179                                            float   [deg C] CCD controller CCD temperature
RADESYS  FK5                                                  str     Coordinate reference frame of major/minor axes
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
CRYOTEMP 140.034                                              float   [deg K] Cryostat CCD temperature
CLOCK13  9.9992,2.9993                                        str     [V] high rail, low rail
CLOCK2   9.9999,-2.0001                                       str     [V] high rail, low rail
DAC16    39.9961,39.27                                        str     [V] set value, measured value
DAC9     -25.0003,-24.7383                                    str     [V] set value, measured value
DAC13    0.0,0.0                                              str     [V] set value, measured value
TRIMSECC [8:2064, 2130:4193]                                  str     Trim section for quadrant C
CLOCK7   -2.0001,3.9999                                       str     [V] high rail, low rail
DATASECA [8:2064, 2:2065]                                     str     Data section for quadrant A
DAC1     -9.0002,-9.0228                                      str     [V] set value, measured value
CASETEMP 56.1228                                              float   [deg C] CCD controller case temperature
ORSECA   [8:2064, 2066:2097]                                  str     Row overscan section for quadrant A
DETSECC  [1:2057, 2065:4128]                                  str     Detector section for quadrant C
CCDSECB  [2058:4114, 1:2064]                                  str     CCD section for quadrant B
DATASECC [8:2064, 2130:4193]                                  str     Data section for quadrant C
BIASSECB [2129:2192, 2:2065]                                  str     Bias section for quadrant B
CDSPARMS 400, 400, 8, 2000                                    str     CDS parameters
CLOCK4   9.9999,-2.0001                                       str     [V] high rail, low rail
TRIMSECD [2193:4249, 2130:4193]                               str     Trim section for quadrant D
CCDSECA  [1:2057, 1:2064]                                     str     CCD section for quadrant A
BIASSECD [2129:2192, 2130:4193]                               str     Bias section for quadrant D
CLOCK10  9.9992,2.9993                                        str     [V] high rail, low rail
PRESECA  [1:7, 2:2065]                                        str     Prescan section for quadrant A
CCDTMING flatdark_lbnl_timing.txt                             str     CCD timing file
AMPSECB  [4114:2058, 1:2064]                                  str     AMP section for quadrant B
CLOCK0   9.9999,-2.0001                                       str     [V] high rail, low rail
CLOCK5   9.9999,-2.0001                                       str     [V] high rail, low rail
DAC10    -25.0003,-24.946                                     str     [V] set value, measured value
PGAGAIN  3                                                    int     Controller gain
PRRSECA  [8:2064, 1:1]                                        str     Row prescan section for quadrant A
DAC2     -9.0002,-8.9507                                      str     [V] set value, measured value
CCDSECC  [1:2057, 2065:4128]                                  str     CCD section for quadrant C
OFFSET5  2.0,5.9491                                           str     [V] set value, measured value
AMPSECD  [4114:2058, 4128:2065]                               str     AMP section for quadrant D
DAC15    0.0,-0.0297                                          str     [V] set value, measured value
OFFSET6  2.0,6.049                                            str     [V] set value, measured value
PRESECC  [1:7, 2130:4193]                                     str     Prescan section for quadrant C
ORSECC   [8:2064, 2098:2129]                                  str     Row overscan section for quadrant C
CLOCK15  9.9992,2.9993                                        str     [V] high rail, low rail
DAC11    -25.0003,-24.9312                                    str     [V] set value, measured value
DETSECD  [2058:4114, 2065:4128]                               str     Detector section for quadrant D
CLOCK18  9.0,0.9999                                           str     [V] high rail, low rail
AMPSECC  [1:2057, 4128:2065]                                  str     AMP section for quadrant C
PRESECD  [4250:4256, 2130:4193]                               str     Prescan section for quadrant D
DAC14    0.0,-0.0148                                          str     [V] set value, measured value
DAC17    20.0008,12.383                                       str     [V] set value, measured value
CLOCK1   9.9999,-2.0001                                       str     [V] high rail, low rail
DAC4     5.9998,6.0385                                        str     [V] set value, measured value
DAC5     5.9998,5.9491                                        str     [V] set value, measured value
CCDCFG   M1-60_lbnl_20211202.cfg                              str     CCD configuration file
CLOCK14  9.9992,2.9993                                        str     [V] high rail, low rail
CLOCK8   9.9992,2.9993                                        str     [V] high rail, low rail
CCDSIZE  4194,4256                                            str     CCD size in pixels (rows, columns)
CCDSECD  [2058:4114, 2065:4128]                               str     CCD section for quadrant D
OFFSET0  0.4000000059604645,-8.9713                           str     [V] set value, measured value
PRRSECD  [2193:4249, 4194:4194]                               str     Row prescan section for quadrant D
OFFSET1  0.4000000059604645,-9.0125                           str     [V] set value, measured value
TRIMSECB [2193:4249, 2:2065]                                  str     Trim section for quadrant B
OFFSET7  2.0,6.0174                                           str     [V] set value, measured value
DAC7     5.9998,6.0174                                        str     [V] set value, measured value
OFFSET4  2.0,6.0437                                           str     [V] set value, measured value
CLOCK17  9.0,0.9999                                           str     [V] high rail, low rail
DAC6     5.9998,6.049                                         str     [V] set value, measured value
OFFSET3  0.4000000059604645,-8.9713                           str     [V] set value, measured value
DELAYS   20, 20, 25, 40, 7, 3000, 7, 7, 400, 7                str     [10] Delay settings
DAC8     -25.0003,-25.0796                                    str     [V] set value, measured value
ORSECB   [2193:4249, 2066:2097]                               str     Row overscan section for quadrant B
AMPSECA  [1:2057, 1:2064]                                     str     AMP section for quadrant A
BIASSECA [2065:2128, 2:2065]                                  str     Bias section for quadrant A
DATASECB [2193:4249, 2:2065]                                  str     Data section for quadrant B
DATASECD [2193:4249, 2130:4193]                               str     Data section for quadrant D
DIGITIME 56.4527                                              float   [s] Time to digitize image
BIASSECC [2065:2128, 2130:4193]                               str     Bias section for quadrant C
PRRSECB  [2193:4249, 1:1]                                     str     Row prescan section for quadrant B
CRYOPRES 4.300e-08                                            str     [mb] Cryostat pressure (IP)
CLOCK6   9.9999,-2.0001                                       str     [V] high rail, low rail
CLOCK12  9.9992,2.9993                                        str     [V] high rail, low rail
PRESECB  [4250:4256, 2:2065]                                  str     Prescan section for quadrant B
DAC12    0.0,0.0                                              str     [V] set value, measured value
CLOCK11  9.9992,2.9993                                        str     [V] high rail, low rail
CLOCK16  9.9999,3.0                                           str     [V] high rail, low rail
OFFSET2  0.4000000059604645,-8.9404                           str     [V] set value, measured value
CAMERA   z3                                                   str     Camera name
DAC0     -9.0002,-8.9713                                      str     [V] set value, measured value
DETECTOR M1-60                                                str     Detector (ccd) identification
DETSECA  [1:2057, 1:2064]                                     str     Detector section for quadrant A
DETSECB  [2058:4114, 1:2064]                                  str     Detector section for quadrant B
CPUTEMP  56.2558                                              float   [deg C] CCD controller CPU temperature
CCDPREP  purge,clear                                          str     CCD prep actions
PRRSECC  [8:2064, 4194:4194]                                  str     Row prescan section for quadrant C
ORSECD   [2193:4249, 2098:2129]                               str     Row bias section for quadrant D
BLDTIME  0.3519                                               float   [s] Time to build image
CCDNAME  CCDSM6Z                                              str     CCD name
CLOCK3   -2.0001,3.9999                                       str     [V] high rail, low rail
CLOCK9   9.9992,2.9993                                        str     [V] high rail, low rail
DAC3     -9.0002,-8.9713                                      str     [V] set value, measured value
SETTINGS CCDSM6Z                                              str     Name of DESI CCD settings file
TRIMSECA [8:2064, 2:2065]                                     str     Trim section for quadrant A
REQTIME  1860.0                                               float   [s] Requested exposure time
OBSID    kp4m20220114t110417                                  str     Unique observation identifier
PROCTYPE RAW                                                  str     Data processing level
PRODTYPE image                                                str     Data product type
CHECKSUM Qdb8Tda6Qda6Qda6                                     str     HDU checksum updated 2022-01-14T11:15:08
DATASUM  1751351011                                           str     data unit checksum updated 2022-01-14T11:15:08
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 4256x4194]

HDU30
-----

EXTNAME = R3

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   4194                                                 int     number of rows in table
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
EXPID    118526                                               int     Exposure number
EXPFRAME 0                                                    int     Frame number
FRAMES   None                                                 Unknown Number of Frames in Archive
TILEID   4403                                                 int     DESI Tile ID
FIBASSGN /data/tiles/SVN_tiles/004/fiberassign-004403.fits.gz str     Fiber assign
FLAVOR   science                                              str     Observation type
SEQUENCE _Split                                               str     OCS Sequence name
PURPOSE  Main Survey                                          str     Purpose of observing night
PROGRAM  DARK                                                 str     Program name
PROPID   2020B-5000                                           str     Proposal ID
OBSERVER Jessica Chellino, Corentin Ravoux                    str     Names of observers
LEAD     Martin Landriau                                      str     Lead observer
INSTRUME DESI                                                 str     Instrument name
OBSERVAT KPNO                                                 str     Observatory name
OBS-LAT  31.96403                                             str     [deg] Observatory latitude
OBS-LONG -111.59989                                           str     [deg] Observatory east longitude
OBS-ELEV 2097.0                                               float   [m] Observatory elevation
TELESCOP KPNO 4.0-m telescope                                 str     Telescope name
CORRCTOR DESI Corrector                                       str     Corrector Identification
NIGHT    20220113                                             int     Observing night
TIMESYS  UTC                                                  str     Time system used for date-obs
DATE-OBS 2022-01-14T11:04:17.802424064                        str     [UTC] Observation data and start tim
TIME-OBS 2022-01-14T11:04:17.802424064                        str     [UTC] Observation start time
MJD-OBS  59593.46131716                                       float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:04:18.589818                           str     Time shutter opened
ST       11:13:28.550000                                      str     Local Sidereal time at observation start (HH:MM
EXPTIME  579.116                                              float   [s] Actual exposure time
REQRA    170.239                                              float   [deg] Requested right ascension (observer input
REQDEC   -7.093                                               float   [deg] Requested declination (observer input)
FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                   str     Telescope focus settings
VCCD     ON                                                   str     True (ON) if CCD voltage is on
VCCDON   2022-01-10T20:55:36.881677                           str     Time when CCD voltage was turned on
VCCDSEC  310758.1                                             float   [s] CCD on time in seconds
TRUSTEMP 12.267                                               float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.675                                               float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                               float   Epoch of observation
MOUNTAZ  176.725567                                           float   [deg] Mount azimuth angle
MOUNTDEC -7.102329                                            float   [deg] Mount declination
MOUNTEL  50.883914                                            float   [deg] Mount elevation angle
MOUNTHA  -2.081118                                            float   [deg] Mount hour angle
SKYDEC   -7.102329                                            float   [deg] Telescope declination (pointing on sky)
SKYRA    170.24163                                            float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.102329                                            float   [deg] Target declination (to TCS)
TARGTRA  170.24163                                            float   [deg] Target right ascension (to TCS)
USEETC   T                                                    bool    ETC data available if true
USESKY   T                                                    bool    DOS Control: use Sky Monitor
USEFOCUS T                                                    bool    DOS Control: use focus
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                              str     Hexapod trim values
USEROTAT T                                                    bool    DOS Control: use rotator
ROTOFFST 138.8                                                float   [arcsec] Rotator offset
ROTENBLD T                                                    bool    Rotator enabled
ROTRATE  0.513                                                float   [arcsec/min] Rotator rate
USEGUIDR T                                                    bool    DOS Control: use guider
USEDONUT T                                                    bool    DOS Control: use donuts
SPECGRPH 3                                                    int     Spectrograph logical name (SP)
SPECID   6                                                    int     Spectrograph serial number (SM)
FEEBOX   lbnl074                                              str     CCD Controller serial number
VESSEL   11                                                   int     Cryostat serial number
FEEVER   v20160312                                            str     CCD Controller version
DETFLVER FAILED: invalid argument for get command             str     CCD Controller detector f
FEEPOWER ON                                                   str     FEE power status
FEEDMASK 2134851391                                           int     FEE dac mask
FEECMASK 1048575                                              int     FEE clk mask
CCDTEMP  -139.6505                                            float   [deg C] CCD controller CCD temperature
RADESYS  FK5                                                  str     Coordinate reference frame of major/minor axes
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
DAC17    20.0008,14.2862                                      str     [V] set value, measured value
OFFSET6  2.0,6.028                                            str     [V] set value, measured value
AMPSECD  [4114:2058, 4128:2065]                               str     AMP section for quadrant D
PRRSECA  [8:2064, 1:1]                                        str     Row prescan section for quadrant A
PRESECB  [4250:4256, 2:2065]                                  str     Prescan section for quadrant B
CLOCK8   9.9992,2.9993                                        str     [V] high rail, low rail
DETSECC  [1:2057, 2065:4128]                                  str     Detector section for quadrant C
DAC8     -25.0003,-25.0202                                    str     [V] set value, measured value
CLOCK6   9.9999,0.0                                           str     [V] high rail, low rail
CLOCK16  9.9999,3.0                                           str     [V] high rail, low rail
DAC5     5.9998,6.028                                         str     [V] set value, measured value
DAC0     -9.0002,-8.9095                                      str     [V] set value, measured value
AMPSECA  [1:2057, 1:2064]                                     str     AMP section for quadrant A
CCDTMING flatdark_lbnl_timing.txt                             str     CCD timing file
CRYOPRES 8.521e-08                                            str     [mb] Cryostat pressure (IP)
DATASECA [8:2064, 2:2065]                                     str     Data section for quadrant A
CLOCK0   9.9999,0.0                                           str     [V] high rail, low rail
TRIMSECA [8:2064, 2:2065]                                     str     Trim section for quadrant A
DAC1     -9.0002,-8.8065                                      str     [V] set value, measured value
CCDNAME  CCDSM6R                                              str     CCD name
CDSPARMS 400, 400, 8, 2000                                    str     CDS parameters
OFFSET0  0.4000000059604645,-8.9095                           str     [V] set value, measured value
TRIMSECC [8:2064, 2130:4193]                                  str     Trim section for quadrant C
CLOCK17  9.0,0.9999                                           str     [V] high rail, low rail
BIASSECA [2065:2128, 2:2065]                                  str     Bias section for quadrant A
CLOCK11  9.9992,2.9993                                        str     [V] high rail, low rail
ORSECD   [2193:4249, 2098:2129]                               str     Row bias section for quadrant D
BIASSECD [2129:2192, 2130:4193]                               str     Bias section for quadrant D
CLOCK3   -2.0001,3.9999                                       str     [V] high rail, low rail
OFFSET3  0.4000000059604645,-10.3824                          str     [V] set value, measured value
CLOCK10  9.9992,2.9993                                        str     [V] high rail, low rail
DAC11    -25.0003,-24.7086                                    str     [V] set value, measured value
PRESECC  [1:7, 2130:4193]                                     str     Prescan section for quadrant C
AMPSECB  [4114:2058, 1:2064]                                  str     AMP section for quadrant B
DAC12    0.0,0.0148                                           str     [V] set value, measured value
PRESECA  [1:7, 2:2065]                                        str     Prescan section for quadrant A
CLOCK9   9.9992,2.9993                                        str     [V] high rail, low rail
DELAYS   20, 20, 25, 30, 7, 3000, 7, 7, 400, 7                str     [10] Delay settings
CLOCK15  9.9992,2.9993                                        str     [V] high rail, low rail
DAC3     -10.5005,-10.3824                                    str     [V] set value, measured value
DIGITIME 55.9267                                              float   [s] Time to digitize image
CCDSECC  [1:2057, 2065:4128]                                  str     CCD section for quadrant C
PRRSECD  [2193:4249, 4194:4194]                               str     Row prescan section for quadrant D
DAC6     5.9998,6.028                                         str     [V] set value, measured value
CLOCK1   9.9999,0.0                                           str     [V] high rail, low rail
CCDSECA  [1:2057, 1:2064]                                     str     CCD section for quadrant A
CCDPREP  purge,clear                                          str     CCD prep actions
CLOCK13  9.9992,2.9993                                        str     [V] high rail, low rail
DAC4     5.9998,6.028                                         str     [V] set value, measured value
CLOCK18  9.0,0.9999                                           str     [V] high rail, low rail
BLDTIME  0.3528                                               float   [s] Time to build image
PGAGAIN  3                                                    int     Controller gain
DETSECA  [1:2057, 1:2064]                                     str     Detector section for quadrant A
DAC7     6.4999,6.4856                                        str     [V] set value, measured value
DAC14    0.0,0.0148                                           str     [V] set value, measured value
DETSECD  [2058:4114, 2065:4128]                               str     Detector section for quadrant D
CPUTEMP  56.2558                                              float   [deg C] CCD controller CPU temperature
CLOCK14  9.9992,2.9993                                        str     [V] high rail, low rail
DAC15    0.0,0.0297                                           str     [V] set value, measured value
CLOCK5   9.9999,0.0                                           str     [V] high rail, low rail
OFFSET4  2.0,6.028                                            str     [V] set value, measured value
PRESECD  [4250:4256, 2130:4193]                               str     Prescan section for quadrant D
DAC16    48.0,46.7082                                         str     [V] set value, measured value
BIASSECB [2129:2192, 2:2065]                                  str     Bias section for quadrant B
ORSECA   [8:2064, 2066:2097]                                  str     Row overscan section for quadrant A
SETTINGS detectors_sm_20210128.json                           str     Name of DESI CCD settings file
CCDCFG   M1-50_lbnl_20210128.cfg                              str     CCD configuration file
OFFSET2  0.4000000059604645,-8.9713                           str     [V] set value, measured value
CLOCK2   9.9999,0.0                                           str     [V] high rail, low rail
ORSECB   [2193:4249, 2066:2097]                               str     Row overscan section for quadrant B
DAC9     -25.0003,-24.6789                                    str     [V] set value, measured value
CLOCK7   -2.0001,3.9999                                       str     [V] high rail, low rail
CASETEMP 56.4919                                              float   [deg C] CCD controller case temperature
TRIMSECD [2193:4249, 2130:4193]                               str     Trim section for quadrant D
DETSECB  [2058:4114, 1:2064]                                  str     Detector section for quadrant B
CCDSECD  [2058:4114, 2065:4128]                               str     CCD section for quadrant D
ORSECC   [8:2064, 2098:2129]                                  str     Row overscan section for quadrant C
CLOCK12  9.9992,2.9993                                        str     [V] high rail, low rail
OFFSET1  0.4000000059604645,-8.8065                           str     [V] set value, measured value
BIASSECC [2065:2128, 2130:4193]                               str     Bias section for quadrant C
CLOCK4   9.9999,0.0                                           str     [V] high rail, low rail
CAMERA   r3                                                   str     Camera name
CRYOTEMP 163.044                                              float   [deg K] Cryostat CCD temperature
DATASECC [8:2064, 2130:4193]                                  str     Data section for quadrant C
OFFSET5  2.0,6.0227                                           str     [V] set value, measured value
DETECTOR M1-50                                                str     Detector (ccd) identification
OFFSET7  2.0,6.4908                                           str     [V] set value, measured value
PRRSECC  [8:2064, 4194:4194]                                  str     Row prescan section for quadrant C
DAC2     -9.0002,-8.9713                                      str     [V] set value, measured value
TRIMSECB [2193:4249, 2:2065]                                  str     Trim section for quadrant B
DAC13    0.0,0.0                                              str     [V] set value, measured value
PRRSECB  [2193:4249, 1:1]                                     str     Row prescan section for quadrant B
CCDSECB  [2058:4114, 1:2064]                                  str     CCD section for quadrant B
DATASECD [2193:4249, 2130:4193]                               str     Data section for quadrant D
CCDSIZE  4194,4256                                            str     CCD size in pixels (rows, columns)
DATASECB [2193:4249, 2:2065]                                  str     Data section for quadrant B
DAC10    -25.0003,-24.9906                                    str     [V] set value, measured value
AMPSECC  [1:2057, 4128:2065]                                  str     AMP section for quadrant C
REQTIME  1860.0                                               float   [s] Requested exposure time
OBSID    kp4m20220114t110417                                  str     Unique observation identifier
PROCTYPE RAW                                                  str     Data processing level
PRODTYPE image                                                str     Data product type
CHECKSUM 6jHF7hH96hHC6hH9                                     str     HDU checksum updated 2022-01-14T11:15:08
DATASUM  157674405                                            str     data unit checksum updated 2022-01-14T11:15:08
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 4256x4194]

HDU31
-----

EXTNAME = B3

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   4162                                                 int     number of rows in table
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
EXPID    118526                                               int     Exposure number
EXPFRAME 0                                                    int     Frame number
FRAMES   None                                                 Unknown Number of Frames in Archive
TILEID   4403                                                 int     DESI Tile ID
FIBASSGN /data/tiles/SVN_tiles/004/fiberassign-004403.fits.gz str     Fiber assign
FLAVOR   science                                              str     Observation type
SEQUENCE _Split                                               str     OCS Sequence name
PURPOSE  Main Survey                                          str     Purpose of observing night
PROGRAM  DARK                                                 str     Program name
PROPID   2020B-5000                                           str     Proposal ID
OBSERVER Jessica Chellino, Corentin Ravoux                    str     Names of observers
LEAD     Martin Landriau                                      str     Lead observer
INSTRUME DESI                                                 str     Instrument name
OBSERVAT KPNO                                                 str     Observatory name
OBS-LAT  31.96403                                             str     [deg] Observatory latitude
OBS-LONG -111.59989                                           str     [deg] Observatory east longitude
OBS-ELEV 2097.0                                               float   [m] Observatory elevation
TELESCOP KPNO 4.0-m telescope                                 str     Telescope name
CORRCTOR DESI Corrector                                       str     Corrector Identification
NIGHT    20220113                                             int     Observing night
TIMESYS  UTC                                                  str     Time system used for date-obs
DATE-OBS 2022-01-14T11:04:17.802424064                        str     [UTC] Observation data and start tim
TIME-OBS 2022-01-14T11:04:17.802424064                        str     [UTC] Observation start time
MJD-OBS  59593.46131716                                       float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:04:18.589818                           str     Time shutter opened
ST       11:13:28.550000                                      str     Local Sidereal time at observation start (HH:MM
EXPTIME  579.116                                              float   [s] Actual exposure time
REQRA    170.239                                              float   [deg] Requested right ascension (observer input
REQDEC   -7.093                                               float   [deg] Requested declination (observer input)
FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                   str     Telescope focus settings
VCCD     ON                                                   str     True (ON) if CCD voltage is on
VCCDON   2022-01-10T20:55:39.332962                           str     Time when CCD voltage was turned on
VCCDSEC  310754.5                                             float   [s] CCD on time in seconds
TRUSTEMP 12.267                                               float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.675                                               float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                               float   Epoch of observation
MOUNTAZ  176.725567                                           float   [deg] Mount azimuth angle
MOUNTDEC -7.102329                                            float   [deg] Mount declination
MOUNTEL  50.883914                                            float   [deg] Mount elevation angle
MOUNTHA  -2.081118                                            float   [deg] Mount hour angle
SKYDEC   -7.102329                                            float   [deg] Telescope declination (pointing on sky)
SKYRA    170.24163                                            float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.102329                                            float   [deg] Target declination (to TCS)
TARGTRA  170.24163                                            float   [deg] Target right ascension (to TCS)
USEETC   T                                                    bool    ETC data available if true
USESKY   T                                                    bool    DOS Control: use Sky Monitor
USEFOCUS T                                                    bool    DOS Control: use focus
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                              str     Hexapod trim values
USEROTAT T                                                    bool    DOS Control: use rotator
ROTOFFST 138.8                                                float   [arcsec] Rotator offset
ROTENBLD T                                                    bool    Rotator enabled
ROTRATE  0.513                                                float   [arcsec/min] Rotator rate
USEGUIDR T                                                    bool    DOS Control: use guider
USEDONUT T                                                    bool    DOS Control: use donuts
SPECGRPH 3                                                    int     Spectrograph logical name (SP)
SPECID   6                                                    int     Spectrograph serial number (SM)
FEEBOX   lbnl079                                              str     CCD Controller serial number
VESSEL   16                                                   int     Cryostat serial number
FEEVER   v20160312                                            str     CCD Controller version
DETFLVER FAILED: invalid argument for get command             str     CCD Controller detector f
FEEPOWER ON                                                   str     FEE power status
FEEDMASK 2134851391                                           int     FEE dac mask
FEECMASK 1048575                                              int     FEE clk mask
CCDTEMP  850.0                                                float   [deg C] CCD controller CCD temperature
RADESYS  FK5                                                  str     Coordinate reference frame of major/minor axes
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
OFFSET5  -1.100000023841858,-0.0053                           str     [V] set value, measured value
PRESECB  [4229:4232, 2:2049]                                  str     Prescan section for quadrant B
CCDSECA  [1:2048, 1:2048]                                     str     CCD section for quadrant A
CCDSIZE  4162,4232                                            str     CCD size in pixels (rows, columns)
DETSECC  [1:2048, 2049:4096]                                  str     Detector section for quadrant C
DAC0     15.9998,15.9032                                      str     [V] set value, measured value
DATASECC [5:2052, 2114:4161]                                  str     Data section for quadrant C
BIASSECD [2117:2180, 2114:4161]                               str     Bias section for quadrant D
DAC17    -0.0,0.0366                                          str     [V] set value, measured value
ORSECC   [5:2052, 2082:2113]                                  str     Row overscan section for quadrant C
PRRSECC  [5:2052, 4162:4162]                                  str     Row prescan section for quadrant C
CLOCK6   3.9999,-4.0002                                       str     [V] high rail, low rail
BIASSECB [2117:2180, 2:2049]                                  str     Bias section for quadrant B
PRRSECA  [5:2052, 1:1]                                        str     Row prescan section for quadrant A
DATASECB [2181:4228, 2:2049]                                  str     Data section for quadrant B
SETTINGS detectors_sm_20210128.json                           str     Name of DESI CCD settings file
OFFSET1  -1.5,15.8105                                         str     [V] set value, measured value
PRESECC  [1:4, 2114:4161]                                     str     Prescan section for quadrant C
DELAYS   13, 13, 25, 25, 8, 3000, 7, 7, 400, 7                str     [10] Delay settings
DAC10    26.9998,27.0533                                      str     [V] set value, measured value
DAC2     15.9998,16.0062                                      str     [V] set value, measured value
DAC7     0.0,-0.0105                                          str     [V] set value, measured value
PGAGAIN  5                                                    int     Controller gain
CCDSECD  [2049:4096, 2049:4096]                               str     CCD section for quadrant D
DATASECA [5:2052, 2:2049]                                     str     Data section for quadrant A
CLOCK2   3.9999,-4.0002                                       str     [V] high rail, low rail
CCDSECB  [2049:4096, 1:2048]                                  str     CCD section for quadrant B
CCDNAME  CCDSM6B                                              str     CCD name
CCDTMING flatdark_sta_timing.txt                              str     CCD timing file
CLOCK17  3.9999,-4.0002                                       str     [V] high rail, low rail
OFFSET6  -1.100000023841858,0.0                               str     [V] set value, measured value
AMPSECB  [2049:4096, 2048:1]                                  str     AMP section for quadrant B
TRIMSECB [2181:4228, 2:2049]                                  str     Trim section for quadrant B
CASETEMP 54.6462                                              float   [deg C] CCD controller case temperature
CLOCK7   6.9999,-2.0001                                       str     [V] high rail, low rail
CRYOPRES 8.521e-08                                            str     [mb] Cryostat pressure (IP)
OFFSET7  -1.100000023841858,-0.0105                           str     [V] set value, measured value
DAC4     0.0,-0.0105                                          str     [V] set value, measured value
PRRSECD  [2181:4228, 4162:4162]                               str     Row prescan section for quadrant D
TRIMSECD [2181:4228, 2114:4161]                               str     Trim section for quadrant D
DAC13    -5.0006,-5.0336                                      str     [V] set value, measured value
CLOCK14  3.0,-7.0002                                          str     [V] high rail, low rail
CAMERA   b3                                                   str     Camera name
AMPSECC  [2048:1, 2049:4096]                                  str     AMP section for quadrant C
DETSECD  [2049:4096, 2049:4096]                               str     Detector section for quadrant D
DAC14    0.0,0.7176                                           str     [V] set value, measured value
AMPSECD  [4096:2049, 4096:2049]                               str     AMP section for quadrant D
CLOCK0   3.9999,-4.0002                                       str     [V] high rail, low rail
CLOCK13  3.0,-7.0002                                          str     [V] high rail, low rail
CLOCK10  3.0,-7.0002                                          str     [V] high rail, low rail
DIGITIME 54.7803                                              float   [s] Time to digitize image
DETSECA  [1:2048, 1:2048]                                     str     Detector section for quadrant A
TRIMSECC [5:2052, 2114:4161]                                  str     Trim section for quadrant C
ORSECA   [5:2052, 2050:2081]                                  str     Row overscan section for quadrant A
CDSPARMS 400, 400, 8, 1000                                    str     CDS parameters
ORSECD   [2181:4228, 2082:2113]                               str     Row bias section for quadrant D
ORSECB   [2181:4228, 2050:2081]                               str     Row overscan section for quadrant B
DATASECD [2181:4228, 2114:4161]                               str     Data section for quadrant D
DETSECB  [2049:4096, 1:2048]                                  str     Detector section for quadrant B
PRESECA  [1:4, 2:2049]                                        str     Prescan section for quadrant A
DAC5     0.0,-0.0105                                          str     [V] set value, measured value
AMPSECA  [1:2048, 1:2048]                                     str     AMP section for quadrant A
DAC12    4.9997,5.096                                         str     [V] set value, measured value
CLOCK3   6.9999,-2.0001                                       str     [V] high rail, low rail
CLOCK4   3.9999,-4.0002                                       str     [V] high rail, low rail
CLOCK15  0.0,0.0                                              str     [V] high rail, low rail
DETECTOR sn22804                                              str     Detector (ccd) identification
BIASSECC [2053:2116, 2114:4161]                               str     Bias section for quadrant C
DAC11    26.9998,27.0236                                      str     [V] set value, measured value
BIASSECA [2053:2116, 2:2049]                                  str     Bias section for quadrant A
CLOCK8   3.0,-7.0002                                          str     [V] high rail, low rail
PRESECD  [4229:4232, 2114:4161]                               str     Prescan section for quadrant D
DAC1     15.9998,15.8002                                      str     [V] set value, measured value
PRRSECB  [2181:4228, 1:1]                                     str     Row prescan section for quadrant B
OFFSET2  -1.5,15.9959                                         str     [V] set value, measured value
CLOCK1   3.9999,-4.0002                                       str     [V] high rail, low rail
DAC9     26.9998,26.8752                                      str     [V] set value, measured value
TRIMSECA [5:2052, 2:2049]                                     str     Trim section for quadrant A
DAC3     15.9998,15.9547                                      str     [V] set value, measured value
CRYOTEMP 163.044                                              float   [deg K] Cryostat CCD temperature
CLOCK12  3.0,-7.0002                                          str     [V] high rail, low rail
CCDCFG   default_sta_20210128.cfg                             str     CCD configuration file
DAC15    19.9997,19.9264                                      str     [V] set value, measured value
CPUTEMP  54.4101                                              float   [deg C] CCD controller CPU temperature
OFFSET4  -1.100000023841858,-0.0158                           str     [V] set value, measured value
CCDPREP  purge,clear                                          str     CCD prep actions
CLOCK18  3.9999,-4.0002                                       str     [V] high rail, low rail
OFFSET0  -1.5,15.9135                                         str     [V] set value, measured value
CCDSECC  [1:2048, 2049:4096]                                  str     CCD section for quadrant C
BLDTIME  0.3518                                               float   [s] Time to build image
OFFSET3  -1.5,15.9444                                         str     [V] set value, measured value
DAC6     0.0,-0.0053                                          str     [V] set value, measured value
CLOCK9   3.0,-7.0002                                          str     [V] high rail, low rail
CLOCK11  0.0,0.0                                              str     [V] high rail, low rail
CLOCK5   3.9999,-4.0002                                       str     [V] high rail, low rail
DAC16    0.0,64.449                                           str     [V] set value, measured value
DAC8     26.9998,26.9791                                      str     [V] set value, measured value
CLOCK16  0.0,0.0                                              str     [V] high rail, low rail
REQTIME  1860.0                                               float   [s] Requested exposure time
OBSID    kp4m20220114t110417                                  str     Unique observation identifier
PROCTYPE RAW                                                  str     Data processing level
PRODTYPE image                                                str     Data product type
CHECKSUM odYFrbVFobVFobVF                                     str     HDU checksum updated 2022-01-14T11:15:08
DATASUM  475364108                                            str     data unit checksum updated 2022-01-14T11:15:08
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 4232x4162]

HDU32
-----

EXTNAME = SPECTCONS

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============================================================================================================ ======= ===============================================
KEY      Example Value                                                                                                Type    Comment
======== ============================================================================================================ ======= ===============================================
NAXIS1   352                                                                                                          int     width of table in bytes
NAXIS2   10                                                                                                           int     number of rows in table
EXPID    118526                                                                                                       int     Exposure number
EXPFRAME 0                                                                                                            int     Frame number
FRAMES   None                                                                                                         Unknown Number of Frames in Archive
TILEID   4403                                                                                                         int     DESI Tile ID
FIBASSGN /data/tiles/SVN_tiles/004/fiberassign-004403.fits.gz                                                         str     Fiber assign
FLAVOR   science                                                                                                      str     Observation type
SEQUENCE _Split                                                                                                       str     OCS Sequence name
PURPOSE  Main Survey                                                                                                  str     Purpose of observing night
PROGRAM  DARK                                                                                                         str     Program name
PROPID   2020B-5000                                                                                                   str     Proposal ID
OBSERVER Jessica Chellino, Corentin Ravoux                                                                            str     Names of observers
LEAD     Martin Landriau                                                                                              str     Lead observer
INSTRUME DESI                                                                                                         str     Instrument name
OBSERVAT KPNO                                                                                                         str     Observatory name
OBS-LAT  31.96403                                                                                                     str     [deg] Observatory latitude
OBS-LONG -111.59989                                                                                                   str     [deg] Observatory east longitude
OBS-ELEV 2097.0                                                                                                       float   [m] Observatory elevation
TELESCOP KPNO 4.0-m telescope                                                                                         str     Telescope name
CORRCTOR DESI Corrector                                                                                               str     Corrector Identification
NIGHT    20220113                                                                                                     int     Observing night
TIMESYS  UTC                                                                                                          str     Time system used for date-obs
REQRA    170.239                                                                                                      float   [deg] Requested right ascension (observer input
REQDEC   -7.093                                                                                                       float   [deg] Requested declination (observer input)
FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                                                                           str     Telescope focus settings
TRUSTEMP 12.267                                                                                                       float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.675                                                                                                       float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                                                                                       float   Epoch of observation
MOUNTAZ  176.725567                                                                                                   float   [deg] Mount azimuth angle
MOUNTDEC -7.102329                                                                                                    float   [deg] Mount declination
MOUNTEL  50.883914                                                                                                    float   [deg] Mount elevation angle
MOUNTHA  -2.081118                                                                                                    float   [deg] Mount hour angle
SKYDEC   -7.102329                                                                                                    float   [deg] Telescope declination (pointing on sky)
SKYRA    170.24163                                                                                                    float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.102329                                                                                                    float   [deg] Target declination (to TCS)
TARGTRA  170.24163                                                                                                    float   [deg] Target right ascension (to TCS)
USEETC   T                                                                                                            bool    ETC data available if true
USESKY   T                                                                                                            bool    DOS Control: use Sky Monitor
USEFOCUS T                                                                                                            bool    DOS Control: use focus
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                                                                                      str     Hexapod trim values
USEROTAT T                                                                                                            bool    DOS Control: use rotator
ROTOFFST 138.8                                                                                                        float   [arcsec] Rotator offset
ROTENBLD T                                                                                                            bool    Rotator enabled
ROTRATE  0.513                                                                                                        float   [arcsec/min] Rotator rate
USEGUIDR T                                                                                                            bool    DOS Control: use guider
USEDONUT T                                                                                                            bool    DOS Control: use donuts
SPCGRPHS SP4, SP9, SP8, SP2, SP0, SP5, SP7, SP6, SP1, SP3                                                             str     Participating spe
DEVICES  SPECTCON4, SPECTCON9, SPECTCON8, SPECTCON2, SPECTCON0, SPECTCON5, SPECTCON7, SPECTCON6, SPECTCON1, SPECTCON3 str     Participating devices (spectro controller)
RADESYS  FK5                                                                                                          str     Coordinate reference frame of major/minor axes
DOSVER   trunk                                                                                                        str     DOS software version
OCSVER   1.2                                                                                                          float   OCS software version
CONSTVER DESI:CURRENT                                                                                                 str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini                                                             str     DOS Configuration
REQTIME  1860.0                                                                                                       float   [s] Requested exposure time
OBSID    kp4m20220114t110417                                                                                          str     Unique observation identifier
PROCTYPE RAW                                                                                                          str     Data processing level
PRODTYPE image                                                                                                        str     Data product type
CHECKSUM 0YhA1VZ30VfA0VZ3                                                                                             str     HDU checksum updated 2022-01-14T11:15:09
DATASUM  2915472531                                                                                                   str     data unit checksum updated 2022-01-14T11:15:09
======== ============================================================================================================ ======= ===============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

*Add notes and examples here.  You can also create links to example files.*
