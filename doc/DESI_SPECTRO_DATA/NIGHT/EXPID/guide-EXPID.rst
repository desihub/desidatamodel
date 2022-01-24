===========
guide-EXPID
===========

:Summary: Datamodel for the guider GFA raw data
:Naming Convention: ``guide-EXPID.fits.fz``, where EXPID is the zero-padded
    8-digit exposure ID.
:Regex: ``guide-[0-9]{8}\.fits\.fz``
:File Type: FITS, 732 MB


Contents
========

====== ======== ================ ===================
Number EXTNAME  Type             Contents
====== ======== ================ ===================
HDU00_ GUIDER   Empty HDU        Header keywords only
HDU01_ PMGSTARS BINTABLE         PlateMaker star table
HDU02_ GUIDE5   Compressed IMAGE GUIDE5 image cube
HDU03_ GUIDE5T  BINTABLE         GUIDE5 image cube metadata
HDU04_ GUIDE3   Compressed IMAGE GUIDE3 image cube
HDU05_ GUIDE3T  BINTABLE         GUIDE3 image cube metadata
HDU06_ GUIDE2   Compressed IMAGE GUIDE2 image cube
HDU07_ GUIDE2T  BINTABLE         GUIDE2 image cube metadata
HDU08_ GUIDE7   Compressed IMAGE GUIDE7 image cube
HDU09_ GUIDE7T  BINTABLE         GUIDE7 image cube metadata
HDU10_ GUIDE8   Compressed IMAGE GUIDE8 image cube
HDU11_ GUIDE8T  BINTABLE         GUIDE8 image cube metadata
HDU12_ GUIDE0   Compressed IMAGE GUIDE0 image cube
HDU13_ GUIDE0T  BINTABLE         GUIDE0 image cube metadata
====== ======== ================ ===================

The GUIDEn data will be 3D[nframes, ny, nx] such that
``data[i]`` is the 2D GFA frame number ``i``.  Row ``i`` of the
GUIDEnT table will contain the metadata about that frame, for example the
``DATE-OBS`` and ``EXPTIME``. The image cubes include the overscan and prescan;
``nx`` is 2248 and `ny` is 1032. The active image area is 2048 by 1032
pixels once overscan and prescan have been removed.

Note that other than the blank data primary HDU, the order of the other
HDUs is arbitrary and some GUIDEn(T) HDUs may even be missing.  The
nominal set (0,2,3,5,7,8) is the plan for full DESI, but particularly during
commissioning other subsets will appear in the data. Also note
that the acquisition image is frame ``i = 0`` when there is an acquisition
image (a ``sequence=DESI`` exposure has an acquisition image but a
``sequence=_Split`` exposure does not, for example).

Other than the name and number of the HDUs, the structure of this format
is identical to the focus GFA raw data.

FITS Header Units
=================

HDU00
-----

EXTNAME = GUIDER

Blank data HDU with a header that contains a lot of exposure-level metadata.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ===================================================================== ======= ===============================================
KEY      Example Value                                                         Type    Comment
======== ===================================================================== ======= ===============================================
MODULE   GUIDE                                                                 str     Image Sources/Component
EXPID    118526                                                                int     Exposure number
FRAMES   72                                                                    int     Number of Frames in Archive
COSMSPLT F                                                                     bool    Cosmics split exposure if true
MAXSPLIT 0                                                                     int     Number of allowed exposure splits
VISITIDS 118524                                                                str     List of expids for a visit (same tile)
TILEID   4403                                                                  int     DESI Tile ID
FIBASSGN /data/tiles/SVN_tiles/004/fiberassign-004403.fits.gz                  str     Fiber assign
FLAVOR   science                                                               str     Observation type
OBSTYPE  SCIENCE                                                               str     Spectrograph observation type
SEQUENCE DESI                                                                  str     OCS Sequence name
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
SEQSTART 2022-01-14T10:13:58.576904                                            str     Start time of sequence processing
TIMESYS  UTC                                                                   str     Time system used for date-obs
DATE-OBS 2022-01-14T11:03:58.319124                                            str     [UTC] Observation data and start time
MJD-OBS  59593.46109166                                                        float   Modified Julian Date of observation
STARTADJ 2022-01-14T10:14:26.234369                                            str     Time sequence starts adjusting the inst
OPENSHUT 2022-01-14T11:03:58.319124                                            str     Time shutter opened
CAMSHUT  open                                                                  str     Shutter status during observation
ST       11:13:16.9528                                                         str     Local Sidereal time at observation start (HH:MM
EXPTIME  5.0                                                                   float   [s] Actual exposure time
ACQTIME  15.0                                                                  float   [s] acqusition image exposure time
GUIDTIME 5.0                                                                   float   [s] guider GFA exposure time
FOCSTIME 60.0                                                                  float   [s] focus GFA exposure time
SKYTIME  60.0                                                                  float   [s] sky camera exposure time (acquisition)
REQRA    170.239                                                               float   [deg] Requested right ascension (observer input
REQDEC   -7.093                                                                float   [deg] Requested declination (observer input)
DELTARA  None                                                                  Unknown [arcsec] Offset], right ascension, observer inp
DELTADEC None                                                                  Unknown [arcsec] Offset], declination, observer input
WHITESPT F                                                                     bool    Telescope is at whitespot
ZENITH   F                                                                     bool    Telescope is at zenith
SEANNEX  F                                                                     bool    Telescope is at SE annex
BEYONDP  F                                                                     bool    Telescope is beyond pole
AIRMASS  1.331363                                                              float   Airmass
FOCUS    948.5,-231.1,-91.3,-18.3,10.0,126.3                                   str     Telescope focus settings
VCCD     ON                                                                    str     True (ON) if CCD voltage is on
TRUSTEMP 12.4                                                                  float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.662                                                                float   [deg] Average primary mirror temperature (nit,e
PMREADY  T                                                                     bool    Primary mirror ready
PMCOVER  open                                                                  str     Primary mirror cover
PMCOOL   off                                                                   str     Primary mirror cooling
DOMSHUTU open                                                                  str     Upper dome shutter
DOMSHUTL open                                                                  str     Lower dome shutter
DOMLIGHH off                                                                   str     High dome lights
DOMLIGHL off                                                                   str     Low dome lights
DOMEAZ   165.277                                                               float   [deg] Dome azimuth angle
DOMINPOS T                                                                     bool    Dome is in position
EPOCH    2000.0                                                                float   Epoch of observation
GUIDOFFR 0.0                                                                   float   [arcsec] Cummulative guider offset (RA)
GUIDOFFD -0.0                                                                  float   [arcsec] Cummulative guider offset (dec)
SUNRA    296.113998                                                            float   [deg] Sun RA at start of exposure
SUNDEC   -21.270133                                                            float   [deg] Sun declination at start of exposure
MOONDEC  23.881736                                                             float   [deg] Moon declination at start of exposure
MOONRA   73.512629                                                             float   [deg] Moon RA at start of exposure
MOONSEP  99.425                                                                float   [deg] Moon Separation
SLEWANGL 5.795                                                                 float   [deg] Slew Angle
SLEWTIME 31.341                                                                float   [s] Slew Time
MOUNTAZ  158.328478                                                            float   [deg] Mount azimuth angle
MOUNTDEC -7.10233                                                              float   [deg] Mount declination
MOUNTEL  48.640103                                                             float   [deg] Mount elevation angle
MOUNTHA  -14.235346                                                            float   [deg] Mount hour angle
INCTRL   T                                                                     bool    DESI in control
INPOS    T                                                                     bool    Mount in position
MNTOFFD  -0.0                                                                  float   [arcsec] Mount offset (dec)
MNTOFFR  -0.0                                                                  float   [arcsec] Mount offset (RA)
PARALLAC -18.404235                                                            float   [deg] Parallactic angle
SKYDEC   -7.10233                                                              float   [deg] Telescope declination (pointing on sky)
SKYRA    170.241629                                                            float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.10233                                                              float   [deg] Target declination (to TCS)
TARGTRA  170.241629                                                            float   [deg] Target right ascension (to TCS)
TARGTAZ  158.328478                                                            float   [deg] Target azimuth
TARGTEL  48.640103                                                             float   [deg] Target elevation
TRGTOFFD 0.0                                                                   float   [arcsec] Telescope target offset (dec)
TRGTOFFR 0.0                                                                   float   [arcsec] Telescope target offset (RA)
ZD       41.359897                                                             float   [deg] Telescope zenith distance
TILERA   170.239                                                               float   RA of tile given in fiberassign file
TILEDEC  -7.093                                                                float   DEC of tile given in fiberassign file
TCSST    10:24:01.508                                                          str     Local Sidereal time reported by TCS (HH:MM:SS)
TCSMJD   59593.427501                                                          float   MJD reported by TCS
USETURB  T                                                                     bool    Turbulence corrections are applied if true
USEETC   T                                                                     bool    ETC data available if true
SEEING   None                                                                  Unknown [arcsec] ETC/PM seeing
TRANSPAR None                                                                  Unknown ETC/PM transparency
SKYLEVEL 4.036                                                                 float   [unit?] PM/ETC sky level
PMSEEING None                                                                  Unknown [arcsec] PlateMaker GFAPROC seeing
PMTRANSP None                                                                  Unknown [%] PlateMaker GFAPROC transparency
ACQCAM   GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                             str     Acquisition cameras used
GUIDECAM GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                             str     Guide cameras used for t
FOCUSCAM FOCUS1,FOCUS4,FOCUS6,FOCUS9                                           str     Focus cameras used for this exposure
SKYCAM   SKYCAM0,SKYCAM1                                                       str     Sky cameras used for this exposure
REQADC   316.38,12.3                                                           str     [deg] requested ADC angles
ADCCORR  T                                                                     bool    Correct pointing for ADC setting if True
ADC1PHI  316.380005                                                            float   [deg] ADC 1 angle
ADC2PHI  12.300831                                                             float   [deg] ADC 2 angle
ADC1HOME F                                                                     bool    ADC 1 at home position if True
ADC2HOME F                                                                     bool    ADC 2 at home position if True
ADC1NREV -1.0                                                                  float   ADC 1 number of revs
ADC2NREV 1.0                                                                   float   ADC 2 number of revs
ADC1STAT STOPPED                                                               str     ADC 1 status
ADC2STAT STOPPED                                                               str     ADC 2 status
USESKY   T                                                                     bool    DOS Control: use Sky Monitor
USEFOCUS T                                                                     bool    DOS Control: use focus
HEXPOS   948.5,-231.1,-91.3,-18.3,10.0,126.3                                   str     Hexapod position
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                                               str     Hexapod trim values
USEROTAT T                                                                     bool    DOS Control: use rotator
ROTOFFST 121.0                                                                 float   [arcsec] Rotator offset
ROTENBLD T                                                                     bool    Rotator enabled
ROTRATE  0.0                                                                   float   [arcsec/min] Rotator rate
RESETROT F                                                                     bool    DOS Control: reset hex rotator
SPLITEXP F                                                                     bool    Split exposure part of a visit
USESPLIT T                                                                     bool    Exposure splits are allowed
USEPOS   T                                                                     bool    Fiber positioner data available if true
PETALS   PETAL0,PETAL1,PETAL2,PETAL3,PETAL4,PETAL5,PETAL6,PETAL7,PETAL8,PETAL9 str     Participating petals
USEGUIDR T                                                                     bool    DOS Control: use guider
GUIDMODE catalog                                                               str     Guider mode
USEDONUT T                                                                     bool    DOS Control: use donuts
USESPCTR T                                                                     bool    DOS Control: use spectrographs
SPCGRPHS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                               str     Participating spectrograph
ILLSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                               str     Participating illuminate s
CCDSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                               str     Participating ccd spectrog
TDEWPNT  -33.473                                                               float   Telescope air dew point
TAIRFLOW 0.0                                                                   float   Telescope air flow
TAIRITMP 12.7                                                                  float   [deg] Telescope air in temperature
TAIROTMP 12.8                                                                  float   [deg] Telescope air out temperature
TAIRTEMP 11.3                                                                  float   [deg] Telescope air temperature
TCASITMP 6.6                                                                   float   [deg] Telescope Cass Cage in temperature
TCASOTMP 12.3                                                                  float   [deg] Telescope Cass Cage out temperature
TCSITEMP 12.1                                                                  float   [deg] Telescope center section in temperature
TCSOTEMP 12.2                                                                  float   [deg] Telescope center section out temperature
TCIBTEMP 0.0                                                                   float   [deg] Telescope chimney IB temperature
TCIMTEMP 0.0                                                                   float   [deg] Telescope chimney IM temperature
TCITTEMP 0.0                                                                   float   [deg] Telescope chimney IT temperature
TCOSTEMP 0.0                                                                   float   [deg] Telescope chimney OS temperature
TCOWTEMP 0.0                                                                   float   [deg] Telescope chimney OW temperature
TDBTEMP  12.3                                                                  float   [deg] Telescope dec bore temperature
TFLOWIN  0.0                                                                   float   Telescope flow rate in
TFLOWOUT 0.0                                                                   float   Telescope flow rate out
TGLYCOLI 12.9                                                                  float   [deg] Telescope glycol in temperature
TGLYCOLO 12.6                                                                  float   [deg] Telescope glycol out temperature
THINGES  12.3                                                                  float   [deg] Telescope hinge S temperature
THINGEW  22.3                                                                  float   [deg] Telescope hinge W temperature
TPMAVERT 11.695                                                                float   [deg] Telescope mirror averagetemperature
TPMDESIT 6.0                                                                   float   [deg] Telescope mirror desired temperature
TPMEIBT  12.2                                                                  float   [deg] Telescope mirror EIB temperature
TPMEITT  11.5                                                                  float   [deg] Telescope mirror EIT temperature
TPMEOBT  12.3                                                                  float   [deg] Telescope mirror EOB temperature
TPMEOTT  12.0                                                                  float   [deg] Telescope mirror EOT temperature
TPMNIBT  12.0                                                                  float   [deg] Telescope mirror NIB temperature
TPMNITT  11.4                                                                  float   [deg] Telescope mirror NIT temperature
TPMNOBT  12.3                                                                  float   [deg] Telescope mirror NOB temperature
TPMNOTT  12.0                                                                  float   [deg] Telescope mirror NOT temperature
TPMRTDT  11.68                                                                 float   [deg] Telescope mirror RTD temperature
TPMSIBT  12.1                                                                  float   [deg] Telescope mirror SIB temperature
TPMSITT  11.5                                                                  float   [deg] Telescope mirror SIT temperature
TPMSOBT  12.1                                                                  float   [deg] Telescope mirror SOB temperature
TPMSOTT  11.8                                                                  float   [deg] Telescope mirror SOT temperature
TPMSTAT  ready                                                                 str     Telescope mirror status
TPMWIBT  11.9                                                                  float   [deg] Telescope mirror WIB temperature
TPMWITT  11.3                                                                  float   [deg] Telescope mirror WIT temperature
TPMWOBT  11.9                                                                  float   [deg] Telescope mirror WOB temperature
TPMWOTT  11.8                                                                  float   [deg] Telescope mirror WOT temperature
TPCITEMP 12.1                                                                  float   [deg] Telescope primary cell in temperature
TPCOTEMP 12.1                                                                  float   [deg] Telescope primary cell out temperature
TPR1HUM  0.0                                                                   float   Telescope probe 1 humidity
TPR1TEMP 0.0                                                                   float   [deg] Telescope probe1 temperature
TPR2HUM  0.0                                                                   float   Telescope probe 2 humidity
TPR2TEMP 0.0                                                                   float   [deg] Telescope probe2 temperature
TSERVO   40.0                                                                  float   Telescope servo setpoint
TTRSTEMP 12.1                                                                  float   [deg] Telescope top ring S temperature
TTRWTEMP 12.0                                                                  float   [deg] Telescope top ring W temperature
TTRUETBT -1.5                                                                  float   [deg] Telescope truss ETB temperature
TTRUETTT 11.7                                                                  float   [deg] Telescope truss ETT temperature
TTRUNTBT 11.7                                                                  float   [deg] Telescope truss NTB temperature
TTRUNTTT 11.7                                                                  float   [deg] Telescope truss NTT temperature
TTRUSTBT 11.7                                                                  float   [deg] Telescope truss STB temperature
TTRUSTST 10.8                                                                  float   [deg] Telescope truss STS temperature
TTRUSTTT 11.9                                                                  float   [deg] Telescope truss STT temperature
TTRUTSBT 12.4                                                                  float   [deg] Telescope truss TSB temperature
TTRUTSMT 12.5                                                                  float   [deg] Telescope truss TSM temperature
TTRUTSTT 12.3                                                                  float   [deg] Telescope truss TST temperature
TTRUWTBT 11.6                                                                  float   [deg] Telescope truss WTB temperature
TTRUWTTT 11.7                                                                  float   [deg] Telescope truss WTT temperature
ALARM    F                                                                     bool    UPS major alarm or check battery
ALARM-ON F                                                                     bool    UPS active alarm condition
BATTERY  100.0                                                                 float   [%] UPS Battery left
SECLEFT  5904.0                                                                float   [s] UPS Seconds left
UPSSTAT  System Normal - On Line(7)                                            str     UPS Status
INAMPS   72.1                                                                  float   [A] UPS total input current
OUTWATTS 4900.0,7600.0,4600.0                                                  str     [W] UPS Phase A, B, C output watts
COMPDEW  -10.4                                                                 float   [deg C] Computer room dewpoint
COMPHUM  14.1                                                                  float   [%] Computer room humidity
COMPAMB  25.2                                                                  float   [deg C] Computer room ambient temperature
COMPTEMP 17.3                                                                  float   [deg C] Computer room hygrometer temperature
DEWPOINT -36.9                                                                 float   [deg C] (outside) dewpoint
HUMIDITY 1.6                                                                   float   [%] (outside) humidity
PRESSURE 793.6                                                                 float   [torr] (outside) air pressure
OUTTEMP  11.0                                                                  float   [deg C] outside temperature
WINDDIR  252.9                                                                 float   [deg] wind direction
WINDSPD  10.7                                                                  float   [m/s] wind speed
GUST     13.0                                                                  float   [m/s] Wind gusts speed
AMNIENTN 16.8                                                                  float   [deg C] ambient temperature north
CFLOOR   11.6                                                                  float   [deg C] temperature on C floor
NWALLIN  17.3                                                                  float   [deg C] temperature at north wall inside
NWALLOUT 11.1                                                                  float   [deg C] temperature at north wall outside
WWALLIN  16.6                                                                  float   [deg C] temperature at west wall inside
WWALLOUT 11.5                                                                  float   [deg C] temperature at west wall outside
AMBIENTS 17.6                                                                  float   [deg C] ambient temperature south
FLOOR    15.8                                                                  float   [deg C] temperature at floor (LCR)
EWALLCMP 11.9                                                                  float   [deg C] temperature at east wall, computer room
EWALLCOU 11.6                                                                  float   [deg C] temperature at east wall, Coude room
ROOF     11.0                                                                  float   [deg C] temperature on roof
ROOFAMB  11.3                                                                  float   [deg C] ambient temperature on roof
DOMEBLOW 11.2                                                                  float   [deg C] temperature at dome back, lower
DOMEBUP  11.3                                                                  float   [deg C] temperature at dome back, upper
DOMELLOW 11.2                                                                  float   [deg C] temperature at dome left, lower
DOMELUP  11.1                                                                  float   [deg C] temperature at dome left, upper
DOMERLOW 11.1                                                                  float   [deg C] temperature at dome right, lower
DOMERUP  10.8                                                                  float   [deg C] temperature at dome right, upper
PLATFORM 10.8                                                                  float   [deg C] temperature at platform
SHACKC   16.6                                                                  float   [deg C] temperature at shack ceiling
SHACKW   16.7                                                                  float   [deg C] temperature at shack wall
STAIRSL  11.2                                                                  float   [deg C] temperature at stairs, lower
STAIRSM  11.0                                                                  float   [deg C] temperature at stairs, mid
STAIRSU  11.1                                                                  float   [deg C] temperature at stairs, upper
TELBASE  11.7                                                                  float   [deg C] temperature at telescope base
UTILWALL 11.4                                                                  float   [deg C] temperature at utility room wall
UTILROOM 10.3                                                                  float   [deg C] temperature in utilitiy room
RADESYS  FK5                                                                   str     Coordinate reference frame of major/minor axes
TNFSPROC 7.9838                                                                float   [s] PlateMaker NFSPROC processing time
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
GSGUIDE2 (664.34,38.87)                                                        str
GSGUIDE5 (593.78,1504.27),(437.14,545.33)                                      str
GSGUIDE3 (537.68,1656.18),(360.10,1393.84)                                     str
GSGUIDE7 (223.31,1205.23),(687.61,1805.82)                                     str
GSGUIDE8 (479.93,780.28),(548.26,388.92)                                       str
GSGUIDE0 (167.25,277.52),(622.59,595.97)                                       str
ARCHIVE  /exposures/desi/20220113/00118526/guide-00118526.fits.fz              str
CHECKSUM lFAHlC7GlCAGlC5G                                                      str     HDU checksum updated 2022-01-14T11:13:59
DATASUM           0                                                            str     data unit checksum updated 2022-01-14T11:13:59
======== ===================================================================== ======= ===============================================

Empty HDU.

HDU01
-----

EXTNAME = PMGSTARS

Binary table of candidate guide/ETC stars detected by PlateMaker.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   86               int  width of table in bytes
NAXIS2   18               int  number of rows in table
CHECKSUM YeEnYZBmYbBmYZBm str  HDU checksum updated 2022-01-14T11:13:59
DATASUM  315340011        str  data unit checksum updated 2022-01-14T11:13:59
======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

========== ======= ===== ===================
Name       Type    Units Description
========== ======= ===== ===================
GFA_LOC    char[6]       PETAL_LOC number
RA         float64       Star RA in degrees
DEC        float64       Star Dec in degrees
ROW        float64       Star y pixel coord
COL        float64       Star x pixel coord
RA_IVAR    float64       RA inverse variance
DEC_IVAR   float64       Dec inverse variance
MAG        float64       Star magnitude
MORPHTYPE  int64         Morphological type
GUIDE_FLAG int64         Guiding bitmask
ETC_FLAG   int64         ETC bitmask
========== ======= ===== ===================

``COL`` is the x pixel coordinate of each star in a convention
where the left edge of the image has x = 0.

``ROW`` is the y pixel coordinate of each star in a convention
where the bottom edge of the image has y = 0.

So in this convention the center of the lower left pixel is
(x, y) = (0.5, 0.5) rather than (0, 0).

The star MAG is a synthetic version of DECam r created from
Gaia photometry, inherited from the fiberassign GFA_TARGETS
extension.

MORPHTYPE is the GFA_TARGETS morphological type; this
may, by definition, always be equal to 0, since the
GFA_TARGETS target list should not include resolved galaxies.

GUIDE_FLAG is a flag indicating whether each star is suitable
for use as a guide star. This may always be equal to 1 by
definition, as the PMGSTARS table would simply discard any
star not suitable for use as a guide star.

ETC_FLAG is a bitmask indicating whether each PlateMaker-selected
guide star is suitable for use by the ETC. The main problem
case that ETC_FLAG is supposed to address is variable stars,
which can be fine for guiding but would mess up ETC transparency estimates.
ETC_FLAG = 0 means that a star is usable for the ETC, whereas
nonzero ETC_FLAG means that a star should not be used by the ETC.

HDU02
-----

EXTNAME = GUIDE5

GUIDE5 image cube

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   74304                                                int     number of rows in table
ZTILE3   1                                                    int     size of tiles to be compressed
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
DEVICE   GUIDE5                                               str     Device/controller name
UNIT     5                                                    int     Unit number/letter
UNITTYPE GUIDE                                                str     Image Sources/Component
EXPID    118526                                               int     Exposure number
FRAMES   72                                                   int     Number of Frames in Archive
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
DATE-OBS 2022-01-14T11:03:58.319124                           str     [UTC] Observation data and start time
MJD-OBS  59593.46109166                                       float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:03:58.319124                           str     Time shutter opened
ST       11:13:16.9528                                        str     Local Sidereal time at observation start (HH:MM
ACQTIME  15.0                                                 float   [s] acqusition image exposure time
GUIDTIME 5.0                                                  float   [s] guider GFA exposure time
REQRA    170.239                                              float   [deg] Requested right ascension (observer input
REQDEC   -7.093                                               float   [deg] Requested declination (observer input)
DELTARA  None                                                 Unknown [arcsec] Offset], right ascension, observer inp
DELTADEC None                                                 Unknown [arcsec] Offset], declination, observer input
FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                   str     Telescope focus settings
TRUSTEMP 12.267                                               float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.675                                               float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                               float   Epoch of observation
EQUINOX  2000.0                                               float   Equinox of selected coordinate reference frame
MOUNTAZ  176.725567                                           float   [deg] Mount azimuth angle
MOUNTDEC -7.102329                                            float   [deg] Mount declination
MOUNTEL  50.883914                                            float   [deg] Mount elevation angle
MOUNTHA  -2.081118                                            float   [deg] Mount hour angle
SKYDEC   -7.102329                                            float   [deg] Telescope declination (pointing on sky)
SKYRA    170.24163                                            float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.102329                                            float   [deg] Target declination (to TCS)
TARGTRA  170.24163                                            float   [deg] Target right ascension (to TCS)
USEETC   T                                                    bool    ETC data available if true
ACQCAM   GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8            str     Acquisition cameras used
GUIDECAM GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8            str     Guide cameras used for t
FOCUSCAM FOCUS1,FOCUS4,FOCUS6,FOCUS9                          str     Focus cameras used for this exposure
SKYCAM   SKYCAM0,SKYCAM1                                      str     Sky cameras used for this exposure
ADC1PHI  None                                                 Unknown [deg] ADC 1 angle
USESKY   T                                                    bool    DOS Control: use Sky Monitor
USEFOCUS T                                                    bool    DOS Control: use focus
HEXPOS   946.7,-231.6,-83.4,-18.3,9.9,138.8                   str     Hexapod position
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                              str     Hexapod trim values
USEROTAT T                                                    bool    DOS Control: use rotator
ROTOFFST 138.8                                                float   [arcsec] Rotator offset
ROTENBLD T                                                    bool    Rotator enabled
ROTRATE  0.513                                                float   [arcsec/min] Rotator rate
USEGUIDR T                                                    bool    DOS Control: use guider
USEDONUT T                                                    bool    DOS Control: use donuts
WCSAXES  2                                                    int
RADESYS  FK5                                                  str     Coordinate reference frame of major/minor axes
CTYPE1   RA---TAN                                             str
CTYPE2   DEC--TAN                                             str
CD1_1    5.6345e-05                                           float
CD1_2    -1.6764e-05                                          float
CD2_1    -1.8252e-05                                          float
CD2_2    -5.1779e-05                                          float
SHAPE    1032,2248                                            str
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
ADCPHI2  None                                                 Unknown
ROI      None                                                 Unknown
ROIWIDTH None                                                 Unknown
GEXPMODE normal                                               str     GFA readout mode (loop/normal)
DEVICEID dev08                                                str     GFA device id (serial number)
REQTIME  1860.0                                               float   [s] Requested exposure time
CHECKSUM drbFfoZDdobDdoZD                                     str     HDU checksum updated 2022-01-14T11:13:59
DATASUM  1908774157                                           str     data unit checksum updated 2022-01-14T11:13:59
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 2248x1032x72]

HDU03
-----

EXTNAME = GUIDE5T

GUIDE5 image cube metadata

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   242              int  width of table in bytes
NAXIS2   72               int  number of rows in table
CHECKSUM CZCLCWCKCWCKCWCK str  HDU checksum updated 2022-01-14T11:13:59
DATASUM  79233899         str  data unit checksum updated 2022-01-14T11:13:59
======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

======== ======== ===== ===================
Name     Type     Units Description
======== ======== ===== ===================
EXPTIME  float64        Exposure time (sec)
NIGHT    int64          Observing night
DATE-OBS char[26]       YYYY-MM-DDTHH:MM:SS.SSSSSS (UT)
TIME-OBS char[15]       HH:MM:SS.SSSSSS (UT)
MJD-OBS  float64        MJD (start of frame)
OPENSHUT char[26]       YYYY-MM-DDTHH:MM:SS.SSSSSS (UT)
ST       char[13]       HH:MM:SS.SS (Local Sidereal Time at frame start)
HEXPOS   char[34]       Hexapod position
GAMBNTT  float64        GFA ambient temp (C)
GFPGAT   float64        GFA FPGA temp (C)
GFILTERT float64        GFA filter temp (C)
GCOLDTEC float64        GFA cold peltier temp (C)
GHOTTEC  float64        GFA hot peltier temp (C)
GCCDTEMP float64        GFA CCD temp (C)
GCAMTEMP float64        GFA camera temp (C)
GHUMID2  float64        GFA humidity 2
GHUMID3  float64        GFA humidity 3
CRPIX1   float64        Reference pixel in axis1
CRPIX2   float64        Reference pixel in axis2
CRVAL1   float64        Physical value of the reference pixel
CRVAL2   float64        Physical value of the reference pixel
======== ======== ===== ===================

``HEXPOS`` is a string containing the six hexapod parameters
separated by commas, ordered as X, Y, Z, tip, tilt, rotation
(positions in microns, angles in arcseconds).

HDU04
-----

EXTNAME = GUIDE3

GUIDE3 image cube

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   74304                                                int     number of rows in table
ZTILE3   1                                                    int     size of tiles to be compressed
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
DEVICE   GUIDE3                                               str     Device/controller name
UNIT     3                                                    int     Unit number/letter
UNITTYPE GUIDE                                                str     Image Sources/Component
EXPID    118526                                               int     Exposure number
FRAMES   72                                                   int     Number of Frames in Archive
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
DATE-OBS 2022-01-14T11:03:58.319124                           str     [UTC] Observation data and start time
MJD-OBS  59593.46109166                                       float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:03:58.319124                           str     Time shutter opened
ST       11:13:16.9528                                        str     Local Sidereal time at observation start (HH:MM
ACQTIME  15.0                                                 float   [s] acqusition image exposure time
GUIDTIME 5.0                                                  float   [s] guider GFA exposure time
REQRA    170.239                                              float   [deg] Requested right ascension (observer input
REQDEC   -7.093                                               float   [deg] Requested declination (observer input)
DELTARA  None                                                 Unknown [arcsec] Offset], right ascension, observer inp
DELTADEC None                                                 Unknown [arcsec] Offset], declination, observer input
FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                   str     Telescope focus settings
TRUSTEMP 12.267                                               float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.675                                               float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                               float   Epoch of observation
EQUINOX  2000.0                                               float   Equinox of selected coordinate reference frame
MOUNTAZ  176.725567                                           float   [deg] Mount azimuth angle
MOUNTDEC -7.102329                                            float   [deg] Mount declination
MOUNTEL  50.883914                                            float   [deg] Mount elevation angle
MOUNTHA  -2.081118                                            float   [deg] Mount hour angle
SKYDEC   -7.102329                                            float   [deg] Telescope declination (pointing on sky)
SKYRA    170.24163                                            float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.102329                                            float   [deg] Target declination (to TCS)
TARGTRA  170.24163                                            float   [deg] Target right ascension (to TCS)
USEETC   T                                                    bool    ETC data available if true
ACQCAM   GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8            str     Acquisition cameras used
GUIDECAM GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8            str     Guide cameras used for t
FOCUSCAM FOCUS1,FOCUS4,FOCUS6,FOCUS9                          str     Focus cameras used for this exposure
SKYCAM   SKYCAM0,SKYCAM1                                      str     Sky cameras used for this exposure
ADC1PHI  None                                                 Unknown [deg] ADC 1 angle
USESKY   T                                                    bool    DOS Control: use Sky Monitor
USEFOCUS T                                                    bool    DOS Control: use focus
HEXPOS   946.7,-231.6,-83.4,-18.3,9.9,138.8                   str     Hexapod position
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                              str     Hexapod trim values
USEROTAT T                                                    bool    DOS Control: use rotator
ROTOFFST 138.8                                                float   [arcsec] Rotator offset
ROTENBLD T                                                    bool    Rotator enabled
ROTRATE  0.513                                                float   [arcsec/min] Rotator rate
USEGUIDR T                                                    bool    DOS Control: use guider
USEDONUT T                                                    bool    DOS Control: use donuts
WCSAXES  2                                                    int
RADESYS  FK5                                                  str     Coordinate reference frame of major/minor axes
CTYPE1   RA---TAN                                             str
CTYPE2   DEC--TAN                                             str
CD1_1    3.4943e-05                                           float
CD1_2    4.3939e-05                                           float
CD2_1    4.7823e-05                                           float
CD2_2    -3.2116e-05                                          float
SHAPE    1032,2248                                            str
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
ADCPHI2  None                                                 Unknown
ROI      None                                                 Unknown
ROIWIDTH None                                                 Unknown
GEXPMODE normal                                               str     GFA readout mode (loop/normal)
DEVICEID dev02                                                str     GFA device id (serial number)
REQTIME  1860.0                                               float   [s] Requested exposure time
CHECKSUM loGEloDBloDBloDB                                     str     HDU checksum updated 2022-01-14T11:14:00
DATASUM  2587335691                                           str     data unit checksum updated 2022-01-14T11:14:00
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 2248x1032x72]

HDU05
-----

EXTNAME = GUIDE3T

GUIDE3 image cube metadata

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   242              int  width of table in bytes
NAXIS2   72               int  number of rows in table
CHECKSUM ZA2Ve40TZ90Tb90T str  HDU checksum updated 2022-01-14T11:14:00
DATASUM  1996482551       str  data unit checksum updated 2022-01-14T11:14:00
======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

======== ======== ===== ===================
Name     Type     Units Description
======== ======== ===== ===================
EXPTIME  float64        Exposure time (sec)
NIGHT    int64          Observing night
DATE-OBS char[26]       YYYY-MM-DDTHH:MM:SS.SSSSSS (UT)
TIME-OBS char[15]       HH:MM:SS.SSSSSS (UT)
MJD-OBS  float64        MJD (start of frame)
OPENSHUT char[26]       YYYY-MM-DDTHH:MM:SS.SSSSSS (UT)
ST       char[13]       HH:MM:SS.SS (Local Sidereal Time at frame start)
HEXPOS   char[34]       Hexapod position
GAMBNTT  float64        GFA ambient temp (C)
GFPGAT   float64        GFA FPGA temp (C)
GFILTERT float64        GFA filter temp (C)
GCOLDTEC float64        GFA cold peltier temp (C)
GHOTTEC  float64        GFA hot peltier temp (C)
GCCDTEMP float64        GFA CCD temp (C)
GCAMTEMP float64        GFA camera temp (C)
GHUMID2  float64        GFA humidity 2
GHUMID3  float64        GFA humidity 3
CRPIX1   float64        Reference pixel in axis1
CRPIX2   float64        Reference pixel in axis2
CRVAL1   float64        Physical value of the reference pixel
CRVAL2   float64        Physical value of the reference pixel
======== ======== ===== ===================

HDU06
-----

EXTNAME = GUIDE2

GUIDE2 image cube

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   74304                                                int     number of rows in table
ZTILE3   1                                                    int     size of tiles to be compressed
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
DEVICE   GUIDE2                                               str     Device/controller name
UNIT     2                                                    int     Unit number/letter
UNITTYPE GUIDE                                                str     Image Sources/Component
EXPID    118526                                               int     Exposure number
FRAMES   72                                                   int     Number of Frames in Archive
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
DATE-OBS 2022-01-14T11:03:58.319124                           str     [UTC] Observation data and start time
MJD-OBS  59593.46109166                                       float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:03:58.319124                           str     Time shutter opened
ST       11:13:16.9528                                        str     Local Sidereal time at observation start (HH:MM
ACQTIME  15.0                                                 float   [s] acqusition image exposure time
GUIDTIME 5.0                                                  float   [s] guider GFA exposure time
REQRA    170.239                                              float   [deg] Requested right ascension (observer input
REQDEC   -7.093                                               float   [deg] Requested declination (observer input)
DELTARA  None                                                 Unknown [arcsec] Offset], right ascension, observer inp
DELTADEC None                                                 Unknown [arcsec] Offset], declination, observer input
FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                   str     Telescope focus settings
TRUSTEMP 12.267                                               float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.675                                               float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                               float   Epoch of observation
EQUINOX  2000.0                                               float   Equinox of selected coordinate reference frame
MOUNTAZ  176.725567                                           float   [deg] Mount azimuth angle
MOUNTDEC -7.102329                                            float   [deg] Mount declination
MOUNTEL  50.883914                                            float   [deg] Mount elevation angle
MOUNTHA  -2.081118                                            float   [deg] Mount hour angle
SKYDEC   -7.102329                                            float   [deg] Telescope declination (pointing on sky)
SKYRA    170.24163                                            float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.102329                                            float   [deg] Target declination (to TCS)
TARGTRA  170.24163                                            float   [deg] Target right ascension (to TCS)
USEETC   T                                                    bool    ETC data available if true
ACQCAM   GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8            str     Acquisition cameras used
GUIDECAM GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8            str     Guide cameras used for t
FOCUSCAM FOCUS1,FOCUS4,FOCUS6,FOCUS9                          str     Focus cameras used for this exposure
SKYCAM   SKYCAM0,SKYCAM1                                      str     Sky cameras used for this exposure
ADC1PHI  None                                                 Unknown [deg] ADC 1 angle
USESKY   T                                                    bool    DOS Control: use Sky Monitor
USEFOCUS T                                                    bool    DOS Control: use focus
HEXPOS   946.7,-231.6,-83.4,-18.3,9.9,138.8                   str     Hexapod position
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                              str     Hexapod trim values
USEROTAT T                                                    bool    DOS Control: use rotator
ROTOFFST 138.8                                                float   [arcsec] Rotator offset
ROTENBLD T                                                    bool    Rotator enabled
ROTRATE  0.513                                                float   [arcsec/min] Rotator rate
USEGUIDR T                                                    bool    DOS Control: use guider
USEDONUT T                                                    bool    DOS Control: use donuts
WCSAXES  2                                                    int
RADESYS  FK5                                                  str     Coordinate reference frame of major/minor axes
CTYPE1   RA---TAN                                             str
CTYPE2   DEC--TAN                                             str
CD1_1    1.9486e-07                                           float
CD1_2    5.4424e-05                                           float
CD2_1    5.9241e-05                                           float
CD2_2    -1.8383e-07                                          float
SHAPE    1032,2248                                            str
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
ADCPHI2  None                                                 Unknown
ROI      None                                                 Unknown
ROIWIDTH None                                                 Unknown
GEXPMODE normal                                               str     GFA readout mode (loop/normal)
DEVICEID dev06                                                str     GFA device id (serial number)
REQTIME  1860.0                                               float   [s] Requested exposure time
CHECKSUM 9iG4AfE49fE4AfE4                                     str     HDU checksum updated 2022-01-14T11:14:01
DATASUM  2955333335                                           str     data unit checksum updated 2022-01-14T11:14:01
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 2248x1032x72]

HDU07
-----

EXTNAME = GUIDE2T

GUIDE2 image cube metadata

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   242              int  width of table in bytes
NAXIS2   72               int  number of rows in table
CHECKSUM 7qDGAoD90oDE7oD9 str  HDU checksum updated 2022-01-14T11:14:01
DATASUM  2746564241       str  data unit checksum updated 2022-01-14T11:14:01
======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

======== ======== ===== ===================
Name     Type     Units Description
======== ======== ===== ===================
EXPTIME  float64        Exposure time (sec)
NIGHT    int64          Observing night
DATE-OBS char[26]       YYYY-MM-DDTHH:MM:SS.SSSSSS (UT)
TIME-OBS char[15]       HH:MM:SS.SSSSSS (UT)
MJD-OBS  float64        MJD (start of frame)
OPENSHUT char[26]       YYYY-MM-DDTHH:MM:SS.SSSSSS (UT)
ST       char[13]       HH:MM:SS.SS (Local Sidereal Time at frame start)
HEXPOS   char[34]       Hexapod position
GAMBNTT  float64        GFA ambient temp (C)
GFPGAT   float64        GFA FPGA temp (C)
GFILTERT float64        GFA filter temp (C)
GCOLDTEC float64        GFA cold peltier temp (C)
GHOTTEC  float64        GFA hot peltier temp (C)
GCCDTEMP float64        GFA CCD temp (C)
GCAMTEMP float64        GFA camera temp (C)
GHUMID2  float64        GFA humidity 2
GHUMID3  float64        GFA humidity 3
CRPIX1   float64        Reference pixel in axis1
CRPIX2   float64        Reference pixel in axis2
CRVAL1   float64        Physical value of the reference pixel
CRVAL2   float64        Physical value of the reference pixel
======== ======== ===== ===================

HDU08
-----

EXTNAME = GUIDE7

GUIDE7 image cube

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   74304                                                int     number of rows in table
ZTILE3   1                                                    int     size of tiles to be compressed
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
DEVICE   GUIDE7                                               str     Device/controller name
UNIT     7                                                    int     Unit number/letter
UNITTYPE GUIDE                                                str     Image Sources/Component
EXPID    118526                                               int     Exposure number
FRAMES   72                                                   int     Number of Frames in Archive
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
DATE-OBS 2022-01-14T11:03:58.319124                           str     [UTC] Observation data and start time
MJD-OBS  59593.46109166                                       float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:03:58.319124                           str     Time shutter opened
ST       11:13:16.9528                                        str     Local Sidereal time at observation start (HH:MM
ACQTIME  15.0                                                 float   [s] acqusition image exposure time
GUIDTIME 5.0                                                  float   [s] guider GFA exposure time
REQRA    170.239                                              float   [deg] Requested right ascension (observer input
REQDEC   -7.093                                               float   [deg] Requested declination (observer input)
DELTARA  None                                                 Unknown [arcsec] Offset], right ascension, observer inp
DELTADEC None                                                 Unknown [arcsec] Offset], declination, observer input
FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                   str     Telescope focus settings
TRUSTEMP 12.267                                               float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.675                                               float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                               float   Epoch of observation
EQUINOX  2000.0                                               float   Equinox of selected coordinate reference frame
MOUNTAZ  176.725567                                           float   [deg] Mount azimuth angle
MOUNTDEC -7.102329                                            float   [deg] Mount declination
MOUNTEL  50.883914                                            float   [deg] Mount elevation angle
MOUNTHA  -2.081118                                            float   [deg] Mount hour angle
SKYDEC   -7.102329                                            float   [deg] Telescope declination (pointing on sky)
SKYRA    170.24163                                            float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.102329                                            float   [deg] Target declination (to TCS)
TARGTRA  170.24163                                            float   [deg] Target right ascension (to TCS)
USEETC   T                                                    bool    ETC data available if true
ACQCAM   GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8            str     Acquisition cameras used
GUIDECAM GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8            str     Guide cameras used for t
FOCUSCAM FOCUS1,FOCUS4,FOCUS6,FOCUS9                          str     Focus cameras used for this exposure
SKYCAM   SKYCAM0,SKYCAM1                                      str     Sky cameras used for this exposure
ADC1PHI  None                                                 Unknown [deg] ADC 1 angle
USESKY   T                                                    bool    DOS Control: use Sky Monitor
USEFOCUS T                                                    bool    DOS Control: use focus
HEXPOS   946.7,-231.6,-83.4,-18.3,9.9,138.8                   str     Hexapod position
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                              str     Hexapod trim values
USEROTAT T                                                    bool    DOS Control: use rotator
ROTOFFST 138.8                                                float   [arcsec] Rotator offset
ROTENBLD T                                                    bool    Rotator enabled
ROTRATE  0.513                                                float   [arcsec/min] Rotator rate
USEGUIDR T                                                    bool    DOS Control: use guider
USEDONUT T                                                    bool    DOS Control: use donuts
WCSAXES  2                                                    int
RADESYS  FK5                                                  str     Coordinate reference frame of major/minor axes
CTYPE1   RA---TAN                                             str
CTYPE2   DEC--TAN                                             str
CD1_1    2.0968e-07                                           float
CD1_2    -5.443e-05                                           float
CD2_1    -5.9249e-05                                          float
CD2_2    -1.8791e-07                                          float
SHAPE    1032,2248                                            str
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
ADCPHI2  None                                                 Unknown
ROI      None                                                 Unknown
ROIWIDTH None                                                 Unknown
GEXPMODE normal                                               str     GFA readout mode (loop/normal)
DEVICEID dev01                                                str     GFA device id (serial number)
REQTIME  1860.0                                               float   [s] Requested exposure time
CHECKSUM HB4WH93VHA3VH73V                                     str     HDU checksum updated 2022-01-14T11:14:02
DATASUM  1347049373                                           str     data unit checksum updated 2022-01-14T11:14:02
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 2248x1032x72]

HDU09
-----

EXTNAME = GUIDE7T

GUIDE7 image cube metadata

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   242              int  width of table in bytes
NAXIS2   72               int  number of rows in table
CHECKSUM IbGoJaDnIaDnIaDn str  HDU checksum updated 2022-01-14T11:14:02
DATASUM  3635643212       str  data unit checksum updated 2022-01-14T11:14:02
======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

======== ======== ===== ===================
Name     Type     Units Description
======== ======== ===== ===================
EXPTIME  float64        Exposure time (sec)
NIGHT    int64          Observing night
DATE-OBS char[26]       YYYY-MM-DDTHH:MM:SS.SSSSSS (UT)
TIME-OBS char[15]       HH:MM:SS.SSSSSS (UT)
MJD-OBS  float64        MJD (start of frame)
OPENSHUT char[26]       YYYY-MM-DDTHH:MM:SS.SSSSSS (UT)
ST       char[13]       HH:MM:SS.SS (Local Sidereal Time at frame start)
HEXPOS   char[34]       Hexapod position
GAMBNTT  float64        GFA ambient temp (C)
GFPGAT   float64        GFA FPGA temp (C)
GFILTERT float64        GFA filter temp (C)
GCOLDTEC float64        GFA cold peltier temp (C)
GHOTTEC  float64        GFA hot peltier temp (C)
GCCDTEMP float64        GFA CCD temp (C)
GCAMTEMP float64        GFA camera temp (C)
GHUMID2  float64        GFA humidity 2
GHUMID3  float64        GFA humidity 3
CRPIX1   float64        Reference pixel in axis1
CRPIX2   float64        Reference pixel in axis2
CRVAL1   float64        Physical value of the reference pixel
CRVAL2   float64        Physical value of the reference pixel
======== ======== ===== ===================

HDU10
-----

EXTNAME = GUIDE8

GUIDE8 image cube

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   74304                                                int     number of rows in table
ZTILE3   1                                                    int     size of tiles to be compressed
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
DEVICE   GUIDE8                                               str     Device/controller name
UNIT     8                                                    int     Unit number/letter
UNITTYPE GUIDE                                                str     Image Sources/Component
EXPID    118526                                               int     Exposure number
FRAMES   72                                                   int     Number of Frames in Archive
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
DATE-OBS 2022-01-14T11:03:58.319124                           str     [UTC] Observation data and start time
MJD-OBS  59593.46109166                                       float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:03:58.319124                           str     Time shutter opened
ST       11:13:16.9528                                        str     Local Sidereal time at observation start (HH:MM
ACQTIME  15.0                                                 float   [s] acqusition image exposure time
GUIDTIME 5.0                                                  float   [s] guider GFA exposure time
REQRA    170.239                                              float   [deg] Requested right ascension (observer input
REQDEC   -7.093                                               float   [deg] Requested declination (observer input)
DELTARA  None                                                 Unknown [arcsec] Offset], right ascension, observer inp
DELTADEC None                                                 Unknown [arcsec] Offset], declination, observer input
FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                   str     Telescope focus settings
TRUSTEMP 12.267                                               float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.675                                               float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                               float   Epoch of observation
EQUINOX  2000.0                                               float   Equinox of selected coordinate reference frame
MOUNTAZ  176.725567                                           float   [deg] Mount azimuth angle
MOUNTDEC -7.102329                                            float   [deg] Mount declination
MOUNTEL  50.883914                                            float   [deg] Mount elevation angle
MOUNTHA  -2.081118                                            float   [deg] Mount hour angle
SKYDEC   -7.102329                                            float   [deg] Telescope declination (pointing on sky)
SKYRA    170.24163                                            float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.102329                                            float   [deg] Target declination (to TCS)
TARGTRA  170.24163                                            float   [deg] Target right ascension (to TCS)
USEETC   T                                                    bool    ETC data available if true
ACQCAM   GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8            str     Acquisition cameras used
GUIDECAM GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8            str     Guide cameras used for t
FOCUSCAM FOCUS1,FOCUS4,FOCUS6,FOCUS9                          str     Focus cameras used for this exposure
SKYCAM   SKYCAM0,SKYCAM1                                      str     Sky cameras used for this exposure
ADC1PHI  None                                                 Unknown [deg] ADC 1 angle
USESKY   T                                                    bool    DOS Control: use Sky Monitor
USEFOCUS T                                                    bool    DOS Control: use focus
HEXPOS   946.7,-231.6,-83.4,-18.3,9.9,138.8                   str     Hexapod position
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                              str     Hexapod trim values
USEROTAT T                                                    bool    DOS Control: use rotator
ROTOFFST 138.8                                                float   [arcsec] Rotator offset
ROTENBLD T                                                    bool    Rotator enabled
ROTRATE  0.513                                                float   [arcsec/min] Rotator rate
USEGUIDR T                                                    bool    DOS Control: use guider
USEDONUT T                                                    bool    DOS Control: use donuts
WCSAXES  2                                                    int
RADESYS  FK5                                                  str     Coordinate reference frame of major/minor axes
CTYPE1   RA---TAN                                             str
CTYPE2   DEC--TAN                                             str
CD1_1    -3.4681e-05                                          float
CD1_2    -4.4134e-05                                          float
CD2_1    -4.804e-05                                           float
CD2_2    3.1872e-05                                           float
SHAPE    1032,2248                                            str
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
ADCPHI2  None                                                 Unknown
ROI      None                                                 Unknown
ROIWIDTH None                                                 Unknown
GEXPMODE normal                                               str     GFA readout mode (loop/normal)
DEVICEID dev04                                                str     GFA device id (serial number)
REQTIME  1860.0                                               float   [s] Requested exposure time
CHECKSUM 9KhoAJhn4Jhn9Jhn                                     str     HDU checksum updated 2022-01-14T11:14:03
DATASUM  663748813                                            str     data unit checksum updated 2022-01-14T11:14:03
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 2248x1032x72]

HDU11
-----

EXTNAME = GUIDE8T

GUIDE8 image cube metadata

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   241              int  width of table in bytes
NAXIS2   72               int  number of rows in table
CHECKSUM EAADG439E99CE999 str  HDU checksum updated 2022-01-14T11:14:03
DATASUM  2061256282       str  data unit checksum updated 2022-01-14T11:14:03
======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

======== ======== ===== ===================
Name     Type     Units Description
======== ======== ===== ===================
EXPTIME  float64        Exposure time (sec)
NIGHT    int64          Observing night
DATE-OBS char[26]       YYYY-MM-DDTHH:MM:SS.SSSSSS (UT)
TIME-OBS char[15]       HH:MM:SS.SSSSSS (UT)
MJD-OBS  float64        MJD (start of frame)
OPENSHUT char[26]       YYYY-MM-DDTHH:MM:SS.SSSSSS (UT)
ST       char[13]       HH:MM:SS.SS (Local Sidereal Time at frame start)
HEXPOS   char[34]       Hexapod position
GAMBNTT  float64        GFA ambient temp (C)
GFPGAT   float64        GFA FPGA temp (C)
GFILTERT float64        GFA filter temp (C)
GCOLDTEC float64        GFA cold peltier temp (C)
GHOTTEC  float64        GFA hot peltier temp (C)
GCCDTEMP float64        GFA CCD temp (C)
GCAMTEMP float64        GFA camera temp (C)
GHUMID2  float64        GFA humidity 2
GHUMID3  float64        GFA humidity 3
CRPIX1   float64        Reference pixel in axis1
CRPIX2   float64        Reference pixel in axis2
CRVAL1   float64        Physical value of the reference pixel
CRVAL2   float64        Physical value of the reference pixel
======== ======== ===== ===================

HDU12
-----

EXTNAME = GUIDE0

GUIDE0 image cube

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   74304                                                int     number of rows in table
ZTILE3   1                                                    int     size of tiles to be compressed
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
DEVICE   GUIDE0                                               str     Device/controller name
UNIT     0                                                    int     Unit number/letter
UNITTYPE GUIDE                                                str     Image Sources/Component
EXPID    118526                                               int     Exposure number
FRAMES   72                                                   int     Number of Frames in Archive
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
DATE-OBS 2022-01-14T11:03:58.319124                           str     [UTC] Observation data and start time
MJD-OBS  59593.46109166                                       float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:03:58.319124                           str     Time shutter opened
ST       11:13:16.9528                                        str     Local Sidereal time at observation start (HH:MM
ACQTIME  15.0                                                 float   [s] acqusition image exposure time
GUIDTIME 5.0                                                  float   [s] guider GFA exposure time
REQRA    170.239                                              float   [deg] Requested right ascension (observer input
REQDEC   -7.093                                               float   [deg] Requested declination (observer input)
DELTARA  None                                                 Unknown [arcsec] Offset], right ascension, observer inp
DELTADEC None                                                 Unknown [arcsec] Offset], declination, observer input
FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                   str     Telescope focus settings
TRUSTEMP 12.267                                               float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.675                                               float   [deg] Average primary mirror temperature (nit,e
EPOCH    2000.0                                               float   Epoch of observation
EQUINOX  2000.0                                               float   Equinox of selected coordinate reference frame
MOUNTAZ  176.725567                                           float   [deg] Mount azimuth angle
MOUNTDEC -7.102329                                            float   [deg] Mount declination
MOUNTEL  50.883914                                            float   [deg] Mount elevation angle
MOUNTHA  -2.081118                                            float   [deg] Mount hour angle
SKYDEC   -7.102329                                            float   [deg] Telescope declination (pointing on sky)
SKYRA    170.24163                                            float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.102329                                            float   [deg] Target declination (to TCS)
TARGTRA  170.24163                                            float   [deg] Target right ascension (to TCS)
USEETC   T                                                    bool    ETC data available if true
ACQCAM   GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8            str     Acquisition cameras used
GUIDECAM GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8            str     Guide cameras used for t
FOCUSCAM FOCUS1,FOCUS4,FOCUS6,FOCUS9                          str     Focus cameras used for this exposure
SKYCAM   SKYCAM0,SKYCAM1                                      str     Sky cameras used for this exposure
ADC1PHI  None                                                 Unknown [deg] ADC 1 angle
USESKY   T                                                    bool    DOS Control: use Sky Monitor
USEFOCUS T                                                    bool    DOS Control: use focus
HEXPOS   946.7,-231.6,-83.4,-18.3,9.9,138.8                   str     Hexapod position
HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                              str     Hexapod trim values
USEROTAT T                                                    bool    DOS Control: use rotator
ROTOFFST 138.8                                                float   [arcsec] Rotator offset
ROTENBLD T                                                    bool    Rotator enabled
ROTRATE  0.513                                                float   [arcsec/min] Rotator rate
USEGUIDR T                                                    bool    DOS Control: use guider
USEDONUT T                                                    bool    DOS Control: use donuts
WCSAXES  2                                                    int
RADESYS  FK5                                                  str     Coordinate reference frame of major/minor axes
CTYPE1   RA---TAN                                             str
CTYPE2   DEC--TAN                                             str
CD1_1    -5.6334e-05                                          float
CD1_2    1.6861e-05                                           float
CD2_1    1.836e-05                                            float
CD2_2    5.1764e-05                                           float
SHAPE    1032,2248                                            str
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
ADCPHI2  None                                                 Unknown
ROI      None                                                 Unknown
ROIWIDTH None                                                 Unknown
GEXPMODE normal                                               str     GFA readout mode (loop/normal)
DEVICEID dev10                                                str     GFA device id (serial number)
REQTIME  1860.0                                               float   [s] Requested exposure time
CHECKSUM X2EZY2DZX2DZX2DZ                                     str     HDU checksum updated 2022-01-14T11:14:04
DATASUM  2619950170                                           str     data unit checksum updated 2022-01-14T11:14:04
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 2248x1032x72]

HDU13
-----

EXTNAME = GUIDE0T

GUIDE0 image cube metadata

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   242              int  width of table in bytes
NAXIS2   72               int  number of rows in table
CHECKSUM Jo9AJm64Jm6AJm63 str  HDU checksum updated 2022-01-14T11:14:04
DATASUM  2766359628       str  data unit checksum updated 2022-01-14T11:14:04
======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

======== ======== ===== ===================
Name     Type     Units Description
======== ======== ===== ===================
EXPTIME  float64        Exposure time (sec)
NIGHT    int64          Observing night
DATE-OBS char[26]       YYYY-MM-DDTHH:MM:SS.SSSSSS (UT)
TIME-OBS char[15]       HH:MM:SS.SSSSSS (UT)
MJD-OBS  float64        MJD (start of frame)
OPENSHUT char[26]       YYYY-MM-DDTHH:MM:SS.SSSSSS (UT)
ST       char[13]       HH:MM:SS.SS (Local Sidereal Time at frame start)
HEXPOS   char[34]       Hexapod position
GAMBNTT  float64        GFA ambient temp (C)
GFPGAT   float64        GFA FPGA temp (C)
GFILTERT float64        GFA filter temp (C)
GCOLDTEC float64        GFA cold peltier temp (C)
GHOTTEC  float64        GFA hot peltier temp (C)
GCCDTEMP float64        GFA CCD temp (C)
GCAMTEMP float64        GFA camera temp (C)
GHUMID2  float64        GFA humidity 2
GHUMID3  float64        GFA humidity 3
CRPIX1   float64        Reference pixel in axis1
CRPIX2   float64        Reference pixel in axis2
CRVAL1   float64        Physical value of the reference pixel
CRVAL2   float64        Physical value of the reference pixel
======== ======== ===== ===================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
