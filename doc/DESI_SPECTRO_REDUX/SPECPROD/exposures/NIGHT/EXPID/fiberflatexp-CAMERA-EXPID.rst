============
fiberflatexp
============

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``fiberflatexp-{CAMERA}-{EXPID}.fits``, where ``{camera}`` is the camera
    name (*e.g.* b0, r1, z9) and ``{EXPID}`` is the zero padded 8-digit exposure ID.
:Regex: ``fiberflatexp-[brz][0-9]-[0-9]{8}\.fits``
:File Type: FITS, 15 MB

Contents
========

====== ========== ======== ===================
Number EXTNAME    Type     Contents
====== ========== ======== ===================
HDU0_  FIBERFLAT  IMAGE    *Brief Description*
HDU1_  IVAR       IMAGE    *Brief Description*
HDU2_  MASK       IMAGE    *Brief Description*
HDU3_  MEANSPEC   IMAGE    *Brief Description*
HDU4_  WAVELENGTH IMAGE    *Brief Description*
HDU5_  FIBERMAP   BINTABLE *Brief Description*
====== ========== ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = FIBERFLAT

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords table

    .. rst-class:: keywords

    ======== ============================================================ ======= ====================================================
    KEY      Example Value                                                Type    Comment
    ======== ============================================================ ======= ====================================================
    NAXIS1   2326                                                         int
    NAXIS2   500                                                          int
    EXPID    68978                                                        int     Exposure number
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
    DATE-OBS 2020-12-20T22:21:08.680251                                   str     [UTC] Observation data and start time
    TIME-OBS 22:21:08.680251                                              str     [UTC] Observation start time
    MJD-OBS  59203.93135047                                               float   Modified Julian Date of observation
    ST       20:54:33.840                                                 str     Local Sidereal time at observation start (HH:MM
    EXPTIME  120.042                                                      float   [s] Actual exposure time
    DELTARA  0.0                                                          float   [arcsec] Offset], right ascension, observer inp
    DELTADEC 0.0                                                          float   [arcsec] Offset], declination, observer input
    VCCD     ON                                                           str     True (ON) if CCD voltage is on
    VCCDON   2020-12-09T21:23:19.320868                                   str     Time when CCD voltage was turned on
    VCCDSEC  954038.9                                                     float   [s] CCD on time in seconds
    EQUINOX  2000.0                                                       float   Epoch of observation
    SPECGRPH 0                                                            int     Spectrograph logical name (SP)
    SPECID   4                                                            int     Spectrograph serial number (SM)
    FEEBOX   lbnl078                                                      str     CCD Controller serial number
    VESSEL   14                                                           int     Cryostat serial number
    FEEVER   v20160312                                                    str     CCD Controller version
    FEEPOWER ON                                                           str     FEE power status
    FEEDMASK 2134851391                                                   int     FEE dac mask
    FEECMASK 1048575                                                      int     FEE clk mask
    CCDTEMP  -142.1871                                                    float   [deg C] CCD controller CCD temperature
    RADESYS  FK5                                                          str     Coordinate reference frame of major/minor axes
    FILENAME /exposures/desi/specs/20201220/00068978/sp0-00068978.fits.fz str     Name
    DOSVER   trunk                                                        str     DOS software version
    OCSVER   1.2                                                          float   OCS software version
    CONSTVER DESI:CURRENT                                                 str     Constants version
    INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini             str     DOS Configuration
    CASETEMP 57.3533                                                      float   [deg C] CCD controller case temperature
    OFFSET1  0.4000000059604645,-8.858                                    str     [V] set value, measured value
    CLOCK18  9.0,0.9999                                                   str     [V] high rail, low rail
    BIASSECC [2065:2128, 2130:4193]                                       str     Bias section for quadrant C
    CLOCK12  9.9992,2.9993                                                str     [V] high rail, low rail
    CLOCK9   9.9992,2.9993                                                str     [V] high rail, low rail
    AMPSECC  [1:2057, 4128:2065]                                          str     AMP section for quadrant C
    DAC9     -25.0003,-24.5305                                            str     [V] set value, measured value
    CLOCK15  9.9992,2.9993                                                str     [V] high rail, low rail
    CLOCK8   9.9992,2.9993                                                str     [V] high rail, low rail
    PRESECA  [1:7, 2:2065]                                                str     Prescan section for quadrant A
    CCDPREP  purge,clear                                                  str     CCD prep actions
    DAC16    39.9961,39.5934                                              str     [V] set value, measured value
    OFFSET3  0.4000000059604645,-8.9095                                   str     [V] set value, measured value
    DETSECB  [2058:4114, 1:2064]                                          str     Detector section for quadrant B
    BIASSECA [2065:2128, 2:2065]                                          str     Bias section for quadrant A
    PGAGAIN  3                                                            int     Controller gain
    DAC13    0.0,0.0148                                                   str     [V] set value, measured value
    CLOCK6   9.9999,0.0                                                   str     [V] high rail, low rail
    DAC10    -25.0003,-24.3376                                            str     [V] set value, measured value
    DAC7     5.9998,6.028                                                 str     [V] set value, measured value
    CLOCK1   9.9999,0.0                                                   str     [V] high rail, low rail
    CLOCK5   9.9999,0.0                                                   str     [V] high rail, low rail
    CLOCK11  9.9992,2.9993                                                str     [V] high rail, low rail
    ORSECC   [8:2064, 2098:2129]                                          str     Row overscan section for quadrant C
    DAC15    0.0,-0.0148                                                  str     [V] set value, measured value
    DETSECA  [1:2057, 1:2064]                                             str     Detector section for quadrant A
    CDSPARMS 400, 400, 8, 2000                                            str     CDS parameters
    PRRSECC  [8:2064, 4194:4194]                                          str     Row prescan section for quadrant C
    BLDTIME  0.3509                                                       float   [s] Time to build image
    DAC11    -25.0003,-24.3673                                            str     [V] set value, measured value
    OFFSET2  0.4000000059604645,-8.9301                                   str     [V] set value, measured value
    BIASSECB [2129:2192, 2:2065]                                          str     Bias section for quadrant B
    DELAYS   20, 20, 25, 40, 7, 3000, 7, 7, 7, 7                          str     [10] Delay settings
    CLOCK0   9.9999,0.0                                                   str     [V] high rail, low rail
    OFFSET5  2.0,6.028                                                    str     [V] set value, measured value
    CLOCK10  9.9992,2.9993                                                str     [V] high rail, low rail
    DATASECD [2193:4249, 2130:4193]                                       str     Data section for quadrant D
    DAC1     -9.0002,-8.858                                               str     [V] set value, measured value
    DIGITIME 47.5334                                                      float   [s] Time to digitize image
    CAMERA   r0                                                           str     Camera name
    CCDNAME  CCDSM4R                                                      str     CCD name
    DAC6     5.9998,6.0017                                                str     [V] set value, measured value
    CCDSIZE  4194,4256                                                    str     CCD size in pixels (rows, columns)
    CLOCK4   9.9999,0.0                                                   str     [V] high rail, low rail
    CCDSECD  [2058:4114, 2065:4128]                                       str     CCD section for quadrant D
    CCDSECB  [2058:4114, 1:2064]                                          str     CCD section for quadrant B
    DAC8     -25.0003,-24.9164                                            str     [V] set value, measured value
    CLOCK14  9.9992,2.9993                                                str     [V] high rail, low rail
    CLOCK2   9.9999,0.0                                                   str     [V] high rail, low rail
    CCDCFG   default_lbnl_20190717.cfg                                    str     CCD configuration file
    PRESECD  [4250:4256, 2130:4193]                                       str     Prescan section for quadrant D
    DETSECD  [2058:4114, 2065:4128]                                       str     Detector section for quadrant D
    DATASECA [8:2064, 2:2065]                                             str     Data section for quadrant A
    CLOCK13  9.9992,2.9993                                                str     [V] high rail, low rail
    ORSECB   [2193:4249, 2066:2097]                                       str     Row overscan section for quadrant B
    DATASECC [8:2064, 2130:4193]                                          str     Data section for quadrant C
    AMPSECA  [1:2057, 1:2064]                                             str     AMP section for quadrant A
    ORSECD   [2193:4249, 2098:2129]                                       str     Row bias section for quadrant D
    PRRSECA  [8:2064, 1:1]                                                str     Row prescan section for quadrant A
    CCDSECA  [1:2057, 1:2064]                                             str     CCD section for quadrant A
    DAC3     -9.0002,-8.9095                                              str     [V] set value, measured value
    SETTINGS detectors_sm_20191211.json                                   str     Name of DESI CCD settings file
    AMPSECB  [4114:2058, 1:2064]                                          str     AMP section for quadrant B
    CRYOTEMP 163.044                                                      float   [deg K] Cryostat CCD temperature
    DAC17    20.0008,11.9804                                              str     [V] set value, measured value
    CLOCK7   -2.0001,3.9999                                               str     [V] high rail, low rail
    TRIMSECB [2193:4249, 2:2065]                                          str     Trim section for quadrant B
    CCDSECC  [1:2057, 2065:4128]                                          str     CCD section for quadrant C
    PRRSECB  [2193:4249, 1:1]                                             str     Row prescan section for quadrant B
    DATASECB [2193:4249, 2:2065]                                          str     Data section for quadrant B
    PRESECC  [1:7, 2130:4193]                                             str     Prescan section for quadrant C
    DAC5     5.9998,6.028                                                 str     [V] set value, measured value
    DAC14    0.0,-0.0148                                                  str     [V] set value, measured value
    PRESECB  [4250:4256, 2:2065]                                          str     Prescan section for quadrant B
    PRRSECD  [2193:4249, 4194:4194]                                       str     Row prescan section for quadrant D
    AMPSECD  [4114:2058, 4128:2065]                                       str     AMP section for quadrant D
    DAC12    0.0,0.0                                                      str     [V] set value, measured value
    TRIMSECC [8:2064, 2130:4193]                                          str     Trim section for quadrant C
    CLOCK17  9.0,0.9999                                                   str     [V] high rail, low rail
    TRIMSECD [2193:4249, 2130:4193]                                       str     Trim section for quadrant D
    DETSECC  [1:2057, 2065:4128]                                          str     Detector section for quadrant C
    CRYOPRES 9.322e-08                                                    str     [mb] Cryostat pressure (IP)
    OFFSET0  0.4000000059604645,-8.9198                                   str     [V] set value, measured value
    CPUTEMP  56.9941                                                      float   [deg C] CCD controller CPU temperature
    CLOCK16  9.9999,3.0                                                   str     [V] high rail, low rail
    OFFSET4  2.0,6.0174                                                   str     [V] set value, measured value
    CCDTMING default_lbnl_timing_20180905.txt                             str     CCD timing file
    TRIMSECA [8:2064, 2:2065]                                             str     Trim section for quadrant A
    DAC4     5.9998,6.0174                                                str     [V] set value, measured value
    OFFSET7  2.0,6.0332                                                   str     [V] set value, measured value
    CLOCK3   -2.0001,3.9999                                               str     [V] high rail, low rail
    ORSECA   [8:2064, 2066:2097]                                          str     Row overscan section for quadrant A
    OFFSET6  2.0,6.0017                                                   str     [V] set value, measured value
    DETECTOR M1-49                                                        str     Detector (ccd) identification
    DAC0     -9.0002,-8.9198                                              str     [V] set value, measured value
    DAC2     -9.0002,-8.9301                                              str     [V] set value, measured value
    BIASSECD [2129:2192, 2130:4193]                                       str     Bias section for quadrant D
    REQTIME  120.0                                                        float   [s] Requested exposure time
    OBSID    kp4m20201220t222108                                          str     Unique observation identifier
    PROCTYPE RAW                                                          str     Data processing level
    PRODTYPE image                                                        str     Data product type
    CHECKSUM oo3Aon02on08on08                                             str     HDU checksum updated 2022-01-29T01:26:43
    DATASUM  424075550                                                    str     data unit checksum updated 2022-01-29T01:26:43
    GAINA    1.655                                                        float   e/ADU (gain applied to image)
    SATULEVA 65535.0                                                      float   saturation or non lin. level, in ADU, inc. bias
    OSTEPA   0.7301409887440968                                           float   ADUs (max-min of median overscan per row)
    OMETHA   AVERAGE                                                      str     use average overscan
    OVERSCNA 1978.069214285938                                            float   ADUs (gain not applied)
    OBSRDNA  2.798159188935688                                            float   electrons (gain is applied)
    SATUELEA 105186.7204503568                                            float   saturation or non lin. level, in electrons
    GAINB    1.488                                                        float   e/ADU (gain applied to image)
    SATULEVB 65535.0                                                      float   saturation or non lin. level, in ADU, inc. bias
    OSTEPB   0.7607557420124067                                           float   ADUs (max-min of median overscan per row)
    OMETHB   AVERAGE                                                      str     use average overscan
    OVERSCNB 1987.133968648987                                            float   ADUs (gain not applied)
    OBSRDNB  2.557416670656615                                            float   electrons (gain is applied)
    SATUELEB 94559.2246546503                                             float   saturation or non lin. level, in electrons
    GAINC    1.583                                                        float   e/ADU (gain applied to image)
    SATULEVC 65535.0                                                      float   saturation or non lin. level, in ADU, inc. bias
    OSTEPC   0.6293911971442867                                           float   ADUs (max-min of median overscan per row)
    OMETHC   AVERAGE                                                      str     use average overscan
    OVERSCNC 1966.939262512987                                            float   ADUs (gain not applied)
    OBSRDNC  2.703494293725218                                            float   electrons (gain is applied)
    SATUELEC 100628.2401474419                                            float   saturation or non lin. level, in electrons
    GAIND    1.507                                                        float   e/ADU (gain applied to image)
    SATULEVD 65535.0                                                      float   saturation or non lin. level, in ADU, inc. bias
    OSTEPD   0.6596786995360162                                           float   ADUs (max-min of median overscan per row)
    OMETHD   AVERAGE                                                      str     use average overscan
    OVERSCND 1994.41783538263                                             float   ADUs (gain not applied)
    OBSRDND  2.441905057216482                                            float   electrons (gain is applied)
    SATUELED 95755.65732207838                                            float   saturation or non lin. level, in electrons
    FIBERMIN 0                                                            int
    LONGSTRN OGIP 1.0                                                     str     The OGIP Long String Convention may be used.
    MODULE   CI                                                           str     Image Sources/Component
    FRAMES   None                                                         Unknown Number of Frames in Archive
    COSMSPLT F                                                            bool    Cosmics split exposure if true
    MAXSPLIT 0                                                            int     Number of allowed exposure splits
    SPLITIDS 68978                                                        str     List of expids for split exposures
    OBSTYPE  FLAT                                                         str     Spectrograph observation type
    MANIFEST F                                                            bool    DOS exposure manifest
    OBJECT                                                                str     Object name
    SEQID    3 requests                                                   str     Exposure sequence identifier
    SEQNUM   1                                                            int     Number of exposure in sequence
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
    TRUSTEMP 13.2                                                         float   [deg] Average Telescope truss temperature (only
    PMIRTEMP 7.3                                                          float   [deg] Average primary mirror temperature (nit,e
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
    MOONDEC  -9.840963                                                    float   [deg] Moon declination at start of exposure
    MOONRA   350.487504                                                   float   [deg] Moon RA at start of exposure
    MOUNTAZ  73.494042                                                    float   [deg] Mount azimuth angle
    MOUNTDEC 31.962725                                                    float   [deg] Mount declination
    MOUNTEL  41.035784                                                    float   [deg] Mount elevation angle
    MOUNTHA  -58.479517                                                   float   [deg] Mount hour angle
    INCTRL   F                                                            bool    DESI in control
    INPOS    T                                                            bool    Mount in position
    MNTOFFD  -0.0                                                         float   [arcsec] Mount offset (dec)
    MNTOFFR  -0.0                                                         float   [arcsec] Mount offset (RA)
    PARALLAC -73.492831                                                   float   [deg] Parallactic angle
    SKYDEC   31.962725                                                    float   [deg] Telescope declination (pointing on sky)
    SKYRA    12.118172                                                    float   [deg] Telescope right ascension (pointing on sk
    TARGTDEC 31.9633                                                      float   [deg] Target declination (to TCS)
    TARGTRA  6.305085                                                     float   [deg] Target right ascension (to TCS)
    TARGTAZ  75.317651                                                    float   [deg] Target azimuth
    TARGTEL  45.786076                                                    float   [deg] Target elevation
    TRGTOFFD 0.0                                                          float   [arcsec] Telescope target offset (dec)
    TRGTOFFR 0.0                                                          float   [arcsec] Telescope target offset (RA)
    ZD       48.964216                                                    float   [deg] Telescope zenith distance
    TCSST    20:54:33.277                                                 str     Local Sidereal time reported by TCS (HH:MM:SS)
    TCSMJD   59203.93178                                                  float   MJD reported by TCS
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
    TDEWPNT  -18.063                                                      float   Telescope air dew point
    TAIRFLOW 1.121                                                        float   Telescope air flow
    TAIRITMP 10.5                                                         float   [deg] Telescope air in temperature
    TAIROTMP 5.7                                                          float   [deg] Telescope air out temperature
    TAIRTEMP 11.843                                                       float   [deg] Telescope air temperature
    TCASITMP 0.0                                                          float   [deg] Telescope Cass Cage in temperature
    TCASOTMP 9.6                                                          float   [deg] Telescope Cass Cage out temperature
    TCSITEMP 7.4                                                          float   [deg] Telescope center section in temperature
    TCSOTEMP 10.2                                                         float   [deg] Telescope center section out temperature
    TCIBTEMP 0.0                                                          float   [deg] Telescope chimney IB temperature
    TCIMTEMP 0.0                                                          float   [deg] Telescope chimney IM temperature
    TCITTEMP 0.0                                                          float   [deg] Telescope chimney IT temperature
    TCOSTEMP 0.0                                                          float   [deg] Telescope chimney OS temperature
    TCOWTEMP 0.0                                                          float   [deg] Telescope chimney OW temperature
    TDBTEMP  7.3                                                          float   [deg] Telescope dec bore temperature
    TFLOWIN  8.0                                                          float   Telescope flow rate in
    TFLOWOUT 8.3                                                          float   Telescope flow rate out
    TGLYCOLI -1.9                                                         float   [deg] Telescope glycol in temperature
    TGLYCOLO 0.0                                                          float   [deg] Telescope glycol out temperature
    THINGES  12.9                                                         float   [deg] Telescope hinge S temperature
    THINGEW  11.9                                                         float   [deg] Telescope hinge W temperature
    TPMAVERT 7.295                                                        float   [deg] Telescope mirror averagetemperature
    TPMDESIT 7.0                                                          float   [deg] Telescope mirror desired temperature
    TPMEIBT  7.4                                                          float   [deg] Telescope mirror EIB temperature
    TPMEITT  7.3                                                          float   [deg] Telescope mirror EIT temperature
    TPMEOBT  7.4                                                          float   [deg] Telescope mirror EOB temperature
    TPMEOTT  7.1                                                          float   [deg] Telescope mirror EOT temperature
    TPMNIBT  7.5                                                          float   [deg] Telescope mirror NIB temperature
    TPMNITT  7.2                                                          float   [deg] Telescope mirror NIT temperature
    TPMNOBT  7.7                                                          float   [deg] Telescope mirror NOB temperature
    TPMNOTT  7.5                                                          float   [deg] Telescope mirror NOT temperature
    TPMRTDT  7.09                                                         float   [deg] Telescope mirror RTD temperature
    TPMSIBT  7.4                                                          float   [deg] Telescope mirror SIB temperature
    TPMSITT  7.0                                                          float   [deg] Telescope mirror SIT temperature
    TPMSOBT  7.4                                                          float   [deg] Telescope mirror SOB temperature
    TPMSOTT  7.1                                                          float   [deg] Telescope mirror SOT temperature
    TPMSTAT  soft air                                                     str     Telescope mirror status
    TPMWIBT  7.3                                                          float   [deg] Telescope mirror WIB temperature
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
    TTRSTEMP 13.0                                                         float   [deg] Telescope top ring S temperature
    TTRWTEMP 13.4                                                         float   [deg] Telescope top ring W temperature
    TTRUETBT -4.8                                                         float   [deg] Telescope truss ETB temperature
    TTRUETTT 11.6                                                         float   [deg] Telescope truss ETT temperature
    TTRUNTBT 11.0                                                         float   [deg] Telescope truss NTB temperature
    TTRUNTTT 11.8                                                         float   [deg] Telescope truss NTT temperature
    TTRUSTBT 11.2                                                         float   [deg] Telescope truss STB temperature
    TTRUSTST 10.8                                                         float   [deg] Telescope truss STS temperature
    TTRUSTTT 12.4                                                         float   [deg] Telescope truss STT temperature
    TTRUTSBT 13.5                                                         float   [deg] Telescope truss TSB temperature
    TTRUTSMT 13.6                                                         float   [deg] Telescope truss TSM temperature
    TTRUTSTT 12.5                                                         float   [deg] Telescope truss TST temperature
    TTRUWTBT 11.0                                                         float   [deg] Telescope truss WTB temperature
    TTRUWTTT 11.7                                                         float   [deg] Telescope truss WTT temperature
    ALARM    F                                                            bool    UPS major alarm or check battery
    ALARM-ON F                                                            bool    UPS active alarm condition
    BATTERY  100.0                                                        float   [%] UPS Battery left
    SECLEFT  5682.0                                                       float   [s] UPS Seconds left
    UPSSTAT  System Normal - On Line(7)                                   str     UPS Status
    INAMPS   65.7                                                         float   [A] UPS total input current
    OUTWATTS 4700.0,6900.0,4100.0                                         str     [W] UPS Phase A, B, C output watts
    COMPDEW  -12.1                                                        float   [deg C] Computer room dewpoint
    COMPHUM  7.7                                                          float   [%] Computer room humidity
    COMPAMB  19.3                                                         float   [deg C] Computer room ambient temperature
    COMPTEMP 24.9                                                         float   [deg C] Computer room hygrometer temperature
    DEWPOINT 5.7                                                          float   [deg C] (outside) dewpoint
    HUMIDITY 7.0                                                          float   [%] (outside) humidity
    PRESSURE 795.0                                                        float   [torr] (outside) air pressure
    OUTTEMP  0.0                                                          float   [deg C] outside temperature
    WINDDIR  87.0                                                         float   [deg] wind direction
    WINDSPD  19.1                                                         float   [m/s] wind speed
    GUST     14.4                                                         float   [m/s] Wind gusts speed
    AMNIENTN 13.4                                                         float   [deg C] ambient temperature north
    CFLOOR   8.1                                                          float   [deg C] temperature on C floor
    NWALLIN  13.6                                                         float   [deg C] temperature at north wall inside
    NWALLOUT 8.8                                                          float   [deg C] temperature at north wall outside
    WWALLIN  12.8                                                         float   [deg C] temperature at west wall inside
    WWALLOUT 9.4                                                          float   [deg C] temperature at west wall outside
    AMBIENTS 14.6                                                         float   [deg C] ambient temperature south
    FLOOR    12.4                                                         float   [deg C] temperature at floor (LCR)
    EWALLCMP 10.2                                                         float   [deg C] temperature at east wall, computer room
    EWALLCOU 9.5                                                          float   [deg C] temperature at east wall, Coude room
    ROOF     9.9                                                          float   [deg C] temperature on roof
    ROOFAMB  9.9                                                          float   [deg C] ambient temperature on roof
    DOMEBLOW 12.1                                                         float   [deg C] temperature at dome back, lower
    DOMEBUP  12.5                                                         float   [deg C] temperature at dome back, upper
    DOMELLOW 14.4                                                         float   [deg C] temperature at dome left, lower
    DOMELUP  19.4                                                         float   [deg C] temperature at dome left, upper
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
    NSPEC    500                                                          int     Number of spectra
    WAVEMIN  5760.0                                                       float   First wavelength [Angstroms]
    WAVEMAX  7620.0                                                       float   Last wavelength [Angstroms]
    WAVESTEP 0.8                                                          float   Wavelength step size [Angstroms]
    SPECTER  0.10.0                                                       str     https://github.com/desihub/specter
    IN_PSF   SPECPROD/exposures/20201220/00068978/psf-r0-00068978.fits    str     Input sp
    IN_IMG   SPECPROD/preproc/20201220/00068978/preproc-r0-00068978.fits  str
    ORIG_PSF SPECPROD/calibnight/20201220/psfnight-r0-20201220.fits       str
    CHI2PDF  1.088304575350556                                            float
    BUNIT                                                                 str     adimensional quantity to divide to flatfield a frame
    ======== ============================================================ ======= ====================================================

Data: FITS image [float32, 2751x500]

HDU1
----

EXTNAME = IVAR

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2751             int
    NAXIS2   500              int
    BUNIT                     str  inverse variance, adimensional
    CHECKSUM kdmLldmJkdmJkdmJ str  HDU checksum updated 2022-02-01T22:58:01
    DATASUM  4118276244       str  data unit checksum updated 2022-02-01T22:58:01
    ======== ================ ==== ==============================================

Data: FITS image [float32, 2751x500]

HDU2
----

EXTNAME = MASK

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2751             int
    NAXIS2   500              int
    BSCALE   1                int
    BZERO    2147483648       int
    CHECKSUM RHdLRGcIRGcIRGcI str  HDU checksum updated 2022-02-01T22:58:02
    DATASUM  687834           str  data unit checksum updated 2022-02-01T22:58:02
    ======== ================ ==== ==============================================

Data: FITS image [int32, 2751x500]

HDU3
----

EXTNAME = MEANSPEC

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords table

    .. rst-class:: keywords

    ======== ================= ==== ==============================================
    KEY      Example Value     Type Comment
    ======== ================= ==== ==============================================
    NAXIS1   2751              int
    BUNIT    electron/Angstrom str
    CHECKSUM 4TMJ6RKJ4RKJ4RKJ  str  HDU checksum updated 2022-02-01T22:58:02
    DATASUM  2617283155        str  data unit checksum updated 2022-02-01T22:58:02
    ======== ================= ==== ==============================================

Data: FITS image [float32, 2751]

HDU4
----

EXTNAME = WAVELENGTH

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2751             int
    BUNIT    Angstrom         str
    CHECKSUM 5qI85oG75oG75oG7 str  HDU checksum updated 2022-02-01T22:58:02
    DATASUM  2458411755       str  data unit checksum updated 2022-02-01T22:58:02
    ======== ================ ==== ==============================================

Data: FITS image [float32, 2751]

HDU5
----

EXTNAME = FIBERMAP

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   369              int  length of dimension 1
    NAXIS2   500              int  length of dimension 2
    ENCODING ascii            str
    CHECKSUM aBFAbA93aAE9aA99 str  HDU checksum updated 2022-02-01T22:58:02
    DATASUM  3386980400       str  data unit checksum updated 2022-02-01T22:58:02
    ======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

===================== ======= ===== ===========
Name                  Type    Units Description
===================== ======= ===== ===========
TARGETID              int64
PETAL_LOC             int16
DEVICE_LOC            int32
LOCATION              int64
FIBER                 int32
FIBERSTATUS           int32
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
BRICKNAME             char[8]
BRICKID               int64
BRICK_OBJID           int64
MORPHTYPE             char[4]
EBV                   float32
FLUX_G                float32
FLUX_R                float32
FLUX_Z                float32
FLUX_W1               float32
FLUX_W2               float32
FLUX_IVAR_G           float32
FLUX_IVAR_R           float32
FLUX_IVAR_Z           float32
FLUX_IVAR_W1          float32
FLUX_IVAR_W2          float32
FIBERFLUX_G           float32
FIBERFLUX_R           float32
FIBERFLUX_Z           float32
FIBERTOTFLUX_G        float32
FIBERTOTFLUX_R        float32
FIBERTOTFLUX_Z        float32
MASKBITS              int16
SERSIC                float32
SHAPE_R               float32
SHAPE_E1              float32
SHAPE_E2              float32
REF_ID                int64
REF_CAT               char[2]
GAIA_PHOT_G_MEAN_MAG  float32
GAIA_PHOT_BP_MEAN_MAG float32
GAIA_PHOT_RP_MEAN_MAG float32
PARALLAX              float32
PHOTSYS               char[1]
PRIORITY_INIT         int64
NUMOBS_INIT           int64
DESI_TARGET           int64
BGS_TARGET            int64
MWS_TARGET            int64
SCND_TARGET           int64
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
===================== ======= ===== ===========


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
