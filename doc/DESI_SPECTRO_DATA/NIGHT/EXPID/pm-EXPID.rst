========
pm-EXPID
========

:Summary: PlateMaker data.
:Naming Convention: ``pm-EXPID.fits``, where EXPID is the zero-padded
    8-digit exposure ID.
:Regex: ``pm-[0-9]{8}\.fits``
:File Type: FITS, 1 MB

Contents
========

====== ======== ======== ===================
Number EXTNAME  Type     Contents
====== ======== ======== ===================
HDU0_  PM       IMAGE    Header Keywords
HDU1_  PMGSTARS BINTABLE *Brief Description*
HDU2_  PMGWCS   BINTABLE *Brief Description*
HDU3_  PMFIDPOS BINTABLE *Brief Description*
HDU4_  PMPOSPOS BINTABLE *Brief Description*
HDU5_  PMCNTPOS BINTABLE *Brief Description*
HDU6_  PMFIBMAP BINTABLE *Brief Description*
====== ======== ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = PM

The data contents are a dummy payload that should not be used. The most important
header keywords are:

* ``CENTER``: Apparent telescope coordinates needed to place field center at center of the focal plane.
* ``GCENTER``: Pointing corrections after computing astrometric solution.
* ``GHEXROT``: Absolute hexapod rotation and rate after computing astrometric solution. Rate is not used.
* ``PMNFSADC``: Absolute ADC angles.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ============================================================= ===== ===============================================
    KEY      Example Value                                                 Type  Comment
    ======== ============================================================= ===== ===============================================
    NAXIS1   1                                                             int   length of data axis 1
    DEVICE   GUIDE8                                                        str   Device/controller name
    UNIT     8                                                             int   Unit number/letter
    UNITTYPE GUIDE                                                         str   Image Sources/Component
    MODULE   GUIDE                                                         str   Image Sources/Component
    EXPID    182039                                                        int   Exposure number
    EXPFRAME 0                                                             int   Frame number
    FRAMES   1                                                             int   Number of Frames in Archive
    TILEID   4361                                                          int   DESI Tile ID
    FIBASSGN /data/tiles/SVN_tiles/004/fiberassign-004361.fits.gz          str   Fiber assign
    FLAVOR   SCIENCE                                                       str   Observation type
    SEQUENCE DESI                                                          str   OCS Sequence name
    OBJECT   start_loop                                                    str   Object name
    PURPOSE  Main Survey                                                   str   Purpose of observing night
    PROGRAM  DARK                                                          str   Program name
    PROPID   2020B-5000                                                    str   Proposal ID
    OBSERVER Rodrigo Calderon, Khaled Said                                 str   Names of observers
    LEAD     Martin Landriau                                               str   Lead observer
    INSTRUME DESI                                                          str   Instrument name
    OBSERVAT KPNO                                                          str   Observatory name
    OBS-LAT  31.96403                                                      str   [deg] Observatory latitude
    OBS-LONG -111.59989                                                    str   [deg] Observatory east longitude
    OBS-ELEV 2097.0                                                        float [m] Observatory elevation
    TELESCOP KPNO 4.0-m telescope                                          str   Telescope name
    CORRCTOR DESI Corrector                                                str   Corrector Identification
    NIGHT    20230524                                                      int   Observing night
    TIMESYS  UTC                                                           str   Time system used for date-obs
    DATE-OBS 2023-05-25T08:34:19.830256                                    str   [UTC] Observation data and start time
    TIME-OBS 08:34:19.830256                                               str   [UTC] Observation start time
    MJD-OBS  60089.35717396                                                float Modified Julian Date of observation
    OPENSHUT 2023-05-25T08:34:19.830256                                    str   [s] Time shutter opened
    ST       17:18:55.6097                                                 str   Local Sidereal time at observation start (HH:MM
    EXPTIME  15.0                                                          float [s] Actual exposure time
    ACQTIME  15.0                                                          float [s] acqusition image exposure time
    REQRA    244.33                                                        float [deg] Requested right ascension (observer input
    REQDEC   15.297                                                        float [deg] Requested declination (observer input)
    FOCUS    1331.8,-319.4,-468.0,-11.5,32.4,174.9                         str   Telescope focus settings
    TRUSTEMP 15.633                                                        float [deg] Average Telescope truss temperature (only
    PMIRTEMP 15.188                                                        float [deg] Average primary mirror temperature (nit,e
    EPOCH    2000.0                                                        float Epoch of observation
    EQUINOX  2000.0                                                        float Equinox of selected coordinate reference frame
    MOUNTAZ  223.47215                                                     float [deg] Mount azimuth angle
    MOUNTDEC 15.29368                                                      float [deg] Mount declination
    MOUNTEL  68.266626                                                     float [deg] Mount elevation angle
    MOUNTHA  15.314189                                                     float [deg] Mount hour angle
    SKYDEC   15.29368                                                      float [deg] Telescope declination (pointing on sky)
    SKYRA    244.327071                                                    float [deg] Telescope right ascension (pointing on sk
    TARGTDEC 15.29368                                                      float [deg] Target declination (to TCS)
    TARGTRA  244.327071                                                    float [deg] Target right ascension (to TCS)
    USEETC   T                                                             bool  ETC data available if true
    ACQCAM   GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                     str   Acquisition cameras used
    GUIDECAM GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                     str   Guide cameras used for t
    FOCUSCAM FOCUS1,FOCUS4,FOCUS6,FOCUS9                                   str   Focus cameras used for this exposure
    SKYCAM   SKYCAM0,SKYCAM1                                               str   Sky cameras used for this exposure
    USESKY   T                                                             bool  DOS Control: use Sky Monitor
    USEFOCUS T                                                             bool  DOS Control: use focus
    HEXPOS   1331.8,-319.4,-468.0,-11.5,32.4,174.9                         str   Hexapod position
    USEGUIDR T                                                             bool  DOS Control: use guider
    USEDONUT T                                                             bool  DOS Control: use donuts
    WCSAXES  2                                                             int
    RADESYS  FK5                                                           str   Coordinate reference frame of major/minor axes
    CTYPE1   RA---TAN                                                      str
    CTYPE2   DEC--TAN                                                      str
    CD1_1    -3.521e-05                                                    float
    CD1_2    -4.3757e-05                                                   float
    CD2_1    -4.7625e-05                                                   float
    CD2_2    3.235e-05                                                     float
    CRPIX1   1036.7                                                        float
    CRPIX2   522.17                                                        float
    CRVAL1   245.6899                                                      float
    CRVAL2   14.4297                                                       float
    TNFSPROC 8.9117                                                        float [s] PlateMaker NFSPROC processing time
    TGFAPROC 5.0955                                                        float [s] PlateMaker GFAPROC processing time
    FILENAME /exposures/desi/20230524/00182039/guide-00182039-0000.fits.fz str   Name
    SHAPE    1032,2248                                                     str
    DTYPE    uint16                                                        str
    DOSVER   trunk                                                         str   DOS software version
    OCSVER   1.2                                                           float OCS software version
    CONSTVER DESI:CURRENT                                                  str   Constants version
    INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini              str   DOS Configuration
    CENTER   244.32707,15.29368                                            str   Platemaker nfsproc center (ra, dec)
    GCENTER  8.27,53.17                                                    str   Platemaker gfaproc center (ra, dec)
    GHEXROT  165.2,0.38                                                    str   Platemaker gfaproc hexapod rotation (initial an
    PMNFSADC 28.06,52.49                                                   str   Platemaker nfsproc adc angles
    REQTIME  1860.0                                                        float [s] Requested exposure time
    ROLE     GUIDERMAN                                                     str
    OVERSCAN 50                                                            int
    DEVICEID dev04                                                         str   GFA device id (serial number)
    GAMBNTT  10.313                                                        float [deg C] GFA ambient temperature
    GFPGAT   32.748                                                        float [deg C] GFA fpga temperature
    GFILTERT 10.281                                                        float [deg C] GFA filter temperature
    GCOLDTEC 10.479                                                        float [deg C] GFA cold Peltier temperature
    GHOTTEC  10.236                                                        float [deg C] GFA hot Peltier temperature
    GCCDTEMP 10.479                                                        float [deg C] GFA CCD temperature
    GCAMTEMP 10.281                                                        float [deg C] GFA camera temperature
    GCAMHUM  3.346                                                         float [%/100] GFA camera humidity
    GHUMID2  3.346                                                         float [%/100] GFA humidity sensor 2
    GHUMID3  0.0                                                           float [%/100]GFA humidity sensor 3
    GEXPMODE normal                                                        str   GFA readout mode (loop/normal)
    READOUT  OK                                                            str
    ROIS     469.4,1724.9776.3,505.3                                       str
    CHECKSUM ZjADfi99ZiACfi79                                              str   HDU checksum updated 2023-05-25T08:35:47
    DATASUM  1072693248                                                    str   data unit checksum updated 2023-05-25T08:35:47
    ======== ============================================================= ===== ===============================================

Data: FITS image [float64, 1]

HDU1
----

EXTNAME = PMGSTARS

Table of guide stars to be used for guiding.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   86               int  width of table in bytes
    NAXIS2   29               int  number of rows in table
    EXPID    182039           int
    MODULE   GUIDESTARS       str
    CHECKSUM 8qKfAnKe1nKe8nKe str  HDU checksum updated 2023-05-25T08:35:47
    DATASUM  612635513        str  data unit checksum updated 2023-05-25T08:35:47
    ======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

========== ======= ====== ==================================================================================
Name       Type    Units  Description
========== ======= ====== ==================================================================================
GFA_LOC    char[6]        Location on focal plane of GFA (same numbering convention as petal location)
RA         float64 deg    Barycentric Right Ascension in ICRS
DEC        float64 deg    Barycentric declination in ICRS
ROW        float64        GFA pixel row coordinate
COL        float64        GFA pixel col coordinate
RA_IVAR    float64 deg^-2 Inverse variance of RA (no cosine term!), excluding astrometric calibration errors
DEC_IVAR   float64 deg^-2 Inverse variance of DEC, excluding astrometric calibration errors
MAG        float64        Gaia "G" magnitude
MORPHTYPE  int64          Imaging Surveys morphological type from Tractor
GUIDE_FLAG int64          Should be 1
ETC_FLAG   int64          Should be 0
========== ======= ====== ==================================================================================

HDU2
----

EXTNAME = PMGWCS

Table of WCS coefficients for each GFA.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   72               int  width of table in bytes
    NAXIS2   7                int  number of rows in table
    EXPID    182039           int
    MODULE   GUIDERWCS        str
    CHECKSUM CaGaCW9WCaEaCU9W str  HDU checksum updated 2023-05-25T08:35:47
    DATASUM  2237461692       str  data unit checksum updated 2023-05-25T08:35:47
    ======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

======= ======= ===== =====================
Name    Type    Units Description
======= ======= ===== =====================
GFA_LOC int64         Location on focal plane of GFA (same numbering convention as petal location)
CRVAL1  float64       WCS keyword and value
CRVAL2  float64       WCS keyword and value
CRPIX1  float64       WCS keyword and value
CRPIX2  float64       WCS keyword and value
CD1_1   float64       WCS keyword and value
CD1_2   float64       WCS keyword and value
CD2_1   float64       WCS keyword and value
CD2_2   float64       WCS keyword and value
======= ======= ===== =====================

HDU3
----

EXTNAME = PMFIDPOS

Table of predicted FVC CCD pixel coordinates for illuminated fiducials in an
FVC image of the focal plane. These are the average of 4 pinhole positions.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   40               int  width of table in bytes
    NAXIS2   113              int  number of rows in table
    EXPID    182039           int
    MODULE   FIDUCIALPOS      str
    CHECKSUM gPHJiPEGgPEGgPEG str  HDU checksum updated 2023-05-25T08:35:47
    DATASUM  2559088998       str  data unit checksum updated 2023-05-25T08:35:47
    ======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

========== ======= ===== ======================================
Name       Type    Units Description
========== ======= ===== ======================================
PETAL_LOC  int64         Petal location [0-9]
DEVICE_LOC int64         Device location on focal plane [0-523]
XPIX       float64       CCD X (column) coordinate
YPIX       float64       CCD Y (row) coordinate
FLAGS      int64         Flags as defined somewhere
========== ======= ===== ======================================

HDU4
----

EXTNAME = PMPOSPOS

Table of predicted FVC CCD pixel coordinates for back-illuminated positioner
fibers in an FVC image of the focal plane.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   75               int  width of table in bytes
    NAXIS2   5020             int  number of rows in table
    EXPID    182039           int
    MODULE   POSITIONERPOS    str
    CHECKSUM QioaRglUQglaQglU str  HDU checksum updated 2023-05-25T08:35:47
    DATASUM  2541629356       str  data unit checksum updated 2023-05-25T08:35:47
    ======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

=========== ======= ===== =============================================
Name        Type    Units Description
=========== ======= ===== =============================================
PETAL_LOC   int64         Petal location [0-9]
DEVICE_LOC  int64         Device location on focal plane [0-523]
DEVICE_TYPE char[3]       Device type
XFPA        float64 mm    Focal plane CS5 X coordinate
YFPA        float64 mm    Focal plane CS5 Y coordinate
Q           float64 rad   Focal plane CS5 Q coordinate (position angle)
S           float64 mm    Focal plane CS5 S coordinates (radius)
XPIX        float64       CCD X (column) coordinate
YPIX        float64       CCD Y (row) coordinate
FLAGS       int64         Flags as defined somewhere
=========== ======= ===== =============================================

HDU5
----

EXTNAME = PMCNTPOS

Table of predicted FVC pixel coordinates for the location of the
center-of-travel for positioners in an FVC image of the focal plane.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   40               int  width of table in bytes
    NAXIS2   5133             int  number of rows in table
    EXPID    182039           int
    MODULE   CENTERPOS        str
    CHECKSUM ooVAolUAolUAolUA str  HDU checksum updated 2023-05-25T08:35:47
    DATASUM  1382328634       str  data unit checksum updated 2023-05-25T08:35:47
    ======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

========== ======= ===== ======================================
Name       Type    Units Description
========== ======= ===== ======================================
PETAL_LOC  int64         Petal location [0-9]
DEVICE_LOC int64         Device location on focal plane [0-523]
XPIX       float64       CCD X (column) coordinate
YPIX       float64       CCD Y (column) coordinate
FLAGS      int64         Flags as defined somewhere
========== ======= ===== ======================================

HDU6
----

EXTNAME = PMFIBMAP

Table of all target and sky monitor positions after calibration with the FVC.

NOTE: For targets with a non-zero proper motion, ``FIBER_RA`` and ``FIBER_DEC``
refer to the position at the reference epoch.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   94               int  width of table in bytes
    NAXIS2   5020             int  number of rows in table
    EXPID    182039           int
    MODULE   FIBERMAP         str
    CHECKSUM OQIDPOI9OOIAOOI9 str  HDU checksum updated 2023-05-25T08:35:47
    DATASUM  2870350002       str  data unit checksum updated 2023-05-25T08:35:47
    ======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

=============== ======= ========= =======================================================
Name            Type    Units     Description
=============== ======= ========= =======================================================
FIBER_RA        float64 deg       RA of actual fiber position
FIBER_DEC       float64 deg       DEC of actual fiber position
FIBER_XI        float64 deg       Actual ICRS tangent plane xi coordinates pointed to by a fiber
FIBER_ETA       float64 deg       Actual ICRS tangent plane eta coordinates pointed to by a fiber
FIBER_RA_IVAR   float32 arcsec^-2 Inverse variance (not meaningful)
FIBER_DEC_IVAR  float32 arcsec^-2 Inverse variance (not meaningful)
FIBER_X         float64 mm        CS5 X location requested by PlateMaker
FIBER_Y         float64 mm        CS5 Y location requested by PlateMaker
DELTA_XFPA      float32 mm        Focal plane X correction (target minus actual)
DELTA_YFPA      float32 mm        Focal plane Y correction (target minus actual)
DELTA_XFPA_IVAR float32 mm^-2     Inverse variance (not meaningful)
DELTA_YFPA_IVAR float32 mm^-2     Inverse variance (not meaningful)
LOCATION        int32             Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBERSTATUS     int32             Fiber status mask. 0=good
DEVICE_LOC      int32             Device location on focal plane [0-523]
NUM_ITER        int32             Number of positioner iterations
SPECTROID       int32             0 (not used)
PETAL_LOC       int16             Petal location [0-9]
=============== ======= ========= =======================================================


Notes and Examples
==================

There is an inaccuracy in the way proper motions are applied in fields
at high dec: the proper motions are applied after target positions have
been converted to tangent plane coordinates centered on the field center,
but are not corrected to account for the fact that lines of constant
RA and DEC are not Cartesian coordinates in the tangent plane.
