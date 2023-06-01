=========
fvc-EXPID
=========

:Summary: Fiber View Camera data
:Naming Convention: ``fvc-EXPID.fits.fz``, where EXPID is the zero-padded
    8-digit exposure ID.
:Regex: ``fvc-[0-9]{8}\.fits(\.fz)?``
:File Type: FITS, 30 MB

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_  FVC     IMAGE    TODO: description needed
HDU1_  F0000   BINTABLE TODO: description needed
HDU2_  C0000   BINTABLE TODO: description needed
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = FVC

TODO: description needed

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ===================================================================== ======= ===============================================
    KEY      Example Value                                                         Type    Comment
    ======== ===================================================================== ======= ===============================================
    NAXIS1   1                                                                     int     length of data axis 1
    MODULE   FVC                                                                   str     Image Sources/Component
    EXPID    118526                                                                int     Exposure number
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
    DATE-OBS None                                                                  Unknown [UTC] Observation data and start time
    MJD-OBS  None                                                                  Unknown Modified Julian Date of observation
    STARTADJ 2022-01-14T11:03:22.140652                                            str     Time sequence starts adjusting the inst
    OPENSHUT 2022-01-14T11:04:18.577390                                            str     Time shutter opened
    CAMSHUT  open                                                                  str     Shutter status during observation
    ST       None                                                                  Unknown Local Sidereal time at observation start (HH:MM
    EXPTIME  None                                                                  Unknown [s] Actual exposure time
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
    FOCUS    946.7,-231.6,-83.4,-18.3,9.9,138.8                                    str     Telescope focus settings
    VCCD     ON                                                                    str     True (ON) if CCD voltage is on
    TRUSTEMP 12.2                                                                  float   [deg] Average Telescope truss temperature (only
    PMIRTEMP 11.65                                                                 float   [deg] Average primary mirror temperature (nit,e
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
    MOUNTAZ  177.063681                                                            float   [deg] Mount azimuth angle
    MOUNTDEC -7.10233                                                              float   [deg] Mount declination
    MOUNTEL  50.893802                                                             float   [deg] Mount elevation angle
    MOUNTHA  -1.865946                                                             float   [deg] Mount hour angle
    INCTRL   T                                                                     bool    DESI in control
    INPOS    T                                                                     bool    Mount in position
    MNTOFFD  75.86                                                                 float   [arcsec] Mount offset (dec)
    MNTOFFR  -31.1                                                                 float   [arcsec] Mount offset (RA)
    PARALLAC -2.510103                                                             float   [deg] Parallactic angle
    SKYDEC   -7.10233                                                              float   [deg] Telescope declination (pointing on sky)
    SKYRA    170.241629                                                            float   [deg] Telescope right ascension (pointing on sk
    TARGTDEC -7.10233                                                              float   [deg] Target declination (to TCS)
    TARGTRA  170.241629                                                            float   [deg] Target right ascension (to TCS)
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
    SEEING   None                                                                  Unknown [arcsec] ETC/PM seeing
    TRANSPAR None                                                                  Unknown ETC/PM transparency
    SKYLEVEL 4.415                                                                 float   [unit?] PM/ETC sky level
    PMSEEING None                                                                  Unknown [arcsec] PlateMaker GFAPROC seeing
    PMTRANSP None                                                                  Unknown [%] PlateMaker GFAPROC transparency
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
    EXCLUDED                                                                       str     Components excluded from this exposure
    DOSVER   trunk                                                                 str     DOS software version
    OCSVER   1.2                                                                   float   OCS software version
    PMVER    desi-138368                                                           str     PlateMaker/Dervish version
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
    CHECKSUM KdJcMZJbKdJbKZJb                                                      str     HDU checksum updated 2022-01-14T11:04:35
    DATASUM  1072693248                                                            str     data unit checksum updated 2022-01-14T11:04:35
    ======== ===================================================================== ======= ===============================================

Data: FITS image [float64, 1]

HDU1
----

EXTNAME = F0000

TODO: description needed

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ==================== ===== ==============================================
    KEY      Example Value        Type  Comment
    ======== ==================== ===== ==============================================
    NAXIS1   8                    int   width of table in bytes
    NAXIS2   6000                 int   number of rows in table
    BZERO    32768                int   offset data range to that of unsigned short
    BSCALE   1                    int   default scaling factor
    EXPID    118526.0             float
    EXPTIME  2.0                  float
    RDTIME   4.26886796951294     float
    DRKEXP   0                    int
    DRKFLAG  0                    int
    IDLEFLAG 0                    int
    SIMFLAG  0                    int
    SIMFIB   0                    int
    CCDTEMP  -10.0                float
    BASETMP  18.0                 float
    TEMPSET  -10.0                float
    COOLPOW  48.0                 float
    PIXSZX   6.00000021222513e-06 float
    PIXSZY   6.00000021222513e-06 float
    CCDX1    0                    int
    CCDX2    8304                 int
    CCDY1    0                    int
    CCDY2    6220                 int
    VISX1    64                   int
    VISX2    8240                 int
    VISY1    45                   int
    VISY2    6177                 int
    SUBX1    1152                 int
    SUBX2    7151                 int
    SUBY1    111                  int
    SUBY2    6110                 int
    HBIN     0                    int
    VBIN     0                    int
    OBSNUM   118526               int
    OBSFRM   0                    int
    HDREV    256                  int
    FWREV    516                  int
    DATE     2022-01-14T11:04:12  str
    CHECKSUM 97c4H4b494b4E4b4     str   HDU checksum updated 2022-01-14T11:04:36
    DATASUM  2941763729           str   data unit checksum updated 2022-01-14T11:04:36
    ======== ==================== ===== ==============================================

Data: FITS image [int16 (compressed), 6000x6000]

HDU2
----

EXTNAME = C0000

TODO: description needed

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   48               int  width of table in bytes
    NAXIS2   5439             int  number of rows in table
    EXPID    118526           int
    MODULE   CENTROIDS        str
    CHECKSUM 93Ad908Z90Ad907Z str  HDU checksum updated 2022-01-14T11:04:37
    DATASUM  1135191656       str  data unit checksum updated 2022-01-14T11:04:37
    ======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

========= ======= ===== ===================
Name      Type    Units Description
========= ======= ===== ===================
x         float64       TODO: description needed
y         float64       TODO: description needed
mag       float64       TODO: description needed
fwhm      float64       TODO: description needed
flags     int64         TODO: description needed
device_id int64         TODO: description needed
========= ======= ===== ===================
