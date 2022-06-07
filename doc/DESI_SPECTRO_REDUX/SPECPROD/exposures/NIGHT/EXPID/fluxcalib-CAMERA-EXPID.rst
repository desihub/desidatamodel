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
HDU4_  FIBERCORR        BINTABLE *Brief Description*
HDU5_  STDSTAR_FIBERMAP BINTABLE *Brief Description*
====== ================ ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = FLUXCALIB

Flux calibration model such that calibrated flux = uncalibrated photons / model.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ===================================================================== ===== ===============================================
    KEY      Example Value                                                         Type  Comment
    ======== ===================================================================== ===== ===============================================
    NAXIS1   2881                                                                  int
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
    VCCDON   2020-12-09T21:23:25.472733                                            str   Time when CCD voltage was turned on
    VCCDSEC  969696.0                                                              float [s] CCD on time in seconds
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
    SPECGRPH 6                                                                     int   Spectrograph logical name (SP)
    SPECID   7                                                                     int   Spectrograph serial number (SM)
    FEEBOX   lbnl061                                                               str   CCD Controller serial number
    VESSEL   21                                                                    int   Cryostat serial number
    FEEVER   v20160312                                                             str   CCD Controller version
    FEEPOWER ON                                                                    str   FEE power status
    FEEDMASK 2134851391                                                            int   FEE dac mask
    FEECMASK 1048575                                                               int   FEE clk mask
    CCDTEMP  -134.1517                                                             float [deg C] CCD controller CCD temperature
    RADESYS  FK5                                                                   str   Coordinate reference frame of major/minor axes
    FILENAME /exposures/desi/specs/20201220/00069022/sp1-00069022.fits.fz          str   Name
    DOSVER   trunk                                                                 str   DOS software version
    OCSVER   1.2                                                                   float OCS software version
    CONSTVER DESI:CURRENT                                                          str   Constants version
    INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini                      str   DOS Configuration
    PRESECC  [1:7, 2130:4193]                                                      str   Prescan section for quadrant C
    CLOCK13  9.9992,2.9993                                                         str   [V] high rail, low rail
    DETECTOR M1-51                                                                 str   Detector (ccd) identification
    SETTINGS detectors_sm_20191211.json                                            str   Name of DESI CCD settings file
    PRRSECA  [8:2064, 1:1]                                                         str   Row prescan section for quadrant A
    CLOCK11  9.9992,2.9993                                                         str   [V] high rail, low rail
    OFFSET2  0.4000000059604645,-8.9507                                            str   [V] set value, measured value
    AMPSECC  [1:2057, 4128:2065]                                                   str   AMP section for quadrant C
    DAC11    -25.0003,-25.0351                                                     str   [V] set value, measured value
    CLOCK1   9.9999,0.0                                                            str   [V] high rail, low rail
    DAC7     5.9998,6.0017                                                         str   [V] set value, measured value
    DAC16    39.9961,39.5472                                                       str   [V] set value, measured value
    CCDSECB  [2058:4114, 1:2064]                                                   str   CCD section for quadrant B
    CLOCK17  9.0,0.9999                                                            str   [V] high rail, low rail
    CLOCK5   9.9999,0.0                                                            str   [V] high rail, low rail
    AMPSECB  [4114:2058, 1:2064]                                                   str   AMP section for quadrant B
    CLOCK4   9.9999,0.0                                                            str   [V] high rail, low rail
    DETSECB  [2058:4114, 1:2064]                                                   str   Detector section for quadrant B
    BIASSECA [2065:2128, 2:2065]                                                   str   Bias section for quadrant A
    CRYOPRES 2.938e-07                                                             str   [mb] Cryostat pressure (IP)
    CCDTMING default_lbnl_timing_20180905.txt                                      str   CCD timing file
    CLOCK9   9.9992,2.9993                                                         str   [V] high rail, low rail
    PGAGAIN  3                                                                     int   Controller gain
    CLOCK6   9.9999,0.0                                                            str   [V] high rail, low rail
    OFFSET3  0.4000000059604645,-8.8889                                            str   [V] set value, measured value
    PRRSECB  [2193:4249, 1:1]                                                      str   Row prescan section for quadrant B
    DAC5     5.9998,6.0174                                                         str   [V] set value, measured value
    CLOCK3   -2.0001,3.9999                                                        str   [V] high rail, low rail
    DAC14    0.0,-0.0297                                                           str   [V] set value, measured value
    CLOCK15  9.9992,2.9993                                                         str   [V] high rail, low rail
    AMPSECD  [4114:2058, 4128:2065]                                                str   AMP section for quadrant D
    CCDSECA  [1:2057, 1:2064]                                                      str   CCD section for quadrant A
    DAC9     -25.0003,-25.0351                                                     str   [V] set value, measured value
    DAC10    -25.0003,-24.8273                                                     str   [V] set value, measured value
    CCDPREP  purge,clear                                                           str   CCD prep actions
    DAC4     5.9998,6.0437                                                         str   [V] set value, measured value
    OFFSET4  2.0,6.049                                                             str   [V] set value, measured value
    BLDTIME  0.3499                                                                float [s] Time to build image
    CLOCK16  9.9999,3.0                                                            str   [V] high rail, low rail
    DAC2     -9.0002,-8.961                                                        str   [V] set value, measured value
    OFFSET1  0.4000000059604645,-8.9507                                            str   [V] set value, measured value
    CLOCK10  9.9992,2.9993                                                         str   [V] high rail, low rail
    OFFSET7  2.0,6.0017                                                            str   [V] set value, measured value
    ORSECD   [2193:4249, 2098:2129]                                                str   Row bias section for quadrant D
    OFFSET0  0.4000000059604645,-8.9713                                            str   [V] set value, measured value
    CLOCK0   9.9999,0.0                                                            str   [V] high rail, low rail
    CRYOTEMP 139.986                                                               float [deg K] Cryostat CCD temperature
    DATASECB [2193:4249, 2:2065]                                                   str   Data section for quadrant B
    DAC6     5.9998,6.049                                                          str   [V] set value, measured value
    DAC12    0.0,-0.0148                                                           str   [V] set value, measured value
    CLOCK2   9.9999,0.0                                                            str   [V] high rail, low rail
    TRIMSECC [8:2064, 2130:4193]                                                   str   Trim section for quadrant C
    PRRSECD  [2193:4249, 4194:4194]                                                str   Row prescan section for quadrant D
    DAC15    0.0,0.0                                                               str   [V] set value, measured value
    DATASECA [8:2064, 2:2065]                                                      str   Data section for quadrant A
    DAC3     -9.0002,-8.8889                                                       str   [V] set value, measured value
    CCDSIZE  4194,4256                                                             str   CCD size in pixels (rows, columns)
    AMPSECA  [1:2057, 1:2064]                                                      str   AMP section for quadrant A
    PRESECD  [4250:4256, 2130:4193]                                                str   Prescan section for quadrant D
    ORSECA   [8:2064, 2066:2097]                                                   str   Row overscan section for quadrant A
    CCDSECC  [1:2057, 2065:4128]                                                   str   CCD section for quadrant C
    CLOCK18  9.0,0.9999                                                            str   [V] high rail, low rail
    DETSECD  [2058:4114, 2065:4128]                                                str   Detector section for quadrant D
    CCDSECD  [2058:4114, 2065:4128]                                                str   CCD section for quadrant D
    CPUTEMP  57.1172                                                               float [deg C] CCD controller CPU temperature
    DELAYS   20, 20, 25, 40, 7, 3000, 7, 7, 7, 7                                   str   [10] Delay settings
    DATASECD [2193:4249, 2130:4193]                                                str   Data section for quadrant D
    BIASSECC [2065:2128, 2130:4193]                                                str   Bias section for quadrant C
    CCDCFG   default_lbnl_20190717.cfg                                             str   CCD configuration file
    DATASECC [8:2064, 2130:4193]                                                   str   Data section for quadrant C
    BIASSECD [2129:2192, 2130:4193]                                                str   Bias section for quadrant D
    PRESECA  [1:7, 2:2065]                                                         str   Prescan section for quadrant A
    OFFSET6  2.0,6.0543                                                            str   [V] set value, measured value
    DETSECC  [1:2057, 2065:4128]                                                   str   Detector section for quadrant C
    DAC13    0.0,-0.0297                                                           str   [V] set value, measured value
    DETSECA  [1:2057, 1:2064]                                                      str   Detector section for quadrant A
    PRRSECC  [8:2064, 4194:4194]                                                   str   Row prescan section for quadrant C
    CLOCK12  9.9992,2.9993                                                         str   [V] high rail, low rail
    CASETEMP 56.8611                                                               float [deg C] CCD controller case temperature
    BIASSECB [2129:2192, 2:2065]                                                   str   Bias section for quadrant B
    OFFSET5  2.0,6.0174                                                            str   [V] set value, measured value
    CLOCK7   -2.0001,3.9999                                                        str   [V] high rail, low rail
    CLOCK8   9.9992,2.9993                                                         str   [V] high rail, low rail
    CAMERA   z6                                                                    str   Camera name
    PRESECB  [4250:4256, 2:2065]                                                   str   Prescan section for quadrant B
    TRIMSECB [2193:4249, 2:2065]                                                   str   Trim section for quadrant B
    DAC17    20.0008,11.9316                                                       str   [V] set value, measured value
    DIGITIME 47.5453                                                               float [s] Time to digitize image
    TRIMSECD [2193:4249, 2130:4193]                                                str   Trim section for quadrant D
    DAC8     -25.0003,-24.6196                                                     str   [V] set value, measured value
    TRIMSECA [8:2064, 2:2065]                                                      str   Trim section for quadrant A
    CLOCK14  9.9992,2.9993                                                         str   [V] high rail, low rail
    DAC0     -9.0002,-8.9713                                                       str   [V] set value, measured value
    CDSPARMS 400, 400, 8, 2000                                                     str   CDS parameters
    DAC1     -9.0002,-8.9507                                                       str   [V] set value, measured value
    ORSECC   [8:2064, 2098:2129]                                                   str   Row overscan section for quadrant C
    ORSECB   [2193:4249, 2066:2097]                                                str   Row overscan section for quadrant B
    CCDNAME  CCDSM7Z                                                               str   CCD name
    REQTIME  300.0                                                                 float [s] Requested exposure time
    OBSID    kp4m20201221t023911                                                   str   Unique observation identifier
    PROCTYPE RAW                                                                   str   Data processing level
    PRODTYPE image                                                                 str   Data product type
    CHECKSUM LfaELdXDLdaDLdUD                                                      str   HDU checksum updated 2022-02-14T08:22:45
    DATASUM  1867608608                                                            str   data unit checksum updated 2022-02-14T08:22:45
    GAINA    1.387                                                                 float e/ADU (gain applied to image)
    SATULEVA 61000.0                                                               float saturation or non lin. level, in ADU, inc. bias
    OSTEPA   0.7319095199345611                                                    float ADUs (max-min of median overscan per row)
    OMETHA   AVERAGE                                                               str   use average overscan
    OVERSCNA 1966.054034223049                                                     float ADUs (gain not applied)
    OBSRDNA  2.176414404248625                                                     float electrons (gain is applied)
    SATUELEA 81880.08305453263                                                     float saturation or non lin. level, in electrons
    GAINB    1.518                                                                 float e/ADU (gain applied to image)
    SATULEVB 65535.0                                                               float saturation or non lin. level, in ADU, inc. bias
    OSTEPB   0.5937273930649098                                                    float ADUs (max-min of median overscan per row)
    OMETHB   AVERAGE                                                               str   use average overscan
    OVERSCNB 1987.334317960662                                                     float ADUs (gain not applied)
    OBSRDNB  2.29569819578003                                                      float electrons (gain is applied)
    SATUELEB 96465.35650533572                                                     float saturation or non lin. level, in electrons
    GAINC    1.534                                                                 float e/ADU (gain applied to image)
    SATULEVC 40000.0                                                               float saturation or non lin. level, in ADU, inc. bias
    OSTEPC   0.9199855706829112                                                    float ADUs (max-min of median overscan per row)
    OMETHC   AVERAGE                                                               str   use average overscan
    OVERSCNC 1980.643479043017                                                     float ADUs (gain not applied)
    OBSRDNC  2.511180716174036                                                     float electrons (gain is applied)
    SATUELEC 58321.69290314802                                                     float saturation or non lin. level, in electrons
    GAIND    1.554                                                                 float e/ADU (gain applied to image)
    SATULEVD 62000.0                                                               float saturation or non lin. level, in ADU, inc. bias
    OSTEPD   1.375711494358256                                                     float ADUs (max-min of median overscan per row)
    OMETHD   AVERAGE                                                               str   use average overscan
    OVERSCND 1982.563334159938                                                     float ADUs (gain not applied)
    OBSRDND  2.417154801423475                                                     float electrons (gain is applied)
    SATUELED 93267.09657871546                                                     float saturation or non lin. level, in electrons
    FIBERMIN 3000                                                                  int
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
    WAVEMIN  7520.0                                                                float First wavelength [Angstroms]
    WAVEMAX  9824.0                                                                float Last wavelength [Angstroms]
    WAVESTEP 0.8                                                                   float Wavelength step size [Angstroms]
    SPECTER  0.10.0                                                                str   https://github.com/desihub/specter
    IN_PSF   SPECPROD/exposures/20201220/00069022/psf-z6-00069022.fits             str   Input sp
    IN_IMG   SPECPROD/preproc/20201220/00069022/preproc-z6-00069022.fits           str
    ORIG_PSF SPECPROD/calibnight/20201220/psfnight-z6-20201220.fits                str
    BUNIT    10**+17 cm2 count s / erg                                             str   i.e. (elec/A) / (1e-17 erg/s/cm2/A)
    IN_FRAME SPECPROD/exposures/20201220/00069022/frame-z6-00069022.fits           str
    IN_SKY   SPECPROD/exposures/20201220/00069022/sky-z6-00069022.fits             str
    FIBERFLT SPECPROD/exposures/20201220/00069022/fiberflatexp-z6-00069022.fits    str
    STDMODEL SPECPROD/exposures/20201220/00069022/stdstars-6-00069022.fits         str
    ======== ===================================================================== ===== ===============================================

Data: FITS image [float32, 2326x500]

HDU1
----

EXTNAME = IVAR

Inverse variance of flux calibration model.

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

Mask of flux calibration model; 0=good.

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

Wavelengths at which the flux calibration model is evaluated.

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

HDU4
----

EXTNAME = FIBERCORR

*Summarize the contents of this HDU.*

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

================= ======= ===== ===========
Name              Type    Units Description
================= ======= ===== ===========
FLAT_TO_PSF_FLUX  float64
PSF_TO_FIBER_FLUX float64
================= ======= ===== ===========

HDU5
----

EXTNAME = STDSTAR_FIBERMAP

Fibermap of what targets were assigned to what fibers.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ======================================================================== ======= ==============================================
    KEY      Example Value                                                            Type    Comment
    ======== ======================================================================== ======= ==============================================
    NAXIS1   385                                                                      int     length of dimension 1
    NAXIS2   18                                                                       int     length of dimension 2
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
    VCCDON   2020-12-09T21:23:25.472733                                               str
    VCCDSEC  969696.0                                                                 float
    SPECGRPH 6                                                                        int
    SPECID   7                                                                        int
    FEEBOX   lbnl061                                                                  str
    VESSEL   21                                                                       int
    FEEVER   v20160312                                                                str
    FEEPOWER ON                                                                       str
    FEEDMASK 2134851391                                                               int
    FEECMASK 1048575                                                                  int
    CCDTEMP  -134.1517                                                                float
    PRESECC  [1:7, 2130:4193]                                                         str
    CLOCK13  9.9992,2.9993                                                            str
    DETECTOR M1-51                                                                    str
    SETTINGS detectors_sm_20191211.json                                               str
    PRRSECA  [8:2064, 1:1]                                                            str
    CLOCK11  9.9992,2.9993                                                            str
    OFFSET2  0.4000000059604645,-8.9507                                               str
    AMPSECC  [1:2057, 4128:2065]                                                      str
    DAC11    -25.0003,-25.0351                                                        str
    CLOCK1   9.9999,0.0                                                               str
    DAC7     5.9998,6.0017                                                            str
    DAC16    39.9961,39.5472                                                          str
    CCDSECB  [2058:4114, 1:2064]                                                      str
    CLOCK17  9.0,0.9999                                                               str
    CLOCK5   9.9999,0.0                                                               str
    AMPSECB  [4114:2058, 1:2064]                                                      str
    CLOCK4   9.9999,0.0                                                               str
    DETSECB  [2058:4114, 1:2064]                                                      str
    BIASSECA [2065:2128, 2:2065]                                                      str
    CRYOPRES 2.938e-07                                                                str
    CCDTMING default_lbnl_timing_20180905.txt                                         str
    CLOCK9   9.9992,2.9993                                                            str
    PGAGAIN  3                                                                        int
    CLOCK6   9.9999,0.0                                                               str
    OFFSET3  0.4000000059604645,-8.8889                                               str
    PRRSECB  [2193:4249, 1:1]                                                         str
    DAC5     5.9998,6.0174                                                            str
    CLOCK3   -2.0001,3.9999                                                           str
    DAC14    0.0,-0.0297                                                              str
    CLOCK15  9.9992,2.9993                                                            str
    AMPSECD  [4114:2058, 4128:2065]                                                   str
    CCDSECA  [1:2057, 1:2064]                                                         str
    DAC9     -25.0003,-25.0351                                                        str
    DAC10    -25.0003,-24.8273                                                        str
    CCDPREP  purge,clear                                                              str
    DAC4     5.9998,6.0437                                                            str
    OFFSET4  2.0,6.049                                                                str
    BLDTIME  0.3499                                                                   float
    CLOCK16  9.9999,3.0                                                               str
    DAC2     -9.0002,-8.961                                                           str
    OFFSET1  0.4000000059604645,-8.9507                                               str
    CLOCK10  9.9992,2.9993                                                            str
    OFFSET7  2.0,6.0017                                                               str
    ORSECD   [2193:4249, 2098:2129]                                                   str
    OFFSET0  0.4000000059604645,-8.9713                                               str
    CLOCK0   9.9999,0.0                                                               str
    CRYOTEMP 139.986                                                                  float
    DATASECB [2193:4249, 2:2065]                                                      str
    DAC6     5.9998,6.049                                                             str
    DAC12    0.0,-0.0148                                                              str
    CLOCK2   9.9999,0.0                                                               str
    TRIMSECC [8:2064, 2130:4193]                                                      str
    PRRSECD  [2193:4249, 4194:4194]                                                   str
    DAC15    0.0,0.0                                                                  str
    DATASECA [8:2064, 2:2065]                                                         str
    DAC3     -9.0002,-8.8889                                                          str
    CCDSIZE  4194,4256                                                                str
    AMPSECA  [1:2057, 1:2064]                                                         str
    PRESECD  [4250:4256, 2130:4193]                                                   str
    ORSECA   [8:2064, 2066:2097]                                                      str
    CCDSECC  [1:2057, 2065:4128]                                                      str
    CLOCK18  9.0,0.9999                                                               str
    DETSECD  [2058:4114, 2065:4128]                                                   str
    CCDSECD  [2058:4114, 2065:4128]                                                   str
    CPUTEMP  57.1172                                                                  float
    DELAYS   20, 20, 25, 40, 7, 3000, 7, 7, 7, 7                                      str
    DATASECD [2193:4249, 2130:4193]                                                   str
    BIASSECC [2065:2128, 2130:4193]                                                   str
    CCDCFG   default_lbnl_20190717.cfg                                                str
    DATASECC [8:2064, 2130:4193]                                                      str
    BIASSECD [2129:2192, 2130:4193]                                                   str
    PRESECA  [1:7, 2:2065]                                                            str
    OFFSET6  2.0,6.0543                                                               str
    DETSECC  [1:2057, 2065:4128]                                                      str
    DAC13    0.0,-0.0297                                                              str
    DETSECA  [1:2057, 1:2064]                                                         str
    PRRSECC  [8:2064, 4194:4194]                                                      str
    CLOCK12  9.9992,2.9993                                                            str
    CASETEMP 56.8611                                                                  float
    BIASSECB [2129:2192, 2:2065]                                                      str
    OFFSET5  2.0,6.0174                                                               str
    CLOCK7   -2.0001,3.9999                                                           str
    CLOCK8   9.9992,2.9993                                                            str
    CAMERA   z6                                                                       str
    PRESECB  [4250:4256, 2:2065]                                                      str
    TRIMSECB [2193:4249, 2:2065]                                                      str
    DAC17    20.0008,11.9316                                                          str
    DIGITIME 47.5453                                                                  float
    TRIMSECD [2193:4249, 2130:4193]                                                   str
    DAC8     -25.0003,-24.6196                                                        str
    TRIMSECA [8:2064, 2:2065]                                                         str
    CLOCK14  9.9992,2.9993                                                            str
    DAC0     -9.0002,-8.9713                                                          str
    CDSPARMS 400, 400, 8, 2000                                                        str
    DAC1     -9.0002,-8.9507                                                          str
    ORSECC   [8:2064, 2098:2129]                                                      str
    ORSECB   [2193:4249, 2066:2097]                                                   str
    CCDNAME  CCDSM7Z                                                                  str
    OBSID    kp4m20201221t023911                                                      str
    PROCTYPE RAW                                                                      str
    PRODTYPE image                                                                    str
    GAINA    1.387                                                                    float
    SATULEVA 61000.0                                                                  float
    OSTEPA   0.7319095199345611                                                       float
    OMETHA   AVERAGE                                                                  str
    OVERSCNA 1966.054034223049                                                        float
    OBSRDNA  2.176414404248625                                                        float
    SATUELEA 81880.08305453263                                                        float
    GAINB    1.518                                                                    float
    SATULEVB 65535.0                                                                  float
    OSTEPB   0.5937273930649098                                                       float
    OMETHB   AVERAGE                                                                  str
    OVERSCNB 1987.334317960662                                                        float
    OBSRDNB  2.29569819578003                                                         float
    SATUELEB 96465.35650533572                                                        float
    GAINC    1.534                                                                    float
    SATULEVC 40000.0                                                                  float
    OSTEPC   0.9199855706829112                                                       float
    OMETHC   AVERAGE                                                                  str
    OVERSCNC 1980.643479043017                                                        float
    OBSRDNC  2.511180716174036                                                        float
    SATUELEC 58321.69290314802                                                        float
    GAIND    1.554                                                                    float
    SATULEVD 62000.0                                                                  float
    OSTEPD   1.375711494358256                                                        float
    OMETHD   AVERAGE                                                                  str
    OVERSCND 1982.563334159938                                                        float
    OBSRDND  2.417154801423475                                                        float
    SATUELED 93267.09657871546                                                        float
    FIBERMIN 3000                                                                     int
    ENCODING ascii                                                                    str
    CHECKSUM aRITbQHRaQHRaQHR                                                         str     HDU checksum updated 2022-02-14T08:22:46
    DATASUM  3195504281                                                               str     data unit checksum updated 2022-02-14T08:22:46
    ======== ======================================================================== ======= ==============================================


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

We may add an additional HDU with ``EXTNAME=METADATA`` containing a
binary table with one row per standard star giving
the details of which model was used, etc.
This is not yet implemented and details TBD.
