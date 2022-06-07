================================
fiberflatnight-CAMERA-NIGHT.fits
================================

:Summary: Relative fiber-to-fiber variations ("fiberflat") as measured by
    continuum lamp calibration spectra, combined across multiple exposures.
    Corrected flux = original flux / fiberflat.
:Naming Convention: ``fiberflatnight-CAMERA-NIGHT.fits``, where ``CAMERA`` is
    *e.g.*, "b0", "r5", etc. and ``NIGHT`` is the observation night in
    YYYYMMDD format.
:Regex: ``fiberflatnight-[brz][0-9]-[0-9]{8}\.fits``
:File Type: FITS, 10 MB

Contents
========

====== ========== ======== =================================
Number EXTNAME    Type     Contents
====== ========== ======== =================================
HDU0_  FIBERFLAT  IMAGE    Relative fiber-to-fiber variation
HDU1_  IVAR       IMAGE    Inverse variance of fiberflat
HDU2_  MASK       IMAGE    Mask of fiberflat (0=good)
HDU3_  MEANSPEC   IMAGE    Average spectrum
HDU4_  WAVELENGTH IMAGE    Wavelength
HDU5_  FIBERMAP   BINTABLE fibermap
====== ========== ======== =================================


FITS Header Units
=================

HDU0
----

EXTNAME = FIBERFLAT

Relative fiber-to-fiber variation.  Corrected flux = original flux / fiberflat.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords table

    .. rst-class:: keywords

    ======== =========================================================== ======= ====================================================
    KEY      Example Value                                               Type    Comment
    ======== =========================================================== ======= ====================================================
    NAXIS1   2751                                                        int
    NAXIS2   500                                                         int
    EXPID    91342                                                       int     Exposure number
    EXPFRAME 0                                                           int     Frame number
    FLAVOR   science                                                     str     Observation type
    SEQUENCE Spectrographs                                               str     OCS Sequence name
    PURPOSE  Main Survey                                                 str     Purpose of observing night
    PROGRAM  CALIB DESI-CALIB-00 LEDs only                               str     Program name
    PROPID   2020B-5000                                                  str     Proposal ID
    OBSERVER DESIObserver                                                str     Names of observers
    LEAD     RunManager                                                  str     Lead observer
    INSTRUME DESI                                                        str     Instrument name
    OBSERVAT KPNO                                                        str     Observatory name
    OBS-LAT  31.96403                                                    str     [deg] Observatory latitude
    OBS-LONG -111.59989                                                  str     [deg] Observatory east longitude
    OBS-ELEV 2097.0                                                      float   [m] Observatory elevation
    TELESCOP KPNO 4.0-m telescope                                        str     Telescope name
    CORRCTOR DESI Corrector                                              str     Corrector Identification
    NIGHT    20210606                                                    int     Observing night
    TIMESYS  UTC                                                         str     Time system used for date-obs
    DATE-OBS 2021-06-07T00:37:22.927269888                               str     [UTC] Observation data and start tim
    TIME-OBS 2021-06-06T00:37:22.927269888                               str     [UTC] Observation start time
    MJD-OBS  59372.02595981                                              float   Modified Julian Date of observation
    OPENSHUT 2021-06-07T00:37:23.710751                                  str     Time shutter opened
    ST       10:13:31.760000                                             str     Local Sidereal time at observation start (HH:MM
    EXPTIME  120.04                                                      float   [s] Actual exposure time
    DELTARA  0.0                                                         float   [arcsec] Offset], right ascension, observer inp
    DELTADEC 0.0                                                         float   [arcsec] Offset], declination, observer input
    VCCD     ON                                                          str     True (ON) if CCD voltage is on
    VCCDON   2021-05-19T22:18:47.035384                                  str     Time when CCD voltage was turned on
    VCCDSEC  1563696.6                                                   float   [s] CCD on time in seconds
    EQUINOX  2000.0                                                      float   Epoch of observation
    SPECGRPH 0                                                           int     Spectrograph logical name (SP)
    SPECID   4                                                           int     Spectrograph serial number (SM)
    FEEBOX   lbnl081                                                     str     CCD Controller serial number
    VESSEL   15                                                          int     Cryostat serial number
    FEEVER   v20160312                                                   str     CCD Controller version
    FEEPOWER ON                                                          str     FEE power status
    FEEDMASK 2134851391                                                  int     FEE dac mask
    FEECMASK 1048575                                                     int     FEE clk mask
    CCDTEMP  850.0                                                       float   [deg C] CCD controller CCD temperature
    RADESYS  FK5                                                         str     Coordinate reference frame of major/minor axes
    DOSVER   trunk                                                       str     DOS software version
    OCSVER   1.2                                                         float   OCS software version
    CONSTVER DESI:CURRENT                                                str     Constants version
    INIFILE  /data/msdos/dos_home/architectures/kpno/desi.ini            str     DOS Configuration
    CLOCK0   3.9999,-4.0002                                              str     [V] high rail, low rail
    CCDSECD  [2049:4096, 2049:4096]                                      str     CCD section for quadrant D
    CLOCK17  3.9999,-4.0002                                              str     [V] high rail, low rail
    DELAYS   13, 13, 25, 25, 8, 3000, 7, 7, 400, 7                       str     [10] Delay settings
    BIASSECD [2117:2180, 2114:4161]                                      str     Bias section for quadrant D
    DATASECD [2181:4228, 2114:4161]                                      str     Data section for quadrant D
    CLOCK14  3.0,-7.0002                                                 str     [V] high rail, low rail
    PRRSECC  [5:2052, 4162:4162]                                         str     Row prescan section for quadrant C
    CCDSECC  [1:2048, 2049:4096]                                         str     CCD section for quadrant C
    CPUTEMP  56.0097                                                     float   [deg C] CCD controller CPU temperature
    BIASSECA [2053:2116, 2:2049]                                         str     Bias section for quadrant A
    DAC13    -5.0006,-4.9816                                             str     [V] set value, measured value
    OFFSET5  -1.100000023841858,0.0105                                   str     [V] set value, measured value
    DAC0     15.9998,15.965                                              str     [V] set value, measured value
    DAC11    26.9998,26.9049                                             str     [V] set value, measured value
    OFFSET6  -1.100000023841858,0.0158                                   str     [V] set value, measured value
    OFFSET2  -1.5,15.8311                                                str     [V] set value, measured value
    CLOCK15  0.0,0.0                                                     str     [V] high rail, low rail
    TRIMSECB [2181:4228, 2:2049]                                         str     Trim section for quadrant B
    ORSECC   [5:2052, 2082:2113]                                         str     Row overscan section for quadrant C
    BIASSECB [2117:2180, 2:2049]                                         str     Bias section for quadrant B
    OFFSET1  -1.5,15.8208                                                str     [V] set value, measured value
    ORSECA   [5:2052, 2050:2081]                                         str     Row overscan section for quadrant A
    CAMERA   b0                                                          str     Camera name
    CLOCK1   3.9999,-4.0002                                              str     [V] high rail, low rail
    DETSECC  [1:2048, 2049:4096]                                         str     Detector section for quadrant C
    DAC5     0.0,0.0158                                                  str     [V] set value, measured value
    TRIMSECC [5:2052, 2114:4161]                                         str     Trim section for quadrant C
    DAC7     0.0,0.0105                                                  str     [V] set value, measured value
    DAC3     15.9998,15.965                                              str     [V] set value, measured value
    ORSECD   [2181:4228, 2082:2113]                                      str     Row bias section for quadrant D
    CCDSECB  [2049:4096, 1:2048]                                         str     CCD section for quadrant B
    DAC1     15.9998,15.8208                                             str     [V] set value, measured value
    DAC8     26.9998,26.6081                                             str     [V] set value, measured value
    CCDSIZE  4162,4232                                                   str     CCD size in pixels (rows, columns)
    CASETEMP 56.3689                                                     float   [deg C] CCD controller case temperature
    PRESECA  [1:4, 2:2049]                                               str     Prescan section for quadrant A
    CLOCK3   6.9999,-2.0001                                              str     [V] high rail, low rail
    SETTINGS detectors_sm_20210128.json                                  str     Name of DESI CCD settings file
    OFFSET3  -1.5,15.965                                                 str     [V] set value, measured value
    OFFSET0  -1.5,15.965                                                 str     [V] set value, measured value
    DETSECD  [2049:4096, 2049:4096]                                      str     Detector section for quadrant D
    AMPSECB  [2049:4096, 2048:1]                                         str     AMP section for quadrant B
    DATASECA [5:2052, 2:2049]                                            str     Data section for quadrant A
    CLOCK2   3.9999,-4.0002                                              str     [V] high rail, low rail
    BLDTIME  0.3504                                                      float   [s] Time to build image
    CCDNAME  CCDSM4B                                                     str     CCD name
    PRRSECA  [5:2052, 1:1]                                               str     Row prescan section for quadrant A
    DAC14    0.0,0.8216                                                  str     [V] set value, measured value
    CCDCFG   default_sta_20210128.cfg                                    str     CCD configuration file
    PRESECB  [4229:4232, 2:2049]                                         str     Prescan section for quadrant B
    CDSPARMS 400, 400, 8, 1000                                           str     CDS parameters
    CRYOTEMP 162.97                                                      float   [deg K] Cryostat CCD temperature
    CLOCK6   3.9999,-4.0002                                              str     [V] high rail, low rail
    DATASECB [2181:4228, 2:2049]                                         str     Data section for quadrant B
    CLOCK11  0.0,0.0                                                     str     [V] high rail, low rail
    DAC9     26.9998,26.9346                                             str     [V] set value, measured value
    DAC2     15.9998,15.8208                                             str     [V] set value, measured value
    DAC6     0.0,0.0158                                                  str     [V] set value, measured value
    DETSECA  [1:2048, 1:2048]                                            str     Detector section for quadrant A
    CLOCK13  3.0,-7.0002                                                 str     [V] high rail, low rail
    DATASECC [5:2052, 2114:4161]                                         str     Data section for quadrant C
    CLOCK16  0.0,0.0                                                     str     [V] high rail, low rail
    CLOCK9   3.0,-7.0002                                                 str     [V] high rail, low rail
    TRIMSECA [5:2052, 2:2049]                                            str     Trim section for quadrant A
    DAC15    19.9997,20.0616                                             str     [V] set value, measured value
    AMPSECD  [4096:2049, 4096:2049]                                      str     AMP section for quadrant D
    DAC17    -0.0,0.0366                                                 str     [V] set value, measured value
    DETSECB  [2049:4096, 1:2048]                                         str     Detector section for quadrant B
    PRRSECD  [2181:4228, 4162:4162]                                      str     Row prescan section for quadrant D
    PRRSECB  [2181:4228, 1:1]                                            str     Row prescan section for quadrant B
    CLOCK8   3.0,-7.0002                                                 str     [V] high rail, low rail
    OFFSET4  -1.100000023841858,0.0053                                   str     [V] set value, measured value
    AMPSECC  [2048:1, 2049:4096]                                         str     AMP section for quadrant C
    CCDTMING flatdark_sta_timing.txt                                     str     CCD timing file
    TRIMSECD [2181:4228, 2114:4161]                                      str     Trim section for quadrant D
    CCDPREP  purge,clear                                                 str     CCD prep actions
    CLOCK18  3.9999,-4.0002                                              str     [V] high rail, low rail
    PRESECD  [4229:4232, 2114:4161]                                      str     Prescan section for quadrant D
    DAC4     0.0,0.0105                                                  str     [V] set value, measured value
    DAC16    0.0,65.6502                                                 str     [V] set value, measured value
    BIASSECC [2053:2116, 2114:4161]                                      str     Bias section for quadrant C
    ORSECB   [2181:4228, 2050:2081]                                      str     Row overscan section for quadrant B
    CLOCK10  3.0,-7.0002                                                 str     [V] high rail, low rail
    DETECTOR sn22797                                                     str     Detector (ccd) identification
    CLOCK7   6.9999,-2.0001                                              str     [V] high rail, low rail
    DAC10    26.9998,26.8456                                             str     [V] set value, measured value
    CLOCK5   3.9999,-4.0002                                              str     [V] high rail, low rail
    AMPSECA  [1:2048, 1:2048]                                            str     AMP section for quadrant A
    CLOCK12  3.0,-7.0002                                                 str     [V] high rail, low rail
    PRESECC  [1:4, 2114:4161]                                            str     Prescan section for quadrant C
    CRYOPRES 1.002e-07                                                   str     [mb] Cryostat pressure (IP)
    DAC12    4.9997,22.62                                                str     [V] set value, measured value
    OFFSET7  -1.100000023841858,0.0105                                   str     [V] set value, measured value
    CLOCK4   3.9999,-4.0002                                              str     [V] high rail, low rail
    DIGITIME 54.7987                                                     float   [s] Time to digitize image
    PGAGAIN  5                                                           int     Controller gain
    CCDSECA  [1:2048, 1:2048]                                            str     CCD section for quadrant A
    REQTIME  120.0                                                       float   [s] Requested exposure time
    OBSID    kp4m20210607t003722                                         str     Unique observation identifier
    PROCTYPE RAW                                                         str     Data processing level
    PRODTYPE image                                                       str     Data product type
    CHECKSUM 9aCgFaCZ9aCdCaCZ                                            str     HDU checksum updated 2022-02-06T08:13:11
    DATASUM  4268167737                                                  str     data unit checksum updated 2022-02-06T08:13:11
    GAINA    1.133                                                       float   e/ADU (gain applied to image)
    SATULEVA 65535.0                                                     float   saturation or non lin. level, in ADU, inc. bias
    OSTEPA   1.2530904947198                                             float   ADUs (max-min of median overscan per row)
    OMETHA   AVERAGE                                                     str     use average overscan
    OVERSCNA 1209.671055084825                                           float   ADUs (gain not applied)
    OBSRDNA  4.085456675058811                                           float   electrons (gain is applied)
    SATUELEA 72880.5976945889                                            float   saturation or non lin. level, in electrons
    GAINB    1.117                                                       float   e/ADU (gain applied to image)
    SATULEVB 65535.0                                                     float   saturation or non lin. level, in ADU, inc. bias
    OSTEPB   1.01353762880899                                            float   ADUs (max-min of median overscan per row)
    OMETHB   AVERAGE                                                     str     use average overscan
    OVERSCNB 1198.692841450332                                           float   ADUs (gain not applied)
    OBSRDNB  2.953525302217383                                           float   electrons (gain is applied)
    SATUELEB 71863.65509609997                                           float   saturation or non lin. level, in electrons
    GAINC    1.122                                                       float   e/ADU (gain applied to image)
    SATULEVC 65535.0                                                     float   saturation or non lin. level, in ADU, inc. bias
    OSTEPC   1.285695178230526                                           float   ADUs (max-min of median overscan per row)
    OMETHC   AVERAGE                                                     str     use average overscan
    OVERSCNC 1190.789779784249                                           float   ADUs (gain not applied)
    OBSRDNC  3.539433190358737                                           float   electrons (gain is applied)
    SATUELEC 72194.20386708208                                           float   saturation or non lin. level, in electrons
    GAIND    1.122                                                       float   e/ADU (gain applied to image)
    SATULEVD 65535.0                                                     float   saturation or non lin. level, in ADU, inc. bias
    OSTEPD   0.9090212500377675                                          float   ADUs (max-min of median overscan per row)
    OMETHD   AVERAGE                                                     str     use average overscan
    OVERSCND 1181.653571158484                                           float   ADUs (gain not applied)
    OBSRDND  3.286804241230265                                           float   electrons (gain is applied)
    SATUELED 72204.4546931602                                            float   saturation or non lin. level, in electrons
    FIBERMIN 0                                                           int
    LONGSTRN OGIP 1.0                                                    str     The OGIP Long String Convention may be used.
    MODULE   CI                                                          str     Image Sources/Component
    FRAMES   None                                                        Unknown Number of Frames in Archive
    COSMSPLT F                                                           bool    Cosmics split exposure if true
    MAXSPLIT 0                                                           int     Number of allowed exposure splits
    OBSTYPE  FLAT                                                        str     Spectrograph observation type
    MANIFEST F                                                           bool    DOS exposure manifest
    OBJECT                                                               str     Object name
    NTSSURVY na                                                          str     NTS survey name
    SEQID    3 requests                                                  str     Exposure sequence identifier
    SEQNUM   1                                                           int     Number of exposure in sequence
    SEQTOT   3                                                           int     Total number of exposures in sequence
    SEQSTART 2021-06-07T00:37:19.875612                                  str     Start time of sequence processing
    CAMSHUT  open                                                        str     Shutter status during observation
    WHITESPT T                                                           bool    Telescope is at whitespot
    ZENITH   F                                                           bool    Telescope is at zenith
    SEANNEX  F                                                           bool    Telescope is at SE annex
    BEYONDP  F                                                           bool    Telescope is beyond pole
    FIDUCIAL off                                                         str     Fiducials status during observation
    AIRMASS  1.521278                                                    float   Airmass
    FOCUS    1143.6,-727.1,-829.6,5.1,35.1,-0.0                          str     Telescope focus settings
    PMREADY  T                                                           bool    Primary mirror ready
    DOMEAZ   106.784                                                     float   [deg] Dome azimuth angle
    DOMINPOS T                                                           bool    Dome is in position
    GUIDOFFR 0.0                                                         float   [arcsec] Cummulative guider offset (RA)
    GUIDOFFD -0.0                                                        float   [arcsec] Cummulative guider offset (dec)
    SUNRA    75.340488                                                   float   [deg] Sun RA at start of exposure
    SUNDEC   22.752292                                                   float   [deg] Sun declination at start of exposure
    MOONDEC  11.86839                                                    float   [deg] Moon declination at start of exposure
    MOONRA   37.518292                                                   float   [deg] Moon RA at start of exposure
    MOONSEP  56.776                                                      float   [deg] Moon Separation
    MOUNTAZ  286.506397                                                  float   [deg] Mount azimuth angle
    MOUNTDEC 31.963302                                                   float   [deg] Mount declination
    MOUNTEL  41.036698                                                   float   [deg] Mount elevation angle
    MOUNTHA  58.478595                                                   float   [deg] Mount hour angle
    INCTRL   F                                                           bool    DESI in control
    INPOS    T                                                           bool    Mount in position
    MNTOFFD  -0.0                                                        float   [arcsec] Mount offset (dec)
    MNTOFFR  -0.0                                                        float   [arcsec] Mount offset (RA)
    PARALLAC 73.493607                                                   float   [deg] Parallactic angle
    SKYDEC   31.963302                                                   float   [deg] Telescope declination (pointing on sky)
    SKYRA    94.904717                                                   float   [deg] Telescope right ascension (pointing on sk
    TARGTDEC 31.963305                                                   float   [deg] Target declination (to TCS)
    TARGTRA  88.232751                                                   float   [deg] Target right ascension (to TCS)
    TARGTAZ  288.686999                                                  float   [deg] Target azimuth
    TARGTEL  35.641227                                                   float   [deg] Target elevation
    TRGTOFFD 0.0                                                         float   [arcsec] Telescope target offset (dec)
    TRGTOFFR 0.0                                                         float   [arcsec] Telescope target offset (RA)
    ZD       48.963302                                                   float   [deg] Telescope zenith distance
    TCSST    10:13:31.995                                                str     Local Sidereal time reported by TCS (HH:MM:SS)
    TCSMJD   59372.026394                                                float   MJD reported by TCS
    SEEING   None                                                        Unknown [arcsec] ETC/PM seeing
    TRANSPAR None                                                        Unknown ETC/PM transparency
    ADCCORR  F                                                           bool    Correct pointing for ADC setting if True
    ADC1PHI  123.200072                                                  float   [deg] ADC 1 angle
    ADC2PHI  151.330141                                                  float   [deg] ADC 2 angle
    ADC1HOME F                                                           bool    ADC 1 at home position if True
    ADC2HOME F                                                           bool    ADC 2 at home position if True
    ADC1NREV 0.0                                                         float   ADC 1 number of revs
    ADC2NREV -1.0                                                        float   ADC 2 number of revs
    ADC1STAT STOPPED                                                     str     ADC 1 status
    ADC2STAT STOPPED                                                     str     ADC 2 status
    HEXPOS   1143.6,-727.1,-829.6,5.1,35.1,-0.0                          str     Hexapod position
    HEXTRIM  0.0,0.0,0.0,0.0,0.0,0.0                                     str     Hexapod trim values
    ROTOFFST 0.0                                                         float   [arcsec] Rotator offset
    ROTENBLD F                                                           bool    Rotator enabled
    ROTRATE  0.0                                                         float   [arcsec/min] Rotator rate
    RESETROT F                                                           bool    DOS Control: reset hex rotator
    GUIDMODE catalog                                                     str     Guider mode
    SPCGRPHS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                     str     Participating spectrograph
    ILLSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                     str     Participating illuminate s
    CCDSPECS SP0,SP1,SP2,SP3,SP4,SP5,SP6,SP7,SP8,SP9                     str     Participating ccd spectrog
    UPSSTAT  SUCCESS                                                     str     UPS Status
    FILENAME /exposures/desi/20210606/00091342/desi-00091342.fits.fz     str     Name of (F
    EXCLUDED                                                             str     Components excluded from this exposure
    TCSKRA   1.5 0 0                                                     str     TCS Kalman (RA)
    TCSKDEC  1.5 0 0                                                     str     TCS Kalman (dec)
    TCSGRA   0.3                                                         float   TCS simple gain (RA)
    TCSGDEC  0.3                                                         float   TCS simple gain (dec)
    TCSMFRA  1                                                           int     TCS moving filter length (RA)
    TCSMFDEC 1                                                           int     TCS moving filter length (dec)
    TCSPIRA  1.0,0.0,0.0,0.0                                             str     TCS PI settings (P, I (gain, error window, satu
    TCSPIDEC 1.0,0.0,0.0,0.0                                             str     TCS PI settings (P, I (gain, error window, satu
    NSPEC    500                                                         int     Number of spectra
    WAVEMIN  3600.0                                                      float   First wavelength [Angstroms]
    WAVEMAX  5800.0                                                      float   Last wavelength [Angstroms]
    WAVESTEP 0.8                                                         float   Wavelength step size [Angstroms]
    SPECTER  0.10.0                                                      str     https://github.com/desihub/specter
    IN_PSF   SPECPROD/exposures/20210606/00091342/psf-b0-00091342.fits   str     Input sp
    IN_IMG   SPECPROD/preproc/20210606/00091342/preproc-b0-00091342.fits str
    ORIG_PSF SPECPROD/calibnight/20210606/psfnight-b0-20210606.fits      str
    CHI2PDF  1.102403823484989                                           float
    BUNIT                                                                str     adimensional quantity to divide to flatfield a frame
    ======== =========================================================== ======= ====================================================

Data: FITS image [float32, 2751x500]

HDU1
----

EXTNAME = IVAR

Inverse variance of fiberflat.

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
    CHECKSUM 75OIA2LF92LFA2LF str  HDU checksum updated 2021-07-07T19:21:58
    DATASUM  2784291411       str  data unit checksum updated 2021-07-07T19:21:58
    ======== ================ ==== ==============================================

Data: FITS image [float32, 2751x500]

HDU2
----

EXTNAME = MASK

Mask of fiberflat (0=good).

Prior to desispec/0.24.0 and software release 18.9, the MASK HDU was compressed.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords table

   .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2751             int  Number of wavelengths
    NAXIS2   500              int  Number of spectra (number of rows)
    BSCALE   1                int
    BZERO    2147483648       int
    CHECKSUM TDeFWDbFTDbFTDbF str  HDU checksum updated 2021-07-07T19:21:58
    DATASUM  687822           str  data unit checksum updated 2021-07-07T19:21:58
    ======== ================ ==== ==============================================

Data: FITS image [int32, 2751x500]

HDU3
----

EXTNAME = MEANSPEC

Average continuum lamp spectrum.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords table

   .. rst-class:: keywords

    ======== ================= ==== ==============================================
    KEY      Example Value     Type Comment
    ======== ================= ==== ==============================================
    NAXIS1   2751              int  Number of wavelengths
    BUNIT    electron/Angstrom str
    CHECKSUM nXJGnXGFnXGFnXGF  str  HDU checksum updated 2021-07-07T19:21:58
    DATASUM  2097385325        str  data unit checksum updated 2021-07-07T19:21:58
    ======== ================= ==== ==============================================

Data: FITS image [float32, 2751]

HDU4
----

EXTNAME = WAVELENGTH

Wavelengths in Angstroms at which the fiberflat is measured.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords table

   .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   2751             int  Number of wavelengths
    BUNIT    Angstrom         str
    CHECKSUM 4nG56kG34kG34kG3 str  HDU checksum updated 2021-07-07T19:21:58
    DATASUM  2458411755       str  data unit checksum updated 2021-07-07T19:21:58
    ======== ================ ==== ==============================================

Data: FITS image [float32, 2751]

HDU5
----

EXTNAME = FIBERMAP

The fibermap HDU copied from other files.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords table

   .. rst-class:: keywords

    ======== ================ ==== ==============================================
    KEY      Example Value    Type Comment
    ======== ================ ==== ==============================================
    NAXIS1   373              int  length of dimension 1
    NAXIS2   500              int  length of dimension 2
    ENCODING ascii            str
    CHECKSUM 2imG4ZkE2fkE2ZkE str  HDU checksum updated 2021-07-07T19:21:58
    DATASUM  508954227        str  data unit checksum updated 2021-07-07T19:21:58
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
FIBER                 int32
LOCATION              int64
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

Corrected flux = original flux / fiberflat.

.. code::

  fiberflat = desispec.fiberflat.compute_fiberflat(flatframe)
  desispec.fiberflat.apply_fiberflat(scienceframe, fiberflat)
