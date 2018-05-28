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
CAMERA           b4                string     b0-b9, r0-r9, z0-z9
EXPID            00003900          int  	  Exposure ID
FLAVOR           science           string     The type of exposure that can flat, arc or science 
PANAME           ApplyFiberFlat_QL string     Name of pipeline algorihm
QATIME           2018-05-27T       float      Timestamp (UTC) of time of QA execution
                 11:33:21.646
NIGHT            20191017          int        The night of observation
PROGRAM          dark              string     Name of the observing program: dark, grey, bright 
                 06:05:34.555
SKYCONT          210.0             float      Sky continuum in all configured continuum areas averaged over all sky fibers
SKYCONT_FIBER    357.238           float[N]   Sky continuum per sky fiber averaged over two continuum regions, 'N' is number of sky fibers
SKYFIBERID       4                 int[N]     FIBERID of sky fibers 
Sky_Rband        1000              float
Sky_fib_Rband    1000              float      Average sky fiber magnitude in camera r [if the camera is not r, this is equal to the value of the Sky_Rband]
Sky_Rflux_diff   []                float[N]   Difference between flux from sky monitor and the calculated magnitude from the sky fibers
SKYCONT_STATUS   NORMAL            string     Reports the status of the SKYCONT 
================ ================= ========== ==============================================

Example JSON Output
~~~~~~~~~~~~~~~~~~~

::

    {
    "CAMERA": "b4",
    "EXPID": "00003900",
    "FLAVOR": "science",
    "METRICS": {
        "SKYCONT": 157.25023111654713,
        "SKYCONT_FIBER": [
            157.49714226354033,
            157.33003323141287,
            157.27465437573582,
            157.39663945409848,
            157.6130890672511,
            156.12769928310098,
            158.0197827372052,
            156.2474524068964,
            156.726057886396,
            158.11654104258815,
            158.0413167773663,
            157.3799225729967,
            159.92146935310254,
            157.63296481766565,
            157.62250031884912,
            156.78986070531354,
            155.76293239911928,
            157.5245717555618,
            157.86206419445745,
            157.027038924728,
            157.88516749561518,
            156.54035165563843,
            156.51811647812065,
            157.66591061489737,
            157.06034148582262,
            157.20363838986205,
            156.42290620012565,
            156.34416171954973,
            157.51649798212142,
            158.02825941322772,
            157.4296416561391,
            156.10146985139625,
            157.57032390832507,
            155.84241824728042,
            157.11836495563233,
            157.7336712013439,
            157.36357648976076
        ],
        "SKYCONT_STATUS": "NORMAL",
        "SKYFIBERID": [
            10,
            21,
            68,
            123,
            146,
            153,
            162,
            177,
            184,
            187,
            224,
            230,
            234,
            247,
            251,
            260,
            278,
            279,
            283,
            300,
            313,
            324,
            334,
            339,
            352,
            376,
            395,
            404,
            406,
            414,
            416,
            417,
            427,
            472,
            495,
            498,
            499
        ],
        "Sky_Rband": 1000,
        "Sky_Rflux_diff": 1000,
        "Sky_fib_Rband": []
    },
    "NIGHT": "20191017",
    "PANAME": "ApplyFiberFlat_QL",
    "PARAMS": {
        "B_CONT": [
            "4000, 4500",
            "5250, 5550"
        ],
        "R_CONT": [
            "5950, 6200",
            "6990, 7230"
        ],
        "SKYCONT_NORMAL_RANGE": [
            100.0,
            400.0
        ],
        "SKYCONT_REF": 0,
        "SKYCONT_WARN_RANGE": [
            50.0,
            600.0
        ],
        "Z_CONT": [
            "8120, 8270",
            "9110, 9280"
        ]
    },
    "PROGRAM": "dark",
    "QATIME": "2018-05-27T11:33:22.157139",
    "QA_STATUS": "UNKNOWN"
}
