=============================
ql-skyresid-CAMERA-EXPID.json
=============================

:Summary: This QA for QuickLook includes the calculation of the sky
	  continuum level in sky fibers.
:Naming Convention: ``ql-skyresid-{ARM}{SPECTROGRAPH}-{EXPID}.json``, where 
        {ARM} is the 1-char arm name (r,b,z), {SPECTROGRAPH} indexes 
        CCDs 0-9 on that arm, and {EXPID} is the 8-digit exposure ID.  
        Together, {ARM}{SPECTROGRAPH} specify a {CAMERA}.
:Regex: ``ql-skyresid-[brz][0-9]-[0-9]{8}\.json``
:File Type:  JSON


Inputs
======

Written by qa_quicklook.py, with Sky_Residual using:

- frame, sky model

Contents
========

========== ================ ==============================================
KEYNAME    Type             Contents
========== ================ ==============================================
SKYRESID   Py dictionary    Residuals calculation on sky fibers
========== ================ ==============================================



Dictionary Contents
===================

KEYNAME = SKYRESID

Sky residuals calculations over each sky fiber and averaged over sky fibers.


Keyword Description
~~~~~~~~~~~~~~~~~~~

================ =================  ================ ===================================================
KEY              Example Value      Type             Comment
================ =================  ================ ===================================================
CAMERA           b4                 string           b0-b9, r0-r9, z0-z9
EXPID            00003900           int  	     Exposure ID
FLAVOR           science            string           The type of exposure that can flat, arc or science 
PANAME           ApplyFiberFlat_QL  string           Name of pipeline algorihm
QATIME           2018-05-27T        float            Timestamp (UTC) of time of QA execution
                 11:35:45.62
NIGHT            20191017           int              The night of observation
PROGRAM          dark               string           Name of the observing program: dark, grey, bright 
MED_RESID	 0.786	            float      	     Median of residuals over all sky fibers
MED_RESID_FIBER  0.548..0.001       float[NSKY_FIB]  Median of residuals per sky fiber
MED_RESID_WAVE   0.426..0.371       float[NWAVE]     Median of residuals vs. wavelength in NWAVE bins
NBAD_PCHI        0	            int		     Number of fibers with bad chi^2
NREJ		 0                  int              Number of rejected fibers
NSKY_FIB         34	            int              Number of good sky fibers
RESID_PER	 28.83, 31.75       float[2]         95% c.l. boundaries of residuals distribution
WAVELENGTH	 5630...7740.       float[NWAVE]     Wavelength (Ang.) in NWAVE bins
RA               [500RA]            float[500]       Right ascention of 500 targets from the fibermap
DEC              [500DEC]           float[500]       Declination of 500 targets from the fibermap
SKYFIBERID       [37FIBERID]        int[N]           N is number of sky fibers 
WAVG_RES_WAVE    [2701]             float[NWAVE]     Wavelength (Ang.)in NWAVE bins for the sky residual 
RESID_STATUS     NORMAL             string           Reports the status of MED_RESID
================ =================  ===============  ===================================================

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
            21.90059973240197,
            21.859592929966595,
            21.872541810121973,
            21.917932990695206,
            21.801447235139577,
            21.831540683579036,
            21.94172558439847,
            22.269272523319387,
            22.034558597611735,
            21.985926857588197,
            22.353911267780717,
            22.32892764396665,
            22.41375970864624,
            21.927311569249582
        ],
        "MED_RESID": 0.7276316449002991,
        "MED_RESID_FIBER": [
            1.2568609891685298,
            1.0527575061361745,
            0.21255234730099914,
            0.8789084554595661,
            0.9130550223971454,
            0.7245695211741179,
            0.9945268712956477,
            0.5300647208032672,
            0.5040544948046843,
            0.935063635147884,
            0.7950061364409464,
            0.985017930916797,
            1.3878735701062226,
            0.9189974319605767,
            1.0745920920786602,
            0.5216382609174559,
            0.12405146989650007,
            0.16337750375609517,
            0.3681961469972421,
            0.7611769357112053,
            0.8555736567710426,
            0.6655582871934129,
            0.5989908405988729,
            0.39234184166093655,
            0.4909732026144127,
            0.9252757527328015,
            0.5855395725639312,
            0.9494403500927433,
            0.5237315895009829,
            1.2272244410634698,
            0.8137278242269019,
            0.24203972806745355,
            0.6742157442480519,
            0.5652148025339514,
            0.7904989362755117,
            0.6694699749189255,
            0.5005592833496166
        ],
        "MED_RESID_WAVE": [
            0.5745416619619164,
            0.9960327413386736,
            -0.6635758564707164,
            1.0370870537775083,
            0.6585096377366391,
            0.37429128852124904,
            3.232159983083619
        ],
        "MED_SKY": 161.7560924392828,
        "NBAD_PCHI": 23,
        "NREJ": 0,
        "NSKY_FIB": 37,
        "RA": [
            266.4916642633111,
            266.4970976025655,
            266.38371316301436,
            266.389322356526,
            266.83762130178553,
            266.8534326111375,
            266.9023341779871,
            266.917368173174,
            266.82661563413376,
            266.74234113825537,
            266.86995540537663,
            266.27022788465985,
            266.2301640479942,
            266.3747437884682,
            266.2184661684719,
            266.4044423436187,
            266.22424630492117,
            266.1014775421213,
            266.26543951838596,
            266.09566406010117,
            266.45604752117356,
            266.7315031576531,
            266.7210694601056,
            266.6478043633041,
            266.7211067886968,
            266.68412119940604,
            266.67375510360904,
            ...,
            266.6948250567388
        ],
        "RESID_PER": [
            -25.149610421851662,
            28.337551737374536
        ],
        "RESID_STATUS": "NORMAL",
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
        "WAVELENGTH": [
            3570.0,
            3570.8,
            3571.6000000000004,
            3572.4000000000005,
            3573.2000000000007,
            3574.000000000001,
            3574.800000000001,
            3575.6000000000013,
            3576.4000000000015,
            3577.2000000000016,
            3578.000000000002,
            3578.800000000002,
            3579.600000000002,
            3580.4000000000024,
            3581.2000000000025,
            3582.0000000000027,
            3582.800000000003,
            3583.600000000003,
            ...,
            3584.4000000000033,
            3585.2000000000035,
            3586.0000000000036,
            3586.800000000004,
            3587.600000000004,
            3588.400000000004,
            5729.200000000491,
            5730.000000000491
        ],
        "WAVG_RES_WAVE": [
            0.19489687166520253,
            -0.1170422342786701,
            -0.11731835286460443,
            0.18732949810837374,
            0.06462167229015336,
            -0.014248165577506591,
            -0.09882937131035334,
            0.08688376825567252,
            0.030884535495678548,
            0.08864069163197943,
            -0.161379481520509,
            ...,
            0.22163775489830406,
            -0.14288055259933471,
            0.10083654653906268,
            0.1503838936601779,
            -0.04828957815074004,
            0.030697383654788035
        ]
    },
    "NIGHT": "20191017",
    "PANAME": "SkySub_QL",
    "PARAMS": {
        "BIN_SZ": 0.1,
        "MED_RESID_REF": 0,
        "PCHI_RESID": 0.05,
        "PER_RESID": 95.0,
        "RESID_NORMAL_RANGE": [
            -5.0,
            5.0
        ],
        "RESID_WARN_RANGE": [
            -10.0,
            10.0
        ]
    },
    "PROGRAM": "dark",
    "QATIME": "2018-05-27T11:35:45.625958",
    "QA_STATUS": "UNKNOWN"
}
