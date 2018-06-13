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
CAMERA           b4                string     b0-b9, r0-r9, z0-z9
EXPID            00003900          int  	  Exposure ID
FLAVOR           science           string     The type of exposure that can flat, arc or science 
PANAME           ApplyFiberFlat_QL string     Name of pipeline algorihm
QATIME           2018-05-27T       float      Timestamp (UTC) of time of QA execution
                 11:33:21.646
NIGHT            20191017          int        The night of observation
PROGRAM          dark              string     name of the observing program: dark, grey, bright 
                 
SUMCOUNT         1500.0            float[500] summed counts over specified peak sky wavelengths
SUMCOUNT_RMS     1445.0            float      rms of summed counts over sky peaks
SUMCOUNT_RMS_SKY 1455.0            float      rms of summed counts over sky peaks on sky fibers
SUMCOUNT_RMS_AMP 1444.0            float[4]   rms of summed counts on sky fibers per AMP
================ ================= ========== ==============================================

Example JSON Output
~~~~~~~~~~~~~~~~~~~

::

    {
    "CAMERA": "b4",
    "EXPID": "00003900",
    "FLAVOR": "science",
    "METRICS": {
        "PEAKCOUNT": [
            4.282293116542009,
            4.0728734401088325,
            4.193777093245643,...
            4.480814131904552,
            4.087671032323141,
            4.044146000897669,
            3.998570825525542
        ],
        "PEAKCOUNT_MED_SKY": [],
        "PEAKCOUNT_NOISE": 0.07211437189013367,
        "PEAKCOUNT_STATUS": "ALARM"
    },
    "NIGHT": "20191017",
    "PANAME": "ApplyFiberFlat_QL",
    "PARAMS": {
        "B_PEAKS": [
            3914.4,
            5199.3,
            5201.8
        ],
        "PEAKCOUNT_NORMAL_RANGE": [
            1000.0,
            20000.0
        ],
        "PEAKCOUNT_REF": [
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,...
            0.0,
            0.0,
            0.0,
            0.0
        ],
        "PEAKCOUNT_WARN_RANGE": [
            500.0,
            40000.0
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
    "QATIME": "2018-05-27T11:33:22.465071",
    "QA_STATUS": "UNKNOWN"
    }
