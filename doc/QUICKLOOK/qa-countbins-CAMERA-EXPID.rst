==============================
ql-countbins-CAMERA-EXPID.json
==============================

:Summary: This QA for QuickLook includes the calculation of the number
	  of spectral bins above threshold.
:Naming Convention: ``ql-countbins-{ARM}{SPECTROGRAPH}-{EXPID}.json``, where 
        {ARM} is the 1-char arm name (r,b,z), {SPECTROGRAPH} indexes 
        CCDs 0-9 on that arm, and {EXPID} is the 8-digit exposure ID.  
        Together, {ARM}{SPECTROGRAPH} specify a {CAMERA}.
:Regex: ``ql-countbins-[brz][0-9]-[0-9]{8}\.json``
:File Type:  JSON


Inputs
======

Written by qa_quicklook.py, with CountSpectralBins using:

- frame
- psfboot

Contents
========

========== ================ ===========================================
KEYNAME    Type             Contents
========== ================ ===========================================
COUNTBINS  Py dictionary    Number of bins per spectrum above threshold
========== ================ ===========================================



Dictionary Contents
===================

KEYNAME = COUNTBINS

Calculation of number of bins above a threshold per spectrum.

Keyword Description
~~~~~~~~~~~~~~~~~~~

================ ============= ========== ============================================================
KEY              Example Value Type       Comment
================ ============= ========== ============================================================
CAMERA           b4            string     b0-b9, r0-r9, z0-z9
EXPID            00003900      int  	  Exposure ID
FLAVOR           science       string     The type of exposure that can flat, arc or science 
PANAME           BoxcarExtract string     Name of pipeline algorihm
QATIME           2018-05-27T   float      Timestamp (UTC) of time of QA execution
                 11:33:21.646358
NIGHT            20191017      int        The night of observation
PROGRAM          dark          string     name of the observing program: dark, grey, bright 

NGOODFIB         500            int        number of fibers with a nonzero number of bins above highest threshold 
N_KNOWN_BROKEN_FIBERS 0         int        number od known broken fibers
NGOODFIB_STATUS "ALARM"         string   
================ ============= ========== ============================================================

Example JSON Output
~~~~~~~~~~~~~~~~~~~

::

{
    "CAMERA": "b4",
    "EXPID": "00003900",
    "FLAVOR": "science",
    "METRICS": {
        "GOOD_FIBER": [500
        ]        
        "NGOODFIB": 500,
        "NGOODFIB_STATUS": "ALARM"
    },
    "NIGHT": "20191017",
    "PANAME": "BoxcarExtract",
    "PARAMS": {
        "CUTBINS": 5,
        "NGOODFIB_NORMAL_RANGE": [
            -1,
            1
        ],
        "NGOODFIB_REF": 0,
        "NGOODFIB_WARN_RANGE": [
            -2,
            2
        ],
        "N_KNOWN_BROKEN_FIBERS": 0
    },
    "PROGRAM": "dark",
    "QATIME": "2018-05-27T11:33:21.646358",
    "QA_STATUS": "UNKNOWN"
}
