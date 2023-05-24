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
HDU12_ TRUTH         BINTABLE Truth metadata about the targets
HDU13_ FIBERMAP      BINTABLE Fibermap
HDU14_ OBSCONDITIONS BINTABLE Observing conditions metadata
HDU15_ TRUTH_BGS     BINTABLE BGS-specific truth metadata
HDU16_ TRUTH_ELG     BINTABLE ELG-specific truth metadata
HDU17_ TRUTH_STAR    BINTABLE STAR-specific truth metadata
HDU18_ TRUTH_WD      BINTABLE WD-specific truth metadata
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
NAXIS1   32001               int   Number of wavelength pixels
NIGHT    YYYYMMDD            str   Night of observation
EXPID    0                   int   DESI exposure ID
TILEID   1                   int   DESI tile ID
PROGRAM  dark                str   Program name
FLAVOR   science             str   Flavor of observation (arc, flat, science)
TELRA    0.0                 float Telescope pointing RA [degrees]
TELDEC   0.0                 float Telescope pointing Dec [degrees]
AIRMASS  1.0                 float Airmass at middle of exposure
EXPTIME  1000.0              float Exposure time [sec]
SEEING   1.080542206764221   float Seeing FWHM [arcsec]
MOONFRAC 0.4083473802955095  float Moon illumination fraction 0-1; 1=full
MOONALT  -4.92578905244666   float Moon altitude [degrees]
MOONSEP  135.3911422523808   float Moon:tile separation angle [degrees]
DATE-OBS 2017-06-15T22:00:00 str   Start of exposure
MJD      58925.38986146489   float
SNR2FRAC 0.501188337802887   float
TRANSP   0.9904059171676636  float
SKY      1.0                 float
RA       150.73              float
DEC      30.52               float
PASS     4                   int
DOSVER   SIM                 str
FEEVER   SIM                 str
BUNIT    Angstrom            str   Wavelength unit
AIRORVAC vac                 str   Vacuum wavelengths
======== =================== ===== ==========================================

Data: FITS image [float64, 32001]

HDU1
----

EXTNAME = FLUX

Input object spectra.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============================ ===== ==============
KEY      Value                        Type  Comment
======== ============================ ===== ==============
NAXIS1   32001                        int
NAXIS2   5000                         int
BUNIT    10**-17 erg/(s cm2 Angstrom) str   Flux unit
======== ============================ ===== ==============

Data: FITS image [float32, 32001x5000]

HDU2
----

EXTNAME = SKYFLUX

Input sky flux.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============================ ===== ==============
KEY      Value                        Type  Comment
======== ============================ ===== ==============
NAXIS1   32001                        int
NAXIS2   5000                         int
BUNIT    10**-17 erg/(s cm2 Angstrom) str   Flux unit
======== ============================ ===== ==============

Data: FITS image [float32, 32001x5000]

HDU3
----

EXTNAME = WAVE_B

Input wavelengths b-channel [Angstrom].

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======== ===== ==================
KEY      Value    Type  Comment
======== ======== ===== ==================
NAXIS1   11901    int
======== ======== ===== ==================

Data: FITS image [float64, 11901]

HDU4
----

EXTNAME = PHOT_B

Input object photons b-channel.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======== ===== ==============
KEY      Value    Type  Comment
======== ======== ===== ==============
NAXIS1   11901    int
NAXIS2   5000     int
BUNIT    photon   str
======== ======== ===== ==============

Data: FITS image [float32, 11901x5000]

HDU5
----

EXTNAME = SKYPHOT_B

Input object photons b-channel.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========= ===== ==============
KEY      Value     Type  Comment
======== ========= ===== ==============
NAXIS1   11901     int
NAXIS2   5000      int
BUNIT    photon    str
======== ========= ===== ==============

Data: FITS image [float32, 11901x5000]

HDU6
----

EXTNAME = WAVE_R

Input wavelengths r-channel [Angstrom].

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======== ===== ==================
KEY      Value    Type  Comment
======== ======== ===== ==================
NAXIS1   10581    int
======== ======== ===== ==================

Data: FITS image [float64, 10581]

HDU7
----

EXTNAME = PHOT_R

Input object photons r-channel.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======== ===== ==============
KEY      Value    Type  Comment
======== ======== ===== ==============
NAXIS1   10581    int
NAXIS2   5000     int
BUNIT    photon   str
======== ======== ===== ==============

Data: FITS image [float32, 10581x5000]

HDU8
----

EXTNAME = SKYPHOT_R

Input object photons r-channel.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========= ===== ==============
KEY      Value     Type  Comment
======== ========= ===== ==============
NAXIS1   10581     int
NAXIS2   5000      int
BUNIT    photon    str
======== ========= ===== ==============

Data: FITS image [float32, 10581x5000]

HDU9
----

EXTNAME = WAVE_Z

Input wavelengths z-channel [Angstrom].

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======== ===== ==================
KEY      Value    Type  Comment
======== ======== ===== ==================
NAXIS1   11996    int
======== ======== ===== ==================

Data: FITS image [float64, 11996]

HDU10
-----

EXTNAME = PHOT_Z

Input object photons z-channel.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======== ===== ==============
KEY      Value    Type  Comment
======== ======== ===== ==============
NAXIS1   11996    int
NAXIS2   5000     int
BUNIT    photon   str
======== ======== ===== ==============

Data: FITS image [float32, 11996x5000]

HDU11
-----

EXTNAME = SKYPHOT_Z

Input object photons z-channel.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========= ===== ==============
KEY      Value     Type  Comment
======== ========= ===== ==============
NAXIS1   11996     int
NAXIS2   5000      int
BUNIT    photon    str
======== ========= ===== ==============

Data: FITS image [float32, 11996x5000]

HDU12
-----

EXTNAME = TRUTH

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =====================
KEY    Example Value Type Comment
====== ============= ==== =====================
NAXIS1 109           int  length of dimension 1
NAXIS2 5000          int  length of dimension 2
====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ======== ===== ===========
Name            Type     Units Description
=============== ======== ===== ===========
TARGETID        int64
MOCKID          int64
TRUEZ           float32
TRUESPECTYPE    char[10]
TEMPLATETYPE    char[10]
TEMPLATESUBTYPE char[10]
TEMPLATEID      int32
SEED            int64
MAG             float32
MAGFILTER       char[15]
FLUX_G          float32
FLUX_R          float32
FLUX_Z          float32
FLUX_W1         float32
FLUX_W2         float32
FLUX_W3         float32
FLUX_W4         float32
=============== ======== ===== ===========

HDU13
-----

EXTNAME = FIBERMAP

Map of which fibers are on which targets.
See See :doc:`DESI_SPECTRO_DATA/NIGHT/EXPID/fibermap-EXPID <../../../../DESI_SPECTRO_DATA/NIGHT/EXPID/fibermap-EXPID>`.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================= ===== ======================================
KEY      Example Value           Type  Comment
======== ======================= ===== ======================================
NAXIS1   334                     int   length of dimension 1
NAXIS2   5000                    int   length of dimension 2
NIGHT    20200316                str   Night of observation YEARMMDD
EXPID    10                      int   DESI exposure ID
TILEID   28408                   int   DESI tile ID
PROGRAM  GRAY                    str   program [dark, bright, ...]
FLAVOR   science                 str   Flavor [arc, flat, science, zero, ...]
TELRA    150.73                  float Telescope pointing RA [degrees]
TELDEC   30.52                   float Telescope pointing dec [degrees]
AIRMASS  1.34693655042678        float Airmass at middle of exposure
EXPTIME  757.8536680645208       float Exposure time [sec]
SEEING   1.080542206764221       float Seeing FWHM [arcsec]
MOONFRAC 0.4083473802955095      float Moon illumination fraction 0-1; 1=full
MOONALT  -4.92578905244666       float Moon altitude [degrees]
MOONSEP  135.3911422523808       float Moon:tile separation angle [degrees]
DATE-OBS 2020-03-17T09:21:24.031 str   Start of exposure
======== ======================= ===== ======================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

================= ======= =================== ===========
Name              Type    Units               Description
================= ======= =================== ===========
TARGETID          int64
DESI_TARGET       int64
BGS_TARGET        int64
MWS_TARGET        int64
SECONDARY_TARGET  int64
TARGET_RA         float64
TARGET_DEC        float64
TARGET_RA_IVAR    float64 deg-2
TARGET_DEC_IVAR   float64 deg-2
BRICKID           int64
BRICK_OBJID       int64
MORPHTYPE         char[4]
PRIORITY          int32
SUBPRIORITY       float64
REF_ID            int64
PMRA              float32 10**-3 arcsec yr-1
PMDEC             float32 10**-3 arcsec yr-1
REF_EPOCH         float32
PMRA_IVAR         float32 10**+6 arcsec-2 yr2
PMDEC_IVAR        float32 10**+6 arcsec-2 yr2
RELEASE           int16
FLUX_G            float32
FLUX_R            float32
FLUX_Z            float32
FLUX_W1           float32
FLUX_W2           float32
FLUX_IVAR_G       float32 1/nanomaggies**2
FLUX_IVAR_R       float32 1/nanomaggies**2
FLUX_IVAR_Z       float32 1/nanomaggies**2
FLUX_IVAR_W1      float32 1/nanomaggies**2
FLUX_IVAR_W2      float32 1/nanomaggies**2
FIBERFLUX_G       float32 nanomaggies
FIBERFLUX_R       float32 nanomaggies
FIBERFLUX_Z       float32 nanomaggies
FIBERFLUX_W1      float32 nanomaggies
FIBERFLUX_W2      float32 nanomaggies
FIBERTOTFLUX_G    float32 nanomaggies
FIBERTOTFLUX_R    float32 nanomaggies
FIBERTOTFLUX_Z    float32 nanomaggies
FIBERTOTFLUX_W1   float32 nanomaggies
FIBERTOTFLUX_W2   float32 nanomaggies
MW_TRANSMISSION_G float32
MW_TRANSMISSION_R float32
MW_TRANSMISSION_Z float32
EBV               float32
PHOTSYS           char[1]
OBSCONDITIONS     int32
NUMOBS_INIT       int64
PRIORITY_INIT     int64
NUMOBS_MORE       int32
HPXPIXEL          int64
FIBER             int32
PETAL_LOC         int32
DEVICE_LOC        int32
LOCATION          int32
FIBERSTATUS       int32
OBJTYPE           char[3]
LAMBDA_REF        float32 Angstrom
FIBERASSIGN_X     float32
FIBERASSIGN_Y     float32
FA_TARGET         int64
FA_TYPE           byte
NUMTARGET         int16
FIBER_RA          float64
FIBER_DEC         float64
FIBER_RA_IVAR     float32 deg-2
FIBER_DEC_IVAR    float32 deg-2
PLATEMAKER_X      float32 mm
PLATEMAKER_Y      float32 mm
PLATEMAKER_RA     float32 deg
PLATEMAKER_DEC    float32 deg
NUM_ITER          int32
SPECTROID         int32
BRICKNAME         char[8]
LAMBDAREF         float64
DELTA_X           float64
DELTA_Y           float64
================= ======= =================== ===========

HDU14
-----

EXTNAME = OBSCONDITIONS

Table with a single row defining the observing conditions for this exposure,
e.g. SEEING, AIRMASS, lunar conditions.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =====================
KEY    Example Value Type Comment
====== ============= ==== =====================
NAXIS1 115           int  length of dimension 1
NAXIS2 1             int  length of dimension 2
====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

============ ======= ====== ===========
Name         Type    Units  Description
============ ======= ====== ===========
EXPID        int32          Exposure ID
MJD          float64        Modified Julian Date
EXPTIME      float32 s      Exposure time
TILEID       int32          Tile ID
SNR2FRAC     float32
AIRMASS      float32        Airmass
SEEING       float32 arcsec Atmospheric seeing FWHM
TRANSP       float32        Transparency [0-1]; 0=no photons
SKY          float32
PROGRAM      char[6]        DESI program name (e.g. DARK/GRAY/BRIGHT)
NIGHT        char[8]        Night 'YEARMMDD'
FLAVOR       char[7]        Exposure flavor (e.g. science or calib)
MOONFRAC     float64        Moon illumination fraction [0-1]; 1=full moon
MOONALT      float64 deg    Moon altitude
MOONSEP      float64 deg    Separation angle between moon and center of tile
RA           float64 deg    Right ascension
DEC          float64 deg    Declination
PASS         int16          tiling pass number
============ ======= ====== ===========

TODO: define if AIRMASS etc. are at middle of exposure, averaged, etc.

HDU15
-----

EXTNAME = TRUTH_BGS

Truth metadata that are specific to BGS targets.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =====================
KEY    Example Value Type Comment
====== ============= ==== =====================
NAXIS1 56            int  length of dimension 1
NAXIS2 262           int  length of dimension 2
====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=========== ======= ===== ===========
Name        Type    Units Description
=========== ======= ===== ===========
TARGETID    int64
OIIFLUX     float32
HBETAFLUX   float32
EWOII       float32
EWHBETA     float32
D4000       float32
VDISP       float32
OIIDOUBLET  float32
OIIIHBETA   float32
OIIHBETA    float32
NIIHBETA    float32
SIIHBETA    float32
TRUEZ_NORSD float32
=========== ======= ===== ===========

HDU16
-----

EXTNAME = TRUTH_ELG

Truth metadata that are specific to ELG targets.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =====================
KEY    Example Value Type Comment
====== ============= ==== =====================
NAXIS1 56            int  length of dimension 1
NAXIS2 4225          int  length of dimension 2
====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=========== ======= ===== ===========
Name        Type    Units Description
=========== ======= ===== ===========
TARGETID    int64
OIIFLUX     float32
HBETAFLUX   float32
EWOII       float32
EWHBETA     float32
D4000       float32
VDISP       float32
OIIDOUBLET  float32
OIIIHBETA   float32
OIIHBETA    float32
NIIHBETA    float32
SIIHBETA    float32
TRUEZ_NORSD float32
=========== ======= ===== ===========

HDU17
-----

EXTNAME = TRUTH_STAR

Truth metadata that are specific to STAR targets.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =====================
KEY    Example Value Type Comment
====== ============= ==== =====================
NAXIS1 20            int  length of dimension 1
NAXIS2 106           int  length of dimension 2
====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

======== ======= ===== ===========
Name     Type    Units Description
======== ======= ===== ===========
TARGETID int64
TEFF     float32
LOGG     float32
FEH      float32
======== ======= ===== ===========

HDU18
-----

EXTNAME = TRUTH_WD

Truth metadata that are specific to White Dwarf targets.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =====================
KEY    Example Value Type Comment
====== ============= ==== =====================
NAXIS1 16            int  length of dimension 1
NAXIS2 1             int  length of dimension 2
====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

======== ======= ===== ===========
Name     Type    Units Description
======== ======= ===== ===========
TARGETID int64
TEFF     float32
LOGG     float32
======== ======= ===== ===========
