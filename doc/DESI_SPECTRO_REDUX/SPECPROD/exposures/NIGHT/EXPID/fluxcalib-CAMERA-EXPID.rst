===========================
fluxcalib-CAMERA-EXPID.fits
===========================

:Summary: This holds the flux calibration model for a given camera and exposure.
:Naming Convention: ``fluxcalib-{CAMERA}-{EXPID}.fits``, where ``{CAMERA}`` is
    one of the spectrograph cameras (*e.g.* ``z1``) and ``{EXPID}``
    is the 8-digit exposure ID.
:Regex: ``fluxcalib-[brz][0-9]-[0-9]{8}\.fits``
:File Type: FITS, 13 MB

Contents
========

====== ================ ======== ===================
Number EXTNAME          Type     Contents
====== ================ ======== ===================
HDU0_  FLUXCALIB        IMAGE    Flux calibration model
HDU1_  IVAR             IMAGE    Inverse variance of flux
HDU2_  MASK             IMAGE    Mask (0 = good)
HDU3_  WAVELENGTH       IMAGE    wavelength in Angstrom
HDU4_  FIBERCORR        BINTABLE Correction factors for fiber size input losses
HDU5_  STDSTAR_FIBERMAP BINTABLE stdstar photometry and target:fiber mapping
====== ================ ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = FLUXCALIB

Flux calibration array 'fluxcal', such that calibrated flux = uncalibrated flux / fluxcal.
2D array of dimension [nspec, nwave]. nspec is the number of fibers per camera. nwave in the length of the wavelength array.
The flux calibration of all fibers share the same wavelength grid (given in HDU WAVELENGTH).
The units are electrons / (10^{-17} ergs/s/cm2), such that the calibrated flux has units of 10^{-17} ergs/s/cm2/Angstrom.
The flux calibration is obtained by comparing the sky subtracted and flat-fielded flux from standard stars in the :doc:`sframe file <sframe-CAMERA-EXPID>` with stellar models from the :doc:`stdstars file <stdstars-SPECTROGRAPH-EXPID>`.
This calibration of the total flux is valid for point sources only.
For extended sources, one may consider using a 'fiber flux', which is the flux one would collect in a 1.5 arcsec diameter aperture centered on the object when observed with a 1 arcsec FWHM Gaussian seeing. The 'fiber flux' can be obtained by multiplying the calibrated flux array of each fiber by the corresponding entry in the FIBERCORR_ table column 'PSF_TO_FIBER_SPECFLUX'.


Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ============== ===================================================================== ======= ===============================================
    KEY            Example Value                                                         Type    Comment
    ============== ===================================================================== ======= ===============================================
    NAXIS1         2881                                                                  int
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
    VCCDON         2020-12-09T21:23:25.472733                                            str     Time when CCD voltage was turned on
    VCCDSEC        969696.0                                                              float   [s] CCD on time in seconds
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
    SPECGRPH       6                                                                     int     Spectrograph logical name (SP)
    SPECID         7                                                                     int     Spectrograph serial number (SM)
    FEEBOX         lbnl061                                                               str     CCD Controller serial number
    VESSEL         21                                                                    int     Cryostat serial number
    FEEVER         v20160312                                                             str     CCD Controller version
    FEEPOWER       ON                                                                    str     FEE power status
    FEEDMASK       2134851391                                                            int     FEE dac mask
    FEECMASK       1048575                                                               int     FEE clk mask
    CCDTEMP        -134.1517                                                             float   [deg C] CCD controller CCD temperature
    RADESYS        FK5                                                                   str     Coordinate reference frame of major/minor axes
    FILENAME       /exposures/desi/specs/20201220/00069022/sp1-00069022.fits.fz          str     Name
    DOSVER         trunk                                                                 str     DOS software version
    OCSVER         1.2                                                                   float   OCS software version
    CONSTVER       DESI:CURRENT                                                          str     Constants version
    INIFILE        /data/msdos/dos_home/architectures/kpno/desi.ini                      str     DOS Configuration
    PRESECC        [1:7, 2130:4193]                                                      str     Prescan section for quadrant C
    CLOCK13        9.9992,2.9993                                                         str     [V] high rail, low rail
    DETECTOR       M1-51                                                                 str     Detector (ccd) identification
    SETTINGS       detectors_sm_20191211.json                                            str     Name of DESI CCD settings file
    PRRSECA        [8:2064, 1:1]                                                         str     Row prescan section for quadrant A
    CLOCK11        9.9992,2.9993                                                         str     [V] high rail, low rail
    OFFSET2        0.4000000059604645,-8.9507                                            str     [V] set value, measured value
    AMPSECC        [1:2057, 4128:2065]                                                   str     AMP section for quadrant C
    DAC11          -25.0003,-25.0351                                                     str     [V] set value, measured value
    CLOCK1         9.9999,0.0                                                            str     [V] high rail, low rail
    DAC7           5.9998,6.0017                                                         str     [V] set value, measured value
    DAC16          39.9961,39.5472                                                       str     [V] set value, measured value
    CCDSECB        [2058:4114, 1:2064]                                                   str     CCD section for quadrant B
    CLOCK17        9.0,0.9999                                                            str     [V] high rail, low rail
    CLOCK5         9.9999,0.0                                                            str     [V] high rail, low rail
    AMPSECB        [4114:2058, 1:2064]                                                   str     AMP section for quadrant B
    CLOCK4         9.9999,0.0                                                            str     [V] high rail, low rail
    DETSECB        [2058:4114, 1:2064]                                                   str     Detector section for quadrant B
    BIASSECA       [2065:2128, 2:2065]                                                   str     Bias section for quadrant A
    CRYOPRES [1]_  2.938e-07                                                             str     [mb] Cryostat pressure (IP)
    CCDTMING       default_lbnl_timing_20180905.txt                                      str     CCD timing file
    CLOCK9         9.9992,2.9993                                                         str     [V] high rail, low rail
    PGAGAIN        3                                                                     int     Controller gain
    CLOCK6         9.9999,0.0                                                            str     [V] high rail, low rail
    OFFSET3        0.4000000059604645,-8.8889                                            str     [V] set value, measured value
    PRRSECB        [2193:4249, 1:1]                                                      str     Row prescan section for quadrant B
    DAC5           5.9998,6.0174                                                         str     [V] set value, measured value
    CLOCK3         -2.0001,3.9999                                                        str     [V] high rail, low rail
    DAC14          0.0,-0.0297                                                           str     [V] set value, measured value
    CLOCK15        9.9992,2.9993                                                         str     [V] high rail, low rail
    AMPSECD        [4114:2058, 4128:2065]                                                str     AMP section for quadrant D
    CCDSECA        [1:2057, 1:2064]                                                      str     CCD section for quadrant A
    DAC9           -25.0003,-25.0351                                                     str     [V] set value, measured value
    DAC10          -25.0003,-24.8273                                                     str     [V] set value, measured value
    CCDPREP        purge,clear                                                           str     CCD prep actions
    DAC4           5.9998,6.0437                                                         str     [V] set value, measured value
    OFFSET4        2.0,6.049                                                             str     [V] set value, measured value
    BLDTIME        0.3499                                                                float   [s] Time to build image
    CLOCK16        9.9999,3.0                                                            str     [V] high rail, low rail
    DAC2           -9.0002,-8.961                                                        str     [V] set value, measured value
    OFFSET1        0.4000000059604645,-8.9507                                            str     [V] set value, measured value
    CLOCK10        9.9992,2.9993                                                         str     [V] high rail, low rail
    OFFSET7        2.0,6.0017                                                            str     [V] set value, measured value
    ORSECD         [2193:4249, 2098:2129]                                                str     Row bias section for quadrant D
    OFFSET0        0.4000000059604645,-8.9713                                            str     [V] set value, measured value
    CLOCK0         9.9999,0.0                                                            str     [V] high rail, low rail
    CRYOTEMP [1]_  139.986                                                               float   [deg K] Cryostat CCD temperature
    DATASECB       [2193:4249, 2:2065]                                                   str     Data section for quadrant B
    DAC6           5.9998,6.049                                                          str     [V] set value, measured value
    DAC12          0.0,-0.0148                                                           str     [V] set value, measured value
    CLOCK2         9.9999,0.0                                                            str     [V] high rail, low rail
    TRIMSECC       [8:2064, 2130:4193]                                                   str     Trim section for quadrant C
    PRRSECD        [2193:4249, 4194:4194]                                                str     Row prescan section for quadrant D
    DAC15          0.0,0.0                                                               str     [V] set value, measured value
    DATASECA       [8:2064, 2:2065]                                                      str     Data section for quadrant A
    DAC3           -9.0002,-8.8889                                                       str     [V] set value, measured value
    CCDSIZE        4194,4256                                                             str     CCD size in pixels (rows, columns)
    AMPSECA        [1:2057, 1:2064]                                                      str     AMP section for quadrant A
    PRESECD        [4250:4256, 2130:4193]                                                str     Prescan section for quadrant D
    ORSECA         [8:2064, 2066:2097]                                                   str     Row overscan section for quadrant A
    CCDSECC        [1:2057, 2065:4128]                                                   str     CCD section for quadrant C
    CLOCK18        9.0,0.9999                                                            str     [V] high rail, low rail
    DETSECD        [2058:4114, 2065:4128]                                                str     Detector section for quadrant D
    CCDSECD        [2058:4114, 2065:4128]                                                str     CCD section for quadrant D
    CPUTEMP        57.1172                                                               float   [deg C] CCD controller CPU temperature
    DELAYS         20, 20, 25, 40, 7, 3000, 7, 7, 7, 7                                   str     [10] Delay settings
    DATASECD       [2193:4249, 2130:4193]                                                str     Data section for quadrant D
    BIASSECC       [2065:2128, 2130:4193]                                                str     Bias section for quadrant C
    CCDCFG         default_lbnl_20190717.cfg                                             str     CCD configuration file
    DATASECC       [8:2064, 2130:4193]                                                   str     Data section for quadrant C
    BIASSECD       [2129:2192, 2130:4193]                                                str     Bias section for quadrant D
    PRESECA        [1:7, 2:2065]                                                         str     Prescan section for quadrant A
    OFFSET6        2.0,6.0543                                                            str     [V] set value, measured value
    DETSECC        [1:2057, 2065:4128]                                                   str     Detector section for quadrant C
    DAC13          0.0,-0.0297                                                           str     [V] set value, measured value
    DETSECA        [1:2057, 1:2064]                                                      str     Detector section for quadrant A
    PRRSECC        [8:2064, 4194:4194]                                                   str     Row prescan section for quadrant C
    CLOCK12        9.9992,2.9993                                                         str     [V] high rail, low rail
    CASETEMP       56.8611                                                               float   [deg C] CCD controller case temperature
    BIASSECB       [2129:2192, 2:2065]                                                   str     Bias section for quadrant B
    OFFSET5        2.0,6.0174                                                            str     [V] set value, measured value
    CLOCK7         -2.0001,3.9999                                                        str     [V] high rail, low rail
    CLOCK8         9.9992,2.9993                                                         str     [V] high rail, low rail
    CAMERA         z6                                                                    str     Camera name
    PRESECB        [4250:4256, 2:2065]                                                   str     Prescan section for quadrant B
    TRIMSECB       [2193:4249, 2:2065]                                                   str     Trim section for quadrant B
    DAC17          20.0008,11.9316                                                       str     [V] set value, measured value
    DIGITIME       47.5453                                                               float   [s] Time to digitize image
    TRIMSECD       [2193:4249, 2130:4193]                                                str     Trim section for quadrant D
    DAC8           -25.0003,-24.6196                                                     str     [V] set value, measured value
    TRIMSECA       [8:2064, 2:2065]                                                      str     Trim section for quadrant A
    CLOCK14        9.9992,2.9993                                                         str     [V] high rail, low rail
    DAC0           -9.0002,-8.9713                                                       str     [V] set value, measured value
    CDSPARMS       400, 400, 8, 2000                                                     str     CDS parameters
    DAC1           -9.0002,-8.9507                                                       str     [V] set value, measured value
    ORSECC         [8:2064, 2098:2129]                                                   str     Row overscan section for quadrant C
    ORSECB         [2193:4249, 2066:2097]                                                str     Row overscan section for quadrant B
    CCDNAME        CCDSM7Z                                                               str     CCD name
    REQTIME        300.0                                                                 float   [s] Requested exposure time
    OBSID          kp4m20201221t023911                                                   str     Unique observation identifier
    PROCTYPE       RAW                                                                   str     Data processing level
    PRODTYPE       image                                                                 str     Data product type
    CHECKSUM       LfaELdXDLdaDLdUD                                                      str     HDU checksum updated 2022-02-14T08:22:45
    DATASUM        1867608608                                                            str     data unit checksum updated 2022-02-14T08:22:45
    GAINA          1.387                                                                 float   e/ADU (gain applied to image)
    SATULEVA       61000.0                                                               float   saturation or non lin. level, in ADU, inc. bias
    OSTEPA         0.7319095199345611                                                    float   ADUs (max-min of median overscan per row)
    OMETHA         AVERAGE                                                               str     use average overscan
    OVERSCNA       1966.054034223049                                                     float   ADUs (gain not applied)
    OBSRDNA        2.176414404248625                                                     float   electrons (gain is applied)
    SATUELEA       81880.08305453263                                                     float   saturation or non lin. level, in electrons
    GAINB          1.518                                                                 float   e/ADU (gain applied to image)
    SATULEVB       65535.0                                                               float   saturation or non lin. level, in ADU, inc. bias
    OSTEPB         0.5937273930649098                                                    float   ADUs (max-min of median overscan per row)
    OMETHB         AVERAGE                                                               str     use average overscan
    OVERSCNB       1987.334317960662                                                     float   ADUs (gain not applied)
    OBSRDNB        2.29569819578003                                                      float   electrons (gain is applied)
    SATUELEB       96465.35650533572                                                     float   saturation or non lin. level, in electrons
    GAINC          1.534                                                                 float   e/ADU (gain applied to image)
    SATULEVC       40000.0                                                               float   saturation or non lin. level, in ADU, inc. bias
    OSTEPC         0.9199855706829112                                                    float   ADUs (max-min of median overscan per row)
    OMETHC         AVERAGE                                                               str     use average overscan
    OVERSCNC       1980.643479043017                                                     float   ADUs (gain not applied)
    OBSRDNC        2.511180716174036                                                     float   electrons (gain is applied)
    SATUELEC       58321.69290314802                                                     float   saturation or non lin. level, in electrons
    GAIND          1.554                                                                 float   e/ADU (gain applied to image)
    SATULEVD       62000.0                                                               float   saturation or non lin. level, in ADU, inc. bias
    OSTEPD         1.375711494358256                                                     float   ADUs (max-min of median overscan per row)
    OMETHD         AVERAGE                                                               str     use average overscan
    OVERSCND       1982.563334159938                                                     float   ADUs (gain not applied)
    OBSRDND        2.417154801423475                                                     float   electrons (gain is applied)
    SATUELED       93267.09657871546                                                     float   saturation or non lin. level, in electrons
    FIBERMIN       3000                                                                  int
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
    WAVEMIN        7520.0                                                                float   First wavelength [Angstroms]
    WAVEMAX        9824.0                                                                float   Last wavelength [Angstroms]
    WAVESTEP       0.8                                                                   float   Wavelength step size [Angstroms]
    SPECTER        0.10.0                                                                str     https://github.com/desihub/specter
    IN_PSF         SPECPROD/exposures/20201220/00069022/psf-z6-00069022.fits             str     Input sp
    IN_IMG         SPECPROD/preproc/20201220/00069022/preproc-z6-00069022.fits           str
    ORIG_PSF       SPECPROD/calibnight/20201220/psfnight-z6-20201220.fits                str
    BUNIT          10**+17 cm2 count s / erg                                             str     i.e. (elec/A) / (1e-17 erg/s/cm2/A)
    IN_FRAME       SPECPROD/exposures/20201220/00069022/frame-z6-00069022.fits           str
    IN_SKY         SPECPROD/exposures/20201220/00069022/sky-z6-00069022.fits             str
    FIBERFLT       SPECPROD/exposures/20201220/00069022/fiberflatexp-z6-00069022.fits    str
    STDMODEL       SPECPROD/exposures/20201220/00069022/stdstars-6-00069022.fits         str
    NTSSURVY [1]_  sv2                                                                   str     NTS survey name
    SP8NIRP [1]_   4.941e-08                                                             float   [mb] SP8 NIR pressure
    TCSPIDEC [1]_  1.0,0.0,0.0,0.0                                                       str     TCS PI settings (P, I (gain, error window, satu
    SP3REDP [1]_   5.506e-08                                                             float   [mb] SP3 red pressure
    USESPLITS [1]_ T                                                                     bool    Exposure splits are allowed
    SP9NIRP [1]_   5.207e-08                                                             float   [mb] SP9 NIR pressure
    SP0REDT [1]_   139.96                                                                float   [K] SP0 red temperature
    SP8REDT [1]_   139.94                                                                float   [K] SP8 red temperature
    SP2REDT [1]_   139.99                                                                float   [K] SP2 red temperature
    SEQSTART [1]_  2021-04-04T06:46:24.391377                                            str     Start time of sequence processing
    SP0NIRP [1]_   5.865e-08                                                             float   [mb] SP0 NIR pressure
    SP3NIRP [1]_   5.524e-08                                                             float   [mb] SP3 NIR pressure
    SP7REDT [1]_   139.99                                                                float   [K] SP7 red temperature
    PMSEEING [1]_  0.85                                                                  float   [arcsec] PlateMaker GFAPROC seeing
    SP6REDT [1]_   139.94                                                                float   [K] SP6 red temperature
    SP7NIRT [1]_   139.96                                                                float   [K] SP7 NIR temperature
    SP4BLUT [1]_   163.02                                                                float   [K] SP4 blue temperature
    ACTTEFF [1]_   1513.0686                                                             float   [s] Actual effective exposure time
    SP2NIRT [1]_   139.91                                                                float   [K] SP2 NIR temperature
    SP5NIRT [1]_   139.94                                                                float   [K] SP5 NIR temperature
    SP2BLUT [1]_   163.02                                                                float   [K] SP2 blue temperature
    SP1BLUP [1]_   7.808e-08                                                             float   [mb] SP1 blue pressure
    SP4REDP [1]_   4.72e-08                                                              float   [mb] SP4 red pressure
    SP8BLUP [1]_   8.119e-08                                                             float   [mb] SP8 blue pressure
    SP5BLUT [1]_   163.02                                                                float   [K] SP5 blue temperature
    SP2REDP [1]_   5.348e-08                                                             float   [mb] SP2 red pressure
    SP0REDP [1]_   5.012e-08                                                             float   [mb] SP0 red pressure
    SP2BLUP [1]_   7.391e-08                                                             float   [mb] SP2 blue pressure
    SP9NIRT [1]_   139.89                                                                float   [K] SP9 NIR temperature
    SP6NIRT [1]_   139.89                                                                float   [K] SP6 NIR temperature
    SP5BLUP [1]_   1.125e-07                                                             float   [mb] SP5 blue pressure
    TCSKDEC [1]_   0.3 0.003 0.00003                                                     str     TCS Kalman (dec)
    VISITIDS [1]_  89039                                                                 str     List of expids for a visit (same tile)
    SP6BLUT [1]_   163.02                                                                float   [K] SP6 blue temperature
    SP1BLUT [1]_   163.02                                                                float   [K] SP1 blue temperature
    TCSGRA [1]_    0.3                                                                   float   TCS simple gain (RA)
    SP5REDP [1]_   5.121e-08                                                             float   [mb] SP5 red pressure
    TCSKRA [1]_    0.3 0.003 0.00003                                                     str     TCS Kalman (RA)
    SP4REDT [1]_   140.01                                                                float   [K] SP4 red temperature
    SP8NIRT [1]_   139.99                                                                float   [K] SP8 NIR temperature
    SP0NIRT [1]_   139.89                                                                float   [K] SP0 NIR temperature
    SP6NIRP [1]_   2.811e-07                                                             float   [mb] SP6 NIR pressure
    SP6BLUP [1]_   7.054e-08                                                             float   [mb] SP6 blue pressure
    SP9BLUT [1]_   163.02                                                                float   [K] SP9 blue temperature
    SP4BLUP [1]_   4.868e-08                                                             float   [mb] SP4 blue pressure
    TCSPIRA [1]_   1.0,0.0,0.0,0.0                                                       str     TCS PI settings (P, I (gain, error window, satu
    SP7REDP [1]_   4.279e-08                                                             float   [mb] SP7 red pressure
    SP8BLUT [1]_   162.9                                                                 float   [K] SP8 blue temperature
    SP8REDP [1]_   8.401e-08                                                             float   [mb] SP8 red pressure
    SP3BLUT [1]_   163.02                                                                float   [K] SP3 blue temperature
    SPLITEXP [1]_  F                                                                     bool    Split exposure part of a visit
    SP3REDT [1]_   139.96                                                                float   [K] SP3 red temperature
    SUNDEC [1]_    5.800279                                                              float   [deg] Sun declination at start of exposure
    SP1NIRP [1]_   8.133e-08                                                             float   [mb] SP1 NIR pressure
    SP2NIRP [1]_   5.339e-08                                                             float   [mb] SP2 NIR pressure
    SUNRA [1]_     13.554748                                                             float   [deg] Sun RA at start of exposure
    SP6REDP [1]_   6.486e-08                                                             float   [mb] SP6 red pressure
    MOONSEP [1]_   113.991                                                               float   [deg] Moon Separation
    TCSGDEC [1]_   0.3                                                                   float   TCS simple gain (dec)
    TCSMFDEC [1]_  1                                                                     int     TCS moving filter length (dec)
    SP3NIRT [1]_   140.01                                                                float   [K] SP3 NIR temperature
    FRAMES [1]_    47                                                                    int     Number of Frames in Archive
    SP0BLUT [1]_   162.99                                                                float   [K] SP0 blue temperature
    SP9REDP [1]_   4.354e-08                                                             float   [mb] SP9 red pressure
    SEEING [1]_    0.8607                                                                float   [arcsec] ETC seeing
    SP9BLUP [1]_   1.208e-07                                                             float   [mb] SP9 blue pressure
    SP7BLUP [1]_   9.947e-08                                                             float   [mb] SP7 blue pressure
    SP4NIRT [1]_   139.96                                                                float   [K] SP4 NIR temperature
    SP9REDT [1]_   140.01                                                                float   [K] SP9 red temperature
    TCSMFRA [1]_   1                                                                     int     TCS moving filter length (RA)
    SP1NIRT [1]_   139.89                                                                float   [K] SP1 NIR temperature
    SP3BLUP [1]_   9.345e-08                                                             float   [mb] SP3 blue pressure
    PMTRANS [1]_   93.76                                                                 float   [%] PlateMaker GFAPROC transparency
    SP1REDT [1]_   139.89                                                                float   [K] SP1 red temperature
    SKYLEVEL [1]_  0.933                                                                 float   counts?] ETC sky level
    SP4NIRP [1]_   6.915e-08                                                             float   [mb] SP4 NIR pressure
    REQTEFF [1]_   1000.0                                                                float   [s] Requested effective exposure time
    SP7BLUT [1]_   163.02                                                                float   [K] SP7 blue temperature
    SP5REDT [1]_   139.99                                                                float   [K] SP5 red temperature
    SP7NIRP [1]_   6.211e-08                                                             float   [mb] SP7 NIR pressure
    SP1REDP [1]_   6.567e-08                                                             float   [mb] SP1 red pressure
    SP5NIRP [1]_   9.462e-08                                                             float   [mb] SP5 NIR pressure
    SP0BLUP [1]_   9.115e-08                                                             float   [mb] SP0 blue pressure
    BBKGMAXC [1]_  0.4492153969301811                                                    float
    BBKGMIND [1]_  -0.3135937336084521                                                   float
    BBKGMAXB [1]_  0.5049607921526409                                                    float
    BBKGMINA [1]_  -0.2211057823638513                                                   float
    BBKGMINB [1]_  -0.3689821920680901                                                   float
    BBKGMINC [1]_  -0.3614105403549326                                                   float
    BBKGMAXA [1]_  0.7513851072600307                                                    float
    BBKGMAXD [1]_  0.3423400768828577                                                    float
    SBPROF [1]_    ELG                                                                   str     Profile used by ETC
    CONVERGD [1]_  F                                                                     bool    Positioning loop converged (CNFRC&gt;0.95)
    TOTTEFF [1]_   1214.7279                                                             float   [s] Total effective exposure time for visit
    SLEWANGL [1]_  49.575                                                                float   [deg] Slew Angle
    POSCVFRC [1]_  0.4393                                                                float   Fraction of converged positioners
    USESPLIT [1]_  T                                                                     bool    Exposure splits are allowed
    SEQID [1]_     2 requests                                                            str     Exposure sequence identifier
    SEQTOT [1]_    2                                                                     int     Total number of exposures in sequence
    ETCFRACB [1]_  0.13642                                                               float   ETC transparency weighted average of FFRAC (BGS
    ETCFRACP [1]_  0.390556                                                              float   ETC transparency weighted average of FFRAC (PSF
    ETCTEFF [1]_   61.258228                                                             float   [s] ETC effective exposure time
    ETCFRACE [1]_  0.300922                                                              float   ETC transparency weighted average of FFRAC (ELG
    NTSPROG [1]_   BACKUP                                                                str     NTS program name
    ETCTHRUB [1]_  0.535631                                                              float   ETC averaged thruput (BGS profile)
    ETCSPLIT [1]_  1                                                                     int     ETC split sequence number for this visit
    ETCTRANS [1]_  0.745415                                                              float   ETC averaged TRANSP normalized to 1
    ETCREAL [1]_   348.878632                                                            float   [s] ETC real open shutter time
    ETCVERS [1]_   0.1.12-3-g12b54bb                                                     str     ETC version
    ETCTHRUP [1]_  0.518037                                                              float   ETC averaged thruput (PSF profile)
    MAXTIME [1]_   5400.0                                                                float   [s] Maximum exposure time for entire visit (fro
    ETCSKY [1]_    1.60973                                                               float   ETC averaged, normalized sky camera flux
    ESTTIME [1]_   1500.571                                                              float   [s] Estimated exposure time for visit (from ETC
    TRANSPAR [1]_  None                                                                  float   ETC/PM transparency
    ETCPROF [1]_   PSF                                                                   str     ETC source brightness profile
    MINTIME [1]_   60.0                                                                  float   [s] Minimum exposure time (from NTS, used by ET
    PMTRANSP [1]_  115.88                                                                float   [%] PlateMaker GFAPROC transparency
    ETCSEENG [1]_  2.1165                                                                float   [arcsec] ETC seeing
    ACQFWHM [1]_   2.116458                                                              float   [arcsec] FWHM of guide star PSF in acquisition
    ETCTHRUE [1]_  0.544181                                                              float   ETC averaged thruput (ELG profile)
    ETCPREV [1]_   0.0                                                                   float   [s] ETC cummulative t_eff for visit
    ============== ===================================================================== ======= ===============================================

Data: FITS image [float32, 2326x500]

HDU1
----

EXTNAME = IVAR

Inverse variance of flux calibration array.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2326             int
    NAXIS2   500              int
    CHECKSUM YXHMcU9JZUGJaU9J str  HDU checksum updated 2021-07-08T16:29:44
    DATASUM  2925906445       str  data unit checksum updated 2021-07-08T16:29:44
    ======== ================ ==== ==============================================

Data: FITS image [float32, 2326x500]

HDU2
----

EXTNAME = MASK

Mask of flux calibration model; 0=good. See the :doc:`bitmask documentation </bitmasks>` page for the definition of the bits.
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
    CHECKSUM WHahaERgZEXgaEXg str  HDU checksum updated 2021-07-08T16:29:44
    DATASUM  68479139         str  data unit checksum updated 2021-07-08T16:29:44
    ======== ================ ==== ==============================================

Data: FITS image [int32, 2326x500]

HDU3
----

EXTNAME = WAVELENGTH

Wavelengths at which the flux calibration is evaluated, in Angstrom. Note the wavelength is in the solar system barycenter frame, so that the calibration can be directly applied to the science frame fluxes which are on the same wavelength grid. In order to compare the
calibration from different exposures, one has to convert back the wavelength array to the observer frame, by dividing it by Doppler factor saved in header keyword HELIOCOR in HDU0. See also the frame :ref:`WAVELENGTH documentation <frame-hdu3-wavelength>` for more details.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2326             int
    BUNIT    Angstrom         str
    CHECKSUM PAF9Q8D6PAD6P5D6 str  HDU checksum updated 2021-07-08T16:29:44
    DATASUM  1502044794       str  data unit checksum updated 2021-07-08T16:29:44
    ======== ================ ==== ==============================================

Data: FITS image [float32, 2326]

.. _FIBERCORR:

HDU4
----

EXTNAME = FIBERCORR

Table with the following adimentional scaling factors for each fiber:

FLAT_TO_PSF_FLUX  = normalized ratio of the flat-fielded flux to the total flux for point sources; **already** included in the flux calibration array.

PSF_TO_FIBER_FLUX = ratio of total flux to 'fiber flux'; **not** included in the flux calibration array.

A 'fiber flux' is the flux one would collect in a 1.5 arcsec diameter aperture centered on the object when observed with a 1 arcsec FWHM Gaussian seeing. The variation of plate scale in the focal plane, the seeing condition of the observations, the fiber positioning errors, and the intrinsic angular size of the sources have been considered to compute those scaling factors.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   16               int  length of dimension 1
    NAXIS2   500              int  length of dimension 2
    ENCODING ascii            str
    CHECKSUM GgA3Gg60GgA0Gg50 str  HDU checksum updated 2021-07-08T16:29:44
    DATASUM  2049692696       str  data unit checksum updated 2021-07-08T16:29:44
    ======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

================= ======= ===== ================================================================
Name              Type    Units Description
================= ======= ===== ================================================================
FLAT_TO_PSF_FLUX  float64       adimentional factor applied to calib to convert flat to psf flux
PSF_TO_FIBER_FLUX float64       adimentional factor to apply to convert psf to fiber flux
================= ======= ===== ================================================================

HDU5
----

EXTNAME = STDSTAR_FIBERMAP

Fibermap of what targets were assigned to what fibers.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ============== ===================================================================================================================================================================================================================================================================================================== ======= ==============================================
    KEY            Example Value                                                                                                                                                                                                                                                                                         Type    Comment
    ============== ===================================================================================================================================================================================================================================================================================================== ======= ==============================================
    NAXIS1 [1]_    385                                                                                                                                                                                                                                                                                                   int     length of dimension 1
    NAXIS2 [1]_    18                                                                                                                                                                                                                                                                                                    int     length of dimension 2
    TILEID [1]_    80616                                                                                                                                                                                                                                                                                                 int
    TILERA [1]_    356.0                                                                                                                                                                                                                                                                                                 float
    TILEDEC [1]_   29.0                                                                                                                                                                                                                                                                                                  float
    FIELDROT [1]_  -0.00962199210064233                                                                                                                                                                                                                                                                                  float
    FA_PLAN [1]_   2022-07-01T00:00:00.000                                                                                                                                                                                                                                                                               str
    FA_HA [1]_     0.0                                                                                                                                                                                                                                                                                                   float
    FA_RUN [1]_    2020-03-06T00:00:00                                                                                                                                                                                                                                                                                   str
    FA_M_GFA [1]_  0.4                                                                                                                                                                                                                                                                                                   float
    FA_M_PET [1]_  0.4                                                                                                                                                                                                                                                                                                   float
    FA_M_POS [1]_  0.05                                                                                                                                                                                                                                                                                                  float
    REQRA [1]_     356.0                                                                                                                                                                                                                                                                                                 float
    REQDEC [1]_    29.0                                                                                                                                                                                                                                                                                                  float
    FIELDNUM [1]_  0                                                                                                                                                                                                                                                                                                     int
    FA_VER [1]_    2.0.0.dev2618                                                                                                                                                                                                                                                                                         str
    FA_SURV [1]_   sv1                                                                                                                                                                                                                                                                                                   str
    LONGSTRN [1]_  OGIP 1.0                                                                                                                                                                                                                                                                                              str
    GFA [1]_       /data/target/catalogs/dr9/0.47.0/gfas                                                                                                                                                                                                                                                                 str
    SKY [1]_       /data/target/catalogs/dr9/0.47.0/skies                                                                                                                                                                                                                                                                str
    SKYSUPP [1]_   /data/target/catalogs/gaiadr2/0.47.0/skies-supp                                                                                                                                                                                                                                                       str
    TARG [1]_      /data/target/catalogs/dr9/0.47.0/targets/sv1/resolve/bright/                                                                                                                                                                                                                                          str
    FAFLAVOR [1]_  sv1bgsmws                                                                                                                                                                                                                                                                                             str
    FAOUTDIR [1]_  /software/datasystems/users/raichoor/fiberassign-test/desi-sv1-20201218/                                                                                                                                                                                                                              str
    PMTIME [1]_    2020-12-18T00:00:00.000                                                                                                                                                                                                                                                                               str
    RUNDATE [1]_   2020-03-06T00:00:00                                                                                                                                                                                                                                                                                   str
    SCTARG [1]_    STD_WD,BGS_ANY,MWS_ANY                                                                                                                                                                                                                                                                                str
    OBSCON [1]_    DARK|GRAY|BRIGHT                                                                                                                                                                                                                                                                                      str
    MODULE [1]_    CI                                                                                                                                                                                                                                                                                                    str
    EXPID [1]_     69022                                                                                                                                                                                                                                                                                                 int
    EXPFRAME [1]_  0                                                                                                                                                                                                                                                                                                     int
    COSMSPLT [1]_  F                                                                                                                                                                                                                                                                                                     bool
    MAXSPLIT [1]_  0                                                                                                                                                                                                                                                                                                     int
    SPLITIDS [1]_  69022                                                                                                                                                                                                                                                                                                 str
    FIBASSGN [1]_  /data/tiles/SVN_tiles/080/fiberassign-080616.fits                                                                                                                                                                                                                                                     str
    FLAVOR [1]_    science                                                                                                                                                                                                                                                                                               str
    OBSTYPE [1]_   SCIENCE                                                                                                                                                                                                                                                                                               str
    SEQUENCE [1]_  DESI                                                                                                                                                                                                                                                                                                  str
    MANIFEST [1]_  F                                                                                                                                                                                                                                                                                                     bool
    OBJECT [1]_                                                                                                                                                                                                                                                                                                          str
    PURPOSE [1]_   Commissioning                                                                                                                                                                                                                                                                                         str
    PROGRAM [1]_   SV1 BGS+MWS tile 80616                                                                                                                                                                                                                                                                                str
    PROPID [1]_    2019B-5000                                                                                                                                                                                                                                                                                            str
    OBSERVER [1]_  DESIObserver                                                                                                                                                                                                                                                                                          str
    LEAD [1]_      RunManager                                                                                                                                                                                                                                                                                            str
    INSTRUME [1]_  DESI                                                                                                                                                                                                                                                                                                  str
    OBSERVAT [1]_  KPNO                                                                                                                                                                                                                                                                                                  str
    OBS-LAT [1]_   31.96403                                                                                                                                                                                                                                                                                              str
    OBS-LONG [1]_  -111.59989                                                                                                                                                                                                                                                                                            str
    OBS-ELEV [1]_  2097.0                                                                                                                                                                                                                                                                                                float
    TELESCOP [1]_  KPNO 4.0-m telescope                                                                                                                                                                                                                                                                                  str
    CORRCTOR [1]_  DESI Corrector                                                                                                                                                                                                                                                                                        str
    SEQNUM [1]_    1                                                                                                                                                                                                                                                                                                     int
    NIGHT [1]_     20201220                                                                                                                                                                                                                                                                                              int
    TIMESYS [1]_   UTC                                                                                                                                                                                                                                                                                                   str
    DATE-OBS [1]_  2020-12-21T02:36:32.099838                                                                                                                                                                                                                                                                            str
    MJD-OBS [1]_   59204.10870486                                                                                                                                                                                                                                                                                        float
    OPENSHUT [1]_  2020-12-21T02:36:32.099838                                                                                                                                                                                                                                                                            str
    CAMSHUT [1]_   open                                                                                                                                                                                                                                                                                                  str
    ST [1]_        01:10:39.210                                                                                                                                                                                                                                                                                          str
    ACQTIME [1]_   15.0                                                                                                                                                                                                                                                                                                  float
    GUIDTIME [1]_  5.0                                                                                                                                                                                                                                                                                                   float
    FOCSTIME [1]_  60.0                                                                                                                                                                                                                                                                                                  float
    SKYTIME [1]_   60.0                                                                                                                                                                                                                                                                                                  float
    WHITESPT [1]_  F                                                                                                                                                                                                                                                                                                     bool
    ZENITH [1]_    F                                                                                                                                                                                                                                                                                                     bool
    SEANNEX [1]_   F                                                                                                                                                                                                                                                                                                     bool
    BEYONDP [1]_   F                                                                                                                                                                                                                                                                                                     bool
    FIDUCIAL [1]_  off                                                                                                                                                                                                                                                                                                   str
    BACKLIT [1]_   off                                                                                                                                                                                                                                                                                                   str
    AIRMASS [1]_   1.060311                                                                                                                                                                                                                                                                                              float
    FOCUS [1]_     1426.5,-501.4,81.0,-2.6,42.3,169.2                                                                                                                                                                                                                                                                    str
    VCCD [1]_      ON                                                                                                                                                                                                                                                                                                    str
    TRUSTEMP [1]_  11.767                                                                                                                                                                                                                                                                                                float
    PMIRTEMP [1]_  8.925                                                                                                                                                                                                                                                                                                 float
    PMREADY [1]_   T                                                                                                                                                                                                                                                                                                     bool
    PMCOVER [1]_   open                                                                                                                                                                                                                                                                                                  str
    PMCOOL [1]_    off                                                                                                                                                                                                                                                                                                   str
    DOMSHUTU [1]_  open                                                                                                                                                                                                                                                                                                  str
    DOMSHUTL [1]_  open                                                                                                                                                                                                                                                                                                  str
    DOMLIGHH [1]_  off                                                                                                                                                                                                                                                                                                   str
    DOMLIGHL [1]_  off                                                                                                                                                                                                                                                                                                   str
    DOMEAZ [1]_    255.166                                                                                                                                                                                                                                                                                               float
    DOMINPOS [1]_  T                                                                                                                                                                                                                                                                                                     bool
    EQUINOX [1]_   2000.0                                                                                                                                                                                                                                                                                                float
    GUIDOFFR [1]_  -0.052283                                                                                                                                                                                                                                                                                             float
    GUIDOFFD [1]_  0.136634                                                                                                                                                                                                                                                                                              float
    MOONDEC [1]_   -8.975162                                                                                                                                                                                                                                                                                             float
    MOONRA [1]_    352.538429                                                                                                                                                                                                                                                                                            float
    MOUNTAZ [1]_   266.70224                                                                                                                                                                                                                                                                                             float
    MOUNTDEC [1]_  28.999221                                                                                                                                                                                                                                                                                             float
    MOUNTEL [1]_   71.039837                                                                                                                                                                                                                                                                                             float
    MOUNTHA [1]_   21.769281                                                                                                                                                                                                                                                                                             float
    INCTRL [1]_    T                                                                                                                                                                                                                                                                                                     bool
    INPOS [1]_     T                                                                                                                                                                                                                                                                                                     bool
    MNTOFFD [1]_   -15.76                                                                                                                                                                                                                                                                                                float
    MNTOFFR [1]_   29.32                                                                                                                                                                                                                                                                                                 float
    PARALLAC [1]_  75.635085                                                                                                                                                                                                                                                                                             float
    SKYDEC [1]_    28.999221                                                                                                                                                                                                                                                                                             float
    SKYRA [1]_     355.996551                                                                                                                                                                                                                                                                                            float
    TARGTDEC [1]_  28.999221                                                                                                                                                                                                                                                                                             float
    TARGTRA [1]_   355.996551                                                                                                                                                                                                                                                                                            float
    TARGTAZ [1]_   267.074049                                                                                                                                                                                                                                                                                            float
    TARGTEL [1]_   70.563787                                                                                                                                                                                                                                                                                             float
    TRGTOFFD [1]_  0.0                                                                                                                                                                                                                                                                                                   float
    TRGTOFFR [1]_  0.0                                                                                                                                                                                                                                                                                                   float
    ZD [1]_        19.436213                                                                                                                                                                                                                                                                                             float
    TCSST [1]_     01:13:18.668                                                                                                                                                                                                                                                                                          str
    TCSMJD [1]_    59204.110981                                                                                                                                                                                                                                                                                          float
    USEETC [1]_    F                                                                                                                                                                                                                                                                                                     bool
    ACQCAM [1]_    GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                                                                                                                                                                                                                                                             str
    GUIDECAM [1]_  GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                                                                                                                                                                                                                                                             str
    FOCUSCAM [1]_  FOCUS1,FOCUS4,FOCUS6,FOCUS9                                                                                                                                                                                                                                                                           str
    SKYCAM [1]_    SKYCAM0,SKYCAM1                                                                                                                                                                                                                                                                                       str
    REQADC [1]_    65.78,85.28                                                                                                                                                                                                                                                                                           str
    ADCCORR [1]_   T                                                                                                                                                                                                                                                                                                     bool
    ADC1PHI [1]_   65.780005                                                                                                                                                                                                                                                                                             float
    ADC2PHI [1]_   85.279991                                                                                                                                                                                                                                                                                             float
    ADC1HOME [1]_  F                                                                                                                                                                                                                                                                                                     bool
    ADC2HOME [1]_  F                                                                                                                                                                                                                                                                                                     bool
    ADC1NREV [1]_  -1.0                                                                                                                                                                                                                                                                                                  float
    ADC2NREV [1]_  0.0                                                                                                                                                                                                                                                                                                   float
    ADC1STAT [1]_  STOPPED                                                                                                                                                                                                                                                                                               str
    ADC2STAT [1]_  STOPPED                                                                                                                                                                                                                                                                                               str
    USESKY [1]_    T                                                                                                                                                                                                                                                                                                     bool
    USEFOCUS [1]_  T                                                                                                                                                                                                                                                                                                     bool
    HEXPOS [1]_    1426.5,-501.3,81.0,-2.6,42.3,171.9                                                                                                                                                                                                                                                                    str
    HEXTRIM [1]_   0.0,0.0,0.0,0.0,0.0,0.0                                                                                                                                                                                                                                                                               str
    USEROTAT [1]_  T                                                                                                                                                                                                                                                                                                     bool
    ROTOFFST [1]_  167.1                                                                                                                                                                                                                                                                                                 float
    ROTENBLD [1]_  T                                                                                                                                                                                                                                                                                                     bool
    ROTRATE [1]_   0.0                                                                                                                                                                                                                                                                                                   float
    RESETROT [1]_  F                                                                                                                                                                                                                                                                                                     bool
    USEPOS [1]_    T                                                                                                                                                                                                                                                                                                     bool
    PETALS [1]_    PETAL0,PETAL1,PETAL2,PETAL3,PETAL4,PETAL5,PETAL6,PETAL7,PETAL8,PETAL9                                                                                                                                                                                                                                 str
    POSCYCLE [1]_  1                                                                                                                                                                                                                                                                                                     int
    POSONTGT [1]_  3626                                                                                                                                                                                                                                                                                                  int
    POSONFRC [1]_  0.8613                                                                                                                                                                                                                                                                                                float
    POSDISAB [1]_  37                                                                                                                                                                                                                                                                                                    int
    POSENABL [1]_  4210                                                                                                                                                                                                                                                                                                  int
    POSRMS [1]_    0.0171                                                                                                                                                                                                                                                                                                float
    POSITER [1]_   1                                                                                                                                                                                                                                                                                                     int
    POSFRACT [1]_  0.95                                                                                                                                                                                                                                                                                                  float
    POSTOLER [1]_  0.01                                                                                                                                                                                                                                                                                                  float
    POSMVALL [1]_  T                                                                                                                                                                                                                                                                                                     bool
    USEGUIDR [1]_  T                                                                                                                                                                                                                                                                                                     bool
    GUIDMODE [1]_  catalog                                                                                                                                                                                                                                                                                               str
    USEAOS [1]_    F                                                                                                                                                                                                                                                                                                     bool
    USEDONUT [1]_  T                                                                                                                                                                                                                                                                                                     bool
    USESPCTR [1]_  T                                                                                                                                                                                                                                                                                                     bool
    SPCGRPHS [1]_  SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                                                                                                                                                                                                                                                               str
    ILLSPECS [1]_  SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                                                                                                                                                                                                                                                               str
    CCDSPECS [1]_  SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                                                                                                                                                                                                                                                               str
    TDEWPNT [1]_   -16.043                                                                                                                                                                                                                                                                                               float
    TAIRFLOW [1]_  0.0                                                                                                                                                                                                                                                                                                   float
    TAIRITMP [1]_  11.8                                                                                                                                                                                                                                                                                                  float
    TAIROTMP [1]_  11.7                                                                                                                                                                                                                                                                                                  float
    TAIRTEMP [1]_  10.65                                                                                                                                                                                                                                                                                                 float
    TCASITMP [1]_  0.0                                                                                                                                                                                                                                                                                                   float
    TCASOTMP [1]_  10.8                                                                                                                                                                                                                                                                                                  float
    TCSITEMP [1]_  9.3                                                                                                                                                                                                                                                                                                   float
    TCSOTEMP [1]_  10.8                                                                                                                                                                                                                                                                                                  float
    TCIBTEMP [1]_  0.0                                                                                                                                                                                                                                                                                                   float
    TCIMTEMP [1]_  0.0                                                                                                                                                                                                                                                                                                   float
    TCITTEMP [1]_  0.0                                                                                                                                                                                                                                                                                                   float
    TCOSTEMP [1]_  0.0                                                                                                                                                                                                                                                                                                   float
    TCOWTEMP [1]_  0.0                                                                                                                                                                                                                                                                                                   float
    TDBTEMP [1]_   9.3                                                                                                                                                                                                                                                                                                   float
    TFLOWIN [1]_   0.0                                                                                                                                                                                                                                                                                                   float
    TFLOWOUT [1]_  0.0                                                                                                                                                                                                                                                                                                   float
    TGLYCOLI [1]_  9.9                                                                                                                                                                                                                                                                                                   float
    TGLYCOLO [1]_  9.8                                                                                                                                                                                                                                                                                                   float
    THINGES [1]_   11.4                                                                                                                                                                                                                                                                                                  float
    THINGEW [1]_   11.2                                                                                                                                                                                                                                                                                                  float
    TPMAVERT [1]_  8.931                                                                                                                                                                                                                                                                                                 float
    TPMDESIT [1]_  7.0                                                                                                                                                                                                                                                                                                   float
    TPMEIBT [1]_   8.6                                                                                                                                                                                                                                                                                                   float
    TPMEITT [1]_   8.6                                                                                                                                                                                                                                                                                                   float
    TPMEOBT [1]_   8.5                                                                                                                                                                                                                                                                                                   float
    TPMEOTT [1]_   9.0                                                                                                                                                                                                                                                                                                   float
    TPMNIBT [1]_   8.4                                                                                                                                                                                                                                                                                                   float
    TPMNITT [1]_   8.9                                                                                                                                                                                                                                                                                                   float
    TPMNOBT [1]_   8.8                                                                                                                                                                                                                                                                                                   float
    TPMNOTT [1]_   9.1                                                                                                                                                                                                                                                                                                   float
    TPMRTDT [1]_   9.0                                                                                                                                                                                                                                                                                                   float
    TPMSIBT [1]_   8.6                                                                                                                                                                                                                                                                                                   float
    TPMSITT [1]_   8.8                                                                                                                                                                                                                                                                                                   float
    TPMSOBT [1]_   8.2                                                                                                                                                                                                                                                                                                   float
    TPMSOTT [1]_   8.9                                                                                                                                                                                                                                                                                                   float
    TPMSTAT [1]_   ready                                                                                                                                                                                                                                                                                                 str
    TPMWIBT [1]_   8.2                                                                                                                                                                                                                                                                                                   float
    TPMWITT [1]_   9.1                                                                                                                                                                                                                                                                                                   float
    TPMWOBT [1]_   8.3                                                                                                                                                                                                                                                                                                   float
    TPMWOTT [1]_   8.9                                                                                                                                                                                                                                                                                                   float
    TPCITEMP [1]_  8.5                                                                                                                                                                                                                                                                                                   float
    TPCOTEMP [1]_  8.6                                                                                                                                                                                                                                                                                                   float
    TPR1HUM [1]_   0.0                                                                                                                                                                                                                                                                                                   float
    TPR1TEMP [1]_  0.0                                                                                                                                                                                                                                                                                                   float
    TPR2HUM [1]_   0.0                                                                                                                                                                                                                                                                                                   float
    TPR2TEMP [1]_  0.0                                                                                                                                                                                                                                                                                                   float
    TSERVO [1]_    40.0                                                                                                                                                                                                                                                                                                  float
    TTRSTEMP [1]_  11.4                                                                                                                                                                                                                                                                                                  float
    TTRWTEMP [1]_  11.0                                                                                                                                                                                                                                                                                                  float
    TTRUETBT [1]_  -4.2                                                                                                                                                                                                                                                                                                  float
    TTRUETTT [1]_  11.2                                                                                                                                                                                                                                                                                                  float
    TTRUNTBT [1]_  10.9                                                                                                                                                                                                                                                                                                  float
    TTRUNTTT [1]_  11.2                                                                                                                                                                                                                                                                                                  float
    TTRUSTBT [1]_  10.7                                                                                                                                                                                                                                                                                                  float
    TTRUSTST [1]_  10.8                                                                                                                                                                                                                                                                                                  float
    TTRUSTTT [1]_  11.1                                                                                                                                                                                                                                                                                                  float
    TTRUTSBT [1]_  11.8                                                                                                                                                                                                                                                                                                  float
    TTRUTSMT [1]_  11.8                                                                                                                                                                                                                                                                                                  float
    TTRUTSTT [1]_  11.8                                                                                                                                                                                                                                                                                                  float
    TTRUWTBT [1]_  10.5                                                                                                                                                                                                                                                                                                  float
    TTRUWTTT [1]_  10.9                                                                                                                                                                                                                                                                                                  float
    ALARM [1]_     F                                                                                                                                                                                                                                                                                                     bool
    ALARM-ON [1]_  F                                                                                                                                                                                                                                                                                                     bool
    BATTERY [1]_   100.0                                                                                                                                                                                                                                                                                                 float
    SECLEFT [1]_   5178.0                                                                                                                                                                                                                                                                                                float
    UPSSTAT [1]_   System Normal - On Line(7)                                                                                                                                                                                                                                                                            str
    INAMPS [1]_    70.4                                                                                                                                                                                                                                                                                                  float
    OUTWATTS [1]_  5000.0,7200.0,4800.0                                                                                                                                                                                                                                                                                  str
    COMPDEW [1]_   -12.9                                                                                                                                                                                                                                                                                                 float
    COMPHUM [1]_   7.4                                                                                                                                                                                                                                                                                                   float
    COMPAMB [1]_   19.5                                                                                                                                                                                                                                                                                                  float
    COMPTEMP [1]_  24.5                                                                                                                                                                                                                                                                                                  float
    DEWPOINT [1]_  11.5                                                                                                                                                                                                                                                                                                  float
    HUMIDITY [1]_  10.0                                                                                                                                                                                                                                                                                                  float
    PRESSURE [1]_  795.0                                                                                                                                                                                                                                                                                                 float
    OUTTEMP [1]_   0.0                                                                                                                                                                                                                                                                                                   float
    WINDDIR [1]_   55.0                                                                                                                                                                                                                                                                                                  float
    WINDSPD [1]_   27.3                                                                                                                                                                                                                                                                                                  float
    GUST [1]_      20.6                                                                                                                                                                                                                                                                                                  float
    AMNIENTN [1]_  13.5                                                                                                                                                                                                                                                                                                  float
    CFLOOR [1]_    8.9                                                                                                                                                                                                                                                                                                   float
    NWALLIN [1]_   13.9                                                                                                                                                                                                                                                                                                  float
    NWALLOUT [1]_  9.6                                                                                                                                                                                                                                                                                                   float
    WWALLIN [1]_   12.9                                                                                                                                                                                                                                                                                                  float
    WWALLOUT [1]_  10.6                                                                                                                                                                                                                                                                                                  float
    AMBIENTS [1]_  14.8                                                                                                                                                                                                                                                                                                  float
    FLOOR [1]_     12.6                                                                                                                                                                                                                                                                                                  float
    EWALLCMP [1]_  10.8                                                                                                                                                                                                                                                                                                  float
    EWALLCOU [1]_  10.6                                                                                                                                                                                                                                                                                                  float
    ROOF [1]_      10.3                                                                                                                                                                                                                                                                                                  float
    ROOFAMB [1]_   10.6                                                                                                                                                                                                                                                                                                  float
    DOMEBLOW [1]_  10.4                                                                                                                                                                                                                                                                                                  float
    DOMEBUP [1]_   10.7                                                                                                                                                                                                                                                                                                  float
    DOMELLOW [1]_  10.8                                                                                                                                                                                                                                                                                                  float
    DOMELUP [1]_   10.8                                                                                                                                                                                                                                                                                                  float
    DOMERLOW [1]_  10.6                                                                                                                                                                                                                                                                                                  float
    DOMERUP [1]_   10.5                                                                                                                                                                                                                                                                                                  float
    PLATFORM [1]_  10.4                                                                                                                                                                                                                                                                                                  float
    SHACKC [1]_    14.4                                                                                                                                                                                                                                                                                                  float
    SHACKW [1]_    13.7                                                                                                                                                                                                                                                                                                  float
    STAIRSL [1]_   10.5                                                                                                                                                                                                                                                                                                  float
    STAIRSM [1]_   10.4                                                                                                                                                                                                                                                                                                  float
    STAIRSU [1]_   10.6                                                                                                                                                                                                                                                                                                  float
    TELBASE [1]_   9.6                                                                                                                                                                                                                                                                                                   float
    UTILWALL [1]_  11.1                                                                                                                                                                                                                                                                                                  float
    UTILROOM [1]_  10.9                                                                                                                                                                                                                                                                                                  float
    RADESYS [1]_   FK5                                                                                                                                                                                                                                                                                                   str
    TNFSPROC [1]_  8.1963                                                                                                                                                                                                                                                                                                float
    TGFAPROC [1]_  7.9212                                                                                                                                                                                                                                                                                                float
    SIMGFAP [1]_   F                                                                                                                                                                                                                                                                                                     bool
    USEFVC [1]_    T                                                                                                                                                                                                                                                                                                     bool
    USEFID [1]_    T                                                                                                                                                                                                                                                                                                     bool
    USEILLUM [1]_  T                                                                                                                                                                                                                                                                                                     bool
    USEXSRVR [1]_  T                                                                                                                                                                                                                                                                                                     bool
    USEOPENL [1]_  T                                                                                                                                                                                                                                                                                                     bool
    STOPGUDR [1]_  T                                                                                                                                                                                                                                                                                                     bool
    STOPFOCS [1]_  T                                                                                                                                                                                                                                                                                                     bool
    STOPSKY [1]_   T                                                                                                                                                                                                                                                                                                     bool
    KEEPGUDR [1]_  F                                                                                                                                                                                                                                                                                                     bool
    KEEPFOCS [1]_  F                                                                                                                                                                                                                                                                                                     bool
    KEEPSKY [1]_   F                                                                                                                                                                                                                                                                                                     bool
    REACQUIR [1]_  F                                                                                                                                                                                                                                                                                                     bool
    FILENAME [1]_  /exposures/desi/20201220/00069022/desi-00069022.fits.fz                                                                                                                                                                                                                                               str
    EXCLUDED [1]_                                                                                                                                                                                                                                                                                                        str
    DOSVER [1]_    trunk                                                                                                                                                                                                                                                                                                 str
    OCSVER [1]_    1.2                                                                                                                                                                                                                                                                                                   float
    CONSTVER [1]_  DESI:CURRENT                                                                                                                                                                                                                                                                                          str
    INIFILE [1]_   /data/msdos/dos_home/architectures/kpno/desi.ini                                                                                                                                                                                                                                                      str
    REQTIME [1]_   300.0                                                                                                                                                                                                                                                                                                 float
    FVCTIME [1]_   2.0                                                                                                                                                                                                                                                                                                   float
    SIMGFACQ [1]_  F                                                                                                                                                                                                                                                                                                     bool
    POSCNVGD [1]_  F                                                                                                                                                                                                                                                                                                     bool
    GUIEXPID [1]_  69022                                                                                                                                                                                                                                                                                                 int
    IGFRMNUM [1]_  12                                                                                                                                                                                                                                                                                                    int
    FOCEXPID [1]_  69022                                                                                                                                                                                                                                                                                                 int
    IFFRMNUM [1]_  1                                                                                                                                                                                                                                                                                                     int
    SKYEXPID [1]_  69022                                                                                                                                                                                                                                                                                                 int
    ISFRMNUM [1]_  1                                                                                                                                                                                                                                                                                                     int
    FGFRMNUM [1]_  46                                                                                                                                                                                                                                                                                                    int
    FFFRMNUM [1]_  6                                                                                                                                                                                                                                                                                                     int
    FSFRMNUM [1]_  5                                                                                                                                                                                                                                                                                                     int
    FRAMES [1]_    47                                                                                                                                                                                                                                                                                                    int
    DELTARA [1]_   None                                                                                                                                                                                                                                                                                                  float
    DELTADEC [1]_  None                                                                                                                                                                                                                                                                                                  float
    GSGUIDE0 [1]_  (980.05,685.98),(878.97,731.68)                                                                                                                                                                                                                                                                       str
    GSGUIDE2 [1]_  (372.65,939.43),(784.50,1529.96)                                                                                                                                                                                                                                                                      str
    GSGUIDE3 [1]_  (365.22,1423.83),(249.12,411.52)                                                                                                                                                                                                                                                                      str
    GSGUIDE5 [1]_  (848.52,78.26),(516.16,1410.54)                                                                                                                                                                                                                                                                       str
    GSGUIDE7 [1]_  (540.95,1848.95),(504.68,831.62)                                                                                                                                                                                                                                                                      str
    GSGUIDE8 [1]_  (720.29,552.69),(499.80,465.13)                                                                                                                                                                                                                                                                       str
    ARCHIVE [1]_   /exposures/desi/20201220/00069022/guide-00069022.fits.fz                                                                                                                                                                                                                                              str
    GUIDEFIL [1]_  guide-00069022.fits.fz                                                                                                                                                                                                                                                                                str
    COORDFIL [1]_  coordinates-00069022.fits                                                                                                                                                                                                                                                                             str
    TIME-OBS [1]_  02:39:11.845920                                                                                                                                                                                                                                                                                       str
    EXPTIME [1]_   300.007                                                                                                                                                                                                                                                                                               float
    VCCDON [1]_    2020-12-09T21:23:25.472733                                                                                                                                                                                                                                                                            str
    VCCDSEC [1]_   969696.0                                                                                                                                                                                                                                                                                              float
    SPECGRPH [1]_  6                                                                                                                                                                                                                                                                                                     int
    SPECID [1]_    7                                                                                                                                                                                                                                                                                                     int
    FEEBOX [1]_    lbnl061                                                                                                                                                                                                                                                                                               str
    VESSEL [1]_    21                                                                                                                                                                                                                                                                                                    int
    FEEVER [1]_    v20160312                                                                                                                                                                                                                                                                                             str
    FEEPOWER [1]_  ON                                                                                                                                                                                                                                                                                                    str
    FEEDMASK [1]_  2134851391                                                                                                                                                                                                                                                                                            int
    FEECMASK [1]_  1048575                                                                                                                                                                                                                                                                                               int
    CCDTEMP [1]_   -134.1517                                                                                                                                                                                                                                                                                             float
    PRESECC [1]_   [1:7, 2130:4193]                                                                                                                                                                                                                                                                                      str
    CLOCK13 [1]_   9.9992,2.9993                                                                                                                                                                                                                                                                                         str
    DETECTOR [1]_  M1-51                                                                                                                                                                                                                                                                                                 str
    SETTINGS [1]_  detectors_sm_20191211.json                                                                                                                                                                                                                                                                            str
    PRRSECA [1]_   [8:2064, 1:1]                                                                                                                                                                                                                                                                                         str
    CLOCK11 [1]_   9.9992,2.9993                                                                                                                                                                                                                                                                                         str
    OFFSET2 [1]_   0.4000000059604645,-8.9507                                                                                                                                                                                                                                                                            str
    AMPSECC [1]_   [1:2057, 4128:2065]                                                                                                                                                                                                                                                                                   str
    DAC11 [1]_     -25.0003,-25.0351                                                                                                                                                                                                                                                                                     str
    CLOCK1 [1]_    9.9999,0.0                                                                                                                                                                                                                                                                                            str
    DAC7 [1]_      5.9998,6.0017                                                                                                                                                                                                                                                                                         str
    DAC16 [1]_     39.9961,39.5472                                                                                                                                                                                                                                                                                       str
    CCDSECB [1]_   [2058:4114, 1:2064]                                                                                                                                                                                                                                                                                   str
    CLOCK17 [1]_   9.0,0.9999                                                                                                                                                                                                                                                                                            str
    CLOCK5 [1]_    9.9999,0.0                                                                                                                                                                                                                                                                                            str
    AMPSECB [1]_   [4114:2058, 1:2064]                                                                                                                                                                                                                                                                                   str
    CLOCK4 [1]_    9.9999,0.0                                                                                                                                                                                                                                                                                            str
    DETSECB [1]_   [2058:4114, 1:2064]                                                                                                                                                                                                                                                                                   str
    BIASSECA [1]_  [2065:2128, 2:2065]                                                                                                                                                                                                                                                                                   str
    CRYOPRES [1]_  2.938e-07                                                                                                                                                                                                                                                                                             str
    CCDTMING [1]_  default_lbnl_timing_20180905.txt                                                                                                                                                                                                                                                                      str
    CLOCK9 [1]_    9.9992,2.9993                                                                                                                                                                                                                                                                                         str
    PGAGAIN [1]_   3                                                                                                                                                                                                                                                                                                     int
    CLOCK6 [1]_    9.9999,0.0                                                                                                                                                                                                                                                                                            str
    OFFSET3 [1]_   0.4000000059604645,-8.8889                                                                                                                                                                                                                                                                            str
    PRRSECB [1]_   [2193:4249, 1:1]                                                                                                                                                                                                                                                                                      str
    DAC5 [1]_      5.9998,6.0174                                                                                                                                                                                                                                                                                         str
    CLOCK3 [1]_    -2.0001,3.9999                                                                                                                                                                                                                                                                                        str
    DAC14 [1]_     0.0,-0.0297                                                                                                                                                                                                                                                                                           str
    CLOCK15 [1]_   9.9992,2.9993                                                                                                                                                                                                                                                                                         str
    AMPSECD [1]_   [4114:2058, 4128:2065]                                                                                                                                                                                                                                                                                str
    CCDSECA [1]_   [1:2057, 1:2064]                                                                                                                                                                                                                                                                                      str
    DAC9 [1]_      -25.0003,-25.0351                                                                                                                                                                                                                                                                                     str
    DAC10 [1]_     -25.0003,-24.8273                                                                                                                                                                                                                                                                                     str
    CCDPREP [1]_   purge,clear                                                                                                                                                                                                                                                                                           str
    DAC4 [1]_      5.9998,6.0437                                                                                                                                                                                                                                                                                         str
    OFFSET4 [1]_   2.0,6.049                                                                                                                                                                                                                                                                                             str
    BLDTIME [1]_   0.3499                                                                                                                                                                                                                                                                                                float
    CLOCK16 [1]_   9.9999,3.0                                                                                                                                                                                                                                                                                            str
    DAC2 [1]_      -9.0002,-8.961                                                                                                                                                                                                                                                                                        str
    OFFSET1 [1]_   0.4000000059604645,-8.9507                                                                                                                                                                                                                                                                            str
    CLOCK10 [1]_   9.9992,2.9993                                                                                                                                                                                                                                                                                         str
    OFFSET7 [1]_   2.0,6.0017                                                                                                                                                                                                                                                                                            str
    ORSECD [1]_    [2193:4249, 2098:2129]                                                                                                                                                                                                                                                                                str
    OFFSET0 [1]_   0.4000000059604645,-8.9713                                                                                                                                                                                                                                                                            str
    CLOCK0 [1]_    9.9999,0.0                                                                                                                                                                                                                                                                                            str
    CRYOTEMP [1]_  139.986                                                                                                                                                                                                                                                                                               float
    DATASECB [1]_  [2193:4249, 2:2065]                                                                                                                                                                                                                                                                                   str
    DAC6 [1]_      5.9998,6.049                                                                                                                                                                                                                                                                                          str
    DAC12 [1]_     0.0,-0.0148                                                                                                                                                                                                                                                                                           str
    CLOCK2 [1]_    9.9999,0.0                                                                                                                                                                                                                                                                                            str
    TRIMSECC [1]_  [8:2064, 2130:4193]                                                                                                                                                                                                                                                                                   str
    PRRSECD [1]_   [2193:4249, 4194:4194]                                                                                                                                                                                                                                                                                str
    DAC15 [1]_     0.0,0.0                                                                                                                                                                                                                                                                                               str
    DATASECA [1]_  [8:2064, 2:2065]                                                                                                                                                                                                                                                                                      str
    DAC3 [1]_      -9.0002,-8.8889                                                                                                                                                                                                                                                                                       str
    CCDSIZE [1]_   4194,4256                                                                                                                                                                                                                                                                                             str
    AMPSECA [1]_   [1:2057, 1:2064]                                                                                                                                                                                                                                                                                      str
    PRESECD [1]_   [4250:4256, 2130:4193]                                                                                                                                                                                                                                                                                str
    ORSECA [1]_    [8:2064, 2066:2097]                                                                                                                                                                                                                                                                                   str
    CCDSECC [1]_   [1:2057, 2065:4128]                                                                                                                                                                                                                                                                                   str
    CLOCK18 [1]_   9.0,0.9999                                                                                                                                                                                                                                                                                            str
    DETSECD [1]_   [2058:4114, 2065:4128]                                                                                                                                                                                                                                                                                str
    CCDSECD [1]_   [2058:4114, 2065:4128]                                                                                                                                                                                                                                                                                str
    CPUTEMP [1]_   57.1172                                                                                                                                                                                                                                                                                               float
    DELAYS [1]_    20, 20, 25, 40, 7, 3000, 7, 7, 7, 7                                                                                                                                                                                                                                                                   str
    DATASECD [1]_  [2193:4249, 2130:4193]                                                                                                                                                                                                                                                                                str
    BIASSECC [1]_  [2065:2128, 2130:4193]                                                                                                                                                                                                                                                                                str
    CCDCFG [1]_    default_lbnl_20190717.cfg                                                                                                                                                                                                                                                                             str
    DATASECC [1]_  [8:2064, 2130:4193]                                                                                                                                                                                                                                                                                   str
    BIASSECD [1]_  [2129:2192, 2130:4193]                                                                                                                                                                                                                                                                                str
    PRESECA [1]_   [1:7, 2:2065]                                                                                                                                                                                                                                                                                         str
    OFFSET6 [1]_   2.0,6.0543                                                                                                                                                                                                                                                                                            str
    DETSECC [1]_   [1:2057, 2065:4128]                                                                                                                                                                                                                                                                                   str
    DAC13 [1]_     0.0,-0.0297                                                                                                                                                                                                                                                                                           str
    DETSECA [1]_   [1:2057, 1:2064]                                                                                                                                                                                                                                                                                      str
    PRRSECC [1]_   [8:2064, 4194:4194]                                                                                                                                                                                                                                                                                   str
    CLOCK12 [1]_   9.9992,2.9993                                                                                                                                                                                                                                                                                         str
    CASETEMP [1]_  56.8611                                                                                                                                                                                                                                                                                               float
    BIASSECB [1]_  [2129:2192, 2:2065]                                                                                                                                                                                                                                                                                   str
    OFFSET5 [1]_   2.0,6.0174                                                                                                                                                                                                                                                                                            str
    CLOCK7 [1]_    -2.0001,3.9999                                                                                                                                                                                                                                                                                        str
    CLOCK8 [1]_    9.9992,2.9993                                                                                                                                                                                                                                                                                         str
    CAMERA [1]_    z6                                                                                                                                                                                                                                                                                                    str
    PRESECB [1]_   [4250:4256, 2:2065]                                                                                                                                                                                                                                                                                   str
    TRIMSECB [1]_  [2193:4249, 2:2065]                                                                                                                                                                                                                                                                                   str
    DAC17 [1]_     20.0008,11.9316                                                                                                                                                                                                                                                                                       str
    DIGITIME [1]_  47.5453                                                                                                                                                                                                                                                                                               float
    TRIMSECD [1]_  [2193:4249, 2130:4193]                                                                                                                                                                                                                                                                                str
    DAC8 [1]_      -25.0003,-24.6196                                                                                                                                                                                                                                                                                     str
    TRIMSECA [1]_  [8:2064, 2:2065]                                                                                                                                                                                                                                                                                      str
    CLOCK14 [1]_   9.9992,2.9993                                                                                                                                                                                                                                                                                         str
    DAC0 [1]_      -9.0002,-8.9713                                                                                                                                                                                                                                                                                       str
    CDSPARMS [1]_  400, 400, 8, 2000                                                                                                                                                                                                                                                                                     str
    DAC1 [1]_      -9.0002,-8.9507                                                                                                                                                                                                                                                                                       str
    ORSECC [1]_    [8:2064, 2098:2129]                                                                                                                                                                                                                                                                                   str
    ORSECB [1]_    [2193:4249, 2066:2097]                                                                                                                                                                                                                                                                                str
    CCDNAME [1]_   CCDSM7Z                                                                                                                                                                                                                                                                                               str
    OBSID [1]_     kp4m20201221t023911                                                                                                                                                                                                                                                                                   str
    PROCTYPE [1]_  RAW                                                                                                                                                                                                                                                                                                   str
    PRODTYPE [1]_  image                                                                                                                                                                                                                                                                                                 str
    GAINA [1]_     1.387                                                                                                                                                                                                                                                                                                 float
    SATULEVA [1]_  61000.0                                                                                                                                                                                                                                                                                               float
    OSTEPA [1]_    0.7319095199345611                                                                                                                                                                                                                                                                                    float
    OMETHA [1]_    AVERAGE                                                                                                                                                                                                                                                                                               str
    OVERSCNA [1]_  1966.054034223049                                                                                                                                                                                                                                                                                     float
    OBSRDNA [1]_   2.176414404248625                                                                                                                                                                                                                                                                                     float
    SATUELEA [1]_  81880.08305453263                                                                                                                                                                                                                                                                                     float
    GAINB [1]_     1.518                                                                                                                                                                                                                                                                                                 float
    SATULEVB [1]_  65535.0                                                                                                                                                                                                                                                                                               float
    OSTEPB [1]_    0.5937273930649098                                                                                                                                                                                                                                                                                    float
    OMETHB [1]_    AVERAGE                                                                                                                                                                                                                                                                                               str
    OVERSCNB [1]_  1987.334317960662                                                                                                                                                                                                                                                                                     float
    OBSRDNB [1]_   2.29569819578003                                                                                                                                                                                                                                                                                      float
    SATUELEB [1]_  96465.35650533572                                                                                                                                                                                                                                                                                     float
    GAINC [1]_     1.534                                                                                                                                                                                                                                                                                                 float
    SATULEVC [1]_  40000.0                                                                                                                                                                                                                                                                                               float
    OSTEPC [1]_    0.9199855706829112                                                                                                                                                                                                                                                                                    float
    OMETHC [1]_    AVERAGE                                                                                                                                                                                                                                                                                               str
    OVERSCNC [1]_  1980.643479043017                                                                                                                                                                                                                                                                                     float
    OBSRDNC [1]_   2.511180716174036                                                                                                                                                                                                                                                                                     float
    SATUELEC [1]_  58321.69290314802                                                                                                                                                                                                                                                                                     float
    GAIND [1]_     1.554                                                                                                                                                                                                                                                                                                 float
    SATULEVD [1]_  62000.0                                                                                                                                                                                                                                                                                               float
    OSTEPD [1]_    1.375711494358256                                                                                                                                                                                                                                                                                     float
    OMETHD [1]_    AVERAGE                                                                                                                                                                                                                                                                                               str
    OVERSCND [1]_  1982.563334159938                                                                                                                                                                                                                                                                                     float
    OBSRDND [1]_   2.417154801423475                                                                                                                                                                                                                                                                                     float
    SATUELED [1]_  93267.09657871546                                                                                                                                                                                                                                                                                     float
    FIBERMIN [1]_  3000                                                                                                                                                                                                                                                                                                  int
    ENCODING [1]_  ascii                                                                                                                                                                                                                                                                                                 str
    CHECKSUM [1]_  aRITbQHRaQHRaQHR                                                                                                                                                                                                                                                                                      str     HDU checksum updated 2022-02-14T08:22:46
    DATASUM [1]_   3195504281                                                                                                                                                                                                                                                                                            str     data unit checksum updated 2022-02-14T08:22:46
    NTSSURVY [1]_  sv2                                                                                                                                                                                                                                                                                                   str
    SP8NIRP [1]_   4.941e-08                                                                                                                                                                                                                                                                                             float
    TCSPIDEC [1]_  1.0,0.0,0.0,0.0                                                                                                                                                                                                                                                                                       str
    SP3REDP [1]_   5.506e-08                                                                                                                                                                                                                                                                                             float
    USESPLITS [1]_ T                                                                                                                                                                                                                                                                                                     bool
    SBPROF [1]_    ELG                                                                                                                                                                                                                                                                                                   str
    SP9NIRP [1]_   5.207e-08                                                                                                                                                                                                                                                                                             float
    SP0REDT [1]_   139.96                                                                                                                                                                                                                                                                                                float
    SP8REDT [1]_   139.94                                                                                                                                                                                                                                                                                                float
    SP2REDT [1]_   139.99                                                                                                                                                                                                                                                                                                float
    SEQSTART [1]_  2021-04-04T06:46:24.391377                                                                                                                                                                                                                                                                            str
    SP0NIRP [1]_   5.865e-08                                                                                                                                                                                                                                                                                             float
    SP3NIRP [1]_   5.524e-08                                                                                                                                                                                                                                                                                             float
    SP7REDT [1]_   139.99                                                                                                                                                                                                                                                                                                float
    GOALTYPE [1]_  DARK                                                                                                                                                                                                                                                                                                  str
    PMSEEING [1]_  0.85                                                                                                                                                                                                                                                                                                  float
    SP6REDT [1]_   139.94                                                                                                                                                                                                                                                                                                float
    SP7NIRT [1]_   139.96                                                                                                                                                                                                                                                                                                float
    SP4BLUT [1]_   163.02                                                                                                                                                                                                                                                                                                float
    ACTTEFF [1]_   1513.0686                                                                                                                                                                                                                                                                                             float
    SP2NIRT [1]_   139.91                                                                                                                                                                                                                                                                                                float
    SP5NIRT [1]_   139.94                                                                                                                                                                                                                                                                                                float
    SP2BLUT [1]_   163.02                                                                                                                                                                                                                                                                                                float
    SP1BLUP [1]_   7.808e-08                                                                                                                                                                                                                                                                                             float
    SP4REDP [1]_   4.72e-08                                                                                                                                                                                                                                                                                              float
    SP8BLUP [1]_   8.119e-08                                                                                                                                                                                                                                                                                             float
    SP5BLUT [1]_   163.02                                                                                                                                                                                                                                                                                                float
    SP2REDP [1]_   5.348e-08                                                                                                                                                                                                                                                                                             float
    SP0REDP [1]_   5.012e-08                                                                                                                                                                                                                                                                                             float
    SP2BLUP [1]_   7.391e-08                                                                                                                                                                                                                                                                                             float
    SP9NIRT [1]_   139.89                                                                                                                                                                                                                                                                                                float
    SURVEY [1]_    sv2                                                                                                                                                                                                                                                                                                   str
    MTL [1]_       DESIROOT/target/mtl/0.53.0/mtl/sv2/dark                                                                                                                                                                                                                                                               str
    SP6NIRT [1]_   139.89                                                                                                                                                                                                                                                                                                float
    FAARGS [1]_    --doclean n --dr dr9 --dtver 0.53.0 --gaiadr gaiadr2 --goaltime 1000.0 --mintfrac 0.9 --pmcorr n --pmtime 2021-04-03T00:00:00.000 --program DARK --rundate 2021-03-17T23:20:01 --sbprof ELG --sky_per_petal 80 --standards_per_petal 40 --survey sv2 --tiledec 57.924 --tileid 81014 --tilera 190.731 str
    SP5BLUP [1]_   1.125e-07                                                                                                                                                                                                                                                                                             float
    TCSKDEC [1]_   0.3 0.003 0.00003                                                                                                                                                                                                                                                                                     str
    VISITIDS [1]_  89039                                                                                                                                                                                                                                                                                                 str
    SP6BLUT [1]_   163.02                                                                                                                                                                                                                                                                                                float
    SP1BLUT [1]_   163.02                                                                                                                                                                                                                                                                                                float
    TCSGRA [1]_    0.3                                                                                                                                                                                                                                                                                                   float
    SP5REDP [1]_   5.121e-08                                                                                                                                                                                                                                                                                             float
    TCSKRA [1]_    0.3 0.003 0.00003                                                                                                                                                                                                                                                                                     str
    USESPLIT [1]_  T                                                                                                                                                                                                                                                                                                     bool
    SP4REDT [1]_   140.01                                                                                                                                                                                                                                                                                                float
    SP8NIRT [1]_   139.99                                                                                                                                                                                                                                                                                                float
    SP0NIRT [1]_   139.89                                                                                                                                                                                                                                                                                                float
    SP6NIRP [1]_   2.811e-07                                                                                                                                                                                                                                                                                             float
    SP6BLUP [1]_   7.054e-08                                                                                                                                                                                                                                                                                             float
    SP9BLUT [1]_   163.02                                                                                                                                                                                                                                                                                                float
    SP4BLUP [1]_   4.868e-08                                                                                                                                                                                                                                                                                             float
    TCSPIRA [1]_   1.0,0.0,0.0,0.0                                                                                                                                                                                                                                                                                       str
    SP7REDP [1]_   4.279e-08                                                                                                                                                                                                                                                                                             float
    GOALTIME [1]_  1000.0                                                                                                                                                                                                                                                                                                float
    SP8BLUT [1]_   162.9                                                                                                                                                                                                                                                                                                 float
    SP8REDP [1]_   8.401e-08                                                                                                                                                                                                                                                                                             float
    SP3BLUT [1]_   163.02                                                                                                                                                                                                                                                                                                float
    SPLITEXP [1]_  F                                                                                                                                                                                                                                                                                                     bool
    SP3REDT [1]_   139.96                                                                                                                                                                                                                                                                                                float
    SUNDEC [1]_    5.800279                                                                                                                                                                                                                                                                                              float
    SP1NIRP [1]_   8.133e-08                                                                                                                                                                                                                                                                                             float
    SCND [1]_      -                                                                                                                                                                                                                                                                                                     str
    SP2NIRP [1]_   5.339e-08                                                                                                                                                                                                                                                                                             float
    SUNRA [1]_     13.554748                                                                                                                                                                                                                                                                                             float
    SP6REDP [1]_   6.486e-08                                                                                                                                                                                                                                                                                             float
    MOONSEP [1]_   113.991                                                                                                                                                                                                                                                                                               float
    TCSGDEC [1]_   0.3                                                                                                                                                                                                                                                                                                   float
    EBVFAC [1]_    1.02038914440859                                                                                                                                                                                                                                                                                      float
    PMCORR [1]_    n                                                                                                                                                                                                                                                                                                     str
    TCSMFDEC [1]_  1                                                                                                                                                                                                                                                                                                     int
    FAPRGRM [1]_   DARK                                                                                                                                                                                                                                                                                                  str
    DESIROOT [1]_  /global/cfs/cdirs/desi                                                                                                                                                                                                                                                                                str
    SP3NIRT [1]_   140.01                                                                                                                                                                                                                                                                                                float
    SP0BLUT [1]_   162.99                                                                                                                                                                                                                                                                                                float
    SP9REDP [1]_   4.354e-08                                                                                                                                                                                                                                                                                             float
    SEEING [1]_    0.8607                                                                                                                                                                                                                                                                                                float
    MTLTIME [1]_   2021-04-03T20:57:07                                                                                                                                                                                                                                                                                   str
    SP9BLUP [1]_   1.208e-07                                                                                                                                                                                                                                                                                             float
    SP7BLUP [1]_   9.947e-08                                                                                                                                                                                                                                                                                             float
    SP4NIRT [1]_   139.96                                                                                                                                                                                                                                                                                                float
    SP9REDT [1]_   140.01                                                                                                                                                                                                                                                                                                float
    TCSMFRA [1]_   1                                                                                                                                                                                                                                                                                                     int
    SP1NIRT [1]_   139.89                                                                                                                                                                                                                                                                                                float
    SP3BLUP [1]_   9.345e-08                                                                                                                                                                                                                                                                                             float
    PMTRANS [1]_   93.76                                                                                                                                                                                                                                                                                                 float
    MINTFRAC [1]_  0.9                                                                                                                                                                                                                                                                                                   float
    SP1REDT [1]_   139.89                                                                                                                                                                                                                                                                                                float
    SKYLEVEL [1]_  0.933                                                                                                                                                                                                                                                                                                 float
    SP4NIRP [1]_   6.91499999999999e-08                                                                                                                                                                                                                                                                                  float
    REQTEFF [1]_   1000.0                                                                                                                                                                                                                                                                                                float
    SP7BLUT [1]_   163.02                                                                                                                                                                                                                                                                                                float
    SP5REDT [1]_   139.99                                                                                                                                                                                                                                                                                                float
    SP7NIRP [1]_   6.211e-08                                                                                                                                                                                                                                                                                             float
    SP1REDP [1]_   6.567e-08                                                                                                                                                                                                                                                                                             float
    SP5NIRP [1]_   9.462e-08                                                                                                                                                                                                                                                                                             float
    SP0BLUP [1]_   9.115e-08                                                                                                                                                                                                                                                                                             float
    BBKGMAXC [1]_  0.4492153969301811                                                                                                                                                                                                                                                                                    float
    BBKGMIND [1]_  -0.3135937336084521                                                                                                                                                                                                                                                                                   float
    BBKGMAXB [1]_  0.5049607921526409                                                                                                                                                                                                                                                                                    float
    BBKGMINA [1]_  -0.2211057823638513                                                                                                                                                                                                                                                                                   float
    BBKGMINB [1]_  -0.3689821920680901                                                                                                                                                                                                                                                                                   float
    BBKGMINC [1]_  -0.3614105403549326                                                                                                                                                                                                                                                                                   float
    BBKGMAXA [1]_  0.7513851072600307                                                                                                                                                                                                                                                                                    float
    BBKGMAXD [1]_  0.3423400768828577                                                                                                                                                                                                                                                                                    float
    TOO [1]_       DESIROOT/survey/ops/surveyops/trunk/mtl/sv3/ToO/ToO.ecsv                                                                                                                                                                                                                                              str
    SVNDM [1]_     unknown                                                                                                                                                                                                                                                                                               str
    CONVERGD [1]_  F                                                                                                                                                                                                                                                                                                     bool
    TOTTEFF [1]_   1214.7279                                                                                                                                                                                                                                                                                             float
    SLEWANGL [1]_  49.575                                                                                                                                                                                                                                                                                                float
    SCNDMTL [1]_   DESIROOT/survey/ops/surveyops/trunk/mtl/sv3/secondary/dark                                                                                                                                                                                                                                            str
    POSCVFRC [1]_  0.4393                                                                                                                                                                                                                                                                                                float
    SVNMTL [1]_    unknown                                                                                                                                                                                                                                                                                               str
    FASCRIPT [1]_  /software/datasystems/desiconda/20200924/code/fiberassign/3.0.0/bin/fba_launch                                                                                                                                                                                                                        str
    TARG2 [1]_     DESIROOT/target/catalogs/gaiadr2/0.50.0/targets/sv1/resolve/supp                                                                                                                                                                                                                                      str
    SCSTD [1]_     STD_WD,STD_BRIGHT                                                                                                                                                                                                                                                                                     str
    SEQID [1]_     5 requests                                                                                                                                                                                                                                                                                            str
    SEQTOT [1]_    5                                                                                                                                                                                                                                                                                                     int
    SIMGFAQ [1]_   F                                                                                                                                                                                                                                                                                                     bool
    ETCFRACB [1]_  0.13642                                                                                                                                                                                                                                                                                               float
    ETCFRACP [1]_  0.390556                                                                                                                                                                                                                                                                                              float
    ETCTEFF [1]_   61.258228                                                                                                                                                                                                                                                                                             float
    ETCFRACE [1]_  0.300922                                                                                                                                                                                                                                                                                              float
    NTSPROG [1]_   BACKUP                                                                                                                                                                                                                                                                                                str
    ETCTHRUB [1]_  0.535631                                                                                                                                                                                                                                                                                              float
    ETCSPLIT [1]_  1                                                                                                                                                                                                                                                                                                     int
    ETCTRANS [1]_  0.745415                                                                                                                                                                                                                                                                                              float
    ETCREAL [1]_   348.878632                                                                                                                                                                                                                                                                                            float
    ETCVERS [1]_   0.1.12-3-g12b54bb                                                                                                                                                                                                                                                                                     str
    ETCTHRUP [1]_  0.518037                                                                                                                                                                                                                                                                                              float
    MAXTIME [1]_   5400.0                                                                                                                                                                                                                                                                                                float
    ETCSKY [1]_    1.60973                                                                                                                                                                                                                                                                                               float
    ESTTIME [1]_   1500.571                                                                                                                                                                                                                                                                                              float
    TRANSPAR [1]_  None                                                                                                                                                                                                                                                                                                  float
    ETCPROF [1]_   PSF                                                                                                                                                                                                                                                                                                   str
    MINTIME [1]_   60.0                                                                                                                                                                                                                                                                                                  float
    PMTRANSP [1]_  115.88                                                                                                                                                                                                                                                                                                float
    ETCSEENG [1]_  2.1165                                                                                                                                                                                                                                                                                                float
    ACQFWHM [1]_   2.116458                                                                                                                                                                                                                                                                                              float
    ETCTHRUE [1]_  0.544181                                                                                                                                                                                                                                                                                              float
    ETCPREV [1]_   0.0                                                                                                                                                                                                                                                                                                   float
    PRIORITY [1]_  default                                                                                                                                                                                                                                                                                               str
    DR [1]_        dr9                                                                                                                                                                                                                                                                                                   str
    M31CEN [1]_    n                                                                                                                                                                                                                                                                                                     str
    DTVER [1]_     0.50.0                                                                                                                                                                                                                                                                                                str
    ROLE [1]_      GUIDERMAN                                                                                                                                                                                                                                                                                             str
    SHFTFOCS [1]_  500.0                                                                                                                                                                                                                                                                                                 float
    TARG3 [1]_     DESIROOT/target/catalogs/dr9/0.51.0/targets/sv1/resolve/bright                                                                                                                                                                                                                                        str
    ============== ===================================================================================================================================================================================================================================================================================================== ======= ==============================================


Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

========================== ======= ============ =======================================================================================================================================
Name                       Type    Units        Description
========================== ======= ============ =======================================================================================================================================
TARGETID [1]_              int64                Unique DESI target ID
PETAL_LOC [1]_             int16                Petal location [0-9]
DEVICE_LOC [1]_            int32                Device location on focal plane [0-523]
LOCATION [1]_              int64                Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBER [1]_                 int32                Fiber ID on the CCDs [0-4999]
FIBERSTATUS [1]_           int32                Fiber status mask. 0=good
TARGET_RA [1]_             float64 deg          Barycentric right ascension in ICRS
TARGET_DEC [1]_            float64 deg          Barycentric declination in ICRS
PMRA [1]_                  float32 mas yr^-1    proper motion in the +RA direction (already including cos(dec))
PMDEC [1]_                 float32 mas yr^-1    Proper motion in the +Dec direction
REF_EPOCH [1]_             float32 yr           Reference epoch for Gaia/Tycho astrometry. Typically 2015.5 for Gaia
LAMBDA_REF [1]_            float32 Angstrom     Requested wavelength at which targets should be centered on fibers
FA_TARGET [1]_             int64                Targeting bit internally used by fiberassign (linked with FA_TYPE)
FA_TYPE [1]_               binary               Fiberassign internal target type (science, standard, sky, safe, suppsky)
OBJTYPE [1]_               char[3]              Object type: TGT, SKY, NON, BAD
FIBERASSIGN_X [1]_         float32 mm           Fiberassign expected CS5 X location on focal plane
FIBERASSIGN_Y [1]_         float32 mm           Fiberassign expected CS5 Y location on focal plane
PRIORITY [1]_              int32                Target current priority
SUBPRIORITY [1]_           float64              Random subpriority [0-1) to break assignment ties
OBSCONDITIONS [1]_         int32                Bitmask of allowed observing conditions
RELEASE [1]_               int16                Imaging surveys release ID
BRICKNAME [1]_             char[8]              Brick name from tractor input
BRICKID [1]_               int32                Brick ID from tractor input
BRICK_OBJID [1]_           int32                Imaging Surveys OBJID on that brick
MORPHTYPE [1]_             char[4]              Imaging Surveys morphological type from Tractor
EBV [1]_                   float32 mag          Galactic extinction E(B-V) reddening from SFD98
FLUX_G [1]_                float32 nanomaggy    Flux in the Legacy Survey g-band (AB)
FLUX_R [1]_                float32 nanomaggy    Flux in the Legacy Survey r-band (AB)
FLUX_Z [1]_                float32 nanomaggy    Flux in the Legacy Survey z-band (AB)
FLUX_W1 [1]_               float32 nanomaggy    WISE flux in W1 (AB)
FLUX_W2 [1]_               float32 nanomaggy    WISE flux in W2 (AB)
FLUX_IVAR_G [1]_           float32 nanomaggy^-2 Inverse variance of FLUX_G (AB)
FLUX_IVAR_R [1]_           float32 nanomaggy^-2 Inverse variance of FLUX_R (AB)
FLUX_IVAR_Z [1]_           float32 nanomaggy^-2 Inverse variance of FLUX_Z (AB)
FLUX_IVAR_W1 [1]_          float32 nanomaggy^-2 Inverse variance of FLUX_W1 (AB)
FLUX_IVAR_W2 [1]_          float32 nanomaggy^-2 Inverse variance of FLUX_W2 (AB)
FIBERFLUX_G [1]_           float32 nanomaggy    Predicted g-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERFLUX_R [1]_           float32 nanomaggy    Predicted r-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERFLUX_Z [1]_           float32 nanomaggy    Predicted z-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERTOTFLUX_G [1]_        float32 nanomaggy    Predicted g-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
FIBERTOTFLUX_R [1]_        float32 nanomaggy    Predicted r-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
FIBERTOTFLUX_Z [1]_        float32 nanomaggy    Predicted z-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
MASKBITS [1]_              int16                Bitwise mask from the imaging indicating potential issue or blending
SERSIC [1]_                float32              Power-law index for the Sersic profile model (MORPHTYPE=&#x27;SER&#x27;)
SHAPE_R [1]_               float32 arcsec       Half-light radius of galaxy model (&gt;0)
SHAPE_E1 [1]_              float32              Ellipticity component 1 of galaxy model for galaxy type MORPHTYPE
SHAPE_E2 [1]_              float32              Ellipticity component 2 of galaxy model for galaxy type MORPHTYPE
REF_ID [1]_                int64                Tyc1*1,000,000+Tyc2*10+Tyc3 for Tycho-2; ``sourceid`` for Gaia DR2
REF_CAT [1]_               char[2]              Reference catalog source for star: &#x27;T2&#x27; for Tycho-2, &#x27;G2&#x27; for Gaia DR2, &#x27;L2&#x27; for the SGA, empty otherwise
GAIA_PHOT_G_MEAN_MAG [1]_  float32 mag          Gaia G band magnitude
GAIA_PHOT_BP_MEAN_MAG [1]_ float32 mag          Gaia BP band magnitude
GAIA_PHOT_RP_MEAN_MAG [1]_ float32 mag          Gaia RP band magnitude
PARALLAX [1]_              float32 mas          Reference catalog parallax
PHOTSYS [1]_               char[1]              &#x27;N&#x27; for the MzLS/BASS photometric system, &#x27;S&#x27; for DECaLS
PRIORITY_INIT [1]_         int64                Target initial priority from target selection bitmasks and OBSCONDITIONS
NUMOBS_INIT [1]_           int64                Initial number of observations for target calculated across target selection bitmasks and OBSCONDITIONS
DESI_TARGET [1]_           int64                DESI (dark time program) target selection bitmask
BGS_TARGET [1]_            int64                BGS (Bright Galaxy Survey) target selection bitmask
MWS_TARGET [1]_            int64                Milky Way Survey targeting bits
SCND_TARGET [1]_           int64                Target selection bitmask for secondary programs
PLATE_RA [1]_              float64 deg          Barycentric Right Ascension in ICRS to be used by PlateMaker
PLATE_DEC [1]_             float64 deg          Barycentric Declination in ICRS to be used by PlateMaker
NUM_ITER [1]_              int64                Number of positioner iterations
FIBER_X [1]_               float64 mm           CS5 X location requested by PlateMaker
FIBER_Y [1]_               float64 mm           CS5 Y location requested by PlateMaker
DELTA_X [1]_               float64 mm           CS5 X requested minus actual position
DELTA_Y [1]_               float64 mm           CS5 Y requested minus actual position
FIBER_RA [1]_              float64 deg          RA of actual fiber position
FIBER_DEC [1]_             float64 deg          DEC of actual fiber position
EXPTIME [1]_               float64 s            Length of time shutter was open
SV2_BGS_TARGET [1]_        int64                BGS (bright time program) target selection bitmask for SV2
SV2_SCND_TARGET [1]_       int64                Secondary target selection bitmask for SV2
SV2_MWS_TARGET [1]_        int64                MWS (bright time program) target selection bitmask for SV2
SV2_DESI_TARGET [1]_       int64                DESI (dark time program) target selection bitmask for SV2
SV1_DESI_TARGET [1]_       int64                DESI (dark time program) target selection bitmask for SV1
SV1_SCND_TARGET [1]_       int64                Secondary target selection bitmask for SV1
SV1_BGS_TARGET [1]_        int64                BGS (bright time program) target selection bitmask for SV1
SV1_MWS_TARGET [1]_        int64                MWS (bright time program) target selection bitmask for SV1
SV3_MWS_TARGET [1]_        int64                MWS (bright time program) target selection bitmask for SV3
SV3_DESI_TARGET [1]_       int64                DESI (dark time program) target selection bitmask for SV3
SV3_SCND_TARGET [1]_       int64                Secondary target selection bitmask for SV3
SV3_BGS_TARGET [1]_        int64                BGS (bright time program) target selection bitmask for SV3
========================== ======= ============ =======================================================================================================================================

.. [1] Optional

Notes and Examples
==================

We may add an additional HDU with ``EXTNAME=METADATA`` containing a
binary table with one row per standard star giving
the details of which model was used, etc.
This is not yet implemented and details TBD.
