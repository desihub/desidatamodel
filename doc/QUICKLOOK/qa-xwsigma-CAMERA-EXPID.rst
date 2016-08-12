============================
qa-xwsigma-CAMERA-EXPID.yaml
============================

:Summary: This QA for QuickLook includes the calculation of the X and W
          sigmas from the 2D image file.
:Naming Convention: ``qa-xwsigma-{ARM}{SPECTROGRAPH}-{EXPID}.yaml``, where 
        {ARM} is the 1-char arm name (r,b,z), {SPECTROGRAPH} indexes 
        CCDs 0-9 on that arm, and {EXPID} is the 8-digit exposure ID.  
        Together, {ARM}{SPECTROGRAPH} specify a {CAMERA}.
:Regex: ``qa-xwsigma-[brz][0-9]-[0-9]{8}\.yaml``
:File Type:  YAML


Inputs
======

Written by qa_quicklook.py, with Calc_XWSigma using:

- pix image
- psfboot

Contents
========

========== ================ ==============================================
KEYNAME    Type             Contents
========== ================ ==============================================
XWSIGMA    Py dictionary    sigma calculation at peak sky wavelengths
========== ================ ==============================================



Dictionary Contents
===================

KEYNAME = XWSIGMA

Calculation of standard deviation of Gaussian fit to X and W (i.e. 'wavelength')
profiles at peak sky wavelengths.  


Keyword Description
~~~~~~~~~~~~~~~~~~~

================ ============= ========== ==============================================
KEY              Example Value Type       Comment
================ ============= ========== ==============================================
ARM              r             char       Spectrograph arm b,r,z
SPECTROGRAPH     0             int  	  Camera index 0..9
EXPID            00000002      int  	  exposure ID
PANAME           PREPROC       string     name of pipeline algorihm
QATIME           2016-07-08T   float      timestamp (UTC) of time of QA execution
                 06:05:34.555
XSIGMA		 1.9           float[500] fitted XSIGMA averaged over isolated bright 
                                          sky wavelengths
XSIGMA_MED       1.81          float      median of XSIGMAs for all fibers
XSIGMA_MED_SKY   1.72          float      median of XSIGMAs for sky fibers
XSIGMA_AMP       1.9           float[4]   median of XSIGMAs for all fibers per amp
WSIGMA           1.9           float[500] fitted WSIGMA averaged over isolated bright 
                                          sky wavelengths
WSIGMA_MED       1.81          float      median of WSIGMAs for all fibers
WSIGMA_MED_SKY   1.72          float      median of WSIGMAs for sky fibers
WSIGMA_AMP       1.9           float[4]   median of WSIGMAs for all fibers per amp
================ ============= ========== ==============================================

Example YAML Output
~~~~~~~~~~~~~~~~~~~

::

    {'XWSIGMA': 
         {'ARM': 'r', 'EXPID': '00000006', 'QATIME': '2016-07-08T06:05:34.56', 'PANAME': 'PREPROC', 'SPECTROGRAPH': 0,
          'VALUE': 
              {'XSIGMA': array([ 1.9, 1.81, 1.2...]),
               'XSIGMA_MED': 1.81,
	       'XSIGMA_MED_SKY': 1.72,
	       'XSIGMA_AMP': array([ 1.9, 1.8, 1.7, 1.84]),
               'WSIGMA': array([ 1.9, 1.81, 1.2...]),
               'WSIGMA_MED': 1.81,
               'WSIGMA_MED_SKY': 1.72,
               'WSIGMA_AMP': array([ 1.9, 1.8, 1.7, 1.84]),
              }
         }
    }
