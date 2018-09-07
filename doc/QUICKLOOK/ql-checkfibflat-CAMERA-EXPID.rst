=================================
ql-checkfibflat-CAMERA-EXPID.json
=================================

:Summary: This QA for QuickLook includes the calculation of the average shifts of the fiber trace in x and y direction over all the 500 fibers
:Naming Convention: ``ql-checkfibflat-{ARM}{SPECTROGRAPH}-{EXPID}.json``, where 
        {ARM} is the 1-char arm name (r,b,z), {SPECTROGRAPH} indexes 
        CCDs 0-9 on that arm, and {EXPID} is the 8-digit exposure ID.  
        Together, {ARM}{SPECTROGRAPH} specify a {CAMERA}.
:Regex: ``ql-checkfibflat-[brz][0-9]-[0-9]{8}\.json``
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
CAMERA                r1            string     b0-b9, r0-r9, z0-z9
EXPID                 00003574      int        Exposure ID
FLAVOR                flat          string     The type of exposure that can be flat, arc or science 
PANAME                Flexure       string     Name of pipeline algorihm
QATIME                2018-09-07T   float      Timestamp (UTC) of time of QA execution
                      01:17:34.826
NIGHT                 20191001      int        The night of observation
PROGRAM               flat          string     Name of the observing program: dark, grey, bright 
CHECKFLAT             6684.7        double     The average wavelength in the fiberflat frame
CHECKFLAT_STATUS      "NORMAL"      string     Reports the status of the CHECKFLAT
===================== ============= ========== ============================================================

Example JSON Output
~~~~~~~~~~~~~~~~~~~

::


    {
    "CAMERA": "r1",
    "EXPID": "00003574",
    "FLAVOR": "flat",
    "METRICS": {
        "CHECKFLAT": 6684.799999962981,
        "CHECKFLAT_STATUS": "NORMAL"
    },
    "NIGHT": "20191001",
    "PANAME": "ComputeFiberflat_QL",
    "PARAMS": {
        "CHECKFLAT_NORMAL_RANGE": [
            -0.5,
            0.5
        ],
        "CHECKFLAT_REF": [
            6690.0
        ],
        "CHECKFLAT_WARN_RANGE": [
            -1.0,
            1.0
        ]
    },
    "PROGRAM": "FLAT",
    "QATIME": "2018-09-07T04:27:02.080062"
    }