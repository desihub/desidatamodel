=========
sky-EXPID
=========

:Summary: Raw data from the two DESI Sky Cameras, with one fpack-compressed HDU for each camera.
:Naming Convention: ``sky-EXPID.fits.fz``, where EXPID is the zero-padded
    8-digit exposure ID.
:Regex: ``sky-[0-9]{8}\.fits\.fz``
:File Type: FITS, 70 MB

Contents
========

====== ========== ================= =========================
Number EXTNAME    Type              Contents
====== ========== ================= =========================
HDU0_  SKY        Empty HDU         Header keywords only
HDU1_  SKYCAM1    Compressed IMAGE  Sky camera frames
HDU2_  SKYCAM1T   BINTABLE          Metadata about each frame
HDU3_  SKYCAM0    Compressed IMAGE  Sky camera frames
HDU4_  SKYCAM0T   BINTABLE          Metadata about each frame
====== ========== ================= =========================

The SKYCAMERA data will be 3D[nframes, ny, nx] such that
``data[i]`` is the 2D sky camera frame number ``i``.  Row ``i`` of the
SKYCAM[01]T table will contain the metadata about that frame, *e.g.* the
DATE-OBS and EXPTIME.

FITS Header Units
=================

HDU0
----

EXTNAME = SKY

This HDU contains header keywords only.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ====================================================== ======= ===============================================
    KEY      Example Value                                          Type    Comment
    ======== ====================================================== ======= ===============================================
    MODULE   SKY                                                    str     Image Sources/Component
    EXPID    118526                                                 int     Exposure number
    FRAMES   7                                                      int     Number of Frames in Archive
    TILEID   4403                                                   int     DESI Tile ID
    FLAVOR   science                                                str     Observation type
    PURPOSE  Main Survey                                            str     Purpose of observing night
    PROGRAM  DARK                                                   str     Program name
    NIGHT    20220113                                               int     Observing night
    ACQTIME  None                                                   Unknown [s] acqusition image exposure time
    GUIDTIME None                                                   Unknown [s] guider GFA exposure time
    FOCSTIME None                                                   Unknown [s] focus GFA exposure time
    SKYTIME  60.0                                                   float   [s] sky camera exposure time (acquisition)
    REQRA    170.239                                                float   [deg] Requested right ascension (observer input
    REQDEC   -7.093                                                 float   [deg] Requested declination (observer input)
    DELTARA  None                                                   Unknown [arcsec] Offset], right ascension, observer inp
    DELTADEC None                                                   Unknown [arcsec] Offset], declination, observer input
    FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                     str     Telescope focus settings
    TRUSTEMP 12.267                                                 float   [deg] Average Telescope truss temperature (only
    PMIRTEMP 11.675                                                 float   [deg] Average primary mirror temperature (nit,e
    SKYDEC   -7.102329                                              float   [deg] Telescope declination (pointing on sky)
    SKYRA    170.24163                                              float   [deg] Telescope right ascension (pointing on sk
    TARGTDEC -7.102329                                              float   [deg] Target declination (to TCS)
    TARGTRA  170.24163                                              float   [deg] Target right ascension (to TCS)
    ACQCAM   GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8              str     Acquisition cameras used
    GUIDECAM GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8              str     Guide cameras used for t
    FOCUSCAM FOCUS1,FOCUS4,FOCUS6,FOCUS9                            str     Focus cameras used for this exposure
    SKYCAM   SKYCAM0,SKYCAM1                                        str     Sky cameras used for this exposure
    ADC1PHI  None                                                   Unknown [deg] ADC 1 angle
    ADC2PHI  None                                                   Unknown [deg] ADC 2 angle
    HEXPOS   None                                                   Unknown Hexapod position
    DOSVER   trunk                                                  str     DOS software version
    CONSTVER DESI:CURRENT                                           str     Constants version
    ARCHIVE  /exposures/desi/20220113/00118526/sky-00118526.fits.fz str
    CHECKSUM 1m7R3m7P1m7P1m7P                                       str     HDU checksum updated 2022-01-14T11:14:08
    DATASUM           0                                             str     data unit checksum updated 2022-01-14T11:14:08
    ======== ====================================================== ======= ===============================================

Empty HDU.

HDU1
----

EXTNAME = SKYCAM1

Contains the raw data from multiple exposures of SkyCam1, normally taken concurrently with a DESI spectrograph exposure.
Each raw image contains spots from the ETC fibers whose total flux is a measure of relative sky brightness in the r band.
Use the ``desietc.sky`` module to reduce these images and measure sky fiber fluxes.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ==================================================== ======= ===============================================
    KEY      Example Value                                        Type    Comment
    ======== ==================================================== ======= ===============================================
    NAXIS1   8                                                    int     width of table in bytes
    NAXIS2   14329                                                int     number of rows in table
    ZTILE3   1                                                    int     size of tiles to be compressed
    BZERO    32768                                                int     offset data range to that of unsigned short
    BSCALE   1                                                    int     default scaling factor
    EXPID    118526                                               int     Exposure number
    FRAMES   7                                                    int     Number of Frames in Archive
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
    DATE-OBS 2022-01-14T11:04:17.933414                           str     [UTC] Observation data and start time
    MJD-OBS  59593.46131867                                       float   Modified Julian Date of observation
    ST       11:14:42.9462                                        str     Local Sidereal time at observation start (HH:MM
    SKYTIME  60.0                                                 float   [s] sky camera exposure time (acquisition)
    REQRA    170.239                                              float   [deg] Requested right ascension (observer input
    REQDEC   -7.093                                               float   [deg] Requested declination (observer input)
    DELTARA  None                                                 Unknown [arcsec] Offset], right ascension, observer inp
    DELTADEC None                                                 Unknown [arcsec] Offset], declination, observer input
    FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                   str     Telescope focus settings
    TRUSTEMP 12.267                                               float   [deg] Average Telescope truss temperature (only
    PMIRTEMP 11.675                                               float   [deg] Average primary mirror temperature (nit,e
    EPOCH    2000.0                                               float   Epoch of observation
    EQUINOX  None                                                 Unknown Equinox of selected coordinate reference frame
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
    HEXPOS   None                                                 Unknown Hexapod position
    HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                              str     Hexapod trim values
    USEROTAT T                                                    bool    DOS Control: use rotator
    ROTOFFST 138.8                                                float   [arcsec] Rotator offset
    ROTENBLD T                                                    bool    Rotator enabled
    ROTRATE  0.513                                                float   [arcsec/min] Rotator rate
    USEGUIDR T                                                    bool    DOS Control: use guider
    USEDONUT T                                                    bool    DOS Control: use donuts
    RADESYS  FK5                                                  str     Coordinate reference frame of major/minor axes
    SHAPE    2047,3072                                            str
    DOSVER   trunk                                                str     DOS software version
    OCSVER   1.2                                                  float   OCS software version
    CONSTVER DESI:CURRENT                                         str     Constants version
    INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
    ADCPHI2  None                                                 Unknown
    ROI      None                                                 Unknown
    ROIWIDTH None                                                 Unknown
    GEXPMODE None                                                 Unknown GFA readout mode (loop/normal)
    DEVICEID None                                                 Unknown GFA device id (serial number)
    REQTIME  1860.0                                               float   [s] Requested exposure time
    CHECKSUM CPA0EN50CNA0CN30                                     str     HDU checksum updated 2022-01-14T11:14:08
    DATASUM  4223421838                                           str     data unit checksum updated 2022-01-14T11:14:08
    ======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 3072x2047x7]

HDU2
----

EXTNAME = SKYCAM1T

A table of timestamps and instrument parameters for each SkyCam0 exposure stored in HDU SKYCAM1.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   144              int  width of table in bytes
    NAXIS2   7                int  number of rows in table
    CHECKSUM S14XT04US04US04U str  HDU checksum updated 2022-01-14T11:14:08
    DATASUM  136958306        str  data unit checksum updated 2022-01-14T11:14:08
    ======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

============ ======== ===== ===================
Name         Type     Units Description
============ ======== ===== ===================
EXPTIME      float64        label for field   0
REQTIME [1]_ float64        label for field   1
NIGHT        int64          label for field   2
DATE-OBS     char[26]       label for field   3
TIME-OBS     char[15]       label for field   4
MJD-OBS      float64        label for field   5
OPENSHUT     char[*]        label for field   6
ST           char[*]        label for field   7
HEXPOS       char[4]        label for field   8
GAMBNTT      char[4]        label for field   9
GFPGAT       char[4]        label for field  10
GFILTERT     char[4]        label for field  11
GCOLDTEC     char[4]        label for field  12
GHOTTEC      char[4]        label for field  13
GCCDTEMP     char[4]        label for field  14
GCAMTEMP     char[4]        label for field  15
GHUMID2      char[4]        label for field  16
GHUMID3      char[4]        label for field  17
============ ======== ===== ===================

.. [1] Optional

HDU3
----

EXTNAME = SKYCAM0

Contains the raw data from multiple exposures of SkyCam0, normally taken concurrently with a DESI spectrograph exposure.
Each raw image contains spots from the ETC fibers whose total flux is a measure of relative sky brightness in the r band.
Use the ``desietc.sky`` module to reduce these images and measure sky fiber fluxes.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ==================================================== ======= ===============================================
    KEY      Example Value                                        Type    Comment
    ======== ==================================================== ======= ===============================================
    NAXIS1   8                                                    int     width of table in bytes
    NAXIS2   14329                                                int     number of rows in table
    ZTILE3   1                                                    int     size of tiles to be compressed
    BZERO    32768                                                int     offset data range to that of unsigned short
    BSCALE   1                                                    int     default scaling factor
    EXPID    118526                                               int     Exposure number
    FRAMES   7                                                    int     Number of Frames in Archive
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
    DATE-OBS 2022-01-14T11:04:17.933414                           str     [UTC] Observation data and start time
    MJD-OBS  59593.46131867                                       float   Modified Julian Date of observation
    ST       11:14:42.9462                                        str     Local Sidereal time at observation start (HH:MM
    SKYTIME  60.0                                                 float   [s] sky camera exposure time (acquisition)
    REQRA    170.239                                              float   [deg] Requested right ascension (observer input
    REQDEC   -7.093                                               float   [deg] Requested declination (observer input)
    DELTARA  None                                                 Unknown [arcsec] Offset], right ascension, observer inp
    DELTADEC None                                                 Unknown [arcsec] Offset], declination, observer input
    FOCUS    946.6,-231.6,-83.4,-18.3,9.8,139.4                   str     Telescope focus settings
    TRUSTEMP 12.267                                               float   [deg] Average Telescope truss temperature (only
    PMIRTEMP 11.675                                               float   [deg] Average primary mirror temperature (nit,e
    EPOCH    2000.0                                               float   Epoch of observation
    EQUINOX  None                                                 Unknown Equinox of selected coordinate reference frame
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
    HEXPOS   None                                                 Unknown Hexapod position
    HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                              str     Hexapod trim values
    USEROTAT T                                                    bool    DOS Control: use rotator
    ROTOFFST 138.8                                                float   [arcsec] Rotator offset
    ROTENBLD T                                                    bool    Rotator enabled
    ROTRATE  0.513                                                float   [arcsec/min] Rotator rate
    USEGUIDR T                                                    bool    DOS Control: use guider
    USEDONUT T                                                    bool    DOS Control: use donuts
    RADESYS  FK5                                                  str     Coordinate reference frame of major/minor axes
    SHAPE    2047,3072                                            str
    DOSVER   trunk                                                str     DOS software version
    OCSVER   1.2                                                  float   OCS software version
    CONSTVER DESI:CURRENT                                         str     Constants version
    INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini     str     DOS Configuration
    ADCPHI2  None                                                 Unknown
    ROI      None                                                 Unknown
    ROIWIDTH None                                                 Unknown
    GEXPMODE None                                                 Unknown GFA readout mode (loop/normal)
    DEVICEID None                                                 Unknown GFA device id (serial number)
    REQTIME  1860.0                                               float   [s] Requested exposure time
    CHECKSUM SLfNTKfKSKfKSKfK                                     str     HDU checksum updated 2022-01-14T11:14:09
    DATASUM  4278834758                                           str     data unit checksum updated 2022-01-14T11:14:09
    ======== ==================================================== ======= ===============================================

Data: FITS image [int16 (compressed), 3072x2047x7]

HDU4
----

EXTNAME = SKYCAM0T

A table of timestamps and instrument parameters for each SkyCam0 exposure stored in HDU SKYCAM0.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   144              int  width of table in bytes
    NAXIS2   7                int  number of rows in table
    CHECKSUM dFIceCHbdCHbdCHb str  HDU checksum updated 2022-01-14T11:14:09
    DATASUM  3066928412       str  data unit checksum updated 2022-01-14T11:14:09
    ======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

============ ======== ===== ===================
Name         Type     Units Description
============ ======== ===== ===================
EXPTIME      float64        label for field   0
REQTIME [1]_ float64        label for field   1
NIGHT        int64          label for field   2
DATE-OBS     char[26]       label for field   3
TIME-OBS     char[15]       label for field   4
MJD-OBS      float64        label for field   5
OPENSHUT     char[*]        label for field   6
ST           char[*]        label for field   7
HEXPOS       char[4]        label for field   8
GAMBNTT      char[4]        label for field   9
GFPGAT       char[4]        label for field  10
GFILTERT     char[4]        label for field  11
GCOLDTEC     char[4]        label for field  12
GHOTTEC      char[4]        label for field  13
GCCDTEMP     char[4]        label for field  14
GCAMTEMP     char[4]        label for field  15
GHUMID2      char[4]        label for field  16
GHUMID3      char[4]        label for field  17
============ ======== ===== ===================
