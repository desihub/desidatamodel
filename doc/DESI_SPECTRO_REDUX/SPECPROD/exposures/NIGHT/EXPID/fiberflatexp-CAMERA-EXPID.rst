==============================
fiberflatexp-CAMERA-EXPID.fits
==============================

:Summary: This file contains the fiberflat to use for a specific exposure such that newflux = rawflux/fiberflat.
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

Mean fiber flat field correction to homogeneize the response among fibers of the same camera, for each wavelength. 2D array of dimension [nspec, nwave]. nspec is the number of fibers per camera. nwave in the length of the wavelength array. The fiber flat field of all fibers share the same wavelength grid (given in HDU WAVELENGTH). This file is valid for a specific exposure as it comprises a correction based on the humidity in the spectrograph enclosure.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords table

   .. rst-class:: keywords

    ======== =========================================================== ======= ====================================================
    KEY      Example Value                                               Type    Comment
    ======== =========================================================== ======= ====================================================
    NAXIS1   2751                                                        int
    NAXIS2   500                                                         int
    EXPID    85159                                                       int     Exposure number
    EXPFRAME 0                                                           int     Frame number
    FLAVOR   science                                                     str     Observation type
    SEQUENCE Spectrographs                                               str     OCS Sequence name
    PURPOSE  Commissioning                                               str     Purpose of observing night
    PROGRAM  CALIB DESI-CALIB-00 LEDs only                               str     Program name
    PROPID   2019B-5000                                                  str     Proposal ID
    OBSERVER DESIObserver                                                str     Names of observers
    LEAD     RunManager                                                  str     Lead observer
    INSTRUME DESI                                                        str     Instrument name
    OBSERVAT KPNO                                                        str     Observatory name
    OBS-LAT  31.96403                                                    str     [deg] Observatory latitude
    OBS-LONG -111.59989                                                  str     [deg] Observatory east longitude
    OBS-ELEV 2097.0                                                      float   [m] Observatory elevation
    TELESCOP KPNO 4.0-m telescope                                        str     Telescope name
    CORRCTOR DESI Corrector                                              str     Corrector Identification
    NIGHT    20210417                                                    int     Observing night
    TIMESYS  UTC                                                         str     Time system used for date-obs
    DATE-OBS 2021-04-18T00:46:10.836154880                               str     [UTC] Observation data and start tim
    TIME-OBS 2021-04-17T00:46:10.836154880                               str     [UTC] Observation start time
    MJD-OBS  59322.03206986                                              float   Modified Julian Date of observation
    ST       07:05:13.310000                                             str     Local Sidereal time at observation start (HH:MM
    EXPTIME  120.025                                                     float   [s] Actual exposure time
    DELTARA  0.0                                                         float   [arcsec] Offset], right ascension, observer inp
    DELTADEC 0.0                                                         float   [arcsec] Offset], declination, observer input
    VCCD     ON                                                          str     True (ON) if CCD voltage is on
    VCCDON   2021-04-09T21:16:55.534496                                  str     Time when CCD voltage was turned on
    VCCDSEC  703932.1                                                    float   [s] CCD on time in seconds
    EQUINOX  2000.0                                                      float   Epoch of observation
    SPECGRPH 5                                                           int     Spectrograph logical name (SP)
    SPECID   9                                                           int     Spectrograph serial number (SM)
    FEEBOX   lbnl072                                                     str     CCD Controller serial number
    VESSEL   27                                                          int     Cryostat serial number
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
    DATASECD [2181:4228, 2114:4161]                                      str     Data section for quadrant D
    AMPSECD  [4096:2049, 4096:2049]                                      str     AMP section for quadrant D
    PRESECD  [4229:4232, 2114:4161]                                      str     Prescan section for quadrant D
    BIASSECC [2053:2116, 2114:4161]                                      str     Bias section for quadrant C
    CCDPREP  purge,clear                                                 str     CCD prep actions
    OFFSET3  -1.5,15.7899                                                str     [V] set value, measured value
    CCDTMING flatdark_sta_timing.txt                                     str     CCD timing file
    CAMERA   b5                                                          str     Camera name
    ORSECC   [5:2052, 2082:2113]                                         str     Row overscan section for quadrant C
    CRYOTEMP 162.97                                                      float   [deg K] Cryostat CCD temperature
    DAC16    0.0,65.2806                                                 str     [V] set value, measured value
    DAC0     15.9998,15.9753                                             str     [V] set value, measured value
    CPUTEMP  55.8867                                                     float   [deg C] CCD controller CPU temperature
    ORSECB   [2181:4228, 2050:2081]                                      str     Row overscan section for quadrant B
    DAC15    19.9997,19.9264                                             str     [V] set value, measured value
    CCDSECC  [1:2048, 2049:4096]                                         str     CCD section for quadrant C
    DAC13    -5.0006,-5.044                                              str     [V] set value, measured value
    CLOCK8   3.0,-7.0002                                                 str     [V] high rail, low rail
    DAC12    4.9997,5.0648                                               str     [V] set value, measured value
    CLOCK16  0.0,0.0                                                     str     [V] high rail, low rail
    CRYOPRES 1.121e-07                                                   str     [mb] Cryostat pressure (IP)
    CCDSECA  [1:2048, 1:2048]                                            str     CCD section for quadrant A
    OFFSET5  -1.100000023841858,-0.0158                                  str     [V] set value, measured value
    PRESECB  [4229:4232, 2:2049]                                         str     Prescan section for quadrant B
    PGAGAIN  5                                                           int     Controller gain
    CCDNAME  CCDSM9B                                                     str     CCD name
    OFFSET2  -1.5,15.8414                                                str     [V] set value, measured value
    BIASSECA [2053:2116, 2:2049]                                         str     Bias section for quadrant A
    PRRSECB  [2181:4228, 1:1]                                            str     Row prescan section for quadrant B
    CLOCK12  3.0,-7.0002                                                 str     [V] high rail, low rail
    BIASSECB [2117:2180, 2:2049]                                         str     Bias section for quadrant B
    DAC6     0.0,0.1473                                                  str     [V] set value, measured value
    PRESECC  [1:4, 2114:4161]                                            str     Prescan section for quadrant C
    TRIMSECD [2181:4228, 2114:4161]                                      str     Trim section for quadrant D
    DETECTOR sn22825                                                     str     Detector (ccd) identification
    CLOCK2   3.9999,-4.0002                                              str     [V] high rail, low rail
    PRRSECC  [5:2052, 4162:4162]                                         str     Row prescan section for quadrant C
    CLOCK6   3.9999,-4.0002                                              str     [V] high rail, low rail
    CCDSIZE  4162,4232                                                   str     CCD size in pixels (rows, columns)
    DATASECB [2181:4228, 2:2049]                                         str     Data section for quadrant B
    DAC17    -0.0,0.0488                                                 str     [V] set value, measured value
    DETSECB  [2049:4096, 1:2048]                                         str     Detector section for quadrant B
    DAC3     15.9998,15.7796                                             str     [V] set value, measured value
    CLOCK15  0.0,0.0                                                     str     [V] high rail, low rail
    DELAYS   13, 13, 25, 25, 8, 3000, 7, 7, 400, 7                       str     [10] Delay settings
    DAC7     0.0,-0.021                                                  str     [V] set value, measured value
    DAC5     0.0,-0.0158                                                 str     [V] set value, measured value
    BIASSECD [2117:2180, 2114:4161]                                      str     Bias section for quadrant D
    CLOCK0   3.9999,-4.0002                                              str     [V] high rail, low rail
    OFFSET1  -1.5,15.9032                                                str     [V] set value, measured value
    CLOCK5   3.9999,-4.0002                                              str     [V] high rail, low rail
    DETSECA  [1:2048, 1:2048]                                            str     Detector section for quadrant A
    CLOCK9   3.0,-7.0002                                                 str     [V] high rail, low rail
    DAC2     15.9998,15.8311                                             str     [V] set value, measured value
    CLOCK10  3.0,-7.0002                                                 str     [V] high rail, low rail
    CLOCK1   3.9999,-4.0002                                              str     [V] high rail, low rail
    AMPSECB  [2049:4096, 2048:1]                                         str     AMP section for quadrant B
    CCDSECB  [2049:4096, 1:2048]                                         str     CCD section for quadrant B
    DATASECC [5:2052, 2114:4161]                                         str     Data section for quadrant C
    PRRSECA  [5:2052, 1:1]                                               str     Row prescan section for quadrant A
    BLDTIME  0.3561                                                      float   [s] Time to build image
    CLOCK7   6.9999,-2.0001                                              str     [V] high rail, low rail
    DAC1     15.9998,15.9032                                             str     [V] set value, measured value
    OFFSET0  -1.5,15.9753                                                str     [V] set value, measured value
    DAC14    0.0,0.7176                                                  str     [V] set value, measured value
    AMPSECA  [1:2048, 1:2048]                                            str     AMP section for quadrant A
    TRIMSECC [5:2052, 2114:4161]                                         str     Trim section for quadrant C
    CLOCK14  3.0,-7.0002                                                 str     [V] high rail, low rail
    DAC9     26.9998,26.5042                                             str     [V] set value, measured value
    OFFSET7  -1.100000023841858,-0.021                                   str     [V] set value, measured value
    CLOCK11  0.0,0.0                                                     str     [V] high rail, low rail
    CCDSECD  [2049:4096, 2049:4096]                                      str     CCD section for quadrant D
    PRESECA  [1:4, 2:2049]                                               str     Prescan section for quadrant A
    DETSECD  [2049:4096, 2049:4096]                                      str     Detector section for quadrant D
    CCDCFG   default_sta_20210128.cfg                                    str     CCD configuration file
    CASETEMP 56.1228                                                     float   [deg C] CCD controller case temperature
    OFFSET4  -1.100000023841858,-0.021                                   str     [V] set value, measured value
    SETTINGS detectors_sm_20210128.json                                  str     Name of DESI CCD settings file
    CLOCK18  3.9999,-4.0002                                              str     [V] high rail, low rail
    CLOCK4   3.9999,-4.0002                                              str     [V] high rail, low rail
    TRIMSECB [2181:4228, 2:2049]                                         str     Trim section for quadrant B
    DAC10    26.9998,26.8752                                             str     [V] set value, measured value
    DAC4     0.0,-0.021                                                  str     [V] set value, measured value
    AMPSECC  [2048:1, 2049:4096]                                         str     AMP section for quadrant C
    TRIMSECA [5:2052, 2:2049]                                            str     Trim section for quadrant A
    ORSECA   [5:2052, 2050:2081]                                         str     Row overscan section for quadrant A
    CLOCK13  3.0,-7.0002                                                 str     [V] high rail, low rail
    CLOCK3   6.9999,-2.0001                                              str     [V] high rail, low rail
    DAC8     26.9998,26.5636                                             str     [V] set value, measured value
    CDSPARMS 400, 400, 8, 1000                                           str     CDS parameters
    ORSECD   [2181:4228, 2082:2113]                                      str     Row bias section for quadrant D
    PRRSECD  [2181:4228, 4162:4162]                                      str     Row prescan section for quadrant D
    DIGITIME 54.796                                                      float   [s] Time to digitize image
    DETSECC  [1:2048, 2049:4096]                                         str     Detector section for quadrant C
    OFFSET6  -1.100000023841858,0.1473                                   str     [V] set value, measured value
    DATASECA [5:2052, 2:2049]                                            str     Data section for quadrant A
    CLOCK17  3.9999,-4.0002                                              str     [V] high rail, low rail
    DAC11    26.9998,26.3262                                             str     [V] set value, measured value
    REQTIME  120.0                                                       float   [s] Requested exposure time
    OBSID    kp4m20210418t004610                                         str     Unique observation identifier
    PROCTYPE RAW                                                         str     Data processing level
    PRODTYPE image                                                       str     Data product type
    CHECKSUM gOZigNXhgNXhgNXh                                            str     HDU checksum updated 2022-02-01T22:58:01
    DATASUM  2197647549                                                  str     data unit checksum updated 2022-02-01T22:58:01
    GAINA    1.118                                                       float   e/ADU (gain applied to image)
    SATULEVA 40000.0                                                     float   saturation or non lin. level, in ADU, inc. bias
    OSTEPA   1.419247027777601                                           float   ADUs (max-min of median overscan per row)
    OMETHA   AVERAGE                                                     str     use average overscan
    OVERSCNA 1183.711435498506                                           float   ADUs (gain not applied)
    OBSRDNA  4.911166252375009                                           float   electrons (gain is applied)
    SATUELEA 43396.61061511267                                           float   saturation or non lin. level, in electrons
    GAINB    1.131                                                       float   e/ADU (gain applied to image)
    SATULEVB 65535.0                                                     float   saturation or non lin. level, in ADU, inc. bias
    OSTEPB   1.440472517977469                                           float   ADUs (max-min of median overscan per row)
    OMETHB   AVERAGE                                                     str     use average overscan
    OVERSCNB 1202.062837406498                                           float   ADUs (gain not applied)
    OBSRDNB  4.116415915196709                                           float   electrons (gain is applied)
    SATUELEB 72760.55193089326                                           float   saturation or non lin. level, in electrons
    GAINC    1.131                                                       float   e/ADU (gain applied to image)
    SATULEVC 65535.0                                                     float   saturation or non lin. level, in ADU, inc. bias
    OSTEPC   1.082835692540357                                           float   ADUs (max-min of median overscan per row)
    OMETHC   AVERAGE                                                     str     use average overscan
    OVERSCNC 1173.422083485057                                           float   ADUs (gain not applied)
    OBSRDNC  3.678954901622545                                           float   electrons (gain is applied)
    SATUELEC 72792.9446235784                                            float   saturation or non lin. level, in electrons
    GAIND    1.136                                                       float   e/ADU (gain applied to image)
    SATULEVD 65535.0                                                     float   saturation or non lin. level, in ADU, inc. bias
    OSTEPD   1.059343783024815                                           float   ADUs (max-min of median overscan per row)
    OMETHD   AVERAGE                                                     str     use average overscan
    OVERSCND 1159.508605985513                                           float   ADUs (gain not applied)
    OBSRDND  3.582411359030031                                           float   electrons (gain is applied)
    SATUELED 73130.55822360046                                           float   saturation or non lin. level, in electrons
    FIBERMIN 2500                                                        int
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
    SEQSTART 2021-04-18T00:46:07.786619                                  str     Start time of sequence processing
    OPENSHUT None                                                        Unknown Time shutter opened
    CAMSHUT  open                                                        str     Shutter status during observation
    WHITESPT T                                                           bool    Telescope is at whitespot
    ZENITH   F                                                           bool    Telescope is at zenith
    SEANNEX  F                                                           bool    Telescope is at SE annex
    BEYONDP  F                                                           bool    Telescope is beyond pole
    FIDUCIAL off                                                         str     Fiducials status during observation
    AIRMASS  1.521266                                                    float   Airmass
    FOCUS    1164.3,-689.6,276.6,13.8,24.3,46.8                          str     Telescope focus settings
    PMREADY  F                                                           bool    Primary mirror ready
    DOMEAZ   106.474                                                     float   [deg] Dome azimuth angle
    DOMINPOS F                                                           bool    Dome is in position
    GUIDOFFR 0.0                                                         float   [arcsec] Cummulative guider offset (RA)
    GUIDOFFD -0.0                                                        float   [arcsec] Cummulative guider offset (dec)
    SUNRA    26.209455                                                   float   [deg] Sun RA at start of exposure
    SUNDEC   10.838587                                                   float   [deg] Sun declination at start of exposure
    MOONDEC  25.292604                                                   float   [deg] Moon declination at start of exposure
    MOONRA   92.637574                                                   float   [deg] Moon RA at start of exposure
    MOONSEP  39.751                                                      float   [deg] Moon Separation
    MOUNTAZ  286.506406                                                  float   [deg] Mount azimuth angle
    MOUNTDEC 31.963427                                                   float   [deg] Mount declination
    MOUNTEL  41.037116                                                   float   [deg] Mount elevation angle
    MOUNTHA  58.478125                                                   float   [deg] Mount hour angle
    INCTRL   F                                                           bool    DESI in control
    INPOS    T                                                           bool    Mount in position
    MNTOFFD  -0.0                                                        float   [arcsec] Mount offset (dec)
    MNTOFFR  -0.0                                                        float   [arcsec] Mount offset (RA)
    PARALLAC 73.493862                                                   float   [deg] Parallactic angle
    SKYDEC   31.963427                                                   float   [deg] Telescope declination (pointing on sky)
    SKYRA    47.828892                                                   float   [deg] Telescope right ascension (pointing on sk
    TARGTDEC 31.963305                                                   float   [deg] Target declination (to TCS)
    TARGTRA  40.026704                                                   float   [deg] Target right ascension (to TCS)
    TARGTAZ  289.066423                                                  float   [deg] Target azimuth
    TARGTEL  34.734309                                                   float   [deg] Target elevation
    TRGTOFFD 0.0                                                         float   [arcsec] Telescope target offset (dec)
    TRGTOFFR 0.0                                                         float   [arcsec] Telescope target offset (RA)
    ZD       48.962884                                                   float   [deg] Telescope zenith distance
    TCSST    07:05:13.684                                                str     Local Sidereal time reported by TCS (HH:MM:SS)
    TCSMJD   59322.032506                                                float   MJD reported by TCS
    ADCCORR  F                                                           bool    Correct pointing for ADC setting if True
    ADC1PHI  149.970058                                                  float   [deg] ADC 1 angle
    ADC2PHI  178.629994                                                  float   [deg] ADC 2 angle
    ADC1HOME F                                                           bool    ADC 1 at home position if True
    ADC2HOME F                                                           bool    ADC 2 at home position if True
    ADC1NREV 1.0                                                         float   ADC 1 number of revs
    ADC2NREV -1.0                                                        float   ADC 2 number of revs
    ADC1STAT STOPPED                                                     str     ADC 1 status
    ADC2STAT STOPPED                                                     str     ADC 2 status
    HEXPOS   1164.3,-689.6,276.6,13.8,24.3,46.8                          str     Hexapod position
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
    FILENAME /exposures/desi/20210417/00085159/desi-00085159.fits.fz     str     Name of (F
    EXCLUDED                                                             str     Components excluded from this exposure
    TCSKRA   0.3 0.003 0.00003                                           str     TCS Kalman (RA)
    TCSKDEC  0.3 0.003 0.00003                                           str     TCS Kalman (dec)
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
    IN_PSF   SPECPROD/exposures/20210417/00085159/psf-b5-00085159.fits   str     Input sp
    IN_IMG   SPECPROD/preproc/20210417/00085159/preproc-b5-00085159.fits str
    ORIG_PSF SPECPROD/calibnight/20210417/psfnight-b5-20210417.fits      str
    CHI2PDF  1.083046058380539                                           float
    EXPTHUM  13.21                                                       float   exposure humidity from telemetry
    EXPFHUM  12.22597485078697                                           float   exposure humidity from flat fit
    CALFHUM  12.95777352360177                                           float   dome flat humidity from flat fit
    CALTHUM  13.3025                                                     float   dome flat humidity from telemetry
    BUNIT                                                                str     adimensional quantity to divide to flatfield a frame
    ======== =========================================================== ======= ====================================================

Data: FITS image [float32, 2751x500]

HDU1
----

EXTNAME = IVAR

Inverse variance (1/sigma^2) of the fiber flat field in HDU0.

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

Mask of the fiberflat; 0=good. See the :doc:`bitmask documentation </bitmasks>` page for the definition of the bits.
Prior to desispec/0.24.0 and software release 18.9, the MASK HDU was compressed.

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

Average flat lamp spectrum of fibers in this camera frame. The fiber flat field is in first approximation the ratio of the measured spectra to this mean spectrum (in practice we use a deconvolved mean spectrum and reconvolve it with the resolution of each fiber). The units are electrons per Angstrom.

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

Wavelength grid in Angstrom used by this fiber flat field. Note that contrary to the science frame, this wavelength array is in the observer frame. In consequence, one has to first convert its wavelength to the solar barycenter frame before using this data to flat field a science exposure. See the frame :ref:`WAVELENGTH documentation <frame-hdu3-wavelength>` for more details.

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

Fibermap with information about the fiber status.

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
