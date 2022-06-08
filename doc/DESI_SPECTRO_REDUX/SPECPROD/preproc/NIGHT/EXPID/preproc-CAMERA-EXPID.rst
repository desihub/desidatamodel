=========================
preproc-CAMERA-EXPID.fits
=========================

:Summary: Pre-processed spectrograph CCD raw data.
:Naming Convention: ``preproc-{camera}-{expid}.fits``, where
    ``{camera}`` is the spectrograph camera (e.g. "b0", "r1", "z9"),
    and ``{expid}`` is the zero-padded 8-digit exposure ID.
:Regex: ``preproc-[brz][0-9]-[0-9]{8}\.fits``
:File Type: FITS, 194 MB

Contents
========

====== ========= ======== ===================
Number EXTNAME   Type     Contents
====== ========= ======== ===================
HDU0_  IMAGE     IMAGE    Flat-fielded pixel values in electrons [FLOAT]
HDU1_  IVAR      IMAGE    Inverse variance (1/sigma^2) of pixel values [FLOAT]
HDU2_  MASK      IMAGE    Bitmask to flag bad pixels or cosmics [INT]
HDU3_  READNOISE IMAGE    Flat-fielded readout noise in electrons [FLOAT]
HDU4_  FIBERMAP  BINTABLE Table with information about the targets
====== ========= ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = IMAGE

2D image with flat-fielded pixel values in electrons. Bias level and dark current have been subtracted.
Electronic gains, converting ADC count to electrons have been applied. Pixel values
have been divided by a pixel flat field. Additional corrections for some CCDs are electronic
amplifier cross-talk correction, and negative trails corrections. The pre-scan and over-scan regions
have been removed.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ============================================================ ======= ===============================================
    KEY      Example Value                                                Type    Comment
    ======== ============================================================ ======= ===============================================
    NAXIS1   4114                                                         int
    NAXIS2   4128                                                         int
    EXPID    68979                                                        int     Exposure number
    EXPFRAME 0                                                            int     Frame number
    FLAVOR   science                                                      str     Observation type
    SEQUENCE Spectrographs                                                str     OCS Sequence name
    PURPOSE  Commissioning                                                str     Purpose of observing night
    PROGRAM  CALIB DESI-CALIB-00 LEDs only                                str     Program name
    PROPID   2019B-5000                                                   str     Proposal ID
    OBSERVER DESIObserver                                                 str     Names of observers
    LEAD     RunManager                                                   str     Lead observer
    INSTRUME DESI                                                         str     Instrument name
    OBSERVAT KPNO                                                         str     Observatory name
    OBS-LAT  31.96403                                                     str     [deg] Observatory latitude
    OBS-LONG -111.59989                                                   str     [deg] Observatory east longitude
    OBS-ELEV 2097.0                                                       float   [m] Observatory elevation
    TELESCOP KPNO 4.0-m telescope                                         str     Telescope name
    CORRCTOR DESI Corrector                                               str     Corrector Identification
    NIGHT    20201220                                                     int     Observing night
    TIMESYS  UTC                                                          str     Time system used for date-obs
    DATE-OBS 2020-12-20T22:24:15.672815                                   str     [UTC] Observation data and start time
    TIME-OBS 22:24:15.672815                                              str     [UTC] Observation start time
    MJD-OBS  59203.93351473                                               float   Modified Julian Date of observation
    ST       20:57:41.340                                                 str     Local Sidereal time at observation start (HH:MM
    EXPTIME  120.037                                                      float   [s] Actual exposure time
    DELTARA  0.0                                                          float   [arcsec] Offset], right ascension, observer inp
    DELTADEC 0.0                                                          float   [arcsec] Offset], declination, observer input
    VCCD     ON                                                           str     True (ON) if CCD voltage is on
    VCCDON   2020-12-14T04:22:19.522101                                   str     Time when CCD voltage was turned on
    VCCDSEC  583485.8                                                     float   [s] CCD on time in seconds
    EQUINOX  2000.0                                                       float   Epoch of observation
    SPECGRPH 5                                                            int     Spectrograph logical name (SP)
    SPECID   9                                                            int     Spectrograph serial number (SM)
    FEEBOX   lbnl057                                                      str     CCD Controller serial number
    VESSEL   26                                                           int     Cryostat serial number
    FEEVER   v20160312                                                    str     CCD Controller version
    FEEPOWER ON                                                           str     FEE power status
    FEEDMASK 2134851391                                                   int     FEE dac mask
    FEECMASK 1048575                                                      int     FEE clk mask
    CCDTEMP  -135.8073                                                    float   [deg C] CCD controller CCD temperature
    RADESYS  FK5                                                          str     Coordinate reference frame of major/minor axes
    FILENAME /exposures/desi/specs/20201220/00068979/sp9-00068979.fits.fz str     Name
    DOSVER   trunk                                                        str     DOS software version
    OCSVER   1.2                                                          float   OCS software version
    CONSTVER DESI:CURRENT                                                 str     Constants version
    INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini             str     DOS Configuration
    DAC3     -9.0002,-8.9919                                              str     [V] set value, measured value
    CLOCK5   9.9999,0.0                                                   str     [V] high rail, low rail
    BLDTIME  0.3522                                                       float   [s] Time to build image
    CLOCK2   9.9999,0.0                                                   str     [V] high rail, low rail
    BIASSECD [2129:2192, 2130:4193]                                       str     Bias section for quadrant D
    PGAGAIN  3                                                            int     Controller gain
    OFFSET5  2.0,5.9964                                                   str     [V] set value, measured value
    BIASSECB [2129:2192, 2:2065]                                          str     Bias section for quadrant B
    CLOCK4   9.9999,0.0                                                   str     [V] high rail, low rail
    ORSECD   [2193:4249, 2098:2129]                                       str     Row bias section for quadrant D
    DAC2     -9.0002,-8.9404                                              str     [V] set value, measured value
    DAC6     5.9998,6.0437                                                str     [V] set value, measured value
    CCDPREP  purge,clear                                                  str     CCD prep actions
    CASETEMP 59.322                                                       float   [deg C] CCD controller case temperature
    DAC15    0.0,-0.0148                                                  str     [V] set value, measured value
    DAC16    39.9961,39.8706                                              str     [V] set value, measured value
    DAC9     -25.0003,-24.6344                                            str     [V] set value, measured value
    AMPSECB  [4114:2058, 1:2064]                                          str     AMP section for quadrant B
    DAC11    -25.0003,-24.5157                                            str     [V] set value, measured value
    DELAYS   20, 20, 25, 40, 7, 3000, 7, 7, 7, 7                          str     [10] Delay settings
    CLOCK13  9.9992,2.9993                                                str     [V] high rail, low rail
    PRESECD  [4250:4256, 2130:4193]                                       str     Prescan section for quadrant D
    CDSPARMS 400, 400, 8, 2000                                            str     CDS parameters
    DATASECD [2193:4249, 2130:4193]                                       str     Data section for quadrant D
    CLOCK15  9.9992,2.9993                                                str     [V] high rail, low rail
    CLOCK18  9.0,0.9999                                                   str     [V] high rail, low rail
    CLOCK8   9.9992,2.9993                                                str     [V] high rail, low rail
    OFFSET7  2.0,6.0122                                                   str     [V] set value, measured value
    DAC8     -25.0003,-24.946                                             str     [V] set value, measured value
    CCDSECC  [1:2057, 2065:4128]                                          str     CCD section for quadrant C
    CLOCK14  9.9992,2.9993                                                str     [V] high rail, low rail
    CLOCK3   -2.0001,3.9999                                               str     [V] high rail, low rail
    DIGITIME 47.5948                                                      float   [s] Time to digitize image
    CLOCK1   9.9999,0.0                                                   str     [V] high rail, low rail
    PRRSECD  [2193:4249, 4194:4194]                                       str     Row prescan section for quadrant D
    CLOCK9   9.9992,2.9993                                                str     [V] high rail, low rail
    CCDNAME  CCDSM9R                                                      str     CCD name
    DETSECB  [2058:4114, 1:2064]                                          str     Detector section for quadrant B
    CCDSECA  [1:2057, 1:2064]                                             str     CCD section for quadrant A
    DETSECD  [2058:4114, 2065:4128]                                       str     Detector section for quadrant D
    DATASECB [2193:4249, 2:2065]                                          str     Data section for quadrant B
    CRYOPRES 1.166e-07                                                    str     [mb] Cryostat pressure (IP)
    CAMERA   r5                                                           str     Camera name
    PRRSECA  [8:2064, 1:1]                                                str     Row prescan section for quadrant A
    DAC1     -9.0002,-8.9507                                              str     [V] set value, measured value
    PRESECC  [1:7, 2130:4193]                                             str     Prescan section for quadrant C
    TRIMSECA [8:2064, 2:2065]                                             str     Trim section for quadrant A
    TRIMSECD [2193:4249, 2130:4193]                                       str     Trim section for quadrant D
    CCDCFG   default_lbnl_20190717.cfg                                    str     CCD configuration file
    PRRSECB  [2193:4249, 1:1]                                             str     Row prescan section for quadrant B
    CLOCK12  9.9992,2.9993                                                str     [V] high rail, low rail
    CCDSECB  [2058:4114, 1:2064]                                          str     CCD section for quadrant B
    TRIMSECB [2193:4249, 2:2065]                                          str     Trim section for quadrant B
    DATASECA [8:2064, 2:2065]                                             str     Data section for quadrant A
    DAC17    20.0008,12.3342                                              str     [V] set value, measured value
    CLOCK17  9.0,0.9999                                                   str     [V] high rail, low rail
    PRESECB  [4250:4256, 2:2065]                                          str     Prescan section for quadrant B
    CLOCK0   9.9999,0.0                                                   str     [V] high rail, low rail
    PRESECA  [1:7, 2:2065]                                                str     Prescan section for quadrant A
    ORSECA   [8:2064, 2066:2097]                                          str     Row overscan section for quadrant A
    BIASSECC [2065:2128, 2130:4193]                                       str     Bias section for quadrant C
    DETSECC  [1:2057, 2065:4128]                                          str     Detector section for quadrant C
    DAC14    0.0,-0.0148                                                  str     [V] set value, measured value
    DAC4     5.9998,6.0595                                                str     [V] set value, measured value
    CLOCK16  9.9999,3.0                                                   str     [V] high rail, low rail
    AMPSECA  [1:2057, 1:2064]                                             str     AMP section for quadrant A
    OFFSET4  2.0,6.0595                                                   str     [V] set value, measured value
    CCDSIZE  4194,4256                                                    str     CCD size in pixels (rows, columns)
    OFFSET2  0.4000000059604645,-8.9301                                   str     [V] set value, measured value
    DAC13    0.0,-0.0148                                                  str     [V] set value, measured value
    CRYOTEMP 163.02                                                       float   [deg K] Cryostat CCD temperature
    OFFSET6  2.0,6.0437                                                   str     [V] set value, measured value
    CLOCK6   9.9999,0.0                                                   str     [V] high rail, low rail
    DETSECA  [1:2057, 1:2064]                                             str     Detector section for quadrant A
    CCDTMING default_lbnl_timing_20180905.txt                             str     CCD timing file
    DETECTOR M1-52                                                        str     Detector (ccd) identification
    OFFSET3  0.4000000059604645,-8.9816                                   str     [V] set value, measured value
    AMPSECC  [1:2057, 4128:2065]                                          str     AMP section for quadrant C
    CLOCK10  9.9992,2.9993                                                str     [V] high rail, low rail
    ORSECC   [8:2064, 2098:2129]                                          str     Row overscan section for quadrant C
    SETTINGS detectors_sm_20191211.json                                   str     Name of DESI CCD settings file
    CPUTEMP  58.9629                                                      float   [deg C] CCD controller CPU temperature
    OFFSET0  0.4000000059604645,-8.755                                    str     [V] set value, measured value
    DAC12    0.0,0.0                                                      str     [V] set value, measured value
    DATASECC [8:2064, 2130:4193]                                          str     Data section for quadrant C
    AMPSECD  [4114:2058, 4128:2065]                                       str     AMP section for quadrant D
    DAC10    -25.0003,-25.0054                                            str     [V] set value, measured value
    CLOCK7   -2.0001,3.9999                                               str     [V] high rail, low rail
    DAC0     -9.0002,-8.7653                                              str     [V] set value, measured value
    CLOCK11  9.9992,2.9993                                                str     [V] high rail, low rail
    DAC7     5.9998,6.0122                                                str     [V] set value, measured value
    OFFSET1  0.4000000059604645,-8.9507                                   str     [V] set value, measured value
    DAC5     5.9998,5.9964                                                str     [V] set value, measured value
    ORSECB   [2193:4249, 2066:2097]                                       str     Row overscan section for quadrant B
    CCDSECD  [2058:4114, 2065:4128]                                       str     CCD section for quadrant D
    PRRSECC  [8:2064, 4194:4194]                                          str     Row prescan section for quadrant C
    TRIMSECC [8:2064, 2130:4193]                                          str     Trim section for quadrant C
    BIASSECA [2065:2128, 2:2065]                                          str     Bias section for quadrant A
    REQTIME  120.0                                                        float   [s] Requested exposure time
    OBSID    kp4m20201220t222415                                          str     Unique observation identifier
    PROCTYPE RAW                                                          str     Data processing level
    PRODTYPE image                                                        str     Data product type
    CHECKSUM JfhdMZgdJfgdJZgd                                             str     HDU checksum updated 2022-01-29T00:45:28
    DATASUM  38776208                                                     str     data unit checksum updated 2022-01-29T00:45:28
    GAINA    1.684                                                        float   e/ADU (gain applied to image)
    SATULEVA 33000.0                                                      float   saturation or non lin. level, in ADU, inc. bias
    OSTEPA   0.6500495005602716                                           float   ADUs (max-min of median overscan per row)
    OMETHA   AVERAGE                                                      str     use average overscan
    OVERSCNA 1972.92976646288                                             float   ADUs (gain not applied)
    OBSRDNA  3.218229918807175                                            float   electrons (gain is applied)
    SATUELEA 52249.58627327651                                            float   saturation or non lin. level, in electrons
    GAINB    1.655                                                        float   e/ADU (gain applied to image)
    SATULEVB 47000.0                                                      float   saturation or non lin. level, in ADU, inc. bias
    OSTEPB   0.6179795354764792                                           float   ADUs (max-min of median overscan per row)
    OMETHB   AVERAGE                                                      str     use average overscan
    OVERSCNB 1975.23548556518                                             float   ADUs (gain not applied)
    OBSRDNB  3.153470147761547                                            float   electrons (gain is applied)
    SATUELEB 74515.98527138963                                            float   saturation or non lin. level, in electrons
    GAINC    1.467                                                        float   e/ADU (gain applied to image)
    SATULEVC 65535.0                                                      float   saturation or non lin. level, in ADU, inc. bias
    OSTEPC   0.5848174212296726                                           float   ADUs (max-min of median overscan per row)
    OMETHC   AVERAGE                                                      str     use average overscan
    OVERSCNC 1959.467167892971                                            float   ADUs (gain not applied)
    OBSRDNC  2.894849081776217                                            float   electrons (gain is applied)
    SATUELEC 93265.30666470101                                            float   saturation or non lin. level, in electrons
    GAIND    1.509                                                        float   e/ADU (gain applied to image)
    SATULEVD 65535.0                                                      float   saturation or non lin. level, in ADU, inc. bias
    OSTEPD   0.4709297982626595                                           float   ADUs (max-min of median overscan per row)
    OMETHD   AVERAGE                                                      str     use average overscan
    OVERSCND 1992.393350767962                                            float   ADUs (gain not applied)
    OBSRDND  2.694583892275785                                            float   electrons (gain is applied)
    SATUELED 95885.79343369114                                            float   saturation or non lin. level, in electrons
    FIBERMIN 2500                                                         int
    LONGSTRN OGIP 1.0                                                     str     The OGIP Long String Convention may be used.
    MODULE   CI                                                           str     Image Sources/Component
    FRAMES   None                                                         Unknown Number of Frames in Archive
    COSMSPLT F                                                            bool    Cosmics split exposure if true
    MAXSPLIT 0                                                            int     Number of allowed exposure splits
    SPLITIDS 68979                                                        str     List of expids for split exposures
    OBSTYPE  FLAT                                                         str     Spectrograph observation type
    MANIFEST F                                                            bool    DOS exposure manifest
    OBJECT                                                                str     Object name
    SEQID    3 requests                                                   str     Exposure sequence identifier
    SEQNUM   2                                                            int     Number of exposure in sequence
    SEQTOT   3                                                            int     Total number of exposures in sequence
    OPENSHUT None                                                         Unknown Time shutter opened
    CAMSHUT  open                                                         str     Shutter status during observation
    WHITESPT T                                                            bool    Telescope is at whitespot
    ZENITH   F                                                            bool    Telescope is at zenith
    SEANNEX  F                                                            bool    Telescope is at SE annex
    BEYONDP  F                                                            bool    Telescope is beyond pole
    FIDUCIAL off                                                          str     Fiducials status during observation
    AIRMASS  1.521306                                                     float   Airmass
    FOCUS    1163.9,-689.8,370.4,13.8,24.2,-0.0                           str     Telescope focus settings
    TRUSTEMP 13.267                                                       float   [deg] Average Telescope truss temperature (only
    PMIRTEMP 7.35                                                         float   [deg] Average primary mirror temperature (nit,e
    PMREADY  F                                                            bool    Primary mirror ready
    PMCOVER  open                                                         str     Primary mirror cover
    PMCOOL   on                                                           str     Primary mirror cooling
    DOMSHUTU not open                                                     str     Upper dome shutter
    DOMSHUTL not open                                                     str     Lower dome shutter
    DOMLIGHH off                                                          str     High dome lights
    DOMLIGHL off                                                          str     Low dome lights
    DOMEAZ   253.289                                                      float   [deg] Dome azimuth angle
    DOMINPOS F                                                            bool    Dome is in position
    GUIDOFFR 0.0                                                          float   [arcsec] Cummulative guider offset (RA)
    GUIDOFFD -0.0                                                         float   [arcsec] Cummulative guider offset (dec)
    MOONDEC  -9.830944                                                    float   [deg] Moon declination at start of exposure
    MOONRA   350.511461                                                   float   [deg] Moon RA at start of exposure
    MOUNTAZ  73.49407                                                     float   [deg] Mount azimuth angle
    MOUNTDEC 31.962703                                                    float   [deg] Mount declination
    MOUNTEL  41.035778                                                    float   [deg] Mount elevation angle
    MOUNTHA  -58.479517                                                   float   [deg] Mount hour angle
    INCTRL   F                                                            bool    DESI in control
    INPOS    T                                                            bool    Mount in position
    MNTOFFD  -0.0                                                         float   [arcsec] Mount offset (dec)
    MNTOFFR  -0.0                                                         float   [arcsec] Mount offset (RA)
    PARALLAC -73.492813                                                   float   [deg] Parallactic angle
    SKYDEC   31.962703                                                    float   [deg] Telescope declination (pointing on sky)
    SKYRA    12.901561                                                    float   [deg] Telescope right ascension (pointing on sk
    TARGTDEC 31.963299                                                    float   [deg] Target declination (to TCS)
    TARGTRA  6.305086                                                     float   [deg] Target right ascension (to TCS)
    TARGTAZ  75.558672                                                    float   [deg] Target azimuth
    TARGTEL  46.429343                                                    float   [deg] Target elevation
    TRGTOFFD 0.0                                                          float   [arcsec] Telescope target offset (dec)
    TRGTOFFR 0.0                                                          float   [arcsec] Telescope target offset (RA)
    ZD       48.964222                                                    float   [deg] Telescope zenith distance
    TCSST    20:57:41.291                                                 str     Local Sidereal time reported by TCS (HH:MM:SS)
    TCSMJD   59203.933945                                                 float   MJD reported by TCS
    ADCCORR  F                                                            bool    Correct pointing for ADC setting if True
    ADC1PHI  114.980003                                                   float   [deg] ADC 1 angle
    ADC2PHI  162.869907                                                   float   [deg] ADC 2 angle
    ADC1HOME F                                                            bool    ADC 1 at home position if True
    ADC2HOME F                                                            bool    ADC 2 at home position if True
    ADC1NREV 0.0                                                          float   ADC 1 number of revs
    ADC2NREV -1.0                                                         float   ADC 2 number of revs
    ADC1STAT STOPPED                                                      str     ADC 1 status
    ADC2STAT STOPPED                                                      str     ADC 2 status
    HEXPOS   1163.9,-689.8,370.4,13.8,24.2,-0.0                           str     Hexapod position
    HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                                      str     Hexapod trim values
    ROTOFFST 0.0                                                          float   [arcsec] Rotator offset
    ROTENBLD T                                                            bool    Rotator enabled
    ROTRATE  0.0                                                          float   [arcsec/min] Rotator rate
    RESETROT F                                                            bool    DOS Control: reset hex rotator
    GUIDMODE catalog                                                      str     Guider mode
    USEAOS   F                                                            bool    DOS Control: AOS data available if true
    SPCGRPHS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                      str     Participating spectrograph
    ILLSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                      str     Participating illuminate s
    CCDSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                      str     Participating ccd spectrog
    TDEWPNT  -18.2                                                        float   Telescope air dew point
    TAIRFLOW 1.121                                                        float   Telescope air flow
    TAIRITMP 10.5                                                         float   [deg] Telescope air in temperature
    TAIROTMP 5.5                                                          float   [deg] Telescope air out temperature
    TAIRTEMP 11.86                                                        float   [deg] Telescope air temperature
    TCASITMP 0.0                                                          float   [deg] Telescope Cass Cage in temperature
    TCASOTMP 9.6                                                          float   [deg] Telescope Cass Cage out temperature
    TCSITEMP 7.4                                                          float   [deg] Telescope center section in temperature
    TCSOTEMP 10.2                                                         float   [deg] Telescope center section out temperature
    TCIBTEMP 0.0                                                          float   [deg] Telescope chimney IB temperature
    TCIMTEMP 0.0                                                          float   [deg] Telescope chimney IM temperature
    TCITTEMP 0.0                                                          float   [deg] Telescope chimney IT temperature
    TCOSTEMP 0.0                                                          float   [deg] Telescope chimney OS temperature
    TCOWTEMP 0.0                                                          float   [deg] Telescope chimney OW temperature
    TDBTEMP  7.4                                                          float   [deg] Telescope dec bore temperature
    TFLOWIN  7.7                                                          float   Telescope flow rate in
    TFLOWOUT 8.3                                                          float   Telescope flow rate out
    TGLYCOLI -1.8                                                         float   [deg] Telescope glycol in temperature
    TGLYCOLO 0.0                                                          float   [deg] Telescope glycol out temperature
    THINGES  12.9                                                         float   [deg] Telescope hinge S temperature
    THINGEW  11.7                                                         float   [deg] Telescope hinge W temperature
    TPMAVERT 7.304                                                        float   [deg] Telescope mirror averagetemperature
    TPMDESIT 7.0                                                          float   [deg] Telescope mirror desired temperature
    TPMEIBT  7.3                                                          float   [deg] Telescope mirror EIB temperature
    TPMEITT  7.3                                                          float   [deg] Telescope mirror EIT temperature
    TPMEOBT  7.4                                                          float   [deg] Telescope mirror EOB temperature
    TPMEOTT  7.2                                                          float   [deg] Telescope mirror EOT temperature
    TPMNIBT  7.4                                                          float   [deg] Telescope mirror NIB temperature
    TPMNITT  7.3                                                          float   [deg] Telescope mirror NIT temperature
    TPMNOBT  7.7                                                          float   [deg] Telescope mirror NOB temperature
    TPMNOTT  7.6                                                          float   [deg] Telescope mirror NOT temperature
    TPMRTDT  6.96                                                         float   [deg] Telescope mirror RTD temperature
    TPMSIBT  7.4                                                          float   [deg] Telescope mirror SIB temperature
    TPMSITT  7.0                                                          float   [deg] Telescope mirror SIT temperature
    TPMSOBT  7.4                                                          float   [deg] Telescope mirror SOB temperature
    TPMSOTT  7.2                                                          float   [deg] Telescope mirror SOT temperature
    TPMSTAT  soft air                                                     str     Telescope mirror status
    TPMWIBT  7.2                                                          float   [deg] Telescope mirror WIB temperature
    TPMWITT  7.1                                                          float   [deg] Telescope mirror WIT temperature
    TPMWOBT  7.6                                                          float   [deg] Telescope mirror WOB temperature
    TPMWOTT  8.1                                                          float   [deg] Telescope mirror WOT temperature
    TPCITEMP 7.7                                                          float   [deg] Telescope primary cell in temperature
    TPCOTEMP 7.7                                                          float   [deg] Telescope primary cell out temperature
    TPR1HUM  0.0                                                          float   Telescope probe 1 humidity
    TPR1TEMP 0.0                                                          float   [deg] Telescope probe1 temperature
    TPR2HUM  0.0                                                          float   Telescope probe 2 humidity
    TPR2TEMP 0.0                                                          float   [deg] Telescope probe2 temperature
    TSERVO   7.0                                                          float   Telescope servo setpoint
    TTRSTEMP 13.2                                                         float   [deg] Telescope top ring S temperature
    TTRWTEMP 13.4                                                         float   [deg] Telescope top ring W temperature
    TTRUETBT -4.8                                                         float   [deg] Telescope truss ETB temperature
    TTRUETTT 11.5                                                         float   [deg] Telescope truss ETT temperature
    TTRUNTBT 10.9                                                         float   [deg] Telescope truss NTB temperature
    TTRUNTTT 11.8                                                         float   [deg] Telescope truss NTT temperature
    TTRUSTBT 11.1                                                         float   [deg] Telescope truss STB temperature
    TTRUSTST 10.8                                                         float   [deg] Telescope truss STS temperature
    TTRUSTTT 12.4                                                         float   [deg] Telescope truss STT temperature
    TTRUTSBT 13.6                                                         float   [deg] Telescope truss TSB temperature
    TTRUTSMT 13.7                                                         float   [deg] Telescope truss TSM temperature
    TTRUTSTT 12.5                                                         float   [deg] Telescope truss TST temperature
    TTRUWTBT 10.9                                                         float   [deg] Telescope truss WTB temperature
    TTRUWTTT 11.6                                                         float   [deg] Telescope truss WTT temperature
    ALARM    F                                                            bool    UPS major alarm or check battery
    ALARM-ON F                                                            bool    UPS active alarm condition
    BATTERY  100.0                                                        float   [%] UPS Battery left
    SECLEFT  5772.0                                                       float   [s] UPS Seconds left
    UPSSTAT  System Normal - On Line(7)                                   str     UPS Status
    INAMPS   64.3                                                         float   [A] UPS total input current
    OUTWATTS 4500.0,6800.0,4100.0                                         str     [W] UPS Phase A, B, C output watts
    COMPDEW  -12.0                                                        float   [deg C] Computer room dewpoint
    COMPHUM  7.8                                                          float   [%] Computer room humidity
    COMPAMB  19.4                                                         float   [deg C] Computer room ambient temperature
    COMPTEMP 24.9                                                         float   [deg C] Computer room hygrometer temperature
    DEWPOINT 5.7                                                          float   [deg C] (outside) dewpoint
    HUMIDITY 7.0                                                          float   [%] (outside) humidity
    PRESSURE 794.7                                                        float   [torr] (outside) air pressure
    OUTTEMP  0.0                                                          float   [deg C] outside temperature
    WINDDIR  82.0                                                         float   [deg] wind direction
    WINDSPD  23.3                                                         float   [m/s] wind speed
    GUST     18.1                                                         float   [m/s] Wind gusts speed
    AMNIENTN 13.3                                                         float   [deg C] ambient temperature north
    CFLOOR   8.1                                                          float   [deg C] temperature on C floor
    NWALLIN  13.6                                                         float   [deg C] temperature at north wall inside
    NWALLOUT 8.8                                                          float   [deg C] temperature at north wall outside
    WWALLIN  12.8                                                         float   [deg C] temperature at west wall inside
    WWALLOUT 9.4                                                          float   [deg C] temperature at west wall outside
    AMBIENTS 14.6                                                         float   [deg C] ambient temperature south
    FLOOR    12.3                                                         float   [deg C] temperature at floor (LCR)
    EWALLCMP 10.2                                                         float   [deg C] temperature at east wall, computer room
    EWALLCOU 9.5                                                          float   [deg C] temperature at east wall, Coude room
    ROOF     10.0                                                         float   [deg C] temperature on roof
    ROOFAMB  9.9                                                          float   [deg C] ambient temperature on roof
    DOMEBLOW 12.1                                                         float   [deg C] temperature at dome back, lower
    DOMEBUP  12.5                                                         float   [deg C] temperature at dome back, upper
    DOMELLOW 14.4                                                         float   [deg C] temperature at dome left, lower
    DOMELUP  19.3                                                         float   [deg C] temperature at dome left, upper
    DOMERLOW 12.3                                                         float   [deg C] temperature at dome right, lower
    DOMERUP  12.8                                                         float   [deg C] temperature at dome right, upper
    PLATFORM 15.3                                                         float   [deg C] temperature at platform
    SHACKC   15.2                                                         float   [deg C] temperature at shack ceiling
    SHACKW   13.2                                                         float   [deg C] temperature at shack wall
    STAIRSL  12.6                                                         float   [deg C] temperature at stairs, lower
    STAIRSM  13.3                                                         float   [deg C] temperature at stairs, mid
    STAIRSU  13.6                                                         float   [deg C] temperature at stairs, upper
    TELBASE  8.5                                                          float   [deg C] temperature at telescope base
    UTILWALL 11.6                                                         float   [deg C] temperature at utility room wall
    UTILROOM 12.4                                                         float   [deg C] temperature in utilitiy room
    EXCLUDED                                                              str     Components excluded from this exposure
    ======== ============================================================ ======= ===============================================

Data: FITS image [float32, 4114x4128]

HDU1
----

EXTNAME = IVAR

2D image with the inverse variance (1/sigma^2) of the flat-fielded pixel values. The units are 1/electrons^2.
The variance comprises read noise and Poisson noise from the signal (including Poisson noise from the dark current).
The Poisson noise is based on a model of the illumination of the CCD to minimize the correlation between the noise realization
in the pixel value and the estimated variance. The variance also comprise the noise of the calibration data (master bias and master dark).

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   4114             int
    NAXIS2   4128             int
    CHECKSUM MOb9PMb6MMb6MMb6 str  HDU checksum updated 2022-01-29T00:45:32
    DATASUM  3688631381       str  data unit checksum updated 2022-01-29T00:45:32
    ======== ================ ==== ==============================================

Data: FITS image [float32, 4114x4128]

HDU2
----

EXTNAME = MASK

2D image with bitmask values for the pixels. Good pixels have a mask=0. See
the TBD webpage for the definition of the bits.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   8                int  width of table in bytes
    NAXIS2   4128             int  number of rows in table
    CHECKSUM GfAAId07Gd7AGd77 str  HDU checksum updated 2022-01-29T00:45:35
    DATASUM  856031529        str  data unit checksum updated 2022-01-29T00:45:35
    ======== ================ ==== ==============================================

Data: FITS image [int16 (compressed), 4114x4128]

HDU3
----

EXTNAME = READNOISE

Flat-fielded read noise in electrons. Read noise abusively includes the Poisson noise
from clock induced charges for some CCDs along with the Poisson noise from the
dark current and the calibration frame uncertainties.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   4114             int
    NAXIS2   4128             int
    CHECKSUM cRUgeQRecQRecQRe str  HDU checksum updated 2022-01-29T00:45:38
    DATASUM  2700029362       str  data unit checksum updated 2022-01-29T00:45:38
    ======== ================ ==== ==============================================

Data: FITS image [float32, 4114x4128]

HDU4
----

EXTNAME = FIBERMAP

Exposure :doc:`fibermap <fibermap-EXPID>` trimmed to the fibers of this camera.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ============================================================ ======= ==============================================
    KEY      Example Value                                                Type    Comment
    ======== ============================================================ ======= ==============================================
    NAXIS1   369                                                          int     length of dimension 1
    NAXIS2   500                                                          int     length of dimension 2
    EXPID    68979                                                        int
    EXPFRAME 0                                                            int
    FLAVOR   science                                                      str
    SEQUENCE Spectrographs                                                str
    PURPOSE  Commissioning                                                str
    PROGRAM  CALIB DESI-CALIB-00 LEDs only                                str
    PROPID   2019B-5000                                                   str
    OBSERVER DESIObserver                                                 str
    LEAD     RunManager                                                   str
    INSTRUME DESI                                                         str
    OBSERVAT KPNO                                                         str
    OBS-LAT  31.96403                                                     str
    OBS-LONG -111.59989                                                   str
    OBS-ELEV 2097.0                                                       float
    TELESCOP KPNO 4.0-m telescope                                         str
    CORRCTOR DESI Corrector                                               str
    NIGHT    20201220                                                     int
    TIMESYS  UTC                                                          str
    DATE-OBS 2020-12-20T22:24:15.672815                                   str
    TIME-OBS 22:24:15.672815                                              str
    MJD-OBS  59203.93351473                                               float
    ST       20:57:41.340                                                 str
    EXPTIME  120.037                                                      float
    DELTARA  0.0                                                          float
    DELTADEC 0.0                                                          float
    VCCD     ON                                                           str
    VCCDON   2020-12-14T04:22:19.522101                                   str
    VCCDSEC  583485.8                                                     float
    EQUINOX  2000.0                                                       float
    SPECGRPH 5                                                            int
    SPECID   9                                                            int
    FEEBOX   lbnl057                                                      str
    VESSEL   26                                                           int
    FEEVER   v20160312                                                    str
    FEEPOWER ON                                                           str
    FEEDMASK 2134851391                                                   int
    FEECMASK 1048575                                                      int
    CCDTEMP  -135.8073                                                    float
    RADESYS  FK5                                                          str
    FILENAME /exposures/desi/specs/20201220/00068979/sp9-00068979.fits.fz str
    DOSVER   trunk                                                        str
    OCSVER   1.2                                                          float
    CONSTVER DESI:CURRENT                                                 str
    INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini             str
    DAC3     -9.0002,-8.9919                                              str
    CLOCK5   9.9999,0.0                                                   str
    BLDTIME  0.3522                                                       float
    CLOCK2   9.9999,0.0                                                   str
    BIASSECD [2129:2192, 2130:4193]                                       str
    PGAGAIN  3                                                            int
    OFFSET5  2.0,5.9964                                                   str
    BIASSECB [2129:2192, 2:2065]                                          str
    CLOCK4   9.9999,0.0                                                   str
    ORSECD   [2193:4249, 2098:2129]                                       str
    DAC2     -9.0002,-8.9404                                              str
    DAC6     5.9998,6.0437                                                str
    CCDPREP  purge,clear                                                  str
    CASETEMP 59.322                                                       float
    DAC15    0.0,-0.0148                                                  str
    DAC16    39.9961,39.8706                                              str
    DAC9     -25.0003,-24.6344                                            str
    AMPSECB  [4114:2058, 1:2064]                                          str
    DAC11    -25.0003,-24.5157                                            str
    DELAYS   20, 20, 25, 40, 7, 3000, 7, 7, 7, 7                          str
    CLOCK13  9.9992,2.9993                                                str
    PRESECD  [4250:4256, 2130:4193]                                       str
    CDSPARMS 400, 400, 8, 2000                                            str
    DATASECD [2193:4249, 2130:4193]                                       str
    CLOCK15  9.9992,2.9993                                                str
    CLOCK18  9.0,0.9999                                                   str
    CLOCK8   9.9992,2.9993                                                str
    OFFSET7  2.0,6.0122                                                   str
    DAC8     -25.0003,-24.946                                             str
    CCDSECC  [1:2057, 2065:4128]                                          str
    CLOCK14  9.9992,2.9993                                                str
    CLOCK3   -2.0001,3.9999                                               str
    DIGITIME 47.5948                                                      float
    CLOCK1   9.9999,0.0                                                   str
    PRRSECD  [2193:4249, 4194:4194]                                       str
    CLOCK9   9.9992,2.9993                                                str
    CCDNAME  CCDSM9R                                                      str
    DETSECB  [2058:4114, 1:2064]                                          str
    CCDSECA  [1:2057, 1:2064]                                             str
    DETSECD  [2058:4114, 2065:4128]                                       str
    DATASECB [2193:4249, 2:2065]                                          str
    CRYOPRES 1.166e-07                                                    str
    CAMERA   r5                                                           str
    PRRSECA  [8:2064, 1:1]                                                str
    DAC1     -9.0002,-8.9507                                              str
    PRESECC  [1:7, 2130:4193]                                             str
    TRIMSECA [8:2064, 2:2065]                                             str
    TRIMSECD [2193:4249, 2130:4193]                                       str
    CCDCFG   default_lbnl_20190717.cfg                                    str
    PRRSECB  [2193:4249, 1:1]                                             str
    CLOCK12  9.9992,2.9993                                                str
    CCDSECB  [2058:4114, 1:2064]                                          str
    TRIMSECB [2193:4249, 2:2065]                                          str
    DATASECA [8:2064, 2:2065]                                             str
    DAC17    20.0008,12.3342                                              str
    CLOCK17  9.0,0.9999                                                   str
    PRESECB  [4250:4256, 2:2065]                                          str
    CLOCK0   9.9999,0.0                                                   str
    PRESECA  [1:7, 2:2065]                                                str
    ORSECA   [8:2064, 2066:2097]                                          str
    BIASSECC [2065:2128, 2130:4193]                                       str
    DETSECC  [1:2057, 2065:4128]                                          str
    DAC14    0.0,-0.0148                                                  str
    DAC4     5.9998,6.0595                                                str
    CLOCK16  9.9999,3.0                                                   str
    AMPSECA  [1:2057, 1:2064]                                             str
    OFFSET4  2.0,6.0595                                                   str
    CCDSIZE  4194,4256                                                    str
    OFFSET2  0.4000000059604645,-8.9301                                   str
    DAC13    0.0,-0.0148                                                  str
    CRYOTEMP 163.02                                                       float
    OFFSET6  2.0,6.0437                                                   str
    CLOCK6   9.9999,0.0                                                   str
    DETSECA  [1:2057, 1:2064]                                             str
    CCDTMING default_lbnl_timing_20180905.txt                             str
    DETECTOR M1-52                                                        str
    OFFSET3  0.4000000059604645,-8.9816                                   str
    AMPSECC  [1:2057, 4128:2065]                                          str
    CLOCK10  9.9992,2.9993                                                str
    ORSECC   [8:2064, 2098:2129]                                          str
    SETTINGS detectors_sm_20191211.json                                   str
    CPUTEMP  58.9629                                                      float
    OFFSET0  0.4000000059604645,-8.755                                    str
    DAC12    0.0,0.0                                                      str
    DATASECC [8:2064, 2130:4193]                                          str
    AMPSECD  [4114:2058, 4128:2065]                                       str
    DAC10    -25.0003,-25.0054                                            str
    CLOCK7   -2.0001,3.9999                                               str
    DAC0     -9.0002,-8.7653                                              str
    CLOCK11  9.9992,2.9993                                                str
    DAC7     5.9998,6.0122                                                str
    OFFSET1  0.4000000059604645,-8.9507                                   str
    DAC5     5.9998,5.9964                                                str
    ORSECB   [2193:4249, 2066:2097]                                       str
    CCDSECD  [2058:4114, 2065:4128]                                       str
    PRRSECC  [8:2064, 4194:4194]                                          str
    TRIMSECC [8:2064, 2130:4193]                                          str
    BIASSECA [2065:2128, 2:2065]                                          str
    REQTIME  120.0                                                        float
    OBSID    kp4m20201220t222415                                          str
    PROCTYPE RAW                                                          str
    PRODTYPE image                                                        str
    GAINA    1.684                                                        float
    SATULEVA 33000.0                                                      float
    OSTEPA   0.6500495005602716                                           float
    OMETHA   AVERAGE                                                      str
    OVERSCNA 1972.92976646288                                             float
    OBSRDNA  3.218229918807175                                            float
    SATUELEA 52249.58627327651                                            float
    GAINB    1.655                                                        float
    SATULEVB 47000.0                                                      float
    OSTEPB   0.6179795354764792                                           float
    OMETHB   AVERAGE                                                      str
    OVERSCNB 1975.23548556518                                             float
    OBSRDNB  3.153470147761547                                            float
    SATUELEB 74515.98527138963                                            float
    GAINC    1.467                                                        float
    SATULEVC 65535.0                                                      float
    OSTEPC   0.5848174212296726                                           float
    OMETHC   AVERAGE                                                      str
    OVERSCNC 1959.467167892971                                            float
    OBSRDNC  2.894849081776217                                            float
    SATUELEC 93265.30666470101                                            float
    GAIND    1.509                                                        float
    SATULEVD 65535.0                                                      float
    OSTEPD   0.4709297982626595                                           float
    OMETHD   AVERAGE                                                      str
    OVERSCND 1992.393350767962                                            float
    OBSRDND  2.694583892275785                                            float
    SATUELED 95885.79343369114                                            float
    FIBERMIN 2500                                                         int
    LONGSTRN OGIP 1.0                                                     str
    MODULE   CI                                                           str
    FRAMES   None                                                         Unknown
    COSMSPLT F                                                            bool
    MAXSPLIT 0                                                            int
    SPLITIDS 68979                                                        str
    OBSTYPE  FLAT                                                         str
    MANIFEST F                                                            bool
    OBJECT                                                                str
    SEQID    3 requests                                                   str
    SEQNUM   2                                                            int
    SEQTOT   3                                                            int
    OPENSHUT None                                                         Unknown
    CAMSHUT  open                                                         str
    WHITESPT T                                                            bool
    ZENITH   F                                                            bool
    SEANNEX  F                                                            bool
    BEYONDP  F                                                            bool
    FIDUCIAL off                                                          str
    AIRMASS  1.521306                                                     float
    FOCUS    1163.9,-689.8,370.4,13.8,24.2,-0.0                           str
    TRUSTEMP 13.267                                                       float
    PMIRTEMP 7.35                                                         float
    PMREADY  F                                                            bool
    PMCOVER  open                                                         str
    PMCOOL   on                                                           str
    DOMSHUTU not open                                                     str
    DOMSHUTL not open                                                     str
    DOMLIGHH off                                                          str
    DOMLIGHL off                                                          str
    DOMEAZ   253.289                                                      float
    DOMINPOS F                                                            bool
    GUIDOFFR 0.0                                                          float
    GUIDOFFD -0.0                                                         float
    MOONDEC  -9.830944                                                    float
    MOONRA   350.511461                                                   float
    MOUNTAZ  73.49407                                                     float
    MOUNTDEC 31.962703                                                    float
    MOUNTEL  41.035778                                                    float
    MOUNTHA  -58.479517                                                   float
    INCTRL   F                                                            bool
    INPOS    T                                                            bool
    MNTOFFD  -0.0                                                         float
    MNTOFFR  -0.0                                                         float
    PARALLAC -73.492813                                                   float
    SKYDEC   31.962703                                                    float
    SKYRA    12.901561                                                    float
    TARGTDEC 31.963299                                                    float
    TARGTRA  6.305086                                                     float
    TARGTAZ  75.558672                                                    float
    TARGTEL  46.429343                                                    float
    TRGTOFFD 0.0                                                          float
    TRGTOFFR 0.0                                                          float
    ZD       48.964222                                                    float
    TCSST    20:57:41.291                                                 str
    TCSMJD   59203.933945                                                 float
    ADCCORR  F                                                            bool
    ADC1PHI  114.980003                                                   float
    ADC2PHI  162.869907                                                   float
    ADC1HOME F                                                            bool
    ADC2HOME F                                                            bool
    ADC1NREV 0.0                                                          float
    ADC2NREV -1.0                                                         float
    ADC1STAT STOPPED                                                      str
    ADC2STAT STOPPED                                                      str
    HEXPOS   1163.9,-689.8,370.4,13.8,24.2,-0.0                           str
    HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                                      str
    ROTOFFST 0.0                                                          float
    ROTENBLD T                                                            bool
    ROTRATE  0.0                                                          float
    RESETROT F                                                            bool
    GUIDMODE catalog                                                      str
    USEAOS   F                                                            bool
    SPCGRPHS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                      str
    ILLSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                      str
    CCDSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                      str
    TDEWPNT  -18.2                                                        float
    TAIRFLOW 1.121                                                        float
    TAIRITMP 10.5                                                         float
    TAIROTMP 5.5                                                          float
    TAIRTEMP 11.86                                                        float
    TCASITMP 0.0                                                          float
    TCASOTMP 9.6                                                          float
    TCSITEMP 7.4                                                          float
    TCSOTEMP 10.2                                                         float
    TCIBTEMP 0.0                                                          float
    TCIMTEMP 0.0                                                          float
    TCITTEMP 0.0                                                          float
    TCOSTEMP 0.0                                                          float
    TCOWTEMP 0.0                                                          float
    TDBTEMP  7.4                                                          float
    TFLOWIN  7.7                                                          float
    TFLOWOUT 8.3                                                          float
    TGLYCOLI -1.8                                                         float
    TGLYCOLO 0.0                                                          float
    THINGES  12.9                                                         float
    THINGEW  11.7                                                         float
    TPMAVERT 7.304                                                        float
    TPMDESIT 7.0                                                          float
    TPMEIBT  7.3                                                          float
    TPMEITT  7.3                                                          float
    TPMEOBT  7.4                                                          float
    TPMEOTT  7.2                                                          float
    TPMNIBT  7.4                                                          float
    TPMNITT  7.3                                                          float
    TPMNOBT  7.7                                                          float
    TPMNOTT  7.6                                                          float
    TPMRTDT  6.96                                                         float
    TPMSIBT  7.4                                                          float
    TPMSITT  7.0                                                          float
    TPMSOBT  7.4                                                          float
    TPMSOTT  7.2                                                          float
    TPMSTAT  soft air                                                     str
    TPMWIBT  7.2                                                          float
    TPMWITT  7.1                                                          float
    TPMWOBT  7.6                                                          float
    TPMWOTT  8.1                                                          float
    TPCITEMP 7.7                                                          float
    TPCOTEMP 7.7                                                          float
    TPR1HUM  0.0                                                          float
    TPR1TEMP 0.0                                                          float
    TPR2HUM  0.0                                                          float
    TPR2TEMP 0.0                                                          float
    TSERVO   7.0                                                          float
    TTRSTEMP 13.2                                                         float
    TTRWTEMP 13.4                                                         float
    TTRUETBT -4.8                                                         float
    TTRUETTT 11.5                                                         float
    TTRUNTBT 10.9                                                         float
    TTRUNTTT 11.8                                                         float
    TTRUSTBT 11.1                                                         float
    TTRUSTST 10.8                                                         float
    TTRUSTTT 12.4                                                         float
    TTRUTSBT 13.6                                                         float
    TTRUTSMT 13.7                                                         float
    TTRUTSTT 12.5                                                         float
    TTRUWTBT 10.9                                                         float
    TTRUWTTT 11.6                                                         float
    ALARM    F                                                            bool
    ALARM-ON F                                                            bool
    BATTERY  100.0                                                        float
    SECLEFT  5772.0                                                       float
    UPSSTAT  System Normal - On Line(7)                                   str
    INAMPS   64.3                                                         float
    OUTWATTS 4500.0,6800.0,4100.0                                         str
    COMPDEW  -12.0                                                        float
    COMPHUM  7.8                                                          float
    COMPAMB  19.4                                                         float
    COMPTEMP 24.9                                                         float
    DEWPOINT 5.7                                                          float
    HUMIDITY 7.0                                                          float
    PRESSURE 794.7                                                        float
    OUTTEMP  0.0                                                          float
    WINDDIR  82.0                                                         float
    WINDSPD  23.3                                                         float
    GUST     18.1                                                         float
    AMNIENTN 13.3                                                         float
    CFLOOR   8.1                                                          float
    NWALLIN  13.6                                                         float
    NWALLOUT 8.8                                                          float
    WWALLIN  12.8                                                         float
    WWALLOUT 9.4                                                          float
    AMBIENTS 14.6                                                         float
    FLOOR    12.3                                                         float
    EWALLCMP 10.2                                                         float
    EWALLCOU 9.5                                                          float
    ROOF     10.0                                                         float
    ROOFAMB  9.9                                                          float
    DOMEBLOW 12.1                                                         float
    DOMEBUP  12.5                                                         float
    DOMELLOW 14.4                                                         float
    DOMELUP  19.3                                                         float
    DOMERLOW 12.3                                                         float
    DOMERUP  12.8                                                         float
    PLATFORM 15.3                                                         float
    SHACKC   15.2                                                         float
    SHACKW   13.2                                                         float
    STAIRSL  12.6                                                         float
    STAIRSM  13.3                                                         float
    STAIRSU  13.6                                                         float
    TELBASE  8.5                                                          float
    UTILWALL 11.6                                                         float
    UTILROOM 12.4                                                         float
    EXCLUDED                                                              str
    CHECKSUM oLYrpJYooJYooJYo                                             str     HDU checksum updated 2022-01-29T00:45:38
    DATASUM  1239496881                                                   str     data unit checksum updated 2022-01-29T00:45:38
    ======== ============================================================ ======= ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

===================== ======= ================== ===========
Name                  Type    Units              Description
===================== ======= ================== ===========
TARGETID              int64
PETAL_LOC             int16
DEVICE_LOC            int32
LOCATION              int64
FIBER                 int32
FIBERSTATUS           int32
TARGET_RA             float64 deg
TARGET_DEC            float64 deg
PMRA                  float32 10**-3 arcsec yr-1
PMDEC                 float32 10**-3 arcsec yr-1
REF_EPOCH             float32
LAMBDA_REF            float32 Angstrom
FA_TARGET             int64
FA_TYPE               binary
OBJTYPE               char[3]
FIBERASSIGN_X         float32 mm
FIBERASSIGN_Y         float32 mm
PRIORITY              int32
SUBPRIORITY           float64
OBSCONDITIONS         int32
RELEASE               int16
BRICKNAME             char[8]
BRICKID               int64
BRICK_OBJID           int64
MORPHTYPE             char[4]
EBV                   float32
FLUX_G                float32 nanomaggies
FLUX_R                float32 nanomaggies
FLUX_Z                float32 nanomaggies
FLUX_W1               float32 nanomaggies
FLUX_W2               float32 nanomaggies
FLUX_IVAR_G           float32 1/nanomaggies**2
FLUX_IVAR_R           float32 1/nanomaggies**2
FLUX_IVAR_Z           float32 1/nanomaggies**2
FLUX_IVAR_W1          float32 1/nanomaggies**2
FLUX_IVAR_W2          float32 1/nanomaggies**2
FIBERFLUX_G           float32 nanomaggies
FIBERFLUX_R           float32 nanomaggies
FIBERFLUX_Z           float32 nanomaggies
FIBERTOTFLUX_G        float32 nanomaggies
FIBERTOTFLUX_R        float32 nanomaggies
FIBERTOTFLUX_Z        float32 nanomaggies
MASKBITS              int16
SERSIC                float32
SHAPE_R               float32 arcsec
SHAPE_E1              float32
SHAPE_E2              float32
REF_ID                int64
REF_CAT               char[2]
GAIA_PHOT_G_MEAN_MAG  float32 mag
GAIA_PHOT_BP_MEAN_MAG float32 mag
GAIA_PHOT_RP_MEAN_MAG float32 mag
PARALLAX              float32 10**-3 arcsec
PHOTSYS               char[1]
PRIORITY_INIT         int64
NUMOBS_INIT           int64
DESI_TARGET           int64
BGS_TARGET            int64
MWS_TARGET            int64
SCND_TARGET           int64
PLATE_RA              float64 deg
PLATE_DEC             float64 deg
NUM_ITER              int64
FIBER_X               float64 mm
FIBER_Y               float64 mm
DELTA_X               float64 mm
DELTA_Y               float64 mm
FIBER_RA              float64 deg
FIBER_DEC             float64 deg
EXPTIME               float64 s
===================== ======= ================== ===========


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
