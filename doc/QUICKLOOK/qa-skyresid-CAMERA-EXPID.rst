============================
qa-skyresid-CAMERA-EXPID.yaml
============================

:Summary: This QA for QuickLook includes the calculation of the sky
	  continuum level in sky fibers.
:Naming Convention: ``qa-skyresid-{ARM}{SPECTROGRAPH}-{EXPID}.yaml``, where 
        {ARM} is the 1-char arm name (r,b,z), {SPECTROGRAPH} indexes 
        CCDs 0-9 on that arm, and {EXPID} is the 8-digit exposure ID.  
        Together, {ARM}{SPECTROGRAPH} specify a {CAMERA}.
:Regex: ``qa-skyresid-[brz][0-9]-[0-9]{8}\.yaml``
:File Type:  YAML


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

================ ============= ================ ================================================
KEY              Example Value Type             Comment
================ ============= ================ ================================================
ARM              r             char       	Spectrograph arm b,r,z
SPECTROGRAPH     0             int  	  	Camera index 0..9
EXPID            00000002      int  	  	exposure ID
PANAME           FIBERFLAT     string     	name of pipeline algorihm
QATIME           2016-07-08T   float      	timestamp (UTC) of time of QA execution
                 06:05:34.555
MED_RESID	 0.786	       float      	median of residuals over all sky fibers
MED_RESID_FIBER  0.548..0.001  float[NSKY_FIB]  median of residuals per sky fiber
MED_RESID_WAVE   0.426..0.371  float[NWAVE]     median of residuals vs. wavelength in NWAVE bins
NBAD_PCHI        0	       int		number of fibers with bad chi^2
NREJ		 0             int              number of rejected fibers
NSKY_FIB         34	       int              number of good sky fibers
RESID_PER	 -28.83, 31.75 float[2]         95% c.l. boundaries of residuals distribution
WAVELENGTH	 5630...7740.  float[NWAVE]     wavelength (Ang.) in NWAVE bins
================ ============= ================ ==============================================

Example YAML Output
~~~~~~~~~~~~~~~~~~~

::

    {'SKYCONT': 
         {'ARM': 'r', 'EXPID': '00000006', 'QATIME': '2016-07-08T06:05:34.56', 'PANAME': 'APPLY_FIBERFLAT', 'SPECTROGRAPH': 0,
          'VALUE': 
	      {'MED_RESID': 0.786,
               'MED_RESID_FIBER': array([  5.47905858e-01,   1.08058461e-03,...-5.44937745e-01]),
               'MED_RESID_WAVE': array([ 0.42623056,  0.3707578 , ..., 1.57167314]),
  	       'NBAD_PCHI': 0,
   	       'NREJ': 0,
   	       'NSKY_FIB': 34,
   	       'RESID_PER': [-28.832766714800194, 31.747264536151032],
   	       'WAVELENGTH': array([ 5630.,  5631.,  5632., ...,  7738.,  7739.,  7740.])
              }
         }
    }
