=============================
qa-countpix-CAMERA-EXPID.yaml
=============================

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

========== ================ ================================
KEYNAME    Type             Contents
========== ================ ================================
COUNTPIX   Py dictionary    Number of pixels above threshold
========== ================ ================================



Dictionary Contents
===================

KEYNAME = COUNTPIX

Integral counts of pixels above three thresholds per image and per CCD amp.

Keyword Description
~~~~~~~~~~~~~~~~~~~

================ ============= ========== ==================================================
KEY              Example Value Type       Comment
================ ============= ========== ==================================================
ARM              r             char       Spectrograph arm b,r,z
SPECTROGRAPH     0             int  	  Camera index 0..9
EXPID            00000002      int  	  exposure ID
PANAME           PREPROC       string     name of pipeline algorihm
QATIME           2016-07-08T   float      timestamp (UTC) of time of QA execution
                 06:05:34.555
NPIX3SIG         1000          int        number of pixels above 3 sigma
NPIX3SIG_AMP     900           int[4]     number of pixelsabove 3 sigma over each amplifier
NPIX100          100           int        number of pixels above 100 counts
NPIX100_AMP      90            int[4]     number of pixels above 100 over each amplifier
NPIX500          20            int        number of pixels above 500 counts
NPIX500_AMP      20            int[4]     number of pixelsabove 500 over each amplifier
================ ============= ========== ==================================================

Example YAML Output
~~~~~~~~~~~~~~~~~~~

::

    {'COUNTPIX': 
         {'ARM': 'r', 'EXPID': '00000006', 'QATIME': '2016-07-08T06:05:34.56', 'PANAME': 'PREPROC', 'SPECTROGRAPH': 0,
          'VALUE':
              {'NPIX100': 0,
               'NPIX100_AMP': [254549, 0, 242623, 0],
               'NPIX3SIG': 3713,
               'NPIX3SIG_AMP': [128158, 2949, 132594, 3713],
               'NPIX500': 0,
               'NPIX500_AMP': [1566, 0, 1017, 0]
              }
         }
    }
