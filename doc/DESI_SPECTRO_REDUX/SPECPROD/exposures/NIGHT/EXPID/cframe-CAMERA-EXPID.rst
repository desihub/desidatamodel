========================
cframe-CAMERA-EXPID.fits
========================

:Summary: This holds the calibrated spectra for a given camera and exposure.
    See the datamodel for :doc:`frame-CAMERA-EXPID.fits <frame-CAMERA-EXPID>`
    files for details of the format.
:Naming Convention: ``cframe-{CAMERA}-{EXPID}.fits``, where ``{CAMERA}`` is
    one of the spectrograph cameras (*e.g.* ``z1``) and ``{EXPID}``
    is the 8-digit exposure ID.
:Regex: ``cframe-[brz][0-9]-[0-9]{8}\.fits``
:File Type: FITS, 82 MB

Contents
========

====== ========== ======== ======================================
Number EXTNAME    Type     Contents
====== ========== ======== ======================================
HDU0_  FLUX       IMAGE    Flux, erg/s/cm2/A
HDU1_  IVAR       IMAGE    Inverse variance, ``(erg/s/cm2/A)^-2``
HDU2_  MASK       IMAGE    Mask (0 = good)
HDU3_  WAVELENGTH IMAGE    wavelength in Angstrom
HDU4_  RESOLUTION IMAGE    Resolution Matrix
HDU5_  FIBERMAP   BINTABLE Fibermap
HDU6_  CHI2PIX    IMAGE    chi2 fit of PSF model to CCD image
HDU7_  SCORES     BINTABLE Quality Assurance scores
====== ========== ======== ======================================


FITS Header Units
=================

HDU0
----

EXTNAME = FLUX

Calibrated spectral flux in 1e-17 erg / (s cm2 Angstrom).

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ============== ===================================================================== ======= ===============================================
    KEY            Example Value                                                         Type    Comment
    ============== ===================================================================== ======= ===============================================
    NAXIS1         2326                                                                  int
    NAXIS2         500                                                                   int
    EXPID          69022                                                                 int     Exposure number
    EXPFRAME       0                                                                     int     Frame number
    TILEID         80616                                                                 int     DESI Tile ID
    FIBASSGN       /data/tiles/SVN_tiles/080/fiberassign-080616.fits                     str     Fiber assign fil
    FLAVOR         science                                                               str     Observation type
    SEQUENCE       DESI                                                                  str     OCS Sequence name
    PURPOSE        Commissioning                                                         str     Purpose of observing night
    PROGRAM        SV1 BGS+MWS tile 80616                                                str     Program name
    PROPID         2019B-5000                                                            str     Proposal ID
    OBSERVER       DESIObserver                                                          str     Names of observers
    LEAD           RunManager                                                            str     Lead observer
    INSTRUME       DESI                                                                  str     Instrument name
    OBSERVAT       KPNO                                                                  str     Observatory name
    OBS-LAT        31.96403                                                              str     [deg] Observatory latitude
    OBS-LONG       -111.59989                                                            str     [deg] Observatory east longitude
    OBS-ELEV       2097.0                                                                float   [m] Observatory elevation
    TELESCOP       KPNO 4.0-m telescope                                                  str     Telescope name
    CORRCTOR       DESI Corrector                                                        str     Corrector Identification
    NIGHT          20201220                                                              int     Observing night
    TIMESYS        UTC                                                                   str     Time system used for date-obs
    DATE-OBS       2020-12-21T02:36:32.099838                                            str     [UTC] Observation data and start time
    TIME-OBS       02:39:11.845920                                                       str     [UTC] Observation start time
    MJD-OBS        59204.10870486                                                        float   Modified Julian Date of observation
    OPENSHUT       2020-12-21T02:36:32.099838                                            Unknown Time shutter opened
    ST             01:10:39.210                                                          str     Local Sidereal time at observation start (HH:MM
    EXPTIME        300.007                                                               float   [s] Actual exposure time
    REQRA          356.0                                                                 float   [deg] Requested right ascension (observer input
    REQDEC         29.0                                                                  float   [deg] Requested declination (observer input)
    FOCUS          1426.5,-501.4,81.0,-2.6,42.3,169.2                                    str     Telescope focus settings
    VCCD           ON                                                                    str     True (ON) if CCD voltage is on
    VCCDON         2020-12-09T21:23:19.307761                                            str     Time when CCD voltage was turned on
    VCCDSEC        969702.2                                                              float   [s] CCD on time in seconds
    TRUSTEMP       11.767                                                                float   [deg] Average Telescope truss temperature (only
    PMIRTEMP       8.925                                                                 float   [deg] Average primary mirror temperature (nit,e
    EQUINOX        2000.0                                                                float   Epoch of observation
    MOUNTAZ        266.70224                                                             float   [deg] Mount azimuth angle
    MOUNTDEC       28.999221                                                             float   [deg] Mount declination
    MOUNTEL        71.039837                                                             float   [deg] Mount elevation angle
    MOUNTHA        21.769281                                                             float   [deg] Mount hour angle
    SKYDEC         28.999221                                                             float   [deg] Telescope declination (pointing on sky)
    SKYRA          355.996551                                                            float   [deg] Telescope right ascension (pointing on sk
    TARGTDEC       28.999221                                                             float   [deg] Target declination (to TCS)
    TARGTRA        355.996551                                                            float   [deg] Target right ascension (to TCS)
    USEETC         F                                                                     bool    ETC data available if true
    USESKY         T                                                                     bool    DOS Control: use Sky Monitor
    USEFOCUS       T                                                                     bool    DOS Control: use focus
    HEXTRIM        0.0,0.0,0.0,0.0,0.0,0.0                                               str     Hexapod trim values
    USEROTAT       T                                                                     bool    DOS Control: use rotator
    ROTOFFST       167.1                                                                 float   [arcsec] Rotator offset
    ROTENBLD       T                                                                     bool    Rotator enabled
    ROTRATE        0.0                                                                   float   [arcsec/min] Rotator rate
    USEGUIDR       T                                                                     bool    DOS Control: use guider
    USEDONUT       T                                                                     bool    DOS Control: use donuts
    SPECGRPH       8                                                                     int     Spectrograph logical name (SP)
    SPECID         2                                                                     int     Spectrograph serial number (SM)
    FEEBOX         lbnl050                                                               str     CCD Controller serial number
    VESSEL         8                                                                     int     Cryostat serial number
    FEEVER         v20160312                                                             str     CCD Controller version
    FEEPOWER       ON                                                                    str     FEE power status
    FEEDMASK       2134851391                                                            int     FEE dac mask
    FEECMASK       1048575                                                               int     FEE clk mask
    CCDTEMP        -135.3315                                                             float   [deg C] CCD controller CCD temperature
    RADESYS        FK5                                                                   str     Coordinate reference frame of major/minor axes
    FILENAME       /exposures/desi/specs/20201220/00069022/sp1-00069022.fits.fz          str     Name
    DOSVER         trunk                                                                 str     DOS software version
    OCSVER         1.2                                                                   float   OCS software version
    CONSTVER       DESI:CURRENT                                                          str     Constants version
    INIFILE        /data/msdos/dos_home/architectures/kpno/desi.ini                      str     DOS Configuration
    AMPSECB        [4114:2058, 1:2064]                                                   str     AMP section for quadrant B
    DAC16          39.9961,39.3162                                                       str     [V] set value, measured value
    CLOCK8         9.9992,2.9993                                                         str     [V] high rail, low rail
    PRRSECD        [2193:4249, 4194:4194]                                                str     Row prescan section for quadrant D
    CCDPREP        purge,clear                                                           str     CCD prep actions
    CLOCK10        9.9992,2.9993                                                         str     [V] high rail, low rail
    DAC17          20.0008,12.2732                                                       str     [V] set value, measured value
    ORSECB         [2193:4249, 2066:2097]                                                str     Row overscan section for quadrant B
    DAC15          0.0,0.0148                                                            str     [V] set value, measured value
    ORSECD         [2193:4249, 2098:2129]                                                str     Row bias section for quadrant D
    DIGITIME       47.5899                                                               float   [s] Time to digitize image
    BIASSECA       [2065:2128, 2:2065]                                                   str     Bias section for quadrant A
    CLOCK9         9.9992,2.9993                                                         str     [V] high rail, low rail
    CLOCK18        9.0,0.9999                                                            str     [V] high rail, low rail
    CAMERA         r8                                                                    str     Camera name
    CLOCK17        9.0,0.9999                                                            str     [V] high rail, low rail
    CLOCK5         9.9999,0.0                                                            str     [V] high rail, low rail
    TRIMSECD       [2193:4249, 2130:4193]                                                str     Trim section for quadrant D
    DETSECD        [2058:4114, 2065:4128]                                                str     Detector section for quadrant D
    DAC0           -9.0002,-8.9507                                                       str     [V] set value, measured value
    CLOCK15        9.9992,2.9993                                                         str     [V] high rail, low rail
    TRIMSECA       [8:2064, 2:2065]                                                      str     Trim section for quadrant A
    BIASSECB       [2129:2192, 2:2065]                                                   str     Bias section for quadrant B
    CLOCK11        9.9992,2.9993                                                         str     [V] high rail, low rail
    CLOCK12        9.9992,2.9993                                                         str     [V] high rail, low rail
    AMPSECD        [4114:2058, 4128:2065]                                                str     AMP section for quadrant D
    CLOCK4         9.9999,0.0                                                            str     [V] high rail, low rail
    PRRSECB        [2193:4249, 1:1]                                                      str     Row prescan section for quadrant B
    CCDSECD        [2058:4114, 2065:4128]                                                str     CCD section for quadrant D
    CCDTMING       default_lbnl_timing_20180905.txt                                      str     CCD timing file
    TRIMSECB       [2193:4249, 2:2065]                                                   str     Trim section for quadrant B
    CCDSIZE        4194,4256                                                             str     CCD size in pixels (rows, columns)
    PGAGAIN        3                                                                     int     Controller gain
    PRESECD        [4250:4256, 2130:4193]                                                str     Prescan section for quadrant D
    CLOCK6         9.9999,0.0                                                            str     [V] high rail, low rail
    CLOCK13        9.9992,2.9993                                                         str     [V] high rail, low rail
    DAC7           5.9998,6.028                                                          str     [V] set value, measured value
    DATASECA       [8:2064, 2:2065]                                                      str     Data section for quadrant A
    CRYOTEMP [1]_  162.97                                                                float   [deg K] Cryostat CCD temperature
    OFFSET2        0.4000000059604645,-8.9198                                            str     [V] set value, measured value
    OFFSET6        2.0,6.0437                                                            str     [V] set value, measured value
    DELAYS         20, 20, 25, 40, 7, 3000, 7, 7, 7, 7                                   str     [10] Delay settings
    BIASSECD       [2129:2192, 2130:4193]                                                str     Bias section for quadrant D
    PRRSECA        [8:2064, 1:1]                                                         str     Row prescan section for quadrant A
    TRIMSECC       [8:2064, 2130:4193]                                                   str     Trim section for quadrant C
    CLOCK3         -2.0001,3.9999                                                        str     [V] high rail, low rail
    CCDNAME        CCDSM2R                                                               str     CCD name
    DAC9           -25.0003,-24.768                                                      str     [V] set value, measured value
    CCDSECC        [1:2057, 2065:4128]                                                   str     CCD section for quadrant C
    ORSECA         [8:2064, 2066:2097]                                                   str     Row overscan section for quadrant A
    DAC5           5.9998,6.0543                                                         str     [V] set value, measured value
    CCDSECB        [2058:4114, 1:2064]                                                   str     CCD section for quadrant B
    DETSECB        [2058:4114, 1:2064]                                                   str     Detector section for quadrant B
    OFFSET0        0.4000000059604645,-8.9507                                            str     [V] set value, measured value
    SETTINGS       detectors_sm_20191211.json                                            str     Name of DESI CCD settings file
    DAC11          -25.0003,-24.8422                                                     str     [V] set value, measured value
    BIASSECC       [2065:2128, 2130:4193]                                                str     Bias section for quadrant C
    CASETEMP       59.8142                                                               float   [deg C] CCD controller case temperature
    DAC10          -25.0003,-24.7086                                                     str     [V] set value, measured value
    DAC1           -9.0002,-8.9198                                                       str     [V] set value, measured value
    DAC14          0.0,0.0594                                                            str     [V] set value, measured value
    DETECTOR       M1-46                                                                 str     Detector (ccd) identification
    CDSPARMS       400, 400, 8, 2000                                                     str     CDS parameters
    OFFSET3        0.4000000059604645,-8.9095                                            str     [V] set value, measured value
    DATASECB       [2193:4249, 2:2065]                                                   str     Data section for quadrant B
    ORSECC         [8:2064, 2098:2129]                                                   str     Row overscan section for quadrant C
    CRYOPRES [1]_  8.897e-08                                                             str     [mb] Cryostat pressure (IP)
    AMPSECA        [1:2057, 1:2064]                                                      str     AMP section for quadrant A
    OFFSET7        2.0,6.028                                                             str     [V] set value, measured value
    DAC4           5.9998,6.028                                                          str     [V] set value, measured value
    DATASECC       [8:2064, 2130:4193]                                                   str     Data section for quadrant C
    PRESECC        [1:7, 2130:4193]                                                      str     Prescan section for quadrant C
    CLOCK16        9.9999,3.0                                                            str     [V] high rail, low rail
    CLOCK1         9.9999,0.0                                                            str     [V] high rail, low rail
    PRESECB        [4250:4256, 2:2065]                                                   str     Prescan section for quadrant B
    DAC12          0.0,0.0297                                                            str     [V] set value, measured value
    DAC8           -25.0003,-24.9312                                                     str     [V] set value, measured value
    OFFSET4        2.0,6.0332                                                            str     [V] set value, measured value
    DAC2           -9.0002,-8.9198                                                       str     [V] set value, measured value
    CCDCFG         default_lbnl_20190717.cfg                                             str     CCD configuration file
    BLDTIME        0.3547                                                                float   [s] Time to build image
    PRESECA        [1:7, 2:2065]                                                         str     Prescan section for quadrant A
    DATASECD       [2193:4249, 2130:4193]                                                str     Data section for quadrant D
    DETSECC        [1:2057, 2065:4128]                                                   str     Detector section for quadrant C
    PRRSECC        [8:2064, 4194:4194]                                                   str     Row prescan section for quadrant C
    DAC6           5.9998,6.0437                                                         str     [V] set value, measured value
    DETSECA        [1:2057, 1:2064]                                                      str     Detector section for quadrant A
    CLOCK2         9.9999,0.0                                                            str     [V] high rail, low rail
    DAC3           -9.0002,-8.9095                                                       str     [V] set value, measured value
    OFFSET1        0.4000000059604645,-8.9198                                            str     [V] set value, measured value
    AMPSECC        [1:2057, 4128:2065]                                                   str     AMP section for quadrant C
    CLOCK7         -2.0001,3.9999                                                        str     [V] high rail, low rail
    DAC13          0.0,0.0148                                                            str     [V] set value, measured value
    CCDSECA        [1:2057, 1:2064]                                                      str     CCD section for quadrant A
    OFFSET5        2.0,6.049                                                             str     [V] set value, measured value
    CLOCK14        9.9992,2.9993                                                         str     [V] high rail, low rail
    CLOCK0         9.9999,0.0                                                            str     [V] high rail, low rail
    CPUTEMP        60.8086                                                               float   [deg C] CCD controller CPU temperature
    REQTIME        300.0                                                                 float   [s] Requested exposure time
    OBSID          kp4m20201221t023911                                                   str     Unique observation identifier
    PROCTYPE       RAW                                                                   str     Data processing level
    PRODTYPE       image                                                                 str     Data product type
    CHECKSUM       OUDTPU9ROUCROU9R                                                      str     HDU checksum updated 2022-02-14T08:25:01
    DATASUM        737508938                                                             str     data unit checksum updated 2022-02-14T08:25:01
    GAINA          1.627                                                                 float   e/ADU (gain applied to image)
    SATULEVA       65535.0                                                               float   saturation or non lin. level, in ADU, inc. bias
    OSTEPA         0.5704803307307884                                                    float   ADUs (max-min of median overscan per row)
    OMETHA         AVERAGE                                                               str     use average overscan
    OVERSCNA       1984.679589024373                                                     float   ADUs (gain not applied)
    OBSRDNA        2.48375231913931                                                      float   electrons (gain is applied)
    SATUELEA       103396.3713086573                                                     float   saturation or non lin. level, in electrons
    GAINB          1.482                                                                 float   e/ADU (gain applied to image)
    SATULEVB       65535.0                                                               float   saturation or non lin. level, in ADU, inc. bias
    OSTEPB         0.5242006066837348                                                    float   ADUs (max-min of median overscan per row)
    OMETHB         AVERAGE                                                               str     use average overscan
    OVERSCNB       1980.885980481041                                                     float   ADUs (gain not applied)
    OBSRDNB        2.179252294581384                                                     float   electrons (gain is applied)
    SATUELEB       94187.1969769271                                                      float   saturation or non lin. level, in electrons
    GAINC          1.581                                                                 float   e/ADU (gain applied to image)
    SATULEVC       65535.0                                                               float   saturation or non lin. level, in ADU, inc. bias
    OSTEPC         0.6303264842863427                                                    float   ADUs (max-min of median overscan per row)
    OMETHC         AVERAGE                                                               str     use average overscan
    OVERSCNC       1966.11973127108                                                      float   ADUs (gain not applied)
    OBSRDNC        2.455388696359903                                                     float   electrons (gain is applied)
    SATUELEC       100502.3997048604                                                     float   saturation or non lin. level, in electrons
    GAIND          1.589                                                                 float   e/ADU (gain applied to image)
    SATULEVD       65535.0                                                               float   saturation or non lin. level, in ADU, inc. bias
    OSTEPD         0.6243009115278255                                                    float   ADUs (max-min of median overscan per row)
    OMETHD         AVERAGE                                                               str     use average overscan
    OVERSCND       1987.970298453192                                                     float   ADUs (gain not applied)
    OBSRDND        2.518301447806098                                                     float   electrons (gain is applied)
    SATUELED       100976.2301957579                                                     float   saturation or non lin. level, in electrons
    FIBERMIN       4000                                                                  int
    LONGSTRN       OGIP 1.0                                                              str     The OGIP Long String Convention may be used.
    MODULE         CI                                                                    str     Image Sources/Component
    COSMSPLT       F                                                                     bool    Cosmics split exposure if true
    MAXSPLIT       0                                                                     int     Number of allowed exposure splits
    SPLITIDS [1]_  69022                                                                 str     List of expids for split exposures
    OBSTYPE        SCIENCE                                                               str     Spectrograph observation type
    MANIFEST       F                                                                     bool    DOS exposure manifest
    OBJECT                                                                               str     Object name
    SEQNUM         1                                                                     int     Number of exposure in sequence
    CAMSHUT        open                                                                  str     Shutter status during observation
    ACQTIME        15.0                                                                  int     [s] acqusition image exposure time
    GUIDTIME       5.0                                                                   float   [s] guider GFA exposure time
    FOCSTIME [1]_  60.0                                                                  float   [s] focus GFA exposure time
    SKYTIME [1]_   60.0                                                                  float   [s] sky camera exposure time (acquisition)
    WHITESPT       F                                                                     bool    Telescope is at whitespot
    ZENITH         F                                                                     bool    Telescope is at zenith
    SEANNEX        F                                                                     bool    Telescope is at SE annex
    BEYONDP        F                                                                     bool    Telescope is beyond pole
    FIDUCIAL       off                                                                   str     Fiducials status during observation
    BACKLIT        off                                                                   str     Fibers are backlit if True
    AIRMASS        1.060311                                                              float   Airmass
    PMREADY        T                                                                     bool    Primary mirror ready
    PMCOVER        open                                                                  str     Primary mirror cover
    PMCOOL         off                                                                   str     Primary mirror cooling
    DOMSHUTU       open                                                                  str     Upper dome shutter
    DOMSHUTL       open                                                                  str     Lower dome shutter
    DOMLIGHH       off                                                                   str     High dome lights
    DOMLIGHL       off                                                                   str     Low dome lights
    DOMEAZ         255.166                                                               float   [deg] Dome azimuth angle
    DOMINPOS       T                                                                     bool    Dome is in position
    GUIDOFFR       -0.052283                                                             float   [arcsec] Cummulative guider offset (RA)
    GUIDOFFD       0.136634                                                              float   [arcsec] Cummulative guider offset (dec)
    MOONDEC        -8.975162                                                             float   [deg] Moon declination at start of exposure
    MOONRA         352.538429                                                            float   [deg] Moon RA at start of exposure
    INCTRL         T                                                                     bool    DESI in control
    INPOS          T                                                                     bool    Mount in position
    MNTOFFD        -15.76                                                                float   [arcsec] Mount offset (dec)
    MNTOFFR        29.32                                                                 float   [arcsec] Mount offset (RA)
    PARALLAC       75.635085                                                             float   [deg] Parallactic angle
    TARGTAZ        267.074049                                                            float   [deg] Target azimuth
    TARGTEL        70.563787                                                             float   [deg] Target elevation
    TRGTOFFD       0.0                                                                   float   [arcsec] Telescope target offset (dec)
    TRGTOFFR       0.0                                                                   float   [arcsec] Telescope target offset (RA)
    ZD             19.436213                                                             float   [deg] Telescope zenith distance
    TILERA         356.0                                                                 float   RA of tile given in fiberassign file
    TILEDEC        29.0                                                                  float   DEC of tile given in fiberassign file
    TCSST          01:13:18.668                                                          str     Local Sidereal time reported by TCS (HH:MM:SS)
    TCSMJD         59204.110981                                                          float   MJD reported by TCS
    ACQCAM         GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                             str     Acquisition cameras used
    GUIDECAM       GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                             str     Guide cameras used for t
    FOCUSCAM [1]_  FOCUS1,FOCUS4,FOCUS6,FOCUS9                                           str     Focus cameras used for this exposure
    SKYCAM [1]_    SKYCAM0,SKYCAM1                                                       str     Sky cameras used for this exposure
    REQADC         65.78,85.28                                                           str     [deg] requested ADC angles
    ADCCORR        T                                                                     bool    Correct pointing for ADC setting if True
    ADC1PHI        65.780005                                                             float   [deg] ADC 1 angle
    ADC2PHI        85.279991                                                             float   [deg] ADC 2 angle
    ADC1HOME       F                                                                     bool    ADC 1 at home position if True
    ADC2HOME       F                                                                     bool    ADC 2 at home position if True
    ADC1NREV       -1.0                                                                  float   ADC 1 number of revs
    ADC2NREV       0.0                                                                   float   ADC 2 number of revs
    ADC1STAT       STOPPED                                                               str     ADC 1 status
    ADC2STAT       STOPPED                                                               str     ADC 2 status
    HEXPOS         1426.5,-501.3,81.0,-2.6,42.3,171.9                                    str     Hexapod position
    RESETROT       F                                                                     bool    DOS Control: reset hex rotator
    USEPOS         T                                                                     bool    Fiber positioner data available if true
    PETALS         PETAL0,PETAL1,PETAL2,PETAL3,PETAL4,PETAL5,PETAL6,PETAL7,PETAL8,PETAL9 str     Participating petals
    POSCYCLE       1                                                                     int     Number of current iteration
    POSONTGT       3626                                                                  int     Number of positioners on target
    POSONFRC       0.8613                                                                float   Fraction of positioners on target
    POSDISAB       37                                                                    int     Number of disabled positioners
    POSENABL       4210                                                                  int     Number of enabled positioners
    POSRMS         0.0171                                                                float   [micron] RMS of positioner accuracy
    POSITER        1                                                                     int     Positioning Control: max. number of pos. cycles
    POSFRACT       0.95                                                                  float
    POSTOLER       0.01                                                                  float   Positioning Control: in_position tolerance (mm)
    POSMVALL       T                                                                     bool    Positioning Control: move all positioners
    GUIDMODE       catalog                                                               str     Guider mode
    USEAOS [1]_    F                                                                     bool    DOS Control: AOS data available if true
    USESPCTR       T                                                                     bool    DOS Control: use spectrographs
    SPCGRPHS       SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                               str     Participating spectrograph
    ILLSPECS [1]_  SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                               str     Participating illuminate s
    CCDSPECS [1]_  SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                               str     Participating ccd spectrog
    TDEWPNT        -16.043                                                               float   Telescope air dew point
    TAIRFLOW       0.0                                                                   float   Telescope air flow
    TAIRITMP       11.8                                                                  float   [deg] Telescope air in temperature
    TAIROTMP       11.7                                                                  float   [deg] Telescope air out temperature
    TAIRTEMP       10.65                                                                 float   [deg] Telescope air temperature
    TCASITMP       0.0                                                                   float   [deg] Telescope Cass Cage in temperature
    TCASOTMP       10.8                                                                  float   [deg] Telescope Cass Cage out temperature
    TCSITEMP       9.3                                                                   float   [deg] Telescope center section in temperature
    TCSOTEMP       10.8                                                                  float   [deg] Telescope center section out temperature
    TCIBTEMP       0.0                                                                   float   [deg] Telescope chimney IB temperature
    TCIMTEMP       0.0                                                                   float   [deg] Telescope chimney IM temperature
    TCITTEMP       0.0                                                                   float   [deg] Telescope chimney IT temperature
    TCOSTEMP       0.0                                                                   float   [deg] Telescope chimney OS temperature
    TCOWTEMP       0.0                                                                   float   [deg] Telescope chimney OW temperature
    TDBTEMP        9.3                                                                   float   [deg] Telescope dec bore temperature
    TFLOWIN        0.0                                                                   float   Telescope flow rate in
    TFLOWOUT       0.0                                                                   float   Telescope flow rate out
    TGLYCOLI       9.9                                                                   float   [deg] Telescope glycol in temperature
    TGLYCOLO       9.8                                                                   float   [deg] Telescope glycol out temperature
    THINGES        11.4                                                                  float   [deg] Telescope hinge S temperature
    THINGEW        11.2                                                                  float   [deg] Telescope hinge W temperature
    TPMAVERT       8.931                                                                 float   [deg] Telescope mirror averagetemperature
    TPMDESIT       7.0                                                                   float   [deg] Telescope mirror desired temperature
    TPMEIBT        8.6                                                                   float   [deg] Telescope mirror EIB temperature
    TPMEITT        8.6                                                                   float   [deg] Telescope mirror EIT temperature
    TPMEOBT        8.5                                                                   float   [deg] Telescope mirror EOB temperature
    TPMEOTT        9.0                                                                   float   [deg] Telescope mirror EOT temperature
    TPMNIBT        8.4                                                                   float   [deg] Telescope mirror NIB temperature
    TPMNITT        8.9                                                                   float   [deg] Telescope mirror NIT temperature
    TPMNOBT        8.8                                                                   float   [deg] Telescope mirror NOB temperature
    TPMNOTT        9.1                                                                   float   [deg] Telescope mirror NOT temperature
    TPMRTDT        9.0                                                                   float   [deg] Telescope mirror RTD temperature
    TPMSIBT        8.6                                                                   float   [deg] Telescope mirror SIB temperature
    TPMSITT        8.8                                                                   float   [deg] Telescope mirror SIT temperature
    TPMSOBT        8.2                                                                   float   [deg] Telescope mirror SOB temperature
    TPMSOTT        8.9                                                                   float   [deg] Telescope mirror SOT temperature
    TPMSTAT        ready                                                                 str     Telescope mirror status
    TPMWIBT        8.2                                                                   float   [deg] Telescope mirror WIB temperature
    TPMWITT        9.1                                                                   float   [deg] Telescope mirror WIT temperature
    TPMWOBT        8.3                                                                   float   [deg] Telescope mirror WOB temperature
    TPMWOTT        8.9                                                                   float   [deg] Telescope mirror WOT temperature
    TPCITEMP       8.5                                                                   float   [deg] Telescope primary cell in temperature
    TPCOTEMP       8.6                                                                   float   [deg] Telescope primary cell out temperature
    TPR1HUM        0.0                                                                   float   Telescope probe 1 humidity
    TPR1TEMP       0.0                                                                   float   [deg] Telescope probe1 temperature
    TPR2HUM        0.0                                                                   float   Telescope probe 2 humidity
    TPR2TEMP       0.0                                                                   float   [deg] Telescope probe2 temperature
    TSERVO         40.0                                                                  float   Telescope servo setpoint
    TTRSTEMP       11.4                                                                  float   [deg] Telescope top ring S temperature
    TTRWTEMP       11.0                                                                  float   [deg] Telescope top ring W temperature
    TTRUETBT       -4.2                                                                  float   [deg] Telescope truss ETB temperature
    TTRUETTT       11.2                                                                  float   [deg] Telescope truss ETT temperature
    TTRUNTBT       10.9                                                                  float   [deg] Telescope truss NTB temperature
    TTRUNTTT       11.2                                                                  float   [deg] Telescope truss NTT temperature
    TTRUSTBT       10.7                                                                  float   [deg] Telescope truss STB temperature
    TTRUSTST       10.8                                                                  float   [deg] Telescope truss STS temperature
    TTRUSTTT       11.1                                                                  float   [deg] Telescope truss STT temperature
    TTRUTSBT       11.8                                                                  float   [deg] Telescope truss TSB temperature
    TTRUTSMT       11.8                                                                  float   [deg] Telescope truss TSM temperature
    TTRUTSTT       11.8                                                                  float   [deg] Telescope truss TST temperature
    TTRUWTBT       10.5                                                                  float   [deg] Telescope truss WTB temperature
    TTRUWTTT       10.9                                                                  float   [deg] Telescope truss WTT temperature
    ALARM          F                                                                     bool    UPS major alarm or check battery
    ALARM-ON       F                                                                     bool    UPS active alarm condition
    BATTERY        100.0                                                                 float   [%] UPS Battery left
    SECLEFT        5178.0                                                                float   [s] UPS Seconds left
    UPSSTAT        System Normal - On Line(7)                                            str     UPS Status
    INAMPS         70.4                                                                  float   [A] UPS total input current
    OUTWATTS       5000.0,7200.0,4800.0                                                  str     [W] UPS Phase A, B, C output watts
    COMPDEW        -12.9                                                                 float   [deg C] Computer room dewpoint
    COMPHUM        7.4                                                                   float   [%] Computer room humidity
    COMPAMB        19.5                                                                  float   [deg C] Computer room ambient temperature
    COMPTEMP       24.5                                                                  float   [deg C] Computer room hygrometer temperature
    DEWPOINT       11.5                                                                  float   [deg C] (outside) dewpoint
    HUMIDITY       10.0                                                                  float   [%] (outside) humidity
    PRESSURE       795.0                                                                 float   [torr] (outside) air pressure
    OUTTEMP        0.0                                                                   float   [deg C] outside temperature
    WINDDIR        55.0                                                                  float   [deg] wind direction
    WINDSPD        27.3                                                                  float   [m/s] wind speed
    GUST           20.6                                                                  float   [m/s] Wind gusts speed
    AMNIENTN       13.5                                                                  float   [deg C] ambient temperature north
    CFLOOR         8.9                                                                   float   [deg C] temperature on C floor
    NWALLIN        13.9                                                                  float   [deg C] temperature at north wall inside
    NWALLOUT       9.6                                                                   float   [deg C] temperature at north wall outside
    WWALLIN        12.9                                                                  float   [deg C] temperature at west wall inside
    WWALLOUT       10.6                                                                  float   [deg C] temperature at west wall outside
    AMBIENTS       14.8                                                                  float   [deg C] ambient temperature south
    FLOOR          12.6                                                                  float   [deg C] temperature at floor (LCR)
    EWALLCMP       10.8                                                                  float   [deg C] temperature at east wall, computer room
    EWALLCOU       10.6                                                                  float   [deg C] temperature at east wall, Coude room
    ROOF           10.3                                                                  float   [deg C] temperature on roof
    ROOFAMB        10.6                                                                  float   [deg C] ambient temperature on roof
    DOMEBLOW       10.4                                                                  float   [deg C] temperature at dome back, lower
    DOMEBUP        10.7                                                                  float   [deg C] temperature at dome back, upper
    DOMELLOW       10.8                                                                  float   [deg C] temperature at dome left, lower
    DOMELUP        10.8                                                                  float   [deg C] temperature at dome left, upper
    DOMERLOW       10.6                                                                  float   [deg C] temperature at dome right, lower
    DOMERUP        10.5                                                                  float   [deg C] temperature at dome right, upper
    PLATFORM       10.4                                                                  float   [deg C] temperature at platform
    SHACKC         14.4                                                                  float   [deg C] temperature at shack ceiling
    SHACKW         13.7                                                                  float   [deg C] temperature at shack wall
    STAIRSL        10.5                                                                  float   [deg C] temperature at stairs, lower
    STAIRSM        10.4                                                                  float   [deg C] temperature at stairs, mid
    STAIRSU        10.6                                                                  float   [deg C] temperature at stairs, upper
    TELBASE        9.6                                                                   float   [deg C] temperature at telescope base
    UTILWALL       11.1                                                                  float   [deg C] temperature at utility room wall
    UTILROOM       10.9                                                                  float   [deg C] temperature in utilitiy room
    TNFSPROC [1]_  8.1963                                                                float   [s] PlateMaker NFSPROC processing time
    TGFAPROC [1]_  7.9212                                                                float   [s] PlateMaker GFAPROC processing time
    SIMGFAP        F                                                                     bool    DOS Control: simulate GFAPROC
    USEFVC         T                                                                     bool    DOS Control: use fvc
    USEFID         T                                                                     bool    DOS Control: use fiducials
    USEILLUM       T                                                                     bool    DOS Control: use illuminator
    USEXSRVR       T                                                                     bool    DOS Control: use exposure server
    USEOPENL       T                                                                     bool    DOS Control: use open loop move
    STOPGUDR       T                                                                     bool    DOS Control: stop guider
    STOPFOCS       T                                                                     bool    DOS Control: stop focus
    STOPSKY        T                                                                     bool    DOS Control: stop sky monitor
    KEEPGUDR       F                                                                     bool    DOS Control: keep guider running
    KEEPFOCS       F                                                                     bool    DOS Control: keep focus running
    KEEPSKY        F                                                                     bool    DOS Control: keep sky mon. running
    REACQUIR       F                                                                     bool    DOS Control: reacquire same files
    EXCLUDED                                                                             str     Components excluded from this exposure
    FVCTIME [1]_   2.0                                                                   float   [s] FVC exposure time
    SIMGFACQ       F                                                                     bool
    POSCNVGD [1]_  F                                                                     bool    Number of positioners converged
    GUIEXPID       69022                                                                 int     Guider exposure id at start of spectro exp.
    IGFRMNUM       12                                                                    int     Guider frame number at start of spectro exp.
    FOCEXPID       69022                                                                 int     Focus exposure id at start of spectro exp.
    IFFRMNUM       1                                                                     int     Focus frame number at start of spectro exp.
    SKYEXPID       69022                                                                 int     Sky exposure id at start of spectro exp.
    ISFRMNUM       1                                                                     int     Sky frame number at start of spectro exp.
    FGFRMNUM       46                                                                    int     Guider frame number at end of spectro exp.
    FFFRMNUM       6                                                                     int     Focus frame number at end of spectro exp.
    FSFRMNUM       5                                                                     int     Sky frame number at end of spectro exp.
    HELIOCOR       0.9999115198216216                                                    float
    NSPEC          500                                                                   int     Number of spectra
    WAVEMIN        5760.0                                                                float   First wavelength [Angstroms]
    WAVEMAX        7620.0                                                                float   Last wavelength [Angstroms]
    WAVESTEP       0.8                                                                   float   Wavelength step size [Angstroms]
    SPECTER        0.10.0                                                                str     https://github.com/desihub/specter
    IN_PSF         SPECPROD/exposures/20201220/00069022/psf-r8-00069022.fits             str     Input sp
    IN_IMG         SPECPROD/preproc/20201220/00069022/preproc-r8-00069022.fits           str
    ORIG_PSF       SPECPROD/calibnight/20201220/psfnight-r8-20201220.fits                str
    BUNIT          10**-17 erg/(s cm2 Angstrom)                                          str
    TSNRALPH       1.469972702034016                                                     float
    IN_FRAME       SPECPROD/exposures/20201220/00069022/frame-r8-00069022.fits           str
    FIBERFLT       SPECPROD/exposures/20201220/00069022/fiberflatexp-r8-00069022.fits    str
    IN_SKY         SPECPROD/exposures/20201220/00069022/sky-r8-00069022.fits             str
    IN_CALIB       SPECPROD/exposures/20201220/00069022/fluxcalib-r8-00069022.fits       str
    BBKGMINC [1]_  -0.3364347403909462                                                   float
    BBKGMAXB [1]_  0.8957266211094218                                                    float
    BBKGMINB [1]_  -0.04275468459496062                                                  float
    BBKGMIND [1]_  -0.6146250452424397                                                   float
    BBKGMAXA [1]_  0.6126625684320178                                                    float
    BBKGMAXC [1]_  0.4926723425188555                                                    float
    BBKGMINA [1]_  -0.4336472364870191                                                   float
    BBKGMAXD [1]_  0.8117108701207832                                                    float
    SP2REDP [1]_   6.448e-08                                                             float   [mb] SP2 red pressure
    SP8BLUP [1]_   8.153e-08                                                             float   [mb] SP8 blue pressure
    SP9NIRT [1]_   139.96                                                                float   [K] SP9 NIR temperature
    SP4REDP [1]_   5.168e-08                                                             float   [mb] SP4 red pressure
    TCSKDEC [1]_   0.3 0.003 0.00003                                                     str     TCS Kalman (dec)
    TCSPIRA [1]_   1.0,0.0,0.0,0.0                                                       str     TCS PI settings (P, I (gain, error window, satu
    SP4BLUT [1]_   163.02                                                                float   [K] SP4 blue temperature
    TCSMFDEC [1]_  1                                                                     int     TCS moving filter length (dec)
    SP4REDT [1]_   140.03                                                                float   [K] SP4 red temperature
    SP9REDP [1]_   8.485e-08                                                             float   [mb] SP9 red pressure
    SP9NIRP [1]_   5.579e-08                                                             float   [mb] SP9 NIR pressure
    SP5REDP [1]_   4.908e-08                                                             float   [mb] SP5 red pressure
    SP1REDT [1]_   139.96                                                                float   [K] SP1 red temperature
    SUNRA [1]_     21.738482                                                             float   [deg] Sun RA at start of exposure
    SP3BLUT [1]_   163.02                                                                float   [K] SP3 blue temperature
    SP8NIRP [1]_   4.831e-08                                                             float   [mb] SP8 NIR pressure
    SP9BLUP [1]_   1.208e-07                                                             float   [mb] SP9 blue pressure
    SKYLEVEL [1]_  1.133                                                                 float   counts?] ETC sky level
    TCSKRA [1]_    0.3 0.003 0.00003                                                     str     TCS Kalman (RA)
    SP4BLUP [1]_   6.109e-08                                                             float   [mb] SP4 blue pressure
    SP2NIRT [1]_   139.96                                                                float   [K] SP2 NIR temperature
    SP7BLUP [1]_   9.938e-08                                                             float   [mb] SP7 blue pressure
    SP0NIRP [1]_   5.934e-08                                                             float   [mb] SP0 NIR pressure
    FRAMES [1]_    47                                                                    int     Number of Frames in Archive
    SP4NIRP [1]_   7.072e-08                                                             float   [mb] SP4 NIR pressure
    SP1BLUT [1]_   162.97                                                                float   [K] SP1 blue temperature
    SP6NIRP [1]_   2.873e-07                                                             float   [mb] SP6 NIR pressure
    SP2REDT [1]_   139.99                                                                float   [K] SP2 red temperature
    SP6REDT [1]_   139.96                                                                float   [K] SP6 red temperature
    TCSPIDEC [1]_  1.0,0.0,0.0,0.0                                                       str     TCS PI settings (P, I (gain, error window, satu
    MOONSEP [1]_   147.894                                                               float   [deg] Moon Separation
    TOTTEFF [1]_   1403.0837                                                             float   [s] Total effective exposure time for visit
    SP6NIRT [1]_   139.96                                                                float   [K] SP6 NIR temperature
    SP5NIRT [1]_   139.99                                                                float   [K] SP5 NIR temperature
    SPLITEXP [1]_  T                                                                     bool    Split exposure part of a visit
    SP4NIRT [1]_   139.96                                                                float   [K] SP4 NIR temperature
    SP7BLUT [1]_   162.97                                                                float   [K] SP7 blue temperature
    SP1BLUP [1]_   8.153e-08                                                             float   [mb] SP1 blue pressure
    SP0REDT [1]_   139.99                                                                float   [K] SP0 red temperature
    SP2BLUP [1]_   7.737e-08                                                             float   [mb] SP2 blue pressure
    SUNDEC [1]_    9.120592                                                              float   [deg] Sun declination at start of exposure
    SP3REDP [1]_   7.227e-08                                                             float   [mb] SP3 red pressure
    SP5BLUP [1]_   1.126e-07                                                             float   [mb] SP5 blue pressure
    TCSGRA [1]_    0.3                                                                   float   TCS simple gain (RA)
    ACTTEFF [1]_   621.6407                                                              float   [s] Actual effective exposure time
    SEEING [1]_    1.0943                                                                float   [arcsec] ETC seeing
    SP5BLUT [1]_   162.97                                                                float   [K] SP5 blue temperature
    SP8BLUT [1]_   162.97                                                                float   [K] SP8 blue temperature
    SP3REDT [1]_   139.99                                                                float   [K] SP3 red temperature
    SP2NIRP [1]_   9.168e-08                                                             float   [mb] SP2 NIR pressure
    SP1REDP [1]_   6.17e-08                                                              float   [mb] SP1 red pressure
    VISITIDS [1]_  84509,84510                                                           str     List of expids for a visit (same tile)
    SP0REDP [1]_   1.14e-07                                                              float   [mb] SP0 red pressure
    SP1NIRP [1]_   7.269e-08                                                             float   [mb] SP1 NIR pressure
    SP0BLUT [1]_   162.97                                                                float   [K] SP0 blue temperature
    SP9REDT [1]_   139.99                                                                float   [K] SP9 red temperature
    SP7REDT [1]_   139.99                                                                float   [K] SP7 red temperature
    REQTEFF [1]_   1400.0                                                                float   [s] Requested effective exposure time
    SP5NIRP [1]_   6.289e-08                                                             float   [mb] SP5 NIR pressure
    SP6BLUT [1]_   162.97                                                                float   [K] SP6 blue temperature
    SP7REDP [1]_   6.326e-08                                                             float   [mb] SP7 red pressure
    SP1NIRT [1]_   139.96                                                                float   [K] SP1 NIR temperature
    TCSMFRA [1]_   1                                                                     int     TCS moving filter length (RA)
    SP6BLUP [1]_   7.215e-08                                                             float   [mb] SP6 blue pressure
    SP2BLUT [1]_   163.02                                                                float   [K] SP2 blue temperature
    SP3NIRT [1]_   139.99                                                                float   [K] SP3 NIR temperature
    SEQSTART [1]_  2021-04-13T04:52:57.031162                                            str     Start time of sequence processing
    SP8REDP [1]_   8.415e-08                                                             float   [mb] SP8 red pressure
    SP6REDP [1]_   6.486e-08                                                             float   [mb] SP6 red pressure
    SP7NIRT [1]_   139.99                                                                float   [K] SP7 NIR temperature
    USESPLIT [1]_  T                                                                     bool    Exposure splits are allowed
    SP9BLUT [1]_   163.02                                                                float   [K] SP9 blue temperature
    SP8NIRT [1]_   139.96                                                                float   [K] SP8 NIR temperature
    SP0BLUP [1]_   7.565e-08                                                             float   [mb] SP0 blue pressure
    SP5REDT [1]_   139.99                                                                float   [K] SP5 red temperature
    SP3NIRP [1]_   3.653e-08                                                             float   [mb] SP3 NIR pressure
    SP8REDT [1]_   139.99                                                                float   [K] SP8 red temperature
    NTSSURVY [1]_  sv3                                                                   str     NTS survey name
    TCSGDEC [1]_   0.3                                                                   float   TCS simple gain (dec)
    SP7NIRP [1]_   1.329e-07                                                             float   [mb] SP7 NIR pressure
    SP3BLUP [1]_   7.078e-08                                                             float   [mb] SP3 blue pressure
    SP0NIRT [1]_   139.96                                                                float   [K] SP0 NIR temperature
    PMSEEING [1]_  2.33                                                                  float   [arcsec] PlateMaker GFAPROC seeing
    PMTRANS [1]_   108.64                                                                float   [%] PlateMaker GFAPROC transparency
    SEQTOT [1]_    2                                                                     int     Total number of exposures in sequence
    SEQID [1]_     2 requests                                                            str     Exposure sequence identifier
    TRANSPAR [1]_  74.6046588181844                                                      float   ETC transparency
    SLEWANGL [1]_  0.13                                                                  float   [deg] Slew Angle
    CONVERGD [1]_  F                                                                     bool    Positioning loop converged (CNFRC&gt;0.95)
    POSCVFRC [1]_  0.4153                                                                float   Fraction of converged positioners
    SBPROF [1]_    BGS                                                                   str     Profile used by ETC
    ETCVERS [1]_   0.1.12-3-g12b54bb                                                     str     ETC version
    MAXTIME [1]_   5400.0                                                                float   [s] Maximum exposure time for entire visit (fro
    MINTIME [1]_   60.0                                                                  float   [s] Minimum exposure time (from NTS, used by ET
    ETCTEFF [1]_   68.498291                                                             float   [s] ETC effective exposure time
    ESTTIME [1]_   1088.936                                                              float   [s] Estimated exposure time for visit (from ETC
    NTSPROG [1]_   BACKUP                                                                str     NTS program name
    ACQFWHM [1]_   1.080625                                                              float   [arcsec] FWHM of guide star PSF in acquisition
    PMTRANSP [1]_  96.38                                                                 float   [%] PlateMaker GFAPROC transparency
    ETCFRACE [1]_  0.460059                                                              float   ETC transparency weighted average of FFRAC (ELG
    ETCTRANS [1]_  0.931484                                                              float   ETC averaged TRANSP normalized to 1
    ETCREAL [1]_   145.539062                                                            float   [s] ETC real open shutter time
    ETCSPLIT [1]_  1                                                                     int     ETC split sequence number for this visit
    ETCTHRUP [1]_  1.079734                                                              float   ETC averaged thruput (PSF profile)
    ETCSKY [1]_    1.606062                                                              float   ETC averaged, normalized sky camera flux
    ETCSEENG [1]_  1.0806                                                                float   [arcsec] ETC seeing
    ETCPROF [1]_   PSF                                                                   str     ETC source brightness profile
    ETCFRACB [1]_  0.204095                                                              float   ETC transparency weighted average of FFRAC (BGS
    ETCFRACP [1]_  0.651421                                                              float   ETC transparency weighted average of FFRAC (PSF
    ETCTHRUB [1]_  1.001377                                                              float   ETC averaged thruput (BGS profile)
    ETCPREV [1]_   0.0                                                                   float   [s] ETC cummulative t_eff for visit
    ETCTHRUE [1]_  1.039635                                                              float   ETC averaged thruput (ELG profile)
    USESPLITS [1]_ T                                                                     bool    Exposure splits are allowed
    ============== ===================================================================== ======= ===============================================

Data: FITS image [float32, 2881x500]

HDU1
----

EXTNAME = IVAR

Inverse variance of flux (*i.e.* ``error**-2``).

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2881             int
    NAXIS2   500              int
    CHECKSUM ZhXFagUETgUEZgUE str  HDU checksum updated 2021-07-16T15:54:37
    DATASUM  1428281379       str  data unit checksum updated 2021-07-16T15:54:37
    ======== ================ ==== ==============================================

Data: FITS image [float32, 2881x500]

HDU2
----

EXTNAME = MASK

Mask of spectra; 0=good.

Prior to desispec/0.24.0 and software release 18.9, the MASK HDU was compressed.

TODO: add documentation link to what bits mean what.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2881             int
    NAXIS2   500              int
    BSCALE   1                int
    BZERO    2147483648       int
    CHECKSUM UA8FU87FUA7FU77F str  HDU checksum updated 2021-07-16T15:54:38
    DATASUM  413756347        str  data unit checksum updated 2021-07-16T15:54:38
    ======== ================ ==== ==============================================

Data: FITS image [int32, 2881x500]

HDU3
----

EXTNAME = WAVELENGTH

Wavelengths at which flux is measured.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2881             int
    BUNIT    Angstrom         str
    CHECKSUM jbdTkaZRjabRjaZR str  HDU checksum updated 2021-07-16T15:54:38
    DATASUM  3106662670       str  data unit checksum updated 2021-07-16T15:54:38
    ======== ================ ==== ==============================================

Data: FITS image [float64, 2881]

HDU4
----

EXTNAME = RESOLUTION

Diagonal elements of convolution matrix describing spectral resolution.

TODO: add code example for using this.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2881             int
    NAXIS2   11               int
    NAXIS3   500              int
    CHECKSUM fiDjhZAiffAifZAi str  HDU checksum updated 2021-07-16T15:54:41
    DATASUM  2514154349       str  data unit checksum updated 2021-07-16T15:54:41
    ======== ================ ==== ==============================================

Data: FITS image [float32, 2881x11x500]

HDU5
----

EXTNAME = FIBERMAP

Fibermap of what targets were assigned to what fibers.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ============== ============================================================================================================================================================================================================================================================================================= ======= ==============================================
    KEY            Example Value                                                                                                                                                                                                                                                                                 Type    Comment
    ============== ============================================================================================================================================================================================================================================================================================= ======= ==============================================
    NAXIS1         393                                                                                                                                                                                                                                                                                           int     length of dimension 1
    NAXIS2         500                                                                                                                                                                                                                                                                                           int     length of dimension 2
    TILEID         80616                                                                                                                                                                                                                                                                                         int
    TILERA         356.0                                                                                                                                                                                                                                                                                         float
    TILEDEC        29.0                                                                                                                                                                                                                                                                                          float
    FIELDROT       -0.00962199210064233                                                                                                                                                                                                                                                                          float
    FA_PLAN        2022-07-01T00:00:00.000                                                                                                                                                                                                                                                                       str
    FA_HA          0.0                                                                                                                                                                                                                                                                                           float
    FA_RUN         2020-03-06T00:00:00                                                                                                                                                                                                                                                                           str
    FA_M_GFA [1]_  0.4                                                                                                                                                                                                                                                                                           float
    FA_M_PET [1]_  0.4                                                                                                                                                                                                                                                                                           float
    FA_M_POS [1]_  0.05                                                                                                                                                                                                                                                                                          float
    REQRA          356.0                                                                                                                                                                                                                                                                                         float
    REQDEC         29.0                                                                                                                                                                                                                                                                                          float
    FIELDNUM       0                                                                                                                                                                                                                                                                                             int
    FA_VER         2.0.0.dev2618                                                                                                                                                                                                                                                                                 str
    FA_SURV        sv1                                                                                                                                                                                                                                                                                           str
    LONGSTRN       OGIP 1.0                                                                                                                                                                                                                                                                                      str
    GFA            /data/target/catalogs/dr9/0.47.0/gfas                                                                                                                                                                                                                                                         str
    SKY            /data/target/catalogs/dr9/0.47.0/skies                                                                                                                                                                                                                                                        str
    SKYSUPP        /data/target/catalogs/gaiadr2/0.47.0/skies-supp                                                                                                                                                                                                                                               str
    TARG           /data/target/catalogs/dr9/0.47.0/targets/sv1/resolve/bright/                                                                                                                                                                                                                                  str
    FAFLAVOR       sv1bgsmws                                                                                                                                                                                                                                                                                     str
    FAOUTDIR       /software/datasystems/users/raichoor/fiberassign-test/desi-sv1-20201218/                                                                                                                                                                                                                      str
    PMTIME [1]_    2020-12-18T00:00:00.000                                                                                                                                                                                                                                                                       str
    RUNDATE        2020-03-06T00:00:00                                                                                                                                                                                                                                                                           str
    SCTARG [1]_    STD_WD,BGS_ANY,MWS_ANY                                                                                                                                                                                                                                                                        str
    OBSCON         DARK|GRAY|BRIGHT                                                                                                                                                                                                                                                                              str
    MODULE         CI                                                                                                                                                                                                                                                                                            str
    EXPID          69022                                                                                                                                                                                                                                                                                         int
    EXPFRAME       0                                                                                                                                                                                                                                                                                             int
    COSMSPLT       F                                                                                                                                                                                                                                                                                             bool
    MAXSPLIT       0                                                                                                                                                                                                                                                                                             int
    SPLITIDS [1]_  69022                                                                                                                                                                                                                                                                                         str
    FIBASSGN       /data/tiles/SVN_tiles/080/fiberassign-080616.fits                                                                                                                                                                                                                                             str
    FLAVOR         science                                                                                                                                                                                                                                                                                       str
    OBSTYPE        SCIENCE                                                                                                                                                                                                                                                                                       str
    SEQUENCE       DESI                                                                                                                                                                                                                                                                                          str
    MANIFEST       F                                                                                                                                                                                                                                                                                             bool
    OBJECT                                                                                                                                                                                                                                                                                                       str
    PURPOSE        Commissioning                                                                                                                                                                                                                                                                                 str
    PROGRAM        SV1 BGS+MWS tile 80616                                                                                                                                                                                                                                                                        str
    PROPID         2019B-5000                                                                                                                                                                                                                                                                                    str
    OBSERVER       DESIObserver                                                                                                                                                                                                                                                                                  str
    LEAD           RunManager                                                                                                                                                                                                                                                                                    str
    INSTRUME       DESI                                                                                                                                                                                                                                                                                          str
    OBSERVAT       KPNO                                                                                                                                                                                                                                                                                          str
    OBS-LAT        31.96403                                                                                                                                                                                                                                                                                      str
    OBS-LONG       -111.59989                                                                                                                                                                                                                                                                                    str
    OBS-ELEV       2097.0                                                                                                                                                                                                                                                                                        float
    TELESCOP       KPNO 4.0-m telescope                                                                                                                                                                                                                                                                          str
    CORRCTOR       DESI Corrector                                                                                                                                                                                                                                                                                str
    SEQNUM         1                                                                                                                                                                                                                                                                                             int
    NIGHT          20201220                                                                                                                                                                                                                                                                                      int
    TIMESYS        UTC                                                                                                                                                                                                                                                                                           str
    DATE-OBS       2020-12-21T02:36:32.099838                                                                                                                                                                                                                                                                    str
    MJD-OBS        59204.10870486                                                                                                                                                                                                                                                                                float
    OPENSHUT       2020-12-21T02:36:32.099838                                                                                                                                                                                                                                                                    Unknown
    CAMSHUT        open                                                                                                                                                                                                                                                                                          str
    ST             01:10:39.210                                                                                                                                                                                                                                                                                  str
    ACQTIME        15.0                                                                                                                                                                                                                                                                                          int
    GUIDTIME       5.0                                                                                                                                                                                                                                                                                           float
    FOCSTIME       60.0                                                                                                                                                                                                                                                                                          float
    SKYTIME        60.0                                                                                                                                                                                                                                                                                          float
    WHITESPT       F                                                                                                                                                                                                                                                                                             bool
    ZENITH         F                                                                                                                                                                                                                                                                                             bool
    SEANNEX        F                                                                                                                                                                                                                                                                                             bool
    BEYONDP        F                                                                                                                                                                                                                                                                                             bool
    FIDUCIAL       off                                                                                                                                                                                                                                                                                           str
    BACKLIT        off                                                                                                                                                                                                                                                                                           str
    AIRMASS        1.060311                                                                                                                                                                                                                                                                                      float
    FOCUS          1426.5,-501.4,81.0,-2.6,42.3,169.2                                                                                                                                                                                                                                                            str
    VCCD           ON                                                                                                                                                                                                                                                                                            str
    TRUSTEMP       11.767                                                                                                                                                                                                                                                                                        float
    PMIRTEMP       8.925                                                                                                                                                                                                                                                                                         float
    PMREADY        T                                                                                                                                                                                                                                                                                             bool
    PMCOVER        open                                                                                                                                                                                                                                                                                          str
    PMCOOL         off                                                                                                                                                                                                                                                                                           str
    DOMSHUTU       open                                                                                                                                                                                                                                                                                          str
    DOMSHUTL       open                                                                                                                                                                                                                                                                                          str
    DOMLIGHH       off                                                                                                                                                                                                                                                                                           str
    DOMLIGHL       off                                                                                                                                                                                                                                                                                           str
    DOMEAZ         255.166                                                                                                                                                                                                                                                                                       float
    DOMINPOS       T                                                                                                                                                                                                                                                                                             bool
    EQUINOX        2000.0                                                                                                                                                                                                                                                                                        float
    GUIDOFFR       -0.052283                                                                                                                                                                                                                                                                                     float
    GUIDOFFD       0.136634                                                                                                                                                                                                                                                                                      float
    MOONDEC        -8.975162                                                                                                                                                                                                                                                                                     float
    MOONRA         352.538429                                                                                                                                                                                                                                                                                    float
    MOUNTAZ        266.70224                                                                                                                                                                                                                                                                                     float
    MOUNTDEC       28.999221                                                                                                                                                                                                                                                                                     float
    MOUNTEL        71.039837                                                                                                                                                                                                                                                                                     float
    MOUNTHA        21.769281                                                                                                                                                                                                                                                                                     float
    INCTRL         T                                                                                                                                                                                                                                                                                             bool
    INPOS          T                                                                                                                                                                                                                                                                                             bool
    MNTOFFD        -15.76                                                                                                                                                                                                                                                                                        float
    MNTOFFR        29.32                                                                                                                                                                                                                                                                                         float
    PARALLAC       75.635085                                                                                                                                                                                                                                                                                     float
    SKYDEC         28.999221                                                                                                                                                                                                                                                                                     float
    SKYRA          355.996551                                                                                                                                                                                                                                                                                    float
    TARGTDEC       28.999221                                                                                                                                                                                                                                                                                     float
    TARGTRA        355.996551                                                                                                                                                                                                                                                                                    float
    TARGTAZ        267.074049                                                                                                                                                                                                                                                                                    float
    TARGTEL        70.563787                                                                                                                                                                                                                                                                                     float
    TRGTOFFD       0.0                                                                                                                                                                                                                                                                                           float
    TRGTOFFR       0.0                                                                                                                                                                                                                                                                                           float
    ZD             19.436213                                                                                                                                                                                                                                                                                     float
    TCSST          01:13:18.668                                                                                                                                                                                                                                                                                  str
    TCSMJD         59204.110981                                                                                                                                                                                                                                                                                  float
    USEETC         F                                                                                                                                                                                                                                                                                             bool
    ACQCAM         GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                                                                                                                                                                                                                                                     str
    GUIDECAM       GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                                                                                                                                                                                                                                                     str
    FOCUSCAM       FOCUS1,FOCUS4,FOCUS6,FOCUS9                                                                                                                                                                                                                                                                   str
    SKYCAM         SKYCAM0,SKYCAM1                                                                                                                                                                                                                                                                               str
    REQADC         65.78,85.28                                                                                                                                                                                                                                                                                   str
    ADCCORR        T                                                                                                                                                                                                                                                                                             bool
    ADC1PHI        65.780005                                                                                                                                                                                                                                                                                     float
    ADC2PHI        85.279991                                                                                                                                                                                                                                                                                     float
    ADC1HOME       F                                                                                                                                                                                                                                                                                             bool
    ADC2HOME       F                                                                                                                                                                                                                                                                                             bool
    ADC1NREV       -1.0                                                                                                                                                                                                                                                                                          float
    ADC2NREV       0.0                                                                                                                                                                                                                                                                                           float
    ADC1STAT       STOPPED                                                                                                                                                                                                                                                                                       str
    ADC2STAT       STOPPED                                                                                                                                                                                                                                                                                       str
    USESKY         T                                                                                                                                                                                                                                                                                             bool
    USEFOCUS       T                                                                                                                                                                                                                                                                                             bool
    HEXPOS         1426.5,-501.3,81.0,-2.6,42.3,171.9                                                                                                                                                                                                                                                            str
    HEXTRIM        0.0,0.0,0.0,0.0,0.0,0.0                                                                                                                                                                                                                                                                       str
    USEROTAT       T                                                                                                                                                                                                                                                                                             bool
    ROTOFFST       167.1                                                                                                                                                                                                                                                                                         float
    ROTENBLD       T                                                                                                                                                                                                                                                                                             bool
    ROTRATE        0.0                                                                                                                                                                                                                                                                                           float
    RESETROT       F                                                                                                                                                                                                                                                                                             bool
    USEPOS         T                                                                                                                                                                                                                                                                                             bool
    PETALS         PETAL0,PETAL1,PETAL2,PETAL3,PETAL4,PETAL5,PETAL6,PETAL7,PETAL8,PETAL9                                                                                                                                                                                                                         str
    POSCYCLE       1                                                                                                                                                                                                                                                                                             int
    POSONTGT       3626                                                                                                                                                                                                                                                                                          int
    POSONFRC       0.8613                                                                                                                                                                                                                                                                                        float
    POSDISAB       37                                                                                                                                                                                                                                                                                            int
    POSENABL       4210                                                                                                                                                                                                                                                                                          int
    POSRMS         0.0171                                                                                                                                                                                                                                                                                        float
    POSITER        1                                                                                                                                                                                                                                                                                             int
    POSFRACT       0.95                                                                                                                                                                                                                                                                                          float
    POSTOLER       0.01                                                                                                                                                                                                                                                                                          float
    POSMVALL       T                                                                                                                                                                                                                                                                                             bool
    USEGUIDR       T                                                                                                                                                                                                                                                                                             bool
    GUIDMODE       catalog                                                                                                                                                                                                                                                                                       str
    USEAOS [1]_    F                                                                                                                                                                                                                                                                                             bool
    USEDONUT       T                                                                                                                                                                                                                                                                                             bool
    USESPCTR       T                                                                                                                                                                                                                                                                                             bool
    SPCGRPHS       SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                                                                                                                                                                                                                                                       str
    ILLSPECS [1]_  SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                                                                                                                                                                                                                                                       str
    CCDSPECS [1]_  SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                                                                                                                                                                                                                                                       str
    TDEWPNT        -16.043                                                                                                                                                                                                                                                                                       float
    TAIRFLOW       0.0                                                                                                                                                                                                                                                                                           float
    TAIRITMP       11.8                                                                                                                                                                                                                                                                                          float
    TAIROTMP       11.7                                                                                                                                                                                                                                                                                          float
    TAIRTEMP       10.65                                                                                                                                                                                                                                                                                         float
    TCASITMP       0.0                                                                                                                                                                                                                                                                                           float
    TCASOTMP       10.8                                                                                                                                                                                                                                                                                          float
    TCSITEMP       9.3                                                                                                                                                                                                                                                                                           float
    TCSOTEMP       10.8                                                                                                                                                                                                                                                                                          float
    TCIBTEMP       0.0                                                                                                                                                                                                                                                                                           float
    TCIMTEMP       0.0                                                                                                                                                                                                                                                                                           float
    TCITTEMP       0.0                                                                                                                                                                                                                                                                                           float
    TCOSTEMP       0.0                                                                                                                                                                                                                                                                                           float
    TCOWTEMP       0.0                                                                                                                                                                                                                                                                                           float
    TDBTEMP        9.3                                                                                                                                                                                                                                                                                           float
    TFLOWIN        0.0                                                                                                                                                                                                                                                                                           float
    TFLOWOUT       0.0                                                                                                                                                                                                                                                                                           float
    TGLYCOLI       9.9                                                                                                                                                                                                                                                                                           float
    TGLYCOLO       9.8                                                                                                                                                                                                                                                                                           float
    THINGES        11.4                                                                                                                                                                                                                                                                                          float
    THINGEW        11.2                                                                                                                                                                                                                                                                                          float
    TPMAVERT       8.931                                                                                                                                                                                                                                                                                         float
    TPMDESIT       7.0                                                                                                                                                                                                                                                                                           float
    TPMEIBT        8.6                                                                                                                                                                                                                                                                                           float
    TPMEITT        8.6                                                                                                                                                                                                                                                                                           float
    TPMEOBT        8.5                                                                                                                                                                                                                                                                                           float
    TPMEOTT        9.0                                                                                                                                                                                                                                                                                           float
    TPMNIBT        8.4                                                                                                                                                                                                                                                                                           float
    TPMNITT        8.9                                                                                                                                                                                                                                                                                           float
    TPMNOBT        8.8                                                                                                                                                                                                                                                                                           float
    TPMNOTT        9.1                                                                                                                                                                                                                                                                                           float
    TPMRTDT        9.0                                                                                                                                                                                                                                                                                           float
    TPMSIBT        8.6                                                                                                                                                                                                                                                                                           float
    TPMSITT        8.8                                                                                                                                                                                                                                                                                           float
    TPMSOBT        8.2                                                                                                                                                                                                                                                                                           float
    TPMSOTT        8.9                                                                                                                                                                                                                                                                                           float
    TPMSTAT        ready                                                                                                                                                                                                                                                                                         str
    TPMWIBT        8.2                                                                                                                                                                                                                                                                                           float
    TPMWITT        9.1                                                                                                                                                                                                                                                                                           float
    TPMWOBT        8.3                                                                                                                                                                                                                                                                                           float
    TPMWOTT        8.9                                                                                                                                                                                                                                                                                           float
    TPCITEMP       8.5                                                                                                                                                                                                                                                                                           float
    TPCOTEMP       8.6                                                                                                                                                                                                                                                                                           float
    TPR1HUM        0.0                                                                                                                                                                                                                                                                                           float
    TPR1TEMP       0.0                                                                                                                                                                                                                                                                                           float
    TPR2HUM        0.0                                                                                                                                                                                                                                                                                           float
    TPR2TEMP       0.0                                                                                                                                                                                                                                                                                           float
    TSERVO         40.0                                                                                                                                                                                                                                                                                          float
    TTRSTEMP       11.4                                                                                                                                                                                                                                                                                          float
    TTRWTEMP       11.0                                                                                                                                                                                                                                                                                          float
    TTRUETBT       -4.2                                                                                                                                                                                                                                                                                          float
    TTRUETTT       11.2                                                                                                                                                                                                                                                                                          float
    TTRUNTBT       10.9                                                                                                                                                                                                                                                                                          float
    TTRUNTTT       11.2                                                                                                                                                                                                                                                                                          float
    TTRUSTBT       10.7                                                                                                                                                                                                                                                                                          float
    TTRUSTST       10.8                                                                                                                                                                                                                                                                                          float
    TTRUSTTT       11.1                                                                                                                                                                                                                                                                                          float
    TTRUTSBT       11.8                                                                                                                                                                                                                                                                                          float
    TTRUTSMT       11.8                                                                                                                                                                                                                                                                                          float
    TTRUTSTT       11.8                                                                                                                                                                                                                                                                                          float
    TTRUWTBT       10.5                                                                                                                                                                                                                                                                                          float
    TTRUWTTT       10.9                                                                                                                                                                                                                                                                                          float
    ALARM          F                                                                                                                                                                                                                                                                                             bool
    ALARM-ON       F                                                                                                                                                                                                                                                                                             bool
    BATTERY        100.0                                                                                                                                                                                                                                                                                         float
    SECLEFT        5178.0                                                                                                                                                                                                                                                                                        float
    UPSSTAT        System Normal - On Line(7)                                                                                                                                                                                                                                                                    str
    INAMPS         70.4                                                                                                                                                                                                                                                                                          float
    OUTWATTS       5000.0,7200.0,4800.0                                                                                                                                                                                                                                                                          str
    COMPDEW        -12.9                                                                                                                                                                                                                                                                                         float
    COMPHUM        7.4                                                                                                                                                                                                                                                                                           float
    COMPAMB        19.5                                                                                                                                                                                                                                                                                          float
    COMPTEMP       24.5                                                                                                                                                                                                                                                                                          float
    DEWPOINT       11.5                                                                                                                                                                                                                                                                                          float
    HUMIDITY       10.0                                                                                                                                                                                                                                                                                          float
    PRESSURE       795.0                                                                                                                                                                                                                                                                                         float
    OUTTEMP        0.0                                                                                                                                                                                                                                                                                           float
    WINDDIR        55.0                                                                                                                                                                                                                                                                                          float
    WINDSPD        27.3                                                                                                                                                                                                                                                                                          float
    GUST           20.6                                                                                                                                                                                                                                                                                          float
    AMNIENTN       13.5                                                                                                                                                                                                                                                                                          float
    CFLOOR         8.9                                                                                                                                                                                                                                                                                           float
    NWALLIN        13.9                                                                                                                                                                                                                                                                                          float
    NWALLOUT       9.6                                                                                                                                                                                                                                                                                           float
    WWALLIN        12.9                                                                                                                                                                                                                                                                                          float
    WWALLOUT       10.6                                                                                                                                                                                                                                                                                          float
    AMBIENTS       14.8                                                                                                                                                                                                                                                                                          float
    FLOOR          12.6                                                                                                                                                                                                                                                                                          float
    EWALLCMP       10.8                                                                                                                                                                                                                                                                                          float
    EWALLCOU       10.6                                                                                                                                                                                                                                                                                          float
    ROOF           10.3                                                                                                                                                                                                                                                                                          float
    ROOFAMB        10.6                                                                                                                                                                                                                                                                                          float
    DOMEBLOW       10.4                                                                                                                                                                                                                                                                                          float
    DOMEBUP        10.7                                                                                                                                                                                                                                                                                          float
    DOMELLOW       10.8                                                                                                                                                                                                                                                                                          float
    DOMELUP        10.8                                                                                                                                                                                                                                                                                          float
    DOMERLOW       10.6                                                                                                                                                                                                                                                                                          float
    DOMERUP        10.5                                                                                                                                                                                                                                                                                          float
    PLATFORM       10.4                                                                                                                                                                                                                                                                                          float
    SHACKC         14.4                                                                                                                                                                                                                                                                                          float
    SHACKW         13.7                                                                                                                                                                                                                                                                                          float
    STAIRSL        10.5                                                                                                                                                                                                                                                                                          float
    STAIRSM        10.4                                                                                                                                                                                                                                                                                          float
    STAIRSU        10.6                                                                                                                                                                                                                                                                                          float
    TELBASE        9.6                                                                                                                                                                                                                                                                                           float
    UTILWALL       11.1                                                                                                                                                                                                                                                                                          float
    UTILROOM       10.9                                                                                                                                                                                                                                                                                          float
    RADESYS        FK5                                                                                                                                                                                                                                                                                           str
    TNFSPROC       8.1963                                                                                                                                                                                                                                                                                        float
    TGFAPROC [1]_  7.9212                                                                                                                                                                                                                                                                                        float
    SIMGFAP        F                                                                                                                                                                                                                                                                                             bool
    USEFVC         T                                                                                                                                                                                                                                                                                             bool
    USEFID         T                                                                                                                                                                                                                                                                                             bool
    USEILLUM       T                                                                                                                                                                                                                                                                                             bool
    USEXSRVR       T                                                                                                                                                                                                                                                                                             bool
    USEOPENL       T                                                                                                                                                                                                                                                                                             bool
    STOPGUDR       T                                                                                                                                                                                                                                                                                             bool
    STOPFOCS       T                                                                                                                                                                                                                                                                                             bool
    STOPSKY        T                                                                                                                                                                                                                                                                                             bool
    KEEPGUDR       F                                                                                                                                                                                                                                                                                             bool
    KEEPFOCS       F                                                                                                                                                                                                                                                                                             bool
    KEEPSKY        F                                                                                                                                                                                                                                                                                             bool
    REACQUIR       F                                                                                                                                                                                                                                                                                             bool
    FILENAME       /exposures/desi/20201220/00069022/desi-00069022.fits.fz                                                                                                                                                                                                                                       str
    EXCLUDED                                                                                                                                                                                                                                                                                                     str
    DOSVER         trunk                                                                                                                                                                                                                                                                                         str
    OCSVER         1.2                                                                                                                                                                                                                                                                                           float
    CONSTVER       DESI:CURRENT                                                                                                                                                                                                                                                                                  str
    INIFILE        /data/msdos/dos_home/architectures/kpno/desi.ini                                                                                                                                                                                                                                              str
    REQTIME        300.0                                                                                                                                                                                                                                                                                         float
    FVCTIME [1]_   2.0                                                                                                                                                                                                                                                                                           float
    SIMGFACQ       F                                                                                                                                                                                                                                                                                             bool
    POSCNVGD [1]_  F                                                                                                                                                                                                                                                                                             bool
    GUIEXPID       69022                                                                                                                                                                                                                                                                                         int
    IGFRMNUM       12                                                                                                                                                                                                                                                                                            int
    FOCEXPID       69022                                                                                                                                                                                                                                                                                         int
    IFFRMNUM       1                                                                                                                                                                                                                                                                                             int
    SKYEXPID       69022                                                                                                                                                                                                                                                                                         int
    ISFRMNUM       1                                                                                                                                                                                                                                                                                             int
    FGFRMNUM       46                                                                                                                                                                                                                                                                                            int
    FFFRMNUM       6                                                                                                                                                                                                                                                                                             int
    FSFRMNUM       5                                                                                                                                                                                                                                                                                             int
    FRAMES [1]_    47                                                                                                                                                                                                                                                                                            int
    DELTARA [1]_   None                                                                                                                                                                                                                                                                                          Unknown
    DELTADEC [1]_  None                                                                                                                                                                                                                                                                                          Unknown
    GSGUIDE0 [1]_  (980.05,685.98),(878.97,731.68)                                                                                                                                                                                                                                                               str
    GSGUIDE2 [1]_  (372.65,939.43),(784.50,1529.96)                                                                                                                                                                                                                                                              str
    GSGUIDE3 [1]_  (365.22,1423.83),(249.12,411.52)                                                                                                                                                                                                                                                              str
    GSGUIDE5 [1]_  (848.52,78.26),(516.16,1410.54)                                                                                                                                                                                                                                                               str
    GSGUIDE7 [1]_  (540.95,1848.95),(504.68,831.62)                                                                                                                                                                                                                                                              str
    GSGUIDE8 [1]_  (720.29,552.69),(499.80,465.13)                                                                                                                                                                                                                                                               str
    ARCHIVE [1]_   /exposures/desi/20201220/00069022/guide-00069022.fits.fz                                                                                                                                                                                                                                      str
    GUIDEFIL       guide-00069022.fits.fz                                                                                                                                                                                                                                                                        str
    COORDFIL       coordinates-00069022.fits                                                                                                                                                                                                                                                                     str
    TIME-OBS       02:39:11.845920                                                                                                                                                                                                                                                                               str
    EXPTIME        300.007                                                                                                                                                                                                                                                                                       float
    VCCDON         2020-12-09T21:23:19.307761                                                                                                                                                                                                                                                                    str
    VCCDSEC        969702.2                                                                                                                                                                                                                                                                                      float
    SPECGRPH       8                                                                                                                                                                                                                                                                                             int
    SPECID         2                                                                                                                                                                                                                                                                                             int
    FEEBOX         lbnl050                                                                                                                                                                                                                                                                                       str
    VESSEL         8                                                                                                                                                                                                                                                                                             int
    FEEVER         v20160312                                                                                                                                                                                                                                                                                     str
    FEEPOWER       ON                                                                                                                                                                                                                                                                                            str
    FEEDMASK       2134851391                                                                                                                                                                                                                                                                                    int
    FEECMASK       1048575                                                                                                                                                                                                                                                                                       int
    CCDTEMP        -135.3315                                                                                                                                                                                                                                                                                     float
    AMPSECB        [4114:2058, 1:2064]                                                                                                                                                                                                                                                                           str
    DAC16          39.9961,39.3162                                                                                                                                                                                                                                                                               str
    CLOCK8         9.9992,2.9993                                                                                                                                                                                                                                                                                 str
    PRRSECD        [2193:4249, 4194:4194]                                                                                                                                                                                                                                                                        str
    CCDPREP        purge,clear                                                                                                                                                                                                                                                                                   str
    CLOCK10        9.9992,2.9993                                                                                                                                                                                                                                                                                 str
    DAC17          20.0008,12.2732                                                                                                                                                                                                                                                                               str
    ORSECB         [2193:4249, 2066:2097]                                                                                                                                                                                                                                                                        str
    DAC15          0.0,0.0148                                                                                                                                                                                                                                                                                    str
    ORSECD         [2193:4249, 2098:2129]                                                                                                                                                                                                                                                                        str
    DIGITIME       47.5899                                                                                                                                                                                                                                                                                       float
    BIASSECA       [2065:2128, 2:2065]                                                                                                                                                                                                                                                                           str
    CLOCK9         9.9992,2.9993                                                                                                                                                                                                                                                                                 str
    CLOCK18        9.0,0.9999                                                                                                                                                                                                                                                                                    str
    CAMERA         r8                                                                                                                                                                                                                                                                                            str
    CLOCK17        9.0,0.9999                                                                                                                                                                                                                                                                                    str
    CLOCK5         9.9999,0.0                                                                                                                                                                                                                                                                                    str
    TRIMSECD       [2193:4249, 2130:4193]                                                                                                                                                                                                                                                                        str
    DETSECD        [2058:4114, 2065:4128]                                                                                                                                                                                                                                                                        str
    DAC0           -9.0002,-8.9507                                                                                                                                                                                                                                                                               str
    CLOCK15        9.9992,2.9993                                                                                                                                                                                                                                                                                 str
    TRIMSECA       [8:2064, 2:2065]                                                                                                                                                                                                                                                                              str
    BIASSECB       [2129:2192, 2:2065]                                                                                                                                                                                                                                                                           str
    CLOCK11        9.9992,2.9993                                                                                                                                                                                                                                                                                 str
    CLOCK12        9.9992,2.9993                                                                                                                                                                                                                                                                                 str
    AMPSECD        [4114:2058, 4128:2065]                                                                                                                                                                                                                                                                        str
    CLOCK4         9.9999,0.0                                                                                                                                                                                                                                                                                    str
    PRRSECB        [2193:4249, 1:1]                                                                                                                                                                                                                                                                              str
    CCDSECD        [2058:4114, 2065:4128]                                                                                                                                                                                                                                                                        str
    CCDTMING       default_lbnl_timing_20180905.txt                                                                                                                                                                                                                                                              str
    TRIMSECB       [2193:4249, 2:2065]                                                                                                                                                                                                                                                                           str
    CCDSIZE        4194,4256                                                                                                                                                                                                                                                                                     str
    PGAGAIN        3                                                                                                                                                                                                                                                                                             int
    PRESECD        [4250:4256, 2130:4193]                                                                                                                                                                                                                                                                        str
    CLOCK6         9.9999,0.0                                                                                                                                                                                                                                                                                    str
    CLOCK13        9.9992,2.9993                                                                                                                                                                                                                                                                                 str
    DAC7           5.9998,6.028                                                                                                                                                                                                                                                                                  str
    DATASECA       [8:2064, 2:2065]                                                                                                                                                                                                                                                                              str
    CRYOTEMP [1]_  162.97                                                                                                                                                                                                                                                                                        float
    OFFSET2        0.4000000059604645,-8.9198                                                                                                                                                                                                                                                                    str
    OFFSET6        2.0,6.0437                                                                                                                                                                                                                                                                                    str
    DELAYS         20, 20, 25, 40, 7, 3000, 7, 7, 7, 7                                                                                                                                                                                                                                                           str
    BIASSECD       [2129:2192, 2130:4193]                                                                                                                                                                                                                                                                        str
    PRRSECA        [8:2064, 1:1]                                                                                                                                                                                                                                                                                 str
    TRIMSECC       [8:2064, 2130:4193]                                                                                                                                                                                                                                                                           str
    CLOCK3         -2.0001,3.9999                                                                                                                                                                                                                                                                                str
    CCDNAME        CCDSM2R                                                                                                                                                                                                                                                                                       str
    DAC9           -25.0003,-24.768                                                                                                                                                                                                                                                                              str
    CCDSECC        [1:2057, 2065:4128]                                                                                                                                                                                                                                                                           str
    ORSECA         [8:2064, 2066:2097]                                                                                                                                                                                                                                                                           str
    DAC5           5.9998,6.0543                                                                                                                                                                                                                                                                                 str
    CCDSECB        [2058:4114, 1:2064]                                                                                                                                                                                                                                                                           str
    DETSECB        [2058:4114, 1:2064]                                                                                                                                                                                                                                                                           str
    OFFSET0        0.4000000059604645,-8.9507                                                                                                                                                                                                                                                                    str
    SETTINGS       detectors_sm_20191211.json                                                                                                                                                                                                                                                                    str
    DAC11          -25.0003,-24.8422                                                                                                                                                                                                                                                                             str
    BIASSECC       [2065:2128, 2130:4193]                                                                                                                                                                                                                                                                        str
    CASETEMP       59.8142                                                                                                                                                                                                                                                                                       float
    DAC10          -25.0003,-24.7086                                                                                                                                                                                                                                                                             str
    DAC1           -9.0002,-8.9198                                                                                                                                                                                                                                                                               str
    DAC14          0.0,0.0594                                                                                                                                                                                                                                                                                    str
    DETECTOR       M1-46                                                                                                                                                                                                                                                                                         str
    CDSPARMS       400, 400, 8, 2000                                                                                                                                                                                                                                                                             str
    OFFSET3        0.4000000059604645,-8.9095                                                                                                                                                                                                                                                                    str
    DATASECB       [2193:4249, 2:2065]                                                                                                                                                                                                                                                                           str
    ORSECC         [8:2064, 2098:2129]                                                                                                                                                                                                                                                                           str
    CRYOPRES [1]_  8.897e-08                                                                                                                                                                                                                                                                                     str
    AMPSECA        [1:2057, 1:2064]                                                                                                                                                                                                                                                                              str
    OFFSET7        2.0,6.028                                                                                                                                                                                                                                                                                     str
    DAC4           5.9998,6.028                                                                                                                                                                                                                                                                                  str
    DATASECC       [8:2064, 2130:4193]                                                                                                                                                                                                                                                                           str
    PRESECC        [1:7, 2130:4193]                                                                                                                                                                                                                                                                              str
    CLOCK16        9.9999,3.0                                                                                                                                                                                                                                                                                    str
    CLOCK1         9.9999,0.0                                                                                                                                                                                                                                                                                    str
    PRESECB        [4250:4256, 2:2065]                                                                                                                                                                                                                                                                           str
    DAC12          0.0,0.0297                                                                                                                                                                                                                                                                                    str
    DAC8           -25.0003,-24.9312                                                                                                                                                                                                                                                                             str
    OFFSET4        2.0,6.0332                                                                                                                                                                                                                                                                                    str
    DAC2           -9.0002,-8.9198                                                                                                                                                                                                                                                                               str
    CCDCFG         default_lbnl_20190717.cfg                                                                                                                                                                                                                                                                     str
    BLDTIME        0.3547                                                                                                                                                                                                                                                                                        float
    PRESECA        [1:7, 2:2065]                                                                                                                                                                                                                                                                                 str
    DATASECD       [2193:4249, 2130:4193]                                                                                                                                                                                                                                                                        str
    DETSECC        [1:2057, 2065:4128]                                                                                                                                                                                                                                                                           str
    PRRSECC        [8:2064, 4194:4194]                                                                                                                                                                                                                                                                           str
    DAC6           5.9998,6.0437                                                                                                                                                                                                                                                                                 str
    DETSECA        [1:2057, 1:2064]                                                                                                                                                                                                                                                                              str
    CLOCK2         9.9999,0.0                                                                                                                                                                                                                                                                                    str
    DAC3           -9.0002,-8.9095                                                                                                                                                                                                                                                                               str
    OFFSET1        0.4000000059604645,-8.9198                                                                                                                                                                                                                                                                    str
    AMPSECC        [1:2057, 4128:2065]                                                                                                                                                                                                                                                                           str
    CLOCK7         -2.0001,3.9999                                                                                                                                                                                                                                                                                str
    DAC13          0.0,0.0148                                                                                                                                                                                                                                                                                    str
    CCDSECA        [1:2057, 1:2064]                                                                                                                                                                                                                                                                              str
    OFFSET5        2.0,6.049                                                                                                                                                                                                                                                                                     str
    CLOCK14        9.9992,2.9993                                                                                                                                                                                                                                                                                 str
    CLOCK0         9.9999,0.0                                                                                                                                                                                                                                                                                    str
    CPUTEMP        60.8086                                                                                                                                                                                                                                                                                       float
    OBSID          kp4m20201221t023911                                                                                                                                                                                                                                                                           str
    PROCTYPE       RAW                                                                                                                                                                                                                                                                                           str
    PRODTYPE       image                                                                                                                                                                                                                                                                                         str
    GAINA          1.627                                                                                                                                                                                                                                                                                         float
    SATULEVA       65535.0                                                                                                                                                                                                                                                                                       float
    OSTEPA         0.5704803307307884                                                                                                                                                                                                                                                                            float
    OMETHA         AVERAGE                                                                                                                                                                                                                                                                                       str
    OVERSCNA       1984.679589024373                                                                                                                                                                                                                                                                             float
    OBSRDNA        2.48375231913931                                                                                                                                                                                                                                                                              float
    SATUELEA       103396.3713086573                                                                                                                                                                                                                                                                             float
    GAINB          1.482                                                                                                                                                                                                                                                                                         float
    SATULEVB       65535.0                                                                                                                                                                                                                                                                                       float
    OSTEPB         0.5242006066837348                                                                                                                                                                                                                                                                            float
    OMETHB         AVERAGE                                                                                                                                                                                                                                                                                       str
    OVERSCNB       1980.885980481041                                                                                                                                                                                                                                                                             float
    OBSRDNB        2.179252294581384                                                                                                                                                                                                                                                                             float
    SATUELEB       94187.1969769271                                                                                                                                                                                                                                                                              float
    GAINC          1.581                                                                                                                                                                                                                                                                                         float
    SATULEVC       65535.0                                                                                                                                                                                                                                                                                       float
    OSTEPC         0.6303264842863427                                                                                                                                                                                                                                                                            float
    OMETHC         AVERAGE                                                                                                                                                                                                                                                                                       str
    OVERSCNC       1966.11973127108                                                                                                                                                                                                                                                                              float
    OBSRDNC        2.455388696359903                                                                                                                                                                                                                                                                             float
    SATUELEC       100502.3997048604                                                                                                                                                                                                                                                                             float
    GAIND          1.589                                                                                                                                                                                                                                                                                         float
    SATULEVD       65535.0                                                                                                                                                                                                                                                                                       float
    OSTEPD         0.6243009115278255                                                                                                                                                                                                                                                                            float
    OMETHD         AVERAGE                                                                                                                                                                                                                                                                                       str
    OVERSCND       1987.970298453192                                                                                                                                                                                                                                                                             float
    OBSRDND        2.518301447806098                                                                                                                                                                                                                                                                             float
    SATUELED       100976.2301957579                                                                                                                                                                                                                                                                             float
    FIBERMIN       4000                                                                                                                                                                                                                                                                                          int
    CHECKSUM       jfN5jZK5jdK5jZK5                                                                                                                                                                                                                                                                              str     HDU checksum updated 2022-02-14T08:25:04
    DATASUM        2198099738                                                                                                                                                                                                                                                                                    str     data unit checksum updated 2022-02-14T08:25:04
    BBKGMINC [1]_  -0.3364347403909462                                                                                                                                                                                                                                                                           float
    BBKGMAXB [1]_  0.8957266211094218                                                                                                                                                                                                                                                                            float
    BBKGMINB [1]_  -0.04275468459496062                                                                                                                                                                                                                                                                          float
    BBKGMIND [1]_  -0.6146250452424397                                                                                                                                                                                                                                                                           float
    BBKGMAXA [1]_  0.6126625684320178                                                                                                                                                                                                                                                                            float
    BBKGMAXC [1]_  0.4926723425188555                                                                                                                                                                                                                                                                            float
    BBKGMINA [1]_  -0.4336472364870191                                                                                                                                                                                                                                                                           float
    BBKGMAXD [1]_  0.8117108701207832                                                                                                                                                                                                                                                                            float
    SP2REDP [1]_   6.448e-08                                                                                                                                                                                                                                                                                     float
    SP8BLUP [1]_   8.153e-08                                                                                                                                                                                                                                                                                     float
    SP9NIRT [1]_   139.96                                                                                                                                                                                                                                                                                        float
    SP4REDP [1]_   5.168e-08                                                                                                                                                                                                                                                                                     float
    TCSKDEC [1]_   0.3 0.003 0.00003                                                                                                                                                                                                                                                                             str
    TCSPIRA [1]_   1.0,0.0,0.0,0.0                                                                                                                                                                                                                                                                               str
    SCND [1]_      DESIROOT/target/catalogs/dr9/0.57.0/targets/sv3/secondary/dark/sv3targets-dark-secondary.fits                                                                                                                                                                                                 str
    SP4BLUT [1]_   163.02                                                                                                                                                                                                                                                                                        float
    TCSMFDEC [1]_  1                                                                                                                                                                                                                                                                                             int
    SP4REDT [1]_   140.03                                                                                                                                                                                                                                                                                        float
    SP9REDP [1]_   8.485e-08                                                                                                                                                                                                                                                                                     float
    FAPRGRM [1]_   DARK                                                                                                                                                                                                                                                                                          str
    SP9NIRP [1]_   5.579e-08                                                                                                                                                                                                                                                                                     float
    SP5REDP [1]_   4.908e-08                                                                                                                                                                                                                                                                                     float
    SP1REDT [1]_   139.96                                                                                                                                                                                                                                                                                        float
    SUNRA [1]_     21.738482                                                                                                                                                                                                                                                                                     float
    SP3BLUT [1]_   163.02                                                                                                                                                                                                                                                                                        float
    SP8NIRP [1]_   4.831e-08                                                                                                                                                                                                                                                                                     float
    SP9BLUP [1]_   1.208e-07                                                                                                                                                                                                                                                                                     float
    SBPROF [1]_    ELG                                                                                                                                                                                                                                                                                           str
    TCSKRA [1]_    0.3 0.003 0.00003                                                                                                                                                                                                                                                                             str
    SKYLEVEL [1]_  1.133                                                                                                                                                                                                                                                                                         float
    FAARGS [1]_    --doclean n --dr dr9 --dtver 0.57.0 --gaiadr gaiadr2 --goaltime 1200.0 --mintfrac 0.9 --pmcorr n --pmtime 2021-04-10T21:28:37 --program DARK --rundate 2021-04-10T21:28:37 --sbprof ELG --sky_per_petal 40 --standards_per_petal 10 --survey sv3 --tiledec 0.056 --tileid 58 --tilera 182.994 str
    SP4BLUP [1]_   6.109e-08                                                                                                                                                                                                                                                                                     float
    SCNDMTL [1]_   DESIROOT/survey/ops/surveyops/trunk/mtl/sv3/secondary/dark                                                                                                                                                                                                                                    str
    SP2NIRT [1]_   139.96                                                                                                                                                                                                                                                                                        float
    SP7BLUP [1]_   9.93799999999999e-08                                                                                                                                                                                                                                                                          float
    EBVFAC [1]_    1.04684301894635                                                                                                                                                                                                                                                                              float
    SP0NIRP [1]_   5.934e-08                                                                                                                                                                                                                                                                                     float
    SP4NIRP [1]_   7.072e-08                                                                                                                                                                                                                                                                                     float
    SP1BLUT [1]_   162.97                                                                                                                                                                                                                                                                                        float
    SP6NIRP [1]_   2.873e-07                                                                                                                                                                                                                                                                                     float
    SURVEY [1]_    sv3                                                                                                                                                                                                                                                                                           str
    SP2REDT [1]_   139.99                                                                                                                                                                                                                                                                                        float
    GOALTIME [1]_  1200.0                                                                                                                                                                                                                                                                                        float
    GOALTYPE [1]_  DARK                                                                                                                                                                                                                                                                                          str
    PMCORR [1]_    n                                                                                                                                                                                                                                                                                             str
    MTL [1]_       DESIROOT/survey/ops/surveyops/trunk/mtl/sv3/dark                                                                                                                                                                                                                                              str
    SP6REDT [1]_   139.96                                                                                                                                                                                                                                                                                        float
    TCSPIDEC [1]_  1.0,0.0,0.0,0.0                                                                                                                                                                                                                                                                               str
    MOONSEP [1]_   147.894                                                                                                                                                                                                                                                                                       float
    TOTTEFF [1]_   1403.0837                                                                                                                                                                                                                                                                                     float
    SP6NIRT [1]_   139.96                                                                                                                                                                                                                                                                                        float
    SP5NIRT [1]_   139.99                                                                                                                                                                                                                                                                                        float
    SPLITEXP [1]_  T                                                                                                                                                                                                                                                                                             bool
    SP4NIRT [1]_   139.96                                                                                                                                                                                                                                                                                        float
    DESIROOT [1]_  /global/cfs/cdirs/desi                                                                                                                                                                                                                                                                        str
    SP7BLUT [1]_   162.97                                                                                                                                                                                                                                                                                        float
    SP1BLUP [1]_   8.153e-08                                                                                                                                                                                                                                                                                     float
    SP0REDT [1]_   139.99                                                                                                                                                                                                                                                                                        float
    SP2BLUP [1]_   7.737e-08                                                                                                                                                                                                                                                                                     float
    SUNDEC [1]_    9.120592                                                                                                                                                                                                                                                                                      float
    SP3REDP [1]_   7.227e-08                                                                                                                                                                                                                                                                                     float
    SP5BLUP [1]_   1.126e-07                                                                                                                                                                                                                                                                                     float
    TCSGRA [1]_    0.3                                                                                                                                                                                                                                                                                           float
    ACTTEFF [1]_   621.6407                                                                                                                                                                                                                                                                                      float
    SEEING [1]_    1.0943                                                                                                                                                                                                                                                                                        float
    SP5BLUT [1]_   162.97                                                                                                                                                                                                                                                                                        float
    SP8BLUT [1]_   162.97                                                                                                                                                                                                                                                                                        float
    SP3REDT [1]_   139.99                                                                                                                                                                                                                                                                                        float
    SP2NIRP [1]_   9.168e-08                                                                                                                                                                                                                                                                                     float
    SP1REDP [1]_   6.17e-08                                                                                                                                                                                                                                                                                      float
    VISITIDS [1]_  84509,84510                                                                                                                                                                                                                                                                                   str
    SP0REDP [1]_   1.14e-07                                                                                                                                                                                                                                                                                      float
    SP1NIRP [1]_   7.269e-08                                                                                                                                                                                                                                                                                     float
    SP0BLUT [1]_   162.97                                                                                                                                                                                                                                                                                        float
    SP9REDT [1]_   139.99                                                                                                                                                                                                                                                                                        float
    SP7REDT [1]_   139.99                                                                                                                                                                                                                                                                                        float
    REQTEFF [1]_   1400.0                                                                                                                                                                                                                                                                                        float
    SP5NIRP [1]_   6.289e-08                                                                                                                                                                                                                                                                                     float
    SP6BLUT [1]_   162.97                                                                                                                                                                                                                                                                                        float
    SP7REDP [1]_   6.326e-08                                                                                                                                                                                                                                                                                     float
    SP1NIRT [1]_   139.96                                                                                                                                                                                                                                                                                        float
    MTLTIME [1]_   2021-04-10T21:28:37                                                                                                                                                                                                                                                                           str
    TCSMFRA [1]_   1                                                                                                                                                                                                                                                                                             int
    SP6BLUP [1]_   7.21499999999999e-08                                                                                                                                                                                                                                                                          float
    SP2BLUT [1]_   163.02                                                                                                                                                                                                                                                                                        float
    SP3NIRT [1]_   139.99                                                                                                                                                                                                                                                                                        float
    SEQSTART [1]_  2021-04-13T04:52:57.031162                                                                                                                                                                                                                                                                    str
    SP8REDP [1]_   8.415e-08                                                                                                                                                                                                                                                                                     float
    SP6REDP [1]_   6.486e-08                                                                                                                                                                                                                                                                                     float
    SP7NIRT [1]_   139.99                                                                                                                                                                                                                                                                                        float
    MINTFRAC [1]_  0.9                                                                                                                                                                                                                                                                                           float
    USESPLIT [1]_  T                                                                                                                                                                                                                                                                                             bool
    SP9BLUT [1]_   163.02                                                                                                                                                                                                                                                                                        float
    SP8NIRT [1]_   139.96                                                                                                                                                                                                                                                                                        float
    SP0BLUP [1]_   7.565e-08                                                                                                                                                                                                                                                                                     float
    SP5REDT [1]_   139.99                                                                                                                                                                                                                                                                                        float
    SP3NIRP [1]_   3.653e-08                                                                                                                                                                                                                                                                                     float
    SP8REDT [1]_   139.99                                                                                                                                                                                                                                                                                        float
    NTSSURVY [1]_  sv3                                                                                                                                                                                                                                                                                           str
    TCSGDEC [1]_   0.3                                                                                                                                                                                                                                                                                           float
    SP7NIRP [1]_   1.329e-07                                                                                                                                                                                                                                                                                     float
    SP3BLUP [1]_   7.078e-08                                                                                                                                                                                                                                                                                     float
    SP0NIRT [1]_   139.96                                                                                                                                                                                                                                                                                        float
    PMSEEING [1]_  2.33                                                                                                                                                                                                                                                                                          float
    PMTRANS [1]_   108.64                                                                                                                                                                                                                                                                                        float
    SEQTOT [1]_    2                                                                                                                                                                                                                                                                                             int
    SEQID [1]_     2 requests                                                                                                                                                                                                                                                                                    str
    SCSTD [1]_     STD_WD,STD_BRIGHT                                                                                                                                                                                                                                                                             str
    TARG2 [1]_     DESIROOT/target/catalogs/gaiadr2/0.50.0/targets/sv1/resolve/supp                                                                                                                                                                                                                              str
    SIMGFAQ [1]_   F                                                                                                                                                                                                                                                                                             bool
    USESPLITS [1]_ T                                                                                                                                                                                                                                                                                             bool
    TRANSPAR [1]_  74.6046588181844                                                                                                                                                                                                                                                                              float
    TOO [1]_       /data/afternoon_planning/surveyops/trunk/mtl/sv3/ToO/ToO.ecsv                                                                                                                                                                                                                                 str
    SLEWANGL [1]_  0.13                                                                                                                                                                                                                                                                                          float
    CONVERGD [1]_  F                                                                                                                                                                                                                                                                                             bool
    POSCVFRC [1]_  0.4153                                                                                                                                                                                                                                                                                        float
    FASCRIPT [1]_  /software/datasystems/desiconda/20200924/code/fiberassign/2.5.0/bin/fba_launch                                                                                                                                                                                                                str
    SVNDM [1]_     136362                                                                                                                                                                                                                                                                                        str
    SVNMTL [1]_    476                                                                                                                                                                                                                                                                                           str
    ETCVERS [1]_   0.1.12-3-g12b54bb                                                                                                                                                                                                                                                                             str
    MAXTIME [1]_   5400.0                                                                                                                                                                                                                                                                                        float
    MINTIME [1]_   60.0                                                                                                                                                                                                                                                                                          float
    ETCTEFF [1]_   68.498291                                                                                                                                                                                                                                                                                     float
    ESTTIME [1]_   1088.936                                                                                                                                                                                                                                                                                      float
    NTSPROG [1]_   BACKUP                                                                                                                                                                                                                                                                                        str
    ACQFWHM [1]_   1.080625                                                                                                                                                                                                                                                                                      float
    PMTRANSP [1]_  96.38                                                                                                                                                                                                                                                                                         float
    ETCFRACE [1]_  0.460059                                                                                                                                                                                                                                                                                      float
    ETCTRANS [1]_  0.931484                                                                                                                                                                                                                                                                                      float
    ETCREAL [1]_   145.539062                                                                                                                                                                                                                                                                                    float
    ETCSPLIT [1]_  1                                                                                                                                                                                                                                                                                             int
    ETCTHRUP [1]_  1.079734                                                                                                                                                                                                                                                                                      float
    ETCSKY [1]_    1.606062                                                                                                                                                                                                                                                                                      float
    ETCSEENG [1]_  1.0806                                                                                                                                                                                                                                                                                        float
    ETCPROF [1]_   PSF                                                                                                                                                                                                                                                                                           str
    ETCFRACB [1]_  0.204095                                                                                                                                                                                                                                                                                      float
    ETCFRACP [1]_  0.651421                                                                                                                                                                                                                                                                                      float
    ETCTHRUB [1]_  1.001377                                                                                                                                                                                                                                                                                      float
    ETCPREV [1]_   0.0                                                                                                                                                                                                                                                                                           float
    ETCTHRUE [1]_  1.039635                                                                                                                                                                                                                                                                                      float
    SHFTFOCS [1]_  220.0                                                                                                                                                                                                                                                                                         float
    TARG3 [1]_     DESIROOT/target/catalogs/dr9/0.51.0/targets/sv1/resolve/bright                                                                                                                                                                                                                                str
    ROLE [1]_      GUIDERMAN                                                                                                                                                                                                                                                                                     str
    DR [1]_        dr9                                                                                                                                                                                                                                                                                           str
    PRIORITY [1]_  default                                                                                                                                                                                                                                                                                       str
    DTVER [1]_     0.50.0                                                                                                                                                                                                                                                                                        str
    M31CEN [1]_    n                                                                                                                                                                                                                                                                                             str
    ============== ============================================================================================================================================================================================================================================================================================= ======= ==============================================

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
SV1_DESI_TARGET [1]_  int64
SV1_BGS_TARGET [1]_   int64
SV1_MWS_TARGET [1]_   int64
SV1_SCND_TARGET [1]_  int64
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
PSF_TO_FIBER_SPECFLUX float64
SV3_MWS_TARGET [1]_   int64
SV3_SCND_TARGET [1]_  int64
SV3_DESI_TARGET [1]_  int64
SV3_BGS_TARGET [1]_   int64
SV2_DESI_TARGET [1]_  int64
SV2_BGS_TARGET [1]_   int64
SV2_MWS_TARGET [1]_   int64
SV2_SCND_TARGET [1]_  int64
CMX_TARGET [1]_       int64
===================== ======= ===== ==============================

.. [1] Optional

HDU6
----

EXTNAME = CHI2PIX

:math:`chi^2` of PSF fit to CCD data per flux bin.  Large values indicate poor fits,
*e.g.* due to unmasked cosmics or other CCD defects.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2881             int  Number of wavelengths
    NAXIS2   500              int  Number of spectra
    CHECKSUM cBAJe94GcAAGc93G str  HDU checksum updated 2021-07-16T15:54:42
    DATASUM  3947425746       str  data unit checksum updated 2021-07-16T15:54:42
    ======== ================ ==== ==============================================

Data: FITS image [float32, 2881x500]

HDU7
----

EXTNAME = SCORES

Scores / metrics measured from the spectra for use in QA and systematics
studies.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   160              int  length of dimension 1
    NAXIS2   500              int  length of dimension 2
    CHECKSUM YanYbZkXZakXaYkX str  HDU checksum updated 2021-07-16T15:54:42
    DATASUM  3675881366       str  data unit checksum updated 2021-07-16T15:54:42
    ======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Although all of the columns below are marked as optional, each file will
have the complete set of ``_C`` columns where ``_C`` (for camera) represents
``_B``, ``_R``, or ``_Z``. These are designed such that the
SCORES tables from individual frames can be later combined into a summary
table for the exposure.

TODO: document wavelength ranges covered per camera.

.. rst-class:: columns

========================== ======= ===== ============================================
Name                       Type    Units Description
========================== ======= ===== ============================================
SUM_RAW_COUNT_Z [1]_       float64       sum counts in wave. range 7600,9800A
MEDIAN_RAW_COUNT_Z [1]_    float64       median counts/A in wave. range 7600,9800A
MEDIAN_RAW_SNR_Z [1]_      float64       median SNR/sqrt(A) in wave. range 7600,9800A
SUM_FFLAT_COUNT_Z [1]_     float64       sum counts in wave. range 7600,9800A
MEDIAN_FFLAT_COUNT_Z [1]_  float64       median counts/A in wave. range 7600,9800A
MEDIAN_FFLAT_SNR_Z [1]_    float64       median SNR/sqrt(A) in wave. range 7600,9800A
SUM_SKYSUB_COUNT_Z [1]_    float64       sum counts in wave. range 7600,9800A
MEDIAN_SKYSUB_COUNT_Z [1]_ float64       median counts/A in wave. range 7600,9800A
MEDIAN_SKYSUB_SNR_Z [1]_   float64       median SNR/sqrt(A) in wave. range 7600,9800A
SUM_CALIB_COUNT_Z [1]_     float64       sum counts in wave. range 7600,9800A
MEDIAN_CALIB_COUNT_Z [1]_  float64       median counts/A in wave. range 7600,9800A
MEDIAN_CALIB_SNR_Z [1]_    float64       median SNR/sqrt(A) in wave. range 7600,9800A
TSNR2_GPBDARK_Z [1]_       float64       from calc_frame_tsnr
TSNR2_ELG_Z [1]_           float64       from calc_frame_tsnr
TSNR2_GPBBRIGHT_Z [1]_     float64       from calc_frame_tsnr
TSNR2_LYA_Z [1]_           float64       from calc_frame_tsnr
TSNR2_BGS_Z [1]_           float64       from calc_frame_tsnr
TSNR2_GPBBACKUP_Z [1]_     float64       from calc_frame_tsnr
TSNR2_QSO_Z [1]_           float64       from calc_frame_tsnr
TSNR2_LRG_Z [1]_           float64       from calc_frame_tsnr
TSNR2_LRG_B [1]_           float64       from calc_frame_tsnr
TSNR2_GPBDARK_B [1]_       float64       from calc_frame_tsnr
MEDIAN_SKYSUB_SNR_B [1]_   float64       median SNR/sqrt(A) in wave. range 4000,5800A
MEDIAN_FFLAT_SNR_B [1]_    float64       median SNR/sqrt(A) in wave. range 4000,5800A
TSNR2_ELG_B [1]_           float64       from calc_frame_tsnr
TSNR2_BGS_B [1]_           float64       from calc_frame_tsnr
MEDIAN_CALIB_SNR_B [1]_    float64       median SNR/sqrt(A) in wave. range 4000,5800A
MEDIAN_FFLAT_COUNT_B [1]_  float64       median counts/A in wave. range 4000,5800A
TSNR2_QSO_B [1]_           float64       from calc_frame_tsnr
MEDIAN_SKYSUB_COUNT_B [1]_ float64       median counts/A in wave. range 4000,5800A
MEDIAN_RAW_COUNT_B [1]_    float64       median counts/A in wave. range 4000,5800A
TSNR2_GPBBRIGHT_B [1]_     float64       from calc_frame_tsnr
TSNR2_LYA_B [1]_           float64       from calc_frame_tsnr
SUM_SKYSUB_COUNT_B [1]_    float64       sum counts in wave. range 4000,5800A
MEDIAN_CALIB_COUNT_B [1]_  float64       median counts/A in wave. range 4000,5800A
TSNR2_GPBBACKUP_B [1]_     float64       from calc_frame_tsnr
SUM_FFLAT_COUNT_B [1]_     float64       sum counts in wave. range 4000,5800A
SUM_RAW_COUNT_B [1]_       float64       sum counts in wave. range 4000,5800A
SUM_CALIB_COUNT_B [1]_     float64       sum counts in wave. range 4000,5800A
MEDIAN_RAW_SNR_B [1]_      float64       median SNR/sqrt(A) in wave. range 4000,5800A
SUM_CALIB_COUNT_R [1]_     float64       sum counts in wave. range 5800,7600A
MEDIAN_RAW_COUNT_R [1]_    float64       median counts/A in wave. range 5800,7600A
TSNR2_QSO_R [1]_           float64       from calc_frame_tsnr
TSNR2_LRG_R [1]_           float64       from calc_frame_tsnr
TSNR2_LYA_R [1]_           float64       from calc_frame_tsnr
TSNR2_GPBBRIGHT_R [1]_     float64       from calc_frame_tsnr
SUM_SKYSUB_COUNT_R [1]_    float64       sum counts in wave. range 5800,7600A
SUM_RAW_COUNT_R [1]_       float64       sum counts in wave. range 5800,7600A
SUM_FFLAT_COUNT_R [1]_     float64       sum counts in wave. range 5800,7600A
MEDIAN_FFLAT_SNR_R [1]_    float64       median SNR/sqrt(A) in wave. range 5800,7600A
TSNR2_BGS_R [1]_           float64       from calc_frame_tsnr
TSNR2_GPBBACKUP_R [1]_     float64       from calc_frame_tsnr
MEDIAN_SKYSUB_SNR_R [1]_   float64       median SNR/sqrt(A) in wave. range 5800,7600A
MEDIAN_CALIB_SNR_R [1]_    float64       median SNR/sqrt(A) in wave. range 5800,7600A
MEDIAN_FFLAT_COUNT_R [1]_  float64       median counts/A in wave. range 5800,7600A
MEDIAN_RAW_SNR_R [1]_      float64       median SNR/sqrt(A) in wave. range 5800,7600A
MEDIAN_SKYSUB_COUNT_R [1]_ float64       median counts/A in wave. range 5800,7600A
MEDIAN_CALIB_COUNT_R [1]_  float64       median counts/A in wave. range 5800,7600A
TSNR2_GPBDARK_R [1]_       float64       from calc_frame_tsnr
TSNR2_ELG_R [1]_           float64       from calc_frame_tsnr
========================== ======= ===== ============================================

Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
