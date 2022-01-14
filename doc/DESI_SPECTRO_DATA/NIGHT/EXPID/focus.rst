=====
focus
=====

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``focus-00118526.fits.fz``, where ... *Give a human readable
    description of the filename, e.g. ``blat-{EXPID}`` where ``{EXPID}``
    is the 8-digit exposure ID.*
:Regex: ``focus-00118526.fits.fz`` *Give a regular expression for this filename.
    For example, a six-digit number would correspond to ``[0-9]{6}``.*
:File Type: FITS, 91 MB  *This section gives the type of the file
    and its approximate size.*

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_  FOCUS   IMAGE    *Brief Description*
HDU1_  FOCUS4  BINTABLE *Brief Description*
HDU2_  FOCUS4T BINTABLE *Brief Description*
HDU3_  FOCUS1  BINTABLE *Brief Description*
HDU4_  FOCUS1T BINTABLE *Brief Description*
HDU5_  FOCUS9  BINTABLE *Brief Description*
HDU6_  FOCUS9T BINTABLE *Brief Description*
HDU7_  FOCUS6  BINTABLE *Brief Description*
HDU8_  FOCUS6T BINTABLE *Brief Description*
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = FOCUS

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================================================== ======= ===============================================
KEY      Example Value                                            Type    Comment
======== ======================================================== ======= ===============================================
MODULE   FOCUS                                                    str     Image Sources/Component
EXPID    118526                                                   int     Exposure number
FRAMES   9                                                        int     Number of Frames in Archive
TILEID   4403                                                     int     DESI Tile ID
FLAVOR   science                                                  str     Observation type
PURPOSE  Main Survey                                              str     Purpose of observing night
PROGRAM  DARK                                                     str     Program name
NIGHT    20220113                                                 int     Observing night
ACQTIME  None                                                     Unknown [s] acqusition image exposure time
GUIDTIME None                                                     Unknown [s] guider GFA exposure time
FOCSTIME 60.0                                                     float   [s] focus GFA exposure time
SKYTIME  None                                                     Unknown [s] sky camera exposure time (acquisition)
REQRA    170.239                                                  float   [deg] Requested right ascension (observer input
REQDEC   -7.093                                                   float   [deg] Requested declination (observer input)
DELTARA  0.0                                                      float   [arcsec] Offset], right ascension, observer inp
DELTADEC 0.0                                                      float   [arcsec] Offset], declination, observer input
FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                       str     Telescope focus settings
TRUSTEMP 12.267                                                   float   [deg] Average Telescope truss temperature (only
PMIRTEMP 11.675                                                   float   [deg] Average primary mirror temperature (nit,e
SKYDEC   -7.102329                                                float   [deg] Telescope declination (pointing on sky)
SKYRA    170.24163                                                float   [deg] Telescope right ascension (pointing on sk
TARGTDEC -7.102329                                                float   [deg] Target declination (to TCS)
TARGTRA  170.24163                                                float   [deg] Target right ascension (to TCS)
ACQCAM   GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                str     Acquisition cameras used
GUIDECAM GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                str     Guide cameras used for t
FOCUSCAM FOCUS1,FOCUS4,FOCUS6,FOCUS9                              str     Focus cameras used for this exposure
SKYCAM   SKYCAM0,SKYCAM1                                          str     Sky cameras used for this exposure
ADC1PHI  None                                                     Unknown [deg] ADC 1 angle
ADC2PHI  None                                                     Unknown [deg] ADC 2 angle
HEXPOS   946.7,-231.6,-83.4,-18.3,9.9,138.8                       str     Hexapod position
DOSVER   trunk                                                    str     DOS software version
CONSTVER DESI:CURRENT                                             str     Constants version
ARCHIVE  /exposures/desi/20220113/00118526/focus-00118526.fits.fz str
CHECKSUM FAA2H992FAA2F772                                         str     HDU checksum updated 2022-01-14T11:13:59
DATASUM           0                                               str     data unit checksum updated 2022-01-14T11:13:59
======== ======================================================== ======= ===============================================

Empty HDU.

HDU1
----

EXTNAME = FOCUS4

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   9288                                                 int     number of rows in table
ZTILE3   1                                                    int     size of tiles to be compressed
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
DEVICE   FOCUS4                                               str     Device/controller name
UNIT     4                                                    int     Unit number/letter
UNITTYPE FOCUS                                                str     Image Sources/Component
EXPID    118526                                               int     Exposure number
FRAMES   9                                                    int     Number of Frames in Archive
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
DATE-OBS 2022-01-14T11:03:58.542861                           str     [UTC] Observation data and start time
MJD-OBS  59593.46109425                                       float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:03:58.542861                           str     Time shutter opened
ST       11:14:12.2376                                        str     Local Sidereal time at observation start (HH:MM
FOCSTIME 60.0                                                 float   [s] focus GFA exposure time
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
CD1_1    5.6335e-05                                           float
CD1_2    1.6773e-05                                           float
CD2_1    1.8252e-05                                           float
CD2_2    -5.1774e-05                                          float
SHAPE    1032,2248                                            str
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
ADCPHI2  None                                                 Unknown
ROI      None                                                 Unknown
ROIWIDTH None                                                 Unknown
GEXPMODE normal                                               str     GFA readout mode (loop/normal)
DEVICEID dev07                                                str     GFA device id (serial number)
REQTIME  1860.0                                               float   [s] Requested exposure time
CHECKSUM 4hDA7hAA4hAA4hAA                                     str     HDU checksum updated 2022-01-14T11:13:59
DATASUM  1294762993                                           str     data unit checksum updated 2022-01-14T11:13:59
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 2248x1032x9]

HDU2
----

EXTNAME = FOCUS4T

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   242              int  width of table in bytes
NAXIS2   9                int  number of rows in table
CHECKSUM RNb1SLa0RLa0RLa0 str  HDU checksum updated 2022-01-14T11:13:59
DATASUM  1194419227       str  data unit checksum updated 2022-01-14T11:13:59
======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

======== ======== ===== ===================
Name     Type     Units Description
======== ======== ===== ===================
EXPTIME  float64        label for field   1
NIGHT    int64          label for field   2
DATE-OBS char[26]       label for field   3
TIME-OBS char[15]       label for field   4
MJD-OBS  float64        label for field   5
OPENSHUT char[26]       label for field   6
ST       char[13]       label for field   7
HEXPOS   char[34]       label for field   8
GAMBNTT  float64        label for field   9
GFPGAT   float64        label for field  10
GFILTERT float64        label for field  11
GCOLDTEC float64        label for field  12
GHOTTEC  float64        label for field  13
GCCDTEMP float64        label for field  14
GCAMTEMP float64        label for field  15
GHUMID2  float64        label for field  16
GHUMID3  float64        label for field  17
CRPIX1   float64        label for field  18
CRPIX2   float64        label for field  19
CRVAL1   float64        label for field  20
CRVAL2   float64        label for field  21
======== ======== ===== ===================

HDU3
----

EXTNAME = FOCUS1

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   9288                                                 int     number of rows in table
ZTILE3   1                                                    int     size of tiles to be compressed
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
DEVICE   FOCUS1                                               str     Device/controller name
UNIT     1                                                    int     Unit number/letter
UNITTYPE FOCUS                                                str     Image Sources/Component
EXPID    118526                                               int     Exposure number
FRAMES   9                                                    int     Number of Frames in Archive
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
DATE-OBS 2022-01-14T11:03:58.542861                           str     [UTC] Observation data and start time
MJD-OBS  59593.46109425                                       float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:03:58.542861                           str     Time shutter opened
ST       11:14:12.2376                                        str     Local Sidereal time at observation start (HH:MM
FOCSTIME 60.0                                                 float   [s] focus GFA exposure time
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
CD1_1    -3.4711e-05                                          float
CD1_2    4.4105e-05                                           float
CD2_1    4.8013e-05                                           float
CD2_2    3.1893e-05                                           float
SHAPE    1032,2248                                            str
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
ADCPHI2  None                                                 Unknown
ROI      None                                                 Unknown
ROIWIDTH None                                                 Unknown
GEXPMODE normal                                               str     GFA readout mode (loop/normal)
DEVICEID dev05                                                str     GFA device id (serial number)
REQTIME  1860.0                                               float   [s] Requested exposure time
CHECKSUM 4NNh7NNg4NNg4NNg                                     str     HDU checksum updated 2022-01-14T11:13:59
DATASUM  3152869116                                           str     data unit checksum updated 2022-01-14T11:13:59
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 2248x1032x9]

HDU4
----

EXTNAME = FOCUS1T

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   242              int  width of table in bytes
NAXIS2   9                int  number of rows in table
CHECKSUM jaafmSWfjYafjYUf str  HDU checksum updated 2022-01-14T11:13:59
DATASUM  626101938        str  data unit checksum updated 2022-01-14T11:13:59
======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

======== ======== ===== ===================
Name     Type     Units Description
======== ======== ===== ===================
EXPTIME  float64        label for field   1
NIGHT    int64          label for field   2
DATE-OBS char[26]       label for field   3
TIME-OBS char[15]       label for field   4
MJD-OBS  float64        label for field   5
OPENSHUT char[26]       label for field   6
ST       char[13]       label for field   7
HEXPOS   char[34]       label for field   8
GAMBNTT  float64        label for field   9
GFPGAT   float64        label for field  10
GFILTERT float64        label for field  11
GCOLDTEC float64        label for field  12
GHOTTEC  float64        label for field  13
GCCDTEMP float64        label for field  14
GCAMTEMP float64        label for field  15
GHUMID2  float64        label for field  16
GHUMID3  float64        label for field  17
CRPIX1   float64        label for field  18
CRPIX2   float64        label for field  19
CRVAL1   float64        label for field  20
CRVAL2   float64        label for field  21
======== ======== ===== ===================

HDU5
----

EXTNAME = FOCUS9

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   9288                                                 int     number of rows in table
ZTILE3   1                                                    int     size of tiles to be compressed
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
DEVICE   FOCUS9                                               str     Device/controller name
UNIT     9                                                    int     Unit number/letter
UNITTYPE FOCUS                                                str     Image Sources/Component
EXPID    118526                                               int     Exposure number
FRAMES   9                                                    int     Number of Frames in Archive
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
DATE-OBS 2022-01-14T11:03:58.542861                           str     [UTC] Observation data and start time
MJD-OBS  59593.46109425                                       float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:03:58.542861                           str     Time shutter opened
ST       11:14:12.2376                                        str     Local Sidereal time at observation start (HH:MM
FOCSTIME 60.0                                                 float   [s] focus GFA exposure time
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
CD1_1    -5.6317e-05                                          float
CD1_2    -1.6905e-05                                          float
CD2_1    -1.8398e-05                                          float
CD2_2    5.1751e-05                                           float
SHAPE    1032,2248                                            str
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
ADCPHI2  None                                                 Unknown
ROI      None                                                 Unknown
ROIWIDTH None                                                 Unknown
GEXPMODE normal                                               str     GFA readout mode (loop/normal)
DEVICEID dev03                                                str     GFA device id (serial number)
REQTIME  1860.0                                               float   [s] Requested exposure time
CHECKSUM gjaCgjZBgjaBgjWB                                     str     HDU checksum updated 2022-01-14T11:13:59
DATASUM  1001490193                                           str     data unit checksum updated 2022-01-14T11:13:59
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 2248x1032x9]

HDU6
----

EXTNAME = FOCUS9T

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   242              int  width of table in bytes
NAXIS2   9                int  number of rows in table
CHECKSUM 79AXA97X79AXA97X str  HDU checksum updated 2022-01-14T11:14:00
DATASUM  2395983219       str  data unit checksum updated 2022-01-14T11:14:00
======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

======== ======== ===== ===================
Name     Type     Units Description
======== ======== ===== ===================
EXPTIME  float64        label for field   1
NIGHT    int64          label for field   2
DATE-OBS char[26]       label for field   3
TIME-OBS char[15]       label for field   4
MJD-OBS  float64        label for field   5
OPENSHUT char[26]       label for field   6
ST       char[13]       label for field   7
HEXPOS   char[34]       label for field   8
GAMBNTT  float64        label for field   9
GFPGAT   float64        label for field  10
GFILTERT float64        label for field  11
GCOLDTEC float64        label for field  12
GHOTTEC  float64        label for field  13
GCCDTEMP float64        label for field  14
GCAMTEMP float64        label for field  15
GHUMID2  float64        label for field  16
GHUMID3  float64        label for field  17
CRPIX1   float64        label for field  18
CRPIX2   float64        label for field  19
CRVAL1   float64        label for field  20
CRVAL2   float64        label for field  21
======== ======== ===== ===================

HDU7
----

EXTNAME = FOCUS6

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================================================== ======= ===============================================
KEY      Example Value                                        Type    Comment
======== ==================================================== ======= ===============================================
NAXIS1   8                                                    int     width of table in bytes
NAXIS2   9288                                                 int     number of rows in table
ZTILE3   1                                                    int     size of tiles to be compressed
BZERO    32768                                                int     offset data range to that of unsigned short
BSCALE   1                                                    int     default scaling factor
DEVICE   FOCUS6                                               str     Device/controller name
UNIT     6                                                    int     Unit number/letter
UNITTYPE FOCUS                                                str     Image Sources/Component
EXPID    118526                                               int     Exposure number
FRAMES   9                                                    int     Number of Frames in Archive
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
DATE-OBS 2022-01-14T11:03:58.542861                           str     [UTC] Observation data and start time
MJD-OBS  59593.46109425                                       float   Modified Julian Date of observation
OPENSHUT 2022-01-14T11:03:58.542861                           str     Time shutter opened
ST       11:14:12.2376                                        str     Local Sidereal time at observation start (HH:MM
FOCSTIME 60.0                                                 float   [s] focus GFA exposure time
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
CD1_1    3.496e-05                                            float
CD1_2    -4.3929e-05                                          float
CD2_1    -4.782e-05                                           float
CD2_2    -3.2123e-05                                          float
SHAPE    1032,2248                                            str
DOSVER   trunk                                                str     DOS software version
OCSVER   1.2                                                  float   OCS software version
CONSTVER DESI:CURRENT                                         str     Constants version
INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
ADCPHI2  None                                                 Unknown
ROI      None                                                 Unknown
ROIWIDTH None                                                 Unknown
GEXPMODE normal                                               str     GFA readout mode (loop/normal)
DEVICEID dev13                                                str     GFA device id (serial number)
REQTIME  1860.0                                               float   [s] Requested exposure time
CHECKSUM Uf34ac13Vc13ac13                                     str     HDU checksum updated 2022-01-14T11:14:00
DATASUM  1884870740                                           str     data unit checksum updated 2022-01-14T11:14:00
======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 2248x1032x9]

HDU8
----

EXTNAME = FOCUS6T

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   242              int  width of table in bytes
NAXIS2   9                int  number of rows in table
CHECKSUM K2DmK0BjK0BjK0Bj str  HDU checksum updated 2022-01-14T11:14:00
DATASUM  2998174015       str  data unit checksum updated 2022-01-14T11:14:00
======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

======== ======== ===== ===================
Name     Type     Units Description
======== ======== ===== ===================
EXPTIME  float64        label for field   1
NIGHT    int64          label for field   2
DATE-OBS char[26]       label for field   3
TIME-OBS char[15]       label for field   4
MJD-OBS  float64        label for field   5
OPENSHUT char[26]       label for field   6
ST       char[13]       label for field   7
HEXPOS   char[34]       label for field   8
GAMBNTT  float64        label for field   9
GFPGAT   float64        label for field  10
GFILTERT float64        label for field  11
GCOLDTEC float64        label for field  12
GHOTTEC  float64        label for field  13
GCCDTEMP float64        label for field  14
GCAMTEMP float64        label for field  15
GHUMID2  float64        label for field  16
GHUMID3  float64        label for field  17
CRPIX1   float64        label for field  18
CRPIX2   float64        label for field  19
CRVAL1   float64        label for field  20
CRVAL2   float64        label for field  21
======== ======== ===== ===================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
