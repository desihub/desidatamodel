==================
Datamodel: simspec
==================

General Description
===================

Summary
-------

Input spectra to simulate with pixsim.

Naming Convention
-----------------

``simspec-{EXPID}.fits``, where {EXPID} is the 8-digit exposure ID.

regex: ``simspec-[0-9]{8}.fits``

File Type
---------

FITS, 2 GB

Contents
========

====== ========= ======== ===================
Number EXTNAME   Type     Contents           
====== ========= ======== ===================
HDU0_  FLUX      IMAGE    Input object flux
HDU1_  SKYFLUX   IMAGE    Input sky flux
HDU2_  METADATA  BINTABLE Metadata about the input spectra
HDU3_  PHOT_B    IMAGE    Input object photons b-channel
HDU4_  SKYPHOT_B IMAGE    Input sky photons b-channel
HDU5_  PHOT_R    IMAGE    Input object photons r-channel
HDU6_  SKYPHOT_R IMAGE    Input sky photons r-channel
HDU7_  PHOT_Z    IMAGE    Input object photons z-channel
HDU6_  SKYPHOT_Z IMAGE    Input sky photons z-channel
====== ========= ======== ===================


FITS Header Units
=================

HDU0
----

Input object flux.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======== ===== ==================================
KEY      Value    Type  Comment                           
======== ======== ===== ==================================
CRVAL1   3533.0   float Starting wavelength [Angstroms]   
CDELT1   0.2      float Wavelength step [Angstroms]       
AIRORVAC vac      str   Vacuum wavelengths                
LOGLAM   0        int   linear wavelength steps, not log10
EXTNAME  FLUX     str   Object flux [erg/s/cm2/A]         
======== ======== ===== ==================================

HDU1
----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======== ===== ==================================
KEY      Value    Type  Comment                           
======== ======== ===== ==================================
CRVAL1   3533.0   float Starting wavelength [Angstroms]   
CDELT1   0.2      float Wavelength step [Angstroms]       
AIRORVAC vac      str   Vacuum wavelengths                
LOGLAM   0        int   linear wavelength steps, not log10
EXTNAME  SKYFLUX  str   Sky flux [erg/s/cm2/A/arcsec2]    
======== ======== ===== ==================================

Data: FITS image

HDU2
----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ======== ==== ==============
KEY     Value    Type Comment       
======= ======== ==== ==============
EXTNAME METADATA str  extension name
======= ======== ==== ==============

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

========== ======== ========= ======================================
Name       Type     Units     Description                           
========== ======== ========= ======================================
OBJTYPE    char[10]           Object type (ELG, LRG, QSO, STD, STAR)
REDSHIFT   float32            true object redshift                  
TEMPLATEID int32              input template ID                     
O2FLUX     float32  erg/s/cm2 [OII] flux [erg/s/cm2]                
========== ======== ========= ======================================

HDU3
----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======== ===== ==================================
KEY      Value    Type  Comment                           
======== ======== ===== ==================================
CRVAL1   3533.0   float Starting wavelength [Angstroms]   
CDELT1   0.2      float Wavelength step [Angstroms]       
AIRORVAC vac      str   Vacuum wavelengths                
LOGLAM   0        int   linear wavelength steps, not log10
EXTNAME  PHOT_B   str   B channel object photons per bin  
======== ======== ===== ==================================

Data: FITS image

HDU4
----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========= ===== ==================================
KEY      Value     Type  Comment                           
======== ========= ===== ==================================
CRVAL1   3533.0    float Starting wavelength [Angstroms]   
CDELT1   0.2       float Wavelength step [Angstroms]       
AIRORVAC vac       str   Vacuum wavelengths                
LOGLAM   0         int   linear wavelength steps, not log10
EXTNAME  SKYPHOT_B str   B channel sky photons per bin     
======== ========= ===== ==================================

Data: FITS image

HDU5
----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======== ===== ==================================
KEY      Value    Type  Comment                           
======== ======== ===== ==================================
CRVAL1   5564.2   float Starting wavelength [Angstroms]   
CDELT1   0.2      float Wavelength step [Angstroms]       
AIRORVAC vac      str   Vacuum wavelengths                
LOGLAM   0        int   linear wavelength steps, not log10
EXTNAME  PHOT_R   str   R channel object photons per bin  
======== ======== ===== ==================================

Data: FITS image

HDU6
----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========= ===== ==================================
KEY      Value     Type  Comment                           
======== ========= ===== ==================================
CRVAL1   5564.2    float Starting wavelength [Angstroms]   
CDELT1   0.2       float Wavelength step [Angstroms]       
AIRORVAC vac       str   Vacuum wavelengths                
LOGLAM   0         int   linear wavelength steps, not log10
EXTNAME  SKYPHOT_R str   R channel sky photons per bin     
======== ========= ===== ==================================

Data: FITS image

HDU7
----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======== ===== ==================================
KEY      Value    Type  Comment                           
======== ======== ===== ==================================
CRVAL1   7360.2   float Starting wavelength [Angstroms]   
CDELT1   0.2      float Wavelength step [Angstroms]       
AIRORVAC vac      str   Vacuum wavelengths                
LOGLAM   0        int   linear wavelength steps, not log10
EXTNAME  PHOT_Z   str   Z channel object photons per bin  
======== ======== ===== ==================================

Data: FITS image

HDU8
----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========= ===== ==================================
KEY      Value     Type  Comment                           
======== ========= ===== ==================================
CRVAL1   7360.2    float Starting wavelength [Angstroms]   
CDELT1   0.2       float Wavelength step [Angstroms]       
AIRORVAC vac       str   Vacuum wavelengths                
LOGLAM   0         int   linear wavelength steps, not log10
EXTNAME  SKYPHOT_Z str   Z channel sky photons per bin     
======== ========= ===== ==================================

Data: FITS image


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*

