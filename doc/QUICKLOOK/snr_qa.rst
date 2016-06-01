==============
desi-QL_SNR_QA
==============

:Summary: This QA for QuickLook first includes the calculation of 
        signal-to-noise in the spectrum after sky subtraction. 
:Naming Convention: ``qa-{ARM}{SPECTROGRAPH}-{EXPID}.yaml``, where 
        {ARM} is the 1-char arm name (r,b,z), {SPECTROGRAPH} indexes 
        CCDs 0-9 on that arm, and {EXPID} is the 8-digit exposure ID.
:Regex: ``qa-[brz][0-9]-[0-9]{8}\.yaml``
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



FITS Header Units
=================

KEYNAME = SNR

Spectral signal-to-noise calculations per fiber and per CCD amp.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

================ ============= ========== ============
KEY              Example Value Type       Comment
================ ============= ========== ============
ARM              r             char       Spectrograph arm b,r,z
SPECTROGRAPH     0             int  	  Camera index 0..9
EXPID            00000002      int  	  exposure ID
QANAME		 SNR           string
TOTAL_SNR        40            float[500] summed S/N per fiber 
MEDIAN_SNR       1.5           float[500] median S/N per fiber
TOT_AMP_SNR	 40	       float[4]   summed S/N averaged over each amplifier
MEDIAN_AMP_SNR	 1.5	       float[4]   median S/N averaged over each amplifier
================ ============= ========== ============




