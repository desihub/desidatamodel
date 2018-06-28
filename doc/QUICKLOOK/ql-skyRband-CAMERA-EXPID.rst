============================
ql-skycont-CAMERA-EXPID.json
============================

:Summary: This QA for QuickLook includes the calculation of the sky
	  continuum level in sky fibers.
:Naming Convention: ``ql-skycont-{ARM}{SPECTROGRAPH}-{EXPID}.json``, where 
        {ARM} is the 1-char arm name (r,b,z), {SPECTROGRAPH} indexes 
        CCDs 0-9 on that arm, and {EXPID} is the 8-digit exposure ID.  
        Together, {ARM}{SPECTROGRAPH} specify a {CAMERA}.
:Regex: ``ql-skycont-[brz][0-9]-[0-9]{8}\.json``
:File Type:  JSON


Inputs
======

Written by qa_quicklook.py, with Sky_Continuum using:

- frame

Contents
========

========== ================ ==============================================
KEYNAME    Type             Contents
========== ================ ==============================================
SKYCONT    Py dictionary    continuum level calculation on sky fibers
========== ================ ==============================================



Dictionary Contents
===================

KEYNAME = SKYCONT

Sky level calculations in continuum regions averaged over sky fibers, and per CCD amp.


Keyword Description
~~~~~~~~~~~~~~~~~~~

================ ================= ========== ==============================================
KEY              Example Value     Type       Comment
================ ================= ========== ==============================================
CAMERA           r5                string     b0-b9, r0-r9, z0-z9
EXPID            00003580          int        Exposure ID
FLAVOR           science           string     The type of exposure that can flat, arc or science 
PANAME           SkySub_QL         string     Name of pipeline algorihm
QATIME           2018-06-26T       float      Timestamp (UTC) of time of QA execution
                 13:30:59.33
NIGHT            20191001          int        The night of observation
PROGRAM          dark              string     Name of the observing program: dark, grey, bright 
                 06:05:34.555
SKYRBAND         100               float
SKY_FIB_RBAND    [64.109,...]      float[N]   sky fiber magnitudes in camera r [if the camera is not r, this is equal to the value of the SKYRBAND]
SKY_RFLUX_DIFF   31.744744042      float      Averaged difference between flux from sky monitor and the calculated magnitude from the sky fibers
SKYRBAND_STATUS  ALARM             string     Reports the status of the SKYRBAND 
================ ================= ========== ==============================================

Example JSON Output
~~~~~~~~~~~~~~~~~~~

::

    {
    "CAMERA": "r5",
    "EXPID": "00003580",
    "FLAVOR": "science",
    "METRICS": {
        "SKYRBAND": 100,
        "SKYRBAND_STATUS": "ALARM",
        "SKY_FIB_RBAND": [
            64.10902850525247,
            47.19984127221782,
            33.71937202880539,
            21.305337648086788,
            54.728441675605175,
            26.29630286147452,
            301.03653687572336,
            116.52752469676646,
            28.327416830460482,
            84.05590386404947,
            27.959516225440034,
            42.66742376597998,
            51.99917719294775,
            87.9449520047327,
            36.51377573241133,
            85.32478390471992,
            46.08670585163529,
            27.82588052471271,
            6.129358372836027,
            33.86565967964211,
            149.71209670926157,
            77.64065564544616,
            83.51049544767781,
            51.87332161680941,
            70.89269700910947,
            25.162782600114745,
            41.1894316913002,
            253.32126724576884,
            200.25134201834766,
            131.2515322436119,
            12.465323441830302,
            25.96324312444476,
            62.42378339818336,
            20.087256043546077,
            37.111661964920785,
            36.46195333646981,
            51.78189746157241,
            38.976045855080464
        ],
        "SKY_RFLUX_DIFF": 31.74474404297382
    },
    "NIGHT": "20191001",
    "PANAME": "SkySub_QL",
    "PARAMS": {
        "B_CONT": [
            "4000, 4500",
            "5250, 5550"
        ],
        "R_CONT": [
            "5950, 6200",
            "6990, 7230"
        ],
        "SKYRBAND_NORMAL_RANGE": [
            -1.0,
            1.0
        ],
        "SKYRBAND_REF": 0,
        "SKYRBAND_WARN_RANGE": [
            -2.0,
            2.0
        ],
        "Z_CONT": [
            "8120, 8270",
            "9110, 9280"
        ]
    },
    "PROGRAM": "dark",
    "QATIME": "2018-06-26T13:30:59.330035"
    }