========================
qa-countpix-CAMERA-EXPID.yaml
========================

:Summary: This QA for QuickLook includes the calculation of the number of
        pixels above three thresholds in the 2-D pix file after the preprocessing stage. 
:Naming Convention: ``qa-countpix-{ARM}{SPECTROGRAPH}-{EXPID}.yaml``, where 
        {ARM} is the 1-char arm name (r,b,z), {SPECTROGRAPH} indexes 
        CCDs 0-9 on that arm, and {EXPID} is the 8-digit exposure ID.  
        Together, {ARM}{SPECTROGRAPH} specify a {CAMERA}.
:Regex: ``qa-countpix-[brz][0-9]-[0-9]{8}\.yaml``
:File Type:  YAML


Inputs
======

Written by qa_quicklook.py, with Count_Pixels using:

- pix 2D file

Contents
========

========== ================ ===========================
KEYNAME     Type                 Contents
========== ================ ===========================
COUNTPIX        Py dictionary    Number of pixels above threshold
========== ================ ===========================



Dictionary Contents
===================

KEYNAME = COUNTPIX

Integral counts of pixels above three thresholds per image and per CCD amp.

Keyword Description
~~~~~~~~~~~~~~~~~~~

================ ============= ========== ============
KEY              Example Value Type       Comment
================ ============= ========== ============
ARM              r             char       Spectrograph arm b,r,z
SPECTROGRAPH     0             int  	  Camera index 0..9
EXPID            00000002      int  	  exposure ID
QANAME		 COUNTPIX           string     name of QA algorithm
PANAME            PREPROC         string     name of pipeline algorihm
TIMESTAMP       12.01234        float       time in hours of the day (UTC) of QA execution
NPIX3SIG                   1000                int      number of pixels above 3 sigma
NPIX3SIG_AMP           900               int[4]    number of pixelsabove 3 sigma over each amplifier
NPIX100                   100                int      number of pixels above 100 counts
NPIX100_AMP           90               int[4]    number of pixels above 100 over each amplifier
NPIX500                   20                int      number of pixels above 500 counts
NPIX500_AMP           20               int[4]    number of pixelsabove 500 over each amplifier
================ ============= ========== ============

Example YAML Output
~~~~~~~~~~~~~~~~~~

::

    {'COUNTPIX': 
        {'EXPID': '00000002', 'SPECTROGRAPH': 0, 'ARM': 'r', 'PANAME': 'PREPROC', 'TIMESTAMP', 12.0123, 
         'VALUE': 
             {'NPIX3SIG': 1000,
	      'NPIX3SIG_AMP': array([900, 1100, 0., 0. ])
	      'NPIX100': 100,
	      'NPIX100_AMP': array([90, 110, 0., 0. ])
	      'NPIX500': 20,
	      'NPIX500_AMP': array([20, 20, 0., 0. ])
	      }
         }
     }
