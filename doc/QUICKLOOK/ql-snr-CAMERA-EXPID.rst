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

================ ================= ===========  =======================================
KEY              Example Value     Type         Comment
================ ================= ===========  =======================================
CAMERA           r5                string       b0-b9, r0-r9, z0-z9
EXPID            00003580          int          Exposure ID
FLAVOR           science           string       The type of exposure that can flat, arc or science 
PANAME           SkySub_QL         string       Name of pipeline algorihm
QATIME           2018-06-26T       float        Timestamp (UTC) of time of QA execution
                 1:35:46.731
NIGHT            20191001          int          The night of observation
PROGRAM          dark              string       Name of the observing program: dark, grey, bright 
MEDIAN_SNR       [1.3,...]         float[500]   Median S/N per fiber
NUM_NEGATIVE_SNR 0                 int          Number of targets with negative SNR
MAGNITUDES       3,500             float[500]   List of 3 imaging mags [DECAM_G,DECAM_R,DECAM_Z] for all the 500 fibers 
ELG_FIBERID      331               int[ne]      Fiber IDs for ELG candidates, ne is number of the ELGs
LRG_FIBERID      65                int[nl]      Fiber IDs for LRG candidates, nl is number of the LRGs
QSO_FIBERID      56                int[nq]      Fiber IDs for QSO candidates, nq is number of the QSOs
STAR_FIBERID     11                int[ns]      Fiber IDs for standard STARs, ns is number of the STARs
SNR_MAG_TGT      4                 float[N]     List of average SNR for target type, N is number of target types   
SNR_RESID        436               float[Nobj]  List of the SNR values for the targets, Nobj is 500-Nskyfibers
FIDSNR_TGT       4                 float[4]     List of fiducial SNR per target type 
RA               500               float[500]   List of 500 RA for the 500 fibers 
DEC              500               float[500]   List of 500 DEC for the 500 fibers 
FITCOEFF_TGT     4,2               float[4,2]   List of 4 [a,B] Best fit throughput("a") and sky b/g ("B") per target type
FITCOVAR_TGT     4,2x2             float[16]    List of 2x2 covariance matrices [[[c1,c2],[c3,c4]],[[c1,c2],[c3,c4]], ...]  
FIDSNR_STATUS    NORMAL            string       Reports the status of FIDSNR_TGT
================ ================= ===========  =======================================

Example JSON Output 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    {
    "CAMERA": "r5",
    "EXPID": "00003580",
    "FLAVOR": "science",
    "METRICS": {
        "DEC": [
            52.072322910306625,
            52.07753822508801,
            52.019446929065744,
            52.04600403688608,
            ...,
            52.26222360255711,
            52.29168030498678,
            52.278695573328704,
            52.33416610672152,
            52.35910853722059,
            52.380516463988975,
            52.443566736563774,
            52.397126382311164,
            52.478463424508064,
            52.48685298702915,
            52.35559992338816,
            52.29990696806419,
            52.422088344036275,
            52.40193923325824
        ],
        "MED_RESID": 1.027462190391721,
        "MED_RESID_FIBER": [
            0.4057629704110326,
            1.0910490963628519,
            1.0879855458359486,
            1.7002100702265892,
            0.31122944804289254,
            1.4505440435290602,
            1.5875425785502841,
            0.4080417729727799,
            0.9446808260591979,
            1.7613498310248445,
            0.29953923369807,
            0.7014108845780811,
            0.6406359028940471,
            1.411695308634961,
            1.1244807007236517,
            0.8785083866010694,
            0.7383726426310737,
            1.4282236673339241,
            0.6272419531853757,
            1.280661042776842,
            0.9688670274591544,
            1.6638976636134295,
            1.5185168063502985,
            0.9069535720654045,
            1.9985202590142563,
            1.7732479960291556,
            1.6380996384630002,
            1.2398754093396107,
            0.44588057199327125,
            1.0411633543362058,
            1.01365933038295,
            0.02545830780536562,
            0.6745063943603942,
            0.6919725016568279,
            1.4223112513357563,
            0.48053129697626673,
            1.018819913848219,
            1.1932568806741273
        ],
        "MED_RESID_WAVE": [
            -0.37636081158876245,
            -0.10420036942629274,
            1.8242356981374965,
            -0.015137348955733376,
            ...,
            3.357898556865514,
            2.68922058017419,
            0.20142280305596216,
            2.1509171497127753,
            -0.685631307813388
        ],
        "MED_SKY": 216.22270821276066,
        "NBAD_PCHI": 38,
        "NREJ": 0,
        "NSKY_FIB": 38,
        "RA": [
            129.64226379314877,
            129.4010799807199,
            129.49180214773585,
            ...,
            129.6739682547491,
            130.07816197705785,
            130.21106098800425,
            129.76174495200144
        ],
        "RESID_PER": [
            -36.42725212678916,
            51.560300548531714
        ],
        "RESID_STATUS": "NORMAL",
        "SKYFIBERID": [
            10,
            31,
            55,
            57,
            82,
            84,
            109,
            115,
            132,
            151,
            171,
            184,
            195,
            203,
            206,
            217,
            236,
            253,
            273,
            291,
            294,
            317,
            319,
            324,
            334,
            346,
            362,
            378,
            379,
            393,
            416,
            418,
            420,
            423,
            448,
            453,
            464,
            488
        ],
        "WAVELENGTH": [
            5630.0,
            5630.8,
            5631.6,
            5632.400000000001,
            ...,
            7735.600000000479,
            7736.400000000479,
            7737.200000000479,
            7738.000000000479,
            7738.8000000004795,
            7739.60000000048
        ],
        "WAVG_RES_WAVE": [
            -0.018538573822382484,
            0.07503820670272326,
            0.06851037238008865,
            ...,
            5.868282545697325,
            1.2009071804529925,
            0.7624632437881925,
            1.6277833028232955,
            0.04715205590883664
        ]
    },
    "NIGHT": "20191001",
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
    "QATIME": "2018-06-26T13:30:59.536560"
    }
