===========================
biasnight-CAMERA-NIGHT.fits
===========================

:Summary: Master bias frame for the preprocessing of the night data
:Naming Convention: ``biasnight-CAMERA-NIGHT.fits.gz``, where ``CAMERA`` is
    *e.g.*, "b0", "r5", etc. and ``NIGHT`` is the observation night in
    YYYYMMDD format.
:Regex: ``biasnight-[brz][0-9]-[0-9]{8}\.fits\.gz``
:File Type: FITS, 20 MB

Contents
========

====== ======= ===== ===================
Number EXTNAME Type  Contents
====== ======= ===== ===================
HDU0_  BIAS    IMAGE *Brief Description*
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

    ======== ===================================== ===== =======================================
    KEY      Example Value                         Type  Comment
    ======== ===================================== ===== =======================================
    NAXIS1   4256                                  int
    NAXIS2   4194                                  int
    TELESCOP KPNO 4.0-m telescope                  str   Telescope name
    INSTRUME DESI                                  str   Instrument name
    SPECGRPH 8                                     int   Spectrograph logical name (SP)
    SPECID   2                                     int   Spectrograph serial number (SM)
    DETECTOR M1-42                                 str   Detector (ccd) identification
    CAMERA   z8                                    str   Camera name
    CCDNAME  CCDSM2Z                               str   CCD name
    CCDPREP  purge,clear                           str   CCD prep actions
    CCDSIZE  4194,4256                             str   CCD size in pixels (rows, columns)
    CCDTEMP  -136.0659                             float [deg C] CCD controller CCD temperature
    CPUTEMP  57.3633                               float [deg C] CCD controller CPU temperature
    CASETEMP 57.3533                               float [deg C] CCD controller case temperature
    CCDTMING flatdark_lbnl_timing.txt              str   CCD timing file
    CCDCFG   default_lbnl_20210128.cfg             str   CCD configuration file
    SETTINGS detectors_sm_20210128.json            str   Name of DESI CCD settings file
    VESSEL   9                                     int   Cryostat serial number
    FEEVER   v20160312                             str   CCD Controller version
    FEEBOX   lbnl055                               str   CCD Controller serial number
    PRESECA  [1:7, 2:2065]                         str   Prescan section for quadrant A
    PRRSECA  [8:2064, 1:1]                         str   Row prescan section for quadrant A
    DATASECA [8:2064, 2:2065]                      str   Data section for quadrant A
    TRIMSECA [8:2064, 2:2065]                      str   Trim section for quadrant A
    BIASSECA [2065:2128, 2:2065]                   str   Bias section for quadrant A
    ORSECA   [8:2064, 2066:2097]                   str   Row overscan section for quadrant A
    CCDSECA  [1:2057, 1:2064]                      str   CCD section for quadrant A
    DETSECA  [1:2057, 1:2064]                      str   Detector section for quadrant A
    AMPSECA  [1:2057, 1:2064]                      str   AMP section for quadrant A
    PRESECB  [4250:4256, 2:2065]                   str   Prescan section for quadrant B
    PRRSECB  [2193:4249, 1:1]                      str   Row prescan section for quadrant B
    DATASECB [2193:4249, 2:2065]                   str   Data section for quadrant B
    TRIMSECB [2193:4249, 2:2065]                   str   Trim section for quadrant B
    BIASSECB [2129:2192, 2:2065]                   str   Bias section for quadrant B
    ORSECB   [2193:4249, 2066:2097]                str   Row overscan section for quadrant B
    CCDSECB  [2058:4114, 1:2064]                   str   CCD section for quadrant B
    DETSECB  [2058:4114, 1:2064]                   str   Detector section for quadrant B
    AMPSECB  [4114:2058, 1:2064]                   str   AMP section for quadrant B
    PRESECC  [1:7, 2130:4193]                      str   Prescan section for quadrant C
    PRRSECC  [8:2064, 4194:4194]                   str   Row prescan section for quadrant C
    DATASECC [8:2064, 2130:4193]                   str   Data section for quadrant C
    TRIMSECC [8:2064, 2130:4193]                   str   Trim section for quadrant C
    BIASSECC [2065:2128, 2130:4193]                str   Bias section for quadrant C
    ORSECC   [8:2064, 2098:2129]                   str   Row overscan section for quadrant C
    CCDSECC  [1:2057, 2065:4128]                   str   CCD section for quadrant C
    DETSECC  [1:2057, 2065:4128]                   str   Detector section for quadrant C
    AMPSECC  [1:2057, 4128:2065]                   str   AMP section for quadrant C
    PRESECD  [4250:4256, 2130:4193]                str   Prescan section for quadrant D
    PRRSECD  [2193:4249, 4194:4194]                str   Row prescan section for quadrant D
    DATASECD [2193:4249, 2130:4193]                str   Data section for quadrant D
    TRIMSECD [2193:4249, 2130:4193]                str   Trim section for quadrant D
    BIASSECD [2129:2192, 2130:4193]                str   Bias section for quadrant D
    ORSECD   [2193:4249, 2098:2129]                str   Row bias section for quadrant D
    CCDSECD  [2058:4114, 2065:4128]                str   CCD section for quadrant D
    DETSECD  [2058:4114, 2065:4128]                str   Detector section for quadrant D
    AMPSECD  [4114:2058, 4128:2065]                str   AMP section for quadrant D
    DAC0     -9.0002,-9.0331                       str   [V] set value, measured value
    DAC1     -9.0002,-8.9816                       str   [V] set value, measured value
    DAC2     -9.0002,-8.961                        str   [V] set value, measured value
    DAC3     -9.0002,-8.9816                       str   [V] set value, measured value
    DAC4     5.9998,6.0437                         str   [V] set value, measured value
    DAC5     5.9998,6.0595                         str   [V] set value, measured value
    DAC6     5.9998,5.9964                         str   [V] set value, measured value
    DAC7     5.9998,6.0069                         str   [V] set value, measured value
    DAC8     -25.0003,-25.0796                     str   [V] set value, measured value
    DAC9     -25.0003,-25.3467                     str   [V] set value, measured value
    DAC10    -25.0003,-25.0648                     str   [V] set value, measured value
    DAC11    -25.0003,-25.3467                     str   [V] set value, measured value
    DAC12    0.0,-0.0148                           str   [V] set value, measured value
    DAC13    0.0,-0.0297                           str   [V] set value, measured value
    DAC14    0.0,-0.0297                           str   [V] set value, measured value
    DAC15    0.0,-0.0148                           str   [V] set value, measured value
    DAC16    39.9961,39.4548                       str   [V] set value, measured value
    DAC17    20.0008,12.2854                       str   [V] set value, measured value
    CLOCK0   9.9999,0.0                            str   [V] high rail, low rail
    CLOCK1   9.9999,0.0                            str   [V] high rail, low rail
    CLOCK2   9.9999,0.0                            str   [V] high rail, low rail
    CLOCK3   -2.0001,3.9999                        str   [V] high rail, low rail
    CLOCK4   9.9999,0.0                            str   [V] high rail, low rail
    CLOCK5   9.9999,0.0                            str   [V] high rail, low rail
    CLOCK6   9.9999,0.0                            str   [V] high rail, low rail
    CLOCK7   -2.0001,3.9999                        str   [V] high rail, low rail
    CLOCK8   9.9992,2.9993                         str   [V] high rail, low rail
    CLOCK9   9.9992,2.9993                         str   [V] high rail, low rail
    CLOCK10  9.9992,2.9993                         str   [V] high rail, low rail
    CLOCK11  9.9992,2.9993                         str   [V] high rail, low rail
    CLOCK12  9.9992,2.9993                         str   [V] high rail, low rail
    CLOCK13  9.9992,2.9993                         str   [V] high rail, low rail
    CLOCK14  9.9992,2.9993                         str   [V] high rail, low rail
    CLOCK15  9.9992,2.9993                         str   [V] high rail, low rail
    CLOCK16  9.9999,3.0                            str   [V] high rail, low rail
    CLOCK17  9.0,0.9999                            str   [V] high rail, low rail
    CLOCK18  9.0,0.9999                            str   [V] high rail, low rail
    OFFSET0  0.4000000059604645,-9.0434            str   [V] set value, measured value
    OFFSET1  0.4000000059604645,-8.9816            str   [V] set value, measured value
    OFFSET2  0.4000000059604645,-8.961             str   [V] set value, measured value
    OFFSET3  0.4000000059604645,-8.9713            str   [V] set value, measured value
    OFFSET4  2.0,6.0385                            str   [V] set value, measured value
    OFFSET5  2.0,6.0648                            str   [V] set value, measured value
    OFFSET6  2.0,6.0017                            str   [V] set value, measured value
    OFFSET7  2.0,6.0017                            str   [V] set value, measured value
    DELAYS   20, 20, 25, 40, 7, 3000, 7, 7, 400, 7 str   [10] Delay settings
    CDSPARMS 400, 400, 8, 2000                     str   CDS parameters
    PGAGAIN  3                                     int   Controller gain
    OCSVER   1.2                                   float OCS software version
    DOSVER   trunk                                 str   DOS software version
    CONSTVER DESI:CURRENT                          str   Constants version
    BUNIT    adu                                   str
    NIGHT    20210407                              int
    ======== ===================================== ===== =======================================

Data: FITS image [float32, 4256x4194]


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
