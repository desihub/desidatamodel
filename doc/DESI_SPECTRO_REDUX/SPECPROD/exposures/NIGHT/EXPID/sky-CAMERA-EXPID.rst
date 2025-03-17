=====================
sky-CAMERA-EXPID.fits
=====================

:Summary: This holds the sky model for a given camera and exposure.
:Naming Convention: ``sky-{CAMERA}-{EXPID}.fits``, where ``{CAMERA}`` is
    one of the spectrograph cameras (*e.g.* ``z1``) and ``{EXPID}``
    is the 8-digit exposure ID.
:Regex: ``sky-[brz][0-9]-[0-9]{8}\.fits``
:File Type: FITS, 17 MB

Contents
========

====== =============== ===== ===================
Number EXTNAME         Type  Contents
====== =============== ===== ===================
HDU0_  SKY             IMAGE Sky model in electrons per Angstrom
HDU1_  IVAR            IMAGE Inverse variance of sky model
HDU2_  MASK            IMAGE Sky mask (0 = good)
HDU3_  WAVELENGTH      IMAGE Wavelength in Angstrom
HDU4_  STATIVAR        IMAGE Statistical-only inverse variance of sky model
HDU5_  THRPUTCORR      IMAGE Achromatic throughput correction per fiber
HDU6_  THRPUTCORR_MOD  IMAGE Model multiplicative throughput corrections for each fiber
HDU6_  DWAVECOEFF      IMAGE Vector of PCA coefficients for wavelength offsets
HDU7_  DLSFCOEFF       IMAGE Vector of PCA coefficients for LSF size changes
HDU8_  SKYGRADPCACOEFF IMAGE Vector of gradient amplitudes for sky gradient spectra
====== =============== ===== ===================

The SKY HDU is the sky model per-fiber accounting for different fiber
resolutions, but it does *not* include the empirical per-fiber throughput
correction in the THRPUTCORR HDU.  The final sky model per fiber is
``SKY * THRPUTCORR``.


FITS Header Units
=================

HDU0
----

EXTNAME = SKY

2D array of sky flux model of dimension [nspec, nwave] in units of electrons per Ansgtrom (fiber flat fielded). nspec is the number of fibers per camera. nwave in the length of the wavelength array. The spectra of all fibers share the same
wavelength grid (given in HDU WAVELENGTH). The sky model is different for each fiber because it is adapted to the resolution of each fiber, it contains corrections on bright sky line, and in some cases an anisotropic component.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====================== ===================================================================== ======= ===============================================
    KEY                    Example Value                                                         Type    Comment
    ====================== ===================================================================== ======= ===============================================
    NAXIS1                 2751                                                                  int
    NAXIS2                 500                                                                   int
    EXPID                  69022                                                                 int     Exposure number
    EXPFRAME               0                                                                     int     Frame number
    TILEID                 80616                                                                 int     DESI Tile ID
    FIBASSGN               /data/tiles/SVN_tiles/080/fiberassign-080616.fits                     str     Fiber assign fil
    FLAVOR                 science                                                               str     Observation type
    SEQUENCE               DESI                                                                  str     OCS Sequence name
    PURPOSE                Commissioning                                                         str     Purpose of observing night
    PROGRAM                SV1 BGS+MWS tile 80616                                                str     Program name
    PROPID                 2019B-5000                                                            str     Proposal ID
    OBSERVER               DESIObserver                                                          str     Names of observers
    LEAD                   RunManager                                                            str     Lead observer
    INSTRUME               DESI                                                                  str     Instrument name
    OBSERVAT               KPNO                                                                  str     Observatory name
    OBS-LAT                31.96403                                                              str     [deg] Observatory latitude
    OBS-LONG               -111.59989                                                            str     [deg] Observatory east longitude
    OBS-ELEV               2097.0                                                                float   [m] Observatory elevation
    TELESCOP               KPNO 4.0-m telescope                                                  str     Telescope name
    CORRCTOR               DESI Corrector                                                        str     Corrector Identification
    NIGHT                  20201220                                                              int     Observing night
    TIMESYS                UTC                                                                   str     Time system used for date-obs
    DATE-OBS               2020-12-21T02:36:32.099838                                            str     [UTC] Observation data and start time
    TIME-OBS               02:39:11.845920                                                       str     [UTC] Observation start time
    MJD-OBS                59204.10870486                                                        float   Modified Julian Date of observation
    OPENSHUT               2020-12-21T02:36:32.099838                                            str     Time shutter opened
    ST                     01:10:39.210                                                          str     Local Sidereal time at observation start (HH:MM
    EXPTIME                300.007                                                               float   [s] Actual exposure time
    REQRA                  356.0                                                                 float   [deg] Requested right ascension (observer input
    REQDEC                 29.0                                                                  float   [deg] Requested declination (observer input)
    FOCUS                  1426.5,-501.4,81.0,-2.6,42.3,169.2                                    str     Telescope focus settings
    VCCD                   ON                                                                    str     True (ON) if CCD voltage is on
    VCCDON                 2020-12-09T21:23:21.278481                                            str     Time when CCD voltage was turned on
    VCCDSEC                969694.4                                                              float   [s] CCD on time in seconds
    TRUSTEMP               11.767                                                                float   [deg] Average Telescope truss temperature (only
    PMIRTEMP               8.925                                                                 float   [deg] Average primary mirror temperature (nit,e
    EQUINOX                2000.0                                                                float   Epoch of observation
    MOUNTAZ                266.70224                                                             float   [deg] Mount azimuth angle
    MOUNTDEC               28.999221                                                             float   [deg] Mount declination
    MOUNTEL                71.039837                                                             float   [deg] Mount elevation angle
    MOUNTHA                21.769281                                                             float   [deg] Mount hour angle
    SKYDEC                 28.999221                                                             float   [deg] Telescope declination (pointing on sky)
    SKYRA                  355.996551                                                            float   [deg] Telescope right ascension (pointing on sk
    TARGTDEC               28.999221                                                             float   [deg] Target declination (to TCS)
    TARGTRA                355.996551                                                            float   [deg] Target right ascension (to TCS)
    USEETC                 F                                                                     bool    ETC data available if true
    USESKY                 T                                                                     bool    DOS Control: use Sky Monitor
    USEFOCUS               T                                                                     bool    DOS Control: use focus
    HEXTRIM                0.0,0.0,0.0,0.0,0.0,0.0                                               str     Hexapod trim values
    USEROTAT               T                                                                     bool    DOS Control: use rotator
    ROTOFFST               167.1                                                                 float   [arcsec] Rotator offset
    ROTENBLD               T                                                                     bool    Rotator enabled
    ROTRATE                0.0                                                                   float   [arcsec/min] Rotator rate
    USEGUIDR               T                                                                     bool    DOS Control: use guider
    USEDONUT               T                                                                     bool    DOS Control: use donuts
    SPECGRPH               6                                                                     int     Spectrograph logical name (SP)
    SPECID                 7                                                                     int     Spectrograph serial number (SM)
    FEEBOX                 lbnl075                                                               str     CCD Controller serial number
    VESSEL                 22                                                                    int     Cryostat serial number
    FEEVER                 v20160312                                                             str     CCD Controller version
    DETFLVER [1]_          FAILED: invalid argument for get command                              str     CCD Controller detector f
    FEEPOWER               ON                                                                    str     FEE power status
    FEEDMASK               2134851391                                                            int     FEE dac mask
    FEECMASK               1048575                                                               int     FEE clk mask
    CCDTEMP                850.0                                                                 float   [deg C] CCD controller CCD temperature
    RADESYS                FK5                                                                   str     Coordinate reference frame of major/minor axes
    FILENAME               /exposures/desi/specs/20201220/00069022/sp1-00069022.fits.fz          str     Name
    DOSVER                 trunk                                                                 str     DOS software version
    OCSVER                 1.2                                                                   float   OCS software version
    CONSTVER               DESI:CURRENT                                                          str     Constants version
    INIFILE                /data/msdos/dos_home/architectures/kpno/desi.ini                      str     DOS Configuration
    DELAYS                 13, 13, 25, 25, 8, 3000, 7, 7, 7, 7                                   str     [10] Delay settings
    CCDPREP                purge,clear                                                           str     CCD prep actions
    DETSECA                [1:2048, 1:2048]                                                      str     Detector section for quadrant A
    CDSPARMS               350, 350, 8, 1000                                                     str     CDS parameters
    CRYOTEMP [1]_          162.97                                                                float   [deg K] Cryostat CCD temperature
    CLOCK15                0.0,0.0                                                               str     [V] high rail, low rail
    CLOCK11                0.0,0.0                                                               str     [V] high rail, low rail
    ORSECA                 [5:2052, 2050:2081]                                                   str     Row overscan section for quadrant A
    CASETEMP               51.9392                                                               float   [deg C] CCD controller case temperature
    AMPSECC                [2048:1, 2049:4096]                                                   str     AMP section for quadrant C
    CLOCK4                 3.9999,-4.0002                                                        str     [V] high rail, low rail
    CLOCK17                3.9999,-4.0002                                                        str     [V] high rail, low rail
    DAC13                  0.0,-5.0544                                                           str     [V] set value, measured value
    DAC2                   15.9998,15.9032                                                       str     [V] set value, measured value
    DATASECA               [5:2052, 2:2049]                                                      str     Data section for quadrant A
    DATASECB               [2181:4228, 2:2049]                                                   str     Data section for quadrant B
    PRESECB                [4229:4232, 2:2049]                                                   str     Prescan section for quadrant B
    DAC14                  0.0,0.8008                                                            str     [V] set value, measured value
    ORSECD                 [2181:4228, 2082:2113]                                                str     Row bias section for quadrant D
    CCDSIZE                4162,4232                                                             str     CCD size in pixels (rows, columns)
    SETTINGS               detectors_sm_20191211.json                                            str     Name of DESI CCD settings file
    PRESECA                [1:4, 2:2049]                                                         str     Prescan section for quadrant A
    CLOCK14                3.0,-8.0001                                                           str     [V] high rail, low rail
    DAC16                  0.0,64.1256                                                           str     [V] set value, measured value
    CCDNAME                CCDSM7B                                                               str     CCD name
    AMPSECD                [4096:2049, 4096:2049]                                                str     AMP section for quadrant D
    PRRSECC                [5:2052, 4162:4162]                                                   str     Row prescan section for quadrant C
    CCDCFG                 sn22813_sta_20190405.cfg                                              str     CCD configuration file
    DAC8                   26.9998,26.0294                                                       str     [V] set value, measured value
    BIASSECD               [2117:2180, 2114:4161]                                                str     Bias section for quadrant D
    PRESECC                [1:4, 2114:4161]                                                      str     Prescan section for quadrant C
    CCDSECD                [2049:4096, 2049:4096]                                                str     CCD section for quadrant D
    CLOCK8                 3.0,-8.0001                                                           str     [V] high rail, low rail
    TRIMSECA               [5:2052, 2:2049]                                                      str     Trim section for quadrant A
    DAC5                   0.0,0.0                                                               str     [V] set value, measured value
    BIASSECC               [2053:2116, 2114:4161]                                                str     Bias section for quadrant C
    OFFSET0                -1.5,15.8311                                                          str     [V] set value, measured value
    CLOCK18                3.9999,-4.0002                                                        str     [V] high rail, low rail
    CCDTMING               default_sta_timing_20180905.txt                                       str     CCD timing file
    TRIMSECD               [2181:4228, 2114:4161]                                                str     Trim section for quadrant D
    OFFSET1                -1.5,15.8208                                                          str     [V] set value, measured value
    OFFSET4                -1.100000023841858,0.0105                                             str     [V] set value, measured value
    DATASECD               [2181:4228, 2114:4161]                                                str     Data section for quadrant D
    CLOCK3                 6.9999,-2.0001                                                        str     [V] high rail, low rail
    PGAGAIN                5                                                                     int     Controller gain
    PRRSECA                [5:2052, 1:1]                                                         str     Row prescan section for quadrant A
    CLOCK12                3.0,-8.0001                                                           str     [V] high rail, low rail
    CLOCK6                 3.9999,-4.0002                                                        str     [V] high rail, low rail
    OFFSET5                -1.100000023841858,-0.0053                                            str     [V] set value, measured value
    CLOCK2                 3.9999,-4.0002                                                        str     [V] high rail, low rail
    CLOCK16                0.0,0.0                                                               str     [V] high rail, low rail
    ORSECB                 [2181:4228, 2050:2081]                                                str     Row overscan section for quadrant B
    DAC12                  0.0,5.0232                                                            str     [V] set value, measured value
    DETSECC                [1:2048, 2049:4096]                                                   str     Detector section for quadrant C
    DAC15                  19.9997,19.6768                                                       str     [V] set value, measured value
    CAMERA                 b6                                                                    str     Camera name
    DAC6                   0.0,0.0053                                                            str     [V] set value, measured value
    BIASSECB               [2117:2180, 2:2049]                                                   str     Bias section for quadrant B
    DAC4                   0.0,0.0105                                                            str     [V] set value, measured value
    CLOCK1                 3.9999,-4.0002                                                        str     [V] high rail, low rail
    PRRSECD                [2181:4228, 4162:4162]                                                str     Row prescan section for quadrant D
    DAC7                   0.0,0.0                                                               str     [V] set value, measured value
    DETSECD                [2049:4096, 2049:4096]                                                str     Detector section for quadrant D
    ORSECC                 [5:2052, 2082:2113]                                                   str     Row overscan section for quadrant C
    DAC17                  -0.0,0.0488                                                           str     [V] set value, measured value
    CRYOPRES [1]_          9.252e-08                                                             str     [mb] Cryostat pressure (IP)
    AMPSECA                [1:2048, 1:2048]                                                      str     AMP section for quadrant A
    CLOCK5                 3.9999,-4.0002                                                        str     [V] high rail, low rail
    CCDSECA                [1:2048, 1:2048]                                                      str     CCD section for quadrant A
    DAC9                   26.9998,26.252                                                        str     [V] set value, measured value
    CLOCK0                 3.9999,-4.0002                                                        str     [V] high rail, low rail
    DETSECB                [2049:4096, 1:2048]                                                   str     Detector section for quadrant B
    DAC1                   15.9998,15.8311                                                       str     [V] set value, measured value
    DAC3                   15.9998,15.8517                                                       str     [V] set value, measured value
    DAC11                  26.9998,26.9198                                                       str     [V] set value, measured value
    CLOCK9                 3.0,-8.0001                                                           str     [V] high rail, low rail
    DIGITIME               41.6984                                                               float   [s] Time to digitize image
    OFFSET2                -1.5,15.9135                                                          str     [V] set value, measured value
    PRESECD                [4229:4232, 2114:4161]                                                str     Prescan section for quadrant D
    CLOCK10                3.0,-8.0001                                                           str     [V] high rail, low rail
    DAC0                   15.9998,15.8311                                                       str     [V] set value, measured value
    TRIMSECB               [2181:4228, 2:2049]                                                   str     Trim section for quadrant B
    OFFSET3                -1.5,15.8414                                                          str     [V] set value, measured value
    AMPSECB                [2049:4096, 2048:1]                                                   str     AMP section for quadrant B
    CPUTEMP                51.334                                                                float   [deg C] CCD controller CPU temperature
    CCDSECC                [1:2048, 2049:4096]                                                   str     CCD section for quadrant C
    OFFSET7                -1.100000023841858,0.0                                                str     [V] set value, measured value
    BLDTIME                0.3499                                                                float   [s] Time to build image
    DATASECC               [5:2052, 2114:4161]                                                   str     Data section for quadrant C
    DETECTOR               sn22813                                                               str     Detector (ccd) identification
    OFFSET6                -1.100000023841858,0.0053                                             str     [V] set value, measured value
    BIASSECA               [2053:2116, 2:2049]                                                   str     Bias section for quadrant A
    TRIMSECC               [5:2052, 2114:4161]                                                   str     Trim section for quadrant C
    PRRSECB                [2181:4228, 1:1]                                                      str     Row prescan section for quadrant B
    CCDSECB                [2049:4096, 1:2048]                                                   str     CCD section for quadrant B
    DAC10                  26.9998,26.9198                                                       str     [V] set value, measured value
    CLOCK13                3.0,-8.0001                                                           str     [V] high rail, low rail
    CLOCK7                 6.9999,-2.0001                                                        str     [V] high rail, low rail
    REQTIME                300.0                                                                 float   [s] Requested exposure time
    OBSID                  kp4m20201221t023911                                                   str     Unique observation identifier
    PROCTYPE               RAW                                                                   str     Data processing level
    PRODTYPE               image                                                                 str     Data product type
    CHECKSUM               VAChW8AfVAAfV7Af                                                      str     HDU checksum updated 2022-02-14T06:13:54
    DATASUM                1301167967                                                            str     data unit checksum updated 2022-02-14T06:13:54
    GAINA                  1.29                                                                  float   e/ADU (gain applied to image)
    SATULEVA               40000.0                                                               float   saturation or non lin. level, in ADU, inc. bias
    OSTEPA                 1.21893160851323                                                      float   ADUs (max-min of median overscan per row)
    OMETHA                 AVERAGE                                                               str     use average overscan
    OVERSCNA               1201.407080585313                                                     float   ADUs (gain not applied)
    OBSRDNA                3.932320693814749                                                     float   electrons (gain is applied)
    SATUELEA               50050.18486604495                                                     float   saturation or non lin. level, in electrons
    GAINB                  1.284                                                                 float   e/ADU (gain applied to image)
    SATULEVB               65535.0                                                               float   saturation or non lin. level, in ADU, inc. bias
    OSTEPB                 0.9970038118117373                                                    float   ADUs (max-min of median overscan per row)
    OMETHB                 AVERAGE                                                               str     use average overscan
    OVERSCNB               1212.197611701435                                                     float   ADUs (gain not applied)
    OBSRDNB                3.323361580066672                                                     float   electrons (gain is applied)
    SATUELEB               82590.47826657536                                                     float   saturation or non lin. level, in electrons
    GAINC                  1.292                                                                 float   e/ADU (gain applied to image)
    SATULEVC               40000.0                                                               float   saturation or non lin. level, in ADU, inc. bias
    OSTEPC                 0.7691677607072052                                                    float   ADUs (max-min of median overscan per row)
    OMETHC                 AVERAGE                                                               str     use average overscan
    OVERSCNC               1178.422505897216                                                     float   ADUs (gain not applied)
    OBSRDNC                3.252427649816138                                                     float   electrons (gain is applied)
    SATUELEC               50157.4781223808                                                      float   saturation or non lin. level, in electrons
    GAIND                  1.295                                                                 float   e/ADU (gain applied to image)
    SATULEVD               44000.0                                                               float   saturation or non lin. level, in ADU, inc. bias
    OSTEPD                 0.9395222094608471                                                    float   ADUs (max-min of median overscan per row)
    OMETHD                 AVERAGE                                                               str     use average overscan
    OVERSCND               1174.800960708566                                                     float   ADUs (gain not applied)
    OBSRDND                3.333804957383686                                                     float   electrons (gain is applied)
    SATUELED               55458.6327558824                                                      float   saturation or non lin. level, in electrons
    FIBERMIN               3000                                                                  int
    BBKGMINA [1]_          -0.2077800596230136                                                   float
    BBKGMAXA [1]_          0.5254324469128164                                                    float
    BBKGMINB [1]_          -0.2033242713025349                                                   float
    BBKGMAXB [1]_          0.4258502359052168                                                    float
    BBKGMINC [1]_          -0.1314577356495719                                                   float
    BBKGMAXC [1]_          0.4236035445727393                                                    float
    BBKGMIND [1]_          -0.2582211042496522                                                   float
    BBKGMAXD [1]_          0.3659635169905933                                                    float
    LONGSTRN               OGIP 1.0                                                              str     The OGIP Long String Convention may be used.
    MODULE                 CI                                                                    str     Image Sources/Component
    COSMSPLT               F                                                                     bool    Cosmics split exposure if true
    MAXSPLIT               0                                                                     int     Number of allowed exposure splits
    SPLITIDS [1]_          69022                                                                 str     List of expids for split exposures
    OBSTYPE                SCIENCE                                                               str     Spectrograph observation type
    MANIFEST               F                                                                     bool    DOS exposure manifest
    OBJECT                                                                                       str     Object name
    SEQNUM                 1                                                                     int     Number of exposure in sequence
    CAMSHUT                open                                                                  str     Shutter status during observation
    ACQTIME                15.0                                                                  float   [s] acqusition image exposure time
    GUIDTIME               5.0                                                                   float   [s] guider GFA exposure time
    FOCSTIME [1]_          60.0                                                                  float   [s] focus GFA exposure time
    SKYTIME [1]_           60.0                                                                  float   [s] sky camera exposure time (acquisition)
    WHITESPT               F                                                                     bool    Telescope is at whitespot
    ZENITH                 F                                                                     bool    Telescope is at zenith
    SEANNEX                F                                                                     bool    Telescope is at SE annex
    BEYONDP                F                                                                     bool    Telescope is beyond pole
    FIDUCIAL               off                                                                   str     Fiducials status during observation
    BACKLIT                off                                                                   str     Fibers are backlit if True
    AIRMASS                1.060311                                                              float   Airmass
    PMREADY                T                                                                     bool    Primary mirror ready
    PMCOVER                open                                                                  str     Primary mirror cover
    PMCOOL                 off                                                                   str     Primary mirror cooling
    DOMSHUTU               open                                                                  str     Upper dome shutter
    DOMSHUTL               open                                                                  str     Lower dome shutter
    DOMLIGHH               off                                                                   str     High dome lights
    DOMLIGHL               off                                                                   str     Low dome lights
    DOMEAZ                 255.166                                                               float   [deg] Dome azimuth angle
    DOMINPOS               T                                                                     bool    Dome is in position
    GUIDOFFR               -0.052283                                                             float   [arcsec] Cummulative guider offset (RA)
    GUIDOFFD               0.136634                                                              float   [arcsec] Cummulative guider offset (dec)
    MOONDEC                -8.975162                                                             float   [deg] Moon declination at start of exposure
    MOONRA                 352.538429                                                            float   [deg] Moon RA at start of exposure
    INCTRL                 T                                                                     bool    DESI in control
    INPOS                  T                                                                     bool    Mount in position
    MNTOFFD                -15.76                                                                float   [arcsec] Mount offset (dec)
    MNTOFFR                29.32                                                                 float   [arcsec] Mount offset (RA)
    PARALLAC               75.635085                                                             float   [deg] Parallactic angle
    TARGTAZ                267.074049                                                            float   [deg] Target azimuth
    TARGTEL                70.563787                                                             float   [deg] Target elevation
    TRGTOFFD               0.0                                                                   float   [arcsec] Telescope target offset (dec)
    TRGTOFFR               0.0                                                                   float   [arcsec] Telescope target offset (RA)
    ZD                     19.436213                                                             float   [deg] Telescope zenith distance
    TILERA                 356.0                                                                 float   RA of tile given in fiberassign file
    TILEDEC                29.0                                                                  float   DEC of tile given in fiberassign file
    TCSST                  01:13:18.668                                                          str     Local Sidereal time reported by TCS (HH:MM:SS)
    TCSMJD                 59204.110981                                                          float   MJD reported by TCS
    USETURB [1]_           T                                                                     bool    Turbulence corrections are applied if true
    ACQCAM                 GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                             str     Acquisition cameras used
    GUIDECAM               GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                             str     Guide cameras used for t
    FOCUSCAM [1]_          FOCUS1,FOCUS4,FOCUS6,FOCUS9                                           str     Focus cameras used for this exposure
    SKYCAM [1]_            SKYCAM0,SKYCAM1                                                       str     Sky cameras used for this exposure
    REQADC                 65.78,85.28                                                           str     [deg] requested ADC angles
    ADCCORR                T                                                                     bool    Correct pointing for ADC setting if True
    ADC1PHI                65.780005                                                             float   [deg] ADC 1 angle
    ADC2PHI                85.279991                                                             float   [deg] ADC 2 angle
    ADC1HOME               F                                                                     bool    ADC 1 at home position if True
    ADC2HOME               F                                                                     bool    ADC 2 at home position if True
    ADC1NREV               -1.0                                                                  float   ADC 1 number of revs
    ADC2NREV               0.0                                                                   float   ADC 2 number of revs
    ADC1STAT               STOPPED                                                               str     ADC 1 status
    ADC2STAT               STOPPED                                                               str     ADC 2 status
    HEXPOS                 1426.5,-501.3,81.0,-2.6,42.3,171.9                                    str     Hexapod position
    RESETROT               F                                                                     bool    DOS Control: reset hex rotator
    USEPOS                 T                                                                     bool    Fiber positioner data available if true
    PETALS                 PETAL0,PETAL1,PETAL2,PETAL3,PETAL4,PETAL5,PETAL6,PETAL7,PETAL8,PETAL9 str     Participating petals
    POSCYCLE               1                                                                     int     Number of current iteration
    POSONTGT               3626                                                                  int     Number of positioners on target
    POSNOTON [1]_          6                                                                     int     Number of enabled positioners not on target
    POSONFRC               0.8613                                                                float   Fraction of positioners on target
    POSDISAB               37                                                                    int     Number of disabled positioners
    POSENABL               4210                                                                  int     Number of enabled positioners
    POSRMS                 0.0171                                                                float   [mm] RMS of positioner accuracy
    TURBRMS [1]_           0.0071                                                                float   [mm] RMS of turbulence correction
    POSITER                1                                                                     int     Positioning Control: max. number of pos. cycles
    POSFRACT               0.95                                                                  float
    POSTOLER               0.01                                                                  float   Positioning Control: in_position tolerance (mm)
    POSMVALL               T                                                                     bool    Positioning Control: move all positioners
    GUIDMODE               catalog                                                               str     Guider mode
    USEAOS [1]_            F                                                                     bool    DOS Control: AOS data available if true
    USESPCTR               T                                                                     bool    DOS Control: use spectrographs
    SPCGRPHS               SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                               str     Participating spectrograph
    ILLSPECS [1]_          SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                               str     Participating illuminate s
    CCDSPECS [1]_          SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                               str     Participating ccd spectrog
    TDEWPNT                -16.043                                                               float   Telescope air dew point
    TAIRFLOW               0.0                                                                   float   Telescope air flow
    TAIRITMP               11.8                                                                  float   [deg] Telescope air in temperature
    TAIROTMP               11.7                                                                  float   [deg] Telescope air out temperature
    TAIRTEMP               10.65                                                                 float   [deg] Telescope air temperature
    TCASITMP               0.0                                                                   float   [deg] Telescope Cass Cage in temperature
    TCASOTMP               10.8                                                                  float   [deg] Telescope Cass Cage out temperature
    TCSITEMP               9.3                                                                   float   [deg] Telescope center section in temperature
    TCSOTEMP               10.8                                                                  float   [deg] Telescope center section out temperature
    TCIBTEMP               0.0                                                                   float   [deg] Telescope chimney IB temperature
    TCIMTEMP               0.0                                                                   float   [deg] Telescope chimney IM temperature
    TCITTEMP               0.0                                                                   float   [deg] Telescope chimney IT temperature
    TCOSTEMP               0.0                                                                   float   [deg] Telescope chimney OS temperature
    TCOWTEMP               0.0                                                                   float   [deg] Telescope chimney OW temperature
    TDBTEMP                9.3                                                                   float   [deg] Telescope dec bore temperature
    TFLOWIN                0.0                                                                   float   Telescope flow rate in
    TFLOWOUT               0.0                                                                   float   Telescope flow rate out
    TGLYCOLI               9.9                                                                   float   [deg] Telescope glycol in temperature
    TGLYCOLO               9.8                                                                   float   [deg] Telescope glycol out temperature
    THINGES                11.4                                                                  float   [deg] Telescope hinge S temperature
    THINGEW                11.2                                                                  float   [deg] Telescope hinge W temperature
    TPMAVERT               8.931                                                                 float   [deg] Telescope mirror averagetemperature
    TPMDESIT               7.0                                                                   float   [deg] Telescope mirror desired temperature
    TPMEIBT                8.6                                                                   float   [deg] Telescope mirror EIB temperature
    TPMEITT                8.6                                                                   float   [deg] Telescope mirror EIT temperature
    TPMEOBT                8.5                                                                   float   [deg] Telescope mirror EOB temperature
    TPMEOTT                9.0                                                                   float   [deg] Telescope mirror EOT temperature
    TPMNIBT                8.4                                                                   float   [deg] Telescope mirror NIB temperature
    TPMNITT                8.9                                                                   float   [deg] Telescope mirror NIT temperature
    TPMNOBT                8.8                                                                   float   [deg] Telescope mirror NOB temperature
    TPMNOTT                9.1                                                                   float   [deg] Telescope mirror NOT temperature
    TPMRTDT                9.0                                                                   float   [deg] Telescope mirror RTD temperature
    TPMSIBT                8.6                                                                   float   [deg] Telescope mirror SIB temperature
    TPMSITT                8.8                                                                   float   [deg] Telescope mirror SIT temperature
    TPMSOBT                8.2                                                                   float   [deg] Telescope mirror SOB temperature
    TPMSOTT                8.9                                                                   float   [deg] Telescope mirror SOT temperature
    TPMSTAT                ready                                                                 str     Telescope mirror status
    TPMWIBT                8.2                                                                   float   [deg] Telescope mirror WIB temperature
    TPMWITT                9.1                                                                   float   [deg] Telescope mirror WIT temperature
    TPMWOBT                8.3                                                                   float   [deg] Telescope mirror WOB temperature
    TPMWOTT                8.9                                                                   float   [deg] Telescope mirror WOT temperature
    TPCITEMP               8.5                                                                   float   [deg] Telescope primary cell in temperature
    TPCOTEMP               8.6                                                                   float   [deg] Telescope primary cell out temperature
    TPR1HUM                0.0                                                                   float   Telescope probe 1 humidity
    TPR1TEMP               0.0                                                                   float   [deg] Telescope probe1 temperature
    TPR2HUM                0.0                                                                   float   Telescope probe 2 humidity
    TPR2TEMP               0.0                                                                   float   [deg] Telescope probe2 temperature
    TSERVO                 40.0                                                                  float   Telescope servo setpoint
    TTRSTEMP               11.4                                                                  float   [deg] Telescope top ring S temperature
    TTRWTEMP               11.0                                                                  float   [deg] Telescope top ring W temperature
    TTRUETBT               -4.2                                                                  float   [deg] Telescope truss ETB temperature
    TTRUETTT               11.2                                                                  float   [deg] Telescope truss ETT temperature
    TTRUNTBT               10.9                                                                  float   [deg] Telescope truss NTB temperature
    TTRUNTTT               11.2                                                                  float   [deg] Telescope truss NTT temperature
    TTRUSTBT               10.7                                                                  float   [deg] Telescope truss STB temperature
    TTRUSTST               10.8                                                                  float   [deg] Telescope truss STS temperature
    TTRUSTTT               11.1                                                                  float   [deg] Telescope truss STT temperature
    TTRUTSBT               11.8                                                                  float   [deg] Telescope truss TSB temperature
    TTRUTSMT               11.8                                                                  float   [deg] Telescope truss TSM temperature
    TTRUTSTT               11.8                                                                  float   [deg] Telescope truss TST temperature
    TTRUWTBT               10.5                                                                  float   [deg] Telescope truss WTB temperature
    TTRUWTTT               10.9                                                                  float   [deg] Telescope truss WTT temperature
    ALARM                  F                                                                     bool    UPS major alarm or check battery
    ALARM-ON               F                                                                     bool    UPS active alarm condition
    BATTERY                100.0                                                                 float   [%] UPS Battery left
    SECLEFT                5178.0                                                                float   [s] UPS Seconds left
    UPSSTAT [1]_           System Normal - On Line(7)                                            str     UPS Status
    INAMPS                 70.4                                                                  float   [A] UPS total input current
    OUTWATTS               5000.0,7200.0,4800.0                                                  str     [W] UPS Phase A, B, C output watts
    COMPDEW                -12.9                                                                 float   [deg C] Computer room dewpoint
    COMPHUM                7.4                                                                   float   [%] Computer room humidity
    COMPAMB                19.5                                                                  float   [deg C] Computer room ambient temperature
    COMPTEMP               24.5                                                                  float   [deg C] Computer room hygrometer temperature
    DEWPOINT               11.5                                                                  float   [deg C] (outside) dewpoint
    HUMIDITY               10.0                                                                  float   [%] (outside) humidity
    PRESSURE               795.0                                                                 float   [torr] (outside) air pressure
    OUTTEMP                0.0                                                                   float   [deg C] outside temperature
    WINDDIR                55.0                                                                  float   [deg] wind direction
    WINDSPD                27.3                                                                  float   [m/s] wind speed
    GUST                   20.6                                                                  float   [m/s] Wind gusts speed
    AMNIENTN               13.5                                                                  float   [deg C] ambient temperature north
    CFLOOR                 8.9                                                                   float   [deg C] temperature on C floor
    NWALLIN                13.9                                                                  float   [deg C] temperature at north wall inside
    NWALLOUT               9.6                                                                   float   [deg C] temperature at north wall outside
    WWALLIN                12.9                                                                  float   [deg C] temperature at west wall inside
    WWALLOUT               10.6                                                                  float   [deg C] temperature at west wall outside
    AMBIENTS               14.8                                                                  float   [deg C] ambient temperature south
    FLOOR                  12.6                                                                  float   [deg C] temperature at floor (LCR)
    EWALLCMP               10.8                                                                  float   [deg C] temperature at east wall, computer room
    EWALLCOU               10.6                                                                  float   [deg C] temperature at east wall, Coude room
    ROOF                   10.3                                                                  float   [deg C] temperature on roof
    ROOFAMB                10.6                                                                  float   [deg C] ambient temperature on roof
    DOMEBLOW               10.4                                                                  float   [deg C] temperature at dome back, lower
    DOMEBUP                10.7                                                                  float   [deg C] temperature at dome back, upper
    DOMELLOW               10.8                                                                  float   [deg C] temperature at dome left, lower
    DOMELUP                10.8                                                                  float   [deg C] temperature at dome left, upper
    DOMERLOW               10.6                                                                  float   [deg C] temperature at dome right, lower
    DOMERUP                10.5                                                                  float   [deg C] temperature at dome right, upper
    PLATFORM               10.4                                                                  float   [deg C] temperature at platform
    SHACKC                 14.4                                                                  float   [deg C] temperature at shack ceiling
    SHACKW                 13.7                                                                  float   [deg C] temperature at shack wall
    STAIRSL                10.5                                                                  float   [deg C] temperature at stairs, lower
    STAIRSM                10.4                                                                  float   [deg C] temperature at stairs, mid
    STAIRSU                10.6                                                                  float   [deg C] temperature at stairs, upper
    TELBASE                9.6                                                                   float   [deg C] temperature at telescope base
    UTILWALL               11.1                                                                  float   [deg C] temperature at utility room wall
    UTILROOM               10.9                                                                  float   [deg C] temperature in utilitiy room
    TNFSPROC [1]_          8.1963                                                                float   [s] PlateMaker NFSPROC processing time
    TGFAPROC [1]_          7.9212                                                                float   [s] PlateMaker GFAPROC processing time
    SIMGFAP                F                                                                     bool    DOS Control: simulate GFAPROC
    USEFVC                 T                                                                     bool    DOS Control: use fvc
    USEFID                 T                                                                     bool    DOS Control: use fiducials
    USEILLUM               T                                                                     bool    DOS Control: use illuminator
    USEXSRVR               T                                                                     bool    DOS Control: use exposure server
    USEOPENL               T                                                                     bool    DOS Control: use open loop move
    USEMIDPT [1]_          T                                                                     bool    Use exposure midpoint if true
    STOPGUDR               T                                                                     bool    DOS Control: stop guider
    STOPFOCS               T                                                                     bool    DOS Control: stop focus
    STOPSKY                T                                                                     bool    DOS Control: stop sky monitor
    KEEPGUDR               F                                                                     bool    DOS Control: keep guider running
    KEEPFOCS               F                                                                     bool    DOS Control: keep focus running
    KEEPSKY                F                                                                     bool    DOS Control: keep sky mon. running
    REACQUIR               F                                                                     bool    DOS Control: reacquire same files
    EXCLUDED                                                                                     str     Components excluded from this exposure
    PMVER [1]_             desi-138368                                                           str     PlateMaker/Dervish version
    FVCTIME [1]_           2.0                                                                   float   [s] FVC exposure time
    SIMGFACQ               F                                                                     bool
    POSCNVGD [1]_          F                                                                     bool    Number of positioners converged
    GUIEXPID               69022                                                                 int     Guider exposure id at start of spectro exp.
    IGFRMNUM               12                                                                    int     Guider frame number at start of spectro exp.
    FOCEXPID               69022                                                                 int     Focus exposure id at start of spectro exp.
    IFFRMNUM               1                                                                     int     Focus frame number at start of spectro exp.
    TMEBTEXP [1]_          1219.825                                                              float   [s] Time between (DESI) exposures
    SKYEXPID               69022                                                                 int     Sky exposure id at start of spectro exp.
    ISFRMNUM               1                                                                     int     Sky frame number at start of spectro exp.
    FGFRMNUM               46                                                                    int     Guider frame number at end of spectro exp.
    FFFRMNUM               6                                                                     int     Focus frame number at end of spectro exp.
    FSFRMNUM               5                                                                     int     Sky frame number at end of spectro exp.
    ETCSKYLV [1]_          15.1381                                                               float   [unit?] ETC skylevel
    HELIOCOR               0.9999115198216216                                                    float
    NSPEC                  500                                                                   int     Number of spectra
    WAVEMIN                3600.0                                                                float   First wavelength [Angstroms]
    WAVEMAX                5800.0                                                                float   Last wavelength [Angstroms]
    WAVESTEP               0.8                                                                   float   Wavelength step size [Angstroms]
    SPECTER                0.10.0                                                                str     https://github.com/desihub/specter
    IN_PSF                 SPECPROD/exposures/20201220/00069022/psf-b6-00069022.fits             str     Input sp
    IN_IMG                 SPECPROD/preproc/20201220/00069022/preproc-b6-00069022.fits           str
    ORIG_PSF               SPECPROD/calibnight/20201220/psfnight-b6-20201220.fits                str
    BUNIT                  electron/Angstrom                                                     str
    IN_FRAME               SPECPROD/exposures/20201220/00069022/frame-b6-00069022.fits           str
    FIBERFLT               SPECPROD/exposures/20201220/00069022/fiberflatexp-b6-00069022.fits    str
    SP1NIRT [1]_           139.91                                                                float   [K] SP1 NIR temperature
    SP4NIRT [1]_           139.96                                                                float   [K] SP4 NIR temperature
    PMTRANS [1]_           96.38                                                                 float   [%] PlateMaker GFAPROC transparency
    SUNRA [1]_             16.188197                                                             float   [deg] Sun RA at start of exposure
    SP3REDT [1]_           139.96                                                                float   [K] SP3 red temperature
    SP2NIRP [1]_           5.108e-08                                                             float   [mb] SP2 NIR pressure
    SP6NIRP [1]_           2.875e-07                                                             float   [mb] SP6 NIR pressure
    SP8REDP [1]_           6.99e-08                                                              float   [mb] SP8 red pressure
    SP4REDP [1]_           4.945e-08                                                             float   [mb] SP4 red pressure
    SP0NIRP [1]_           5.598e-08                                                             float   [mb] SP0 NIR pressure
    SP1REDP [1]_           5.142e-08                                                             float   [mb] SP1 red pressure
    SP5NIRT [1]_           139.94                                                                float   [K] SP5 NIR temperature
    SP8BLUP [1]_           8.113e-08                                                             float   [mb] SP8 blue pressure
    SP1REDT [1]_           139.89                                                                float   [K] SP1 red temperature
    SP3NIRT [1]_           140.01                                                                float   [K] SP3 NIR temperature
    SP6BLUP [1]_           7.209e-08                                                             float   [mb] SP6 blue pressure
    SP9BLUP [1]_           1.181e-07                                                             float   [mb] SP9 blue pressure
    SP2REDP [1]_           8.846e-08                                                             float   [mb] SP2 red pressure
    USESPLIT [1]_          T                                                                     bool    Exposure splits are allowed
    SP7REDT [1]_           139.99                                                                float   [K] SP7 red temperature
    SP9NIRT [1]_           139.89                                                                float   [K] SP9 NIR temperature
    SP0REDP [1]_           4.896e-08                                                             float   [mb] SP0 red pressure
    SP7NIRP [1]_           4.315e-08                                                             float   [mb] SP7 NIR pressure
    SP2REDT [1]_           139.99                                                                float   [K] SP2 red temperature
    SP7REDP [1]_           5.383e-08                                                             float   [mb] SP7 red pressure
    SP6NIRT [1]_           139.89                                                                float   [K] SP6 NIR temperature
    SP6REDP [1]_           5.397e-08                                                             float   [mb] SP6 red pressure
    SP8REDT [1]_           139.94                                                                float   [K] SP8 red temperature
    FRAMES [1]_            None                                                                  Unknown Number of Frames in Archive
    SP9REDT [1]_           140.01                                                                float   [K] SP9 red temperature
    SP2NIRT [1]_           139.91                                                                float   [K] SP2 NIR temperature
    SP4BLUP [1]_           4.978e-08                                                             float   [mb] SP4 blue pressure
    SP8NIRP [1]_           4.945e-08                                                             float   [mb] SP8 NIR pressure
    SPLITEXP [1]_          F                                                                     bool    Split exposure part of a visit
    SEQSTART [1]_          2021-04-07T03:54:14.413292                                            str     Start time of sequence processing
    STARTADJ [1]_          2022-03-18T03:57:35.888348                                            str     Time sequence starts adjusting the inst
    SP8NIRT [1]_           139.99                                                                float   [K] SP8 NIR temperature
    SP7BLUT [1]_           163.02                                                                float   [K] SP7 blue temperature
    SP5REDP [1]_           4.693e-08                                                             float   [mb] SP5 red pressure
    SP5NIRP [1]_           7.197e-08                                                             float   [mb] SP5 NIR pressure
    SP5BLUT [1]_           163.02                                                                float   [K] SP5 blue temperature
    SP0BLUP [1]_           9.122e-08                                                             float   [mb] SP0 blue pressure
    SP1NIRP [1]_           4.585e-08                                                             float   [mb] SP1 NIR pressure
    TCSKDEC [1]_           0.3 0.003 0.00003                                                     str     TCS Kalman (dec)
    SP6REDT [1]_           139.94                                                                float   [K] SP6 red temperature
    TCSPIDEC [1]_          1.0,0.0,0.0,0.0                                                       str     TCS PI settings (P, I (gain, error window, satu
    TCSGRA [1]_            0.3                                                                   float   TCS simple gain (RA)
    TCSGDEC [1]_           0.3                                                                   float   TCS simple gain (dec)
    SP1BLUT [1]_           163.02                                                                float   [K] SP1 blue temperature
    SP9NIRP [1]_           5.207e-08                                                             float   [mb] SP9 NIR pressure
    SP0NIRT [1]_           139.89                                                                float   [K] SP0 NIR temperature
    SP4BLUT [1]_           163.02                                                                float   [K] SP4 blue temperature
    SP9BLUT [1]_           163.02                                                                float   [K] SP9 blue temperature
    SP9REDP [1]_           4.884e-08                                                             float   [mb] SP9 red pressure
    PMSEEING [1]_          1.19                                                                  float   [arcsec] PlateMaker GFAPROC seeing
    SP0REDT [1]_           139.96                                                                float   [K] SP0 red temperature
    SP2BLUT [1]_           163.02                                                                float   [K] SP2 blue temperature
    TCSKRA [1]_            0.3 0.003 0.00003                                                     str     TCS Kalman (RA)
    SP3NIRP [1]_           4.194e-08                                                             float   [mb] SP3 NIR pressure
    TCSPIRA [1]_           1.0,0.0,0.0,0.0                                                       str     TCS PI settings (P, I (gain, error window, satu
    SP8BLUT [1]_           162.9                                                                 float   [K] SP8 blue temperature
    VISITIDS [1]_          83717                                                                 str     List of expids for a visit (same tile)
    MOONSEP [1]_           138.187                                                               float   [deg] Moon Separation
    SP5BLUP [1]_           1.125e-07                                                             float   [mb] SP5 blue pressure
    TCSMFDEC [1]_          1                                                                     int     TCS moving filter length (dec)
    SP4NIRP [1]_           6.595e-08                                                             float   [mb] SP4 NIR pressure
    SP7BLUP [1]_           9.98e-08                                                              float   [mb] SP7 blue pressure
    SP2BLUP [1]_           6.432e-08                                                             float   [mb] SP2 blue pressure
    SUNDEC [1]_            6.890581                                                              float   [deg] Sun declination at start of exposure
    SP1BLUP [1]_           8.039e-08                                                             float   [mb] SP1 blue pressure
    SKYLEVEL [1]_          1.398                                                                 float   [counts?] ETC sky level
    TCSMFRA [1]_           1                                                                     int     TCS moving filter length (RA)
    SP3BLUP [1]_           8.133e-08                                                             float   [mb] SP3 blue pressure
    SP5REDT [1]_           139.99                                                                float   [K] SP5 red temperature
    SP7NIRT [1]_           139.96                                                                float   [K] SP7 NIR temperature
    SP0BLUT [1]_           163.02                                                                float   [K] SP0 blue temperature
    SP3REDP [1]_           6.033e-08                                                             float   [mb] SP3 red pressure
    NTSSURVY [1]_          sv3                                                                   str     NTS survey name
    SP3BLUT [1]_           163.04                                                                float   [K] SP3 blue temperature
    SP4REDT [1]_           140.01                                                                float   [K] SP4 red temperature
    SP6BLUT [1]_           163.02                                                                float   [K] SP6 blue temperature
    SEQID [1]_             6 requests                                                            str     Exposure sequence identifier
    SEQTOT [1]_            6                                                                     int     Total number of exposures in sequence
    MINTIME [1]_           120.0                                                                 float   [s] Minimum exposure time (from NTS, used by ET
    MIDTIME [1]_           840.2095                                                              float   [s] Exposure midpoint time used by PlateMaker
    SEEING [1]_            None                                                                  float   [arcsec] ETC/PM seeing
    ETCTEFF [1]_           226.882385                                                            float   [s] ETC effective exposure time
    ETCPREV [1]_           0.0                                                                   float   [s] ETC cummulative t_eff for visit
    ETCSPLIT [1]_          1                                                                     int     ETC split sequence number for this visit
    TOTTEFF [1]_           225.6017                                                              float   [s] Total effective exposure time for visit
    TRANSPAR [1]_          None                                                                  float   ETC/PM transparency
    ACQFWHM [1]_           0.890634                                                              float   [arcsec] FWHM of guide star PSF in acquisition
    POSCVFRC [1]_          0.4956                                                                float   Fraction of converged positioners
    ETCTRANS [1]_          0.915827                                                              float   ETC averaged TRANSP normalized to 1
    SLEWANGL [1]_          16.255                                                                float   [deg] Slew Angle
    SLEWTIME [1]_          123.315                                                               float   [s] Slew Time
    SBPROF [1]_            BGS                                                                   str     Profile used by ETC
    ETCREAL [1]_           392.495819                                                            float   [s] ETC real open shutter time
    ETCTHRUB [1]_          0.964227                                                              float   ETC averaged thruput (BGS profile)
    ETCFRACE [1]_          0.45002                                                               float   ETC transparency weighted average of FFRAC (ELG
    ETCPROF [1]_           BGS                                                                   str     ETC source brightness profile
    ACTTEFF [1]_           226.882385                                                            float   [s] Actual effective exposure time
    ESTTIME [1]_           366.345                                                               float   [s] Estimated exposure time for visit (from ETC
    ETCTHRUP [1]_          1.034724                                                              float   ETC averaged thruput (PSF profile)
    PMTRANSP [1]_          98.17                                                                 float   [%] PlateMaker GFAPROC transparency
    ETCFRACP [1]_          0.634939                                                              float   ETC transparency weighted average of FFRAC (PSF
    ETCVERS [1]_           0.1.12-3-g12b54bb                                                     str     ETC version
    ETCFRACB [1]_          0.199883                                                              float   ETC transparency weighted average of FFRAC (BGS
    MAXTIME [1]_           5400.0                                                                float   [s] Maximum exposure time for entire visit (fro
    NTSPROG [1]_           BRIGHT                                                                str     NTS program name
    CONVERGD [1]_          F                                                                     bool    Positioning loop converged (CNFRC&gt;0.95)
    ETCTHRUE [1]_          0.999856                                                              float   ETC averaged thruput (ELG profile)
    ETCSKY [1]_            1.924707                                                              float   ETC averaged, normalized sky camera flux
    ETCSEENG [1]_          0.8906                                                                float   [arcsec] ETC seeing
    REQTEFF [1]_           220.0                                                                 float   [s] Requested effective exposure time
    USESPLITS [1]_         T                                                                     bool    Exposure splits are allowed
    UPSSTAT [1]_           17826.0                                                               float   UPS Status
    ====================== ===================================================================== ======= ===============================================

.. [1] Optional

Data: FITS image [float32, 2326x500]

HDU1
----

EXTNAME = IVAR

Inverse variance of sky model in units of (electrons per Ansgtrom)^-2.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2326             int
    NAXIS2   500              int
    CHECKSUM WMCiXJ9ZWJCfWJ9Z str  HDU checksum updated 2021-07-08T02:23:26
    DATASUM  3732109365       str  data unit checksum updated 2021-07-08T02:23:26
    ======== ================ ==== ==============================================

Data: FITS image [float32, 2326x500]

HDU2
----

EXTNAME = MASK

Sky mask; 0=good. See the :doc:`bitmask documentation </bitmasks>` page for the definition of the bits.
Prior to desispec/0.24.0 and software release 18.9, the MASK HDU was compressed.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2326             int
    NAXIS2   500              int
    BSCALE   1                int
    BZERO    2147483648       int
    CHECKSUM kIf3lGc0kGc0kGc0 str  HDU checksum updated 2021-07-08T02:23:26
    DATASUM  581500           str  data unit checksum updated 2021-07-08T02:23:26
    ======== ================ ==== ==============================================

Data: FITS image [int32, 2326x500]

HDU3
----

EXTNAME = WAVELENGTH

1D array of wavelengths, in Angstrom. Note the wavelength is in the solar system barycenter frame, so that the sky flux array
can be directly subtracted to the flat-fielded frame fluxes which are on the same wavelength grid. In order to compare the
sky spectrum of different exposures, or with litterature data, one has to convert back the wavelength array to the observer frame,
by dividing it by Doppler factor saved in header keyword HELIOCOR in HDU0. See also the frame :ref:`WAVELENGTH documentation <frame-hdu3-wavelength>` for more details.


Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2326             int
    BUNIT    Angstrom         str  Wavelength units
    CHECKSUM 7BAoAA3l7A9lAA9l str  HDU checksum updated 2021-07-08T02:23:26
    DATASUM  1502044794       str  data unit checksum updated 2021-07-08T02:23:26
    ======== ================ ==== ==============================================

Data: FITS image [float32, 2326]

HDU4
----

EXTNAME = STATIVAR

Statistical-only inverse variance of sky model.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2326             int
    NAXIS2   500              int
    CHECKSUM SAMkT5JjSAJjS3Jj str  HDU checksum updated 2021-07-08T02:23:27
    DATASUM  3877575180       str  data unit checksum updated 2021-07-08T02:23:27
    ======== ================ ==== ==============================================

Data: FITS image [float32, 2326x500]

HDU5
----

EXTNAME = THRPUTCORR

Multiplicative achromatic throughput correction per fiber. This term has been measured on the bright sky lines
of each fiber from the exposure (EXPID). It is used as a correction to the mean sky model.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   500              int
    CHECKSUM VPA5WO62VOA2VO52 str  HDU checksum updated 2021-07-08T02:23:27
    DATASUM  63793519         str  data unit checksum updated 2021-07-08T02:23:27
    ======== ================ ==== ==============================================

Data: FITS image [float32, 500]

HDU6
----

EXTNAME = THRPUTCORR_MOD

Model multiplicative throughput corrections for each fiber.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   500              int
    CHECKSUM VPA5WO62VOA2VO52 str  HDU checksum updated 2021-07-08T02:23:27
    DATASUM  63793519         str  data unit checksum updated 2021-07-08T02:23:27
    ======== ================ ==== ==============================================

Data: FITS image [float32, 500]

HDU7
----

EXTNAME = DWAVECOEFF

Vector of PCA coefficients for wavelength offsets.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   4                int
    CHECKSUM VPA5WO62VOA2VO52 str  HDU checksum updated 2021-07-08T02:23:27
    DATASUM  63793519         str  data unit checksum updated 2021-07-08T02:23:27
    ======== ================ ==== ==============================================

Data: FITS image [float32, 4]

HDU8
----

EXTNAME = DLSFCOEFF

Vector of PCA coefficients for LSF size changes.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   4                int
    CHECKSUM VPA5WO62VOA2VO52 str  HDU checksum updated 2021-07-08T02:23:27
    DATASUM  63793519         str  data unit checksum updated 2021-07-08T02:23:27
    ======== ================ ==== ==============================================

Data: FITS image [float32, 4]

HDU9
----

EXTNAME = SKYGRADPCACOEFF

Vector of gradient amplitudes for sky gradient spectra.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   4                int
    CHECKSUM VPA5WO62VOA2VO52 str  HDU checksum updated 2021-07-08T02:23:27
    DATASUM  63793519         str  data unit checksum updated 2021-07-08T02:23:27
    ======== ================ ==== ==============================================

Data: FITS image [float32, 4]
