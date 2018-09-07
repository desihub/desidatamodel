==============================
ql-checkres-CAMERA-EXPID.json
==============================

:Summary: This QA for QuickLook includes the calculation of the average shifts of the fiber trace in x and y direction over all the 500 fibers
:Naming Convention: ``ql-checkres-{ARM}{SPECTROGRAPH}-{EXPID}.json``, where 
        {ARM} is the 1-char arm name (r,b,z), {SPECTROGRAPH} indexes 
        CCDs 0-9 on that arm, and {EXPID} is the 8-digit exposure ID.  
        Together, {ARM}{SPECTROGRAPH} specify a {CAMERA}.
:Regex: ``ql-checkres-[brz][0-9]-[0-9]{8}\.json``
:File Type:  JSON


Inputs
======

Written by qa_quicklook.py, with Check_Resolution using:

- frame
- psf

Contents
========

========== ================ ==================================================
KEYNAME    Type             Contents
========== ================ ==================================================
XYSHIFTS   Py dictionary    average shifts fiber traces in X,Y over 500 fibers 
========== ================ ==================================================



Dictionary Contents
===================

KEYNAME = XYSHIFTS

Averaged shifts of fiber traces in X and Y directions in pixel unit across the CCD 

Keyword Description
~~~~~~~~~~~~~~~~~~~

===================== ============= ========== ============================================================
KEY                   Example Value Type       Comment
===================== ============= ========== ============================================================
CAMERA                r1            string     b0-b9, r0-r9, z0-z9
EXPID                 00003571      int        Exposure ID
FLAVOR                flat          string     The type of exposure that can be flat, arc or science 
PANAME                Flexure       string     Name of pipeline algorihm
QATIME                2018-09-07T   float      Timestamp (UTC) of time of QA execution
                      01:17:34.826
NIGHT                 20191001      int        The night of observation
PROGRAM               arc           string     Name of the observing program: dark, grey, bright 
CHECKARC              [23,18,26]    int[3]     Number of fibers for which the first, second and third Legendre 
                                               polynomial in their best-fit resolution solution are outside 2sigmas from the median of each   
CHECKARC_STATUS       "NORMAL"      string     Reports the status of the CHECKARC
===================== ============= ========== ============================================================

Example JSON Output
~~~~~~~~~~~~~~~~~~~

::

    {
    "CAMERA": "r1",
    "DATA": {
        "LPolyCoef0": [
            [
                1.1546194553375244
            ],
            [
                1.1298854351043701
            ],
            [
                1.1285881996154785
            ],
            [
                1.06905996799469
            ],
            [
                1.1458834409713745
            ],
            [
                1.1604336500167847
            ],
            [
                1.160584568977356
            ],
            [
                1.1441446542739868
            ],
            [
                1.1145886182785034
            ],
            [
                1.1415733098983765
            ],
            [
                1.16229248046875
            ],
            [
                1.1364524364471436
            ],
            [
                1.1153147220611572
            ],
            [
                1.1442683935165405
            ],
            [
                1.118243932723999
            ],
            [
                1.0786961317062378
            ],
            [
                1.1481678485870361
            ],
            [
                1.1409870386123657
            ],
            [
                1.1507529020309448
            ],
            [
                1.1144084930419922
            ],
            [
                1.120363473892212
            ],
            [
                1.1253105401992798
            ],
            [
                1.140156865119934
            ],
            [
                1.155348539352417
            ],
            [
                1.099780797958374
            ],
            [
                1.1433981657028198
            ],
            [
                1.1111900806427002
            ],
            [
                1.1020066738128662
            ],
            [
                1.1268459558486938
            ],...
        ]
    },
    "EXPID": "00003571",
    "FLAVOR": "arc",
    "METRICS": {
        "CHECKARC": [
            23,
            18,
            26
        ],
        "CHECKARC_STATUS": "NORMAL",
        "Medians": [
            1.1275367736816406,
            0.09040199220180511,
            0.0586770698428154
        ],
        "RMS": [
            0.02402067370712757,
            0.04956553503870964,
            0.06509114801883698
        ]
    },
    "NIGHT": "20191001",
    "PANAME": "ResolutionFit",
    "PARAMS": {
        "CHECKARC_NORMAL_RANGE": [
            -50,
            50
        ],
        "CHECKARC_REF": [
            5,
            5,
            5
        ],
        "CHECKARC_WARN_RANGE": [
            -100,
            100
        ]
    },
    "PROGRAM": "ARC",
    "QATIME": "2018-09-07T03:37:08.470691"
    }
            