============================
ql-getbias-CAMERA-EXPID.json    
============================

:Summary: This QA for QuickLook includes the calculation of the bias
	  in the CCD overscan region.
:Naming Convention: ``ql-getbias-{ARM}{SPECTROGRAPH}-{EXPID}.json``, where 
        {ARM} is the 1-char arm name (r,b,z), {SPECTROGRAPH} indexes 
        CCDs 0-9 on that arm, and {EXPID} is the 8-digit exposure ID.  
        Together, {ARM}{SPECTROGRAPH} specify a {CAMERA}.
:Regex: ``ql-getbias-[brz][0-9]-[0-9]{8}\.json``
:File Type:  JSON


Inputs
======

Written by qa_quicklook.py, with Bias_From_Overscan using:

- pix 2D file

Contents
========

========== ================ =====================================
KEYNAME    Type             Contents
========== ================ =====================================
GETBIAS    Py dictionary    bias calculated from overscan region
========== ================ =====================================



Dictionary Contents
===================

KEYNAME = GETBIAS

Bias calculations per image and per CCD amp.

Keyword Description
~~~~~~~~~~~~~~~~~~~

================ ============= ========== ==============================================
KEY              Example Value Type       Comment
================ ============= ========== ==============================================
CAMERA           b4            string     b0-b9, r0-r9, z0-z9
EXPID            00003900      int  	  Exposure ID
FLAVOR           science       string     The type of exposure that can flat, arc or science 
PANAME           PREPROC       string     Name of pipeline algorihm
QATIME           2018-05-27T   float      Timestamp (UTC) of time of QA execution
                 11:31:43.342
NIGHT            20191017      int        The night of observation            
PROGRAM          dark          string     name of the observing program: dark, grey, bright

BIAS             147.041,      float      value of bias across image
BIAS_AMP         [166.859, 150.606, 155.208, 115.488]        float[4]   value of bias averaged over each amplifier
BIAS_STATUS      ALARM         string     status of BIAS_AMP 
================ ============= ========== ==============================================

Example JSON Output
~~~~~~~~~~~~~~~~~~~

::
{
    "CAMERA": "b4",
    "EXPID": "00003900",
    "EXPTIME": 1000.0,
    "FLAVOR": "science",
    "METRICS": {
        "BIAS": 147.04058349609375,
        "BIAS_AMP": [
            166.859375,
            150.6064453125,
            155.20818359375,
            115.488330078125
        ],
        "BIAS_STATUS": "ALARM"
    },
    "NIGHT": "20191017",
    "PANAME": "Preproc",
    "PARAMS": {
        "BIAS_AMP_REF": [
            0.0,
            0.0,
            0.0,
            0.0
        ],
        "BIAS_NORMAL_RANGE": [
            -1.0,
            1.0
        ],
        "BIAS_WARN_RANGE": [
            -2.0,
            2.0
        ],
        "FITS_DESISPEC_VERSION": "0.21.0.dev2590",
        "PROC_DESISPEC_VERSION": "0.21.0.dev2590",
        "PROC_QuickLook_VERSION": "05.18.0"
    },
    "PROGRAM": "dark",
    "QATIME": "2018-05-27T11:31:42.766594",
    "QA_STATUS": "UNKNOWN"
}

