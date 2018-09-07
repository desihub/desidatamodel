==============================
ql-trace-CAMERA-EXPID.json
==============================

:Summary: This QA for QuickLook includes the calculation of the average shifts of the fiber trace in x and y direction over all the 500 fibers
:Naming Convention: ``ql-trace-{ARM}{SPECTROGRAPH}-{EXPID}.json``, where 
        {ARM} is the 1-char arm name (r,b,z), {SPECTROGRAPH} indexes 
        CCDs 0-9 on that arm, and {EXPID} is the 8-digit exposure ID.  
        Together, {ARM}{SPECTROGRAPH} specify a {CAMERA}.
:Regex: ``ql-trace-[brz][0-9]-[0-9]{8}\.json``
:File Type:  JSON


Inputs
======

Written by qa_quicklook.py, with Flexure using:

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
CAMERA                b5            string     b0-b9, r0-r9, z0-z9
EXPID                 00003574      int        Exposure ID
FLAVOR                flat          string     The type of exposure that can be flat, arc or science 
PANAME                Flexure       string     Name of pipeline algorihm
QATIME                2018-09-07T   float      Timestamp (UTC) of time of QA execution
                      01:17:34.826
NIGHT                 20191001      int        The night of observation
PROGRAM               flat          string     name of the observing program: dark, grey, bright 
XYSHIFTS              []            double[2]  List of two averaged values (in pixel unit) for the fiber traces in X,Y directions
XYSHIFTS_STATUS       "ALARM"       string     Reports the status of the XYSHIFTS
===================== ============= ========== ============================================================

Example JSON Output
~~~~~~~~~~~~~~~~~~~

::

    {
    "CAMERA": "b5",
    "EXPID": "00003574",
    "FLAVOR": "flat",
    "METRICS": {
        "XYSHIFTS": [],
        "XYSHIFTS_STATUS": "ALARM"
    },
    "NIGHT": "20191001",
    "PANAME": "Flexure",
    "PARAMS": {
        "XYSHIFTS_NORMAL_RANGE": [
            -1.0,
            1.0
        ],
        "XYSHIFTS_REF": [
            0.0,
            0.0
        ],
        "XYSHIFTS_WARN_RANGE": [
            -2.0,
            2.0
        ]
    },
    "PROGRAM": "flat",
    "QATIME": "2018-09-07T01:17:34.825999"
    }