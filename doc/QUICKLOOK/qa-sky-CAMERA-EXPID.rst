========================
qa-sky-CAMERA-EXPID.yaml
========================

:Summary: This QA for QuickLook first includes the calculation of 
        signal-to-noise in the spectrum after sky subtraction. 
:Naming Convention: ``qa-sky-{ARM}{SPECTROGRAPH}-{EXPID}.yaml``, where 
        {ARM} is the 1-char arm name (r,b,z), {SPECTROGRAPH} indexes 
        CCDs 0-9 on that arm, and {EXPID} is the 8-digit exposure ID.  
        Together, {ARM}{SPECTROGRAPH} specify a {CAMERA}.
:Regex: ``qa-sky-[brz][0-9]-[0-9]{8}\.yaml``
:File Type:  YAML


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

=============== ============= ========== =======================================
KEY             Example Value Type       Comment
=============== ============= ========== =======================================
ARM             r             char       Spectrograph arm b,r,z
SPECTROGRAPH    0             int        Camera index 0..9
EXPID           00000002      int        exposure ID
PANAME          SKYSUB        string     name of preceding PA
QATIME           2016-07-08T   float      timestamp (UTC) of time of QA execution
                 06:05:34.555
MEDIAN_SNR      1.3233        float[500] median S/N per fiber
MEDIAN_AMP_SNR	1.7905	      float[4]   median S/N averaged over each amplifier
=============== ============= ========== =======================================

Example YAML Output (10 spectra)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    {'SNR': 
         {'ARM': 'r', 'EXPID': '00000006', 'QATIME': '2016-07-08T06:05:34.56', 'PANAME': 'SKYSUB', 'SPECTROGRAPH': 0,
          'VALUE': 
             {'MEDIAN_AMP_SNR': array([ 11.28466596,   0.        ,  13.18927372,   0.        ]),
              'MEDIAN_SNR': array([ 26.29012459,  35.02498105,   3.30635973,   7.69106173,
                    0.586899  ,   3.59830798,  11.75768833,   8.276959  ,  16.70907383,   4.82177165])
             }
         }
     }
