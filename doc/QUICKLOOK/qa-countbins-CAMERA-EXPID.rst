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
QANAME		 COUNTBINS     string     name of QA algorithm
PANAME           BOXCAR        string     name of pipeline algorihm
TIMESTAMP        12.01234      float      time in hours of the day (UTC) of QA execution
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
        {'EXPID': '00000002', 'SPECTROGRAPH': 0, 'ARM': 'r', 'PANAME': 'BOXCAR', 'TIMESTAMP', 12.0123, 
         'VALUE': 
             {'NBINS100': 200.0,
	      'NBINS100_AMP': array([190.12, 200.88, 0., 0. ])
	      'NBINS250': 100.0,
	      'NBINS250_AMP': array([90.12, 100.88, 0., 0. ])
	      'NBINS500': 10.0,
	      'NBINS500_AMP': array([9.12, 10.88, 0., 0. ])
	      }
         }
     }
