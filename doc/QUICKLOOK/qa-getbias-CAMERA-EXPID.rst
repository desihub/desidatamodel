============================
qa-getbias-CAMERA-EXPID.yaml
============================

:Summary: This QA for QuickLook includes the calculation of the bias
	  in the CCD overscan region.
:Naming Convention: ``qa-getbias-{ARM}{SPECTROGRAPH}-{EXPID}.yaml``, where 
        {ARM} is the 1-char arm name (r,b,z), {SPECTROGRAPH} indexes 
        CCDs 0-9 on that arm, and {EXPID} is the 8-digit exposure ID.  
        Together, {ARM}{SPECTROGRAPH} specify a {CAMERA}.
:Regex: ``qa-getbias-[brz][0-9]-[0-9]{8}\.yaml``
:File Type:  YAML


Inputs
======

Written by qa_quicklook.py, with Bias_From_Overscan using:

- pix 2D file

Contents
========

========== ================ =====================================
KEYNAME    Type             Contents
========== ================ =====================================
GETBIAS    Py dictionary    bias calculated from overscan region
========== ================ =====================================



Dictionary Contents
===================

KEYNAME = GETBIAS

Bias calculations per image and per CCD amp.

Keyword Description
~~~~~~~~~~~~~~~~~~~

================ ============= ========== ==============================================
KEY              Example Value Type       Comment
================ ============= ========== ==============================================
ARM              r             char       Spectrograph arm b,r,z
SPECTROGRAPH     0             int  	  Camera index 0..9
EXPID            00000002      int  	  exposure ID
QANAME		 GETBIAS       string     name of QA algorithm
PANAME           PREPROC       string     name of pipeline algorihm
TIMESTAMP        12.01234      float      time in hours of the day (UTC) of QA execution
BIAS             10.0          float      value of bias across image
BIAS_AMP         9.12          float[4]   value of bias averaged over each amplifier
================ ============= ========== ==============================================

Example YAML Output
~~~~~~~~~~~~~~~~~~~

::

    {'GETBIAS': 
        {'EXPID': '00000002', 'SPECTROGRAPH': 0, 'ARM': 'r', 'PANAME': 'PREPROC', 'TIMESTAMP', 12.0123, 
         'VALUE': 
             {'BIAS': 10.0,
	      'BIAS_AMP': array([9.12, 10.88, 0., 0. ])
	     }
         }
     }
