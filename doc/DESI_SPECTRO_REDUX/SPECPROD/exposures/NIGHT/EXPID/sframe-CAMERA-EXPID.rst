========================
sframe-CAMERA-EXPID.fits
========================

:Summary: fiber-flatfielded and sky-subtracted but not flux calibrated
          per-camera spectra.
:Naming Convention: ``sframe-{CAMERA}-{EXPID}.fits``, where ``{CAMERA}`` is
    one of the spectrograph cameras (*e.g.* ``z1``) and ``{EXPID}``
    is the 8-digit exposure ID.
:Regex: ``sframe-[brz][0-9]-[0-9]{8}\.fits``
:File Type: FITS, 70 MB

Contents
========

====== ========== ======== ===================
Number EXTNAME    Type     Contents
====== ========== ======== ===================
HDU0_  FLUX       IMAGE    flatfielded sky subtracted photons
HDU1_  IVAR       IMAGE    Inverse variance of FLUX
HDU2_  MASK       IMAGE    Bad value mask; 0=good
HDU3_  WAVELENGTH IMAGE    Wavelength grid of the extraction
HDU3_  RESOLUTION IMAGE    Resolution matrix
HDU5_  FIBERMAP   BINTABLE Fibermap
HDU6_  CHI2PIX    IMAGE    chi2 of PSF fit to CCD pixels
HDU7_  SCORES     BINTABLE Quality Assurance scores
====== ========== ======== ===================

FITS Header Units
=================

HDU0
----

EXTNAME = FLUX

2D array of fiber flat-fielded and sky subtracted flux of dimension [nspec, nwave] in units of electrons per Angstrom. nspec is the number of fibers per camera. nwave in the length of the wavelength array. The spectra of all fibers share the same
wavelength grid (given in HDU WAVELENGTH). sframe.flux = frame.flux / flatfield - sky .

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
    OPENSHUT       2020-12-21T02:36:32.099838                                            str     Time shutter opened
    ST             01:10:39.210                                                          str     Local Sidereal time at observation start (HH:MM
    EXPTIME        300.007                                                               float   [s] Actual exposure time
    REQRA          356.0                                                                 float   [deg] Requested right ascension (observer input
    REQDEC         29.0                                                                  float   [deg] Requested declination (observer input)
    FOCUS          1426.5,-501.4,81.0,-2.6,42.3,169.2                                    str     Telescope focus settings
    VCCD           ON                                                                    str     True (ON) if CCD voltage is on
    VCCDON         2020-12-14T17:48:28.296248                                            str     Time when CCD voltage was turned on
    VCCDSEC        550592.7                                                              float   [s] CCD on time in seconds
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
    SPECGRPH       3                                                                     int     Spectrograph logical name (SP)
    SPECID         6                                                                     int     Spectrograph serial number (SM)
    FEEBOX         lbnl074                                                               str     CCD Controller serial number
    VESSEL         11                                                                    int     Cryostat serial number
    FEEVER         v20160312                                                             str     CCD Controller version
    FEEPOWER       ON                                                                    str     FEE power status
    FEEDMASK       2134851391                                                            int     FEE dac mask
    FEECMASK       1048575                                                               int     FEE clk mask
    CCDTEMP        -140.2798                                                             float   [deg C] CCD controller CCD temperature
    RADESYS        FK5                                                                   str     Coordinate reference frame of major/minor axes
    FILENAME       /exposures/desi/specs/20201220/00069022/sp1-00069022.fits.fz          str     Name
    DOSVER         trunk                                                                 str     DOS software version
    OCSVER         1.2                                                                   float   OCS software version
    CONSTVER       DESI:CURRENT                                                          str     Constants version
    INIFILE        /data/msdos/dos_home/architectures/kpno/desi.ini                      str     DOS Configuration
    CRYOPRES [1]_  7.233e-08                                                             str     [mb] Cryostat pressure (IP)
    CLOCK7         -2.0001,3.9999                                                        str     [V] high rail, low rail
    TRIMSECA       [8:2064, 2:2065]                                                      str     Trim section for quadrant A
    CCDNAME        CCDSM6R                                                               str     CCD name
    TRIMSECD       [2193:4249, 2130:4193]                                                str     Trim section for quadrant D
    OFFSET2        0.4000000059604645,-8.961                                             str     [V] set value, measured value
    CPUTEMP        56.625                                                                float   [deg C] CCD controller CPU temperature
    DAC11          -25.0003,-24.7086                                                     str     [V] set value, measured value
    AMPSECA        [1:2057, 1:2064]                                                      str     AMP section for quadrant A
    CCDCFG         M1-50_lbnl_20190719.cfg                                               str     CCD configuration file
    TRIMSECB       [2193:4249, 2:2065]                                                   str     Trim section for quadrant B
    CLOCK3         -2.0001,3.9999                                                        str     [V] high rail, low rail
    CCDSECA        [1:2057, 1:2064]                                                      str     CCD section for quadrant A
    CLOCK4         9.9999,0.0                                                            str     [V] high rail, low rail
    DAC0           -9.0002,-8.9095                                                       str     [V] set value, measured value
    CLOCK10        9.9992,2.9993                                                         str     [V] high rail, low rail
    BIASSECA       [2065:2128, 2:2065]                                                   str     Bias section for quadrant A
    PRRSECA        [8:2064, 1:1]                                                         str     Row prescan section for quadrant A
    DAC7           6.4999,6.4856                                                         str     [V] set value, measured value
    AMPSECB        [4114:2058, 1:2064]                                                   str     AMP section for quadrant B
    DAC10          -25.0003,-24.9906                                                     str     [V] set value, measured value
    DELAYS         20, 20, 25, 30, 7, 3000, 7, 7, 7, 7                                   str     [10] Delay settings
    CCDSECD        [2058:4114, 2065:4128]                                                str     CCD section for quadrant D
    CASETEMP       56.4919                                                               float   [deg C] CCD controller case temperature
    CLOCK6         9.9999,0.0                                                            str     [V] high rail, low rail
    CLOCK13        9.9992,2.9993                                                         str     [V] high rail, low rail
    CLOCK9         9.9992,2.9993                                                         str     [V] high rail, low rail
    DAC8           -25.0003,-25.0202                                                     str     [V] set value, measured value
    DAC9           -25.0003,-24.6789                                                     str     [V] set value, measured value
    ORSECB         [2193:4249, 2066:2097]                                                str     Row overscan section for quadrant B
    CLOCK1         9.9999,0.0                                                            str     [V] high rail, low rail
    DETSECC        [1:2057, 2065:4128]                                                   str     Detector section for quadrant C
    AMPSECD        [4114:2058, 4128:2065]                                                str     AMP section for quadrant D
    CLOCK5         9.9999,0.0                                                            str     [V] high rail, low rail
    ORSECA         [8:2064, 2066:2097]                                                   str     Row overscan section for quadrant A
    DAC15          0.0,0.0297                                                            str     [V] set value, measured value
    DATASECA       [8:2064, 2:2065]                                                      str     Data section for quadrant A
    CCDPREP        purge,clear                                                           str     CCD prep actions
    OFFSET7        2.0,6.4908                                                            str     [V] set value, measured value
    DAC5           5.9998,6.028                                                          str     [V] set value, measured value
    CLOCK12        9.9992,2.9993                                                         str     [V] high rail, low rail
    CCDSECB        [2058:4114, 1:2064]                                                   str     CCD section for quadrant B
    OFFSET6        2.0,6.0332                                                            str     [V] set value, measured value
    DAC4           5.9998,6.028                                                          str     [V] set value, measured value
    PRESECC        [1:7, 2130:4193]                                                      str     Prescan section for quadrant C
    OFFSET5        2.0,6.028                                                             str     [V] set value, measured value
    DAC2           -9.0002,-8.9713                                                       str     [V] set value, measured value
    CRYOTEMP [1]_  162.97                                                                float   [deg K] Cryostat CCD temperature
    PRESECB        [4250:4256, 2:2065]                                                   str     Prescan section for quadrant B
    DIGITIME       47.1031                                                               float   [s] Time to digitize image
    DAC3           -10.5005,-10.3824                                                     str     [V] set value, measured value
    CAMERA         r3                                                                    str     Camera name
    DETSECB        [2058:4114, 1:2064]                                                   str     Detector section for quadrant B
    OFFSET1        0.4000000059604645,-8.8065                                            str     [V] set value, measured value
    DATASECD       [2193:4249, 2130:4193]                                                str     Data section for quadrant D
    SETTINGS       detectors_sm_20191211.json                                            str     Name of DESI CCD settings file
    CLOCK11        9.9992,2.9993                                                         str     [V] high rail, low rail
    DAC13          0.0,0.0                                                               str     [V] set value, measured value
    CLOCK14        9.9992,2.9993                                                         str     [V] high rail, low rail
    CCDSECC        [1:2057, 2065:4128]                                                   str     CCD section for quadrant C
    DATASECC       [8:2064, 2130:4193]                                                   str     Data section for quadrant C
    CLOCK0         9.9999,0.0                                                            str     [V] high rail, low rail
    CLOCK15        9.9992,2.9993                                                         str     [V] high rail, low rail
    DAC12          0.0,0.0297                                                            str     [V] set value, measured value
    CCDSIZE        4194,4256                                                             str     CCD size in pixels (rows, columns)
    OFFSET0        0.4000000059604645,-8.9095                                            str     [V] set value, measured value
    ORSECD         [2193:4249, 2098:2129]                                                str     Row bias section for quadrant D
    DAC16          48.0,46.7082                                                          str     [V] set value, measured value
    PRRSECC        [8:2064, 4194:4194]                                                   str     Row prescan section for quadrant C
    PRRSECD        [2193:4249, 4194:4194]                                                str     Row prescan section for quadrant D
    BIASSECB       [2129:2192, 2:2065]                                                   str     Bias section for quadrant B
    DETSECD        [2058:4114, 2065:4128]                                                str     Detector section for quadrant D
    CLOCK18        9.0,0.9999                                                            str     [V] high rail, low rail
    DAC17          20.0008,14.274                                                        str     [V] set value, measured value
    CCDTMING       default_lbnl_timing_20180905.txt                                      str     CCD timing file
    DETECTOR       M1-50                                                                 str     Detector (ccd) identification
    PRRSECB        [2193:4249, 1:1]                                                      str     Row prescan section for quadrant B
    TRIMSECC       [8:2064, 2130:4193]                                                   str     Trim section for quadrant C
    DAC14          0.0,0.0148                                                            str     [V] set value, measured value
    BIASSECD       [2129:2192, 2130:4193]                                                str     Bias section for quadrant D
    CDSPARMS       400, 400, 8, 2000                                                     str     CDS parameters
    OFFSET3        0.4000000059604645,-10.3721                                           str     [V] set value, measured value
    PRESECA        [1:7, 2:2065]                                                         str     Prescan section for quadrant A
    ORSECC         [8:2064, 2098:2129]                                                   str     Row overscan section for quadrant C
    DAC6           5.9998,6.0332                                                         str     [V] set value, measured value
    PGAGAIN        3                                                                     int     Controller gain
    DAC1           -9.0002,-8.8065                                                       str     [V] set value, measured value
    DATASECB       [2193:4249, 2:2065]                                                   str     Data section for quadrant B
    CLOCK2         9.9999,0.0                                                            str     [V] high rail, low rail
    CLOCK16        9.9999,3.0                                                            str     [V] high rail, low rail
    PRESECD        [4250:4256, 2130:4193]                                                str     Prescan section for quadrant D
    OFFSET4        2.0,6.0332                                                            str     [V] set value, measured value
    CLOCK17        9.0,0.9999                                                            str     [V] high rail, low rail
    AMPSECC        [1:2057, 4128:2065]                                                   str     AMP section for quadrant C
    CLOCK8         9.9992,2.9993                                                         str     [V] high rail, low rail
    DETSECA        [1:2057, 1:2064]                                                      str     Detector section for quadrant A
    BIASSECC       [2065:2128, 2130:4193]                                                str     Bias section for quadrant C
    BLDTIME        0.3504                                                                float   [s] Time to build image
    REQTIME        300.0                                                                 float   [s] Requested exposure time
    OBSID          kp4m20201221t023911                                                   str     Unique observation identifier
    PROCTYPE       RAW                                                                   str     Data processing level
    PRODTYPE       image                                                                 str     Data product type
    CHECKSUM       jjGAmi92jiE8ji98                                                      str     HDU checksum updated 2022-02-14T06:14:04
    DATASUM        3075256975                                                            str     data unit checksum updated 2022-02-14T06:14:04
    GAINA          1.681                                                                 float   e/ADU (gain applied to image)
    SATULEVA       28000.0                                                               float   saturation or non lin. level, in ADU, inc. bias
    OSTEPA         0.7048677125421818                                                    float   ADUs (max-min of median overscan per row)
    OMETHA         AVERAGE                                                               str     use average overscan
    OVERSCNA       1979.586454500641                                                     float   ADUs (gain not applied)
    OBSRDNA        2.618213792981265                                                     float   electrons (gain is applied)
    SATUELEA       43740.31516998442                                                     float   saturation or non lin. level, in electrons
    GAINB          1.625                                                                 float   e/ADU (gain applied to image)
    SATULEVB       57000.0                                                               float   saturation or non lin. level, in ADU, inc. bias
    OSTEPB         0.6850349189899134                                                    float   ADUs (max-min of median overscan per row)
    OMETHB         AVERAGE                                                               str     use average overscan
    OVERSCNB       1997.289875350671                                                     float   ADUs (gain not applied)
    OBSRDNB        3.12518985733541                                                      float   electrons (gain is applied)
    SATUELEB       89379.40395255515                                                     float   saturation or non lin. level, in electrons
    GAINC          1.477                                                                 float   e/ADU (gain applied to image)
    SATULEVC       59000.0                                                               float   saturation or non lin. level, in ADU, inc. bias
    OSTEPC         0.6403308619337622                                                    float   ADUs (max-min of median overscan per row)
    OMETHC         AVERAGE                                                               str     use average overscan
    OVERSCNC       1974.691977751432                                                     float   ADUs (gain not applied)
    OBSRDNC        2.344388520757958                                                     float   electrons (gain is applied)
    SATUELEC       84226.37994886114                                                     float   saturation or non lin. level, in electrons
    GAIND          1.492                                                                 float   e/ADU (gain applied to image)
    SATULEVD       62000.0                                                               float   saturation or non lin. level, in ADU, inc. bias
    OSTEPD         0.6246898852550657                                                    float   ADUs (max-min of median overscan per row)
    OMETHD         AVERAGE                                                               str     use average overscan
    OVERSCND       1998.214476179268                                                     float   ADUs (gain not applied)
    OBSRDND        2.301320302261815                                                     float   electrons (gain is applied)
    SATUELED       89522.66400154053                                                     float   saturation or non lin. level, in electrons
    FIBERMIN       1500                                                                  int
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
    ACQTIME        15.0                                                                  float   [s] acqusition image exposure time
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
    IN_PSF         SPECPROD/exposures/20201220/00069022/psf-r3-00069022.fits             str     Input sp
    IN_IMG         SPECPROD/preproc/20201220/00069022/preproc-r3-00069022.fits           str
    ORIG_PSF       SPECPROD/calibnight/20201220/psfnight-r3-20201220.fits                str
    BUNIT          electron/Angstrom                                                     str
    IN_SKY         SPECPROD/exposures/20201220/00069022/sky-r3-00069022.fits             str
    FIBERFLT       SPECPROD/exposures/20201220/00069022/fiberflatexp-r3-00069022.fits    str
    SP6BLUP [1]_   7.899e-08                                                             float   [mb] SP6 blue pressure
    TCSMFDEC [1]_  1                                                                     int     TCS moving filter length (dec)
    SLEWANGL [1]_  15.646                                                                float   [deg] Slew Angle
    SEQTOT [1]_    2                                                                     int     Total number of exposures in sequence
    MOONSEP [1]_   111.881                                                               float   [deg] Moon Separation
    SP5REDP [1]_   9.742e-08                                                             float   [mb] SP5 red pressure
    SEQSTART [1]_  2021-05-08T10:26:00.785886                                            str     Start time of sequence processing
    CONVERGD [1]_  F                                                                     bool    Positioning loop converged (CNFRC&gt;0.95)
    SP9NIRP [1]_   5.455e-08                                                             float   [mb] SP9 NIR pressure
    SP3REDP [1]_   5.899e-08                                                             float   [mb] SP3 red pressure
    SP1BLUT [1]_   162.97                                                                float   [K] SP1 blue temperature
    SP0BLUT [1]_   162.97                                                                float   [K] SP0 blue temperature
    SP8REDT [1]_   139.99                                                                float   [K] SP8 red temperature
    SP3BLUP [1]_   7.952e-08                                                             float   [mb] SP3 blue pressure
    SP9REDT [1]_   139.99                                                                float   [K] SP9 red temperature
    SP4NIRP [1]_   7.251e-08                                                             float   [mb] SP4 NIR pressure
    SP4REDP [1]_   5.049e-08                                                             float   [mb] SP4 red pressure
    PMSEEING [1]_  0.93                                                                  float   [arcsec] PlateMaker GFAPROC seeing
    SP1NIRP [1]_   6.18e-08                                                              float   [mb] SP1 NIR pressure
    SP2REDT [1]_   139.99                                                                float   [K] SP2 red temperature
    SP5REDT [1]_   140.06                                                                float   [K] SP5 red temperature
    SP4NIRT [1]_   139.99                                                                float   [K] SP4 NIR temperature
    SP7BLUT [1]_   162.99                                                                float   [K] SP7 blue temperature
    USESPLIT [1]_  T                                                                     bool    Exposure splits are allowed
    SP1BLUP [1]_   7.999e-08                                                             float   [mb] SP1 blue pressure
    SP1NIRT [1]_   139.96                                                                float   [K] SP1 NIR temperature
    SP1REDT [1]_   139.99                                                                float   [K] SP1 red temperature
    SP8REDP [1]_   3.96e-08                                                              float   [mb] SP8 red pressure
    SP5BLUT [1]_   163.02                                                                float   [K] SP5 blue temperature
    TCSGRA [1]_    0.3                                                                   float   TCS simple gain (RA)
    SUNDEC [1]_    17.206123                                                             float   [deg] Sun declination at start of exposure
    SP7NIRP [1]_   4.416e-08                                                             float   [mb] SP7 NIR pressure
    PMTRANS [1]_   95.5                                                                  float   [%] PlateMaker GFAPROC transparency
    SP0NIRT [1]_   139.99                                                                float   [K] SP0 NIR temperature
    SP5NIRP [1]_   6.573e-08                                                             float   [mb] SP5 NIR pressure
    POSCVFRC [1]_  0.3845                                                                float   Fraction of converged positioners
    SP7BLUP [1]_   1.04e-07                                                              float   [mb] SP7 blue pressure
    NTSSURVY [1]_  na                                                                    Unknown NTS survey name
    SP7REDT [1]_   139.99                                                                float   [K] SP7 red temperature
    SP2REDP [1]_   6.15e-08                                                              float   [mb] SP2 red pressure
    SP4REDT [1]_   140.06                                                                float   [K] SP4 red temperature
    SP6BLUT [1]_   162.97                                                                float   [K] SP6 blue temperature
    SP7REDP [1]_   3.404e-08                                                             float   [mb] SP7 red pressure
    SP8NIRP [1]_   4.941e-08                                                             float   [mb] SP8 NIR pressure
    SP9REDP [1]_   5.113e-08                                                             float   [mb] SP9 red pressure
    SP8NIRT [1]_   139.99                                                                float   [K] SP8 NIR temperature
    TCSKRA [1]_    0.3 0.003 0.00003                                                     str     TCS Kalman (RA)
    TCSMFRA [1]_   1                                                                     int     TCS moving filter length (RA)
    SP0BLUP [1]_   7.565e-08                                                             float   [mb] SP0 blue pressure
    SP3NIRP [1]_   4.105e-08                                                             float   [mb] SP3 NIR pressure
    SP1REDP [1]_   7.239e-08                                                             float   [mb] SP1 red pressure
    SP4BLUP [1]_   6.689e-08                                                             float   [mb] SP4 blue pressure
    SP3NIRT [1]_   140.01                                                                float   [K] SP3 NIR temperature
    SP8BLUP [1]_   8.311e-08                                                             float   [mb] SP8 blue pressure
    SP0REDT [1]_   139.99                                                                float   [K] SP0 red temperature
    SEQID [1]_     2 requests                                                            str     Exposure sequence identifier
    SP2BLUP [1]_   8.297e-08                                                             float   [mb] SP2 blue pressure
    SP2BLUT [1]_   163.02                                                                float   [K] SP2 blue temperature
    FRAMES [1]_    47                                                                    int     Number of Frames in Archive
    SP2NIRP [1]_   4.884e-08                                                             float   [mb] SP2 NIR pressure
    SP9BLUP [1]_   1.237e-07                                                             float   [mb] SP9 blue pressure
    TCSGDEC [1]_   0.3                                                                   float   TCS simple gain (dec)
    SP8BLUT [1]_   162.97                                                                float   [K] SP8 blue temperature
    SP9BLUT [1]_   162.97                                                                float   [K] SP9 blue temperature
    SP4BLUT [1]_   162.97                                                                float   [K] SP4 blue temperature
    TCSPIDEC [1]_  1.0,0.0,0.0,0.0                                                       str     TCS PI settings (P, I (gain, error window, satu
    SP3REDT [1]_   139.99                                                                float   [K] SP3 red temperature
    SP6NIRT [1]_   139.99                                                                float   [K] SP6 NIR temperature
    SP6REDT [1]_   139.99                                                                float   [K] SP6 red temperature
    SP5NIRT [1]_   140.08                                                                float   [K] SP5 NIR temperature
    TCSKDEC [1]_   0.3 0.003 0.00003                                                     str     TCS Kalman (dec)
    SP0NIRP [1]_   7.886e-08                                                             float   [mb] SP0 NIR pressure
    VISITIDS [1]_  87615                                                                 str     List of expids for a visit (same tile)
    SP0REDP [1]_   4.265e-08                                                             float   [mb] SP0 red pressure
    SUNRA [1]_     45.595565                                                             float   [deg] Sun RA at start of exposure
    SP5BLUP [1]_   1.153e-07                                                             float   [mb] SP5 blue pressure
    SKYLEVEL [1]_  0.83                                                                  float   [counts?] ETC sky level
    SP2NIRT [1]_   139.99                                                                float   [K] SP2 NIR temperature
    SP6REDP [1]_   6.491e-08                                                             float   [mb] SP6 red pressure
    TCSPIRA [1]_   1.0,0.0,0.0,0.0                                                       str     TCS PI settings (P, I (gain, error window, satu
    SP7NIRT [1]_   139.99                                                                float   [K] SP7 NIR temperature
    SP9NIRT [1]_   139.99                                                                float   [K] SP9 NIR temperature
    SPLITEXP [1]_  F                                                                     bool    Split exposure part of a visit
    SP6NIRP [1]_   2.807e-07                                                             float   [mb] SP6 NIR pressure
    SP3BLUT [1]_   162.99                                                                float   [K] SP3 blue temperature
    SBPROF [1]_    ELG                                                                   str     Profile used by ETC
    TOTTEFF [1]_   1406.4226                                                             float   [s] Total effective exposure time for visit
    REQTEFF [1]_   1400.0                                                                int     [s] Requested effective exposure time
    ACTTEFF [1]_   1406.4226                                                             float   [s] Actual effective exposure time
    BBKGMINB [1]_  -0.5249611468569187                                                   float
    BBKGMAXA [1]_  1.179777031725897                                                     float
    BBKGMIND [1]_  -0.5599583904094981                                                   float
    BBKGMINA [1]_  -0.9489741260224904                                                   float
    BBKGMAXD [1]_  0.2726660093392476                                                    float
    BBKGMAXB [1]_  0.6927871978458614                                                    float
    SEEING [1]_    1.291                                                                 float   [arcsec] ETC seeing
    BBKGMAXC [1]_  1.270526827094756                                                     float
    BBKGMINC [1]_  -0.8627791108943093                                                   float
    USESPLITS [1]_ T                                                                     bool    Exposure splits are allowed
    ETCTHRUB [1]_  0.575924                                                              float   ETC averaged thruput (BGS profile)
    ACQFWHM [1]_   1.469225                                                              float   [arcsec] FWHM of guide star PSF in acquisition
    ESTTIME [1]_   1374.714                                                              float   [s] Estimated exposure time for visit (from ETC
    ETCSPLIT [1]_  1                                                                     int     ETC split sequence number for this visit
    ETCFRACE [1]_  0.302117                                                              float   ETC transparency weighted average of FFRAC (ELG
    ETCFRACP [1]_  0.392042                                                              float   ETC transparency weighted average of FFRAC (PSF
    ETCTHRUP [1]_  0.556996                                                              float   ETC averaged thruput (PSF profile)
    ETCPREV [1]_   0.0                                                                   float   [s] ETC cummulative t_eff for visit
    ETCTHRUE [1]_  0.585204                                                              float   ETC averaged thruput (ELG profile)
    ETCREAL [1]_   1120.375                                                              float   [s] ETC real open shutter time
    TRANSPAR [1]_  None                                                                  Unknown ETC/PM transparency
    PMTRANSP [1]_  101.86                                                                float   [%] PlateMaker GFAPROC transparency
    ETCPROF [1]_   BGS                                                                   str     ETC source brightness profile
    ETCVERS [1]_   0.1.12-3-g12b54bb                                                     str     ETC version
    ETCFRACB [1]_  0.136941                                                              float   ETC transparency weighted average of FFRAC (BGS
    ETCSKY [1]_    2.674912                                                              float   ETC averaged, normalized sky camera flux
    NTSPROG [1]_   BRIGHT                                                                str     NTS program name
    ETCTRANS [1]_  0.798438                                                              float   ETC averaged TRANSP normalized to 1
    ETCTEFF [1]_   223.989487                                                            float   [s] ETC effective exposure time
    ETCSEENG [1]_  1.4692                                                                float   [arcsec] ETC seeing
    MAXTIME [1]_   5400.0                                                                float   [s] Maximum exposure time for entire visit (fro
    MINTIME [1]_   120.0                                                                 float   [s] Minimum exposure time (from NTS, used by ET
    ============== ===================================================================== ======= ===============================================

Data: FITS image [float32, 2326x500]

HDU1
----

EXTNAME = IVAR

Inverse variance of the flux in HDU0. The unit is 1/(electrons/Angstrom)^2. The noise from neighboring spectral pixels is uncorrelated.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2326             int  Number of wavelengths
    NAXIS2   500              int  Number of spectra
    CHECKSUM 9UJ3CTG29TG2ATG2 str  HDU checksum updated 2021-07-08T15:52:36
    DATASUM  3074959512       str  data unit checksum updated 2021-07-08T15:52:36
    ======== ================ ==== ==============================================

Data: FITS image [float32, 2326x500]

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
    NAXIS1   2326             int  Number of wavelengths
    NAXIS2   500              int  Number of spectra
    BSCALE   1                int
    BZERO    2147483648       int
    CHECKSUM ZGp6dDn5ZDn5bDn5 str  HDU checksum updated 2021-07-08T15:52:36
    DATASUM  47035306         str  data unit checksum updated 2021-07-08T15:52:36
    ======== ================ ==== ==============================================

Data: FITS image [int32, 2326x500]

HDU3
----

EXTNAME = WAVELENGTH

1D array of wavelengths. See the frame :ref:`WAVELENGTH documentation <frame-hdu3-wavelength>` for more details.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2326             int  Number of wavelengths
    BUNIT    Angstrom         str
    CHECKSUM 9MZDCMZA9MZAAMZA str  HDU checksum updated 2021-07-08T15:52:37
    DATASUM  456732359        str  data unit checksum updated 2021-07-08T15:52:37
    ======== ================ ==== ==============================================

Data: FITS image [float64, 2326]

HDU4
----

EXTNAME = RESOLUTION

Resolution matrix stored as a 3D sparse matrix. the frame :ref:`RESOLUTION documentation <frame-hdu4-resolution>` for more details.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2326             int
    NAXIS2   11               int
    NAXIS3   500              int
    CHECKSUM LiPqNgMnLgMnLgMn str  HDU checksum updated 2021-07-08T15:52:39
    DATASUM  2191513558       str  data unit checksum updated 2021-07-08T15:52:39
    ======== ================ ==== ==============================================

Data: FITS image [float32, 2326x11x500]

HDU5
----

EXTNAME = FIBERMAP

Fibermap information combining fiberassign request with actual fiber locations. See also the :doc:`fibermap documentation </DESI_SPECTRO_REDUX/SPECPROD/preproc/NIGHT/EXPID/fibermap-EXPID>` page.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ============== ======================================================================================================================================================================================================== ======= ==============================================
    KEY            Example Value                                                                                                                                                                                            Type    Comment
    ============== ======================================================================================================================================================================================================== ======= ==============================================
    NAXIS1         385                                                                                                                                                                                                      int     length of dimension 1
    NAXIS2         500                                                                                                                                                                                                      int     length of dimension 2
    TILEID         80616                                                                                                                                                                                                    int
    TILERA         356.0                                                                                                                                                                                                    float
    TILEDEC        29.0                                                                                                                                                                                                     float
    FIELDROT       -0.00962199210064233                                                                                                                                                                                     float
    FA_PLAN        2022-07-01T00:00:00.000                                                                                                                                                                                  str
    FA_HA          0.0                                                                                                                                                                                                      float
    FA_RUN         2020-03-06T00:00:00                                                                                                                                                                                      str
    FA_M_GFA [1]_  0.4                                                                                                                                                                                                      float
    FA_M_PET [1]_  0.4                                                                                                                                                                                                      float
    FA_M_POS [1]_  0.05                                                                                                                                                                                                     float
    REQRA          356.0                                                                                                                                                                                                    float
    REQDEC         29.0                                                                                                                                                                                                     float
    FIELDNUM       0                                                                                                                                                                                                        int
    FA_VER         2.0.0.dev2618                                                                                                                                                                                            str
    FA_SURV        sv1                                                                                                                                                                                                      str
    LONGSTRN       OGIP 1.0                                                                                                                                                                                                 str
    GFA            /data/target/catalogs/dr9/0.47.0/gfas                                                                                                                                                                    str
    SKY            /data/target/catalogs/dr9/0.47.0/skies                                                                                                                                                                   str
    SKYSUPP        /data/target/catalogs/gaiadr2/0.47.0/skies-supp                                                                                                                                                          str
    TARG           /data/target/catalogs/dr9/0.47.0/targets/sv1/resolve/bright/                                                                                                                                             str
    FAFLAVOR       sv1bgsmws                                                                                                                                                                                                str
    FAOUTDIR       /software/datasystems/users/raichoor/fiberassign-test/desi-sv1-20201218/                                                                                                                                 str
    PMTIME [1]_    2020-12-18T00:00:00.000                                                                                                                                                                                  str
    RUNDATE        2020-03-06T00:00:00                                                                                                                                                                                      str
    SCTARG [1]_    STD_WD,BGS_ANY,MWS_ANY                                                                                                                                                                                   str
    OBSCON         DARK|GRAY|BRIGHT                                                                                                                                                                                         str
    MODULE         CI                                                                                                                                                                                                       str
    EXPID          69022                                                                                                                                                                                                    int
    EXPFRAME       0                                                                                                                                                                                                        int
    COSMSPLT       F                                                                                                                                                                                                        bool
    MAXSPLIT       0                                                                                                                                                                                                        int
    SPLITIDS [1]_  69022                                                                                                                                                                                                    str
    FIBASSGN       /data/tiles/SVN_tiles/080/fiberassign-080616.fits                                                                                                                                                        str
    FLAVOR         science                                                                                                                                                                                                  str
    OBSTYPE        SCIENCE                                                                                                                                                                                                  str
    SEQUENCE       DESI                                                                                                                                                                                                     str
    MANIFEST       F                                                                                                                                                                                                        bool
    OBJECT                                                                                                                                                                                                                  str
    PURPOSE        Commissioning                                                                                                                                                                                            str
    PROGRAM        SV1 BGS+MWS tile 80616                                                                                                                                                                                   str
    PROPID         2019B-5000                                                                                                                                                                                               str
    OBSERVER       DESIObserver                                                                                                                                                                                             str
    LEAD           RunManager                                                                                                                                                                                               str
    INSTRUME       DESI                                                                                                                                                                                                     str
    OBSERVAT       KPNO                                                                                                                                                                                                     str
    OBS-LAT        31.96403                                                                                                                                                                                                 str
    OBS-LONG       -111.59989                                                                                                                                                                                               str
    OBS-ELEV       2097.0                                                                                                                                                                                                   float
    TELESCOP       KPNO 4.0-m telescope                                                                                                                                                                                     str
    CORRCTOR       DESI Corrector                                                                                                                                                                                           str
    SEQNUM         1                                                                                                                                                                                                        int
    NIGHT          20201220                                                                                                                                                                                                 int
    TIMESYS        UTC                                                                                                                                                                                                      str
    DATE-OBS       2020-12-21T02:36:32.099838                                                                                                                                                                               str
    MJD-OBS        59204.10870486                                                                                                                                                                                           float
    OPENSHUT       2020-12-21T02:36:32.099838                                                                                                                                                                               str
    CAMSHUT        open                                                                                                                                                                                                     str
    ST             01:10:39.210                                                                                                                                                                                             str
    ACQTIME        15.0                                                                                                                                                                                                     float
    GUIDTIME       5.0                                                                                                                                                                                                      float
    FOCSTIME       60.0                                                                                                                                                                                                     float
    SKYTIME        60.0                                                                                                                                                                                                     float
    WHITESPT       F                                                                                                                                                                                                        bool
    ZENITH         F                                                                                                                                                                                                        bool
    SEANNEX        F                                                                                                                                                                                                        bool
    BEYONDP        F                                                                                                                                                                                                        bool
    FIDUCIAL       off                                                                                                                                                                                                      str
    BACKLIT        off                                                                                                                                                                                                      str
    AIRMASS        1.060311                                                                                                                                                                                                 float
    FOCUS          1426.5,-501.4,81.0,-2.6,42.3,169.2                                                                                                                                                                       str
    VCCD           ON                                                                                                                                                                                                       str
    TRUSTEMP       11.767                                                                                                                                                                                                   float
    PMIRTEMP       8.925                                                                                                                                                                                                    float
    PMREADY        T                                                                                                                                                                                                        bool
    PMCOVER        open                                                                                                                                                                                                     str
    PMCOOL         off                                                                                                                                                                                                      str
    DOMSHUTU       open                                                                                                                                                                                                     str
    DOMSHUTL       open                                                                                                                                                                                                     str
    DOMLIGHH       off                                                                                                                                                                                                      str
    DOMLIGHL       off                                                                                                                                                                                                      str
    DOMEAZ         255.166                                                                                                                                                                                                  float
    DOMINPOS       T                                                                                                                                                                                                        bool
    EQUINOX        2000.0                                                                                                                                                                                                   float
    GUIDOFFR       -0.052283                                                                                                                                                                                                float
    GUIDOFFD       0.136634                                                                                                                                                                                                 float
    MOONDEC        -8.975162                                                                                                                                                                                                float
    MOONRA         352.538429                                                                                                                                                                                               float
    MOUNTAZ        266.70224                                                                                                                                                                                                float
    MOUNTDEC       28.999221                                                                                                                                                                                                float
    MOUNTEL        71.039837                                                                                                                                                                                                float
    MOUNTHA        21.769281                                                                                                                                                                                                float
    INCTRL         T                                                                                                                                                                                                        bool
    INPOS          T                                                                                                                                                                                                        bool
    MNTOFFD        -15.76                                                                                                                                                                                                   float
    MNTOFFR        29.32                                                                                                                                                                                                    float
    PARALLAC       75.635085                                                                                                                                                                                                float
    SKYDEC         28.999221                                                                                                                                                                                                float
    SKYRA          355.996551                                                                                                                                                                                               float
    TARGTDEC       28.999221                                                                                                                                                                                                float
    TARGTRA        355.996551                                                                                                                                                                                               float
    TARGTAZ        267.074049                                                                                                                                                                                               float
    TARGTEL        70.563787                                                                                                                                                                                                float
    TRGTOFFD       0.0                                                                                                                                                                                                      float
    TRGTOFFR       0.0                                                                                                                                                                                                      float
    ZD             19.436213                                                                                                                                                                                                float
    TCSST          01:13:18.668                                                                                                                                                                                             str
    TCSMJD         59204.110981                                                                                                                                                                                             float
    USEETC         F                                                                                                                                                                                                        bool
    ACQCAM         GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                                                                                                                                                                str
    GUIDECAM       GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                                                                                                                                                                str
    FOCUSCAM       FOCUS1,FOCUS4,FOCUS6,FOCUS9                                                                                                                                                                              str
    SKYCAM         SKYCAM0,SKYCAM1                                                                                                                                                                                          str
    REQADC         65.78,85.28                                                                                                                                                                                              str
    ADCCORR        T                                                                                                                                                                                                        bool
    ADC1PHI        65.780005                                                                                                                                                                                                float
    ADC2PHI        85.279991                                                                                                                                                                                                float
    ADC1HOME       F                                                                                                                                                                                                        bool
    ADC2HOME       F                                                                                                                                                                                                        bool
    ADC1NREV       -1.0                                                                                                                                                                                                     float
    ADC2NREV       0.0                                                                                                                                                                                                      float
    ADC1STAT       STOPPED                                                                                                                                                                                                  str
    ADC2STAT       STOPPED                                                                                                                                                                                                  str
    USESKY         T                                                                                                                                                                                                        bool
    USEFOCUS       T                                                                                                                                                                                                        bool
    HEXPOS         1426.5,-501.3,81.0,-2.6,42.3,171.9                                                                                                                                                                       str
    HEXTRIM        0.0,0.0,0.0,0.0,0.0,0.0                                                                                                                                                                                  str
    USEROTAT       T                                                                                                                                                                                                        bool
    ROTOFFST       167.1                                                                                                                                                                                                    float
    ROTENBLD       T                                                                                                                                                                                                        bool
    ROTRATE        0.0                                                                                                                                                                                                      float
    RESETROT       F                                                                                                                                                                                                        bool
    USEPOS         T                                                                                                                                                                                                        bool
    PETALS         PETAL0,PETAL1,PETAL2,PETAL3,PETAL4,PETAL5,PETAL6,PETAL7,PETAL8,PETAL9                                                                                                                                    str
    POSCYCLE       1                                                                                                                                                                                                        int
    POSONTGT       3626                                                                                                                                                                                                     int
    POSONFRC       0.8613                                                                                                                                                                                                   float
    POSDISAB       37                                                                                                                                                                                                       int
    POSENABL       4210                                                                                                                                                                                                     int
    POSRMS         0.0171                                                                                                                                                                                                   float
    POSITER        1                                                                                                                                                                                                        int
    POSFRACT       0.95                                                                                                                                                                                                     float
    POSTOLER       0.01                                                                                                                                                                                                     float
    POSMVALL       T                                                                                                                                                                                                        bool
    USEGUIDR       T                                                                                                                                                                                                        bool
    GUIDMODE       catalog                                                                                                                                                                                                  str
    USEAOS [1]_    F                                                                                                                                                                                                        bool
    USEDONUT       T                                                                                                                                                                                                        bool
    USESPCTR       T                                                                                                                                                                                                        bool
    SPCGRPHS       SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                                                                                                                                                                  str
    ILLSPECS [1]_  SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                                                                                                                                                                  str
    CCDSPECS [1]_  SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                                                                                                                                                                  str
    TDEWPNT        -16.043                                                                                                                                                                                                  float
    TAIRFLOW       0.0                                                                                                                                                                                                      float
    TAIRITMP       11.8                                                                                                                                                                                                     float
    TAIROTMP       11.7                                                                                                                                                                                                     float
    TAIRTEMP       10.65                                                                                                                                                                                                    float
    TCASITMP       0.0                                                                                                                                                                                                      float
    TCASOTMP       10.8                                                                                                                                                                                                     float
    TCSITEMP       9.3                                                                                                                                                                                                      float
    TCSOTEMP       10.8                                                                                                                                                                                                     float
    TCIBTEMP       0.0                                                                                                                                                                                                      float
    TCIMTEMP       0.0                                                                                                                                                                                                      float
    TCITTEMP       0.0                                                                                                                                                                                                      float
    TCOSTEMP       0.0                                                                                                                                                                                                      float
    TCOWTEMP       0.0                                                                                                                                                                                                      float
    TDBTEMP        9.3                                                                                                                                                                                                      float
    TFLOWIN        0.0                                                                                                                                                                                                      float
    TFLOWOUT       0.0                                                                                                                                                                                                      float
    TGLYCOLI       9.9                                                                                                                                                                                                      float
    TGLYCOLO       9.8                                                                                                                                                                                                      float
    THINGES        11.4                                                                                                                                                                                                     float
    THINGEW        11.2                                                                                                                                                                                                     float
    TPMAVERT       8.931                                                                                                                                                                                                    float
    TPMDESIT       7.0                                                                                                                                                                                                      float
    TPMEIBT        8.6                                                                                                                                                                                                      float
    TPMEITT        8.6                                                                                                                                                                                                      float
    TPMEOBT        8.5                                                                                                                                                                                                      float
    TPMEOTT        9.0                                                                                                                                                                                                      float
    TPMNIBT        8.4                                                                                                                                                                                                      float
    TPMNITT        8.9                                                                                                                                                                                                      float
    TPMNOBT        8.8                                                                                                                                                                                                      float
    TPMNOTT        9.1                                                                                                                                                                                                      float
    TPMRTDT        9.0                                                                                                                                                                                                      float
    TPMSIBT        8.6                                                                                                                                                                                                      float
    TPMSITT        8.8                                                                                                                                                                                                      float
    TPMSOBT        8.2                                                                                                                                                                                                      float
    TPMSOTT        8.9                                                                                                                                                                                                      float
    TPMSTAT        ready                                                                                                                                                                                                    str
    TPMWIBT        8.2                                                                                                                                                                                                      float
    TPMWITT        9.1                                                                                                                                                                                                      float
    TPMWOBT        8.3                                                                                                                                                                                                      float
    TPMWOTT        8.9                                                                                                                                                                                                      float
    TPCITEMP       8.5                                                                                                                                                                                                      float
    TPCOTEMP       8.6                                                                                                                                                                                                      float
    TPR1HUM        0.0                                                                                                                                                                                                      float
    TPR1TEMP       0.0                                                                                                                                                                                                      float
    TPR2HUM        0.0                                                                                                                                                                                                      float
    TPR2TEMP       0.0                                                                                                                                                                                                      float
    TSERVO         40.0                                                                                                                                                                                                     float
    TTRSTEMP       11.4                                                                                                                                                                                                     float
    TTRWTEMP       11.0                                                                                                                                                                                                     float
    TTRUETBT       -4.2                                                                                                                                                                                                     float
    TTRUETTT       11.2                                                                                                                                                                                                     float
    TTRUNTBT       10.9                                                                                                                                                                                                     float
    TTRUNTTT       11.2                                                                                                                                                                                                     float
    TTRUSTBT       10.7                                                                                                                                                                                                     float
    TTRUSTST       10.8                                                                                                                                                                                                     float
    TTRUSTTT       11.1                                                                                                                                                                                                     float
    TTRUTSBT       11.8                                                                                                                                                                                                     float
    TTRUTSMT       11.8                                                                                                                                                                                                     float
    TTRUTSTT       11.8                                                                                                                                                                                                     float
    TTRUWTBT       10.5                                                                                                                                                                                                     float
    TTRUWTTT       10.9                                                                                                                                                                                                     float
    ALARM          F                                                                                                                                                                                                        bool
    ALARM-ON       F                                                                                                                                                                                                        bool
    BATTERY        100.0                                                                                                                                                                                                    float
    SECLEFT        5178.0                                                                                                                                                                                                   float
    UPSSTAT        System Normal - On Line(7)                                                                                                                                                                               str
    INAMPS         70.4                                                                                                                                                                                                     float
    OUTWATTS       5000.0,7200.0,4800.0                                                                                                                                                                                     str
    COMPDEW        -12.9                                                                                                                                                                                                    float
    COMPHUM        7.4                                                                                                                                                                                                      float
    COMPAMB        19.5                                                                                                                                                                                                     float
    COMPTEMP       24.5                                                                                                                                                                                                     float
    DEWPOINT       11.5                                                                                                                                                                                                     float
    HUMIDITY       10.0                                                                                                                                                                                                     float
    PRESSURE       795.0                                                                                                                                                                                                    float
    OUTTEMP        0.0                                                                                                                                                                                                      float
    WINDDIR        55.0                                                                                                                                                                                                     float
    WINDSPD        27.3                                                                                                                                                                                                     float
    GUST           20.6                                                                                                                                                                                                     float
    AMNIENTN       13.5                                                                                                                                                                                                     float
    CFLOOR         8.9                                                                                                                                                                                                      float
    NWALLIN        13.9                                                                                                                                                                                                     float
    NWALLOUT       9.6                                                                                                                                                                                                      float
    WWALLIN        12.9                                                                                                                                                                                                     float
    WWALLOUT       10.6                                                                                                                                                                                                     float
    AMBIENTS       14.8                                                                                                                                                                                                     float
    FLOOR          12.6                                                                                                                                                                                                     float
    EWALLCMP       10.8                                                                                                                                                                                                     float
    EWALLCOU       10.6                                                                                                                                                                                                     float
    ROOF           10.3                                                                                                                                                                                                     float
    ROOFAMB        10.6                                                                                                                                                                                                     float
    DOMEBLOW       10.4                                                                                                                                                                                                     float
    DOMEBUP        10.7                                                                                                                                                                                                     float
    DOMELLOW       10.8                                                                                                                                                                                                     float
    DOMELUP        10.8                                                                                                                                                                                                     float
    DOMERLOW       10.6                                                                                                                                                                                                     float
    DOMERUP        10.5                                                                                                                                                                                                     float
    PLATFORM       10.4                                                                                                                                                                                                     float
    SHACKC         14.4                                                                                                                                                                                                     float
    SHACKW         13.7                                                                                                                                                                                                     float
    STAIRSL        10.5                                                                                                                                                                                                     float
    STAIRSM        10.4                                                                                                                                                                                                     float
    STAIRSU        10.6                                                                                                                                                                                                     float
    TELBASE        9.6                                                                                                                                                                                                      float
    UTILWALL       11.1                                                                                                                                                                                                     float
    UTILROOM       10.9                                                                                                                                                                                                     float
    RADESYS        FK5                                                                                                                                                                                                      str
    TNFSPROC       8.1963                                                                                                                                                                                                   float
    TGFAPROC [1]_  7.9212                                                                                                                                                                                                   float
    SIMGFAP        F                                                                                                                                                                                                        bool
    USEFVC         T                                                                                                                                                                                                        bool
    USEFID         T                                                                                                                                                                                                        bool
    USEILLUM       T                                                                                                                                                                                                        bool
    USEXSRVR       T                                                                                                                                                                                                        bool
    USEOPENL       T                                                                                                                                                                                                        bool
    STOPGUDR       T                                                                                                                                                                                                        bool
    STOPFOCS       T                                                                                                                                                                                                        bool
    STOPSKY        T                                                                                                                                                                                                        bool
    KEEPGUDR       F                                                                                                                                                                                                        bool
    KEEPFOCS       F                                                                                                                                                                                                        bool
    KEEPSKY        F                                                                                                                                                                                                        bool
    REACQUIR       F                                                                                                                                                                                                        bool
    FILENAME       /exposures/desi/20201220/00069022/desi-00069022.fits.fz                                                                                                                                                  str
    EXCLUDED                                                                                                                                                                                                                str
    DOSVER         trunk                                                                                                                                                                                                    str
    OCSVER         1.2                                                                                                                                                                                                      float
    CONSTVER       DESI:CURRENT                                                                                                                                                                                             str
    INIFILE        /data/msdos/dos_home/architectures/kpno/desi.ini                                                                                                                                                         str
    REQTIME        300.0                                                                                                                                                                                                    float
    FVCTIME [1]_   2.0                                                                                                                                                                                                      float
    SIMGFACQ       F                                                                                                                                                                                                        bool
    POSCNVGD [1]_  F                                                                                                                                                                                                        bool
    GUIEXPID       69022                                                                                                                                                                                                    int
    IGFRMNUM       12                                                                                                                                                                                                       int
    FOCEXPID       69022                                                                                                                                                                                                    int
    IFFRMNUM       1                                                                                                                                                                                                        int
    SKYEXPID       69022                                                                                                                                                                                                    int
    ISFRMNUM       1                                                                                                                                                                                                        int
    FGFRMNUM       46                                                                                                                                                                                                       int
    FFFRMNUM       6                                                                                                                                                                                                        int
    FSFRMNUM       5                                                                                                                                                                                                        int
    FRAMES [1]_    47                                                                                                                                                                                                       int
    DELTARA [1]_   None                                                                                                                                                                                                     Unknown
    DELTADEC [1]_  None                                                                                                                                                                                                     Unknown
    GSGUIDE0 [1]_  (980.05,685.98),(878.97,731.68)                                                                                                                                                                          str
    GSGUIDE2 [1]_  (372.65,939.43),(784.50,1529.96)                                                                                                                                                                         str
    GSGUIDE3 [1]_  (365.22,1423.83),(249.12,411.52)                                                                                                                                                                         str
    GSGUIDE5 [1]_  (848.52,78.26),(516.16,1410.54)                                                                                                                                                                          str
    GSGUIDE7 [1]_  (540.95,1848.95),(504.68,831.62)                                                                                                                                                                         str
    GSGUIDE8 [1]_  (720.29,552.69),(499.80,465.13)                                                                                                                                                                          str
    ARCHIVE [1]_   /exposures/desi/20201220/00069022/guide-00069022.fits.fz                                                                                                                                                 str
    GUIDEFIL       guide-00069022.fits.fz                                                                                                                                                                                   str
    COORDFIL       coordinates-00069022.fits                                                                                                                                                                                str
    TIME-OBS       02:39:11.845920                                                                                                                                                                                          str
    EXPTIME        300.007                                                                                                                                                                                                  float
    VCCDON         2020-12-14T17:48:28.296248                                                                                                                                                                               str
    VCCDSEC        550592.7                                                                                                                                                                                                 float
    SPECGRPH       3                                                                                                                                                                                                        int
    SPECID         6                                                                                                                                                                                                        int
    FEEBOX         lbnl074                                                                                                                                                                                                  str
    VESSEL         11                                                                                                                                                                                                       int
    FEEVER         v20160312                                                                                                                                                                                                str
    FEEPOWER       ON                                                                                                                                                                                                       str
    FEEDMASK       2134851391                                                                                                                                                                                               int
    FEECMASK       1048575                                                                                                                                                                                                  int
    CCDTEMP        -140.2798                                                                                                                                                                                                float
    CRYOPRES [1]_  7.233e-08                                                                                                                                                                                                str
    CLOCK7         -2.0001,3.9999                                                                                                                                                                                           str
    TRIMSECA       [8:2064, 2:2065]                                                                                                                                                                                         str
    CCDNAME        CCDSM6R                                                                                                                                                                                                  str
    TRIMSECD       [2193:4249, 2130:4193]                                                                                                                                                                                   str
    OFFSET2        0.4000000059604645,-8.961                                                                                                                                                                                str
    CPUTEMP        56.625                                                                                                                                                                                                   float
    DAC11          -25.0003,-24.7086                                                                                                                                                                                        str
    AMPSECA        [1:2057, 1:2064]                                                                                                                                                                                         str
    CCDCFG         M1-50_lbnl_20190719.cfg                                                                                                                                                                                  str
    TRIMSECB       [2193:4249, 2:2065]                                                                                                                                                                                      str
    CLOCK3         -2.0001,3.9999                                                                                                                                                                                           str
    CCDSECA        [1:2057, 1:2064]                                                                                                                                                                                         str
    CLOCK4         9.9999,0.0                                                                                                                                                                                               str
    DAC0           -9.0002,-8.9095                                                                                                                                                                                          str
    CLOCK10        9.9992,2.9993                                                                                                                                                                                            str
    BIASSECA       [2065:2128, 2:2065]                                                                                                                                                                                      str
    PRRSECA        [8:2064, 1:1]                                                                                                                                                                                            str
    DAC7           6.4999,6.4856                                                                                                                                                                                            str
    AMPSECB        [4114:2058, 1:2064]                                                                                                                                                                                      str
    DAC10          -25.0003,-24.9906                                                                                                                                                                                        str
    DELAYS         20, 20, 25, 30, 7, 3000, 7, 7, 7, 7                                                                                                                                                                      str
    CCDSECD        [2058:4114, 2065:4128]                                                                                                                                                                                   str
    CASETEMP       56.4919                                                                                                                                                                                                  float
    CLOCK6         9.9999,0.0                                                                                                                                                                                               str
    CLOCK13        9.9992,2.9993                                                                                                                                                                                            str
    CLOCK9         9.9992,2.9993                                                                                                                                                                                            str
    DAC8           -25.0003,-25.0202                                                                                                                                                                                        str
    DAC9           -25.0003,-24.6789                                                                                                                                                                                        str
    ORSECB         [2193:4249, 2066:2097]                                                                                                                                                                                   str
    CLOCK1         9.9999,0.0                                                                                                                                                                                               str
    DETSECC        [1:2057, 2065:4128]                                                                                                                                                                                      str
    AMPSECD        [4114:2058, 4128:2065]                                                                                                                                                                                   str
    CLOCK5         9.9999,0.0                                                                                                                                                                                               str
    ORSECA         [8:2064, 2066:2097]                                                                                                                                                                                      str
    DAC15          0.0,0.0297                                                                                                                                                                                               str
    DATASECA       [8:2064, 2:2065]                                                                                                                                                                                         str
    CCDPREP        purge,clear                                                                                                                                                                                              str
    OFFSET7        2.0,6.4908                                                                                                                                                                                               str
    DAC5           5.9998,6.028                                                                                                                                                                                             str
    CLOCK12        9.9992,2.9993                                                                                                                                                                                            str
    CCDSECB        [2058:4114, 1:2064]                                                                                                                                                                                      str
    OFFSET6        2.0,6.0332                                                                                                                                                                                               str
    DAC4           5.9998,6.028                                                                                                                                                                                             str
    PRESECC        [1:7, 2130:4193]                                                                                                                                                                                         str
    OFFSET5        2.0,6.028                                                                                                                                                                                                str
    DAC2           -9.0002,-8.9713                                                                                                                                                                                          str
    CRYOTEMP [1]_  162.97                                                                                                                                                                                                   float
    PRESECB        [4250:4256, 2:2065]                                                                                                                                                                                      str
    DIGITIME       47.1031                                                                                                                                                                                                  float
    DAC3           -10.5005,-10.3824                                                                                                                                                                                        str
    CAMERA         r3                                                                                                                                                                                                       str
    DETSECB        [2058:4114, 1:2064]                                                                                                                                                                                      str
    OFFSET1        0.4000000059604645,-8.8065                                                                                                                                                                               str
    DATASECD       [2193:4249, 2130:4193]                                                                                                                                                                                   str
    SETTINGS       detectors_sm_20191211.json                                                                                                                                                                               str
    CLOCK11        9.9992,2.9993                                                                                                                                                                                            str
    DAC13          0.0,0.0                                                                                                                                                                                                  str
    CLOCK14        9.9992,2.9993                                                                                                                                                                                            str
    CCDSECC        [1:2057, 2065:4128]                                                                                                                                                                                      str
    DATASECC       [8:2064, 2130:4193]                                                                                                                                                                                      str
    CLOCK0         9.9999,0.0                                                                                                                                                                                               str
    CLOCK15        9.9992,2.9993                                                                                                                                                                                            str
    DAC12          0.0,0.0297                                                                                                                                                                                               str
    CCDSIZE        4194,4256                                                                                                                                                                                                str
    OFFSET0        0.4000000059604645,-8.9095                                                                                                                                                                               str
    ORSECD         [2193:4249, 2098:2129]                                                                                                                                                                                   str
    DAC16          48.0,46.7082                                                                                                                                                                                             str
    PRRSECC        [8:2064, 4194:4194]                                                                                                                                                                                      str
    PRRSECD        [2193:4249, 4194:4194]                                                                                                                                                                                   str
    BIASSECB       [2129:2192, 2:2065]                                                                                                                                                                                      str
    DETSECD        [2058:4114, 2065:4128]                                                                                                                                                                                   str
    CLOCK18        9.0,0.9999                                                                                                                                                                                               str
    DAC17          20.0008,14.274                                                                                                                                                                                           str
    CCDTMING       default_lbnl_timing_20180905.txt                                                                                                                                                                         str
    DETECTOR       M1-50                                                                                                                                                                                                    str
    PRRSECB        [2193:4249, 1:1]                                                                                                                                                                                         str
    TRIMSECC       [8:2064, 2130:4193]                                                                                                                                                                                      str
    DAC14          0.0,0.0148                                                                                                                                                                                               str
    BIASSECD       [2129:2192, 2130:4193]                                                                                                                                                                                   str
    CDSPARMS       400, 400, 8, 2000                                                                                                                                                                                        str
    OFFSET3        0.4000000059604645,-10.3721                                                                                                                                                                              str
    PRESECA        [1:7, 2:2065]                                                                                                                                                                                            str
    ORSECC         [8:2064, 2098:2129]                                                                                                                                                                                      str
    DAC6           5.9998,6.0332                                                                                                                                                                                            str
    PGAGAIN        3                                                                                                                                                                                                        int
    DAC1           -9.0002,-8.8065                                                                                                                                                                                          str
    DATASECB       [2193:4249, 2:2065]                                                                                                                                                                                      str
    CLOCK2         9.9999,0.0                                                                                                                                                                                               str
    CLOCK16        9.9999,3.0                                                                                                                                                                                               str
    PRESECD        [4250:4256, 2130:4193]                                                                                                                                                                                   str
    OFFSET4        2.0,6.0332                                                                                                                                                                                               str
    CLOCK17        9.0,0.9999                                                                                                                                                                                               str
    AMPSECC        [1:2057, 4128:2065]                                                                                                                                                                                      str
    CLOCK8         9.9992,2.9993                                                                                                                                                                                            str
    DETSECA        [1:2057, 1:2064]                                                                                                                                                                                         str
    BIASSECC       [2065:2128, 2130:4193]                                                                                                                                                                                   str
    BLDTIME        0.3504                                                                                                                                                                                                   float
    OBSID          kp4m20201221t023911                                                                                                                                                                                      str
    PROCTYPE       RAW                                                                                                                                                                                                      str
    PRODTYPE       image                                                                                                                                                                                                    str
    GAINA          1.681                                                                                                                                                                                                    float
    SATULEVA       28000.0                                                                                                                                                                                                  float
    OSTEPA         0.7048677125421818                                                                                                                                                                                       float
    OMETHA         AVERAGE                                                                                                                                                                                                  str
    OVERSCNA       1979.586454500641                                                                                                                                                                                        float
    OBSRDNA        2.618213792981265                                                                                                                                                                                        float
    SATUELEA       43740.31516998442                                                                                                                                                                                        float
    GAINB          1.625                                                                                                                                                                                                    float
    SATULEVB       57000.0                                                                                                                                                                                                  float
    OSTEPB         0.6850349189899134                                                                                                                                                                                       float
    OMETHB         AVERAGE                                                                                                                                                                                                  str
    OVERSCNB       1997.289875350671                                                                                                                                                                                        float
    OBSRDNB        3.12518985733541                                                                                                                                                                                         float
    SATUELEB       89379.40395255515                                                                                                                                                                                        float
    GAINC          1.477                                                                                                                                                                                                    float
    SATULEVC       59000.0                                                                                                                                                                                                  float
    OSTEPC         0.6403308619337622                                                                                                                                                                                       float
    OMETHC         AVERAGE                                                                                                                                                                                                  str
    OVERSCNC       1974.691977751432                                                                                                                                                                                        float
    OBSRDNC        2.344388520757958                                                                                                                                                                                        float
    SATUELEC       84226.37994886114                                                                                                                                                                                        float
    GAIND          1.492                                                                                                                                                                                                    float
    SATULEVD       62000.0                                                                                                                                                                                                  float
    OSTEPD         0.6246898852550657                                                                                                                                                                                       float
    OMETHD         AVERAGE                                                                                                                                                                                                  str
    OVERSCND       1998.214476179268                                                                                                                                                                                        float
    OBSRDND        2.301320302261815                                                                                                                                                                                        float
    SATUELED       89522.66400154053                                                                                                                                                                                        float
    FIBERMIN       1500                                                                                                                                                                                                     int
    CHECKSUM       9VRaITQX9TQaGTQU                                                                                                                                                                                         str     HDU checksum updated 2022-02-14T06:14:07
    DATASUM        3502588181                                                                                                                                                                                               str     data unit checksum updated 2022-02-14T06:14:07
    SP6BLUP [1]_   7.89899999999999e-08                                                                                                                                                                                     float
    TCSMFDEC [1]_  1                                                                                                                                                                                                        int
    SLEWANGL [1]_  15.646                                                                                                                                                                                                   float
    TARG2 [1]_     DESIROOT/target/catalogs/gaiadr2/0.51.0/targets/sv1/resolve/supp                                                                                                                                         str
    SEQTOT [1]_    2                                                                                                                                                                                                        int
    MOONSEP [1]_   111.881                                                                                                                                                                                                  float
    SP5REDP [1]_   9.74199999999999e-08                                                                                                                                                                                     float
    SEQSTART [1]_  2021-05-08T10:26:00.785886                                                                                                                                                                               str
    CONVERGD [1]_  F                                                                                                                                                                                                        bool
    SP9NIRP [1]_   5.455e-08                                                                                                                                                                                                float
    SP3REDP [1]_   5.899e-08                                                                                                                                                                                                float
    SP1BLUT [1]_   162.97                                                                                                                                                                                                   float
    SP0BLUT [1]_   162.97                                                                                                                                                                                                   float
    SP8REDT [1]_   139.99                                                                                                                                                                                                   float
    SP3BLUP [1]_   7.952e-08                                                                                                                                                                                                float
    SP9REDT [1]_   139.99                                                                                                                                                                                                   float
    SP4NIRP [1]_   7.251e-08                                                                                                                                                                                                float
    SP4REDP [1]_   5.049e-08                                                                                                                                                                                                float
    PMSEEING [1]_  0.93                                                                                                                                                                                                     float
    SP1NIRP [1]_   6.18e-08                                                                                                                                                                                                 float
    SP2REDT [1]_   139.99                                                                                                                                                                                                   float
    SP5REDT [1]_   140.06                                                                                                                                                                                                   float
    SP4NIRT [1]_   139.99                                                                                                                                                                                                   float
    SP7BLUT [1]_   162.99                                                                                                                                                                                                   float
    USESPLIT [1]_  T                                                                                                                                                                                                        bool
    SP1BLUP [1]_   7.999e-08                                                                                                                                                                                                float
    SP1NIRT [1]_   139.96                                                                                                                                                                                                   float
    SP1REDT [1]_   139.99                                                                                                                                                                                                   float
    SP8REDP [1]_   3.96e-08                                                                                                                                                                                                 float
    SP5BLUT [1]_   163.02                                                                                                                                                                                                   float
    TARG3 [1]_     DESIROOT/target/catalogs/dr9/0.51.0/targets/sv1/resolve/bright                                                                                                                                           str
    TCSGRA [1]_    0.3                                                                                                                                                                                                      float
    SUNDEC [1]_    17.206123                                                                                                                                                                                                float
    SP7NIRP [1]_   4.416e-08                                                                                                                                                                                                float
    PMTRANS [1]_   95.5                                                                                                                                                                                                     float
    SP0NIRT [1]_   139.99                                                                                                                                                                                                   float
    SP5NIRP [1]_   6.57299999999999e-08                                                                                                                                                                                     float
    POSCVFRC [1]_  0.3845                                                                                                                                                                                                   float
    SP7BLUP [1]_   1.04e-07                                                                                                                                                                                                 float
    FAARGS [1]_    --doclean n --dr dr9 --dtver 0.51.0 --faflavor sv1unwisegreen --m31cen n --pmtime 2021-03-12T00:00:00.000 --priority custom --rundate 2020-01-01T00:00:00 --tiledec 54.98 --tileid 80865 --tilera 242.75 str
    NTSSURVY [1]_  na                                                                                                                                                                                                       Unknown
    SP7REDT [1]_   139.99                                                                                                                                                                                                   float
    SP2REDP [1]_   6.15e-08                                                                                                                                                                                                 float
    SP4REDT [1]_   140.06                                                                                                                                                                                                   float
    SP6BLUT [1]_   162.97                                                                                                                                                                                                   float
    SP7REDP [1]_   3.404e-08                                                                                                                                                                                                float
    SP8NIRP [1]_   4.941e-08                                                                                                                                                                                                float
    SP9REDP [1]_   5.113e-08                                                                                                                                                                                                float
    SP8NIRT [1]_   139.99                                                                                                                                                                                                   float
    TCSKRA [1]_    0.3 0.003 0.00003                                                                                                                                                                                        str
    SCND [1]_      DESIROOT/target/catalogs/dr9/0.51.0/targets/sv1/secondary/dark                                                                                                                                           str
    TCSMFRA [1]_   1                                                                                                                                                                                                        int
    SP0BLUP [1]_   7.565e-08                                                                                                                                                                                                float
    SP3NIRP [1]_   4.105e-08                                                                                                                                                                                                float
    SP1REDP [1]_   7.239e-08                                                                                                                                                                                                float
    SP4BLUP [1]_   6.689e-08                                                                                                                                                                                                float
    SP3NIRT [1]_   140.01                                                                                                                                                                                                   float
    SP8BLUP [1]_   8.31099999999999e-08                                                                                                                                                                                     float
    SP0REDT [1]_   139.99                                                                                                                                                                                                   float
    SEQID [1]_     2 requests                                                                                                                                                                                               str
    SP2BLUP [1]_   8.29699999999999e-08                                                                                                                                                                                     float
    DESIROOT [1]_  /global/cfs/cdirs/desi                                                                                                                                                                                   str
    SP2BLUT [1]_   163.02                                                                                                                                                                                                   float
    SP2NIRP [1]_   4.884e-08                                                                                                                                                                                                float
    SP9BLUP [1]_   1.237e-07                                                                                                                                                                                                float
    TCSGDEC [1]_   0.3                                                                                                                                                                                                      float
    SP8BLUT [1]_   162.97                                                                                                                                                                                                   float
    SP9BLUT [1]_   162.97                                                                                                                                                                                                   float
    SP4BLUT [1]_   162.97                                                                                                                                                                                                   float
    TCSPIDEC [1]_  1.0,0.0,0.0,0.0                                                                                                                                                                                          str
    SP3REDT [1]_   139.99                                                                                                                                                                                                   float
    SP6NIRT [1]_   139.99                                                                                                                                                                                                   float
    SP6REDT [1]_   139.99                                                                                                                                                                                                   float
    SP5NIRT [1]_   140.08                                                                                                                                                                                                   float
    TCSKDEC [1]_   0.3 0.003 0.00003                                                                                                                                                                                        str
    SP0NIRP [1]_   7.886e-08                                                                                                                                                                                                float
    SCSTD [1]_     STD_WD,STD_FAINT                                                                                                                                                                                         str
    VISITIDS [1]_  87615                                                                                                                                                                                                    str
    SP0REDP [1]_   4.265e-08                                                                                                                                                                                                float
    SUNRA [1]_     45.595565                                                                                                                                                                                                float
    SP5BLUP [1]_   1.153e-07                                                                                                                                                                                                float
    SKYLEVEL [1]_  0.83                                                                                                                                                                                                     float
    SP2NIRT [1]_   139.99                                                                                                                                                                                                   float
    SP6REDP [1]_   6.491e-08                                                                                                                                                                                                float
    TCSPIRA [1]_   1.0,0.0,0.0,0.0                                                                                                                                                                                          str
    SP7NIRT [1]_   139.99                                                                                                                                                                                                   float
    SP9NIRT [1]_   139.99                                                                                                                                                                                                   float
    SPLITEXP [1]_  F                                                                                                                                                                                                        bool
    SP6NIRP [1]_   2.807e-07                                                                                                                                                                                                float
    SP3BLUT [1]_   162.99                                                                                                                                                                                                   float
    PMCORR [1]_    n                                                                                                                                                                                                        str
    GOALTYPE [1]_  DARK                                                                                                                                                                                                     str
    SURVEY [1]_    special                                                                                                                                                                                                  str
    SCNDMTL [1]_   DESIROOT/survey/ops/surveyops/trunk/mtl/main/secondary/dark                                                                                                                                              str
    MINTFRAC [1]_  0.85                                                                                                                                                                                                     float
    FASCRIPT [1]_  ./fba_launch-20210513-special                                                                                                                                                                            str
    MTLTIME [1]_   2021-05-13T21:05:00+00:00                                                                                                                                                                                str
    GOALTIME [1]_  1000.0                                                                                                                                                                                                   float
    FAPRGRM [1]_   dark                                                                                                                                                                                                     str
    EBVFAC [1]_    1.02471876800862                                                                                                                                                                                         float
    TOO [1]_       DESIROOT/survey/ops/surveyops/trunk/mtl/main/ToO/ToO.ecsv                                                                                                                                                str
    SVNDM [1]_     136361                                                                                                                                                                                                   str
    MTL [1]_       DESIROOT/survey/ops/surveyops/trunk/mtl/main/dark                                                                                                                                                        str
    SBPROF [1]_    ELG                                                                                                                                                                                                      str
    SVNMTL [1]_    476                                                                                                                                                                                                      str
    TOTTEFF [1]_   1406.4226                                                                                                                                                                                                float
    REQTEFF [1]_   1400.0                                                                                                                                                                                                   int
    ACTTEFF [1]_   1406.4226                                                                                                                                                                                                float
    BBKGMINB [1]_  -0.5249611468569187                                                                                                                                                                                      float
    BBKGMAXA [1]_  1.179777031725897                                                                                                                                                                                        float
    BBKGMIND [1]_  -0.5599583904094981                                                                                                                                                                                      float
    BBKGMINA [1]_  -0.9489741260224904                                                                                                                                                                                      float
    BBKGMAXD [1]_  0.2726660093392476                                                                                                                                                                                       float
    BBKGMAXB [1]_  0.6927871978458614                                                                                                                                                                                       float
    SEEING [1]_    1.291                                                                                                                                                                                                    float
    BBKGMAXC [1]_  1.270526827094756                                                                                                                                                                                        float
    BBKGMINC [1]_  -0.8627791108943093                                                                                                                                                                                      float
    USESPLITS [1]_ T                                                                                                                                                                                                        bool
    SIMGFAQ [1]_   F                                                                                                                                                                                                        bool
    SHFTFOCS [1]_  220.0                                                                                                                                                                                                    float
    ROLE [1]_      GUIDERMAN                                                                                                                                                                                                str
    M31CEN [1]_    n                                                                                                                                                                                                        str
    DTVER [1]_     0.50.0                                                                                                                                                                                                   str
    DR [1]_        dr9                                                                                                                                                                                                      str
    PRIORITY [1]_  default                                                                                                                                                                                                  str
    ETCTHRUB [1]_  0.575924                                                                                                                                                                                                 float
    ACQFWHM [1]_   1.469225                                                                                                                                                                                                 float
    ESTTIME [1]_   1374.714                                                                                                                                                                                                 float
    ETCSPLIT [1]_  1                                                                                                                                                                                                        int
    ETCFRACE [1]_  0.302117                                                                                                                                                                                                 float
    ETCFRACP [1]_  0.392042                                                                                                                                                                                                 float
    ETCTHRUP [1]_  0.556996                                                                                                                                                                                                 float
    ETCPREV [1]_   0.0                                                                                                                                                                                                      float
    ETCTHRUE [1]_  0.585204                                                                                                                                                                                                 float
    ETCREAL [1]_   1120.375                                                                                                                                                                                                 float
    TRANSPAR [1]_  None                                                                                                                                                                                                     Unknown
    PMTRANSP [1]_  101.86                                                                                                                                                                                                   float
    ETCPROF [1]_   BGS                                                                                                                                                                                                      str
    ETCVERS [1]_   0.1.12-3-g12b54bb                                                                                                                                                                                        str
    ETCFRACB [1]_  0.136941                                                                                                                                                                                                 float
    ETCSKY [1]_    2.674912                                                                                                                                                                                                 float
    NTSPROG [1]_   BRIGHT                                                                                                                                                                                                   str
    ETCTRANS [1]_  0.798438                                                                                                                                                                                                 float
    ETCTEFF [1]_   223.989487                                                                                                                                                                                               float
    ETCSEENG [1]_  1.4692                                                                                                                                                                                                   float
    MAXTIME [1]_   5400.0                                                                                                                                                                                                   float
    MINTIME [1]_   120.0                                                                                                                                                                                                    float
    ============== ======================================================================================================================================================================================================== ======= ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

===================== ======= ============ =========================================================================================================================
Name                  Type    Units        Description
===================== ======= ============ =========================================================================================================================
TARGETID              int64                Unique target ID
PETAL_LOC             int16                Focal plane petal location 0-9
DEVICE_LOC            int32                Device location 0-5xx
LOCATION              int64                1000*PETAL_LOC + DEVICE_LOC
FIBER                 int32                Fiber number 0-4999
FIBERSTATUS           int32                Fiber status mask; 0=good
TARGET_RA             float64 deg          Barycentric right ascension in ICRS
TARGET_DEC            float64 deg          Barycentric declination in ICRS
PMRA                  float32 mas yr^-1    proper motion in the +RA direction (already including cos(dec))
PMDEC                 float32 mas yr^-1    Proper motion in the +Dec direction
REF_EPOCH             float32 yr           Reference epoch for Gaia/Tycho astrometry. Typically 2015.5 for Gaia
LAMBDA_REF            float32 Angstrom     Requested wavelength at which targets should be centered on fibers
FA_TARGET             int64                Targeting bit internally used by fiberassign (linked with FA_TYPE)
FA_TYPE               binary               Fiberassign internal target type (science, standard, sky, safe, suppsky)
OBJTYPE               char[3]              Object type: TGT, SKY, NON, BAD
FIBERASSIGN_X         float32 mm           Fiberassign expected CS5 X location on focal plane
FIBERASSIGN_Y         float32 mm           Fiberassign expected CS5 Y location on focal plane
PRIORITY              int32                Target current priority
SUBPRIORITY           float64              Random subpriority [0-1) to break assignment ties
OBSCONDITIONS         int32                Bitmask of allowed observing conditions
RELEASE               int16                Imaging surveys release ID
BRICKID               int32                Brick ID from tractor input
BRICK_OBJID           int32                Imaging Surveys OBJID on that brick
MORPHTYPE             char[4]              Imaging Surveys morphological type from Tractor
FLUX_G                float32 nanomaggy    Flux in the Legacy Survey g-band (AB)
FLUX_R                float32 nanomaggy    Flux in the Legacy Survey r-band (AB)
FLUX_Z                float32 nanomaggy    Flux in the Legacy Survey z-band (AB)
FLUX_IVAR_G           float32 nanomaggy^-2 Inverse variance of FLUX_G (AB)
FLUX_IVAR_R           float32 nanomaggy^-2 Inverse variance of FLUX_R (AB)
FLUX_IVAR_Z           float32 nanomaggy^-2 Inverse variance of FLUX_Z (AB)
REF_ID                int64                Tyc1*1,000,000+Tyc2*10+Tyc3 for Tycho-2; “sourceid” for Gaia DR2
REF_CAT               char[2]              Reference catalog source for star: “T2” for Tycho-2, “G2” for Gaia DR2, “L2” for the SGA, empty otherwise
GAIA_PHOT_G_MEAN_MAG  float32 mag          Gaia G band magnitude
GAIA_PHOT_BP_MEAN_MAG float32 mag          Gaia BP band magnitude
GAIA_PHOT_RP_MEAN_MAG float32 mag          Gaia RP band magnitude
PARALLAX              float32 mas          Reference catalog parallax
BRICKNAME             char[8]              Brick name from tractor input
EBV                   float32 mag          Galactic extinction E(B-V) reddening from SFD98
FLUX_W1               float32 nanomaggy    WISE flux in W1 (AB)
FLUX_W2               float32 nanomaggy    WISE flux in W2 (AB)
FLUX_IVAR_W1          float32 nanomaggy^-2 Inverse variance of FLUX_W1 (AB)
FLUX_IVAR_W2          float32 nanomaggy^-2 Inverse variance of FLUX_W2 (AB)
FIBERFLUX_G           float32 nanomaggy    Predicted g-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERFLUX_R           float32 nanomaggy    Predicted r-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERFLUX_Z           float32 nanomaggy    Predicted z-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERTOTFLUX_G        float32 nanomaggy    Predicted g-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
FIBERTOTFLUX_R        float32 nanomaggy    Predicted r-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
FIBERTOTFLUX_Z        float32 nanomaggy    Predicted z-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
MASKBITS              int16                Bitwise mask from the imaging indicating potential issue or blending
SERSIC                float32              Power-law index for the Sersic profile model (MORPHTYPE=”SER”)
SHAPE_R               float32 arcsec       Half-light radius of galaxy model (&gt;0)
SHAPE_E1              float32              Ellipticity component 1 of galaxy model for galaxy type MORPHTYPE
SHAPE_E2              float32              Ellipticity component 2 of galaxy model for galaxy type MORPHTYPE
PHOTSYS               char[1]              'N' for the MzLS/BASS photometric system, 'S' for DECaLS
PRIORITY_INIT         int64                Target initial priority from target selection bitmasks and OBSCONDITIONS
NUMOBS_INIT           int64                Initial number of observations for target calculated across target selection bitmasks and OBSCONDITIONS
SV1_DESI_TARGET [1]_  int64                DESI (dark time program) target selection bitmask for SV1
SV1_BGS_TARGET [1]_   int64                BGS (bright time program) target selection bitmask for SV1
SV1_MWS_TARGET [1]_   int64                MWS (bright time program) target selection bitmask for SV1
SV1_SCND_TARGET [1]_  int64                Secondary target selection bitmask for SV1
DESI_TARGET           int64                DESI (dark time program) target selection bitmask
BGS_TARGET            int64                BGS (Bright Galaxy Survey) target selection bitmask
MWS_TARGET            int64                Milky Way Survey targeting bits
PLATE_RA              float64 deg          Barycentric Right Ascension in ICRS to be used by PlateMaker
PLATE_DEC             float64 deg          Barycentric Declination in ICRS to be used by PlateMaker
NUM_ITER              int64                Number of positioner iterations
FIBER_X               float64 mm           CS5 X location requested by PlateMaker
FIBER_Y               float64 mm           CS5 Y location requested by PlateMaker
DELTA_X               float64 mm           CS5 X requested minus actual position
DELTA_Y               float64 mm           CS5 Y requested minus actual position
FIBER_RA              float64 deg          RA of actual fiber position
FIBER_DEC             float64 deg          DEC of actual fiber position
EXPTIME               float64 s            Length of time shutter was open
SCND_TARGET [1]_      int64                Target selection bitmask for secondary programs
SV3_SCND_TARGET [1]_  int64                Secondary target selection bitmask for SV3
SV3_MWS_TARGET [1]_   int64                MWS (bright time program) target selection bitmask for SV3
SV3_DESI_TARGET [1]_  int64                DESI (dark time program) target selection bitmask for SV3
SV3_BGS_TARGET [1]_   int64                BGS (bright time program) target selection bitmask for SV3
SV2_MWS_TARGET [1]_   int64                MWS (bright time program) target selection bitmask for SV2
SV2_DESI_TARGET [1]_  int64                DESI (dark time program) target selection bitmask for SV2
SV2_SCND_TARGET [1]_  int64                Secondary target selection bitmask for SV2
SV2_BGS_TARGET [1]_   int64                BGS (bright time program) target selection bitmask for SV2
CMX_TARGET [1]_       int64                Target selection bitmask for commissioning
===================== ======= ============ =========================================================================================================================

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
    NAXIS1   2326             int  Number of wavelengths
    NAXIS2   500              int  Number of spectra
    CHECKSUM WY6VaW3VZW3VaW3V str  HDU checksum updated 2021-07-08T15:52:40
    DATASUM  2321269489       str  data unit checksum updated 2021-07-08T15:52:40
    ======== ================ ==== ==============================================

Data: FITS image [float32, 2326x500]

HDU7
----

See `SCORES HDU7 of cframe-CAMERA-EXPID.fits <cframe-CAMERA-EXPID.html#hdu7>`_.


Notes and Examples
==================

For the SURVEY=cmx m33 tile (TILEID=80615) tile and all the SURVEY=sv1 tiles (except TILEID=80971-80976, the dc3r2 ones), proper-motion correction was applied at the :doc:`fiberassign </DESI_TARGET/fiberassign/tiles/TILES_VERSION/TILEXX/fiberassign-TILEID>` design step; thus the following columns can have different values than in the :doc:`desitarget products </DESI_TARGET/TARG_DIR/DR/VERSION/targets/PHASE/RESOLVE/OBSCON/PHASEtargets-OBSCON-RESOLVE-hp-HP>`: ``TARGET_RA``, ``TARGET_DEC``, ``REF_EPOCH``, ``PLATE_RA``, ``PLATE_DEC``, and ``PLATE_REF_EPOCH``.

For targets with a non-zero proper motion, ``FIBER_RA`` and ``FIBER_DEC`` refer to the position at the reference epoch (but note that the proper-motion correction has been applied at the time of the observation, it is just not recorded in ``FIBER_RA`` and ``FIBER_DEC``).
