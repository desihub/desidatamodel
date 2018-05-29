=============================
ql-mergedQA-CAMERA-EXPID.json
=============================

:Summary: This QA for QuickLook includes the calculation of the sky
	  continuum level in sky fibers.
:Naming Convention: ``ql-mergedQA-{ARM}{SPECTROGRAPH}-{EXPID}.json``, where 
        {ARM} is the 1-char arm name (r,b,z), {SPECTROGRAPH} indexes 
        CCDs 0-9 on that arm, and {EXPID} is the 8-digit exposure ID.  
        Together, {ARM}{SPECTROGRAPH} specify a {CAMERA}.
:Regex: ``ql-mergedQA-[brz][0-9]-[0-9]{8}\.json``
:File Type:  JSON


Inputs
======

Written by merger.py using:


Contents
========

========== ================ ==============================================
KEYNAME    Type             Contents
========== ================ ==============================================
SKYRESID   Py dictionary    Residuals calculation on sky fibers
========== ================ ==============================================



Dictionary Contents
===================

KEYNAME = mergedQA

Sky residuals calculations over each sky fiber and averaged over sky fibers.


Keyword Description
~~~~~~~~~~~~~~~~~~~

======================= =================  ================ ===================================================
KEY                     Example Value      Type             Comment
======================= =================  ================ ===================================================
CAMERA                  b4                 string           b0-b9, r0-r9, z0-z9
EXPID                   00003900           int  	    Exposure ID
FLAVOR                  science            string           The type of exposure that can flat, arc or science 
NIGHT                   20191017           int              The night of observation
PROGRAM                 dark               string           Name of the observing program: dark, grey, bright 
SEEING                  1.1                float            From the header of the proproc image 
EXPTIME                 1000.0             float            From the header of the proproc image 
AIRMASS                 1.0                float            From the header of the proproc image 
ELG_FIBERID             331                int[ne]          From the fibermap, ne is number of ELGs
LRG_FIBERID             65                 int[nl]          From the fibermap, nl is number of LRGs
QSO_FIBERID             56                 int[nq]          From the fibermap, nq is number of QSOs
SKY_FIBERID             37                 int[nsky]        From the fibermap, nsky is number of Sky fibers
STAR_FIBERID            11                 int[ns]          From the fibermap, nsky is number STARs
IMAGING_MAGS            500, 3             float[500,3]     From the fibermap [DECAM_G, DECAM_R, DECAM_Z]
RA                      500                float[500]       Right ascention of all the 500 targets
DEC                     500                float[500]       Declination of all the 500 targets
B_PEAKS                 3                  float[3]         configured peak sky wavelengths in b band
R_PEAKS                 5                  float[5]         configured peak sky wavelengths in r band
Z_PEAKS                 6                  float[6]         configured peak sky wavelengths in z band
FITS_DESISPEC_VERSION   0.21.0.dev2590     string           version of the desispec software that created the fits
PROC_QuickLook_VERSION  05.18.0            string           version of the Quicklook software that was ran 
PROC_DESISPEC_VERSION   0.21.0.dev2590     string           versopn of the desispec software created the preproc image
QLrun_datime_UTC        2018-05-27         string           date and time of the merger as the last of quicklook step 

**CHECK_HDUs KEY        Example Value      Type             Comment**

EXPNUM_STATUS           NORMAL             string           Reports the result of a match between exposures number in the 
                                                            header and the 
                                                            one given in the argument
HDU_STATUS              NORMAL             string           Reports the result of finding the camera in the header 

**CHECK_CCDs  KEY       Example Value      Type             Comment**

BIAS_AMP                4                  float[4]         value of bias averaged over each amplifier
BIAS_STATUS             1                  ALARM            Reports the status of BIAS_AMP
BIAS_PATNOISE           4                  float[4]         rms of the row by row bias difference divided by the noise of 
                                                            that amp
DATA5SIG                1                  int              Number of pixels with counts 5sigma below bias in region of CCD
DIFF1SIG                0.032              float            Diff. between 1 sigma low and high percentile bounds 
DIFF2SIG                0.057              float            Diff. between 2 sigma low and high percentile bounds
LITFRAC_AMP             4                  float[4]         Fraction of the pixels per amp that are above CUTPIX = 5sigmas
LITFRAC_STATUS          ALARM              string           Reports the status of LITFRAC_AMP
NOISE_AMP               4                  float[4]         value of RMS per amp read directly from the header of the 
                                                            preproc image
NOISE_OVERSCAN_AMP      4                  float[4]         value of RMS of the onerscan region per amp read directly from 
                                                            the header of the preproc image
NOISE_STATUS            ALARM              string           Reports the status pf NOISE_AMP

**CHECK_FIBERSs KEY     Example Value      Type             Comment**

XWSIGMA_FIB             2,500              float[500,2]     median of XSIGMAs for all fibers per amp
GOOD_FIBER              500                boolean          List of boolians for good[1] and bad[0] fibers
NGOODFIB                <=500              int              Number of good fibers
NGOODFIB_STATUS         ALARM              string           Reports the status of NGOODFIB
XWSIGMA                 2                  float            List of median X and W sigmas
XWSIGMA_AMP             4,2                float[4,2]       List of four [X,W]sigmas
XWSIGMA_STATUS          ALARM              string           Reports the status of XWSIGMA

**CHECK_SPECTRA  KEY    Example Value      Type             Comment**      

DELTAMAG                500	           float[500]	    List of mag diff b/w the fibermag and the imaging mag from the 
                                                            fibermap
DELTAMAG_STATUS         ALARM              string	    Status of DELTAMAG_TGT
DELTAMAG_TGT            [-2.92,...]	   float[N]	    List of the average fiber mag per target types in this camera
FIBER_MAG               [18.22, ...]	   float[500]       Magnitude of the 500 fibers
FIDSNR_STATUS           ALARM	           string	    Reports the status of FIDSNR_TGT
FIDSNR_TGT              4	           float[4]	    List of fiducial SNR per target type
FITCOEFF_TGT            4,2	           float[4,2]	    List of 4[a,B] Best fit throughput("a") & sky b/g "B" per target
FITCOVAR_TGT            4,2x2	           float[16]	    List of 2x2 covariance matrices [[[c1,c2],[c3,c4]], ...]
MEDIAN_SNR              [1.3,...]	   float[500]       Median SNR per fiber
NSKY_FIB                37                 int              Number of sky fibers 
NUM_NEGATIVE_SNR        0	           int	            Number of targets with negative SNR
PEAKCOUNT               500                float[500]       Sum of counts in peak regions per fiber
PEAKCOUNT_MED_SKY       []                 float[]          Median of PEAKCOUNT over sky fibers
PEAKCOUNT_NOISE         0.072              float            rms of PEAKCOUNT over sky fibers FOR SCIENCE EXPOSURES
PEAKCOUNT_STATUS        ALARM              string           reports the status of the PEAKCOUNT 
SKYCONT                 210.0	           float	    Sky cont. in all configured continuum areas averaged over all 
                                                            sky fibers
SKYCONT_FIBER           357.238	           float[N]	    Sky continuum per sky fiber averaged over two continuum regions, 
                                                            'N' is number of sky fibers
SKYCONT_STATUS          NORMAL	           string	    Reports the status of the SKYCONT
SNR_MAG_TGT             4	           float[N]	    List of average SNR for target type, N is number of target types
SNR_RESID               436	           float[Nobj]	    List of the SNR values for the targets, Nobj is 500-Nskyfibers
STAR_FIBERID            11	           int[ns]  	    Fiber IDs for standard STARs, ns is number of the STARs
STD_FIBERID             11                 int[n]           Star Fiber IDs 
Sky_Rband               1000	           float            Average value of sky bg in R-band-> to come from ETC (current 
                                                            value is a place holder)
Sky_Rflux_diff          []                 float[N]         Diff b/w flux from sky monitor and the calculated mag from the 
                                                            sky fibers
Sky_fib_Rband           1000	           float	    Average sky fiber mag in camera r [if the camera is not r, this 
                                                            is equal to the value of the Sky_Rband]
WAVELENGTH              5630...7740	   float[NWAVE]     Wavelength (Ang.) in NWAVE bins
WAVG_RES_WAVE           2701	           float[NWAVE]     Wavelength (Ang.)in NWAVE bins for the sky residual 
======================= =================  ================ ===================================================

Example JSON Output
~~~~~~~~~~~~~~~~~~~
::
    {
    "CAMERA": "b4",
    "EXPID": 3900,
    "FLAVOR": "science",
    "GENERAL_INFO": {
        "AIRMASS": 1.0,
        "B_PEAKS": [
            3914.4,
            5199.3,
            5201.8
        ],
        "DEC": [
            21.97228,
            21.93098,
            22.32893,
            22.41376,
            21.92731
        ],
        "ELG_FIBERID": [
            0,
            1,
            492,
            493,
            496
        ],
        "EXPTIME": 1000.0,
        "FITS_DESISPEC_VERSION": "0.21.0.dev2590",
        "IMAGING_MAGS": [
            [
                21.768278121948242,
                21.49117088317871,
                20.580245971679688
            ],
            [
                24.970773696899414,
                22.382829666137695,
                20.093137741088867
            ],
            [
                21.144075393676758,
                21.167299270629883,
                20.759214401245117
            ],
            [
                22.660327911376953,
                22.387176513671875,
                21.669944763183594
            ],
            [
                21.72871208190918,
                21.392578125,
                20.735403060913086
            ],
            [
                23.56468963623047,
                23.369524002075195,
                22.301538467407227
            ],
            [
                22.619417190551758,
                22.045270919799805,
                21.195775985717773
            ],
            [
                22.03432273864746,
                21.490217208862305,
                20.80316734313965
            ],
            [
                20.19066047668457,
                19.020654678344727,
                18.338804244995117
            ],
            [
                18.301464080810547,
                18.01443862915039,
                17.923023223876953
            ],
            [
                21.553579330444336,
                21.368295669555664,
                20.55998420715332
            ],
            [
                22.378395080566406,
                21.842634201049805,
                20.983251571655273
            ],
            [
                22.77434539794922,
                22.76066780090332,
                21.9818172454834
            ],
            [
                23.220855712890625,
                22.86495590209961,
                22.086009979248047
            ],
            [
                18.10835075378418,
                17.86771583557129,
                17.787166595458984
            ],
            [
                0.0,
                0.0,
                0.0
            ],
            [
                21.079086303710938,
                21.04962158203125,
                20.45486831665039
            ],
            [
                24.13585662841797,
                21.98204803466797,
                20.061687469482422
            ],
            [
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0
            ]
        ],
        "LRG_FIBERID": [
            3,
            4,
            14,
            28,
            41,
            53,
            57,
            66,
            69,
            80,
            82,
            85,
            92,
            93,
            103,
            109,
            111,
            116,
            118,
            128,
            133,
            134,
            141,
            147,
            160,
            170,
            183,
            195,
            196,
            197,
            204,
            205,
            226,
            238,
            242,
            252,
            281,
            286,
            296,
            317,
            320,
            321,
            325,
            327,
            328,
            340,
            343,
            348,
            361,
            366,
            374,
            384,
            393,
            396,
            397,
            398,
            425,
            434,
            439,
            441,
            443,
            468,
            470,
            481,
            497
        ],
        "PROC_DESISPEC_VERSION": "0.21.0.dev2590",
        "PROC_QuickLook_VERSION": "05.18.0",
        "QLrun_datime_UTC": "2018-05-27T18:35:48.415495+00:00",
        "QSO_FIBERID": [
            22,
            23,
            24,
            394,
            407,
            412,
            415,
            418,
            430,
            432,
            450,
            465,
            488
        ],
        "RA": [
            266.49166,
            266.4971,
            266.38371,
            266.6478,
            266.72111,
            266.68412,
            266.67376,
            266.69483
        ],
        "R_PEAKS": [
            6301.9,
            6365.4,
            7318.2,
            7342.8,
            7371.3
        ],
        "SEEING": 1.1,
        "SKY_FIBERID": [
            10,
            21,
            68,
            123,
            146,
            495,
            498,
            499
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
    "NIGHT": "20191017",
    "PROGRAM": "dark",
    "TASKS": {
        "CHECK_CCDs": {
            "METRICS": {
                "BIAS_AMP": [
                    166.859375,
                    150.6064453125,
                    155.20818359375,
                    115.488330078125
                ],
                "BIAS_PATNOISE": [
                    0.001928452933161584,
                    0.0020551932894211223,
                    0.013377496003722351,
                    0.013273444424777932
                ],
                "BIAS_STATUS": "ALARM",
                "DATA5SIG": 1,
                "DIFF1SIG": 0.032,
                "DIFF2SIG": 0.056999999999999995,
                "LITFRAC_AMP": [
                    0.35,
                    0.34,
                    0.4,
                    0.37
                ],
                "LITFRAC_STATUS": "ALARM",
                "NOISE_AMP": [
                    1.9158278538024538,
                    2.013828948358283,
                    2.0502913804455387,
                    2.1458059208513554
                ],
                "NOISE_OVERSCAN_AMP": [
                    1.887512473265009,
                    1.996400550363147,
                    2.032141125973641,
                    2.121880270752116
                ],
                "NOISE_STATUS": "ALARM",
                "XWSIGMA_FIB": [
                    [
                        1.0123793306924045,
                        1.1444027903628013,
                        1.0779326196036232,
                        1.1327402165649072,
                        1.1453319200070724,
                        1.0751026848571685,
                        1.0686079975205944,
                        1.0600127660463265,
                        1.054935919411833,
                        1.108142254722341,
                        1.1137895065931211,
                        1.100255305298232,
                        1.1278924016886318,
                        1.0896967346779587,
                        1.0883014659309582
                    ],
                    [
                        2.2455766193091846,
                        2.200338940760254,
                        2.2390777828190305,
                        2.628837365798121,
                        3.1475902587686995,
                        2.761903371770449,
                        2.4092355105757903,
                        2.198611187615043
                    ]
                ]
            },
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
                "CUTPIX": 5,
                "LITFRAC_AMP_REF": [
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "LITFRAC_NORMAL_RANGE": [
                    -0.1,
                    0.1
                ],
                "LITFRAC_WARN_RANGE": [
                    -0.2,
                    0.2
                ],
                "NOISE_AMP_REF": [
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "NOISE_NORMAL_RANGE": [
                    -1.0,
                    1.0
                ],
                "NOISE_WARN_RANGE": [
                    -2.0,
                    2.0
                ],
                "PERCENTILES": [
                    68.2,
                    95.4,
                    99.7
                ]
            }
        },
        "CHECK_FIBERS": {
            "METRICS": {
                "GOOD_FIBER": [
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1
                ],
                "NGOODFIB": 500,
                "NGOODFIB_STATUS": "ALARM",
                "XWSIGMA": [
                    1.0962765182946193,
                    2.490368288601727
                ],
                "XWSIGMA_AMP": [
                    [
                        1.0932880388002917,
                        1.123310768812173,
                        1.1009015445920427,
                        1.097427842659204
                    ],
                    [
                        2.76543054582097,
                        2.872940343391557,
                        2.1728369775096796,
                        2.03414610561234
                    ]
                ],
                "XWSIGMA_STATUS": "ALARM"
            },
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
                "N_KNOWN_BROKEN_FIBERS": 0,
                "XWSIGMA_NORMAL_RANGE": [
                    -2.0,
                    2.0
                ],
                "XWSIGMA_REF": [
                    0.0,
                    0.0
                ],
                "XWSIGMA_WARN_RANGE": [
                    -4.0,
                    4.0
                ]
            }
        },
        "CHECK_HDUs": {
            "METRICS": {
                "EXPNUM_STATUS": "NORMAL",
                "HDU_STATUS": "NORMAL"
            },
            "PARAMS": {}
        },
        "CHECK_SPECTRA": {
            "METRICS": {
                "DELTAMAG": [
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "DELTAMAG_STATUS": "ALARM",
                "DELTAMAG_TGT": [
                    -2.9209345331080705,
                    NaN,
                    -0.9617997285914122,
                    -4.5797822546440585
                ],
                "FIBER_MAG": [
                    18.22211846792697,
                    18.294963907355225,
                    18.531643981477078,
                    18.093002194566413,
                    19.836466028202693,
                    17.855048480110344,
                    18.037687872067785,
                    16.36508905569825,
                    14.499875077057922,
                    18.04873726973664,
                    18.815403796152726,
                    18.65684747620505,
                    19.496542472637184,
                    14.355974323669292,
                    20.44467651749146,
                    17.614472005720117,
                    20.413050642790882,
                    20.369118034559737,
                    21.828487269112493
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
                    26.44205812988254,
                    0.055429772987813146,
                    2.3737309202724135,
                    0.15843609244301018,
                    0.045657180738248856,
                    0.03217024229506693
                ],
                "NSKY_FIB": 37,
                "NUM_NEGATIVE_SNR": 0,
                "PEAKCOUNT": [
                    4.282293116542009,
                    4.0728734401088325,
                    4.193777093245643,
                    4.122202262066192,
                    4.154971725601357,
                    4.273396777110791,
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
                "SNR_MAG_TGT": [
                    [
                        [
                            1.3888110111835048,
                            0.9910427371615417,
                            1.1047877997495437,
                            1.1228397601173319,
                            1.6203198985339835,
                            0.8092596759192475,
                            0.5770416530937033,
                            0.4192574073425639,
                            2.3737309202724135
                        ],
                        [
                            21.768278121948242,
                            22.190134048461914,
                            22.069507598876953,
                            22.022939682006836,
                            22.680341720581055,
                            22.378395080566406,
                            22.77434539794922,
                            23.220855712890625,
                            21.079086303710938
                        ]
                    ],
                    [
                        [
                            0.42504951691991677,
                            0.33621676451816346,
                            0.13208611652530025,
                            0.11787774262770066,
                            0.16163979408552576,
                            22.871192932128906,
                            22.723430633544922,
                            23.976768493652344,
                            23.876712799072266,
                            24.010169982910156,
                            23.21418571472168,
                            22.481813430786133,
                            23.35832977294922,
                            23.387266159057617,
                            24.6326847076416,
                            22.93088722229004,
                            22.28416633605957,
                            22.16317367553711,
                            24.970773696899414,
                            24.13585662841797
                        ]
                    ],
                    [
                        [
                            2.668064584435045,
                            4.534891775530744,
                            7.001092113343514,
                            23.004459600205564,
                            2.459360160912795,
                            0.70004114648262,
                            1.3281444096053956,
                            0.5787011447281183,
                            0.8227862795956193,
                            2.4661993288805393,
                            5.309835023485187,
                            1.9370139734026364,
                            6.365365808430682,
                            2.5154770949352607,
                            3.767451014026534,
                            1.7147228985097727,
                            5.099272860371672,
                            0.28500281039900943,
                            1.0769896744683076,
                            1.052564077971569,
                            2.541880635280774,
                            1.1668045920346806,
                            1.5575272468532595,
                            4.331985292955852,
                            1.73270979198809,
                            1.9039334573059148,
                            0.9446030297615723,
                            6.556673335915103
                        ],
                        [
                            21.339683532714844,
                            20.391786575317383,
                            20.041345596313477,
                            18.217931747436523,
                            21.482370376586914,
                            21.46392250061035,
                            21.293500900268555,
                            20.6695499420166,
                            21.826372146606445,
                            21.703950881958008,
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
                    0.017515587774205397,
                    0.023087314012686978,
                    -0.0029061145162523915,
                    -0.00312343526779094,
                    0.02174284890361092,
                    -0.030770662143093912,
                    0.002649484531870325,
                    0.027737789245466108,
                    0.013926939780162738,
                    0.04100741778955626,
                    0.10430920001065432,
                    0.3619963218319283,
                    -0.002515847056861169,
                    -0.004043351725173604,
                    -0.010963631146359861,
                    0.02276248815655518,
                    0.005691266747180557,
                    0.015059255635632596,
                    0.008801047729653733,
                    0.00246191243308398,
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
                ],
                "STD_FIBERID": [
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
                ],
                "Sky_Rband": 1000,
                "Sky_Rflux_diff": 1000,
                "Sky_fib_Rband": [],
                "WAVELENGTH": [
                    3570.0,
                    3570.8,
                    3571.6000000000004,
                    3572.4000000000005,
                    3573.2000000000007,
                    3574.000000000001,
                    3574.800000000001,
                    5729.200000000491,
                    5730.000000000491
                ],
                "WAVG_RES_WAVE": [
                    0.19489687166520253,
                    -0.1170422342786701,
                    -0.11731835286460443,
                    -1.0382510251337687,
                    0.5573978912954005,
                    -0.4828991245036719,
                    0.1503838936601779,
                    -0.04828957815074004,
                    0.030697383654788035
                ]
            },
            "PARAMS": {
                "BIN_SZ": 0.1,
                "B_CONT": [
                    "4000, 4500",
                    "5250, 5550"
                ],
                "DELTAMAG_NORMAL_RANGE": [
                    -0.5,
                    0.5
                ],
                "DELTAMAG_TGT_REF": [
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "DELTAMAG_WARN_RANGE": [
                    -1.0,
                    1.0
                ],
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
                ],
                "MED_RESID_REF": 0,
                "PCHI_RESID": 0.05,
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
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "PEAKCOUNT_WARN_RANGE": [
                    500.0,
                    40000.0
                ],
                "PER_RESID": 95.0,
                "RESID_NORMAL_RANGE": [
                    -5.0,
                    5.0
                ],
                "RESID_WARN_RANGE": [
                    -10.0,
                    10.0
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
            }
        }
    }
}
    
    
