===================
Datamodel: fibermap
===================

General Description
===================

Summary
-------

The fibermap contains the fiber positioner configuration information for
each exposure: what fiber is placed where, what target that is, etc.


Naming Convention
-----------------

``fibermap-{EXPID}.fits``, where {EXPID} is the 8-digit exposure ID.

regex: ``fibermap-[0-9]{8}.fits``

File Type
---------

FITS, 1 MB

Contents
========

====== ======== ======== ===================
Number EXTNAME  Type     Contents           
====== ======== ======== ===================
HDU0_           IMAGE    Blank
HDU1_  FIBERMAP BINTABLE Fiber map table
====== ======== ======== ===================


FITS Header Units
=================

HDU0
----

Blank; this HDU has no non-standard required keywords.

HDU1
----

The fiber map table.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== =================== ===== =============================
KEY      Example Value       Type  Comment                      
======== =================== ===== =============================
TILEID   0                   int   Tile ID                      
TELERA   0.0                 float Telescope central RA [deg]   
TELEDEC  0.0                 float Telescope central dec [deg]  
EXPID    2                   int   Exposure number              
NIGHT    20150107            str   Night YEARMMDD               
VDMODEL  0.0.0               str   TODO: desimodel version      
VOPTICS  0.0.0               str   TODO: optics model version   
VFIBVCAM 0.0.0               str   TODO: fiber view code version
HEXPDROT 0.0                 float TODO: hexapod rotation [deg] 
DATE-OBS 2015-01-08T18:46:58 str   Date of observation in UTC   
EXTNAME  FIBERMAP            str   extension name               
======== =================== ===== =============================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

============ ========== ===== ===============================================
Name         Type       Units Description                                    
============ ========== ===== ===============================================
OBJTYPE      char[10]         Target type [ELG, LRG, QSO, STD, STAR, SKY]    
TARGETCAT    char[20]         Name/version of the target catalog             
TARGETID     int64            Unique target ID                               
TARGET_MASK0 int64            Targeting bit mask                             
MAG          float32[5]       magitude                                       
FILTER       char[50]         SDSS_R, DECAM_Z, WISE1, etc.                   
SPECTROID    int64            Spectrograph ID [0-9]                          
POSITIONER   int64            Positioner ID [0-4999]                         
FIBER        int32            Fiber ID [0-4999]                              
LAMBDAREF    float32          Reference wavelength at which to align fiber   
RA_TARGET    float64          Target right ascension [degrees]               
DEC_TARGET   float64          Target declination [degrees]                   
RA_OBS       float64          RA of obs from (X,Y)_FVCOBS and optics [deg]   
DEC_OBS      float64          dec of obs from (X,Y)_FVCOBS and optics [deg]  
X_TARGET     float64          X on focal plane derived from (RA,DEC)_TARGET  
Y_TARGET     float64          Y on focal plane derived from (RA,DEC)_TARGET  
X_FVCOBS     float64          X location observed by Fiber View Cam [mm]     
Y_FVCOBS     float64          Y location observed by Fiber View Cam [mm]     
Y_FVCERR     float32          Y location uncertainty from Fiber View Cam [mm]
X_FVCERR     float32          X location uncertainty from Fiber View Cam [mm]
============ ========== ===== ===============================================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*

