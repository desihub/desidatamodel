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
====== ========== ======== ===================

FITS Header Units
=================

HDU0
----

EXTNAME = FLUX

Extracted electrons[nspec, nwave]

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ===================================================================== ===== ===============================================
    KEY      Example Value                                                         Type  Comment
    ======== ===================================================================== ===== ===============================================
    NAXIS1   2326                                                                  int
    NAXIS2   500                                                                   int
    EXPID    69022                                                                 int   Exposure number
    EXPFRAME 0                                                                     int   Frame number
    TILEID   80616                                                                 int   DESI Tile ID
    FIBASSGN /data/tiles/SVN_tiles/080/fiberassign-080616.fits                     str   Fiber assign fil
    FLAVOR   science                                                               str   Observation type
    SEQUENCE DESI                                                                  str   OCS Sequence name
    PURPOSE  Commissioning                                                         str   Purpose of observing night
    PROGRAM  SV1 BGS+MWS tile 80616                                                str   Program name
    PROPID   2019B-5000                                                            str   Proposal ID
    OBSERVER DESIObserver                                                          str   Names of observers
    LEAD     RunManager                                                            str   Lead observer
    INSTRUME DESI                                                                  str   Instrument name
    OBSERVAT KPNO                                                                  str   Observatory name
    OBS-LAT  31.96403                                                              str   [deg] Observatory latitude
    OBS-LONG -111.59989                                                            str   [deg] Observatory east longitude
    OBS-ELEV 2097.0                                                                float [m] Observatory elevation
    TELESCOP KPNO 4.0-m telescope                                                  str   Telescope name
    CORRCTOR DESI Corrector                                                        str   Corrector Identification
    NIGHT    20201220                                                              int   Observing night
    TIMESYS  UTC                                                                   str   Time system used for date-obs
    DATE-OBS 2020-12-21T02:36:32.099838                                            str   [UTC] Observation data and start time
    TIME-OBS 02:39:11.845920                                                       str   [UTC] Observation start time
    MJD-OBS  59204.10870486                                                        float Modified Julian Date of observation
    OPENSHUT 2020-12-21T02:36:32.099838                                            str   Time shutter opened
    ST       01:10:39.210                                                          str   Local Sidereal time at observation start (HH:MM
    EXPTIME  300.007                                                               float [s] Actual exposure time
    REQRA    356.0                                                                 float [deg] Requested right ascension (observer input
    REQDEC   29.0                                                                  float [deg] Requested declination (observer input)
    FOCUS    1426.5,-501.4,81.0,-2.6,42.3,169.2                                    str   Telescope focus settings
    VCCD     ON                                                                    str   True (ON) if CCD voltage is on
    VCCDON   2020-12-14T17:48:28.296248                                            str   Time when CCD voltage was turned on
    VCCDSEC  550592.7                                                              float [s] CCD on time in seconds
    TRUSTEMP 11.767                                                                float [deg] Average Telescope truss temperature (only
    PMIRTEMP 8.925                                                                 float [deg] Average primary mirror temperature (nit,e
    EQUINOX  2000.0                                                                float Epoch of observation
    MOUNTAZ  266.70224                                                             float [deg] Mount azimuth angle
    MOUNTDEC 28.999221                                                             float [deg] Mount declination
    MOUNTEL  71.039837                                                             float [deg] Mount elevation angle
    MOUNTHA  21.769281                                                             float [deg] Mount hour angle
    SKYDEC   28.999221                                                             float [deg] Telescope declination (pointing on sky)
    SKYRA    355.996551                                                            float [deg] Telescope right ascension (pointing on sk
    TARGTDEC 28.999221                                                             float [deg] Target declination (to TCS)
    TARGTRA  355.996551                                                            float [deg] Target right ascension (to TCS)
    USEETC   F                                                                     bool  ETC data available if true
    USESKY   T                                                                     bool  DOS Control: use Sky Monitor
    USEFOCUS T                                                                     bool  DOS Control: use focus
    HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                                               str   Hexapod trim values
    USEROTAT T                                                                     bool  DOS Control: use rotator
    ROTOFFST 167.1                                                                 float [arcsec] Rotator offset
    ROTENBLD T                                                                     bool  Rotator enabled
    ROTRATE  0.0                                                                   float [arcsec/min] Rotator rate
    USEGUIDR T                                                                     bool  DOS Control: use guider
    USEDONUT T                                                                     bool  DOS Control: use donuts
    SPECGRPH 3                                                                     int   Spectrograph logical name (SP)
    SPECID   6                                                                     int   Spectrograph serial number (SM)
    FEEBOX   lbnl074                                                               str   CCD Controller serial number
    VESSEL   11                                                                    int   Cryostat serial number
    FEEVER   v20160312                                                             str   CCD Controller version
    FEEPOWER ON                                                                    str   FEE power status
    FEEDMASK 2134851391                                                            int   FEE dac mask
    FEECMASK 1048575                                                               int   FEE clk mask
    CCDTEMP  -140.2798                                                             float [deg C] CCD controller CCD temperature
    RADESYS  FK5                                                                   str   Coordinate reference frame of major/minor axes
    FILENAME /exposures/desi/specs/20201220/00069022/sp1-00069022.fits.fz          str   Name
    DOSVER   trunk                                                                 str   DOS software version
    OCSVER   1.2                                                                   float OCS software version
    CONSTVER DESI:CURRENT                                                          str   Constants version
    INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini                      str   DOS Configuration
    CRYOPRES 7.233e-08                                                             str   [mb] Cryostat pressure (IP)
    CLOCK7   -2.0001,3.9999                                                        str   [V] high rail, low rail
    TRIMSECA [8:2064, 2:2065]                                                      str   Trim section for quadrant A
    CCDNAME  CCDSM6R                                                               str   CCD name
    TRIMSECD [2193:4249, 2130:4193]                                                str   Trim section for quadrant D
    OFFSET2  0.4000000059604645,-8.961                                             str   [V] set value, measured value
    CPUTEMP  56.625                                                                float [deg C] CCD controller CPU temperature
    DAC11    -25.0003,-24.7086                                                     str   [V] set value, measured value
    AMPSECA  [1:2057, 1:2064]                                                      str   AMP section for quadrant A
    CCDCFG   M1-50_lbnl_20190719.cfg                                               str   CCD configuration file
    TRIMSECB [2193:4249, 2:2065]                                                   str   Trim section for quadrant B
    CLOCK3   -2.0001,3.9999                                                        str   [V] high rail, low rail
    CCDSECA  [1:2057, 1:2064]                                                      str   CCD section for quadrant A
    CLOCK4   9.9999,0.0                                                            str   [V] high rail, low rail
    DAC0     -9.0002,-8.9095                                                       str   [V] set value, measured value
    CLOCK10  9.9992,2.9993                                                         str   [V] high rail, low rail
    BIASSECA [2065:2128, 2:2065]                                                   str   Bias section for quadrant A
    PRRSECA  [8:2064, 1:1]                                                         str   Row prescan section for quadrant A
    DAC7     6.4999,6.4856                                                         str   [V] set value, measured value
    AMPSECB  [4114:2058, 1:2064]                                                   str   AMP section for quadrant B
    DAC10    -25.0003,-24.9906                                                     str   [V] set value, measured value
    DELAYS   20, 20, 25, 30, 7, 3000, 7, 7, 7, 7                                   str   [10] Delay settings
    CCDSECD  [2058:4114, 2065:4128]                                                str   CCD section for quadrant D
    CASETEMP 56.4919                                                               float [deg C] CCD controller case temperature
    CLOCK6   9.9999,0.0                                                            str   [V] high rail, low rail
    CLOCK13  9.9992,2.9993                                                         str   [V] high rail, low rail
    CLOCK9   9.9992,2.9993                                                         str   [V] high rail, low rail
    DAC8     -25.0003,-25.0202                                                     str   [V] set value, measured value
    DAC9     -25.0003,-24.6789                                                     str   [V] set value, measured value
    ORSECB   [2193:4249, 2066:2097]                                                str   Row overscan section for quadrant B
    CLOCK1   9.9999,0.0                                                            str   [V] high rail, low rail
    DETSECC  [1:2057, 2065:4128]                                                   str   Detector section for quadrant C
    AMPSECD  [4114:2058, 4128:2065]                                                str   AMP section for quadrant D
    CLOCK5   9.9999,0.0                                                            str   [V] high rail, low rail
    ORSECA   [8:2064, 2066:2097]                                                   str   Row overscan section for quadrant A
    DAC15    0.0,0.0297                                                            str   [V] set value, measured value
    DATASECA [8:2064, 2:2065]                                                      str   Data section for quadrant A
    CCDPREP  purge,clear                                                           str   CCD prep actions
    OFFSET7  2.0,6.4908                                                            str   [V] set value, measured value
    DAC5     5.9998,6.028                                                          str   [V] set value, measured value
    CLOCK12  9.9992,2.9993                                                         str   [V] high rail, low rail
    CCDSECB  [2058:4114, 1:2064]                                                   str   CCD section for quadrant B
    OFFSET6  2.0,6.0332                                                            str   [V] set value, measured value
    DAC4     5.9998,6.028                                                          str   [V] set value, measured value
    PRESECC  [1:7, 2130:4193]                                                      str   Prescan section for quadrant C
    OFFSET5  2.0,6.028                                                             str   [V] set value, measured value
    DAC2     -9.0002,-8.9713                                                       str   [V] set value, measured value
    CRYOTEMP 162.97                                                                float [deg K] Cryostat CCD temperature
    PRESECB  [4250:4256, 2:2065]                                                   str   Prescan section for quadrant B
    DIGITIME 47.1031                                                               float [s] Time to digitize image
    DAC3     -10.5005,-10.3824                                                     str   [V] set value, measured value
    CAMERA   r3                                                                    str   Camera name
    DETSECB  [2058:4114, 1:2064]                                                   str   Detector section for quadrant B
    OFFSET1  0.4000000059604645,-8.8065                                            str   [V] set value, measured value
    DATASECD [2193:4249, 2130:4193]                                                str   Data section for quadrant D
    SETTINGS detectors_sm_20191211.json                                            str   Name of DESI CCD settings file
    CLOCK11  9.9992,2.9993                                                         str   [V] high rail, low rail
    DAC13    0.0,0.0                                                               str   [V] set value, measured value
    CLOCK14  9.9992,2.9993                                                         str   [V] high rail, low rail
    CCDSECC  [1:2057, 2065:4128]                                                   str   CCD section for quadrant C
    DATASECC [8:2064, 2130:4193]                                                   str   Data section for quadrant C
    CLOCK0   9.9999,0.0                                                            str   [V] high rail, low rail
    CLOCK15  9.9992,2.9993                                                         str   [V] high rail, low rail
    DAC12    0.0,0.0297                                                            str   [V] set value, measured value
    CCDSIZE  4194,4256                                                             str   CCD size in pixels (rows, columns)
    OFFSET0  0.4000000059604645,-8.9095                                            str   [V] set value, measured value
    ORSECD   [2193:4249, 2098:2129]                                                str   Row bias section for quadrant D
    DAC16    48.0,46.7082                                                          str   [V] set value, measured value
    PRRSECC  [8:2064, 4194:4194]                                                   str   Row prescan section for quadrant C
    PRRSECD  [2193:4249, 4194:4194]                                                str   Row prescan section for quadrant D
    BIASSECB [2129:2192, 2:2065]                                                   str   Bias section for quadrant B
    DETSECD  [2058:4114, 2065:4128]                                                str   Detector section for quadrant D
    CLOCK18  9.0,0.9999                                                            str   [V] high rail, low rail
    DAC17    20.0008,14.274                                                        str   [V] set value, measured value
    CCDTMING default_lbnl_timing_20180905.txt                                      str   CCD timing file
    DETECTOR M1-50                                                                 str   Detector (ccd) identification
    PRRSECB  [2193:4249, 1:1]                                                      str   Row prescan section for quadrant B
    TRIMSECC [8:2064, 2130:4193]                                                   str   Trim section for quadrant C
    DAC14    0.0,0.0148                                                            str   [V] set value, measured value
    BIASSECD [2129:2192, 2130:4193]                                                str   Bias section for quadrant D
    CDSPARMS 400, 400, 8, 2000                                                     str   CDS parameters
    OFFSET3  0.4000000059604645,-10.3721                                           str   [V] set value, measured value
    PRESECA  [1:7, 2:2065]                                                         str   Prescan section for quadrant A
    ORSECC   [8:2064, 2098:2129]                                                   str   Row overscan section for quadrant C
    DAC6     5.9998,6.0332                                                         str   [V] set value, measured value
    PGAGAIN  3                                                                     int   Controller gain
    DAC1     -9.0002,-8.8065                                                       str   [V] set value, measured value
    DATASECB [2193:4249, 2:2065]                                                   str   Data section for quadrant B
    CLOCK2   9.9999,0.0                                                            str   [V] high rail, low rail
    CLOCK16  9.9999,3.0                                                            str   [V] high rail, low rail
    PRESECD  [4250:4256, 2130:4193]                                                str   Prescan section for quadrant D
    OFFSET4  2.0,6.0332                                                            str   [V] set value, measured value
    CLOCK17  9.0,0.9999                                                            str   [V] high rail, low rail
    AMPSECC  [1:2057, 4128:2065]                                                   str   AMP section for quadrant C
    CLOCK8   9.9992,2.9993                                                         str   [V] high rail, low rail
    DETSECA  [1:2057, 1:2064]                                                      str   Detector section for quadrant A
    BIASSECC [2065:2128, 2130:4193]                                                str   Bias section for quadrant C
    BLDTIME  0.3504                                                                float [s] Time to build image
    REQTIME  300.0                                                                 float [s] Requested exposure time
    OBSID    kp4m20201221t023911                                                   str   Unique observation identifier
    PROCTYPE RAW                                                                   str   Data processing level
    PRODTYPE image                                                                 str   Data product type
    CHECKSUM jjGAmi92jiE8ji98                                                      str   HDU checksum updated 2022-02-14T06:14:04
    DATASUM  3075256975                                                            str   data unit checksum updated 2022-02-14T06:14:04
    GAINA    1.681                                                                 float e/ADU (gain applied to image)
    SATULEVA 28000.0                                                               float saturation or non lin. level, in ADU, inc. bias
    OSTEPA   0.7048677125421818                                                    float ADUs (max-min of median overscan per row)
    OMETHA   AVERAGE                                                               str   use average overscan
    OVERSCNA 1979.586454500641                                                     float ADUs (gain not applied)
    OBSRDNA  2.618213792981265                                                     float electrons (gain is applied)
    SATUELEA 43740.31516998442                                                     float saturation or non lin. level, in electrons
    GAINB    1.625                                                                 float e/ADU (gain applied to image)
    SATULEVB 57000.0                                                               float saturation or non lin. level, in ADU, inc. bias
    OSTEPB   0.6850349189899134                                                    float ADUs (max-min of median overscan per row)
    OMETHB   AVERAGE                                                               str   use average overscan
    OVERSCNB 1997.289875350671                                                     float ADUs (gain not applied)
    OBSRDNB  3.12518985733541                                                      float electrons (gain is applied)
    SATUELEB 89379.40395255515                                                     float saturation or non lin. level, in electrons
    GAINC    1.477                                                                 float e/ADU (gain applied to image)
    SATULEVC 59000.0                                                               float saturation or non lin. level, in ADU, inc. bias
    OSTEPC   0.6403308619337622                                                    float ADUs (max-min of median overscan per row)
    OMETHC   AVERAGE                                                               str   use average overscan
    OVERSCNC 1974.691977751432                                                     float ADUs (gain not applied)
    OBSRDNC  2.344388520757958                                                     float electrons (gain is applied)
    SATUELEC 84226.37994886114                                                     float saturation or non lin. level, in electrons
    GAIND    1.492                                                                 float e/ADU (gain applied to image)
    SATULEVD 62000.0                                                               float saturation or non lin. level, in ADU, inc. bias
    OSTEPD   0.6246898852550657                                                    float ADUs (max-min of median overscan per row)
    OMETHD   AVERAGE                                                               str   use average overscan
    OVERSCND 1998.214476179268                                                     float ADUs (gain not applied)
    OBSRDND  2.301320302261815                                                     float electrons (gain is applied)
    SATUELED 89522.66400154053                                                     float saturation or non lin. level, in electrons
    FIBERMIN 1500                                                                  int
    LONGSTRN OGIP 1.0                                                              str   The OGIP Long String Convention may be used.
    MODULE   CI                                                                    str   Image Sources/Component
    COSMSPLT F                                                                     bool  Cosmics split exposure if true
    MAXSPLIT 0                                                                     int   Number of allowed exposure splits
    SPLITIDS 69022                                                                 str   List of expids for split exposures
    OBSTYPE  SCIENCE                                                               str   Spectrograph observation type
    MANIFEST F                                                                     bool  DOS exposure manifest
    OBJECT                                                                         str   Object name
    SEQNUM   1                                                                     int   Number of exposure in sequence
    CAMSHUT  open                                                                  str   Shutter status during observation
    ACQTIME  15.0                                                                  float [s] acqusition image exposure time
    GUIDTIME 5.0                                                                   float [s] guider GFA exposure time
    FOCSTIME 60.0                                                                  float [s] focus GFA exposure time
    SKYTIME  60.0                                                                  float [s] sky camera exposure time (acquisition)
    WHITESPT F                                                                     bool  Telescope is at whitespot
    ZENITH   F                                                                     bool  Telescope is at zenith
    SEANNEX  F                                                                     bool  Telescope is at SE annex
    BEYONDP  F                                                                     bool  Telescope is beyond pole
    FIDUCIAL off                                                                   str   Fiducials status during observation
    BACKLIT  off                                                                   str   Fibers are backlit if True
    AIRMASS  1.060311                                                              float Airmass
    PMREADY  T                                                                     bool  Primary mirror ready
    PMCOVER  open                                                                  str   Primary mirror cover
    PMCOOL   off                                                                   str   Primary mirror cooling
    DOMSHUTU open                                                                  str   Upper dome shutter
    DOMSHUTL open                                                                  str   Lower dome shutter
    DOMLIGHH off                                                                   str   High dome lights
    DOMLIGHL off                                                                   str   Low dome lights
    DOMEAZ   255.166                                                               float [deg] Dome azimuth angle
    DOMINPOS T                                                                     bool  Dome is in position
    GUIDOFFR -0.052283                                                             float [arcsec] Cummulative guider offset (RA)
    GUIDOFFD 0.136634                                                              float [arcsec] Cummulative guider offset (dec)
    MOONDEC  -8.975162                                                             float [deg] Moon declination at start of exposure
    MOONRA   352.538429                                                            float [deg] Moon RA at start of exposure
    INCTRL   T                                                                     bool  DESI in control
    INPOS    T                                                                     bool  Mount in position
    MNTOFFD  -15.76                                                                float [arcsec] Mount offset (dec)
    MNTOFFR  29.32                                                                 float [arcsec] Mount offset (RA)
    PARALLAC 75.635085                                                             float [deg] Parallactic angle
    TARGTAZ  267.074049                                                            float [deg] Target azimuth
    TARGTEL  70.563787                                                             float [deg] Target elevation
    TRGTOFFD 0.0                                                                   float [arcsec] Telescope target offset (dec)
    TRGTOFFR 0.0                                                                   float [arcsec] Telescope target offset (RA)
    ZD       19.436213                                                             float [deg] Telescope zenith distance
    TILERA   356.0                                                                 float RA of tile given in fiberassign file
    TILEDEC  29.0                                                                  float DEC of tile given in fiberassign file
    TCSST    01:13:18.668                                                          str   Local Sidereal time reported by TCS (HH:MM:SS)
    TCSMJD   59204.110981                                                          float MJD reported by TCS
    ACQCAM   GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                             str   Acquisition cameras used
    GUIDECAM GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                             str   Guide cameras used for t
    FOCUSCAM FOCUS1,FOCUS4,FOCUS6,FOCUS9                                           str   Focus cameras used for this exposure
    SKYCAM   SKYCAM0,SKYCAM1                                                       str   Sky cameras used for this exposure
    REQADC   65.78,85.28                                                           str   [deg] requested ADC angles
    ADCCORR  T                                                                     bool  Correct pointing for ADC setting if True
    ADC1PHI  65.780005                                                             float [deg] ADC 1 angle
    ADC2PHI  85.279991                                                             float [deg] ADC 2 angle
    ADC1HOME F                                                                     bool  ADC 1 at home position if True
    ADC2HOME F                                                                     bool  ADC 2 at home position if True
    ADC1NREV -1.0                                                                  float ADC 1 number of revs
    ADC2NREV 0.0                                                                   float ADC 2 number of revs
    ADC1STAT STOPPED                                                               str   ADC 1 status
    ADC2STAT STOPPED                                                               str   ADC 2 status
    HEXPOS   1426.5,-501.3,81.0,-2.6,42.3,171.9                                    str   Hexapod position
    RESETROT F                                                                     bool  DOS Control: reset hex rotator
    USEPOS   T                                                                     bool  Fiber positioner data available if true
    PETALS   PETAL0,PETAL1,PETAL2,PETAL3,PETAL4,PETAL5,PETAL6,PETAL7,PETAL8,PETAL9 str   Participating petals
    POSCYCLE 1                                                                     int   Number of current iteration
    POSONTGT 3626                                                                  int   Number of positioners on target
    POSONFRC 0.8613                                                                float Fraction of positioners on target
    POSDISAB 37                                                                    int   Number of disabled positioners
    POSENABL 4210                                                                  int   Number of enabled positioners
    POSRMS   0.0171                                                                float [micron] RMS of positioner accuracy
    POSITER  1                                                                     int   Positioning Control: max. number of pos. cycles
    POSFRACT 0.95                                                                  float
    POSTOLER 0.01                                                                  float Positioning Control: in_position tolerance (mm)
    POSMVALL T                                                                     bool  Positioning Control: move all positioners
    GUIDMODE catalog                                                               str   Guider mode
    USEAOS   F                                                                     bool  DOS Control: AOS data available if true
    USESPCTR T                                                                     bool  DOS Control: use spectrographs
    SPCGRPHS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                               str   Participating spectrograph
    ILLSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                               str   Participating illuminate s
    CCDSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                               str   Participating ccd spectrog
    TDEWPNT  -16.043                                                               float Telescope air dew point
    TAIRFLOW 0.0                                                                   float Telescope air flow
    TAIRITMP 11.8                                                                  float [deg] Telescope air in temperature
    TAIROTMP 11.7                                                                  float [deg] Telescope air out temperature
    TAIRTEMP 10.65                                                                 float [deg] Telescope air temperature
    TCASITMP 0.0                                                                   float [deg] Telescope Cass Cage in temperature
    TCASOTMP 10.8                                                                  float [deg] Telescope Cass Cage out temperature
    TCSITEMP 9.3                                                                   float [deg] Telescope center section in temperature
    TCSOTEMP 10.8                                                                  float [deg] Telescope center section out temperature
    TCIBTEMP 0.0                                                                   float [deg] Telescope chimney IB temperature
    TCIMTEMP 0.0                                                                   float [deg] Telescope chimney IM temperature
    TCITTEMP 0.0                                                                   float [deg] Telescope chimney IT temperature
    TCOSTEMP 0.0                                                                   float [deg] Telescope chimney OS temperature
    TCOWTEMP 0.0                                                                   float [deg] Telescope chimney OW temperature
    TDBTEMP  9.3                                                                   float [deg] Telescope dec bore temperature
    TFLOWIN  0.0                                                                   float Telescope flow rate in
    TFLOWOUT 0.0                                                                   float Telescope flow rate out
    TGLYCOLI 9.9                                                                   float [deg] Telescope glycol in temperature
    TGLYCOLO 9.8                                                                   float [deg] Telescope glycol out temperature
    THINGES  11.4                                                                  float [deg] Telescope hinge S temperature
    THINGEW  11.2                                                                  float [deg] Telescope hinge W temperature
    TPMAVERT 8.931                                                                 float [deg] Telescope mirror averagetemperature
    TPMDESIT 7.0                                                                   float [deg] Telescope mirror desired temperature
    TPMEIBT  8.6                                                                   float [deg] Telescope mirror EIB temperature
    TPMEITT  8.6                                                                   float [deg] Telescope mirror EIT temperature
    TPMEOBT  8.5                                                                   float [deg] Telescope mirror EOB temperature
    TPMEOTT  9.0                                                                   float [deg] Telescope mirror EOT temperature
    TPMNIBT  8.4                                                                   float [deg] Telescope mirror NIB temperature
    TPMNITT  8.9                                                                   float [deg] Telescope mirror NIT temperature
    TPMNOBT  8.8                                                                   float [deg] Telescope mirror NOB temperature
    TPMNOTT  9.1                                                                   float [deg] Telescope mirror NOT temperature
    TPMRTDT  9.0                                                                   float [deg] Telescope mirror RTD temperature
    TPMSIBT  8.6                                                                   float [deg] Telescope mirror SIB temperature
    TPMSITT  8.8                                                                   float [deg] Telescope mirror SIT temperature
    TPMSOBT  8.2                                                                   float [deg] Telescope mirror SOB temperature
    TPMSOTT  8.9                                                                   float [deg] Telescope mirror SOT temperature
    TPMSTAT  ready                                                                 str   Telescope mirror status
    TPMWIBT  8.2                                                                   float [deg] Telescope mirror WIB temperature
    TPMWITT  9.1                                                                   float [deg] Telescope mirror WIT temperature
    TPMWOBT  8.3                                                                   float [deg] Telescope mirror WOB temperature
    TPMWOTT  8.9                                                                   float [deg] Telescope mirror WOT temperature
    TPCITEMP 8.5                                                                   float [deg] Telescope primary cell in temperature
    TPCOTEMP 8.6                                                                   float [deg] Telescope primary cell out temperature
    TPR1HUM  0.0                                                                   float Telescope probe 1 humidity
    TPR1TEMP 0.0                                                                   float [deg] Telescope probe1 temperature
    TPR2HUM  0.0                                                                   float Telescope probe 2 humidity
    TPR2TEMP 0.0                                                                   float [deg] Telescope probe2 temperature
    TSERVO   40.0                                                                  float Telescope servo setpoint
    TTRSTEMP 11.4                                                                  float [deg] Telescope top ring S temperature
    TTRWTEMP 11.0                                                                  float [deg] Telescope top ring W temperature
    TTRUETBT -4.2                                                                  float [deg] Telescope truss ETB temperature
    TTRUETTT 11.2                                                                  float [deg] Telescope truss ETT temperature
    TTRUNTBT 10.9                                                                  float [deg] Telescope truss NTB temperature
    TTRUNTTT 11.2                                                                  float [deg] Telescope truss NTT temperature
    TTRUSTBT 10.7                                                                  float [deg] Telescope truss STB temperature
    TTRUSTST 10.8                                                                  float [deg] Telescope truss STS temperature
    TTRUSTTT 11.1                                                                  float [deg] Telescope truss STT temperature
    TTRUTSBT 11.8                                                                  float [deg] Telescope truss TSB temperature
    TTRUTSMT 11.8                                                                  float [deg] Telescope truss TSM temperature
    TTRUTSTT 11.8                                                                  float [deg] Telescope truss TST temperature
    TTRUWTBT 10.5                                                                  float [deg] Telescope truss WTB temperature
    TTRUWTTT 10.9                                                                  float [deg] Telescope truss WTT temperature
    ALARM    F                                                                     bool  UPS major alarm or check battery
    ALARM-ON F                                                                     bool  UPS active alarm condition
    BATTERY  100.0                                                                 float [%] UPS Battery left
    SECLEFT  5178.0                                                                float [s] UPS Seconds left
    UPSSTAT  System Normal - On Line(7)                                            str   UPS Status
    INAMPS   70.4                                                                  float [A] UPS total input current
    OUTWATTS 5000.0,7200.0,4800.0                                                  str   [W] UPS Phase A, B, C output watts
    COMPDEW  -12.9                                                                 float [deg C] Computer room dewpoint
    COMPHUM  7.4                                                                   float [%] Computer room humidity
    COMPAMB  19.5                                                                  float [deg C] Computer room ambient temperature
    COMPTEMP 24.5                                                                  float [deg C] Computer room hygrometer temperature
    DEWPOINT 11.5                                                                  float [deg C] (outside) dewpoint
    HUMIDITY 10.0                                                                  float [%] (outside) humidity
    PRESSURE 795.0                                                                 float [torr] (outside) air pressure
    OUTTEMP  0.0                                                                   float [deg C] outside temperature
    WINDDIR  55.0                                                                  float [deg] wind direction
    WINDSPD  27.3                                                                  float [m/s] wind speed
    GUST     20.6                                                                  float [m/s] Wind gusts speed
    AMNIENTN 13.5                                                                  float [deg C] ambient temperature north
    CFLOOR   8.9                                                                   float [deg C] temperature on C floor
    NWALLIN  13.9                                                                  float [deg C] temperature at north wall inside
    NWALLOUT 9.6                                                                   float [deg C] temperature at north wall outside
    WWALLIN  12.9                                                                  float [deg C] temperature at west wall inside
    WWALLOUT 10.6                                                                  float [deg C] temperature at west wall outside
    AMBIENTS 14.8                                                                  float [deg C] ambient temperature south
    FLOOR    12.6                                                                  float [deg C] temperature at floor (LCR)
    EWALLCMP 10.8                                                                  float [deg C] temperature at east wall, computer room
    EWALLCOU 10.6                                                                  float [deg C] temperature at east wall, Coude room
    ROOF     10.3                                                                  float [deg C] temperature on roof
    ROOFAMB  10.6                                                                  float [deg C] ambient temperature on roof
    DOMEBLOW 10.4                                                                  float [deg C] temperature at dome back, lower
    DOMEBUP  10.7                                                                  float [deg C] temperature at dome back, upper
    DOMELLOW 10.8                                                                  float [deg C] temperature at dome left, lower
    DOMELUP  10.8                                                                  float [deg C] temperature at dome left, upper
    DOMERLOW 10.6                                                                  float [deg C] temperature at dome right, lower
    DOMERUP  10.5                                                                  float [deg C] temperature at dome right, upper
    PLATFORM 10.4                                                                  float [deg C] temperature at platform
    SHACKC   14.4                                                                  float [deg C] temperature at shack ceiling
    SHACKW   13.7                                                                  float [deg C] temperature at shack wall
    STAIRSL  10.5                                                                  float [deg C] temperature at stairs, lower
    STAIRSM  10.4                                                                  float [deg C] temperature at stairs, mid
    STAIRSU  10.6                                                                  float [deg C] temperature at stairs, upper
    TELBASE  9.6                                                                   float [deg C] temperature at telescope base
    UTILWALL 11.1                                                                  float [deg C] temperature at utility room wall
    UTILROOM 10.9                                                                  float [deg C] temperature in utilitiy room
    TNFSPROC 8.1963                                                                float [s] PlateMaker NFSPROC processing time
    TGFAPROC 7.9212                                                                float [s] PlateMaker GFAPROC processing time
    SIMGFAP  F                                                                     bool  DOS Control: simulate GFAPROC
    USEFVC   T                                                                     bool  DOS Control: use fvc
    USEFID   T                                                                     bool  DOS Control: use fiducials
    USEILLUM T                                                                     bool  DOS Control: use illuminator
    USEXSRVR T                                                                     bool  DOS Control: use exposure server
    USEOPENL T                                                                     bool  DOS Control: use open loop move
    STOPGUDR T                                                                     bool  DOS Control: stop guider
    STOPFOCS T                                                                     bool  DOS Control: stop focus
    STOPSKY  T                                                                     bool  DOS Control: stop sky monitor
    KEEPGUDR F                                                                     bool  DOS Control: keep guider running
    KEEPFOCS F                                                                     bool  DOS Control: keep focus running
    KEEPSKY  F                                                                     bool  DOS Control: keep sky mon. running
    REACQUIR F                                                                     bool  DOS Control: reacquire same files
    EXCLUDED                                                                       str   Components excluded from this exposure
    FVCTIME  2.0                                                                   float [s] FVC exposure time
    SIMGFACQ F                                                                     bool
    POSCNVGD F                                                                     bool
    GUIEXPID 69022                                                                 int   Guider exposure id at start of spectro exp.
    IGFRMNUM 12                                                                    int   Guider frame number at start of spectro exp.
    FOCEXPID 69022                                                                 int   Focus exposure id at start of spectro exp.
    IFFRMNUM 1                                                                     int   Focus frame number at start of spectro exp.
    SKYEXPID 69022                                                                 int   Sky exposure id at start of spectro exp.
    ISFRMNUM 1                                                                     int   Sky frame number at start of spectro exp.
    FGFRMNUM 46                                                                    int   Guider frame number at end of spectro exp.
    FFFRMNUM 6                                                                     int   Focus frame number at end of spectro exp.
    FSFRMNUM 5                                                                     int   Sky frame number at end of spectro exp.
    HELIOCOR 0.9999115198216216                                                    float
    NSPEC    500                                                                   int   Number of spectra
    WAVEMIN  5760.0                                                                float First wavelength [Angstroms]
    WAVEMAX  7620.0                                                                float Last wavelength [Angstroms]
    WAVESTEP 0.8                                                                   float Wavelength step size [Angstroms]
    SPECTER  0.10.0                                                                str   https://github.com/desihub/specter
    IN_PSF   SPECPROD/exposures/20201220/00069022/psf-r3-00069022.fits             str   Input sp
    IN_IMG   SPECPROD/preproc/20201220/00069022/preproc-r3-00069022.fits           str
    ORIG_PSF SPECPROD/calibnight/20201220/psfnight-r3-20201220.fits                str
    BUNIT    electron/Angstrom                                                     str
    IN_SKY   SPECPROD/exposures/20201220/00069022/sky-r3-00069022.fits             str
    FIBERFLT SPECPROD/exposures/20201220/00069022/fiberflatexp-r3-00069022.fits    str
    ======== ===================================================================== ===== ===============================================

Data: FITS image [float32, 2326x500]

HDU1
----

EXTNAME = IVAR

Inverse variance of the electrons in HDU0.

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

Mask of spectral data; 0=good.

Prior to desispec/0.24.0 and software release 18.9, the MASK HDU was compressed.

TODO: Add link to definition of which bits mean what.

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

1D array of wavelengths.

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

Fibermap information combining fiberassign request with actual fiber locations.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ======================================================================== ======= ==============================================
    KEY      Example Value                                                            Type    Comment
    ======== ======================================================================== ======= ==============================================
    NAXIS1   385                                                                      int     length of dimension 1
    NAXIS2   500                                                                      int     length of dimension 2
    TILEID   80616                                                                    int
    TILERA   356.0                                                                    float
    TILEDEC  29.0                                                                     float
    FIELDROT -0.00962199210064233                                                     float
    FA_PLAN  2022-07-01T00:00:00.000                                                  str
    FA_HA    0.0                                                                      float
    FA_RUN   2020-03-06T00:00:00                                                      str
    REQRA    356.0                                                                    float
    REQDEC   29.0                                                                     float
    FIELDNUM 0                                                                        int
    FA_VER   2.0.0.dev2618                                                            str
    FA_SURV  sv1                                                                      str
    LONGSTRN OGIP 1.0                                                                 str
    GFA      /data/target/catalogs/dr9/0.47.0/gfas                                    str
    SKY      /data/target/catalogs/dr9/0.47.0/skies                                   str
    SKYSUPP  /data/target/catalogs/gaiadr2/0.47.0/skies-supp                          str
    TARG     /data/target/catalogs/dr9/0.47.0/targets/sv1/resolve/bright/             str
    FAFLAVOR sv1bgsmws                                                                str
    FAOUTDIR /software/datasystems/users/raichoor/fiberassign-test/desi-sv1-20201218/ str
    PMTIME   2020-12-18T00:00:00.000                                                  str
    RUNDATE  2020-03-06T00:00:00                                                      str
    SCTARG   STD_WD,BGS_ANY,MWS_ANY                                                   str
    OBSCON   DARK|GRAY|BRIGHT                                                         str
    MODULE   CI                                                                       str
    EXPID    69022                                                                    int
    EXPFRAME 0                                                                        int
    COSMSPLT F                                                                        bool
    MAXSPLIT 0                                                                        int
    SPLITIDS 69022                                                                    str
    FIBASSGN /data/tiles/SVN_tiles/080/fiberassign-080616.fits                        str
    FLAVOR   science                                                                  str
    OBSTYPE  SCIENCE                                                                  str
    SEQUENCE DESI                                                                     str
    MANIFEST F                                                                        bool
    OBJECT                                                                            str
    PURPOSE  Commissioning                                                            str
    PROGRAM  SV1 BGS+MWS tile 80616                                                   str
    PROPID   2019B-5000                                                               str
    OBSERVER DESIObserver                                                             str
    LEAD     RunManager                                                               str
    INSTRUME DESI                                                                     str
    OBSERVAT KPNO                                                                     str
    OBS-LAT  31.96403                                                                 str
    OBS-LONG -111.59989                                                               str
    OBS-ELEV 2097.0                                                                   float
    TELESCOP KPNO 4.0-m telescope                                                     str
    CORRCTOR DESI Corrector                                                           str
    SEQNUM   1                                                                        int
    NIGHT    20201220                                                                 int
    TIMESYS  UTC                                                                      str
    DATE-OBS 2020-12-21T02:36:32.099838                                               str
    MJD-OBS  59204.10870486                                                           float
    OPENSHUT 2020-12-21T02:36:32.099838                                               str
    CAMSHUT  open                                                                     str
    ST       01:10:39.210                                                             str
    ACQTIME  15.0                                                                     float
    GUIDTIME 5.0                                                                      float
    FOCSTIME 60.0                                                                     float
    SKYTIME  60.0                                                                     float
    WHITESPT F                                                                        bool
    ZENITH   F                                                                        bool
    SEANNEX  F                                                                        bool
    BEYONDP  F                                                                        bool
    FIDUCIAL off                                                                      str
    BACKLIT  off                                                                      str
    AIRMASS  1.060311                                                                 float
    FOCUS    1426.5,-501.4,81.0,-2.6,42.3,169.2                                       str
    VCCD     ON                                                                       str
    TRUSTEMP 11.767                                                                   float
    PMIRTEMP 8.925                                                                    float
    PMREADY  T                                                                        bool
    PMCOVER  open                                                                     str
    PMCOOL   off                                                                      str
    DOMSHUTU open                                                                     str
    DOMSHUTL open                                                                     str
    DOMLIGHH off                                                                      str
    DOMLIGHL off                                                                      str
    DOMEAZ   255.166                                                                  float
    DOMINPOS T                                                                        bool
    EQUINOX  2000.0                                                                   float
    GUIDOFFR -0.052283                                                                float
    GUIDOFFD 0.136634                                                                 float
    MOONDEC  -8.975162                                                                float
    MOONRA   352.538429                                                               float
    MOUNTAZ  266.70224                                                                float
    MOUNTDEC 28.999221                                                                float
    MOUNTEL  71.039837                                                                float
    MOUNTHA  21.769281                                                                float
    INCTRL   T                                                                        bool
    INPOS    T                                                                        bool
    MNTOFFD  -15.76                                                                   float
    MNTOFFR  29.32                                                                    float
    PARALLAC 75.635085                                                                float
    SKYDEC   28.999221                                                                float
    SKYRA    355.996551                                                               float
    TARGTDEC 28.999221                                                                float
    TARGTRA  355.996551                                                               float
    TARGTAZ  267.074049                                                               float
    TARGTEL  70.563787                                                                float
    TRGTOFFD 0.0                                                                      float
    TRGTOFFR 0.0                                                                      float
    ZD       19.436213                                                                float
    TCSST    01:13:18.668                                                             str
    TCSMJD   59204.110981                                                             float
    USEETC   F                                                                        bool
    ACQCAM   GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                                str
    GUIDECAM GUIDE0,GUIDE2,GUIDE3,GUIDE5,GUIDE7,GUIDE8                                str
    FOCUSCAM FOCUS1,FOCUS4,FOCUS6,FOCUS9                                              str
    SKYCAM   SKYCAM0,SKYCAM1                                                          str
    REQADC   65.78,85.28                                                              str
    ADCCORR  T                                                                        bool
    ADC1PHI  65.780005                                                                float
    ADC2PHI  85.279991                                                                float
    ADC1HOME F                                                                        bool
    ADC2HOME F                                                                        bool
    ADC1NREV -1.0                                                                     float
    ADC2NREV 0.0                                                                      float
    ADC1STAT STOPPED                                                                  str
    ADC2STAT STOPPED                                                                  str
    USESKY   T                                                                        bool
    USEFOCUS T                                                                        bool
    HEXPOS   1426.5,-501.3,81.0,-2.6,42.3,171.9                                       str
    HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                                                  str
    USEROTAT T                                                                        bool
    ROTOFFST 167.1                                                                    float
    ROTENBLD T                                                                        bool
    ROTRATE  0.0                                                                      float
    RESETROT F                                                                        bool
    USEPOS   T                                                                        bool
    PETALS   PETAL0,PETAL1,PETAL2,PETAL3,PETAL4,PETAL5,PETAL6,PETAL7,PETAL8,PETAL9    str
    POSCYCLE 1                                                                        int
    POSONTGT 3626                                                                     int
    POSONFRC 0.8613                                                                   float
    POSDISAB 37                                                                       int
    POSENABL 4210                                                                     int
    POSRMS   0.0171                                                                   float
    POSITER  1                                                                        int
    POSFRACT 0.95                                                                     float
    POSTOLER 0.01                                                                     float
    POSMVALL T                                                                        bool
    USEGUIDR T                                                                        bool
    GUIDMODE catalog                                                                  str
    USEAOS   F                                                                        bool
    USEDONUT T                                                                        bool
    USESPCTR T                                                                        bool
    SPCGRPHS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                                  str
    ILLSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                                  str
    CCDSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                                  str
    TDEWPNT  -16.043                                                                  float
    TAIRFLOW 0.0                                                                      float
    TAIRITMP 11.8                                                                     float
    TAIROTMP 11.7                                                                     float
    TAIRTEMP 10.65                                                                    float
    TCASITMP 0.0                                                                      float
    TCASOTMP 10.8                                                                     float
    TCSITEMP 9.3                                                                      float
    TCSOTEMP 10.8                                                                     float
    TCIBTEMP 0.0                                                                      float
    TCIMTEMP 0.0                                                                      float
    TCITTEMP 0.0                                                                      float
    TCOSTEMP 0.0                                                                      float
    TCOWTEMP 0.0                                                                      float
    TDBTEMP  9.3                                                                      float
    TFLOWIN  0.0                                                                      float
    TFLOWOUT 0.0                                                                      float
    TGLYCOLI 9.9                                                                      float
    TGLYCOLO 9.8                                                                      float
    THINGES  11.4                                                                     float
    THINGEW  11.2                                                                     float
    TPMAVERT 8.931                                                                    float
    TPMDESIT 7.0                                                                      float
    TPMEIBT  8.6                                                                      float
    TPMEITT  8.6                                                                      float
    TPMEOBT  8.5                                                                      float
    TPMEOTT  9.0                                                                      float
    TPMNIBT  8.4                                                                      float
    TPMNITT  8.9                                                                      float
    TPMNOBT  8.8                                                                      float
    TPMNOTT  9.1                                                                      float
    TPMRTDT  9.0                                                                      float
    TPMSIBT  8.6                                                                      float
    TPMSITT  8.8                                                                      float
    TPMSOBT  8.2                                                                      float
    TPMSOTT  8.9                                                                      float
    TPMSTAT  ready                                                                    str
    TPMWIBT  8.2                                                                      float
    TPMWITT  9.1                                                                      float
    TPMWOBT  8.3                                                                      float
    TPMWOTT  8.9                                                                      float
    TPCITEMP 8.5                                                                      float
    TPCOTEMP 8.6                                                                      float
    TPR1HUM  0.0                                                                      float
    TPR1TEMP 0.0                                                                      float
    TPR2HUM  0.0                                                                      float
    TPR2TEMP 0.0                                                                      float
    TSERVO   40.0                                                                     float
    TTRSTEMP 11.4                                                                     float
    TTRWTEMP 11.0                                                                     float
    TTRUETBT -4.2                                                                     float
    TTRUETTT 11.2                                                                     float
    TTRUNTBT 10.9                                                                     float
    TTRUNTTT 11.2                                                                     float
    TTRUSTBT 10.7                                                                     float
    TTRUSTST 10.8                                                                     float
    TTRUSTTT 11.1                                                                     float
    TTRUTSBT 11.8                                                                     float
    TTRUTSMT 11.8                                                                     float
    TTRUTSTT 11.8                                                                     float
    TTRUWTBT 10.5                                                                     float
    TTRUWTTT 10.9                                                                     float
    ALARM    F                                                                        bool
    ALARM-ON F                                                                        bool
    BATTERY  100.0                                                                    float
    SECLEFT  5178.0                                                                   float
    UPSSTAT  System Normal - On Line(7)                                               str
    INAMPS   70.4                                                                     float
    OUTWATTS 5000.0,7200.0,4800.0                                                     str
    COMPDEW  -12.9                                                                    float
    COMPHUM  7.4                                                                      float
    COMPAMB  19.5                                                                     float
    COMPTEMP 24.5                                                                     float
    DEWPOINT 11.5                                                                     float
    HUMIDITY 10.0                                                                     float
    PRESSURE 795.0                                                                    float
    OUTTEMP  0.0                                                                      float
    WINDDIR  55.0                                                                     float
    WINDSPD  27.3                                                                     float
    GUST     20.6                                                                     float
    AMNIENTN 13.5                                                                     float
    CFLOOR   8.9                                                                      float
    NWALLIN  13.9                                                                     float
    NWALLOUT 9.6                                                                      float
    WWALLIN  12.9                                                                     float
    WWALLOUT 10.6                                                                     float
    AMBIENTS 14.8                                                                     float
    FLOOR    12.6                                                                     float
    EWALLCMP 10.8                                                                     float
    EWALLCOU 10.6                                                                     float
    ROOF     10.3                                                                     float
    ROOFAMB  10.6                                                                     float
    DOMEBLOW 10.4                                                                     float
    DOMEBUP  10.7                                                                     float
    DOMELLOW 10.8                                                                     float
    DOMELUP  10.8                                                                     float
    DOMERLOW 10.6                                                                     float
    DOMERUP  10.5                                                                     float
    PLATFORM 10.4                                                                     float
    SHACKC   14.4                                                                     float
    SHACKW   13.7                                                                     float
    STAIRSL  10.5                                                                     float
    STAIRSM  10.4                                                                     float
    STAIRSU  10.6                                                                     float
    TELBASE  9.6                                                                      float
    UTILWALL 11.1                                                                     float
    UTILROOM 10.9                                                                     float
    RADESYS  FK5                                                                      str
    TNFSPROC 8.1963                                                                   float
    TGFAPROC 7.9212                                                                   float
    SIMGFAP  F                                                                        bool
    USEFVC   T                                                                        bool
    USEFID   T                                                                        bool
    USEILLUM T                                                                        bool
    USEXSRVR T                                                                        bool
    USEOPENL T                                                                        bool
    STOPGUDR T                                                                        bool
    STOPFOCS T                                                                        bool
    STOPSKY  T                                                                        bool
    KEEPGUDR F                                                                        bool
    KEEPFOCS F                                                                        bool
    KEEPSKY  F                                                                        bool
    REACQUIR F                                                                        bool
    FILENAME /exposures/desi/20201220/00069022/desi-00069022.fits.fz                  str
    EXCLUDED                                                                          str
    DOSVER   trunk                                                                    str
    OCSVER   1.2                                                                      float
    CONSTVER DESI:CURRENT                                                             str
    INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini                         str
    REQTIME  300.0                                                                    float
    FVCTIME  2.0                                                                      float
    SIMGFACQ F                                                                        bool
    POSCNVGD F                                                                        bool
    GUIEXPID 69022                                                                    int
    IGFRMNUM 12                                                                       int
    FOCEXPID 69022                                                                    int
    IFFRMNUM 1                                                                        int
    SKYEXPID 69022                                                                    int
    ISFRMNUM 1                                                                        int
    FGFRMNUM 46                                                                       int
    FFFRMNUM 6                                                                        int
    FSFRMNUM 5                                                                        int
    FRAMES   47                                                                       int
    DELTARA  None                                                                     Unknown
    DELTADEC None                                                                     Unknown
    GSGUIDE0 (980.05,685.98),(878.97,731.68)                                          str
    GSGUIDE2 (372.65,939.43),(784.50,1529.96)                                         str
    GSGUIDE3 (365.22,1423.83),(249.12,411.52)                                         str
    GSGUIDE5 (848.52,78.26),(516.16,1410.54)                                          str
    GSGUIDE7 (540.95,1848.95),(504.68,831.62)                                         str
    GSGUIDE8 (720.29,552.69),(499.80,465.13)                                          str
    ARCHIVE  /exposures/desi/20201220/00069022/guide-00069022.fits.fz                 str
    GUIDEFIL guide-00069022.fits.fz                                                   str
    COORDFIL coordinates-00069022.fits                                                str
    TIME-OBS 02:39:11.845920                                                          str
    EXPTIME  300.007                                                                  float
    VCCDON   2020-12-14T17:48:28.296248                                               str
    VCCDSEC  550592.7                                                                 float
    SPECGRPH 3                                                                        int
    SPECID   6                                                                        int
    FEEBOX   lbnl074                                                                  str
    VESSEL   11                                                                       int
    FEEVER   v20160312                                                                str
    FEEPOWER ON                                                                       str
    FEEDMASK 2134851391                                                               int
    FEECMASK 1048575                                                                  int
    CCDTEMP  -140.2798                                                                float
    CRYOPRES 7.233e-08                                                                str
    CLOCK7   -2.0001,3.9999                                                           str
    TRIMSECA [8:2064, 2:2065]                                                         str
    CCDNAME  CCDSM6R                                                                  str
    TRIMSECD [2193:4249, 2130:4193]                                                   str
    OFFSET2  0.4000000059604645,-8.961                                                str
    CPUTEMP  56.625                                                                   float
    DAC11    -25.0003,-24.7086                                                        str
    AMPSECA  [1:2057, 1:2064]                                                         str
    CCDCFG   M1-50_lbnl_20190719.cfg                                                  str
    TRIMSECB [2193:4249, 2:2065]                                                      str
    CLOCK3   -2.0001,3.9999                                                           str
    CCDSECA  [1:2057, 1:2064]                                                         str
    CLOCK4   9.9999,0.0                                                               str
    DAC0     -9.0002,-8.9095                                                          str
    CLOCK10  9.9992,2.9993                                                            str
    BIASSECA [2065:2128, 2:2065]                                                      str
    PRRSECA  [8:2064, 1:1]                                                            str
    DAC7     6.4999,6.4856                                                            str
    AMPSECB  [4114:2058, 1:2064]                                                      str
    DAC10    -25.0003,-24.9906                                                        str
    DELAYS   20, 20, 25, 30, 7, 3000, 7, 7, 7, 7                                      str
    CCDSECD  [2058:4114, 2065:4128]                                                   str
    CASETEMP 56.4919                                                                  float
    CLOCK6   9.9999,0.0                                                               str
    CLOCK13  9.9992,2.9993                                                            str
    CLOCK9   9.9992,2.9993                                                            str
    DAC8     -25.0003,-25.0202                                                        str
    DAC9     -25.0003,-24.6789                                                        str
    ORSECB   [2193:4249, 2066:2097]                                                   str
    CLOCK1   9.9999,0.0                                                               str
    DETSECC  [1:2057, 2065:4128]                                                      str
    AMPSECD  [4114:2058, 4128:2065]                                                   str
    CLOCK5   9.9999,0.0                                                               str
    ORSECA   [8:2064, 2066:2097]                                                      str
    DAC15    0.0,0.0297                                                               str
    DATASECA [8:2064, 2:2065]                                                         str
    CCDPREP  purge,clear                                                              str
    OFFSET7  2.0,6.4908                                                               str
    DAC5     5.9998,6.028                                                             str
    CLOCK12  9.9992,2.9993                                                            str
    CCDSECB  [2058:4114, 1:2064]                                                      str
    OFFSET6  2.0,6.0332                                                               str
    DAC4     5.9998,6.028                                                             str
    PRESECC  [1:7, 2130:4193]                                                         str
    OFFSET5  2.0,6.028                                                                str
    DAC2     -9.0002,-8.9713                                                          str
    CRYOTEMP 162.97                                                                   float
    PRESECB  [4250:4256, 2:2065]                                                      str
    DIGITIME 47.1031                                                                  float
    DAC3     -10.5005,-10.3824                                                        str
    CAMERA   r3                                                                       str
    DETSECB  [2058:4114, 1:2064]                                                      str
    OFFSET1  0.4000000059604645,-8.8065                                               str
    DATASECD [2193:4249, 2130:4193]                                                   str
    SETTINGS detectors_sm_20191211.json                                               str
    CLOCK11  9.9992,2.9993                                                            str
    DAC13    0.0,0.0                                                                  str
    CLOCK14  9.9992,2.9993                                                            str
    CCDSECC  [1:2057, 2065:4128]                                                      str
    DATASECC [8:2064, 2130:4193]                                                      str
    CLOCK0   9.9999,0.0                                                               str
    CLOCK15  9.9992,2.9993                                                            str
    DAC12    0.0,0.0297                                                               str
    CCDSIZE  4194,4256                                                                str
    OFFSET0  0.4000000059604645,-8.9095                                               str
    ORSECD   [2193:4249, 2098:2129]                                                   str
    DAC16    48.0,46.7082                                                             str
    PRRSECC  [8:2064, 4194:4194]                                                      str
    PRRSECD  [2193:4249, 4194:4194]                                                   str
    BIASSECB [2129:2192, 2:2065]                                                      str
    DETSECD  [2058:4114, 2065:4128]                                                   str
    CLOCK18  9.0,0.9999                                                               str
    DAC17    20.0008,14.274                                                           str
    CCDTMING default_lbnl_timing_20180905.txt                                         str
    DETECTOR M1-50                                                                    str
    PRRSECB  [2193:4249, 1:1]                                                         str
    TRIMSECC [8:2064, 2130:4193]                                                      str
    DAC14    0.0,0.0148                                                               str
    BIASSECD [2129:2192, 2130:4193]                                                   str
    CDSPARMS 400, 400, 8, 2000                                                        str
    OFFSET3  0.4000000059604645,-10.3721                                              str
    PRESECA  [1:7, 2:2065]                                                            str
    ORSECC   [8:2064, 2098:2129]                                                      str
    DAC6     5.9998,6.0332                                                            str
    PGAGAIN  3                                                                        int
    DAC1     -9.0002,-8.8065                                                          str
    DATASECB [2193:4249, 2:2065]                                                      str
    CLOCK2   9.9999,0.0                                                               str
    CLOCK16  9.9999,3.0                                                               str
    PRESECD  [4250:4256, 2130:4193]                                                   str
    OFFSET4  2.0,6.0332                                                               str
    CLOCK17  9.0,0.9999                                                               str
    AMPSECC  [1:2057, 4128:2065]                                                      str
    CLOCK8   9.9992,2.9993                                                            str
    DETSECA  [1:2057, 1:2064]                                                         str
    BIASSECC [2065:2128, 2130:4193]                                                   str
    BLDTIME  0.3504                                                                   float
    OBSID    kp4m20201221t023911                                                      str
    PROCTYPE RAW                                                                      str
    PRODTYPE image                                                                    str
    GAINA    1.681                                                                    float
    SATULEVA 28000.0                                                                  float
    OSTEPA   0.7048677125421818                                                       float
    OMETHA   AVERAGE                                                                  str
    OVERSCNA 1979.586454500641                                                        float
    OBSRDNA  2.618213792981265                                                        float
    SATUELEA 43740.31516998442                                                        float
    GAINB    1.625                                                                    float
    SATULEVB 57000.0                                                                  float
    OSTEPB   0.6850349189899134                                                       float
    OMETHB   AVERAGE                                                                  str
    OVERSCNB 1997.289875350671                                                        float
    OBSRDNB  3.12518985733541                                                         float
    SATUELEB 89379.40395255515                                                        float
    GAINC    1.477                                                                    float
    SATULEVC 59000.0                                                                  float
    OSTEPC   0.6403308619337622                                                       float
    OMETHC   AVERAGE                                                                  str
    OVERSCNC 1974.691977751432                                                        float
    OBSRDNC  2.344388520757958                                                        float
    SATUELEC 84226.37994886114                                                        float
    GAIND    1.492                                                                    float
    SATULEVD 62000.0                                                                  float
    OSTEPD   0.6246898852550657                                                       float
    OMETHD   AVERAGE                                                                  str
    OVERSCND 1998.214476179268                                                        float
    OBSRDND  2.301320302261815                                                        float
    SATUELED 89522.66400154053                                                        float
    FIBERMIN 1500                                                                     int
    CHECKSUM 9VRaITQX9TQaGTQU                                                         str     HDU checksum updated 2022-02-14T06:14:07
    DATASUM  3502588181                                                               str     data unit checksum updated 2022-02-14T06:14:07
    ======== ======================================================================== ======= ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

===================== ======= ===== ===========
Name                  Type    Units Description
===================== ======= ===== ===========
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
MASKBITS              int16
SERSIC                float32
SHAPE_R               float32
SHAPE_E1              float32
SHAPE_E2              float32
PHOTSYS               char[1]
PRIORITY_INIT         int64
NUMOBS_INIT           int64
SV1_DESI_TARGET       int64
SV1_BGS_TARGET        int64
SV1_MWS_TARGET        int64
SV1_SCND_TARGET       int64
DESI_TARGET           int64
BGS_TARGET            int64
MWS_TARGET            int64
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


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
