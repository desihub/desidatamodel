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
PANAME           FIBERFLAT     string     name of pipeline algorihm
QATIME           2016-07-08T   float      timestamp (UTC) of time of QA execution
                 06:05:34.555
SKYCONT          210.0         float      sky continuum in all configured continuum areas averaged over all sky fibers
SKYCONT_FIBER    357.238       float[n]   sky continuum per sky fiber averaged over two continuum regions, 'n' is number of sky fibers
SKYFIBERID       4             int[n]     FIBERID of sky fibers 
SKYCONT_AMP      199.12        float[4]   sky continuum per amp averaged over all overlaying sky fibers
================ ============= ========== ==============================================

Example YAML Output
~~~~~~~~~~~~~~~~~~~

::

    {'SKYCONT': 
         {'ARM': 'r', 'EXPID': '00000006', 'QATIME': '2016-07-08T06:05:34.56', 'PANAME': 'APPLY_FIBERFLAT', 'SPECTROGRAPH': 0,
          'VALUE': 
              {'SKYCONT': 359.70078667259668,
               'SKYCONT_AMP': array([ 374.19163643,    0.        ,  344.76184662,    0.        ]),
               'SKYCONT_FIBER': [357.23814787655738,   358.14982775192709,   359.34380640332847,   361.55526717275529,
                    360.46690568746544,   360.49561926858325,   359.08761654248656,   361.26910267767016],
               'SKYFIBERID': [4, 19, 30, 38, 54, 55, 57, 62]
              }
         }
    }
