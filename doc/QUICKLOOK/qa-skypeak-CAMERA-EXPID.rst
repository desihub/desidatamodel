============================
qa-skypeak-CAMERA-EXPID.yaml
============================

:Summary: This QA for QuickLook includes the calculation of the counts and RMS 
	  at peak sky wavelengths in a 1D spectrum.
:Naming Convention: ``qa-skypeaks-{ARM}{SPECTROGRAPH}-{EXPID}.yaml``, where 
        {ARM} is the 1-char arm name (r,b,z), {SPECTROGRAPH} indexes 
        CCDs 0-9 on that arm, and {EXPID} is the 8-digit exposure ID.  
        Together, {ARM}{SPECTROGRAPH} specify a {CAMERA}.
:Regex: ``qa-skypeak-[brz][0-9]-[0-9]{8}\.yaml``
:File Type:  YAML


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

================ ============= ========== ==============================================
KEY              Example Value Type       Comment
================ ============= ========== ==============================================
ARM              r             char       Spectrograph arm b,r,z
SPECTROGRAPH     0             int  	  Camera index 0..9
EXPID            00000002      int  	  exposure ID
PANAME           FIBERFLAT     string     name of pipeline algorihm
QATIME           2016-07-08T   float      timestamp (UTC) of time of QA execution
                 06:05:34.555
SUMCOUNT         1500.0        float[500] summed counts over specified peak sky 
                                          wavelengths
SUMCOUNT_RMS     1445.0        float      rms of summed counts over sky peaks
SUMCOUNT_RMS_SKY 1455.0        float      rms of summed counts over sky peaks on sky fibers
SUMCOUNT_RMS_AMP 1444.0        float[4]   rms of summed counts on sky fibers per AMP
================ ============= ========== ==============================================

Example YAML Output
~~~~~~~~~~~~~~~~~~~

::

    {'SKYCONT': 
         {'ARM': 'r', 'EXPID': '00000006', 'QATIME': '2016-07-08T06:05:34.56', 'PANAME': 'APPLY_FIBERFLAT', 'SPECTROGRAPH': 0,
          'VALUE': 
              {'SUMCOUNT': array([ 1500.0,  1400.0, ....]),
	       'SUMCOUNT_RMS': 1445.0,
	       'SUMCOUNT_RMS_SKY': 1455.0,
	       'SUMCOUNT_RMS_AMP': array([ 1444.0, 1433.0, 1422.0, 1411.0])
              }
         }
    }
