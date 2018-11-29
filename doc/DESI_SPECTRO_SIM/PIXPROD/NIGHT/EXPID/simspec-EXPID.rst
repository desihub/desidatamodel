==================
simspec-EXPID.fits
==================

:Summary: Input spectra to simulate with pixsim.
:Naming Convention: ``simspec-{EXPID}.fits``, where {EXPID} is the 8-digit exposure ID.
:Regex: ``simspec-[0-9]{8}\.fits``
:File Type: FITS, 2 GB

Contents
========

====== ============= ======== ================================
Number EXTNAME       Type     Contents
====== ============= ======== ================================
HDU0_  WAVE          IMAGE    Input wavelength vector
HDU1_  FLUX          IMAGE    Input object spectra
HDU2_  SKYFLUX       IMAGE    Input sky flux
HDU3_  WAVE_B        IMAGE    Input wavelengths b-channel
HDU4_  PHOT_B        IMAGE    Input object photons b-channel
HDU5_  SKYPHOT_B     IMAGE    Input sky photons b-channel
HDU6_  WAVE_R        IMAGE    Input wavelengths r-channel
HDU7_  PHOT_R        IMAGE    Input object photons r-channel
HDU8_  SKYPHOT_R     IMAGE    Input sky photons r-channel
HDU9_  WAVE_Z        IMAGE    Input wavelengths z-channel
HDU10_ PHOT_Z        IMAGE    Input object photons z-channel
HDU11_ SKYPHOT_Z     IMAGE    Input sky photons z-channel
HDU12_ TRUTH         BINTABLE Metadata about the input spectra
HDU13_ FIBERMAP      BINTABLE Metadata about the input spectra
HDU14_ OBSCONDITIONS BINTABLE Metadata about the input spectra
HDU15_ TRUTH_BGS     BINTABLE Metadata about the input spectra
HDU16_ TRUTH_ELG     BINTABLE Metadata about the input spectra
HDU17_ TRUTH_STAR    BINTABLE Metadata about the input spectra
HDU18_ TRUTH_WD      BINTABLE Metadata about the input spectra
====== ============= ======== ================================

FITS Header Units
=================

HDU0
----

EXTNAME = WAVE

Input wavelength vector.  Simulation inputs are stored in header cards.

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
BUNIT    Angstrom            str   Wavelength unit
AIRORVAC vac                 str   Vacuum wavelengths
EXTNAME  WAVE                str   Extension name
======== =================== ===== ==========================================

Data: FITS image

HDU1
----

EXTNAME = FLUX

Input object spectra.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============================ ===== ==============
KEY      Value                        Type  Comment
======== ============================ ===== ==============
BUNIT    10**-17 erg/(s cm2 Angstrom) str   Flux unit
EXTNAME  FLUX                         str   Extension name
======== ============================ ===== ==============

Data: FITS image

HDU2
----

EXTNAME = SKYFLUX

Input sky flux.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============================ ===== ==============
KEY      Value                        Type  Comment
======== ============================ ===== ==============
BUNIT    10**-17 erg/(s cm2 Angstrom) str   Flux unit
EXTNAME  SKYFLUX                      str   Extension name
======== ============================ ===== ==============

Data: FITS image

HDU3
----

EXTNAME = WAVE_B

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

HDU4
----

EXTNAME = PHOT_B

Input object photons b-channel.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======== ===== ==============
KEY      Value    Type  Comment
======== ======== ===== ==============
EXTNAME  PHOT_B   str   Extension name
======== ======== ===== ==============

Data: FITS image

HDU5
----

EXTNAME = SKYPHOT_B

Input object photons b-channel.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========= ===== ==============
KEY      Value     Type  Comment
======== ========= ===== ==============
EXTNAME  SKYPHOT_B str   Extension name
======== ========= ===== ==============

Data: FITS image

HDU6
----

EXTNAME = WAVE_R

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

HDU7
----

EXTNAME = PHOT_R

Input object photons r-channel.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======== ===== ==============
KEY      Value    Type  Comment
======== ======== ===== ==============
EXTNAME  PHOT_R   str   Extension name
======== ======== ===== ==============

Data: FITS image

HDU8
----

EXTNAME = SKYPHOT_R

Input object photons r-channel.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========= ===== ==============
KEY      Value     Type  Comment
======== ========= ===== ==============
EXTNAME  SKYPHOT_R str   Extension name
======== ========= ===== ==============

Data: FITS image

HDU9
----

EXTNAME = WAVE_Z

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

HDU10
-----

EXTNAME = PHOT_Z

Input object photons z-channel.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======== ===== ==============
KEY      Value    Type  Comment
======== ======== ===== ==============
EXTNAME  PHOT_Z   str   Extension name
======== ======== ===== ==============

Data: FITS image

HDU11
-----

EXTNAME = SKYPHOT_Z

Input object photons z-channel.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========= ===== ==============
KEY      Value     Type  Comment
======== ========= ===== ==============
EXTNAME  SKYPHOT_Z str   Extension name
======== ========= ===== ==============

Data: FITS image

HDU12
-----

EXTNAME = TRUTH

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ======== ==== ==============
KEY     Value    Type Comment
======= ======== ==== ==============
EXTNAME TRUTH    str  extension name
======= ======== ==== ==============

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

========== ========== =========== =====================================
Name       Type       Units       Description
========== ========== =========== =====================================
OBJTYPE    char[10]               Object type (e.g., ELG, QSO, STD, WD)
SUBTYPE    char[10]               Subtype (e.g., LYA, DA, DB)
TEMPLATEID int32                  Template ID
SEED       int64                  Random seed
REDSHIFT   float32                True object redshift.
MAG        float32                True object magnitude.
DECAM_FLUX float32[6]             Synthesized DECam ugrizY nanomaggies
WISE_FLUX  float32[2]             Synthesized WISE W1, W2 nanomaggies
OIIFLUX    float32    erg/(s cm2) [OII] flux
HBETAFLUX  float32    erg/(s cm2) H-BETA flux
EWOII      float32    Angstrom    Rest-frame equivalent width of [OII]
EWHBETA    float32    Angstrom    Rest-frame equivalent width of H-beta
D4000      float32                4000-A break index
VDISP      float32    km/s        Stellar velocity dispersion
OIIDOUBLET float32                [OII] doublet ratio
OIIIHBETA  float32                [OIII]/H-beta flux ratio
OIIHBETA   float32                [OII]/H-beta flux ratio
NIIHBETA   float32                [NII]/H-beta flux ratio
SIIHBETA   float32                [SII]/H-beta flux ratio
ZMETAL     float32                Stellar metallicity of SSP
AGE        float32    Gyr         Age of SSP
TEFF       float32    K           Effective temperature
LOGG       float32    cm/s2       Surface gravity
FEH        float32                Iron abundance with respect to solar
========== ========== =========== =====================================

HDU13
-----

EXTNAME = FIBERMAP

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ======== ==== ==============
KEY     Value    Type Comment
======= ======== ==== ==============
EXTNAME FIBERMAP str  extension name
======= ======== ==== ==============

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

========== ========== =========== =====================================
Name       Type       Units       Description
========== ========== =========== =====================================
OBJTYPE    char[10]               Object type (e.g., ELG, QSO, STD, WD)
========== ========== =========== =====================================

HDU14
-----

EXTNAME = OBSCONDITIONS

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ============= ==== ==============
KEY     Value         Type Comment
======= ============= ==== ==============
EXTNAME OBSCONDITIONS str  extension name
======= ============= ==== ==============

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

========== ========== =========== =====================================
Name       Type       Units       Description
========== ========== =========== =====================================
OBJTYPE    char[10]               Object type (e.g., ELG, QSO, STD, WD)
========== ========== =========== =====================================

HDU15
-----

EXTNAME = TRUTH_BGS

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ========= ==== ==============
KEY     Value     Type Comment
======= ========= ==== ==============
EXTNAME TRUTH_BGS str  extension name
======= ========= ==== ==============

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

========== ========== =========== =====================================
Name       Type       Units       Description
========== ========== =========== =====================================
OBJTYPE    char[10]               Object type (e.g., ELG, QSO, STD, WD)
========== ========== =========== =====================================

HDU16
-----

EXTNAME = TRUTH_ELG

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ========= ==== ==============
KEY     Value     Type Comment
======= ========= ==== ==============
EXTNAME TRUTH_ELG str  extension name
======= ========= ==== ==============

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

========== ========== =========== =====================================
Name       Type       Units       Description
========== ========== =========== =====================================
OBJTYPE    char[10]               Object type (e.g., ELG, QSO, STD, WD)
========== ========== =========== =====================================

HDU17
-----

EXTNAME = TRUTH_STAR

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ========== ==== ==============
KEY     Value      Type Comment
======= ========== ==== ==============
EXTNAME TRUTH_STAR str  extension name
======= ========== ==== ==============

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

========== ========== =========== =====================================
Name       Type       Units       Description
========== ========== =========== =====================================
OBJTYPE    char[10]               Object type (e.g., ELG, QSO, STD, WD)
========== ========== =========== =====================================

HDU18
-----

EXTNAME = TRUTH_WD

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ======== ==== ==============
KEY     Value    Type Comment
======= ======== ==== ==============
EXTNAME TRUTH_WD str  extension name
======= ======== ==== ==============

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

========== ========== =========== =====================================
Name       Type       Units       Description
========== ========== =========== =====================================
OBJTYPE    char[10]               Object type (e.g., ELG, QSO, STD, WD)
========== ========== =========== =====================================

Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
