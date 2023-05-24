===============================
biasnighttest-CAMERA-NIGHT.fits
===============================

:Summary: The biasnight code first writes these files and then tests if they
    are better than the default biases.  If they are better,
    they are renamed to the final ``biasnight-*.fits.gz``;
    if they aren't better, they are left behind for comparison
    but not otherwise used by the pipeline.
:Naming Convention: ``biasnighttest-CAMERA-NIGHT.fits.gz``, where ``CAMERA`` is
    *e.g.*, "b0", "r5", etc. and ``NIGHT`` is the observation night in
    YYYYMMDD format.
:Regex: ``biasnighttest-[brz][0-9]-[0-9]{8}\.fits\.gz``
:File Type: FITS, 30 MB

Contents
========

====== ======= ===== ===================
Number EXTNAME Type  Contents
====== ======= ===== ===================
HDU0_  BIAS    IMAGE bias image
====== ======= ===== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = BIAS

2D image with the master bias to subtract to the raw images of the night.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords table

   .. rst-class:: keywords

    ======== ============================================= ===== =======================================
    KEY      Example Value                                 Type  Comment
    ======== ============================================= ===== =======================================
    NAXIS1   4232                                          int
    NAXIS2   4162                                          int
    TELESCOP KPNO 4.0-m telescope                          str   Telescope name
    INSTRUME DESI                                          str   Instrument name
    SPECGRPH 1                                             int   Spectrograph logical name (SP)
    SPECID   10                                            int   Spectrograph serial number (SM)
    DETECTOR sn22822                                       str   Detector (ccd) identification
    CAMERA   b1                                            str   Camera name
    CCDNAME  CCDSM10B                                      str   CCD name
    CCDPREP  purge,clear                                   str   CCD prep actions
    CCDSIZE  4162,4232                                     str   CCD size in pixels (rows, columns)
    CCDTEMP  850.0                                         float [deg C] CCD controller CCD temperature
    CPUTEMP  59.209                                        float [deg C] CCD controller CPU temperature
    CASETEMP 58.9529                                       float [deg C] CCD controller case temperature
    CCDTMING flatdark_sta_timing.txt                       str   CCD timing file
    CCDCFG   CMV_22805_sta_revd_tuned-may2018_20210128.cfg str   CCD configuration fi
    SETTINGS detectors_sm_20210128.json                    str   Name of DESI CCD settings file
    VESSEL   29                                            int   Cryostat serial number
    FEEVER   v20160312                                     str   CCD Controller version
    FEEBOX   lbnl088                                       str   CCD Controller serial number
    PRESECA  [1:4, 2:2049]                                 str   Prescan section for quadrant A
    PRRSECA  [5:2052, 1:1]                                 str   Row prescan section for quadrant A
    DATASECA [5:2052, 2:2049]                              str   Data section for quadrant A
    TRIMSECA [5:2052, 2:2049]                              str   Trim section for quadrant A
    BIASSECA [2053:2116, 2:2049]                           str   Bias section for quadrant A
    ORSECA   [5:2052, 2050:2081]                           str   Row overscan section for quadrant A
    CCDSECA  [1:2048, 1:2048]                              str   CCD section for quadrant A
    DETSECA  [1:2048, 1:2048]                              str   Detector section for quadrant A
    AMPSECA  [1:2048, 1:2048]                              str   AMP section for quadrant A
    PRESECB  [4229:4232, 2:2049]                           str   Prescan section for quadrant B
    PRRSECB  [2181:4228, 1:1]                              str   Row prescan section for quadrant B
    DATASECB [2181:4228, 2:2049]                           str   Data section for quadrant B
    TRIMSECB [2181:4228, 2:2049]                           str   Trim section for quadrant B
    BIASSECB [2117:2180, 2:2049]                           str   Bias section for quadrant B
    ORSECB   [2181:4228, 2050:2081]                        str   Row overscan section for quadrant B
    CCDSECB  [2049:4096, 1:2048]                           str   CCD section for quadrant B
    DETSECB  [2049:4096, 1:2048]                           str   Detector section for quadrant B
    AMPSECB  [2049:4096, 2048:1]                           str   AMP section for quadrant B
    PRESECC  [1:4, 2114:4161]                              str   Prescan section for quadrant C
    PRRSECC  [5:2052, 4162:4162]                           str   Row prescan section for quadrant C
    DATASECC [5:2052, 2114:4161]                           str   Data section for quadrant C
    TRIMSECC [5:2052, 2114:4161]                           str   Trim section for quadrant C
    BIASSECC [2053:2116, 2114:4161]                        str   Bias section for quadrant C
    ORSECC   [5:2052, 2082:2113]                           str   Row overscan section for quadrant C
    CCDSECC  [1:2048, 2049:4096]                           str   CCD section for quadrant C
    DETSECC  [1:2048, 2049:4096]                           str   Detector section for quadrant C
    AMPSECC  [2048:1, 2049:4096]                           str   AMP section for quadrant C
    PRESECD  [4229:4232, 2114:4161]                        str   Prescan section for quadrant D
    PRRSECD  [2181:4228, 4162:4162]                        str   Row prescan section for quadrant D
    DATASECD [2181:4228, 2114:4161]                        str   Data section for quadrant D
    TRIMSECD [2181:4228, 2114:4161]                        str   Trim section for quadrant D
    BIASSECD [2117:2180, 2114:4161]                        str   Bias section for quadrant D
    ORSECD   [2181:4228, 2082:2113]                        str   Row bias section for quadrant D
    CCDSECD  [2049:4096, 2049:4096]                        str   CCD section for quadrant D
    DETSECD  [2049:4096, 2049:4096]                        str   Detector section for quadrant D
    AMPSECD  [4096:2049, 4096:2049]                        str   AMP section for quadrant D
    DAC0     15.9998,15.9547                               str   [V] set value, measured value
    DAC1     15.9998,15.759                                str   [V] set value, measured value
    DAC2     15.9998,15.8105                               str   [V] set value, measured value
    DAC3     15.9998,15.9238                               str   [V] set value, measured value
    DAC4     0.0,-0.0158                                   str   [V] set value, measured value
    DAC5     0.0,-0.021                                    str   [V] set value, measured value
    DAC6     0.0,-0.0158                                   str   [V] set value, measured value
    DAC7     0.0,-0.021                                    str   [V] set value, measured value
    DAC8     26.9998,27.0088                               str   [V] set value, measured value
    DAC9     26.9998,27.0385                               str   [V] set value, measured value
    DAC10    26.9998,27.0978                               str   [V] set value, measured value
    DAC11    26.9998,26.5042                               str   [V] set value, measured value
    DAC12    0.0,5.0752                                    str   [V] set value, measured value
    DAC13    0.0,-5.0232                                   str   [V] set value, measured value
    DAC14    0.0,0.8008                                    str   [V] set value, measured value
    DAC15    19.9997,19.8328                               str   [V] set value, measured value
    DAC16    0.0,0.1386                                    str   [V] set value, measured value
    DAC17    -0.0,0.0732                                   str   [V] set value, measured value
    CLOCK0   3.9999,-4.0002                                str   [V] high rail, low rail
    CLOCK1   3.9999,-4.0002                                str   [V] high rail, low rail
    CLOCK2   3.9999,-4.0002                                str   [V] high rail, low rail
    CLOCK3   6.9999,-2.0001                                str   [V] high rail, low rail
    CLOCK4   3.9999,-4.0002                                str   [V] high rail, low rail
    CLOCK5   3.9999,-4.0002                                str   [V] high rail, low rail
    CLOCK6   3.9999,-4.0002                                str   [V] high rail, low rail
    CLOCK7   6.9999,-2.0001                                str   [V] high rail, low rail
    CLOCK8   3.0,-8.0001                                   str   [V] high rail, low rail
    CLOCK9   3.0,-8.0001                                   str   [V] high rail, low rail
    CLOCK10  3.0,-8.0001                                   str   [V] high rail, low rail
    CLOCK11  0.0,0.0                                       str   [V] high rail, low rail
    CLOCK12  3.0,-8.0001                                   str   [V] high rail, low rail
    CLOCK13  3.0,-8.0001                                   str   [V] high rail, low rail
    CLOCK14  3.0,-8.0001                                   str   [V] high rail, low rail
    CLOCK15  0.0,0.0                                       str   [V] high rail, low rail
    CLOCK16  0.0,0.0                                       str   [V] high rail, low rail
    CLOCK17  3.9999,-4.0002                                str   [V] high rail, low rail
    CLOCK18  3.9999,-4.0002                                str   [V] high rail, low rail
    OFFSET0  -1.5,15.9547                                  str   [V] set value, measured value
    OFFSET1  -1.5,15.7796                                  str   [V] set value, measured value
    OFFSET2  -1.5,15.7899                                  str   [V] set value, measured value
    OFFSET3  -1.5,15.9341                                  str   [V] set value, measured value
    OFFSET4  -1.2599999904632568,-0.0105                   str   [V] set value, measured value
    OFFSET5  -1.309999942779541,-0.0158                    str   [V] set value, measured value
    OFFSET6  -1.5199999809265137,-0.0105                   str   [V] set value, measured value
    OFFSET7  -1.4700000286102295,-0.021                    str   [V] set value, measured value
    DELAYS   13, 13, 25, 25, 8, 3000, 7, 7, 400, 7         str   [10] Delay settings
    CDSPARMS 350, 350, 8, 1000                             str   CDS parameters
    PGAGAIN  5                                             int   Controller gain
    OCSVER   1.2                                           float OCS software version
    DOSVER   trunk                                         str   DOS software version
    CONSTVER DESI:CURRENT                                  str   Constants version
    BUNIT    adu                                           str
    NIGHT    20210407                                      int
    ======== ============================================= ===== =======================================

Data: FITS image [float32, 4232x4162]
