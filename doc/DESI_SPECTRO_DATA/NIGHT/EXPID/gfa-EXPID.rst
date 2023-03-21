=========
gfa-EXPID
=========

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``gfa-EXPID.fits.fz``, where EXPID is the zero-padded
    8-digit exposure ID.
:Regex: ``gfa-[0-9]{8}\.fits\.fz``
:File Type: FITS, 26 MB

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU00_         IMAGE    *Brief Description*
HDU01_ GFA     BINTABLE *Brief Description*
HDU02_ GUIDE0  BINTABLE *Brief Description*
HDU03_ FOCUS9  BINTABLE *Brief Description*
HDU04_ FOCUS1  BINTABLE *Brief Description*
HDU05_ FOCUS4  BINTABLE *Brief Description*
HDU06_ GUIDE3  BINTABLE *Brief Description*
HDU07_ GUIDE7  BINTABLE *Brief Description*
HDU08_ GUIDE5  BINTABLE *Brief Description*
HDU09_ GUIDE2  BINTABLE *Brief Description*
HDU10_ FOCUS6  BINTABLE *Brief Description*
HDU11_ GUIDE8  BINTABLE *Brief Description*
====== ======= ======== ===================


FITS Header Units
=================

HDU00
-----

*Summarize the contents of this HDU.*

This HDU has no non-standard required keywords.

Empty HDU.

HDU01
-----

EXTNAME = GFA

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ====================================================== ======= ===============================================
    KEY      Example Value                                          Type    Comment
    ======== ====================================================== ======= ===============================================
    NAXIS1   8                                                      int     width of table in bytes
    NAXIS2   1                                                      int     number of rows in table
    BZERO    32768                                                  int     offset data range to that of unsigned short
    BSCALE   1                                                      int     default scaling factor
    MODULE   GFA                                                    str     Image Sources/Component
    EXPID    168807                                                 int     Exposure number
    EXPFRAME 0                                                      int     Frame number
    FRAMES   1                                                      int     Number of Frames in Archive
    COSMSPLT F                                                      bool    Cosmics split exposure if true
    MAXSPLIT 0                                                      int     Number of allowed exposure splits
    FLAVOR   science                                                str     Observation type
    SEQUENCE GFA                                                    str     OCS Sequence name
    MANIFEST F                                                      bool    DOS exposure manifest
    OBJECT                                                          str     Object name
    PURPOSE  Main Survey                                            str     Purpose of observing night
    PROGRAM  Kickstart Focus Procedure                              str     Program name
    NTSSURVY na                                                     str     NTS survey name
    PROPID   2020B-5000                                             str     Proposal ID
    OBSERVER Jesse Han, Christopher Manser                          str     Names of observers
    LEAD     Martin Landriau                                        str     Lead observer
    INSTRUME DESI                                                   str     Instrument name
    OBSERVAT KPNO                                                   str     Observatory name
    OBS-LAT  31.96403                                               str     [deg] Observatory latitude
    OBS-LONG -111.59989                                             str     [deg] Observatory east longitude
    OBS-ELEV 2097.0                                                 float   [m] Observatory elevation
    TELESCOP KPNO 4.0-m telescope                                   str     Telescope name
    CORRCTOR DESI Corrector                                         str     Corrector Identification
    SEQNUM   1                                                      int     Number of exposure in sequence
    NIGHT    20230224                                               int     Observing night
    SEQSTART 2023-02-25T01:58:04.748405                             str     Start time of sequence processing
    TIMESYS  UTC                                                    str     Time system used for date-obs
    DATE-OBS 2023-02-25T01:58:27.541024                             str     [UTC] Observation data and start time
    MJD-OBS  60000.08226321                                         float   Modified Julian Date of observation
    OPENSHUT 2023-02-25T01:58:27.541024                             str     [s] Time shutter opened
    CLOSSHUT None                                                   Unknown [s] Time it takes exposure shutter to close
    CAMSHUT  open                                                   str     Shutter status during observation
    ST       4:51:50.015                                            str     Local Sidereal time at observation start (HH:MM
    EXPTIME  60.0                                                   float   [s] Actual exposure time
    GFATIME  60.0                                                   float   [s] GFA camera exposure time
    DELTARA  0.0                                                    float   [arcsec] Offset], right ascension, observer inp
    DELTADEC 0.0                                                    float   [arcsec] Offset], declination, observer input
    WHITESPT F                                                      bool    Telescope is at whitespot
    ZENITH   F                                                      bool    Telescope is at zenith
    SEANNEX  F                                                      bool    Telescope is at SE annex
    BEYONDP  F                                                      bool    Telescope is beyond pole
    FIDUCIAL off                                                    str     Fiducials status during observation
    BACKLIT  off                                                    str     Fibers are backlit if True
    AIRMASS  1.000057                                               float   Airmass
    FOCUS    1140.0,-480.0,690.3,-3.0,25.0,0.0                      str     Telescope focus settings
    TRUSTEMP 6.967                                                  float   [deg] Average Telescope truss temperature (only
    PMIRTEMP 5.0                                                    float   [deg] Average primary mirror temperature (nit,e
    PMREADY  T                                                      bool    Primary mirror ready
    PMCOVER  open                                                   str     Primary mirror cover
    PMCOOL   off                                                    str     Primary mirror cooling
    DOMSHUTU open                                                   str     Upper dome shutter
    DOMSHUTL open                                                   str     Lower dome shutter
    DOMLIGHH off                                                    str     High dome lights
    DOMLIGHL off                                                    str     Low dome lights
    DOMEAZ   106.495                                                float   [deg] Dome azimuth angle
    DOMINPOS T                                                      bool    Dome is in position
    EPOCH    2000.0                                                 float   Epoch of observation
    GUIDOFFR 0.0                                                    float   [arcsec] RA guider offset (cummulative, from TC
    GUIDOFFD -0.0                                                   float   [arcsec] DEC guider offset (cummulative, from T
    SUNRA    337.957105                                             float   [deg] Sun RA at start of exposure
    SUNDEC   -9.241851                                              float   [deg] Sun declination at start of exposure
    MOONDEC  14.950187                                              float   [deg] Moon declination at start of exposure
    MOONRA   36.900458                                              float   [deg] Moon RA at start of exposure
    MOONSEP  36.415                                                 float   [deg] Moon Separation
    SLEWTIME 0.543                                                  float   [s] Slew Time
    MOUNTAZ  269.404239                                             float   [deg] Mount azimuth angle
    MOUNTDEC 31.954914                                              float   [deg] Mount declination
    MOUNTEL  89.388961                                              float   [deg] Mount elevation angle
    MOUNTHA  0.720137                                               float   [deg] Mount hour angle
    INCTRL   T                                                      bool    DESI in control
    INPOS    T                                                      bool    Mount in position
    MNTOFFD  -0.0                                                   float   [arcsec] DEC mMount offset (GFAPROC pointing co
    MNTOFFR  -0.0                                                   float   [arcsec] RA mount offset (GFAPROC pointing corr
    PARALLAC 89.023058                                              float   [deg] Parallactic angle
    SKYDEC   31.954914                                              float   [deg] Telescope declination (pointing on sky)
    SKYRA    71.974937                                              float   [deg] Telescope right ascension (pointing on sk
    TARGTDEC 31.954914                                              float   [deg] Target declination (to TCS)
    TARGTRA  71.974937                                              float   [deg] Target right ascension (to TCS)
    TARGTAZ  269.404239                                             float   [deg] Target azimuth
    TARGTEL  89.388961                                              float   [deg] Target elevation
    TRGTOFFD 0.0                                                    float   [arcsec] Telescope target offset (dec)
    TRGTOFFR 0.0                                                    float   [arcsec] Telescope target offset (RA)
    ZD       0.611039                                               float   [deg] Telescope zenith distance
    TCSST    04:50:46.818                                           str     Local Sidereal time reported by TCS (HH:MM:SS)
    TCSMJD   60000.082691                                           float   MJD reported by TCS
    SEEING   None                                                   Unknown [arcsec] ETC/PM seeing
    TRANSPAR None                                                   Unknown ETC/PM transparency
    PMSEEING None                                                   Unknown [arcsec] PlateMaker GFAPROC seeing
    PMTRANSP None                                                   Unknown [%] PlateMaker GFAPROC transparency
    IMAGECAM G0,G2,G3,G5,G7,G8,F1,F4,F6,F9                          str     Image cameras used for this exposure
    REQADC   96.74,99.01                                            str     [deg] requested ADC angles
    ADCCORR  T                                                      bool    Correct pointing for ADC setting if True
    ADC1PHI  96.739876                                              float   [deg] ADC 1 angle
    ADC2PHI  99.009244                                              float   [deg] ADC 2 angle
    ADC1HOME F                                                      bool    ADC 1 at home position if True
    ADC2HOME F                                                      bool    ADC 2 at home position if True
    ADC1NREV -1.0                                                   float   ADC 1 number of revs
    ADC2NREV 0.0                                                    float   ADC 2 number of revs
    ADC1STAT STOPPED                                                str     ADC 1 status
    ADC2STAT STOPPED                                                str     ADC 2 status
    HEXPOS   1140.0,-480.0,690.3,-3.0,25.0,0.0                      str     Hexapod position
    HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                                str     Hexapod trim values
    ROTOFFST 0.0                                                    float   [arcsec] Rotator offset
    ROTENBLD F                                                      bool    Rotator enabled
    ROTRATE  0.0                                                    float   [arcsec/min] Rotator rate
    RESETROT T                                                      bool    DOS Control: reset hex rotator
    GUIDMODE catalog                                                str     Guider mode
    TDEWPNT  -8.03                                                  float   Telescope air dew point
    TAIRFLOW 0.0                                                    float   Telescope air flow
    TAIRITMP 6.6                                                    float   [deg] Telescope air in temperature
    TAIROTMP 5.7                                                    float   [deg] Telescope air out temperature
    TAIRTEMP 5.695                                                  float   [deg] Telescope air temperature
    TCASITMP 6.6                                                    float   [deg] Telescope Cass Cage in temperature
    TCASOTMP 5.7                                                    float   [deg] Telescope Cass Cage out temperature
    TCSITEMP 4.6                                                    float   [deg] Telescope center section in temperature
    TCSOTEMP 6.1                                                    float   [deg] Telescope center section out temperature
    TCIBTEMP 0.0                                                    float   [deg] Telescope chimney IB temperature
    TCIMTEMP 0.0                                                    float   [deg] Telescope chimney IM temperature
    TCITTEMP 0.0                                                    float   [deg] Telescope chimney IT temperature
    TCOSTEMP 0.0                                                    float   [deg] Telescope chimney OS temperature
    TCOWTEMP 0.0                                                    float   [deg] Telescope chimney OW temperature
    TDBTEMP  4.9                                                    float   [deg] Telescope dec bore temperature
    TFLOWIN  0.0                                                    float   Telescope flow rate in
    TFLOWOUT 0.0                                                    float   Telescope flow rate out
    TGLYCOLI 0.5                                                    float   [deg] Telescope glycol in temperature
    TGLYCOLO 0.9                                                    float   [deg] Telescope glycol out temperature
    THINGES  6.7                                                    float   [deg] Telescope hinge S temperature
    THINGEW  22.3                                                   float   [deg] Telescope hinge W temperature
    TPMAVERT 4.995                                                  float   [deg] Telescope mirror averagetemperature
    TPMDESIT 1.0                                                    float   [deg] Telescope mirror desired temperature
    TPMEIBT  5.0                                                    float   [deg] Telescope mirror EIB temperature
    TPMEITT  5.1                                                    float   [deg] Telescope mirror EIT temperature
    TPMEOBT  4.7                                                    float   [deg] Telescope mirror EOB temperature
    TPMEOTT  5.2                                                    float   [deg] Telescope mirror EOT temperature
    TPMNIBT  4.7                                                    float   [deg] Telescope mirror NIB temperature
    TPMNITT  5.0                                                    float   [deg] Telescope mirror NIT temperature
    TPMNOBT  4.6                                                    float   [deg] Telescope mirror NOB temperature
    TPMNOTT  5.0                                                    float   [deg] Telescope mirror NOT temperature
    TPMRTDT  5.01                                                   float   [deg] Telescope mirror RTD temperature
    TPMSIBT  5.0                                                    float   [deg] Telescope mirror SIB temperature
    TPMSITT  5.0                                                    float   [deg] Telescope mirror SIT temperature
    TPMSOBT  4.5                                                    float   [deg] Telescope mirror SOB temperature
    TPMSOTT  5.0                                                    float   [deg] Telescope mirror SOT temperature
    TPMSTAT  ready                                                  str     Telescope mirror status
    TPMWIBT  4.7                                                    float   [deg] Telescope mirror WIB temperature
    TPMWITT  4.9                                                    float   [deg] Telescope mirror WIT temperature
    TPMWOBT  4.2                                                    float   [deg] Telescope mirror WOB temperature
    TPMWOTT  4.8                                                    float   [deg] Telescope mirror WOT temperature
    TPCITEMP 4.0                                                    float   [deg] Telescope primary cell in temperature
    TPCOTEMP 4.1                                                    float   [deg] Telescope primary cell out temperature
    TPR1HUM  0.0                                                    float   Telescope probe 1 humidity
    TPR1TEMP 0.0                                                    float   [deg] Telescope probe1 temperature
    TPR2HUM  0.0                                                    float   Telescope probe 2 humidity
    TPR2TEMP 0.0                                                    float   [deg] Telescope probe2 temperature
    TSERVO   40.0                                                   float   Telescope servo setpoint
    TTRSTEMP 6.4                                                    float   [deg] Telescope top ring S temperature
    TTRWTEMP 6.4                                                    float   [deg] Telescope top ring W temperature
    TTRUETBT -9.6                                                   float   [deg] Telescope truss ETB temperature
    TTRUETTT 6.4                                                    float   [deg] Telescope truss ETT temperature
    TTRUNTBT 6.0                                                    float   [deg] Telescope truss NTB temperature
    TTRUNTTT 6.6                                                    float   [deg] Telescope truss NTT temperature
    TTRUSTBT 6.1                                                    float   [deg] Telescope truss STB temperature
    TTRUSTST 10.8                                                   float   [deg] Telescope truss STS temperature
    TTRUSTTT 6.2                                                    float   [deg] Telescope truss STT temperature
    TTRUTSBT 7.0                                                    float   [deg] Telescope truss TSB temperature
    TTRUTSMT 6.9                                                    float   [deg] Telescope truss TSM temperature
    TTRUTSTT 7.0                                                    float   [deg] Telescope truss TST temperature
    TTRUWTBT 5.8                                                    float   [deg] Telescope truss WTB temperature
    TTRUWTTT 6.6                                                    float   [deg] Telescope truss WTT temperature
    ALARM    F                                                      bool    UPS major alarm or check battery
    ALARM-ON F                                                      bool    UPS active alarm condition
    BATTERY  100.0                                                  float   [%] UPS Battery left
    SECLEFT  6138.0                                                 float   [s] UPS Seconds left
    UPSSTAT  System Normal - On Line(7)                             str     UPS Status
    INAMPS   67.8                                                   float   [A] UPS total input current
    OUTWATTS 5000.0,7000.0,4500.0                                   str     [W] UPS Phase A, B, C output watts
    COMPDEW  -0.5                                                   float   [deg C] Computer room dewpoint
    COMPHUM  18.5                                                   float   [%] Computer room humidity
    COMPAMB  18.4                                                   float   [deg C] Computer room ambient temperature
    COMPTEMP 25.1                                                   float   [deg C] Computer room hygrometer temperature
    DEWPOINT -9.7                                                   float   [deg C] (outside) dewpoint
    HUMIDITY 32.0                                                   float   [%] (outside) humidity
    PRESSURE 795.0                                                  float   [torr] (outside) air pressure
    OUTTEMP  5.8                                                    float   [deg C] outside temperature
    WINDDIR  133.4                                                  float   [deg] wind direction
    WINDSPD  21.3                                                   float   [m/s] wind speed
    GUST     19.0                                                   float   [m/s] Wind gusts speed
    AMNIENTN 13.6                                                   float   [deg C] ambient temperature north
    CFLOOR   4.9                                                    float   [deg C] temperature on C floor
    NWALLIN  13.8                                                   float   [deg C] temperature at north wall inside
    NWALLOUT 5.1                                                    float   [deg C] temperature at north wall outside
    WWALLIN  13.4                                                   float   [deg C] temperature at west wall inside
    WWALLOUT 5.7                                                    float   [deg C] temperature at west wall outside
    AMBIENTS 14.5                                                   float   [deg C] ambient temperature south
    FLOOR    11.9                                                   float   [deg C] temperature at floor (LCR)
    EWALLCMP 6.1                                                    float   [deg C] temperature at east wall, computer room
    EWALLCOU 5.7                                                    float   [deg C] temperature at east wall, Coude room
    ROOF     5.5                                                    float   [deg C] temperature on roof
    ROOFAMB  5.9                                                    float   [deg C] ambient temperature on roof
    DOMEBLOW 6.3                                                    float   [deg C] temperature at dome back, lower
    DOMEBUP  6.9                                                    float   [deg C] temperature at dome back, upper
    DOMELLOW 5.8                                                    float   [deg C] temperature at dome left, lower
    DOMELUP  5.8                                                    float   [deg C] temperature at dome left, upper
    DOMERLOW 6.2                                                    float   [deg C] temperature at dome right, lower
    DOMERUP  5.9                                                    float   [deg C] temperature at dome right, upper
    PLATFORM 5.7                                                    float   [deg C] temperature at platform
    SHACKC   15.2                                                   float   [deg C] temperature at shack ceiling
    SHACKW   14.2                                                   float   [deg C] temperature at shack wall
    STAIRSL  5.8                                                    float   [deg C] temperature at stairs, lower
    STAIRSM  5.6                                                    float   [deg C] temperature at stairs, mid
    STAIRSU  5.8                                                    float   [deg C] temperature at stairs, upper
    TELBASE  4.5                                                    float   [deg C] temperature at telescope base
    UTILWALL 6.4                                                    float   [deg C] temperature at utility room wall
    UTILROOM 6.3                                                    float   [deg C] temperature in utilitiy room
    RADESYS  FK5                                                    str     Coordinate reference frame of major/minor axes
    FILENAME /exposures/desi/20230224/00168807/gfa-00168807.fits.fz str     Name of (FI
    EXCLUDED                                                        str     Components excluded from this exposure
    DOSVER   trunk                                                  str     DOS software version
    OCSVER   1.2                                                    float   OCS software version
    CONSTVER DESI:CURRENT                                           str     Constants version
    INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini       str     DOS Configuration
    TCSKRA   0 0 0                                                  str     TCS Kalman (RA)
    TCSKDEC  0 0 0                                                  str     TCS Kalman (dec)
    TCSGRA   0.15                                                   float   TCS simple gain (RA)
    TCSGDEC  0.15                                                   float   TCS simple gain (dec)
    TCSMFRA  2                                                      int     TCS moving filter length (RA)
    TCSMFDEC 2                                                      int     TCS moving filter length (dec)
    TCSPIRA  1.0,0.0,0.0,0.0                                        str     TCS PI settings (P, I (gain, error window, satu
    TCSPIDEC 1.0,0.0,0.0,0.0                                        str     TCS PI settings (P, I (gain, error window, satu
    ROLE     GFAMAN                                                 str
    CHECKSUM TAHAV895TAEAT593                                       str     HDU checksum updated 2023-02-25T01:59:31
    DATASUM  306780459                                              str     data unit checksum updated 2023-02-25T01:59:31
    ======== ====================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 10]

HDU02
-----

EXTNAME = GUIDE0

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================================= ===== ===============================================
    KEY      Example Value                     Type  Comment
    ======== ================================= ===== ===============================================
    NAXIS1   8                                 int   width of table in bytes
    NAXIS2   1032                              int   number of rows in table
    BZERO    32768                             int   offset data range to that of unsigned short
    BSCALE   1                                 int   default scaling factor
    DEVICE   GUIDE0                            str   Device/controller name
    UNIT     0                                 int   Unit number/letter
    UNITTYPE GUIDE                             str   Image Sources/Component
    EXPID    168807                            int   Exposure number
    EXPFRAME 0                                 int   Frame number
    FRAMES   1                                 int   Number of Frames in Archive
    FLAVOR   SCIENCE                           str   Observation type
    SEQUENCE GFA                               str   OCS Sequence name
    OBJECT                                     str   Object name
    PROGRAM  Kickstart Focus Procedure         str   Program name
    NIGHT    20230224                          int   Observing night
    TIMESYS  UTC                               str   Time system used for date-obs
    DATE-OBS 2023-02-25T01:58:27.541024        str   [UTC] Observation data and start time
    TIME-OBS 01:58:27.541024                   str   [UTC] Observation start time
    MJD-OBS  60000.08226321                    float Modified Julian Date of observation
    OPENSHUT 2023-02-25T01:58:27.541024        str   [s] Time shutter opened
    ST       4:51:50.015                       str   Local Sidereal time at observation start (HH:MM
    EXPTIME  60.0                              float [s] Actual exposure time
    GFATIME  60.0                              float [s] GFA camera exposure time
    DELTARA  0.0                               float [arcsec] Offset], right ascension, observer inp
    DELTADEC 0.0                               float [arcsec] Offset], declination, observer input
    TRUSTEMP 6.967                             float [deg] Average Telescope truss temperature (only
    PMIRTEMP 5.0                               float [deg] Average primary mirror temperature (nit,e
    EQUINOX  2000.0                            float Equinox of selected coordinate reference frame
    MOUNTAZ  269.404239                        float [deg] Mount azimuth angle
    MOUNTDEC 31.954914                         float [deg] Mount declination
    MOUNTEL  89.388961                         float [deg] Mount elevation angle
    MOUNTHA  0.720137                          float [deg] Mount hour angle
    SKYDEC   31.954914                         float [deg] Telescope declination (pointing on sky)
    SKYRA    71.974937                         float [deg] Telescope right ascension (pointing on sk
    TARGTDEC 31.954914                         float [deg] Target declination (to TCS)
    TARGTRA  71.974937                         float [deg] Target right ascension (to TCS)
    HEXPOS   1140.0,-480.0,690.3,-3.0,25.0,0.0 str   Hexapod position
    WCSAXES  2                                 int
    RADESYS  FK5                               str   Coordinate reference frame of major/minor axes
    CTYPE1   RA---TAN                          str
    CTYPE2   DEC--TAN                          str
    CD1_1    -5.6435e-05                       float
    CD1_2    1.65e-05                          float
    CD2_1    1.7957e-05                        float
    CD2_2    5.1854e-05                        float
    CRPIX1   1024.1                            float
    CRPIX2   513.5                             float
    CRVAL1   71.5016                           float
    CRVAL2   30.4332                           float
    SHAPE    1032,2248                         str
    DTYPE    uint16                            str
    DOSVER   trunk                             str   DOS software version
    OVERSCAN 50                                int
    DEVICEID dev10                             str   GFA device id (serial number)
    GAMBNTT  11.71                             float [deg C] GFA ambient temperature
    GFPGAT   33.241                            float [deg C] GFA fpga temperature
    GFILTERT 11.675                            float [deg C] GFA filter temperature
    GCOLDTEC 11.838                            float [deg C] GFA cold Peltier temperature
    GHOTTEC  11.635                            float [deg C] GFA hot Peltier temperature
    GCCDTEMP 11.838                            float [deg C] GFA CCD temperature
    GCAMTEMP 11.675                            float [deg C] GFA camera temperature
    GCAMHUM  0.467                             float [%/100] GFA camera humidity
    GHUMID2  0.467                             float [%/100] GFA humidity sensor 2
    GHUMID3  0.0                               float [%/100]GFA humidity sensor 3
    GEXPMODE normal                            str   GFA readout mode (loop/normal)
    READOUT  OK                                str
    CHECKSUM gXJAiUJ8gUJAgUJ5                  str   HDU checksum updated 2023-02-25T01:59:31
    DATASUM  3489471984                        str   data unit checksum updated 2023-02-25T01:59:31
    ======== ================================= ===== ===============================================

Data: FITS image [int16 (compressed), 2248x1032]

HDU03
-----

EXTNAME = FOCUS9

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================================= ===== ===============================================
    KEY      Example Value                     Type  Comment
    ======== ================================= ===== ===============================================
    NAXIS1   8                                 int   width of table in bytes
    NAXIS2   1032                              int   number of rows in table
    BZERO    32768                             int   offset data range to that of unsigned short
    BSCALE   1                                 int   default scaling factor
    DEVICE   FOCUS9                            str   Device/controller name
    UNIT     9                                 int   Unit number/letter
    UNITTYPE FOCUS                             str   Image Sources/Component
    EXPID    168807                            int   Exposure number
    EXPFRAME 0                                 int   Frame number
    FRAMES   1                                 int   Number of Frames in Archive
    FLAVOR   SCIENCE                           str   Observation type
    SEQUENCE GFA                               str   OCS Sequence name
    OBJECT                                     str   Object name
    PROGRAM  Kickstart Focus Procedure         str   Program name
    NIGHT    20230224                          int   Observing night
    TIMESYS  UTC                               str   Time system used for date-obs
    DATE-OBS 2023-02-25T01:58:27.546749        str   [UTC] Observation data and start time
    TIME-OBS 01:58:27.546749                   str   [UTC] Observation start time
    MJD-OBS  60000.08226327                    float Modified Julian Date of observation
    OPENSHUT 2023-02-25T01:58:27.546749        str   [s] Time shutter opened
    ST       4:51:50.0253                      str   Local Sidereal time at observation start (HH:MM
    EXPTIME  60.0                              float [s] Actual exposure time
    GFATIME  60.0                              float [s] GFA camera exposure time
    DELTARA  0.0                               float [arcsec] Offset], right ascension, observer inp
    DELTADEC 0.0                               float [arcsec] Offset], declination, observer input
    TRUSTEMP 6.967                             float [deg] Average Telescope truss temperature (only
    PMIRTEMP 5.0                               float [deg] Average primary mirror temperature (nit,e
    EQUINOX  2000.0                            float Equinox of selected coordinate reference frame
    MOUNTAZ  269.404239                        float [deg] Mount azimuth angle
    MOUNTDEC 31.954914                         float [deg] Mount declination
    MOUNTEL  89.388961                         float [deg] Mount elevation angle
    MOUNTHA  0.720137                          float [deg] Mount hour angle
    SKYDEC   31.954914                         float [deg] Telescope declination (pointing on sky)
    SKYRA    71.974937                         float [deg] Telescope right ascension (pointing on sk
    TARGTDEC 31.954914                         float [deg] Target declination (to TCS)
    TARGTRA  71.974937                         float [deg] Target right ascension (to TCS)
    HEXPOS   1140.0,-480.0,690.3,-3.0,25.0,0.0 str   Hexapod position
    WCSAXES  2                                 int
    RADESYS  FK5                               str   Coordinate reference frame of major/minor axes
    CTYPE1   RA---TAN                          str
    CTYPE2   DEC--TAN                          str
    CD1_1    -5.6403e-05                       float
    CD1_2    -1.6591e-05                       float
    CD2_1    -1.8057e-05                       float
    CD2_2    5.1824e-05                        float
    CRPIX1   1024.5                            float
    CRPIX2   516.5                             float
    CRVAL1   72.6287                           float
    CRVAL2   30.4828                           float
    SHAPE    1032,2248                         str
    DTYPE    uint16                            str
    DOSVER   trunk                             str   DOS software version
    OVERSCAN 50                                int
    DEVICEID dev03                             str   GFA device id (serial number)
    GAMBNTT  11.6                              float [deg C] GFA ambient temperature
    GFPGAT   35.332                            float [deg C] GFA fpga temperature
    GFILTERT 11.67                             float [deg C] GFA filter temperature
    GCOLDTEC 11.849                            float [deg C] GFA cold Peltier temperature
    GHOTTEC  11.678                            float [deg C] GFA hot Peltier temperature
    GCCDTEMP 11.849                            float [deg C] GFA CCD temperature
    GCAMTEMP 11.67                             float [deg C] GFA camera temperature
    GCAMHUM  0.0                               float [%/100] GFA camera humidity
    GHUMID2  0.0                               float [%/100] GFA humidity sensor 2
    GHUMID3  0.0                               float [%/100]GFA humidity sensor 3
    GEXPMODE normal                            str   GFA readout mode (loop/normal)
    READOUT  OK                                str
    CHECKSUM dR8EfQ6DdQ6DdQ6D                  str   HDU checksum updated 2023-02-25T01:59:31
    DATASUM  56345574                          str   data unit checksum updated 2023-02-25T01:59:31
    ======== ================================= ===== ===============================================

Data: FITS image [int16 (compressed), 2248x1032]

HDU04
-----

EXTNAME = FOCUS1

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================================= ===== ===============================================
    KEY      Example Value                     Type  Comment
    ======== ================================= ===== ===============================================
    NAXIS1   8                                 int   width of table in bytes
    NAXIS2   1032                              int   number of rows in table
    BZERO    32768                             int   offset data range to that of unsigned short
    BSCALE   1                                 int   default scaling factor
    DEVICE   FOCUS1                            str   Device/controller name
    UNIT     1                                 int   Unit number/letter
    UNITTYPE FOCUS                             str   Image Sources/Component
    EXPID    168807                            int   Exposure number
    EXPFRAME 0                                 int   Frame number
    FRAMES   1                                 int   Number of Frames in Archive
    FLAVOR   SCIENCE                           str   Observation type
    SEQUENCE GFA                               str   OCS Sequence name
    OBJECT                                     str   Object name
    PROGRAM  Kickstart Focus Procedure         str   Program name
    NIGHT    20230224                          int   Observing night
    TIMESYS  UTC                               str   Time system used for date-obs
    DATE-OBS 2023-02-25T01:58:27.543959        str   [UTC] Observation data and start time
    TIME-OBS 01:58:27.543959                   str   [UTC] Observation start time
    MJD-OBS  60000.08226324                    float Modified Julian Date of observation
    OPENSHUT 2023-02-25T01:58:27.543959        str   [s] Time shutter opened
    ST       4:51:50.8273                      str   Local Sidereal time at observation start (HH:MM
    EXPTIME  60.0                              float [s] Actual exposure time
    GFATIME  60.0                              float [s] GFA camera exposure time
    DELTARA  0.0                               float [arcsec] Offset], right ascension, observer inp
    DELTADEC 0.0                               float [arcsec] Offset], declination, observer input
    TRUSTEMP 6.967                             float [deg] Average Telescope truss temperature (only
    PMIRTEMP 5.0                               float [deg] Average primary mirror temperature (nit,e
    EQUINOX  2000.0                            float Equinox of selected coordinate reference frame
    MOUNTAZ  269.404239                        float [deg] Mount azimuth angle
    MOUNTDEC 31.954914                         float [deg] Mount declination
    MOUNTEL  89.388961                         float [deg] Mount elevation angle
    MOUNTHA  0.720137                          float [deg] Mount hour angle
    SKYDEC   31.954914                         float [deg] Telescope declination (pointing on sky)
    SKYRA    71.974937                         float [deg] Telescope right ascension (pointing on sk
    TARGTDEC 31.954914                         float [deg] Target declination (to TCS)
    TARGTRA  71.974937                         float [deg] Target right ascension (to TCS)
    HEXPOS   1140.0,-480.0,690.3,-3.0,25.0,0.0 str   Hexapod position
    WCSAXES  2                                 int
    RADESYS  FK5                               str   Coordinate reference frame of major/minor axes
    CTYPE1   RA---TAN                          str
    CTYPE2   DEC--TAN                          str
    CD1_1    -3.5521e-05                       float
    CD1_2    4.3542e-05                        float
    CD2_1    4.7389e-05                        float
    CD2_2    3.2637e-05                        float
    CRPIX1   1024.5                            float
    CRPIX2   516.5                             float
    CRVAL1   70.5475                           float
    CRVAL2   30.9564                           float
    SHAPE    1032,2248                         str
    DTYPE    uint16                            str
    DOSVER   trunk                             str   DOS software version
    OVERSCAN 50                                int
    DEVICEID dev05                             str   GFA device id (serial number)
    GAMBNTT  11.707                            float [deg C] GFA ambient temperature
    GFPGAT   32.625                            float [deg C] GFA fpga temperature
    GFILTERT 11.712                            float [deg C] GFA filter temperature
    GCOLDTEC 12.07                             float [deg C] GFA cold Peltier temperature
    GHOTTEC  11.787                            float [deg C] GFA hot Peltier temperature
    GCCDTEMP 12.07                             float [deg C] GFA CCD temperature
    GCAMTEMP 11.712                            float [deg C] GFA camera temperature
    GCAMHUM  0.0                               float [%/100] GFA camera humidity
    GHUMID2  0.0                               float [%/100] GFA humidity sensor 2
    GHUMID3  0.0                               float [%/100]GFA humidity sensor 3
    GEXPMODE normal                            str   GFA readout mode (loop/normal)
    READOUT  OK                                str
    CHECKSUM JJAaLH1XJH8aJH8U                  str   HDU checksum updated 2023-02-25T01:59:32
    DATASUM  745303104                         str   data unit checksum updated 2023-02-25T01:59:32
    ======== ================================= ===== ===============================================

Data: FITS image [int16 (compressed), 2248x1032]

HDU05
-----

EXTNAME = FOCUS4

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================================= ===== ===============================================
    KEY      Example Value                     Type  Comment
    ======== ================================= ===== ===============================================
    NAXIS1   8                                 int   width of table in bytes
    NAXIS2   1032                              int   number of rows in table
    BZERO    32768                             int   offset data range to that of unsigned short
    BSCALE   1                                 int   default scaling factor
    DEVICE   FOCUS4                            str   Device/controller name
    UNIT     4                                 int   Unit number/letter
    UNITTYPE FOCUS                             str   Image Sources/Component
    EXPID    168807                            int   Exposure number
    EXPFRAME 0                                 int   Frame number
    FRAMES   1                                 int   Number of Frames in Archive
    FLAVOR   SCIENCE                           str   Observation type
    SEQUENCE GFA                               str   OCS Sequence name
    OBJECT                                     str   Object name
    PROGRAM  Kickstart Focus Procedure         str   Program name
    NIGHT    20230224                          int   Observing night
    TIMESYS  UTC                               str   Time system used for date-obs
    DATE-OBS 2023-02-25T01:58:27.546248        str   [UTC] Observation data and start time
    TIME-OBS 01:58:27.546248                   str   [UTC] Observation start time
    MJD-OBS  60000.08226327                    float Modified Julian Date of observation
    OPENSHUT 2023-02-25T01:58:27.546248        str   [s] Time shutter opened
    ST       4:51:50.1021                      str   Local Sidereal time at observation start (HH:MM
    EXPTIME  60.0                              float [s] Actual exposure time
    GFATIME  60.0                              float [s] GFA camera exposure time
    DELTARA  0.0                               float [arcsec] Offset], right ascension, observer inp
    DELTADEC 0.0                               float [arcsec] Offset], declination, observer input
    TRUSTEMP 6.967                             float [deg] Average Telescope truss temperature (only
    PMIRTEMP 5.0                               float [deg] Average primary mirror temperature (nit,e
    EQUINOX  2000.0                            float Equinox of selected coordinate reference frame
    MOUNTAZ  269.404239                        float [deg] Mount azimuth angle
    MOUNTDEC 31.954914                         float [deg] Mount declination
    MOUNTEL  89.388961                         float [deg] Mount elevation angle
    MOUNTHA  0.720137                          float [deg] Mount hour angle
    SKYDEC   31.954914                         float [deg] Telescope declination (pointing on sky)
    SKYRA    71.974937                         float [deg] Telescope right ascension (pointing on sk
    TARGTDEC 31.954914                         float [deg] Target declination (to TCS)
    TARGTRA  71.974937                         float [deg] Target right ascension (to TCS)
    HEXPOS   1140.0,-480.0,690.3,-3.0,25.0,0.0 str   Hexapod position
    WCSAXES  2                                 int
    RADESYS  FK5                               str   Coordinate reference frame of major/minor axes
    CTYPE1   RA---TAN                          str
    CTYPE2   DEC--TAN                          str
    CD1_1    5.6177e-05                        float
    CD1_2    1.7223e-05                        float
    CD2_1    1.8745e-05                        float
    CD2_2    -5.1616e-05                       float
    CRPIX1   1024.5                            float
    CRPIX2   516.5                             float
    CRVAL1   71.2999                           float
    CRVAL2   33.4235                           float
    SHAPE    1032,2248                         str
    DTYPE    uint16                            str
    DOSVER   trunk                             str   DOS software version
    OVERSCAN 50                                int
    DEVICEID dev07                             str   GFA device id (serial number)
    GAMBNTT  11.798                            float [deg C] GFA ambient temperature
    GFPGAT   33.364                            float [deg C] GFA fpga temperature
    GFILTERT 11.763                            float [deg C] GFA filter temperature
    GCOLDTEC 12.097                            float [deg C] GFA cold Peltier temperature
    GHOTTEC  11.827                            float [deg C] GFA hot Peltier temperature
    GCCDTEMP 12.097                            float [deg C] GFA CCD temperature
    GCAMTEMP 11.763                            float [deg C] GFA camera temperature
    GCAMHUM  0.0                               float [%/100] GFA camera humidity
    GHUMID2  0.0                               float [%/100] GFA humidity sensor 2
    GHUMID3  0.0                               float [%/100]GFA humidity sensor 3
    GEXPMODE normal                            str   GFA readout mode (loop/normal)
    READOUT  OK                                str
    CHECKSUM 78F898E578E578E5                  str   HDU checksum updated 2023-02-25T01:59:32
    DATASUM  874713498                         str   data unit checksum updated 2023-02-25T01:59:32
    ======== ================================= ===== ===============================================

Data: FITS image [int16 (compressed), 2248x1032]

HDU06
-----

EXTNAME = GUIDE3

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================================= ===== ===============================================
    KEY      Example Value                     Type  Comment
    ======== ================================= ===== ===============================================
    NAXIS1   8                                 int   width of table in bytes
    NAXIS2   1032                              int   number of rows in table
    BZERO    32768                             int   offset data range to that of unsigned short
    BSCALE   1                                 int   default scaling factor
    DEVICE   GUIDE3                            str   Device/controller name
    UNIT     3                                 int   Unit number/letter
    UNITTYPE GUIDE                             str   Image Sources/Component
    EXPID    168807                            int   Exposure number
    EXPFRAME 0                                 int   Frame number
    FRAMES   1                                 int   Number of Frames in Archive
    FLAVOR   SCIENCE                           str   Observation type
    SEQUENCE GFA                               str   OCS Sequence name
    OBJECT                                     str   Object name
    PROGRAM  Kickstart Focus Procedure         str   Program name
    NIGHT    20230224                          int   Observing night
    TIMESYS  UTC                               str   Time system used for date-obs
    DATE-OBS 2023-02-25T01:58:27.542072        str   [UTC] Observation data and start time
    TIME-OBS 01:58:27.542072                   str   [UTC] Observation start time
    MJD-OBS  60000.08226322                    float Modified Julian Date of observation
    OPENSHUT 2023-02-25T01:58:27.542072        str   [s] Time shutter opened
    ST       4:51:50.3575                      str   Local Sidereal time at observation start (HH:MM
    EXPTIME  60.0                              float [s] Actual exposure time
    GFATIME  60.0                              float [s] GFA camera exposure time
    DELTARA  0.0                               float [arcsec] Offset], right ascension, observer inp
    DELTADEC 0.0                               float [arcsec] Offset], declination, observer input
    TRUSTEMP 6.967                             float [deg] Average Telescope truss temperature (only
    PMIRTEMP 5.0                               float [deg] Average primary mirror temperature (nit,e
    EQUINOX  2000.0                            float Equinox of selected coordinate reference frame
    MOUNTAZ  269.404239                        float [deg] Mount azimuth angle
    MOUNTDEC 31.954914                         float [deg] Mount declination
    MOUNTEL  89.388961                         float [deg] Mount elevation angle
    MOUNTHA  0.720137                          float [deg] Mount hour angle
    SKYDEC   31.954914                         float [deg] Telescope declination (pointing on sky)
    SKYRA    71.974937                         float [deg] Telescope right ascension (pointing on sk
    TARGTDEC 31.954914                         float [deg] Target declination (to TCS)
    TARGTRA  71.974937                         float [deg] Target right ascension (to TCS)
    HEXPOS   1140.0,-480.0,690.3,-3.0,25.0,0.0 str   Hexapod position
    WCSAXES  2                                 int
    RADESYS  FK5                               str   Coordinate reference frame of major/minor axes
    CTYPE1   RA---TAN                          str
    CTYPE2   DEC--TAN                          str
    CD1_1    3.403e-05                         float
    CD1_2    4.4534e-05                        float
    CD2_1    4.8469e-05                        float
    CD2_2    -3.1267e-05                       float
    CRPIX1   1004.23                           float
    CRPIX2   503.43                            float
    CRVAL1   70.4043                           float
    CRVAL2   32.8036                           float
    SHAPE    1032,2248                         str
    DTYPE    uint16                            str
    DOSVER   trunk                             str   DOS software version
    OVERSCAN 50                                int
    DEVICEID dev02                             str   GFA device id (serial number)
    GAMBNTT  11.838                            float [deg C] GFA ambient temperature
    GFPGAT   34.84                             float [deg C] GFA fpga temperature
    GFILTERT 11.793                            float [deg C] GFA filter temperature
    GCOLDTEC 11.99                             float [deg C] GFA cold Peltier temperature
    GHOTTEC  11.907                            float [deg C] GFA hot Peltier temperature
    GCCDTEMP 11.99                             float [deg C] GFA CCD temperature
    GCAMTEMP 11.793                            float [deg C] GFA camera temperature
    GCAMHUM  0.0                               float [%/100] GFA camera humidity
    GHUMID2  0.0                               float [%/100] GFA humidity sensor 2
    GHUMID3  0.0                               float [%/100]GFA humidity sensor 3
    GEXPMODE normal                            str   GFA readout mode (loop/normal)
    READOUT  OK                                str
    CHECKSUM 3NGeAMEc5MEcAMEc                  str   HDU checksum updated 2023-02-25T01:59:32
    DATASUM  4112356301                        str   data unit checksum updated 2023-02-25T01:59:32
    ======== ================================= ===== ===============================================

Data: FITS image [int16 (compressed), 2248x1032]

HDU07
-----

EXTNAME = GUIDE7

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================================= ===== ===============================================
    KEY      Example Value                     Type  Comment
    ======== ================================= ===== ===============================================
    NAXIS1   8                                 int   width of table in bytes
    NAXIS2   1032                              int   number of rows in table
    BZERO    32768                             int   offset data range to that of unsigned short
    BSCALE   1                                 int   default scaling factor
    DEVICE   GUIDE7                            str   Device/controller name
    UNIT     7                                 int   Unit number/letter
    UNITTYPE GUIDE                             str   Image Sources/Component
    EXPID    168807                            int   Exposure number
    EXPFRAME 0                                 int   Frame number
    FRAMES   1                                 int   Number of Frames in Archive
    FLAVOR   SCIENCE                           str   Observation type
    SEQUENCE GFA                               str   OCS Sequence name
    OBJECT                                     str   Object name
    PROGRAM  Kickstart Focus Procedure         str   Program name
    NIGHT    20230224                          int   Observing night
    TIMESYS  UTC                               str   Time system used for date-obs
    DATE-OBS 2023-02-25T01:58:27.546379        str   [UTC] Observation data and start time
    TIME-OBS 01:58:27.546379                   str   [UTC] Observation start time
    MJD-OBS  60000.08226327                    float Modified Julian Date of observation
    OPENSHUT 2023-02-25T01:58:27.546379        str   [s] Time shutter opened
    ST       4:51:50.0216                      str   Local Sidereal time at observation start (HH:MM
    EXPTIME  60.0                              float [s] Actual exposure time
    GFATIME  60.0                              float [s] GFA camera exposure time
    DELTARA  0.0                               float [arcsec] Offset], right ascension, observer inp
    DELTADEC 0.0                               float [arcsec] Offset], declination, observer input
    TRUSTEMP 6.967                             float [deg] Average Telescope truss temperature (only
    PMIRTEMP 5.0                               float [deg] Average primary mirror temperature (nit,e
    EQUINOX  2000.0                            float Equinox of selected coordinate reference frame
    MOUNTAZ  269.404239                        float [deg] Mount azimuth angle
    MOUNTDEC 31.954914                         float [deg] Mount declination
    MOUNTEL  89.388961                         float [deg] Mount elevation angle
    MOUNTHA  0.720137                          float [deg] Mount hour angle
    SKYDEC   31.954914                         float [deg] Telescope declination (pointing on sky)
    SKYRA    71.974937                         float [deg] Telescope right ascension (pointing on sk
    TARGTDEC 31.954914                         float [deg] Target declination (to TCS)
    TARGTRA  71.974937                         float [deg] Target right ascension (to TCS)
    HEXPOS   1140.0,-480.0,690.3,-3.0,25.0,0.0 str   Hexapod position
    WCSAXES  2                                 int
    RADESYS  FK5                               str   Coordinate reference frame of major/minor axes
    CTYPE1   RA---TAN                          str
    CTYPE2   DEC--TAN                          str
    CD1_1    -9.1428e-07                       float
    CD1_2    -5.4407e-05                       float
    CD2_1    -5.9215e-05                       float
    CD2_2    8.4006e-07                        float
    CRPIX1   1031.43                           float
    CRPIX2   503.9                             float
    CRVAL1   73.8298                           float
    CRVAL2   32.0231                           float
    SHAPE    1032,2248                         str
    DTYPE    uint16                            str
    DOSVER   trunk                             str   DOS software version
    OVERSCAN 50                                int
    DEVICEID dev01                             str   GFA device id (serial number)
    GAMBNTT  11.493                            float [deg C] GFA ambient temperature
    GFPGAT   32.133                            float [deg C] GFA fpga temperature
    GFILTERT -45.0                             float [deg C] GFA filter temperature
    GCOLDTEC 11.803                            float [deg C] GFA cold Peltier temperature
    GHOTTEC  11.638                            float [deg C] GFA hot Peltier temperature
    GCCDTEMP 11.803                            float [deg C] GFA CCD temperature
    GCAMTEMP -45.0                             float [deg C] GFA camera temperature
    GCAMHUM  0.0                               float [%/100] GFA camera humidity
    GHUMID2  0.0                               float [%/100] GFA humidity sensor 2
    GHUMID3  0.0                               float [%/100]GFA humidity sensor 3
    GEXPMODE normal                            str   GFA readout mode (loop/normal)
    READOUT  OK                                str
    CHECKSUM NhPkNhNjNhNjNhNj                  str   HDU checksum updated 2023-02-25T01:59:32
    DATASUM  1863549263                        str   data unit checksum updated 2023-02-25T01:59:32
    ======== ================================= ===== ===============================================

Data: FITS image [int16 (compressed), 2248x1032]

HDU08
-----

EXTNAME = GUIDE5

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================================= ===== ===============================================
    KEY      Example Value                     Type  Comment
    ======== ================================= ===== ===============================================
    NAXIS1   8                                 int   width of table in bytes
    NAXIS2   1032                              int   number of rows in table
    BZERO    32768                             int   offset data range to that of unsigned short
    BSCALE   1                                 int   default scaling factor
    DEVICE   GUIDE5                            str   Device/controller name
    UNIT     5                                 int   Unit number/letter
    UNITTYPE GUIDE                             str   Image Sources/Component
    EXPID    168807                            int   Exposure number
    EXPFRAME 0                                 int   Frame number
    FRAMES   1                                 int   Number of Frames in Archive
    FLAVOR   SCIENCE                           str   Observation type
    SEQUENCE GFA                               str   OCS Sequence name
    OBJECT                                     str   Object name
    PROGRAM  Kickstart Focus Procedure         str   Program name
    NIGHT    20230224                          int   Observing night
    TIMESYS  UTC                               str   Time system used for date-obs
    DATE-OBS 2023-02-25T01:58:27.542201        str   [UTC] Observation data and start time
    TIME-OBS 01:58:27.542201                   str   [UTC] Observation start time
    MJD-OBS  60000.08226322                    float Modified Julian Date of observation
    OPENSHUT 2023-02-25T01:58:27.542201        str   [s] Time shutter opened
    ST       4:51:50.0184                      str   Local Sidereal time at observation start (HH:MM
    EXPTIME  60.0                              float [s] Actual exposure time
    GFATIME  60.0                              float [s] GFA camera exposure time
    DELTARA  0.0                               float [arcsec] Offset], right ascension, observer inp
    DELTADEC 0.0                               float [arcsec] Offset], declination, observer input
    TRUSTEMP 6.967                             float [deg] Average Telescope truss temperature (only
    PMIRTEMP 5.0                               float [deg] Average primary mirror temperature (nit,e
    EQUINOX  2000.0                            float Equinox of selected coordinate reference frame
    MOUNTAZ  269.404239                        float [deg] Mount azimuth angle
    MOUNTDEC 31.954914                         float [deg] Mount declination
    MOUNTEL  89.388961                         float [deg] Mount elevation angle
    MOUNTHA  0.720137                          float [deg] Mount hour angle
    SKYDEC   31.954914                         float [deg] Telescope declination (pointing on sky)
    SKYRA    71.974937                         float [deg] Telescope right ascension (pointing on sk
    TARGTDEC 31.954914                         float [deg] Target declination (to TCS)
    TARGTRA  71.974937                         float [deg] Target right ascension (to TCS)
    HEXPOS   1140.0,-480.0,690.3,-3.0,25.0,0.0 str   Hexapod position
    WCSAXES  2                                 int
    RADESYS  FK5                               str   Coordinate reference frame of major/minor axes
    CTYPE1   RA---TAN                          str
    CTYPE2   DEC--TAN                          str
    CD1_1    5.6271e-05                        float
    CD1_2    -1.6963e-05                       float
    CD2_1    -1.8461e-05                       float
    CD2_2    -5.1702e-05                       float
    CRPIX1   1019.63                           float
    CRPIX2   507.57                            float
    CRVAL1   72.4643                           float
    CRVAL2   33.4748                           float
    SHAPE    1032,2248                         str
    DTYPE    uint16                            str
    DOSVER   trunk                             str   DOS software version
    OVERSCAN 50                                int
    DEVICEID dev08                             str   GFA device id (serial number)
    GAMBNTT  11.771                            float [deg C] GFA ambient temperature
    GFPGAT   33.61                             float [deg C] GFA fpga temperature
    GFILTERT 11.763                            float [deg C] GFA filter temperature
    GCOLDTEC 12.02                             float [deg C] GFA cold Peltier temperature
    GHOTTEC  11.803                            float [deg C] GFA hot Peltier temperature
    GCCDTEMP 12.02                             float [deg C] GFA CCD temperature
    GCAMTEMP 11.763                            float [deg C] GFA camera temperature
    GCAMHUM  0.0                               float [%/100] GFA camera humidity
    GHUMID2  0.0                               float [%/100] GFA humidity sensor 2
    GHUMID3  0.0                               float [%/100]GFA humidity sensor 3
    GEXPMODE normal                            str   GFA readout mode (loop/normal)
    READOUT  OK                                str
    CHECKSUM oeaCqdYCodaCodWC                  str   HDU checksum updated 2023-02-25T01:59:32
    DATASUM  2464151765                        str   data unit checksum updated 2023-02-25T01:59:32
    ======== ================================= ===== ===============================================

Data: FITS image [int16 (compressed), 2248x1032]

HDU09
-----

EXTNAME = GUIDE2

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================================= ===== ===============================================
    KEY      Example Value                     Type  Comment
    ======== ================================= ===== ===============================================
    NAXIS1   8                                 int   width of table in bytes
    NAXIS2   1032                              int   number of rows in table
    BZERO    32768                             int   offset data range to that of unsigned short
    BSCALE   1                                 int   default scaling factor
    DEVICE   GUIDE2                            str   Device/controller name
    UNIT     2                                 int   Unit number/letter
    UNITTYPE GUIDE                             str   Image Sources/Component
    EXPID    168807                            int   Exposure number
    EXPFRAME 0                                 int   Frame number
    FRAMES   1                                 int   Number of Frames in Archive
    FLAVOR   SCIENCE                           str   Observation type
    SEQUENCE GFA                               str   OCS Sequence name
    OBJECT                                     str   Object name
    PROGRAM  Kickstart Focus Procedure         str   Program name
    NIGHT    20230224                          int   Observing night
    TIMESYS  UTC                               str   Time system used for date-obs
    DATE-OBS 2023-02-25T01:58:27.543003        str   [UTC] Observation data and start time
    TIME-OBS 01:58:27.543003                   str   [UTC] Observation start time
    MJD-OBS  60000.08226323                    float Modified Julian Date of observation
    OPENSHUT 2023-02-25T01:58:27.543003        str   [s] Time shutter opened
    ST       4:51:50.1039                      str   Local Sidereal time at observation start (HH:MM
    EXPTIME  60.0                              float [s] Actual exposure time
    GFATIME  60.0                              float [s] GFA camera exposure time
    DELTARA  0.0                               float [arcsec] Offset], right ascension, observer inp
    DELTADEC 0.0                               float [arcsec] Offset], declination, observer input
    TRUSTEMP 6.967                             float [deg] Average Telescope truss temperature (only
    PMIRTEMP 5.0                               float [deg] Average primary mirror temperature (nit,e
    EQUINOX  2000.0                            float Equinox of selected coordinate reference frame
    MOUNTAZ  269.404239                        float [deg] Mount azimuth angle
    MOUNTDEC 31.954914                         float [deg] Mount declination
    MOUNTEL  89.388961                         float [deg] Mount elevation angle
    MOUNTHA  0.720137                          float [deg] Mount hour angle
    SKYDEC   31.954914                         float [deg] Telescope declination (pointing on sky)
    SKYRA    71.974937                         float [deg] Telescope right ascension (pointing on sk
    TARGTDEC 31.954914                         float [deg] Target declination (to TCS)
    TARGTRA  71.974937                         float [deg] Target right ascension (to TCS)
    HEXPOS   1140.0,-480.0,690.3,-3.0,25.0,0.0 str   Hexapod position
    WCSAXES  2                                 int
    RADESYS  FK5                               str   Coordinate reference frame of major/minor axes
    CTYPE1   RA---TAN                          str
    CTYPE2   DEC--TAN                          str
    CD1_1    -1.1129e-06                       float
    CD1_2    5.4405e-05                        float
    CD2_1    5.9213e-05                        float
    CD2_2    1.0225e-06                        float
    CRPIX1   1020.17                           float
    CRPIX2   504.83                            float
    CRVAL1   70.1233                           float
    CRVAL2   31.8598                           float
    SHAPE    1032,2248                         str
    DTYPE    uint16                            str
    DOSVER   trunk                             str   DOS software version
    OVERSCAN 50                                int
    DEVICEID dev06                             str   GFA device id (serial number)
    GAMBNTT  11.771                            float [deg C] GFA ambient temperature
    GFPGAT   33.979                            float [deg C] GFA fpga temperature
    GFILTERT 11.83                             float [deg C] GFA filter temperature
    GCOLDTEC 11.979                            float [deg C] GFA cold Peltier temperature
    GHOTTEC  11.915                            float [deg C] GFA hot Peltier temperature
    GCCDTEMP 11.979                            float [deg C] GFA CCD temperature
    GCAMTEMP 11.83                             float [deg C] GFA camera temperature
    GCAMHUM  0.0                               float [%/100] GFA camera humidity
    GHUMID2  0.0                               float [%/100] GFA humidity sensor 2
    GHUMID3  0.0                               float [%/100]GFA humidity sensor 3
    GEXPMODE normal                            str   GFA readout mode (loop/normal)
    READOUT  OK                                str
    CHECKSUM 7O3i7M0Z7M0f7M0Z                  str   HDU checksum updated 2023-02-25T01:59:32
    DATASUM  3563886804                        str   data unit checksum updated 2023-02-25T01:59:32
    ======== ================================= ===== ===============================================

Data: FITS image [int16 (compressed), 2248x1032]

HDU10
-----

EXTNAME = FOCUS6

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================================= ===== ===============================================
    KEY      Example Value                     Type  Comment
    ======== ================================= ===== ===============================================
    NAXIS1   8                                 int   width of table in bytes
    NAXIS2   1032                              int   number of rows in table
    BZERO    32768                             int   offset data range to that of unsigned short
    BSCALE   1                                 int   default scaling factor
    DEVICE   FOCUS6                            str   Device/controller name
    UNIT     6                                 int   Unit number/letter
    UNITTYPE FOCUS                             str   Image Sources/Component
    EXPID    168807                            int   Exposure number
    EXPFRAME 0                                 int   Frame number
    FRAMES   1                                 int   Number of Frames in Archive
    FLAVOR   SCIENCE                           str   Observation type
    SEQUENCE GFA                               str   OCS Sequence name
    OBJECT                                     str   Object name
    PROGRAM  Kickstart Focus Procedure         str   Program name
    NIGHT    20230224                          int   Observing night
    TIMESYS  UTC                               str   Time system used for date-obs
    DATE-OBS 2023-02-25T01:58:27.544487        str   [UTC] Observation data and start time
    TIME-OBS 01:58:27.544487                   str   [UTC] Observation start time
    MJD-OBS  60000.08226325                    float Modified Julian Date of observation
    OPENSHUT 2023-02-25T01:58:27.544487        str   [s] Time shutter opened
    ST       4:51:50.1179                      str   Local Sidereal time at observation start (HH:MM
    EXPTIME  60.0                              float [s] Actual exposure time
    GFATIME  60.0                              float [s] GFA camera exposure time
    DELTARA  0.0                               float [arcsec] Offset], right ascension, observer inp
    DELTADEC 0.0                               float [arcsec] Offset], declination, observer input
    TRUSTEMP 6.967                             float [deg] Average Telescope truss temperature (only
    PMIRTEMP 5.0                               float [deg] Average primary mirror temperature (nit,e
    EQUINOX  2000.0                            float Equinox of selected coordinate reference frame
    MOUNTAZ  269.404239                        float [deg] Mount azimuth angle
    MOUNTDEC 31.954914                         float [deg] Mount declination
    MOUNTEL  89.388961                         float [deg] Mount elevation angle
    MOUNTHA  0.720137                          float [deg] Mount hour angle
    SKYDEC   31.954914                         float [deg] Telescope declination (pointing on sky)
    SKYRA    71.974937                         float [deg] Telescope right ascension (pointing on sk
    TARGTDEC 31.954914                         float [deg] Target declination (to TCS)
    TARGTRA  71.974937                         float [deg] Target right ascension (to TCS)
    HEXPOS   1140.0,-480.0,690.3,-3.0,25.0,0.0 str   Hexapod position
    WCSAXES  2                                 int
    RADESYS  FK5                               str   Coordinate reference frame of major/minor axes
    CTYPE1   RA---TAN                          str
    CTYPE2   DEC--TAN                          str
    CD1_1    3.4242e-05                        float
    CD1_2    -4.4396e-05                       float
    CD2_1    -4.8319e-05                       float
    CD2_2    -3.1462e-05                       float
    CRPIX1   1024.5                            float
    CRPIX2   516.5                             float
    CRVAL1   73.4335                           float
    CRVAL2   32.937                            float
    SHAPE    1032,2248                         str
    DTYPE    uint16                            str
    DOSVER   trunk                             str   DOS software version
    OVERSCAN 50                                int
    DEVICEID dev13                             str   GFA device id (serial number)
    GAMBNTT  11.707                            float [deg C] GFA ambient temperature
    GFPGAT   33.733                            float [deg C] GFA fpga temperature
    GFILTERT 11.664                            float [deg C] GFA filter temperature
    GCOLDTEC 11.942                            float [deg C] GFA cold Peltier temperature
    GHOTTEC  11.744                            float [deg C] GFA hot Peltier temperature
    GCCDTEMP 11.942                            float [deg C] GFA CCD temperature
    GCAMTEMP 11.664                            float [deg C] GFA camera temperature
    GCAMHUM  2.87                              float [%/100] GFA camera humidity
    GHUMID2  2.87                              float [%/100] GFA humidity sensor 2
    GHUMID3  0.0                               float [%/100]GFA humidity sensor 3
    GEXPMODE normal                            str   GFA readout mode (loop/normal)
    READOUT  OK                                str
    CHECKSUM 9oYA9mY59mYA9mY5                  str   HDU checksum updated 2023-02-25T01:59:32
    DATASUM  1254217566                        str   data unit checksum updated 2023-02-25T01:59:32
    ======== ================================= ===== ===============================================

Data: FITS image [int16 (compressed), 2248x1032]

HDU11
-----

EXTNAME = GUIDE8

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================================= ===== ===============================================
    KEY      Example Value                     Type  Comment
    ======== ================================= ===== ===============================================
    NAXIS1   8                                 int   width of table in bytes
    NAXIS2   1032                              int   number of rows in table
    BZERO    32768                             int   offset data range to that of unsigned short
    BSCALE   1                                 int   default scaling factor
    DEVICE   GUIDE8                            str   Device/controller name
    UNIT     8                                 int   Unit number/letter
    UNITTYPE GUIDE                             str   Image Sources/Component
    EXPID    168807                            int   Exposure number
    EXPFRAME 0                                 int   Frame number
    FRAMES   1                                 int   Number of Frames in Archive
    FLAVOR   SCIENCE                           str   Observation type
    SEQUENCE GFA                               str   OCS Sequence name
    OBJECT                                     str   Object name
    PROGRAM  Kickstart Focus Procedure         str   Program name
    NIGHT    20230224                          int   Observing night
    TIMESYS  UTC                               str   Time system used for date-obs
    DATE-OBS 2023-02-25T01:58:27.544653        str   [UTC] Observation data and start time
    TIME-OBS 01:58:27.544653                   str   [UTC] Observation start time
    MJD-OBS  60000.08226325                    float Modified Julian Date of observation
    OPENSHUT 2023-02-25T01:58:27.544653        str   [s] Time shutter opened
    ST       4:51:50.1118                      str   Local Sidereal time at observation start (HH:MM
    EXPTIME  60.0                              float [s] Actual exposure time
    GFATIME  60.0                              float [s] GFA camera exposure time
    DELTARA  0.0                               float [arcsec] Offset], right ascension, observer inp
    DELTADEC 0.0                               float [arcsec] Offset], declination, observer input
    TRUSTEMP 6.967                             float [deg] Average Telescope truss temperature (only
    PMIRTEMP 5.0                               float [deg] Average primary mirror temperature (nit,e
    EQUINOX  2000.0                            float Equinox of selected coordinate reference frame
    MOUNTAZ  269.404239                        float [deg] Mount azimuth angle
    MOUNTDEC 31.954914                         float [deg] Mount declination
    MOUNTEL  89.388961                         float [deg] Mount elevation angle
    MOUNTHA  0.720137                          float [deg] Mount hour angle
    SKYDEC   31.954914                         float [deg] Telescope declination (pointing on sky)
    SKYRA    71.974937                         float [deg] Telescope right ascension (pointing on sk
    TARGTDEC 31.954914                         float [deg] Target declination (to TCS)
    TARGTRA  71.974937                         float [deg] Target right ascension (to TCS)
    HEXPOS   1140.0,-480.0,690.3,-3.0,25.0,0.0 str   Hexapod position
    WCSAXES  2                                 int
    RADESYS  FK5                               str   Coordinate reference frame of major/minor axes
    CTYPE1   RA---TAN                          str
    CTYPE2   DEC--TAN                          str
    CD1_1    -3.5408e-05                       float
    CD1_2    -4.3618e-05                       float
    CD2_1    -4.7472e-05                       float
    CD2_2    3.2533e-05                        float
    CRPIX1   1036.7                            float
    CRPIX2   522.17                            float
    CRVAL1   73.5165                           float
    CRVAL2   31.0872                           float
    SHAPE    1032,2248                         str
    DTYPE    uint16                            str
    DOSVER   trunk                             str   DOS software version
    OVERSCAN 50                                int
    DEVICEID dev04                             str   GFA device id (serial number)
    GAMBNTT  11.531                            float [deg C] GFA ambient temperature
    GFPGAT   33.856                            float [deg C] GFA fpga temperature
    GFILTERT 11.464                            float [deg C] GFA filter temperature
    GCOLDTEC 11.79                             float [deg C] GFA cold Peltier temperature
    GHOTTEC  11.52                             float [deg C] GFA hot Peltier temperature
    GCCDTEMP 11.79                             float [deg C] GFA CCD temperature
    GCAMTEMP 11.464                            float [deg C] GFA camera temperature
    GCAMHUM  2.313                             float [%/100] GFA camera humidity
    GHUMID2  2.313                             float [%/100] GFA humidity sensor 2
    GHUMID3  0.0                               float [%/100]GFA humidity sensor 3
    GEXPMODE normal                            str   GFA readout mode (loop/normal)
    READOUT  OK                                str
    CHECKSUM fgachdUbfdabfdUb                  str   HDU checksum updated 2023-02-25T01:59:32
    DATASUM  2242340315                        str   data unit checksum updated 2023-02-25T01:59:32
    ======== ================================= ===== ===============================================

Data: FITS image [int16 (compressed), 2248x1032]


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
