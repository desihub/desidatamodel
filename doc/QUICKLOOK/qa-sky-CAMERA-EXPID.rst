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

=============== ============= ========== ============
KEY                                   Example Value           Type                     Comment
=============== ============= ========== ============
ARM                                  r                                char                        Spectrograph arm b,r,z
SPECTROGRAPH                0                                int                       Camera index 0..9
EXPID                                00000002                  int                      exposure ID
QANAME		                 SNR                           string                  name of QA algorithm
PANAME                            SKYSUB                     string                    name of preceding PA
TIMESTAMP                       12.1012                    float                     time of processing in hrs UTC
TOTAL_SNR                      44.484                      float[500]              summed S/N per fiber 
MEDIAN_SNR                    1.3233                      float[500]              median S/N per fiber
TOT_AMP_SNR	                 382.74	                  float[4]                 summed S/N averaged over each amplifier
MEDIAN_AMP_SNR	         1.7905	                  float[4]                 median S/N averaged over each amplifier
=============== ============= ========== ============

Example YAML Output (10 spectra)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    {'SNR': 
        {'EXPID': '00000002', 'SPECTROGRAPH': 0, 'ARM': 'r', 'PANAME': 'SKYSUB', 'TIMESTAMP': 12.1012, 
         'VALUE': 
             {'MED_AMP_SNR': array([ 1.79059346,  1.62490338,  0.        ,  0.        ]), 
 	      'TOT_SNR': array([  69.310733  ,   44.4842588 ,   60.21988334,   43.65503276,
         	   467.18695762,   45.44668542,   46.36697513,   37.60920791,
         	   31.38649155,   93.10937231]), 
 	      'TOT_AMP_SNR': array([ 382.73581891,  433.98941406,    0.        ,    0.        ]), 
 	      'MED_SNR': array([ 1.32332343,  1.15160778,  1.37505349,  1.46805151,  8.56809804,
        	   1.38577165,  1.32318437,  1.4029771 ,  1.15329144,  1.3964762 ])
	     }
         }
     }
