============================
qa-skycont-CAMERA-EXPID.yaml
============================

:Summary: This QA for QuickLook includes the calculation of the sky
	  continuum level in sky fibers.
:Naming Convention: ``qa-skycont-{ARM}{SPECTROGRAPH}-{EXPID}.yaml``, where 
        {ARM} is the 1-char arm name (r,b,z), {SPECTROGRAPH} indexes 
        CCDs 0-9 on that arm, and {EXPID} is the 8-digit exposure ID.  
        Together, {ARM}{SPECTROGRAPH} specify a {CAMERA}.
:Regex: ``qa-skycont-[brz][0-9]-[0-9]{8}\.yaml``
:File Type:  YAML


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

================ ============= ========== ==============================================
KEY              Example Value Type       Comment
================ ============= ========== ==============================================
ARM              r             char       Spectrograph arm b,r,z
SPECTROGRAPH     0             int  	  Camera index 0..9
EXPID            00000002      int  	  exposure ID
QANAME		 SKYCONT       string     name of QA algorithm
PANAME           FIBERFLAT     string     name of pipeline algorihm
TIMESTAMP        12.01234      float      time in hours of the day (UTC) of QA execution
SKY              210.0         float      value of bias across image
SKY_AMP          199.12        float[4]   value of bias averaged over each amplifier
================ ============= ========== ==============================================

Example YAML Output
~~~~~~~~~~~~~~~~~~~

::

    {'SKYCONT': 
        {'EXPID': '00000002', 'SPECTROGRAPH': 0, 'ARM': 'r', 'PANAME': 'FIBERFLAT', 'TIMESTAMP', 12.0123, 
         'VALUE': 
             {'SKY': 210.0,
	      'SKY_AMP': array([199.12, 210.88, 0., 0. ])
	     }
         }
     }
