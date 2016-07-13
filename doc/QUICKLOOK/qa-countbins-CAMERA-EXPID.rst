==============================
qa-countbins-CAMERA-EXPID.yaml
==============================

:Summary: This QA for QuickLook includes the calculation of the number
	  of spectral bins above threshold.
:Naming Convention: ``qa-countbins-{ARM}{SPECTROGRAPH}-{EXPID}.yaml``, where 
        {ARM} is the 1-char arm name (r,b,z), {SPECTROGRAPH} indexes 
        CCDs 0-9 on that arm, and {EXPID} is the 8-digit exposure ID.  
        Together, {ARM}{SPECTROGRAPH} specify a {CAMERA}.
:Regex: ``qa-countbins-[brz][0-9]-[0-9]{8}\.yaml``
:File Type:  YAML


Inputs
======

Written by qa_quicklook.py, with Count_Spectral_bins using:

- frame
- psfboot

Contents
========

========== ================ ===========================================
KEYNAME    Type             Contents
========== ================ ===========================================
COUNTBINS  Py dictionary    Number of bins per spectrum above threshold
========== ================ ===========================================



Dictionary Contents
===================

KEYNAME = COUNTBINS

Calculation of number of bins above a threshold per spectrum.

Keyword Description
~~~~~~~~~~~~~~~~~~~

================ ============= ========== ============================================================
KEY              Example Value Type       Comment
================ ============= ========== ============================================================
ARM              r             char       Spectrograph arm b,r,z
SPECTROGRAPH     0             int  	  Camera index 0..9
EXPID            00000002      int  	  exposure ID
PANAME           BOXCAR        string     name of pipeline algorihm
MJD              57578.78099   float      Modified Julian Date (JD-2400000.5) in days of the time of QA execution
NBINS100         200           int[500]   number of bins above 100 counts per fiber
NBINS100_AMP     190           float[4]   number of bins above 100 counts averaged over each amplifier
NBINS250         100           int[500]   number of bins above 250 cts per fiber
NBINS250_AMP     90            float[4]   number of bins above 250 cts averaged over each amplifier
NBINS500         10            int[500]   number of bins above 500 cts per fiber
NBINS500_AMP     9             float[4]   number of bins above 500 cts averaged over each amplifier
================ ============= ========== ============================================================

Example YAML Output
~~~~~~~~~~~~~~~~~~~

::

    {'COUNTBINS': 
       {'ARM': 'r', 'EXPID': '00000006', 'MJD': 57578.78098693542, 'PANAME': 'BOXCAR', 'SPECTROGRAPH': 0,
        'VALUE': 
            {'NBINS100': array([ 2575.,  2611.,  2451.,  2495.,  2357.,  2452.,  2528.,  2501.,  2548.,  2461.]),
             'NBINS100_AMP': array([ 1249.74,     0.  ,  1198.01,     0.  ]),
             'NBINS250': array([ 2503.,  2539.,  2161.,  2259.,  2077.,  2163.,  2284.,  2268.,  2387.,  2210.]),
             'NBINS250_AMP': array([ 1149.55,     0.  ,  1095.02,     0.  ]),
             'NBINS500': array([ 2307.,  2448.,   229.,  1910.,    94.,   306.,  2056.,  1941.,  2164.,   785.]),
             'NBINS500_AMP': array([ 688.85,    0.  ,  648.75,    0.  ])
            }
       }
    }
