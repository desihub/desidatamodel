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
PANAME           PREPROC       string     name of pipeline algorihm
MJD              57578.78099   float      Modified Julian Date (JD-2400000.5) in days of the time of QA execution
BIAS             10.0          float      value of bias across image
BIAS_AMP         9.12          float[4]   value of bias averaged over each amplifier
================ ============= ========== ==============================================

Example YAML Output
~~~~~~~~~~~~~~~~~~~

::

    {'GETBIAS': 
        {'ARM': 'r', 'EXPID': '00000006', 'MJD': 57578.780704701225, 'PANAME': 'PREPROC', 'SPECTROGRAPH': 0,
         'VALUE': 
             {'BIAS': -0.0080487558302569373,
              'BIAS_AMP': array([-0.01132324, -0.02867701, -0.00277266,  0.0105779 ])
             }
        }
    }
