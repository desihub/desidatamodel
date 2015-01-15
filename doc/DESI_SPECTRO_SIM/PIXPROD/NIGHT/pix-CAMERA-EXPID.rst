==============
pix
==============

General Description
===================

Summary
-------

Pre-processed CCD pixel data.

Naming Convention
-----------------

``pix-{CAMERA}-{EXPID}.fits``, where {CAMERA} is the camera name
(e.g. b0, r1, or z9), and {EXPID} is the 8-digit exposure ID.

regex: ``pix-[brz]{1}[0-9]{1}-[0-9]{8}.fits``

File Type
---------

FITS, 320 MB

Contents
========

====== ======= ===== ===================
Number EXTNAME Type  Contents           
====== ======= ===== ===================
HDU0_          IMAGE Pre-processed electrons
HDU1_  IVAR    IMAGE Inverse variance [1/electrons^2]
HDU1_  MASK    IMAGE Mask 0=good, non-0 is bad
====== ======= ===== ===================


FITS Header Units
=================

HDU0 - ELECTRONS
----------------

Bias subtracted, pixel flat fielded, gain corrected CCD image in electrons.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============= ===== ==================================
KEY      Example Value Type  Comment                           
======== ============= ===== ==================================
CAMERA   b0            str   Spectograph Camera                
VSPECTER 0.0.0         str   TODO: Specter version             
EXPTIME  1000.0        float Exposure time [sec]               
RDNOISE  3.0           float Read noise [electrons]            
FLAVOR   arc           str   Exposure type (arc, flat, science)
======== ============= ===== ==================================

Data: FITS image

HDU1 - IVAR
-----------

Inverse variance image of the electron image in HDU 0

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ======== ===== ======================
KEY     Value    Type  Comment               
======= ======== ===== ======================
EXTNAME IVAR     str   extension name        
RDNOISE 3.0      float Read noise [electrons]
======= ======== ===== ======================

Data: FITS image

HDU2
----

Mask image, where 0=good, non-0=bad.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ======== ==== ==============
KEY     Value    Type Comment       
======= ======== ==== ==============
EXTNAME MASK     str  extension name
======= ======== ==== ==============

Data: FITS image


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*

