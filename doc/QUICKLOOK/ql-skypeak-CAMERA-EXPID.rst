============================
ql-skypeak-CAMERA-EXPID.json
============================

:Summary: This QA for QuickLook includes the calculation of the counts and RMS 
	  at peak sky wavelengths in a 1D spectrum.
:Naming Convention: ``ql-skypeak-{ARM}{SPECTROGRAPH}-{EXPID}.json``, where 
        {ARM} is the 1-char arm name (r,b,z), {SPECTROGRAPH} indexes 
        CCDs 0-9 on that arm, and {EXPID} is the 8-digit exposure ID.  
        Together, {ARM}{SPECTROGRAPH} specify a {CAMERA}.
:Regex: ``ql-skypeak-[brz][0-9]-[0-9]{8}\.json``
:File Type:  JSON


Inputs
======

Written by qa_quicklook.py, with Sky_Peaks using:

- frame

Contents
========

========== ================ ==============================================
KEYNAME    Type             Contents
========== ================ ==============================================
SKYPEAK    Py dictionary    Counts at wavelengths of peak sky lines
========== ================ ==============================================



Dictionary Contents
===================

KEYNAME = SKYPEAK

Sky level calculations in regions of peak sky emission lines.


Keyword Description
~~~~~~~~~~~~~~~~~~~

================ ================= ========== ==============================================
KEY              Example Value     Type       Comment
================ ================= ========== ==============================================
CAMERA           r5                string     b0-b9, r0-r9, z0-z9
EXPID            00003580          int        Exposure ID
FLAVOR           science           string     The type of exposure that can flat, arc or science 
PANAME           ApplyFiberFlat_QL string     Name of pipeline algorihm
QATIME           2018-06-26T       float      Timestamp (UTC) of time of QA execution
                 13:29:24.3386
NIGHT            20191001          int        The night of observation
PROGRAM          dark              string     name of the observing program: dark, grey, bright 
                 
PEAKCOUNT        91.101398         float      Averaged summed counts for sky fibers over specified peak sky wavelengths
PEAKCOUNT_NOISE  2.75402           float      rms of the summed counts over sky peaks for sky fibers
PEAKCOUNT_FIB    [91.56,...]       float[500] summed counts over sky peaks on ALL the 500 fibers
PEAKCOUNT_STATUS NORMAL            string     
================ ================= ========== ==============================================

Example JSON Output
~~~~~~~~~~~~~~~~~~~

::
    {
    "CAMERA": "r5",
    "EXPID": "00003580",
    "FLAVOR": "science",
    "METRICS": {
        "PEAKCOUNT": 91.10139893832053,
        "PEAKCOUNT_FIB": [
            91.5586785206275,
            92.08538403353383,
            91.82304492364685,
            ...,
            91.55562535769134,
            91.59545990233539,
            91.39342572026013
        ],
        "PEAKCOUNT_NOISE": 2.754024873572926,
        "PEAKCOUNT_STATUS": "NORMAL"
    },
    "NIGHT": "20191001",
    "PANAME": "ApplyFiberFlat_QL",
    "PARAMS": {
        "B_PEAKS": [
            3914.4,
            5199.3,
            5201.8
        ],
        "PEAKCOUNT_NORMAL_RANGE": [
            -1.0,
            1.0
        ],
        "PEAKCOUNT_REF": 91.40821918751547,
        "PEAKCOUNT_WARN_RANGE": [
            -2.0,
            2.0
        ],
        "R_PEAKS": [
            6301.9,
            6365.4,
            7318.2,
            7342.8,
            7371.3
        ],
        "Z_PEAKS": [
            8401.5,
            8432.4,
            8467.5,
            9479.4,
            9505.6,
            9521.8
        ]
    },
    "PROGRAM": "dark",
    "QATIME": "2018-06-26T13:29:24.338629"
    }