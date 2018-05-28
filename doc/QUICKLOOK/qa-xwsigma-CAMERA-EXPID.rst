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

================ ============= ========== ==============================================
KEY              Example Value Type       Comment
================ ============= ========== ==============================================
CAMERA           b4            string     b0-b9, r0-r9, z0-z9
EXPID            00003900      int  	  Exposure ID
FLAVOR           science       string     The type of exposure that can flat, arc or science 
PANAME           PREPROC       string     Name of pipeline algorihm
QATIME           2018-05-25T   float      Timestamp (UTC) of time of QA execution
                 09:59:29.102591
NIGHT            20191017      int        The night of observation
            
PARAMS           'XWSIGMA_WARN_RANGE': [-4.0, 4.0]    float[2]  Two representing the lower and upper limts of the warning range
                 'XWSIGMA_NORMAL_RANGE': [-2.0, 2.0]  float[2]  Two floats representing the lower and upper limts of the warning range
                 'XWSIGMA_REF': [0.0, 0.0]            float[2]  Two reference numbers (one for X, one for W direction)
                 'B_PEAKS': [3914.4, 5199.3, 5578.9]  float[3]
                 'R_PEAKS': [6301.9, 6365.4, 7318.2, 7342.8, 7371.3]    float[5]  
                 'Z_PEAKS': [8401.5, 8432.4, 8467.5, 9479.4]            float[4]  
                 
PROGRAM          dark          string     name of the observing program: dark, grey, bright

XWSIGMA		 1.9           float[500] fitted XSIGMA averaged over isolated bright sky wavelengths
XWSIGMA_AMP      1.81          float      median of XSIGMAs for all fibers
XWSIGMA_FIB      1.9           float[4]   median of XSIGMAs for all fibers per amp
XWSIGMA_STATUS   1.9           float[4]   median of XSIGMAs for all fibers per amp

================ ============= ========== ==============================================

Example JSON Output
~~~~~~~~~~~~~~~~~~~

::

{
    "CAMERA": "b4",
    "EXPID": "00003900",
    "FLAVOR": "science",
    "METRICS": {
        "XWSIGMA": [
            1.0962765182946193,
            2.490368288601727
        ],
        "XWSIGMA_AMP": [
            [
                1.0932880388002917,
                1.123310768812173,
                1.1009015445920427,
                1.097427842659204
            ],
            [
                2.76543054582097,
                2.872940343391557,
                2.1728369775096796,
                2.03414610561234
            ]
        ],
        "XWSIGMA_FIB": [
           [500xshifts],[500wshifts]
            
            ]
        ,
        "XWSIGMA_STATUS": "ALARM"
    },
    "NIGHT": "20191017",
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
            0.0,
            0.0
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
    "QATIME": "2018-05-25T09:59:29.102591",
    "QA_STATUS": "UNKNOWN"
}

