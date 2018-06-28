============================
ql-xwsigma-CAMERA-EXPID.json
============================

:Summary: This QA for QuickLook includes the calculation of the X and W
          sigmas from the 2D image file.
:Naming Convention: ``ql-xwsigma-{ARM}{SPECTROGRAPH}-{EXPID}.json``, where 
        {ARM} is the 1-char arm name (r,b,z), {SPECTROGRAPH} indexes 
        CCDs 0-9 on that arm, and {EXPID} is the 8-digit exposure ID.  
        Together, {ARM}{SPECTROGRAPH} specify a {CAMERA}.
:Regex: ``ql-xwsigma-[brz][0-9]-[0-9]{8}\.json``
:File Type:  JSON


Inputs
======

Written by qa_quicklook.py, with Calc_XWSigma using:

- pix image
- psfboot

Contents
========

========== ================ ==============================================
KEYNAME    Type             Contents
========== ================ ==============================================
XWSIGMA    Py dictionary    sigma calculation at peak sky wavelengths
========== ================ ==============================================



Dictionary Contents
===================

KEYNAME = XWSIGMA

Calculation of standard deviation of Gaussian fit to X and W (i.e. 'wavelength')
profiles at peak sky wavelengths.  


Keyword Description
~~~~~~~~~~~~~~~~~~~

================ ============= =========== ==============================================
KEY              Example Value Type        Comment
================ ============= =========== ==============================================
CAMERA           r5            string      b0-b9, r0-r9, z0-z9
EXPID            00003580      int  	   Exposure ID
FLAVOR           science       string      The type of exposure that can flat, arc or science 
PANAME           PREPROC       string      Name of pipeline algorihm
QATIME           2018-06-26T   float       Timestamp (UTC) of time of QA execution
                 13:27:54.919
NIGHT            20191001      int         The night of observation
PROGRAM          dark          string      name of the observing program: dark, grey, bright
XWSIGMA          [1.09,1.9]    float[2]    fitted XWSIGMA averaged over isolated bright sky wavelengths
XWSIGMA_AMP      [1.106,...]   float[4]    median of XWSIGMAs for all fibers
XWSIGMA_FIB      500,2         float[1000] median of XSIGMAs for all 500 fibers and WSIGMAs for all 500 fibers
XWSIGMA_STATUS   NORMAL        string      Reports the status of XWSIGMA
================ ============= =========== ==============================================

Example JSON Output
~~~~~~~~~~~~~~~~~~~

::

    {
    "CAMERA": "r5",
    "EXPID": "00003580",
    "FLAVOR": "science",
    "METRICS": {
        "XWSIGMA": [
            1.0986244016233697,
            1.9001118868808575
        ],
        "XWSIGMA_AMP": [
            [
                1.1062366602442717,
                1.1162373807512163,
                1.0952786117464997,
                1.0906462756070194
            ],
            [
                1.7523560938850724,
                1.74835570799113,
                1.9925146965558338,
                2.00306365673191
            ]
        ],
        "XWSIGMA_FIB": [
            [
                1.124926622739674,
                1.1081116110538574,
                1.1479864769675756,
                ...,
                1.1215125689970857,
                1.1441888175176285,
                1.113584947805048
            ],
            [
                1.8880446585552835,
                1.9211848900176798,
                1.877931778570274,
                ...,
                1.857695518373094,
                1.934861870199298,
                1.8958319396037648
            ]
        ],
        "XWSIGMA_STATUS": "NORMAL"
    },
    "NIGHT": "20191001",
    "PANAME": "Preproc",
    "PARAMS": {
        "B_PEAKS": [
            3914.4,
            5199.3,
            5578.9
        ],
        "R_PEAKS": [
            6301.9,
            6365.4,
            7318.2,
            7342.8,
            7371.3
        ],
        "XWSIGMA_NORMAL_RANGE": [
            -2.0,
            2.0
        ],
        "XWSIGMA_REF": [
            1.0976699284056959,
            1.8978964735080814
        ],
        "XWSIGMA_WARN_RANGE": [
            -4.0,
            4.0
        ],
        "Z_PEAKS": [
            8401.5,
            8432.4,
            8467.5,
            9479.4
        ]
    },
    "PROGRAM": "dark",
    "QATIME": "2018-06-26T13:27:54.919476"
    }