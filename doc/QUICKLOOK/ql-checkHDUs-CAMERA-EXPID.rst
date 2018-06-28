==============================
ql-checkHDUs-CAMERA-EXPID.json
==============================

:Summary: This QA for QuickLook includes the calculation of the total
        number of counts on standard star fibers..
:Naming Convention: ``ql-checkHDUs-{ARM}{SPECTROGRAPH}-{EXPID}.json``, where 
        {ARM} is the 1-char arm name (r,b,z), {SPECTROGRAPH} indexes 
        CCDs 0-9 on that arm, and {EXPID} is the 8-digit exposure ID.  
        Together, {ARM}{SPECTROGRAPH} specify a {CAMERA}.
:Regex: ``ql-checkHDUs-[brz][0-9]-[0-9]{8}\.json``
:File Type:  JSON


Inputs
======

Written by qa_quicklook.py, with Check_HDUs using:

- Raw fits file

Contents
========

========== ================ ==============================================
KEYNAME    Type             Contents
========== ================ ==============================================
HDU_STATUS Py dictionary    Matching EXPNUM and CAMERA from the args and the header 
========== ================ ==============================================



Dictionary Contents
====================

KEYNAME = CHECK_HDUs

Integral counts calculations for standard stars, and averaged over image and per AMP.

Keyword Description
~~~~~~~~~~~~~~~~~~~

================ ============= ========== ==============================================
KEY              Example Value Type       Comment
================ ============= ========== ==============================================
CAMERA           b4            string     b0-9, r0-r9, z0-z9
EXPID            00003900      int  	  Exposure ID
FLAVOR           science       string     The type of exposure that can flat, arc or science 
PANAME           Initialize    string     Name of pipeline algorihm
QATIME           2018-05-27T   float      Timestamp (UTC) of time of QA execution
                 11:35:46.0285
NIGHT            20191017      int        The night of observation
PROGRAM          dark          string     name of the observing program: dark, grey, bright
EXPNUM_STATUS    NORMAL        string     Reports the result of a match between exposures number 
                                          in the header and the one given in the argument
HDU_STATUS       NORMAL        string     Reports the result of finding the camera in the header
================ ============= ========== ==============================================

Example JSON Output
~~~~~~~~~~~~~~~~~~~

::

    {
    "CAMERA": "b4",
    "EXPID": "00003900",
    "FLAVOR": "science",
    "METRICS": {
        "EXPNUM_STATUS": "NORMAL",
        "HDU_STATUS": "NORMAL"
    },
    "NIGHT": "20191017",
    "PANAME": "Initialize",
    "PARAMS": {
        "AIRMASS": 1.0,
        "EXPTIME": 1000.0,
        "SEEING": 1.1
    },
    "PROGRAM": "dark",
    "QATIME": "2018-05-27T11:31:29.246245"
    }
