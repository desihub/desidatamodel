=======================
frame-CAMERA-EXPID.fits
=======================

:Summary: Frame files contain the raw extracted electrons from DESI data, without
    any further calibration.
:Naming Convention: ``frame-{CAMERA}-{EXPID}.fits``, where ``{CAMERA}`` is
    one of the spectrograph cameras (*e.g.* ``z1``) and ``{EXPID}``
    is the 8-digit exposure ID.
:Regex: ``frame-[brz][0-9]-[0-9]{8}\.fits``
:File Type: FITS, 70 MB

Contents
========

====== ========== ======== ===================
Number EXTNAME    Type     Contents
====== ========== ======== ===================
HDU0_  FLUX       IMAGE    Extracted flux in electrons per Angstrom
HDU1_  IVAR       IMAGE    Inverse variance of the extracted flux
HDU2_  MASK       IMAGE    Bad value mask; 0=good
HDU3_  WAVELENGTH IMAGE    Wavelength grid of the extraction (Angstrom)
HDU3_  RESOLUTION IMAGE    Resolution matrix
HDU5_  FIBERMAP   BINTABLE Fibermap
HDU6_  CHI2PIX    IMAGE    chi2 of PSF fit to CCD pixels
====== ========== ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = FLUX

2D array of extracted flux[nspec, nwave] in units of electrons per Angstrom. nspec is the number of fibers per camera.
nwave in the length of the wavelength array. The spectra of all fibers share the same
wavelength grid (given in HDU WAVELENGTH).

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====================== ===================================================================== ======= ===============================================
    KEY                    Example Value                                                         Type    Comment
    ====================== ===================================================================== ======= ===============================================
    NAXIS1                 2326                                                                  int
    NAXIS2                 500                                                                   int
    EXPID                  68979                                                                 int     Exposure number
    EXPFRAME               0                                                                     int     Frame number
    FLAVOR                 science                                                               str     Observation type
    SEQUENCE               Spectrographs                                                         str     OCS Sequence name
    PURPOSE                Commissioning                                                         str     Purpose of observing night
    PROGRAM                CALIB DESI-CALIB-00 LEDs only                                         str     Program name
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
    DATE-OBS               2020-12-20T22:24:15.672815                                            str     [UTC] Observation data and start time
    TIME-OBS               22:24:15.672815                                                       str     [UTC] Observation start time
    MJD-OBS                59203.93351473                                                        float   Modified Julian Date of observation
    ST                     20:57:41.340                                                          str     Local Sidereal time at observation start (HH:MM
    EXPTIME                120.037                                                               float   [s] Actual exposure time
    DELTARA [1]_           0.0                                                                   float   [arcsec] Offset], right ascension, observer inp
    DELTADEC [1]_          0.0                                                                   float   [arcsec] Offset], declination, observer input
    VCCD                   ON                                                                    str     True (ON) if CCD voltage is on
    VCCDON                 2020-12-14T04:22:19.522101                                            str     Time when CCD voltage was turned on
    VCCDSEC                583485.8                                                              float   [s] CCD on time in seconds
    EQUINOX                2000.0                                                                float   Epoch of observation
    SPECGRPH               5                                                                     int     Spectrograph logical name (SP)
    SPECID                 9                                                                     int     Spectrograph serial number (SM)
    FEEBOX                 lbnl057                                                               str     CCD Controller serial number
    VESSEL                 26                                                                    int     Cryostat serial number
    FEEVER                 v20160312                                                             str     CCD Controller version
    FEEPOWER               ON                                                                    str     FEE power status
    FEEDMASK               2134851391                                                            int     FEE dac mask
    FEECMASK               1048575                                                               int     FEE clk mask
    CCDTEMP                -135.8073                                                             float   [deg C] CCD controller CCD temperature
    RADESYS                FK5                                                                   str     Coordinate reference frame of major/minor axes
    FILENAME               /exposures/desi/specs/20201220/00068979/sp9-00068979.fits.fz          str     Name
    DOSVER                 trunk                                                                 str     DOS software version
    OCSVER                 1.2                                                                   float   OCS software version
    CONSTVER               DESI:CURRENT                                                          str     Constants version
    INIFILE                /data/msdos/dos_home/architectures/kpno/desi.ini                      str     DOS Configuration
    DAC3                   -9.0002,-8.9919                                                       str     [V] set value, measured value
    CLOCK5                 9.9999,0.0                                                            str     [V] high rail, low rail
    BLDTIME                0.3522                                                                float   [s] Time to build image
    CLOCK2                 9.9999,0.0                                                            str     [V] high rail, low rail
    BIASSECD               [2129:2192, 2130:4193]                                                str     Bias section for quadrant D
    PGAGAIN                3                                                                     int     Controller gain
    OFFSET5                2.0,5.9964                                                            str     [V] set value, measured value
    BIASSECB               [2129:2192, 2:2065]                                                   str     Bias section for quadrant B
    CLOCK4                 9.9999,0.0                                                            str     [V] high rail, low rail
    ORSECD                 [2193:4249, 2098:2129]                                                str     Row bias section for quadrant D
    DAC2                   -9.0002,-8.9404                                                       str     [V] set value, measured value
    DAC6                   5.9998,6.0437                                                         str     [V] set value, measured value
    CCDPREP                purge,clear                                                           str     CCD prep actions
    CASETEMP               59.322                                                                float   [deg C] CCD controller case temperature
    DAC15                  0.0,-0.0148                                                           str     [V] set value, measured value
    DAC16                  39.9961,39.8706                                                       str     [V] set value, measured value
    DAC9                   -25.0003,-24.6344                                                     str     [V] set value, measured value
    AMPSECB                [4114:2058, 1:2064]                                                   str     AMP section for quadrant B
    DAC11                  -25.0003,-24.5157                                                     str     [V] set value, measured value
    DELAYS                 20, 20, 25, 40, 7, 3000, 7, 7, 7, 7                                   str     [10] Delay settings
    CLOCK13                9.9992,2.9993                                                         str     [V] high rail, low rail
    PRESECD                [4250:4256, 2130:4193]                                                str     Prescan section for quadrant D
    CDSPARMS               400, 400, 8, 2000                                                     str     CDS parameters
    DATASECD               [2193:4249, 2130:4193]                                                str     Data section for quadrant D
    CLOCK15                9.9992,2.9993                                                         str     [V] high rail, low rail
    CLOCK18                9.0,0.9999                                                            str     [V] high rail, low rail
    CLOCK8                 9.9992,2.9993                                                         str     [V] high rail, low rail
    OFFSET7                2.0,6.0122                                                            str     [V] set value, measured value
    DAC8                   -25.0003,-24.946                                                      str     [V] set value, measured value
    CCDSECC                [1:2057, 2065:4128]                                                   str     CCD section for quadrant C
    CLOCK14                9.9992,2.9993                                                         str     [V] high rail, low rail
    CLOCK3                 -2.0001,3.9999                                                        str     [V] high rail, low rail
    DIGITIME               47.5948                                                               float   [s] Time to digitize image
    CLOCK1                 9.9999,0.0                                                            str     [V] high rail, low rail
    PRRSECD                [2193:4249, 4194:4194]                                                str     Row prescan section for quadrant D
    CLOCK9                 9.9992,2.9993                                                         str     [V] high rail, low rail
    CCDNAME                CCDSM9R                                                               str     CCD name
    DETSECB                [2058:4114, 1:2064]                                                   str     Detector section for quadrant B
    CCDSECA                [1:2057, 1:2064]                                                      str     CCD section for quadrant A
    DETSECD                [2058:4114, 2065:4128]                                                str     Detector section for quadrant D
    DATASECB               [2193:4249, 2:2065]                                                   str     Data section for quadrant B
    CRYOPRES [1]_          1.166e-07                                                             str     [mb] Cryostat pressure (IP)
    CAMERA                 r5                                                                    str     Camera name
    PRRSECA                [8:2064, 1:1]                                                         str     Row prescan section for quadrant A
    DAC1                   -9.0002,-8.9507                                                       str     [V] set value, measured value
    PRESECC                [1:7, 2130:4193]                                                      str     Prescan section for quadrant C
    TRIMSECA               [8:2064, 2:2065]                                                      str     Trim section for quadrant A
    TRIMSECD               [2193:4249, 2130:4193]                                                str     Trim section for quadrant D
    CCDCFG                 default_lbnl_20190717.cfg                                             str     CCD configuration file
    PRRSECB                [2193:4249, 1:1]                                                      str     Row prescan section for quadrant B
    CLOCK12                9.9992,2.9993                                                         str     [V] high rail, low rail
    CCDSECB                [2058:4114, 1:2064]                                                   str     CCD section for quadrant B
    TRIMSECB               [2193:4249, 2:2065]                                                   str     Trim section for quadrant B
    DATASECA               [8:2064, 2:2065]                                                      str     Data section for quadrant A
    DAC17                  20.0008,12.3342                                                       str     [V] set value, measured value
    CLOCK17                9.0,0.9999                                                            str     [V] high rail, low rail
    PRESECB                [4250:4256, 2:2065]                                                   str     Prescan section for quadrant B
    CLOCK0                 9.9999,0.0                                                            str     [V] high rail, low rail
    PRESECA                [1:7, 2:2065]                                                         str     Prescan section for quadrant A
    ORSECA                 [8:2064, 2066:2097]                                                   str     Row overscan section for quadrant A
    BIASSECC               [2065:2128, 2130:4193]                                                str     Bias section for quadrant C
    DETSECC                [1:2057, 2065:4128]                                                   str     Detector section for quadrant C
    DAC14                  0.0,-0.0148                                                           str     [V] set value, measured value
    DAC4                   5.9998,6.0595                                                         str     [V] set value, measured value
    CLOCK16                9.9999,3.0                                                            str     [V] high rail, low rail
    AMPSECA                [1:2057, 1:2064]                                                      str     AMP section for quadrant A
    OFFSET4                2.0,6.0595                                                            str     [V] set value, measured value
    CCDSIZE                4194,4256                                                             str     CCD size in pixels (rows, columns)
    OFFSET2                0.4000000059604645,-8.9301                                            str     [V] set value, measured value
    DAC13                  0.0,-0.0148                                                           str     [V] set value, measured value
    CRYOTEMP [1]_          163.02                                                                float   [deg K] Cryostat CCD temperature
    OFFSET6                2.0,6.0437                                                            str     [V] set value, measured value
    CLOCK6                 9.9999,0.0                                                            str     [V] high rail, low rail
    DETSECA                [1:2057, 1:2064]                                                      str     Detector section for quadrant A
    CCDTMING               default_lbnl_timing_20180905.txt                                      str     CCD timing file
    DETECTOR               M1-52                                                                 str     Detector (ccd) identification
    OFFSET3                0.4000000059604645,-8.9816                                            str     [V] set value, measured value
    AMPSECC                [1:2057, 4128:2065]                                                   str     AMP section for quadrant C
    CLOCK10                9.9992,2.9993                                                         str     [V] high rail, low rail
    ORSECC                 [8:2064, 2098:2129]                                                   str     Row overscan section for quadrant C
    SETTINGS               detectors_sm_20191211.json                                            str     Name of DESI CCD settings file
    CPUTEMP                58.9629                                                               float   [deg C] CCD controller CPU temperature
    OFFSET0                0.4000000059604645,-8.755                                             str     [V] set value, measured value
    DAC12                  0.0,0.0                                                               str     [V] set value, measured value
    DATASECC               [8:2064, 2130:4193]                                                   str     Data section for quadrant C
    AMPSECD                [4114:2058, 4128:2065]                                                str     AMP section for quadrant D
    DAC10                  -25.0003,-25.0054                                                     str     [V] set value, measured value
    CLOCK7                 -2.0001,3.9999                                                        str     [V] high rail, low rail
    DAC0                   -9.0002,-8.7653                                                       str     [V] set value, measured value
    CLOCK11                9.9992,2.9993                                                         str     [V] high rail, low rail
    DAC7                   5.9998,6.0122                                                         str     [V] set value, measured value
    OFFSET1                0.4000000059604645,-8.9507                                            str     [V] set value, measured value
    DAC5                   5.9998,5.9964                                                         str     [V] set value, measured value
    ORSECB                 [2193:4249, 2066:2097]                                                str     Row overscan section for quadrant B
    CCDSECD                [2058:4114, 2065:4128]                                                str     CCD section for quadrant D
    PRRSECC                [8:2064, 4194:4194]                                                   str     Row prescan section for quadrant C
    TRIMSECC               [8:2064, 2130:4193]                                                   str     Trim section for quadrant C
    BIASSECA               [2065:2128, 2:2065]                                                   str     Bias section for quadrant A
    REQTIME                120.0                                                                 float   [s] Requested exposure time
    OBSID                  kp4m20201220t222415                                                   str     Unique observation identifier
    PROCTYPE               RAW                                                                   str     Data processing level
    PRODTYPE               image                                                                 str     Data product type
    CHECKSUM               WdnaWcnXWcnaWcnU                                                      str     HDU checksum updated 2022-01-29T01:11:31
    DATASUM                3935488568                                                            str     data unit checksum updated 2022-01-29T01:11:31
    GAINA                  1.684                                                                 float   e/ADU (gain applied to image)
    SATULEVA               33000.0                                                               float   saturation or non lin. level, in ADU, inc. bias
    OSTEPA                 0.6500495005602716                                                    float   ADUs (max-min of median overscan per row)
    OMETHA                 AVERAGE                                                               str     use average overscan
    OVERSCNA               1972.92976646288                                                      float   ADUs (gain not applied)
    OBSRDNA                3.218229918807175                                                     float   electrons (gain is applied)
    SATUELEA               52249.58627327651                                                     float   saturation or non lin. level, in electrons
    GAINB                  1.655                                                                 float   e/ADU (gain applied to image)
    SATULEVB               47000.0                                                               float   saturation or non lin. level, in ADU, inc. bias
    OSTEPB                 0.6179795354764792                                                    float   ADUs (max-min of median overscan per row)
    OMETHB                 AVERAGE                                                               str     use average overscan
    OVERSCNB               1975.23548556518                                                      float   ADUs (gain not applied)
    OBSRDNB                3.153470147761547                                                     float   electrons (gain is applied)
    SATUELEB               74515.98527138963                                                     float   saturation or non lin. level, in electrons
    GAINC                  1.467                                                                 float   e/ADU (gain applied to image)
    SATULEVC               65535.0                                                               float   saturation or non lin. level, in ADU, inc. bias
    OSTEPC                 0.5848174212296726                                                    float   ADUs (max-min of median overscan per row)
    OMETHC                 AVERAGE                                                               str     use average overscan
    OVERSCNC               1959.467167892971                                                     float   ADUs (gain not applied)
    OBSRDNC                2.894849081776217                                                     float   electrons (gain is applied)
    SATUELEC               93265.30666470101                                                     float   saturation or non lin. level, in electrons
    GAIND                  1.509                                                                 float   e/ADU (gain applied to image)
    SATULEVD               65535.0                                                               float   saturation or non lin. level, in ADU, inc. bias
    OSTEPD                 0.4709297982626595                                                    float   ADUs (max-min of median overscan per row)
    OMETHD                 AVERAGE                                                               str     use average overscan
    OVERSCND               1992.393350767962                                                     float   ADUs (gain not applied)
    OBSRDND                2.694583892275785                                                     float   electrons (gain is applied)
    SATUELED               95885.79343369114                                                     float   saturation or non lin. level, in electrons
    FIBERMIN               2500                                                                  int
    LONGSTRN               OGIP 1.0                                                              str     The OGIP Long String Convention may be used.
    MODULE                 CI                                                                    str     Image Sources/Component
    FRAMES [1]_            None                                                                  Unknown Number of Frames in Archive
    COSMSPLT               F                                                                     bool    Cosmics split exposure if true
    MAXSPLIT               0                                                                     int     Number of allowed exposure splits
    SPLITIDS [1]_          68979                                                                 str     List of expids for split exposures
    OBSTYPE                FLAT                                                                  str     Spectrograph observation type
    MANIFEST               F                                                                     bool    DOS exposure manifest
    OBJECT                                                                                       str     Object name
    SEQID [1]_             3 requests                                                            str     Exposure sequence identifier
    SEQNUM                 2                                                                     int     Number of exposure in sequence
    SEQTOT [1]_            3                                                                     int     Total number of exposures in sequence
    OPENSHUT               None                                                                  Unknown Time shutter opened
    CAMSHUT                open                                                                  str     Shutter status during observation
    WHITESPT [1]_          T                                                                     bool    Telescope is at whitespot
    ZENITH [1]_            F                                                                     bool    Telescope is at zenith
    SEANNEX [1]_           F                                                                     bool    Telescope is at SE annex
    BEYONDP [1]_           F                                                                     bool    Telescope is beyond pole
    FIDUCIAL [1]_          off                                                                   str     Fiducials status during observation
    AIRMASS [1]_           1.521306                                                              float   Airmass
    FOCUS [1]_             1163.9,-689.8,370.4,13.8,24.2,-0.0                                    str     Telescope focus settings
    TRUSTEMP [1]_          13.267                                                                float   [deg] Average Telescope truss temperature (only
    PMIRTEMP [1]_          7.35                                                                  float   [deg] Average primary mirror temperature (nit,e
    PMREADY [1]_           F                                                                     bool    Primary mirror ready
    PMCOVER [1]_           open                                                                  str     Primary mirror cover
    PMCOOL [1]_            on                                                                    str     Primary mirror cooling
    DOMSHUTU [1]_          not open                                                              str     Upper dome shutter
    DOMSHUTL [1]_          not open                                                              str     Lower dome shutter
    DOMLIGHH [1]_          off                                                                   str     High dome lights
    DOMLIGHL [1]_          off                                                                   str     Low dome lights
    DOMEAZ [1]_            253.289                                                               float   [deg] Dome azimuth angle
    DOMINPOS [1]_          F                                                                     bool    Dome is in position
    GUIDOFFR [1]_          0.0                                                                   float   [arcsec] Cummulative guider offset (RA)
    GUIDOFFD [1]_          -0.0                                                                  float   [arcsec] Cummulative guider offset (dec)
    MOONDEC [1]_           -9.830944                                                             float   [deg] Moon declination at start of exposure
    MOONRA [1]_            350.511461                                                            float   [deg] Moon RA at start of exposure
    MOUNTAZ [1]_           73.49407                                                              float   [deg] Mount azimuth angle
    MOUNTDEC [1]_          31.962703                                                             float   [deg] Mount declination
    MOUNTEL [1]_           41.035778                                                             float   [deg] Mount elevation angle
    MOUNTHA [1]_           -58.479517                                                            float   [deg] Mount hour angle
    INCTRL [1]_            F                                                                     bool    DESI in control
    INPOS [1]_             T                                                                     bool    Mount in position
    MNTOFFD [1]_           -0.0                                                                  float   [arcsec] Mount offset (dec)
    MNTOFFR [1]_           -0.0                                                                  float   [arcsec] Mount offset (RA)
    PARALLAC [1]_          -73.492813                                                            float   [deg] Parallactic angle
    SKYDEC [1]_            31.962703                                                             float   [deg] Telescope declination (pointing on sky)
    SKYRA [1]_             12.901561                                                             float   [deg] Telescope right ascension (pointing on sk
    TARGTDEC [1]_          31.963299                                                             float   [deg] Target declination (to TCS)
    TARGTRA [1]_           6.305086                                                              float   [deg] Target right ascension (to TCS)
    TARGTAZ [1]_           75.558672                                                             float   [deg] Target azimuth
    TARGTEL [1]_           46.429343                                                             float   [deg] Target elevation
    TRGTOFFD [1]_          0.0                                                                   float   [arcsec] Telescope target offset (dec)
    TRGTOFFR [1]_          0.0                                                                   float   [arcsec] Telescope target offset (RA)
    ZD [1]_                48.964222                                                             float   [deg] Telescope zenith distance
    TCSST [1]_             20:57:41.291                                                          str     Local Sidereal time reported by TCS (HH:MM:SS)
    TCSMJD [1]_            59203.933945                                                          float   MJD reported by TCS
    ADCCORR                F                                                                     bool    Correct pointing for ADC setting if True
    ADC1PHI [1]_           114.980003                                                            float   [deg] ADC 1 angle
    ADC2PHI [1]_           162.869907                                                            float   [deg] ADC 2 angle
    ADC1HOME [1]_          F                                                                     bool    ADC 1 at home position if True
    ADC2HOME [1]_          F                                                                     bool    ADC 2 at home position if True
    ADC1NREV [1]_          0.0                                                                   float   ADC 1 number of revs
    ADC2NREV [1]_          -1.0                                                                  float   ADC 2 number of revs
    ADC1STAT [1]_          STOPPED                                                               str     ADC 1 status
    ADC2STAT [1]_          STOPPED                                                               str     ADC 2 status
    HEXPOS [1]_            1163.9,-689.8,370.4,13.8,24.2,-0.0                                    str     Hexapod position
    HEXTRIM [1]_           0.0,0.0,0.0,0.0,0.0,0.0                                               str     Hexapod trim values
    ROTOFFST [1]_          0.0                                                                   float   [arcsec] Rotator offset
    ROTENBLD [1]_          T                                                                     bool    Rotator enabled
    ROTRATE [1]_           0.0                                                                   float   [arcsec/min] Rotator rate
    RESETROT               F                                                                     bool    DOS Control: reset hex rotator
    GUIDMODE               catalog                                                               str     Guider mode
    USEAOS [1]_            F                                                                     bool    DOS Control: AOS data available if true
    SPCGRPHS               SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                               str     Participating spectrograph
    ILLSPECS [1]_          SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                               str     Participating illuminate s
    CCDSPECS [1]_          SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                               str     Participating ccd spectrog
    TDEWPNT [1]_           -18.2                                                                 float   Telescope air dew point
    TAIRFLOW [1]_          1.121                                                                 float   Telescope air flow
    TAIRITMP [1]_          10.5                                                                  float   [deg] Telescope air in temperature
    TAIROTMP [1]_          5.5                                                                   float   [deg] Telescope air out temperature
    TAIRTEMP [1]_          11.86                                                                 float   [deg] Telescope air temperature
    TCASITMP [1]_          0.0                                                                   float   [deg] Telescope Cass Cage in temperature
    TCASOTMP [1]_          9.6                                                                   float   [deg] Telescope Cass Cage out temperature
    TCSITEMP [1]_          7.4                                                                   float   [deg] Telescope center section in temperature
    TCSOTEMP [1]_          10.2                                                                  float   [deg] Telescope center section out temperature
    TCIBTEMP [1]_          0.0                                                                   float   [deg] Telescope chimney IB temperature
    TCIMTEMP [1]_          0.0                                                                   float   [deg] Telescope chimney IM temperature
    TCITTEMP [1]_          0.0                                                                   float   [deg] Telescope chimney IT temperature
    TCOSTEMP [1]_          0.0                                                                   float   [deg] Telescope chimney OS temperature
    TCOWTEMP [1]_          0.0                                                                   float   [deg] Telescope chimney OW temperature
    TDBTEMP [1]_           7.4                                                                   float   [deg] Telescope dec bore temperature
    TFLOWIN [1]_           7.7                                                                   float   Telescope flow rate in
    TFLOWOUT [1]_          8.3                                                                   float   Telescope flow rate out
    TGLYCOLI [1]_          -1.8                                                                  float   [deg] Telescope glycol in temperature
    TGLYCOLO [1]_          0.0                                                                   float   [deg] Telescope glycol out temperature
    THINGES [1]_           12.9                                                                  float   [deg] Telescope hinge S temperature
    THINGEW [1]_           11.7                                                                  float   [deg] Telescope hinge W temperature
    TPMAVERT [1]_          7.304                                                                 float   [deg] Telescope mirror averagetemperature
    TPMDESIT [1]_          7.0                                                                   float   [deg] Telescope mirror desired temperature
    TPMEIBT [1]_           7.3                                                                   float   [deg] Telescope mirror EIB temperature
    TPMEITT [1]_           7.3                                                                   float   [deg] Telescope mirror EIT temperature
    TPMEOBT [1]_           7.4                                                                   float   [deg] Telescope mirror EOB temperature
    TPMEOTT [1]_           7.2                                                                   float   [deg] Telescope mirror EOT temperature
    TPMNIBT [1]_           7.4                                                                   float   [deg] Telescope mirror NIB temperature
    TPMNITT [1]_           7.3                                                                   float   [deg] Telescope mirror NIT temperature
    TPMNOBT [1]_           7.7                                                                   float   [deg] Telescope mirror NOB temperature
    TPMNOTT [1]_           7.6                                                                   float   [deg] Telescope mirror NOT temperature
    TPMRTDT [1]_           6.96                                                                  float   [deg] Telescope mirror RTD temperature
    TPMSIBT [1]_           7.4                                                                   float   [deg] Telescope mirror SIB temperature
    TPMSITT [1]_           7.0                                                                   float   [deg] Telescope mirror SIT temperature
    TPMSOBT [1]_           7.4                                                                   float   [deg] Telescope mirror SOB temperature
    TPMSOTT [1]_           7.2                                                                   float   [deg] Telescope mirror SOT temperature
    TPMSTAT [1]_           soft air                                                              str     Telescope mirror status
    TPMWIBT [1]_           7.2                                                                   float   [deg] Telescope mirror WIB temperature
    TPMWITT [1]_           7.1                                                                   float   [deg] Telescope mirror WIT temperature
    TPMWOBT [1]_           7.6                                                                   float   [deg] Telescope mirror WOB temperature
    TPMWOTT [1]_           8.1                                                                   float   [deg] Telescope mirror WOT temperature
    TPCITEMP [1]_          7.7                                                                   float   [deg] Telescope primary cell in temperature
    TPCOTEMP [1]_          7.7                                                                   float   [deg] Telescope primary cell out temperature
    TPR1HUM [1]_           0.0                                                                   float   Telescope probe 1 humidity
    TPR1TEMP [1]_          0.0                                                                   float   [deg] Telescope probe1 temperature
    TPR2HUM [1]_           0.0                                                                   float   Telescope probe 2 humidity
    TPR2TEMP [1]_          0.0                                                                   float   [deg] Telescope probe2 temperature
    TSERVO [1]_            7.0                                                                   float   Telescope servo setpoint
    TTRSTEMP [1]_          13.2                                                                  float   [deg] Telescope top ring S temperature
    TTRWTEMP [1]_          13.4                                                                  float   [deg] Telescope top ring W temperature
    TTRUETBT [1]_          -4.8                                                                  float   [deg] Telescope truss ETB temperature
    TTRUETTT [1]_          11.5                                                                  float   [deg] Telescope truss ETT temperature
    TTRUNTBT [1]_          10.9                                                                  float   [deg] Telescope truss NTB temperature
    TTRUNTTT [1]_          11.8                                                                  float   [deg] Telescope truss NTT temperature
    TTRUSTBT [1]_          11.1                                                                  float   [deg] Telescope truss STB temperature
    TTRUSTST [1]_          10.8                                                                  float   [deg] Telescope truss STS temperature
    TTRUSTTT [1]_          12.4                                                                  float   [deg] Telescope truss STT temperature
    TTRUTSBT [1]_          13.6                                                                  float   [deg] Telescope truss TSB temperature
    TTRUTSMT [1]_          13.7                                                                  float   [deg] Telescope truss TSM temperature
    TTRUTSTT [1]_          12.5                                                                  float   [deg] Telescope truss TST temperature
    TTRUWTBT [1]_          10.9                                                                  float   [deg] Telescope truss WTB temperature
    TTRUWTTT [1]_          11.6                                                                  float   [deg] Telescope truss WTT temperature
    ALARM [1]_             F                                                                     bool    UPS major alarm or check battery
    ALARM-ON [1]_          F                                                                     bool    UPS active alarm condition
    BATTERY [1]_           100.0                                                                 float   [%] UPS Battery left
    SECLEFT [1]_           5772.0                                                                float   [s] UPS Seconds left
    UPSSTAT [1]_           System Normal - On Line(7)                                            str     UPS Status
    INAMPS [1]_            64.3                                                                  float   [A] UPS total input current
    OUTWATTS [1]_          4500.0,6800.0,4100.0                                                  str     [W] UPS Phase A, B, C output watts
    COMPDEW [1]_           -12.0                                                                 float   [deg C] Computer room dewpoint
    COMPHUM [1]_           7.8                                                                   float   [%] Computer room humidity
    COMPAMB [1]_           19.4                                                                  float   [deg C] Computer room ambient temperature
    COMPTEMP [1]_          24.9                                                                  float   [deg C] Computer room hygrometer temperature
    DEWPOINT [1]_          5.7                                                                   float   [deg C] (outside) dewpoint
    HUMIDITY [1]_          7.0                                                                   float   [%] (outside) humidity
    PRESSURE [1]_          794.7                                                                 float   [torr] (outside) air pressure
    OUTTEMP [1]_           0.0                                                                   float   [deg C] outside temperature
    WINDDIR [1]_           82.0                                                                  float   [deg] wind direction
    WINDSPD [1]_           23.3                                                                  float   [m/s] wind speed
    GUST [1]_              18.1                                                                  float   [m/s] Wind gusts speed
    AMNIENTN [1]_          13.3                                                                  float   [deg C] ambient temperature north
    CFLOOR [1]_            8.1                                                                   float   [deg C] temperature on C floor
    NWALLIN [1]_           13.6                                                                  float   [deg C] temperature at north wall inside
    NWALLOUT [1]_          8.8                                                                   float   [deg C] temperature at north wall outside
    WWALLIN [1]_           12.8                                                                  float   [deg C] temperature at west wall inside
    WWALLOUT [1]_          9.4                                                                   float   [deg C] temperature at west wall outside
    AMBIENTS [1]_          14.6                                                                  float   [deg C] ambient temperature south
    FLOOR [1]_             12.3                                                                  float   [deg C] temperature at floor (LCR)
    EWALLCMP [1]_          10.2                                                                  float   [deg C] temperature at east wall, computer room
    EWALLCOU [1]_          9.5                                                                   float   [deg C] temperature at east wall, Coude room
    ROOF [1]_              10.0                                                                  float   [deg C] temperature on roof
    ROOFAMB [1]_           9.9                                                                   float   [deg C] ambient temperature on roof
    DOMEBLOW [1]_          12.1                                                                  float   [deg C] temperature at dome back, lower
    DOMEBUP [1]_           12.5                                                                  float   [deg C] temperature at dome back, upper
    DOMELLOW [1]_          14.4                                                                  float   [deg C] temperature at dome left, lower
    DOMELUP [1]_           19.3                                                                  float   [deg C] temperature at dome left, upper
    DOMERLOW [1]_          12.3                                                                  float   [deg C] temperature at dome right, lower
    DOMERUP [1]_           12.8                                                                  float   [deg C] temperature at dome right, upper
    PLATFORM [1]_          15.3                                                                  float   [deg C] temperature at platform
    SHACKC [1]_            15.2                                                                  float   [deg C] temperature at shack ceiling
    SHACKW [1]_            13.2                                                                  float   [deg C] temperature at shack wall
    STAIRSL [1]_           12.6                                                                  float   [deg C] temperature at stairs, lower
    STAIRSM [1]_           13.3                                                                  float   [deg C] temperature at stairs, mid
    STAIRSU [1]_           13.6                                                                  float   [deg C] temperature at stairs, upper
    TELBASE [1]_           8.5                                                                   float   [deg C] temperature at telescope base
    UTILWALL [1]_          11.6                                                                  float   [deg C] temperature at utility room wall
    UTILROOM [1]_          12.4                                                                  float   [deg C] temperature in utilitiy room
    EXCLUDED                                                                                     str     Components excluded from this exposure
    NSPEC                  500                                                                   int     Number of spectra
    WAVEMIN                5760.0                                                                float   First wavelength [Angstroms]
    WAVEMAX                7620.0                                                                float   Last wavelength [Angstroms]
    WAVESTEP               0.8                                                                   float   Wavelength step size [Angstroms]
    SPECTER                0.10.0                                                                str     https://github.com/desihub/specter
    IN_PSF                 SPECPROD/exposures/20201220/00068979/psf-r5-00068979.fits             str     Input sp
    IN_IMG                 SPECPROD/preproc/20201220/00068979/preproc-r5-00068979.fits           str
    ORIG_PSF               SPECPROD/calibnight/20201220/psfnight-r5-20201220.fits                str
    BUNIT                  electron/Angstrom                                                     str
    TCSPIRA [1]_           1.0,0.0,0.0,0.0                                                       str     TCS PI settings (P, I (gain, error window, satu
    SEQSTART [1]_          2021-02-24T01:22:15.381414                                            str     Start time of sequence processing
    TCSPIDEC [1]_          1.0,0.0,0.0,0.0                                                       str     TCS PI settings (P, I (gain, error window, satu
    MOONSEP [1]_           8.81573236983626                                                      float   [deg] Moon Separation
    TCSKRA [1]_            0.3 0.003 0.00003                                                     str     TCS Kalman (RA)
    TCSMFRA [1]_           1                                                                     int     TCS moving filter length (RA)
    TCSGRA [1]_            0.3                                                                   float   TCS simple gain (RA)
    TCSKDEC [1]_           0.3 0.003 0.00003                                                     str     TCS Kalman (dec)
    TCSGDEC [1]_           0.3                                                                   float   TCS simple gain (dec)
    TCSMFDEC [1]_          1                                                                     int     TCS moving filter length (dec)
    FOCSTIME [1]_          60.0                                                                  float   [s] focus GFA exposure time
    KEEPSKY [1]_           F                                                                     bool    DOS Control: keep sky mon. running
    PMTRANS [1]_           94.62                                                                 float   [%] PlateMaker GFAPROC transparency
    USESPCTR [1]_          T                                                                     bool    DOS Control: use spectrographs
    SUNRA [1]_             12.514241                                                             float   [deg] Sun RA at start of exposure
    SP3BLUP [1]_           8.133e-08                                                             float   [mb] SP3 blue pressure
    BACKLIT [1]_           off                                                                   str     Fibers are backlit if True
    SP6REDT [1]_           139.94                                                                float   [K] SP6 red temperature
    USEILLUM [1]_          T                                                                     bool    DOS Control: use illuminator
    SP8REDP [1]_           3.96e-08                                                              float   [mb] SP8 red pressure
    NTSSURVY [1]_          na                                                                    str     NTS survey name
    POSCYCLE [1]_          1                                                                     int     Number of current iteration
    POSTOLER [1]_          0.005                                                                 float   Positioning Control: in_position tolerance (mm)
    SP7REDT [1]_           140.01                                                                float   [K] SP7 red temperature
    SP0NIRT [1]_           139.89                                                                float   [K] SP0 NIR temperature
    SP7NIRP [1]_           4.311e-08                                                             float   [mb] SP7 NIR pressure
    SP0NIRP [1]_           5.998e-08                                                             float   [mb] SP0 NIR pressure
    SP6NIRT [1]_           139.89                                                                float   [K] SP6 NIR temperature
    SP1BLUT [1]_           163.02                                                                float   [K] SP1 blue temperature
    SP3REDT [1]_           139.99                                                                float   [K] SP3 red temperature
    SP4NIRP [1]_           6.683e-08                                                             float   [mb] SP4 NIR pressure
    SP5NIRT [1]_           139.94                                                                float   [K] SP5 NIR temperature
    TGFAPROC [1]_          9.0024                                                                float   [s] PlateMaker GFAPROC processing time
    SP7BLUP [1]_           9.947e-08                                                             float   [mb] SP7 blue pressure
    SKYLEVEL [1]_          1.364                                                                 float   counts?] ETC sky level
    SP0REDT [1]_           139.96                                                                float   [K] SP0 red temperature
    USEOPENL [1]_          T                                                                     bool    DOS Control: use open loop move
    SP0BLUT [1]_           163.02                                                                float   [K] SP0 blue temperature
    SP2BLUP [1]_           8.492e-08                                                             float   [mb] SP2 blue pressure
    SP0BLUP [1]_           8.499e-08                                                             float   [mb] SP0 blue pressure
    POSCNVGD [1]_          F                                                                     bool    Number of positioners converged
    USEFOCUS [1]_          T                                                                     bool    DOS Control: use focus
    ACQCAM [1]_            GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                             str     Acquisition cameras used
    GUIEXPID [1]_          83129                                                                 int     Guider exposure id at start of spectro exp.
    SP3NIRP [1]_           3.566e-08                                                             float   [mb] SP3 NIR pressure
    SP5BLUT [1]_           162.99                                                                float   [K] SP5 blue temperature
    SP9NIRP [1]_           5.211e-08                                                             float   [mb] SP9 NIR pressure
    USEFVC [1]_            T                                                                     bool    DOS Control: use fvc
    USEGUIDR [1]_          T                                                                     bool    DOS Control: use guider
    IGFRMNUM [1]_          14                                                                    int     Guider frame number at start of spectro exp.
    FGFRMNUM [1]_          45                                                                    int     Guider frame number at end of spectro exp.
    SP4BLUP [1]_           6.248e-08                                                             float   [mb] SP4 blue pressure
    SP5BLUP [1]_           1.115e-07                                                             float   [mb] SP5 blue pressure
    SP1REDT [1]_           139.89                                                                float   [K] SP1 red temperature
    SP9BLUT [1]_           163.02                                                                float   [K] SP9 blue temperature
    IFFRMNUM [1]_          1                                                                     int     Focus frame number at start of spectro exp.
    SP1NIRT [1]_           139.89                                                                float   [K] SP1 NIR temperature
    USEFID [1]_            T                                                                     bool    DOS Control: use fiducials
    REQDEC [1]_            32.375                                                                float   [deg] Requested declination (observer input)
    SP9REDP [1]_           5.108e-08                                                             float   [mb] SP9 red pressure
    SP2REDP [1]_           6.944e-08                                                             float   [mb] SP2 red pressure
    USESKY [1]_            T                                                                     bool    DOS Control: use Sky Monitor
    SP6NIRP [1]_           2.809e-07                                                             float   [mb] SP6 NIR pressure
    SP4NIRT [1]_           139.94                                                                float   [K] SP4 NIR temperature
    USEPOS [1]_            T                                                                     bool    Fiber positioner data available if true
    SP2BLUT [1]_           163.02                                                                float   [K] SP2 blue temperature
    ISFRMNUM [1]_          0                                                                     int     Sky frame number at start of spectro exp.
    FOCEXPID [1]_          83129                                                                 int     Focus exposure id at start of spectro exp.
    POSENABL [1]_          4056                                                                  int     Number of enabled positioners
    SUNDEC [1]_            5.365754                                                              float   [deg] Sun declination at start of exposure
    TILEDEC [1]_           32.375                                                                float   DEC of tile given in fiberassign file
    POSFRACT [1]_          0.95                                                                  float
    SP9NIRT [1]_           139.86                                                                float   [K] SP9 NIR temperature
    SPLITEXP [1]_          F                                                                     bool    Split exposure part of a visit
    SP8REDT [1]_           139.94                                                                float   [K] SP8 red temperature
    SKYEXPID [1]_          83129                                                                 int     Sky exposure id at start of spectro exp.
    SP4REDT [1]_           140.01                                                                float   [K] SP4 red temperature
    TILERA [1]_            127.7                                                                 float   RA of tile given in fiberassign file
    KEEPGUDR [1]_          F                                                                     bool    DOS Control: keep guider running
    SP3BLUT [1]_           163.02                                                                float   [K] SP3 blue temperature
    SP0REDP [1]_           6.295e-08                                                             float   [mb] SP0 red pressure
    SP6BLUT [1]_           163.02                                                                float   [K] SP6 blue temperature
    SIMGFAP [1]_           F                                                                     bool    DOS Control: simulate GFAPROC
    TILEID [1]_            80873                                                                 int     DESI Tile ID
    SP1NIRP [1]_           4.585e-08                                                             float   [mb] SP1 NIR pressure
    USEDONUT [1]_          T                                                                     bool    DOS Control: use donuts
    FIBASSGN [1]_          /data/tiles/SVN_tiles/080/fiberassign-080873.fits.gz                  str     Fiber assign
    SP8NIRT [1]_           139.99                                                                float   [K] SP8 NIR temperature
    SP2NIRT [1]_           139.89                                                                float   [K] SP2 NIR temperature
    KEEPFOCS [1]_          F                                                                     bool    DOS Control: keep focus running
    VISITIDS [1]_          83129                                                                 str     List of expids for a visit (same tile)
    FFFRMNUM [1]_          5                                                                     int     Focus frame number at end of spectro exp.
    SP8BLUP [1]_           7.959e-08                                                             float   [mb] SP8 blue pressure
    ACTTEFF [1]_           112.2149                                                              float   [s] Actual effective exposure time
    POSMVALL [1]_          T                                                                     bool    Positioning Control: move all positioners
    SP6BLUP [1]_           6.3e-08                                                               float   [mb] SP6 blue pressure
    GUIDTIME [1]_          5.0                                                                   float   [s] guider GFA exposure time
    SEEING [1]_            1.3508                                                                float   [arcsec] ETC seeing
    SP3REDP [1]_           7.919e-08                                                             float   [mb] SP3 red pressure
    USEETC [1]_            T                                                                     bool    ETC data available if true
    SP5REDT [1]_           139.99                                                                float   [K] SP5 red temperature
    SP6REDP [1]_           6.337e-08                                                             float   [mb] SP6 red pressure
    SP8NIRP [1]_           4.827e-08                                                             float   [mb] SP8 NIR pressure
    USEROTAT [1]_          T                                                                     bool    DOS Control: use rotator
    SP2NIRP [1]_           6.984e-08                                                             float   [mb] SP2 NIR pressure
    POSONFRC [1]_          0.4768                                                                float   Fraction of positioners on target
    PETALS [1]_            PETAL0,PETAL1,PETAL2,PETAL3,PETAL4,PETAL5,PETAL6,PETAL7,PETAL8,PETAL9 str     Participating petals
    STOPSKY [1]_           T                                                                     bool    DOS Control: stop sky monitor
    SP7REDP [1]_           6.038e-08                                                             float   [mb] SP7 red pressure
    GUIDECAM [1]_          GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                             str     Guide cameras used for t
    SP8BLUT [1]_           162.9                                                                 float   [K] SP8 blue temperature
    TNFSPROC [1]_          25.9483                                                               float   [s] PlateMaker NFSPROC processing time
    HELIOCOR [1]_          0.9999087550219705                                                    float
    ACQTIME [1]_           15.0                                                                  float   [s] acqusition image exposure time
    REQADC [1]_            92.63,97.66                                                           str     [deg] requested ADC angles
    SP4BLUT [1]_           163.02                                                                float   [K] SP4 blue temperature
    SP7NIRT [1]_           139.96                                                                float   [K] SP7 NIR temperature
    SP9REDT [1]_           139.99                                                                float   [K] SP9 red temperature
    POSRMS [1]_            0.0076                                                                float   [micron] RMS of positioner accuracy
    REACQUIR [1]_          F                                                                     bool    DOS Control: reacquire same files
    SP5REDP [1]_           5.487e-08                                                             float   [mb] SP5 red pressure
    STOPGUDR [1]_          T                                                                     bool    DOS Control: stop guider
    POSONTGT [1]_          1934                                                                  int     Number of positioners on target
    FOCUSCAM [1]_          FOCUS1,FOCUS4,FOCUS6,FOCUS9                                           str     Focus cameras used for this exposure
    SP5NIRP [1]_           6.003e-08                                                             float   [mb] SP5 NIR pressure
    SP1BLUP [1]_           7.992e-08                                                             float   [mb] SP1 blue pressure
    PMSEEING [1]_          1.33                                                                  float   [arcsec] PlateMaker GFAPROC seeing
    SP9BLUP [1]_           1.231e-07                                                             float   [mb] SP9 blue pressure
    SKYTIME [1]_           60                                                                    float   [s] sky camera exposure time (acquisition)
    POSITER [1]_           1                                                                     int     Positioning Control: max. number of pos. cycles
    USESPLITS [1]_         T                                                                     bool    Exposure splits are allowed
    SP1REDP [1]_           5.506e-08                                                             float   [mb] SP1 red pressure
    SP3NIRT [1]_           140.01                                                                float   [K] SP3 NIR temperature
    SP2REDT [1]_           139.96                                                                float   [K] SP2 red temperature
    SKYCAM [1]_            SKYCAM0,SKYCAM1                                                       str     Sky cameras used for this exposure
    SP4REDP [1]_           4.945e-08                                                             float   [mb] SP4 red pressure
    SP7BLUT [1]_           163.02                                                                float   [K] SP7 blue temperature
    FSFRMNUM [1]_          3                                                                     int     Sky frame number at end of spectro exp.
    SIMGFACQ [1]_          F                                                                     bool
    REQRA [1]_             127.7                                                                 float   [deg] Requested right ascension (observer input
    USEXSRVR [1]_          T                                                                     bool    DOS Control: use exposure server
    POSDISAB [1]_          925                                                                   int     Number of disabled positioners
    STOPFOCS [1]_          T                                                                     bool    DOS Control: stop focus
    REQTEFF [1]_           1000.0                                                                float   [s] Requested effective exposure time
    USESPLIT [1]_          T                                                                     bool    Exposure splits are allowed
    TOTTEFF [1]_           838.56                                                                float   [s] Total effective exposure time for visit
    BBKGMINA [1]_          -0.3947016321413652                                                   float
    BBKGMINC [1]_          -0.2673014085831243                                                   float
    BBKGMIND [1]_          -0.4786751204310712                                                   float
    BBKGMAXA [1]_          0.6036115648904081                                                    float
    BBKGMAXD [1]_          0.2858693184663221                                                    float
    BBKGMAXB [1]_          0.2978123984653912                                                    float
    BBKGMAXC [1]_          0.3636081010150568                                                    float
    BBKGMINB [1]_          -0.2841325038108138                                                   float
    POSCVFRC [1]_          0.3467                                                                float   Fraction of converged positioners
    ETCSPLIT [1]_          1                                                                     int     ETC split sequence number for this visit
    ACQFWHM [1]_           1.71791                                                               float   [arcsec] FWHM of guide star PSF in acquisition
    TRANSPAR [1]_          None                                                                  Unknown ETC/PM transparency
    NTSPROG [1]_           BRIGHT                                                                str     NTS program name
    SLEWANGL [1]_          28.856                                                                float   [deg] Slew Angle
    ESTTIME [1]_           2231.315                                                              float   [s] Estimated exposure time for visit (from ETC
    ETCPREV [1]_           0.0                                                                   float   [s] ETC cummulative t_eff for visit
    ETCTRANS [1]_          0.719235                                                              float   ETC averaged TRANSP normalized to 1
    MINTIME [1]_           120.0                                                                 float   [s] Minimum exposure time (from NTS, used by ET
    ETCTHRUP [1]_          0.442956                                                              float   ETC averaged thruput (PSF profile)
    ETCTEFF [1]_           222.548355                                                            float   [s] ETC effective exposure time
    ETCSKY [1]_            1.43154                                                               float   ETC averaged, normalized sky camera flux
    ETCVERS [1]_           0.1.12-3-g12b54bb                                                     str     ETC version
    ETCFRACE [1]_          0.271983                                                              float   ETC transparency weighted average of FFRAC (ELG
    ETCREAL [1]_           1054.206299                                                           float   [s] ETC real open shutter time
    ETCPROF [1]_           BGS                                                                   str     ETC source brightness profile
    CONVERGD [1]_          F                                                                     bool    Positioning loop converged (CNFRC&gt;0.95)
    ETCSEENG [1]_          1.7179                                                                float   [arcsec] ETC seeing
    ETCTHRUB [1]_          0.469155                                                              float   ETC averaged thruput (BGS profile)
    PMTRANSP [1]_          104.71                                                                float   [%] PlateMaker GFAPROC transparency
    ETCFRACB [1]_          0.123838                                                              float   ETC transparency weighted average of FFRAC (BGS
    SBPROF [1]_            BGS                                                                   str     Profile used by ETC
    ETCFRACP [1]_          0.346107                                                              float   ETC transparency weighted average of FFRAC (PSF
    ETCTHRUE [1]_          0.474574                                                              float   ETC averaged thruput (ELG profile)
    MAXTIME [1]_           5400.0                                                                float   [s] Maximum exposure time for entire visit (fro
    FVCTIME [1]_           2.0                                                                   float   [s] FVC exposure time
    UPSSTAT [1]_           17826.0                                                               float   UPS Status
    ====================== ===================================================================== ======= ===============================================

Data: FITS image [float32, 2751x500]

HDU1
----

EXTNAME = IVAR

Inverse variance of the flux values in HDU0. The unit is 1/(electrons/Angstrom)^2. The noise from neighboring spectral pixels is uncorrelated.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2751             int  Number of wavelengths
    NAXIS2   500              int  Number of spectra
    CHECKSUM YgRiaZOfTdOfYZOf str  HDU checksum updated 2021-07-08T12:56:13
    DATASUM  2402704670       str  data unit checksum updated 2021-07-08T12:56:13
    ======== ================ ==== ==============================================

Data: FITS image [float32, 2751x500]

HDU2
----

EXTNAME = MASK

Mask of spectral data; 0=good. See the :doc:`bitmask documentation </bitmasks>` page for the definition of the bits.
Prior to desispec/0.24.0 and software release 18.9, the MASK HDU was compressed.


Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2751             int  Number of wavelengths
    NAXIS2   500              int  Number of spectra
    BSCALE   1                int
    BZERO    2147483648       int
    CHECKSUM 9GbI9FbG9FbG9FbG str  HDU checksum updated 2021-07-08T12:56:14
    DATASUM  688701           str  data unit checksum updated 2021-07-08T12:56:14
    ======== ================ ==== ==============================================

Data: FITS image [int32, 2751x500]

.. _frame-hdu3-wavelength:

HDU3
----

EXTNAME = WAVELENGTH

1D array of wavelengths in Angstrom, in vacuum (not in air). For science exposures (in opposition to calibration exposures), the wavelength in is the rest frame of the solar system barycenter. The Doppler factor applied to the observed wavelength at the telescope to convert them to the barycentric frame is saved in header keyword HELIOCOR in HDU0. In other words, WAVELENGTH = BARYCENTRIC_FRAME_WAVELENGTH = HELICOR * OBSERVER_FRAME_WAVELENGTH. Note a single factor has been applied to all fibers despite a small difference in pointing.


Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2751             int  Number of wavelengths
    BUNIT    Angstrom         str
    CHECKSUM 9GQG9DPE9DPE9DPE str  HDU checksum updated 2021-07-08T12:56:14
    DATASUM  979185614        str  data unit checksum updated 2021-07-08T12:56:14
    ======== ================ ==== ==============================================

Data: FITS image [float64, 2751]

.. _frame-hdu4-resolution:

HDU4
----

EXTNAME = RESOLUTION

Resolution matrix stored as a 3D sparse matrix:

Rdata[nspec, ndiag, nwave]

To convert this into sparse matrices for convolving a model that is sampled
at the same wavelengths as the extractions (HDU EXTNAME='WAVELENGTH'):

.. code::

    from scipy.sparse import spdiags
    from astropy.io import fits
    import numpy as np

    #- read a model and its wavelength vector from somewhere
    #- IMPORTANT: cast them to .astype(np.float64) to get native endian

    #- read the resolution data
    resdata = fits.getdata(framefile, 'RESOLUTION').astype(np.float64)

    nspec, nwave = model.shape
    convolvedmodel = np.zeros((nspec, nwave))
    diags = np.arange(10, -11, -1)

    for i in range(nspec):
        R = spdiags(resdata[i], diags, nwave, nwave)
        convolvedmodel[i] = R.dot(model)


Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2751             int
    NAXIS2   11               int
    NAXIS3   500              int
    CHECKSUM YGfeaGcdSGcdYGcd str  HDU checksum updated 2021-07-08T12:56:17
    DATASUM  307167897        str  data unit checksum updated 2021-07-08T12:56:17
    ======== ================ ==== ==============================================

Data: FITS image [float32, 2751x11x500]

HDU5
----

EXTNAME = FIBERMAP

Fibermap information combining fiberassign request with actual fiber locations. See also the :doc:`fibermap documentation </DESI_SPECTRO_REDUX/SPECPROD/preproc/NIGHT/EXPID/fibermap-EXPID>` page.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====================== ==================================================================================================================================================================================================== ======= ==============================================
    KEY                    Example Value                                                                                                                                                                                        Type    Comment
    ====================== ==================================================================================================================================================================================================== ======= ==============================================
    NAXIS1                 369                                                                                                                                                                                                  int     length of dimension 1
    NAXIS2                 500                                                                                                                                                                                                  int     length of dimension 2
    EXPID                  68979                                                                                                                                                                                                int
    EXPFRAME               0                                                                                                                                                                                                    int
    FLAVOR                 science                                                                                                                                                                                              str
    SEQUENCE               Spectrographs                                                                                                                                                                                        str
    PURPOSE                Commissioning                                                                                                                                                                                        str
    PROGRAM                CALIB DESI-CALIB-00 LEDs only                                                                                                                                                                        str
    PROPID                 2019B-5000                                                                                                                                                                                           str
    OBSERVER               DESIObserver                                                                                                                                                                                         str
    LEAD                   RunManager                                                                                                                                                                                           str
    INSTRUME               DESI                                                                                                                                                                                                 str
    OBSERVAT               KPNO                                                                                                                                                                                                 str
    OBS-LAT                31.96403                                                                                                                                                                                             str
    OBS-LONG               -111.59989                                                                                                                                                                                           str
    OBS-ELEV               2097.0                                                                                                                                                                                               float
    TELESCOP               KPNO 4.0-m telescope                                                                                                                                                                                 str
    CORRCTOR               DESI Corrector                                                                                                                                                                                       str
    NIGHT                  20201220                                                                                                                                                                                             int
    TIMESYS                UTC                                                                                                                                                                                                  str
    DATE-OBS               2020-12-20T22:24:15.672815                                                                                                                                                                           str
    TIME-OBS               22:24:15.672815                                                                                                                                                                                      str
    MJD-OBS                59203.93351473                                                                                                                                                                                       float
    ST                     20:57:41.340                                                                                                                                                                                         str
    EXPTIME                120.037                                                                                                                                                                                              float
    DELTARA [1]_           0.0                                                                                                                                                                                                  float
    DELTADEC [1]_          0.0                                                                                                                                                                                                  float
    VCCD                   ON                                                                                                                                                                                                   str
    VCCDON                 2020-12-14T04:22:19.522101                                                                                                                                                                           str
    VCCDSEC                583485.8                                                                                                                                                                                             float
    EQUINOX                2000.0                                                                                                                                                                                               float
    SPECGRPH               5                                                                                                                                                                                                    int
    SPECID                 9                                                                                                                                                                                                    int
    FEEBOX                 lbnl057                                                                                                                                                                                              str
    VESSEL                 26                                                                                                                                                                                                   int
    FEEVER                 v20160312                                                                                                                                                                                            str
    FEEPOWER               ON                                                                                                                                                                                                   str
    FEEDMASK               2134851391                                                                                                                                                                                           int
    FEECMASK               1048575                                                                                                                                                                                              int
    CCDTEMP                -135.8073                                                                                                                                                                                            float
    RADESYS                FK5                                                                                                                                                                                                  str
    FILENAME               /exposures/desi/specs/20201220/00068979/sp9-00068979.fits.fz                                                                                                                                         str
    DOSVER                 trunk                                                                                                                                                                                                str
    OCSVER                 1.2                                                                                                                                                                                                  float
    CONSTVER               DESI:CURRENT                                                                                                                                                                                         str
    INIFILE                /data/msdos/dos_home/architectures/kpno/desi.ini                                                                                                                                                     str
    DAC3                   -9.0002,-8.9919                                                                                                                                                                                      str
    CLOCK5                 9.9999,0.0                                                                                                                                                                                           str
    BLDTIME                0.3522                                                                                                                                                                                               float
    CLOCK2                 9.9999,0.0                                                                                                                                                                                           str
    BIASSECD               [2129:2192, 2130:4193]                                                                                                                                                                               str
    PGAGAIN                3                                                                                                                                                                                                    int
    OFFSET5                2.0,5.9964                                                                                                                                                                                           str
    BIASSECB               [2129:2192, 2:2065]                                                                                                                                                                                  str
    CLOCK4                 9.9999,0.0                                                                                                                                                                                           str
    ORSECD                 [2193:4249, 2098:2129]                                                                                                                                                                               str
    DAC2                   -9.0002,-8.9404                                                                                                                                                                                      str
    DAC6                   5.9998,6.0437                                                                                                                                                                                        str
    CCDPREP                purge,clear                                                                                                                                                                                          str
    CASETEMP               59.322                                                                                                                                                                                               float
    DAC15                  0.0,-0.0148                                                                                                                                                                                          str
    DAC16                  39.9961,39.8706                                                                                                                                                                                      str
    DAC9                   -25.0003,-24.6344                                                                                                                                                                                    str
    AMPSECB                [4114:2058, 1:2064]                                                                                                                                                                                  str
    DAC11                  -25.0003,-24.5157                                                                                                                                                                                    str
    DELAYS                 20, 20, 25, 40, 7, 3000, 7, 7, 7, 7                                                                                                                                                                  str
    CLOCK13                9.9992,2.9993                                                                                                                                                                                        str
    PRESECD                [4250:4256, 2130:4193]                                                                                                                                                                               str
    CDSPARMS               400, 400, 8, 2000                                                                                                                                                                                    str
    DATASECD               [2193:4249, 2130:4193]                                                                                                                                                                               str
    CLOCK15                9.9992,2.9993                                                                                                                                                                                        str
    CLOCK18                9.0,0.9999                                                                                                                                                                                           str
    CLOCK8                 9.9992,2.9993                                                                                                                                                                                        str
    OFFSET7                2.0,6.0122                                                                                                                                                                                           str
    DAC8                   -25.0003,-24.946                                                                                                                                                                                     str
    CCDSECC                [1:2057, 2065:4128]                                                                                                                                                                                  str
    CLOCK14                9.9992,2.9993                                                                                                                                                                                        str
    CLOCK3                 -2.0001,3.9999                                                                                                                                                                                       str
    DIGITIME               47.5948                                                                                                                                                                                              float
    CLOCK1                 9.9999,0.0                                                                                                                                                                                           str
    PRRSECD                [2193:4249, 4194:4194]                                                                                                                                                                               str
    CLOCK9                 9.9992,2.9993                                                                                                                                                                                        str
    CCDNAME                CCDSM9R                                                                                                                                                                                              str
    DETSECB                [2058:4114, 1:2064]                                                                                                                                                                                  str
    CCDSECA                [1:2057, 1:2064]                                                                                                                                                                                     str
    DETSECD                [2058:4114, 2065:4128]                                                                                                                                                                               str
    DATASECB               [2193:4249, 2:2065]                                                                                                                                                                                  str
    CRYOPRES [1]_          1.166e-07                                                                                                                                                                                            str
    CAMERA                 r5                                                                                                                                                                                                   str
    PRRSECA                [8:2064, 1:1]                                                                                                                                                                                        str
    DAC1                   -9.0002,-8.9507                                                                                                                                                                                      str
    PRESECC                [1:7, 2130:4193]                                                                                                                                                                                     str
    TRIMSECA               [8:2064, 2:2065]                                                                                                                                                                                     str
    TRIMSECD               [2193:4249, 2130:4193]                                                                                                                                                                               str
    CCDCFG                 default_lbnl_20190717.cfg                                                                                                                                                                            str
    PRRSECB                [2193:4249, 1:1]                                                                                                                                                                                     str
    CLOCK12                9.9992,2.9993                                                                                                                                                                                        str
    CCDSECB                [2058:4114, 1:2064]                                                                                                                                                                                  str
    TRIMSECB               [2193:4249, 2:2065]                                                                                                                                                                                  str
    DATASECA               [8:2064, 2:2065]                                                                                                                                                                                     str
    DAC17                  20.0008,12.3342                                                                                                                                                                                      str
    CLOCK17                9.0,0.9999                                                                                                                                                                                           str
    PRESECB                [4250:4256, 2:2065]                                                                                                                                                                                  str
    CLOCK0                 9.9999,0.0                                                                                                                                                                                           str
    PRESECA                [1:7, 2:2065]                                                                                                                                                                                        str
    ORSECA                 [8:2064, 2066:2097]                                                                                                                                                                                  str
    BIASSECC               [2065:2128, 2130:4193]                                                                                                                                                                               str
    DETSECC                [1:2057, 2065:4128]                                                                                                                                                                                  str
    DAC14                  0.0,-0.0148                                                                                                                                                                                          str
    DAC4                   5.9998,6.0595                                                                                                                                                                                        str
    CLOCK16                9.9999,3.0                                                                                                                                                                                           str
    AMPSECA                [1:2057, 1:2064]                                                                                                                                                                                     str
    OFFSET4                2.0,6.0595                                                                                                                                                                                           str
    CCDSIZE                4194,4256                                                                                                                                                                                            str
    OFFSET2                0.4000000059604645,-8.9301                                                                                                                                                                           str
    DAC13                  0.0,-0.0148                                                                                                                                                                                          str
    CRYOTEMP [1]_          163.02                                                                                                                                                                                               float
    OFFSET6                2.0,6.0437                                                                                                                                                                                           str
    CLOCK6                 9.9999,0.0                                                                                                                                                                                           str
    DETSECA                [1:2057, 1:2064]                                                                                                                                                                                     str
    CCDTMING               default_lbnl_timing_20180905.txt                                                                                                                                                                     str
    DETECTOR               M1-52                                                                                                                                                                                                str
    OFFSET3                0.4000000059604645,-8.9816                                                                                                                                                                           str
    AMPSECC                [1:2057, 4128:2065]                                                                                                                                                                                  str
    CLOCK10                9.9992,2.9993                                                                                                                                                                                        str
    ORSECC                 [8:2064, 2098:2129]                                                                                                                                                                                  str
    SETTINGS               detectors_sm_20191211.json                                                                                                                                                                           str
    CPUTEMP                58.9629                                                                                                                                                                                              float
    OFFSET0                0.4000000059604645,-8.755                                                                                                                                                                            str
    DAC12                  0.0,0.0                                                                                                                                                                                              str
    DATASECC               [8:2064, 2130:4193]                                                                                                                                                                                  str
    AMPSECD                [4114:2058, 4128:2065]                                                                                                                                                                               str
    DAC10                  -25.0003,-25.0054                                                                                                                                                                                    str
    CLOCK7                 -2.0001,3.9999                                                                                                                                                                                       str
    DAC0                   -9.0002,-8.7653                                                                                                                                                                                      str
    CLOCK11                9.9992,2.9993                                                                                                                                                                                        str
    DAC7                   5.9998,6.0122                                                                                                                                                                                        str
    OFFSET1                0.4000000059604645,-8.9507                                                                                                                                                                           str
    DAC5                   5.9998,5.9964                                                                                                                                                                                        str
    ORSECB                 [2193:4249, 2066:2097]                                                                                                                                                                               str
    CCDSECD                [2058:4114, 2065:4128]                                                                                                                                                                               str
    PRRSECC                [8:2064, 4194:4194]                                                                                                                                                                                  str
    TRIMSECC               [8:2064, 2130:4193]                                                                                                                                                                                  str
    BIASSECA               [2065:2128, 2:2065]                                                                                                                                                                                  str
    REQTIME                120.0                                                                                                                                                                                                float
    OBSID                  kp4m20201220t222415                                                                                                                                                                                  str
    PROCTYPE               RAW                                                                                                                                                                                                  str
    PRODTYPE               image                                                                                                                                                                                                str
    GAINA                  1.684                                                                                                                                                                                                float
    SATULEVA               33000.0                                                                                                                                                                                              float
    OSTEPA                 0.6500495005602716                                                                                                                                                                                   float
    OMETHA                 AVERAGE                                                                                                                                                                                              str
    OVERSCNA               1972.92976646288                                                                                                                                                                                     float
    OBSRDNA                3.218229918807175                                                                                                                                                                                    float
    SATUELEA               52249.58627327651                                                                                                                                                                                    float
    GAINB                  1.655                                                                                                                                                                                                float
    SATULEVB               47000.0                                                                                                                                                                                              float
    OSTEPB                 0.6179795354764792                                                                                                                                                                                   float
    OMETHB                 AVERAGE                                                                                                                                                                                              str
    OVERSCNB               1975.23548556518                                                                                                                                                                                     float
    OBSRDNB                3.153470147761547                                                                                                                                                                                    float
    SATUELEB               74515.98527138963                                                                                                                                                                                    float
    GAINC                  1.467                                                                                                                                                                                                float
    SATULEVC               65535.0                                                                                                                                                                                              float
    OSTEPC                 0.5848174212296726                                                                                                                                                                                   float
    OMETHC                 AVERAGE                                                                                                                                                                                              str
    OVERSCNC               1959.467167892971                                                                                                                                                                                    float
    OBSRDNC                2.894849081776217                                                                                                                                                                                    float
    SATUELEC               93265.30666470101                                                                                                                                                                                    float
    GAIND                  1.509                                                                                                                                                                                                float
    SATULEVD               65535.0                                                                                                                                                                                              float
    OSTEPD                 0.4709297982626595                                                                                                                                                                                   float
    OMETHD                 AVERAGE                                                                                                                                                                                              str
    OVERSCND               1992.393350767962                                                                                                                                                                                    float
    OBSRDND                2.694583892275785                                                                                                                                                                                    float
    SATUELED               95885.79343369114                                                                                                                                                                                    float
    FIBERMIN               2500                                                                                                                                                                                                 int
    LONGSTRN               OGIP 1.0                                                                                                                                                                                             str
    MODULE                 CI                                                                                                                                                                                                   str
    FRAMES [1]_            None                                                                                                                                                                                                 Unknown
    COSMSPLT               F                                                                                                                                                                                                    bool
    MAXSPLIT               0                                                                                                                                                                                                    int
    SPLITIDS [1]_          68979                                                                                                                                                                                                str
    OBSTYPE                FLAT                                                                                                                                                                                                 str
    MANIFEST               F                                                                                                                                                                                                    bool
    OBJECT                                                                                                                                                                                                                      str
    SEQID [1]_             3 requests                                                                                                                                                                                           str
    SEQNUM                 2                                                                                                                                                                                                    int
    SEQTOT [1]_            3                                                                                                                                                                                                    int
    OPENSHUT               None                                                                                                                                                                                                 Unknown
    CAMSHUT                open                                                                                                                                                                                                 str
    WHITESPT [1]_          T                                                                                                                                                                                                    bool
    ZENITH [1]_            F                                                                                                                                                                                                    bool
    SEANNEX [1]_           F                                                                                                                                                                                                    bool
    BEYONDP [1]_           F                                                                                                                                                                                                    bool
    FIDUCIAL [1]_          off                                                                                                                                                                                                  str
    AIRMASS [1]_           1.521306                                                                                                                                                                                             float
    FOCUS [1]_             1163.9,-689.8,370.4,13.8,24.2,-0.0                                                                                                                                                                   str
    TRUSTEMP [1]_          13.267                                                                                                                                                                                               float
    PMIRTEMP [1]_          7.35                                                                                                                                                                                                 float
    PMREADY [1]_           F                                                                                                                                                                                                    bool
    PMCOVER [1]_           open                                                                                                                                                                                                 str
    PMCOOL [1]_            on                                                                                                                                                                                                   str
    DOMSHUTU [1]_          not open                                                                                                                                                                                             str
    DOMSHUTL [1]_          not open                                                                                                                                                                                             str
    DOMLIGHH [1]_          off                                                                                                                                                                                                  str
    DOMLIGHL [1]_          off                                                                                                                                                                                                  str
    DOMEAZ [1]_            253.289                                                                                                                                                                                              float
    DOMINPOS [1]_          F                                                                                                                                                                                                    bool
    GUIDOFFR [1]_          0.0                                                                                                                                                                                                  float
    GUIDOFFD [1]_          -0.0                                                                                                                                                                                                 float
    MOONDEC [1]_           -9.830944                                                                                                                                                                                            float
    MOONRA [1]_            350.511461                                                                                                                                                                                           float
    MOUNTAZ [1]_           73.49407                                                                                                                                                                                             float
    MOUNTDEC [1]_          31.962703                                                                                                                                                                                            float
    MOUNTEL [1]_           41.035778                                                                                                                                                                                            float
    MOUNTHA [1]_           -58.479517                                                                                                                                                                                           float
    INCTRL [1]_            F                                                                                                                                                                                                    bool
    INPOS [1]_             T                                                                                                                                                                                                    bool
    MNTOFFD [1]_           -0.0                                                                                                                                                                                                 float
    MNTOFFR [1]_           -0.0                                                                                                                                                                                                 float
    PARALLAC [1]_          -73.492813                                                                                                                                                                                           float
    SKYDEC [1]_            31.962703                                                                                                                                                                                            float
    SKYRA [1]_             12.901561                                                                                                                                                                                            float
    TARGTDEC [1]_          31.963299                                                                                                                                                                                            float
    TARGTRA [1]_           6.305086                                                                                                                                                                                             float
    TARGTAZ [1]_           75.558672                                                                                                                                                                                            float
    TARGTEL [1]_           46.429343                                                                                                                                                                                            float
    TRGTOFFD [1]_          0.0                                                                                                                                                                                                  float
    TRGTOFFR [1]_          0.0                                                                                                                                                                                                  float
    ZD [1]_                48.964222                                                                                                                                                                                            float
    TCSST [1]_             20:57:41.291                                                                                                                                                                                         str
    TCSMJD [1]_            59203.933945                                                                                                                                                                                         float
    ADCCORR                F                                                                                                                                                                                                    bool
    ADC1PHI [1]_           114.980003                                                                                                                                                                                           float
    ADC2PHI [1]_           162.869907                                                                                                                                                                                           float
    ADC1HOME [1]_          F                                                                                                                                                                                                    bool
    ADC2HOME [1]_          F                                                                                                                                                                                                    bool
    ADC1NREV [1]_          0.0                                                                                                                                                                                                  float
    ADC2NREV [1]_          -1.0                                                                                                                                                                                                 float
    ADC1STAT [1]_          STOPPED                                                                                                                                                                                              str
    ADC2STAT [1]_          STOPPED                                                                                                                                                                                              str
    HEXPOS [1]_            1163.9,-689.8,370.4,13.8,24.2,-0.0                                                                                                                                                                   str
    HEXTRIM [1]_           0.0,0.0,0.0,0.0,0.0,0.0                                                                                                                                                                              str
    ROTOFFST [1]_          0.0                                                                                                                                                                                                  float
    ROTENBLD [1]_          T                                                                                                                                                                                                    bool
    ROTRATE [1]_           0.0                                                                                                                                                                                                  float
    RESETROT               F                                                                                                                                                                                                    bool
    GUIDMODE               catalog                                                                                                                                                                                              str
    USEAOS [1]_            F                                                                                                                                                                                                    bool
    SPCGRPHS               SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                                                                                                                                                              str
    ILLSPECS [1]_          SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                                                                                                                                                              str
    CCDSPECS [1]_          SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                                                                                                                                                              str
    TDEWPNT [1]_           -18.2                                                                                                                                                                                                float
    TAIRFLOW [1]_          1.121                                                                                                                                                                                                float
    TAIRITMP [1]_          10.5                                                                                                                                                                                                 float
    TAIROTMP [1]_          5.5                                                                                                                                                                                                  float
    TAIRTEMP [1]_          11.86                                                                                                                                                                                                float
    TCASITMP [1]_          0.0                                                                                                                                                                                                  float
    TCASOTMP [1]_          9.6                                                                                                                                                                                                  float
    TCSITEMP [1]_          7.4                                                                                                                                                                                                  float
    TCSOTEMP [1]_          10.2                                                                                                                                                                                                 float
    TCIBTEMP [1]_          0.0                                                                                                                                                                                                  float
    TCIMTEMP [1]_          0.0                                                                                                                                                                                                  float
    TCITTEMP [1]_          0.0                                                                                                                                                                                                  float
    TCOSTEMP [1]_          0.0                                                                                                                                                                                                  float
    TCOWTEMP [1]_          0.0                                                                                                                                                                                                  float
    TDBTEMP [1]_           7.4                                                                                                                                                                                                  float
    TFLOWIN [1]_           7.7                                                                                                                                                                                                  float
    TFLOWOUT [1]_          8.3                                                                                                                                                                                                  float
    TGLYCOLI [1]_          -1.8                                                                                                                                                                                                 float
    TGLYCOLO [1]_          0.0                                                                                                                                                                                                  float
    THINGES [1]_           12.9                                                                                                                                                                                                 float
    THINGEW [1]_           11.7                                                                                                                                                                                                 float
    TPMAVERT [1]_          7.304                                                                                                                                                                                                float
    TPMDESIT [1]_          7.0                                                                                                                                                                                                  float
    TPMEIBT [1]_           7.3                                                                                                                                                                                                  float
    TPMEITT [1]_           7.3                                                                                                                                                                                                  float
    TPMEOBT [1]_           7.4                                                                                                                                                                                                  float
    TPMEOTT [1]_           7.2                                                                                                                                                                                                  float
    TPMNIBT [1]_           7.4                                                                                                                                                                                                  float
    TPMNITT [1]_           7.3                                                                                                                                                                                                  float
    TPMNOBT [1]_           7.7                                                                                                                                                                                                  float
    TPMNOTT [1]_           7.6                                                                                                                                                                                                  float
    TPMRTDT [1]_           6.96                                                                                                                                                                                                 float
    TPMSIBT [1]_           7.4                                                                                                                                                                                                  float
    TPMSITT [1]_           7.0                                                                                                                                                                                                  float
    TPMSOBT [1]_           7.4                                                                                                                                                                                                  float
    TPMSOTT [1]_           7.2                                                                                                                                                                                                  float
    TPMSTAT [1]_           soft air                                                                                                                                                                                             str
    TPMWIBT [1]_           7.2                                                                                                                                                                                                  float
    TPMWITT [1]_           7.1                                                                                                                                                                                                  float
    TPMWOBT [1]_           7.6                                                                                                                                                                                                  float
    TPMWOTT [1]_           8.1                                                                                                                                                                                                  float
    TPCITEMP [1]_          7.7                                                                                                                                                                                                  float
    TPCOTEMP [1]_          7.7                                                                                                                                                                                                  float
    TPR1HUM [1]_           0.0                                                                                                                                                                                                  float
    TPR1TEMP [1]_          0.0                                                                                                                                                                                                  float
    TPR2HUM [1]_           0.0                                                                                                                                                                                                  float
    TPR2TEMP [1]_          0.0                                                                                                                                                                                                  float
    TSERVO [1]_            7.0                                                                                                                                                                                                  float
    TTRSTEMP [1]_          13.2                                                                                                                                                                                                 float
    TTRWTEMP [1]_          13.4                                                                                                                                                                                                 float
    TTRUETBT [1]_          -4.8                                                                                                                                                                                                 float
    TTRUETTT [1]_          11.5                                                                                                                                                                                                 float
    TTRUNTBT [1]_          10.9                                                                                                                                                                                                 float
    TTRUNTTT [1]_          11.8                                                                                                                                                                                                 float
    TTRUSTBT [1]_          11.1                                                                                                                                                                                                 float
    TTRUSTST [1]_          10.8                                                                                                                                                                                                 float
    TTRUSTTT [1]_          12.4                                                                                                                                                                                                 float
    TTRUTSBT [1]_          13.6                                                                                                                                                                                                 float
    TTRUTSMT [1]_          13.7                                                                                                                                                                                                 float
    TTRUTSTT [1]_          12.5                                                                                                                                                                                                 float
    TTRUWTBT [1]_          10.9                                                                                                                                                                                                 float
    TTRUWTTT [1]_          11.6                                                                                                                                                                                                 float
    ALARM [1]_             F                                                                                                                                                                                                    bool
    ALARM-ON [1]_          F                                                                                                                                                                                                    bool
    BATTERY [1]_           100.0                                                                                                                                                                                                float
    SECLEFT [1]_           5772.0                                                                                                                                                                                               float
    UPSSTAT [1]_           System Normal - On Line(7)                                                                                                                                                                           str
    INAMPS [1]_            64.3                                                                                                                                                                                                 float
    OUTWATTS [1]_          4500.0,6800.0,4100.0                                                                                                                                                                                 str
    COMPDEW [1]_           -12.0                                                                                                                                                                                                float
    COMPHUM [1]_           7.8                                                                                                                                                                                                  float
    COMPAMB [1]_           19.4                                                                                                                                                                                                 float
    COMPTEMP [1]_          24.9                                                                                                                                                                                                 float
    DEWPOINT [1]_          5.7                                                                                                                                                                                                  float
    HUMIDITY [1]_          7.0                                                                                                                                                                                                  float
    PRESSURE [1]_          794.7                                                                                                                                                                                                float
    OUTTEMP [1]_           0.0                                                                                                                                                                                                  float
    WINDDIR [1]_           82.0                                                                                                                                                                                                 float
    WINDSPD [1]_           23.3                                                                                                                                                                                                 float
    GUST [1]_              18.1                                                                                                                                                                                                 float
    AMNIENTN [1]_          13.3                                                                                                                                                                                                 float
    CFLOOR [1]_            8.1                                                                                                                                                                                                  float
    NWALLIN [1]_           13.6                                                                                                                                                                                                 float
    NWALLOUT [1]_          8.8                                                                                                                                                                                                  float
    WWALLIN [1]_           12.8                                                                                                                                                                                                 float
    WWALLOUT [1]_          9.4                                                                                                                                                                                                  float
    AMBIENTS [1]_          14.6                                                                                                                                                                                                 float
    FLOOR [1]_             12.3                                                                                                                                                                                                 float
    EWALLCMP [1]_          10.2                                                                                                                                                                                                 float
    EWALLCOU [1]_          9.5                                                                                                                                                                                                  float
    ROOF [1]_              10.0                                                                                                                                                                                                 float
    ROOFAMB [1]_           9.9                                                                                                                                                                                                  float
    DOMEBLOW [1]_          12.1                                                                                                                                                                                                 float
    DOMEBUP [1]_           12.5                                                                                                                                                                                                 float
    DOMELLOW [1]_          14.4                                                                                                                                                                                                 float
    DOMELUP [1]_           19.3                                                                                                                                                                                                 float
    DOMERLOW [1]_          12.3                                                                                                                                                                                                 float
    DOMERUP [1]_           12.8                                                                                                                                                                                                 float
    PLATFORM [1]_          15.3                                                                                                                                                                                                 float
    SHACKC [1]_            15.2                                                                                                                                                                                                 float
    SHACKW [1]_            13.2                                                                                                                                                                                                 float
    STAIRSL [1]_           12.6                                                                                                                                                                                                 float
    STAIRSM [1]_           13.3                                                                                                                                                                                                 float
    STAIRSU [1]_           13.6                                                                                                                                                                                                 float
    TELBASE [1]_           8.5                                                                                                                                                                                                  float
    UTILWALL [1]_          11.6                                                                                                                                                                                                 float
    UTILROOM [1]_          12.4                                                                                                                                                                                                 float
    EXCLUDED                                                                                                                                                                                                                    str
    CHECKSUM               9IArAH5o2HAo9H5o                                                                                                                                                                                     str     HDU checksum updated 2022-01-29T01:11:34
    DATASUM                1239529649                                                                                                                                                                                           str     data unit checksum updated 2022-01-29T01:11:34
    TCSPIRA [1]_           1.0,0.0,0.0,0.0                                                                                                                                                                                      str
    SEQSTART [1]_          2021-02-24T01:22:15.381414                                                                                                                                                                           str
    TCSPIDEC [1]_          1.0,0.0,0.0,0.0                                                                                                                                                                                      str
    MOONSEP [1]_           8.81573236983626                                                                                                                                                                                     float
    TCSKRA [1]_            0.3 0.003 0.00003                                                                                                                                                                                    str
    TCSMFRA [1]_           1                                                                                                                                                                                                    int
    TCSGRA [1]_            0.3                                                                                                                                                                                                  float
    TCSKDEC [1]_           0.3 0.003 0.00003                                                                                                                                                                                    str
    TCSGDEC [1]_           0.3                                                                                                                                                                                                  float
    TCSMFDEC [1]_          1                                                                                                                                                                                                    int
    FIELDROT [1]_          0.116773054960708                                                                                                                                                                                    float
    FOCSTIME [1]_          60.0                                                                                                                                                                                                 float
    KEEPSKY [1]_           F                                                                                                                                                                                                    bool
    SKY [1]_               DESIROOT/target/catalogs/dr9/0.51.0/skies                                                                                                                                                            str
    PMTRANS [1]_           94.62                                                                                                                                                                                                float
    GUIDEFIL [1]_          guide-00083129.fits.fz                                                                                                                                                                               str
    USESPCTR [1]_          T                                                                                                                                                                                                    bool
    SUNRA [1]_             12.514241                                                                                                                                                                                            float
    SP3BLUP [1]_           8.133e-08                                                                                                                                                                                            float
    BACKLIT [1]_           off                                                                                                                                                                                                  str
    SP6REDT [1]_           139.94                                                                                                                                                                                               float
    USEILLUM [1]_          T                                                                                                                                                                                                    bool
    SP8REDP [1]_           3.96e-08                                                                                                                                                                                             float
    NTSSURVY [1]_          na                                                                                                                                                                                                   str
    POSCYCLE [1]_          1                                                                                                                                                                                                    int
    COORDFIL [1]_          coordinates-00083129.fits                                                                                                                                                                            str
    POSTOLER [1]_          0.005                                                                                                                                                                                                float
    SP7REDT [1]_           140.01                                                                                                                                                                                               float
    SP0NIRT [1]_           139.89                                                                                                                                                                                               float
    SP7NIRP [1]_           4.311e-08                                                                                                                                                                                            float
    SP0NIRP [1]_           5.998e-08                                                                                                                                                                                            float
    SP6NIRT [1]_           139.89                                                                                                                                                                                               float
    SP1BLUT [1]_           163.02                                                                                                                                                                                               float
    SP3REDT [1]_           139.99                                                                                                                                                                                               float
    SP4NIRP [1]_           6.683e-08                                                                                                                                                                                            float
    SP5NIRT [1]_           139.94                                                                                                                                                                                               float
    TGFAPROC [1]_          9.0024                                                                                                                                                                                               float
    SP7BLUP [1]_           9.947e-08                                                                                                                                                                                            float
    GFA [1]_               DESIROOT/target/catalogs/dr9/0.51.0/gfas                                                                                                                                                             str
    GSGUIDE5 [1]_          (806.92,578.08),(449.53,1063.99)                                                                                                                                                                     str
    SKYLEVEL [1]_          1.364                                                                                                                                                                                                float
    TARG [1]_              DESIROOT/target/catalogs/dr9/0.51.0/targets/sv1/resolve/dark                                                                                                                                         str
    SP0REDT [1]_           139.96                                                                                                                                                                                               float
    USEOPENL [1]_          T                                                                                                                                                                                                    bool
    SP0BLUT [1]_           163.02                                                                                                                                                                                               float
    SP2BLUP [1]_           8.492e-08                                                                                                                                                                                            float
    GSGUIDE7 [1]_          (884.73,992.68),(494.79,1738.49)                                                                                                                                                                     str
    SP0BLUP [1]_           8.499e-08                                                                                                                                                                                            float
    POSCNVGD [1]_          F                                                                                                                                                                                                    bool
    USEFOCUS [1]_          T                                                                                                                                                                                                    bool
    ACQCAM [1]_            GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                                                                                                                                                            str
    GSGUIDE0 [1]_          (954.26,900.15),(752.14,1756.37)                                                                                                                                                                     str
    SP3NIRP [1]_           3.566e-08                                                                                                                                                                                            float
    SP5BLUT [1]_           162.99                                                                                                                                                                                               float
    GUIEXPID [1]_          83129                                                                                                                                                                                                int
    SP9NIRP [1]_           5.211e-08                                                                                                                                                                                            float
    USEFVC [1]_            T                                                                                                                                                                                                    bool
    USEGUIDR [1]_          T                                                                                                                                                                                                    bool
    GSGUIDE2 [1]_          (722.18,832.33),(237.62,150.28)                                                                                                                                                                      str
    GSGUIDE3 [1]_          (49.91,660.39),(398.91,1892.18)                                                                                                                                                                      str
    IGFRMNUM [1]_          14                                                                                                                                                                                                   int
    FGFRMNUM [1]_          45                                                                                                                                                                                                   int
    SP4BLUP [1]_           6.248e-08                                                                                                                                                                                            float
    SP5BLUP [1]_           1.115e-07                                                                                                                                                                                            float
    SP1REDT [1]_           139.89                                                                                                                                                                                               float
    SP9BLUT [1]_           163.02                                                                                                                                                                                               float
    FA_VER [1]_            2.1.1.dev2706                                                                                                                                                                                        str
    IFFRMNUM [1]_          1                                                                                                                                                                                                    int
    SCSTD [1]_             STD_WD,STD_FAINT                                                                                                                                                                                     str
    SP1NIRT [1]_           139.89                                                                                                                                                                                               float
    USEFID [1]_            T                                                                                                                                                                                                    bool
    REQDEC [1]_            32.375                                                                                                                                                                                               float
    SP9REDP [1]_           5.108e-08                                                                                                                                                                                            float
    SP2REDP [1]_           6.944e-08                                                                                                                                                                                            float
    FAARGS [1]_            --doclean n --dr dr9 --dtver 0.51.0 --faflavor sv1lrgqso2 --m31cen n --pmtime 2021-03-16T00:00:00.000 --priority custom --rundate 2019-09-16T00:00:00 --tiledec 32.375 --tileid 80873 --tilera 127.7 str
    USESKY [1]_            T                                                                                                                                                                                                    bool
    SP6NIRP [1]_           2.809e-07                                                                                                                                                                                            float
    SP4NIRT [1]_           139.94                                                                                                                                                                                               float
    SCTARG [1]_            STD_WD,LRG,QSO_RF_4PASS,QSO_RF_8PASS,WISE_VAR_QSO,QSO_RED,WD_BINARIES_DARK,BHB,UDG,LOW_MASS_AGN,SPCV                                                                                                 str
    FA_RUN [1]_            2019-09-16T00:00:00                                                                                                                                                                                  str
    USEPOS [1]_            T                                                                                                                                                                                                    bool
    SP2BLUT [1]_           163.02                                                                                                                                                                                               float
    ARCHIVE [1]_           /exposures/desi/20210402/00083129/guide-00083129.fits.fz                                                                                                                                             str
    ISFRMNUM [1]_          0                                                                                                                                                                                                    int
    SKYSUPP [1]_           DESIROOT/target/catalogs/gaiadr2/0.51.0/skies-supp                                                                                                                                                   str
    FOCEXPID [1]_          83129                                                                                                                                                                                                int
    POSENABL [1]_          4056                                                                                                                                                                                                 int
    SUNDEC [1]_            5.365754                                                                                                                                                                                             float
    TILEDEC [1]_           32.375                                                                                                                                                                                               float
    POSFRACT [1]_          0.95                                                                                                                                                                                                 float
    SP9NIRT [1]_           139.86                                                                                                                                                                                               float
    SPLITEXP [1]_          F                                                                                                                                                                                                    bool
    SP8REDT [1]_           139.94                                                                                                                                                                                               float
    SKYEXPID [1]_          83129                                                                                                                                                                                                int
    FAOUTDIR [1]_          /global/cfs/cdirs/desi/survey/fiberassign/SV1/20210316/                                                                                                                                              str
    RUNDATE [1]_           2019-09-16T00:00:00                                                                                                                                                                                  str
    SP4REDT [1]_           140.01                                                                                                                                                                                               float
    TILERA [1]_            127.7                                                                                                                                                                                                float
    KEEPGUDR [1]_          F                                                                                                                                                                                                    bool
    POSDISAB [1]_          925                                                                                                                                                                                                  int
    SP3BLUT [1]_           163.02                                                                                                                                                                                               float
    SP0REDP [1]_           6.295e-08                                                                                                                                                                                            float
    SP6BLUT [1]_           163.02                                                                                                                                                                                               float
    SCND [1]_              DESIROOT/target/catalogs/dr9/0.51.0/targets/sv1/secondary/dark                                                                                                                                       str
    SIMGFAP [1]_           F                                                                                                                                                                                                    bool
    USESPLIT [1]_          T                                                                                                                                                                                                    bool
    TILEID [1]_            80873                                                                                                                                                                                                int
    TARG2 [1]_             DESIROOT/target/catalogs/gaiadr2/0.51.0/targets/sv1/resolve/supp                                                                                                                                     str
    SP1NIRP [1]_           4.585e-08                                                                                                                                                                                            float
    USEDONUT [1]_          T                                                                                                                                                                                                    bool
    FIBASSGN [1]_          /data/tiles/SVN_tiles/080/fiberassign-080873.fits.gz                                                                                                                                                 str
    SP8NIRT [1]_           139.99                                                                                                                                                                                               float
    PMTIME [1]_            2021-03-16T00:00:00.000                                                                                                                                                                              str
    SP2NIRT [1]_           139.89                                                                                                                                                                                               float
    KEEPFOCS [1]_          F                                                                                                                                                                                                    bool
    VISITIDS [1]_          83129                                                                                                                                                                                                str
    FA_SURV [1]_           sv1                                                                                                                                                                                                  str
    FFFRMNUM [1]_          5                                                                                                                                                                                                    int
    SP8BLUP [1]_           7.959e-08                                                                                                                                                                                            float
    ACTTEFF [1]_           112.2149                                                                                                                                                                                             float
    POSMVALL [1]_          T                                                                                                                                                                                                    bool
    SP6BLUP [1]_           6.3e-08                                                                                                                                                                                              float
    GUIDTIME [1]_          5.0                                                                                                                                                                                                  float
    SEEING [1]_            1.3508                                                                                                                                                                                               float
    SP3REDP [1]_           7.919e-08                                                                                                                                                                                            float
    USEETC [1]_            T                                                                                                                                                                                                    bool
    FIELDNUM [1]_          0                                                                                                                                                                                                    int
    SP5REDT [1]_           139.99                                                                                                                                                                                               float
    SP6REDP [1]_           6.337e-08                                                                                                                                                                                            float
    SP8NIRP [1]_           4.827e-08                                                                                                                                                                                            float
    USEROTAT [1]_          T                                                                                                                                                                                                    bool
    FA_PLAN [1]_           2022-07-01T00:00:00.000                                                                                                                                                                              str
    SP2NIRP [1]_           6.984e-08                                                                                                                                                                                            float
    POSONFRC [1]_          0.4768                                                                                                                                                                                               float
    PETALS [1]_            PETAL0,PETAL1,PETAL2,PETAL3,PETAL4,PETAL5,PETAL6,PETAL7,PETAL8,PETAL9                                                                                                                                str
    STOPSKY [1]_           T                                                                                                                                                                                                    bool
    SP7REDP [1]_           6.038e-08                                                                                                                                                                                            float
    GUIDECAM [1]_          GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                                                                                                                                                            str
    SP8BLUT [1]_           162.9                                                                                                                                                                                                float
    TNFSPROC [1]_          25.9483                                                                                                                                                                                              float
    ACQTIME [1]_           15.0                                                                                                                                                                                                 float
    REQADC [1]_            92.63,97.66                                                                                                                                                                                          str
    SP4BLUT [1]_           163.02                                                                                                                                                                                               float
    FAFLAVOR [1]_          sv1lrgqso2                                                                                                                                                                                           str
    OBSCON [1]_            DARK|GRAY|BRIGHT                                                                                                                                                                                     str
    SP7NIRT [1]_           139.96                                                                                                                                                                                               float
    SP9REDT [1]_           139.99                                                                                                                                                                                               float
    POSRMS [1]_            0.0076                                                                                                                                                                                               float
    REACQUIR [1]_          F                                                                                                                                                                                                    bool
    SP5REDP [1]_           5.487e-08                                                                                                                                                                                            float
    STOPGUDR [1]_          T                                                                                                                                                                                                    bool
    POSONTGT [1]_          1934                                                                                                                                                                                                 int
    FOCUSCAM [1]_          FOCUS1,FOCUS4,FOCUS6,FOCUS9                                                                                                                                                                          str
    SP5NIRP [1]_           6.003e-08                                                                                                                                                                                            float
    SP1BLUP [1]_           7.992e-08                                                                                                                                                                                            float
    PMSEEING [1]_          1.33                                                                                                                                                                                                 float
    SP9BLUP [1]_           1.231e-07                                                                                                                                                                                            float
    SKYTIME [1]_           60                                                                                                                                                                                                   float
    POSITER [1]_           1                                                                                                                                                                                                    int
    USESPLITS [1]_         T                                                                                                                                                                                                    bool
    SP1REDP [1]_           5.506e-08                                                                                                                                                                                            float
    SP3NIRT [1]_           140.01                                                                                                                                                                                               float
    FA_HA [1]_             0.0                                                                                                                                                                                                  float
    SP2REDT [1]_           139.96                                                                                                                                                                                               float
    SKYCAM [1]_            SKYCAM0,SKYCAM1                                                                                                                                                                                      str
    SP4REDP [1]_           4.945e-08                                                                                                                                                                                            float
    SP7BLUT [1]_           163.02                                                                                                                                                                                               float
    FSFRMNUM [1]_          3                                                                                                                                                                                                    int
    SIMGFACQ [1]_          F                                                                                                                                                                                                    bool
    REQRA [1]_             127.7                                                                                                                                                                                                float
    GSGUIDE8 [1]_          (364.80,1645.04),(69.26,1479.25)                                                                                                                                                                     str
    DESIROOT [1]_          /global/cfs/cdirs/desi                                                                                                                                                                               str
    USEXSRVR [1]_          T                                                                                                                                                                                                    bool
    STOPFOCS [1]_          T                                                                                                                                                                                                    bool
    REQTEFF [1]_           1000.0                                                                                                                                                                                               float
    GOALTIME [1]_          1200.0                                                                                                                                                                                               float
    SBPROF [1]_            ELG                                                                                                                                                                                                  str
    EBVFAC [1]_            1.07122550132983                                                                                                                                                                                     float
    MTLTIME [1]_           2021-04-17T20:00:39                                                                                                                                                                                  str
    GOALTYPE [1]_          DARK                                                                                                                                                                                                 str
    MTL [1]_               DESIROOT/survey/ops/surveyops/trunk/mtl/sv3/dark                                                                                                                                                     str
    SURVEY [1]_            sv3                                                                                                                                                                                                  str
    SCNDMTL [1]_           DESIROOT/survey/ops/surveyops/trunk/mtl/sv3/secondary/dark                                                                                                                                           str
    FAPRGRM [1]_           DARK                                                                                                                                                                                                 str
    TOTTEFF [1]_           838.56                                                                                                                                                                                               float
    PMCORR [1]_            n                                                                                                                                                                                                    str
    MINTFRAC [1]_          0.9                                                                                                                                                                                                  float
    BBKGMINA [1]_          -0.3947016321413652                                                                                                                                                                                  float
    BBKGMINC [1]_          -0.2673014085831243                                                                                                                                                                                  float
    BBKGMIND [1]_          -0.4786751204310712                                                                                                                                                                                  float
    BBKGMAXA [1]_          0.6036115648904081                                                                                                                                                                                   float
    BBKGMAXD [1]_          0.2858693184663221                                                                                                                                                                                   float
    BBKGMAXB [1]_          0.2978123984653912                                                                                                                                                                                   float
    BBKGMAXC [1]_          0.3636081010150568                                                                                                                                                                                   float
    BBKGMINB [1]_          -0.2841325038108138                                                                                                                                                                                  float
    FVCTIME [1]_           2.0                                                                                                                                                                                                  float
    POSCVFRC [1]_          0.3467                                                                                                                                                                                               float
    ETCSPLIT [1]_          1                                                                                                                                                                                                    int
    ACQFWHM [1]_           1.71791                                                                                                                                                                                              float
    TRANSPAR [1]_          None                                                                                                                                                                                                 Unknown
    NTSPROG [1]_           BRIGHT                                                                                                                                                                                               str
    SLEWANGL [1]_          28.856                                                                                                                                                                                               float
    TOO [1]_               /data/afternoon_planning/surveyops/trunk/mtl/sv3/ToO/ToO.ecsv                                                                                                                                        str
    ESTTIME [1]_           2231.315                                                                                                                                                                                             float
    ETCPREV [1]_           0.0                                                                                                                                                                                                  float
    ETCTRANS [1]_          0.719235                                                                                                                                                                                             float
    MINTIME [1]_           120.0                                                                                                                                                                                                float
    ETCTHRUP [1]_          0.442956                                                                                                                                                                                             float
    ETCTEFF [1]_           222.548355                                                                                                                                                                                           float
    ETCSKY [1]_            1.43154                                                                                                                                                                                              float
    ETCVERS [1]_           0.1.12-3-g12b54bb                                                                                                                                                                                    str
    ETCFRACE [1]_          0.271983                                                                                                                                                                                             float
    ETCREAL [1]_           1054.206299                                                                                                                                                                                          float
    ETCPROF [1]_           BGS                                                                                                                                                                                                  str
    CONVERGD [1]_          F                                                                                                                                                                                                    bool
    ETCSEENG [1]_          1.7179                                                                                                                                                                                               float
    ETCTHRUB [1]_          0.469155                                                                                                                                                                                             float
    PMTRANSP [1]_          104.71                                                                                                                                                                                               float
    ETCFRACB [1]_          0.123838                                                                                                                                                                                             float
    ETCFRACP [1]_          0.346107                                                                                                                                                                                             float
    ETCTHRUE [1]_          0.474574                                                                                                                                                                                             float
    MAXTIME [1]_           5400.0                                                                                                                                                                                               float
    SIMGFAQ [1]_           F                                                                                                                                                                                                    bool
    SHFTFOCS [1]_          220.0                                                                                                                                                                                                float
    FASCRIPT [1]_          ../bin/fba_launch                                                                                                                                                                                    str
    ROLE [1]_              GUIDERMAN                                                                                                                                                                                            str
    SVNDM [1]_             unknown                                                                                                                                                                                              str
    SVNMTL [1]_            unknown                                                                                                                                                                                              str
    TARG3 [1]_             DESIROOT/target/catalogs/dr9/0.51.0/targets/sv1/resolve/bright                                                                                                                                       str
    DR [1]_                dr9                                                                                                                                                                                                  str
    M31CEN [1]_            n                                                                                                                                                                                                    str
    PRIORITY [1]_          default                                                                                                                                                                                              str
    DTVER [1]_             0.50.0                                                                                                                                                                                               str
    UPSSTAT.undefined [1]_ 17826.0                                                                                                                                                                                              float
    FA_M_GFA [1]_          0.4                                                                                                                                                                                                  float
    FA_M_PET [1]_          0.4                                                                                                                                                                                                  float
    FA_M_POS [1]_          0.05                                                                                                                                                                                                 float
    ====================== ==================================================================================================================================================================================================== ======= ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

===================== ======= ===== ==============================
Name                  Type    Units Description
===================== ======= ===== ==============================
TARGETID              int64         Unique target ID
PETAL_LOC             int16         Focal plane petal location 0-9
DEVICE_LOC            int32         Device location 0-5xx
LOCATION              int64         1000*PETAL_LOC + DEVICE_LOC
FIBER                 int32         Fiber number 0-4999
FIBERSTATUS           int32         Fiber status mask; 0=good
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
BRICKID               int32
BRICK_OBJID           int32
MORPHTYPE             char[4]
FLUX_G                float32
FLUX_R                float32
FLUX_Z                float32
FLUX_IVAR_G           float32
FLUX_IVAR_R           float32
FLUX_IVAR_Z           float32
MASKBITS              int16
REF_ID                int64
REF_CAT               char[2]
GAIA_PHOT_G_MEAN_MAG  float32
GAIA_PHOT_BP_MEAN_MAG float32
GAIA_PHOT_RP_MEAN_MAG float32
PARALLAX              float32
BRICKNAME             char[8]
EBV                   float32
FLUX_W1               float32
FLUX_W2               float32
FLUX_IVAR_W1          float32
FLUX_IVAR_W2          float32
FIBERFLUX_G           float32
FIBERFLUX_R           float32
FIBERFLUX_Z           float32
FIBERTOTFLUX_G        float32
FIBERTOTFLUX_R        float32
FIBERTOTFLUX_Z        float32
SERSIC                float32
SHAPE_R               float32
SHAPE_E1              float32
SHAPE_E2              float32
PHOTSYS               char[1]
PRIORITY_INIT         int64
NUMOBS_INIT           int64
CMX_TARGET [1]_       int64
DESI_TARGET           int64
BGS_TARGET            int64
MWS_TARGET            int64
SCND_TARGET [1]_      int64
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
SV1_BGS_TARGET [1]_   int64
SV1_MWS_TARGET [1]_   int64
SV1_DESI_TARGET [1]_  int64
SV1_SCND_TARGET [1]_  int64
SV3_BGS_TARGET [1]_   int64
SV3_DESI_TARGET [1]_  int64
SV3_SCND_TARGET [1]_  int64
SV3_MWS_TARGET [1]_   int64
SV2_DESI_TARGET [1]_  int64
SV2_SCND_TARGET [1]_  int64
SV2_MWS_TARGET [1]_   int64
SV2_BGS_TARGET [1]_   int64
===================== ======= ===== ==============================

.. [1] Optional

HDU6
----

EXTNAME = CHI2PIX

:math:`\chi^2` of PSF fit to CCD pixels per spectrum wavelength bin.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2751             int  Number of wavelengths
    NAXIS2   500              int  Number of spectra
    CHECKSUM SCE8VAB5SAB5SAB5 str  HDU checksum updated 2021-07-08T12:56:18
    DATASUM  3693165584       str  data unit checksum updated 2021-07-08T12:56:18
    ======== ================ ==== ==============================================

Data: FITS image [float32, 2751x500]


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
