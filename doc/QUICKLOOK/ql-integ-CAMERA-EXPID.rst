============================
ql-integ-CAMERA-EXPID.json
============================

:Summary: This QA for QuickLook includes the calculation of the total
        number of counts on standard star fibers..
:Naming Convention: ``ql-integ-{ARM}{SPECTROGRAPH}-{EXPID}.json``, where 
        {ARM} is the 1-char arm name (r,b,z), {SPECTROGRAPH} indexes 
        CCDs 0-9 on that arm, and {EXPID} is the 8-digit exposure ID.  
        Together, {ARM}{SPECTROGRAPH} specify a {CAMERA}.
:Regex: ``ql-integ-[brz][0-9]-[0-9]{8}\.json``
:File Type:  JSON


Inputs
======

Written by qa_quicklook.py, with Integrate_Spectra using:

- frame

Contents
========

========== ================ ==============================================
KEYNAME    Type             Contents
========== ================ ==============================================
INTEG      Py dictionary    integral counts calculation on star fibers
========== ================ ==============================================



Dictionary Contents
===================

KEYNAME = INTEG

Integral counts calculations for standard stars, and averaged over image and per AMP.

Keyword Description
~~~~~~~~~~~~~~~~~~~

================ ============= ========== ==============================================
KEY              Example Value Type       Comment
================ ============= ========== ==============================================
CAMERA           b4            string     b0-9, r0-r9, z0-z9
EXPID            00003900      int  	  Exposure ID
FLAVOR           science       string     The type of exposure that can flat, arc or science 
PANAME           SkySub_QL     string     Name of pipeline algorihm
QATIME           2018-05-27T   float      Timestamp (UTC) of time of QA execution
                 11:35:46.0285
NIGHT            20191017      int        The night of observation
PROGRAM          dark          string     name of the observing program: dark, grey, bright

FIBER_MAG        [18.22, ...]  float[500] Magnitude of the 500 fibers 
RA               [266.49, ...] floar[500] List of right ascention for all the 500 targets assigned to the fibers in this camera
DEC              [21.97,...]   float[500] List of declinations for all the 500 targets assigned to the fibers in this camera 
STD_FIBERID      [11, 63,...]  int[NS]    List of the fiber IDs assigned to NS standard stars
DELTAMAG         [0.,0.,...]   float[500] List of mag diff b/w the fibermag and the imaging mag from the fibermap
DELTAMAG_TGT     [-2.92,...]   float[N]   List of the average fiber mag for each of N target types in this camera
DELTAMAG_STATUS  ALARM         string     Status of DELTAMAG_TGT
================ ============= ========== ==============================================

Example JSON Output
~~~~~~~~~~~~~~~~~~~

::

    {
    "CAMERA": "b4",
    "EXPID": "00003900",
    "FLAVOR": "science",
    "METRICS": {
        "DEC": [
            21.972282314853857,
            21.9309789573323,
            22.32892764396665,
            22.41375970864624,
            ...,
            21.927311569249582
        ],
        "DELTAMAG": [
            0.0,
            0.0,
            0.0,
            0.0,
            ...,
            0.0,
            0.0
        ],
        "DELTAMAG_STATUS": "ALARM",
        "DELTAMAG_TGT": [
            -2.9209345331080705,
            NaN,
            -0.9617997285914122,
            -4.5797822546440585
        ],
        "FIBER_MAG": [
            18.22211846792697,
            18.294963907355225,
            21.828487269112493
        ],
        "RA": [
            266.4916642633111,
            266.4970976025655,
            266.38371316301436,
            266.389322356526,
            ...,
            266.7211067886968,
            266.68412119940604,
            266.67375510360904,
            266.6948250567388
        ],
        "STD_FIBERID": [
            11,
            61,
            63,
            105,
            186,
            221,
            233,
            289,
            461,
            489,
            494
        ]
    },
    "NIGHT": "20191017",
    "PANAME": "SkySub_QL",
    "PARAMS": {
        "DELTAMAG_NORMAL_RANGE": [
            -0.5,
            0.5
        ],
        "DELTAMAG_TGT_REF": [
            0.0,
            0.0,
            0.0,
            0.0
        ],
        "DELTAMAG_WARN_RANGE": [
            -1.0,
            1.0
        ]
    },
    "PROGRAM": "dark",
    "QATIME": "2018-05-27T11:35:46.028467",
    "QA_STATUS": "UNKNOWN"
    }
