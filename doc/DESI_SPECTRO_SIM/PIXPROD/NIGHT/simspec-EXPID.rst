==================
simspec
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

====== ========= ======== ================================
Number EXTNAME   Type     Contents           
====== ========= ======== ================================
HDU0_  PRIMARY   PRIMARY  Simulation inputs
HDU1_  WAVE      IMAGE    Input wavelength vector
HDU2_  FLUX      IMAGE    Input object spectra
HDU3_  SKYFLUX   IMAGE    Input sky flux
HDU4_  WAVE_B    IMAGE    Input wavelengths b-channel
HDU5_  PHOT_B    IMAGE    Input object photons b-channel
HDU6_  SKYPHOT_B IMAGE    Input sky photons b-channel
HDU7_  WAVE_R    IMAGE    Input wavelengths r-channel
HDU8_  PHOT_R    IMAGE    Input object photons r-channel
HDU9_  SKYPHOT_R IMAGE    Input sky photons r-channel
HDU10_ WAVE_Z    IMAGE    Input wavelengths z-channel
HDU11_ PHOT_Z    IMAGE    Input object photons z-channel
HDU12_ SKYPHOT_Z IMAGE    Input sky photons z-channel
HDU13_ METADATA  BINTABLE Metadata about the input spectra
====== ========= ======== ================================

FITS Header Units
=================

HDU0
----

Simulation inputs as header cards.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== =================== ===== ==========================================
KEY      Value               Type  Comment                           
======== =================== ===== ==========================================
NIGHT    YYYYMMDD            str   Night of observation
AIRMASS  1.0                 float Airmass at middle of exposure
TILEID   1                   int   DESI tile ID
EXPID    0                   int   DESI exposure ID
TELRA    0.0                 float Telescope pointing RA [degrees]
EXPTIME  1000.0              float Exposure time [sec]
PROGRAM  dark                str   Program name
TELDEC   0.0                 float Telescope pointing Dec [degrees]
DATE-OBS 2017-06-15T22:00:00 str   Start of exposure
FLAVOR   science             str   Flavor of observation (arc, flat, science)
DOSVER   SIM                 str   ???
======== =================== ===== ==========================================

Data: None

HDU1
----

Input wavelength vector.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======== ===== ==================
KEY      Value    Type  Comment                           
======== ======== ===== ==================
BUNIT    Angstrom str   Wavelength unit
AIRORVAC vac      str   Vacuum wavelengths                
EXTNAME  WAVE     str   Extension name
======== ======== ===== ==================

Data: FITS image

HDU2
----

Input object spectra.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================= ===== ==============
KEY      Value             Type  Comment                           
======== ================= ===== ==============
BUNIT    1e-17 erg/s/cm2/A str   Flux unit 
EXTNAME  FLUX              str   Extension name
======== ================= ===== ==============

Data: FITS image

HDU3
----

Input sky flux.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================= ===== ==============
KEY      Value             Type  Comment                           
======== ================= ===== ==============
BUNIT    1e-17 erg/s/cm2/A str   Flux unit 
EXTNAME  SKYFLUX           str   Extension name
======== ================= ===== ==============

Data: FITS image

HDU4
----

Input wavelengths b-channel.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======== ===== ==================
KEY      Value    Type  Comment                           
======== ======== ===== ==================
BUNIT    Angstrom str   Wavelength unit
AIRORVAC vac      str   Vacuum wavelengths                
EXTNAME  WAVE_B   str   Extension name
======== ======== ===== ==================

Data: FITS image

HDU5
----

Input object photons b-channel.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======== ===== ==============
KEY      Value    Type  Comment                           
======== ======== ===== ==============
EXTNAME  PHOT_B   str   Extension name
======== ======== ===== ==============

Data: FITS image

HDU6
----

Input object photons b-channel.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========= ===== ==============
KEY      Value     Type  Comment                           
======== ========= ===== ==============
EXTNAME  SKYPHOT_B str   Extension name
======== ========= ===== ==============

Data: FITS image

HDU7
----

Input wavelengths r-channel.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======== ===== ==================
KEY      Value    Type  Comment                           
======== ======== ===== ==================
BUNIT    Angstrom str   Wavelength unit
AIRORVAC vac      str   Vacuum wavelengths                
EXTNAME  WAVE_R   str   Extension name
======== ======== ===== ==================

Data: FITS image

HDU8
----

Input object photons r-channel.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======== ===== ==============
KEY      Value    Type  Comment                           
======== ======== ===== ==============
EXTNAME  PHOT_R   str   Extension name
======== ======== ===== ==============

Data: FITS image

HDU9
----

Input object photons r-channel.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========= ===== ==============
KEY      Value     Type  Comment                           
======== ========= ===== ==============
EXTNAME  SKYPHOT_R str   Extension name
======== ========= ===== ==============

Data: FITS image

HDU10
-----

Input wavelengths z-channel.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======== ===== ==================
KEY      Value    Type  Comment                           
======== ======== ===== ==================
BUNIT    Angstrom str   Wavelength unit
AIRORVAC vac      str   Vacuum wavelengths                
EXTNAME  WAVE_Z   str   Extension name
======== ======== ===== ==================

Data: FITS image

HDU11
-----

Input object photons z-channel.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======== ===== ==============
KEY      Value    Type  Comment                           
======== ======== ===== ==============
EXTNAME  PHOT_Z   str   Extension name
======== ======== ===== ==============

Data: FITS image

HDU12
-----

Input object photons z-channel.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========= ===== ==============
KEY      Value     Type  Comment                           
======== ========= ===== ==============
EXTNAME  SKYPHOT_Z str   Extension name
======== ========= ===== ==============

Data: FITS image

HDU13
-----

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ======== ==== ==============
KEY     Value    Type Comment       
======= ======== ==== ==============
EXTNAME METADATA str  extension name
======= ======== ==== ==============

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

========== ========== ========= =====================================
Name       Type       Units     Description                           
========== ========== ========= =====================================
OBJTYPE    char[10]             Object type (e.g., ELG, QSO, STD, WD)
SUBTYPE    char[10]             Subtype (e.g., LYA, DA, DB)
TEMPLATEID int32                Template ID
SEED       int64                Random seed
REDSHIFT   float32              True object redshift.
MAG        float32              True object magnitude.
DECAM_FLUX float32[6]           Synthesized DECam ugrizY nanomaggies
WISE_FLUX  float32[2]           Synthesized WISE W1, W2 nanomaggies
OIIFLUX    float32    erg/s/cm2 [OII] flux
HBETAFLUX  float32    erg/s/cm2 H-BETA flux
EWOII      float32    Angstrom  Rest-frame equivalent width of [OII]
EWHBETA    float32    Angstrom  Rest-frame equivalent width of H-beta
D4000      float32              4000-A break index
VDISP      float32    km/s      Stellar velocity dispersion
OIIDOUBLET float32              [OII] doublet ratio
OIIIHBETA  float32              [OIII]/H-beta flux ratio
OIIHBETA   float32              [OII]/H-beta flux ratio
NIIHBETA   float32              [NII]/H-beta flux ratio
SIIHBETA   float32              [SII]/H-beta flux ratio
ZMETAL     float32              Stellar metallicity of SSP
AGE        float32    Gyr       Age of SSP
TEFF       float32    K         Effective temperature
LOGG       float32    cm/s2     Surface gravity
FEH        float32              Iron abundance with respect to solar
========== ========== ========= =====================================

Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*

