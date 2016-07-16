============================
qa-int-CAMERA-EXPID.yaml
============================

:Summary: This QA for QuickLook includes the calculation of the total
        number of counts on standard star fibers..
:Naming Convention: ``qa-int-{ARM}{SPECTROGRAPH}-{EXPID}.yaml``, where 
        {ARM} is the 1-char arm name (r,b,z), {SPECTROGRAPH} indexes 
        CCDs 0-9 on that arm, and {EXPID} is the 8-digit exposure ID.  
        Together, {ARM}{SPECTROGRAPH} specify a {CAMERA}.
:Regex: ``qa-int-[brz][0-9]-[0-9]{8}\.yaml``
:File Type:  YAML


Inputs
======

Written by qa_quicklook.py, with Integrate_Spectra using:

- frame

Contents
========

========== ================ ==============================================
KEYNAME    Type             Contents
========== ================ ==============================================
INT        Py dictionary    integral counts calculation on star fibers
========== ================ ==============================================



Dictionary Contents
===================

KEYNAME = INT

Integral counts calculations for standard stars, and averaged over image and per AMP.

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
INTEGRAL	 5555.0        float[500] total counts per star fiber 
INT_AVG          5600.0        float      INTEGRAL averaged over stars in image
INT_AVG_AMP      5700.0        float[4]   INTEGRAL averaged over star spectra regions in each AMP
================ ============= ========== ==============================================

Example YAML Output
~~~~~~~~~~~~~~~~~~~

::

    {'INT': 
         {'ARM': 'r', 'EXPID': '00000006', 'QATIME': '2016-07-08T06:05:34.56', 'PANAME': 'SKYSUB', 'SPECTROGRAPH': 0,
          'VALUE': 
              {'INTEGRAL': array([ 5555.0, 5432.0, ... 5000.0]),
               'INT_AVG': 5600.0,
               'INT_AVG_AMP': array([ 5700.0, 5600.0, 5432.0, 5444.0])
              }
         }
    }
