=============================
ql-countpix-CAMERA-EXPID.json
=============================

:Summary: This QA for QuickLook includes the calculation of the number of
        pixels above three thresholds in the 2-D pix file after the preprocessing stage. 
:Naming Convention: ``ql-countpix-{ARM}{SPECTROGRAPH}-{EXPID}.json``, where 
        {ARM} is the 1-char arm name (r,b,z), {SPECTROGRAPH} indexes 
        CCDs 0-9 on that arm, and {EXPID} is the 8-digit exposure ID.  
        Together, {ARM}{SPECTROGRAPH} specify a {CAMERA}.
:Regex: ``ql-countpix-[brz][0-9]-[0-9]{8}\.json``
:File Type:  JSON


Inputs
======

Written by qa_quicklook.py, with Count_Pixels using:

- pix 2D file

Contents
========

========== ================ ================================
KEYNAME    Type             Contents
========== ================ ================================
COUNTPIX   Py dictionary    Number of pixels above threshold
========== ================ ================================



Dictionary Contents
===================

KEYNAME = COUNTPIX

Integral counts of pixels above three thresholds per image and per CCD amp.

Keyword Description
~~~~~~~~~~~~~~~~~~~

================ ============= ========== ==================================================
KEY              Example Value Type       Comment
================ ============= ========== ==================================================
CAMERA           b4            string     b0-9, r0-r9, z0-z9
EXPID            00003900      int  	  Exposure ID
FLAVOR           science       string     The type of exposure that can flat, arc or science 
PANAME           Preproc       string     Name of pipeline algorihm
QATIME           2018-05-27T   float      Timestamp (UTC) of time of QA execution
                 11:33:21.6463
NIGHT            20191017      int        The night of observation
            
PROGRAM          dark          string     name of the observing program: dark, grey, bright
LITFRAC_AMP      [0.35,...]    float[4]   Fraction of the pixels per amp that are above CUTPIX = 5sigmas
LITFRAC_STATUS   NORMAL        string     Reports the status of LITFRAC_AMP
================ ============= ========== ==================================================

Example JSON Output
~~~~~~~~~~~~~~~~~~~

::

    {
    "CAMERA": "b4",
    "EXPID": "00003900",
    "FLAVOR": "science",
    "METRICS": {
        "LITFRAC_AMP": [
            0.35,
            0.34,
            0.4,
            0.37
        ],
        "LITFRAC_STATUS": "NORMAL"
    },
    "NIGHT": "20191017",
    "PANAME": "Preproc",
    "PARAMS": {
        "CUTPIX": 5,
        "LITFRAC_AMP_REF": [
            0.35,
            0.36,
            0.32,
            0.33
        ],
        "LITFRAC_NORMAL_RANGE": [
            -0.1,
            0.1
        ],
        "LITFRAC_WARN_RANGE": [
            -0.2,
            0.2
        ]
    },
    "PROGRAM": "dark",
    "QATIME": "2018-05-27T11:31:44.047383"
    }
