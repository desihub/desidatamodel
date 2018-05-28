========================
ql-snr-CAMERA-EXPID.json
========================

:Summary: This QA for QuickLook first includes the calculation of 
        signal-to-noise in the spectrum after sky subtraction. 
:Naming Convention: ``ql-snr-{ARM}{SPECTROGRAPH}-{EXPID}.json``, where 
        {ARM} is the 1-char arm name (r,b,z), {SPECTROGRAPH} indexes 
        CCDs 0-9 on that arm, and {EXPID} is the 8-digit exposure ID.  
        Together, {ARM}{SPECTROGRAPH} specify a {CAMERA}.
:Regex: ``ql-snr-[brz][0-9]-[0-9]{8}\.json``
:File Type:  JSON


Inputs
======

Written by qa_quicklook.py, with Calculate_SNR using:

- frame
- skymodel

Contents
========

========== ================ ===========================
KEYNAME    Type             Contents
========== ================ ===========================
SNR        Py dictionary    Spectral signal-to-noise
========== ================ ===========================



Dictionary Contents
===================

KEYNAME = SNR

Spectral signal-to-noise calculations per fiber and per CCD amp.

Keyword Description
~~~~~~~~~~~~~~~~~~~

=============== ================   ==========  =======================================
KEY             Example Value      Type        Comment
=============== ================   ==========  =======================================
CAMERA           b4                string      b0-b9, r0-r9, z0-z9
EXPID            00003900          int         Exposure ID
FLAVOR           science           string      The type of exposure that can flat, arc or science 
PANAME           ApplyFiberFlat_QL string      Name of pipeline algorihm
QATIME           2018-05-27T       float       Timestamp (UTC) of time of QA execution
                 1:35:46.731
NIGHT            20191017          int         The night of observation
PROGRAM          dark              string      name of the observing program: dark, grey, bright 
MEDIAN_SNR       1.3233            float[500]  median S/N per fiber
NUM_NEGATIVE_SNR 0                 int  
MAGNITUDES       3,500             float[500]  list of 3 imaging mags [DECAM_G,DECAM_R,DECAM_Z] for all the 500 fibers 
ELG_FIBERID      331               int[ne]     fiber IDs for ELG candidates, ne is number of the ELGs
LRG_FIBERID      65                int[nl]     fiber IDs for LRG candidates, nl is number of the LRGs
QSO_FIBERID      56                int[nq]     fiber IDs for QSO candidates, nq is number of the QSOs
STAR_FIBERID     11                int[ns]     fiber IDs for standard STARs, ns is number of the STARs
SNR_MAG_TGT      4                 float[N]    List of average SNR for target type, N is number of target types   
SNR_RESID        436               float[Nobj] List of the SNR values for the targets, Nobj is 500-Nskyfibers
FIDSNR_TGT       4                 float[4]    List of fiducial SNR per target type 
RA               500               float[500]  List of 500 RA for the 500 fibers 
DEC              500               float[500]  List of 500 DEC for the 500 fibers 
FITCOEFF_TGT     4,2               float[8]    Best fit values of "a" and sky b/g "B" per target type [[a,B],[a,B],[a,B],...]
FITCOVAR_TGT     4,2x2             float[16]   List of 2x2 covariance matrices for the fitting process per target type [[[c1,c2],[c3,c4]],[[c1,c2],[c3,c4]], ...]  
FIDSNR_STATUS    ALARM             string      reports the status of FIDSNR_TGT
===============  ===============   ==========  =======================================

Example JSON Output 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
            ,
            22.41375970864624,
            21.927311569249582
        ],
        "ELG_FIBERID": [
            0,
            1,
            2,
            5,
            6,
            7,
            8,
            9,
            12,
            13,
            15,
            496
        ],
        "FIDSNR_STATUS": "ALARM",
        "FIDSNR_TGT": [
            9.02611794975721,
            2.8323789247849795,
            13.213652882604018,
            14.79627499073459
        ],
        "FITCOEFF_TGT": [
            [
                0.0051414443276263655,
                0.0439294330201913
            ],
            [
                0.00037778210265896294,
                0.0002992350767583131
            ],
            [
                0.013840444648328301,
                0.22651650038430657
            ],
            [
                0.014177811780657513,
                0.13247272671780377
            ]
        ],
        "FITCOVAR_TGT": [
            [
                [
                    6.750847575783027e-08,
                    1.2887319825878186e-06
                ],
                [
                    1.2887319825878189e-06,
                    2.4648452811713728e-05
                ]
            ],
            [
                [
                    2.318551454229215e-09,
                    5.126915890176872e-09
                ],
                [
                    5.126915890176872e-09,
                    1.1619353821195946e-08
                ]
            ],
            [
                [
                    5.21903763795648e-08,
                    2.5038815848408373e-06
                ],
                [
                    2.5038815848408373e-06,
                    0.00014434213087371778
                ]
            ],
            [
                [
                    3.841451018053207e-08,
                    4.260501038214355e-06
                ],
                [
                    4.260501038214355e-06,
                    0.0007107625767667906
                ]
            ]
        ],
        "LRG_FIBERID": [
            3,
            4,
            14,
            28,
            470,
            481,...
            497
        ],
        "MAGNITUDES": [
            [
                21.768278121948242,
                21.49117088317871,
                20.580245971679688
            ],
            [
                22.190134048461914,
                22.245996475219727,
                21.720712661743164
            ],
            [
                22.069507598876953,
                21.93402671813965,
                21.506183624267578
            ],

        ],
        "MEDIAN_SNR": [
            1.3888110111835048,
            0.9910427371615417,
            1.1047877997495437,
            0.42504951691991677,
            0.33621676451816346,
            1.1228397601173319,
            0.6220228751004641,
            0.6067200504064795,
            0.7441302666759139,
            0.03217024229506693
        ],
        "NUM_NEGATIVE_SNR": 0,
        "QSO_FIBERID": [
            22,
            23,
            24,
            37,
            45,
            52,
            72,
            89,
            102,
            110,
            465,
            488
        ],
        "RA": [
            266.4916642633111,
            266.4970976025655,
            266.38371316301436,
            266.389322356526,
            266.54413237029496,
            266.3422819100746,
            266.4362919987584,
            266.5495348885712,
            266.6948250567388
        ],
        "SNR_MAG_TGT": [
            [
                [
                    1.3888110111835048,
                    0.9910427371615417,
                    1.1047877997495437,
                    2.3737309202724135
                ],
                [
                    21.768278121948242,
                    22.190134048461914,
                    21.079086303710938
                ]
            ],
            [
                [
                    0.42504951691991677,
                    0.33621676451816346,
                    0.13208611652530025,
                    0.15843609244301018
                ],
                [
                    22.60101890563965,
                    24.13585662841797
                ]
            ],
            [
                [
                    2.668064584435045,
                    4.534891775530744,
                    7.001092113343514,
                   0.9446030297615723,
                    6.556673335915103
                ],
                [
                    21.339683532714844,
                    20.391786575317383,
                    20.041345596313477,
                    22.55977439880371,
                    20.19066047668457
                ]
            ],
            [
                [
                    41.77538198444144,
                    23.972114953623898,
                    65.23625855202515,
                    48.402580754303656,
                    31.210910974447348,
                    17.908334301642853,
                    62.41700960174561,
                    63.87851988289244,
                    34.11969344603663,
                    23.94751205345668,
                    26.44205812988254
                ],
                [
                    17.211620330810547,
                    18.290325164794922,
                    16.268943786621094,
                    16.94438362121582,
                    17.80036163330078,
                    18.712848663330078,
                    16.344135284423828,
                    16.3100643157959,
                    17.63705825805664,
                    18.301464080810547,
                    18.10835075378418
                ]
            ]
        ],
        "SNR_RESID": [
            -0.010278367991402965,
            0.05409239217317109,
            0.0008644565272702239,
            0.005818959109549498,
            -0.05732501125420436
        ],
        "STAR_FIBERID": [
            11,
            61,
            63,
            105,
            186,
            221,
            233,
            289,
            461,
            489,
            494
        ]
    },
    "NIGHT": "20191017",
    "PANAME": "SkySub_QL",
    "PARAMS": {
        "FIDMAG": 22.0,
        "FIDSNR_NORMAL_RANGE": [
            6.5,
            7.5
        ],
        "FIDSNR_TGT_REF": [
            0.0,
            0.0,
            0.0,
            0.0
        ],
        "FIDSNR_WARN_RANGE": [
            6.0,
            8.0
        ]
    },
    "PROGRAM": "dark",
    "QATIME": "2018-05-27T11:35:46.731521",
    "QA_STATUS": "UNKNOWN"
}
