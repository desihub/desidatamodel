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

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

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

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

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

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

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

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

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

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

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

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

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

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

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

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

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

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

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

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

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

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

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

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

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

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =====================
    KEY    Example Value Type Comment
    ====== ============= ==== =====================
    NAXIS1 109           int  length of dimension 1
    NAXIS2 5000          int  length of dimension 2
    ====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

=============== ======== ========= =====================================
Name            Type     Units     Description
=============== ======== ========= =====================================
TARGETID        int64              Unique DESI target ID
MOCKID          int64              TODO: description needed
TRUEZ           float32            TODO: description needed
TRUESPECTYPE    char[10]           TODO: description needed
TEMPLATETYPE    char[10]           TODO: description needed
TEMPLATESUBTYPE char[10]           TODO: description needed
TEMPLATEID      int32              TODO: description needed
SEED            int64              TODO: description needed
MAG             float32            TODO: description needed
MAGFILTER       char[15]           TODO: description needed
FLUX_G          float32  nanomaggy Flux in the Legacy Survey g-band (AB)
FLUX_R          float32  nanomaggy Flux in the Legacy Survey r-band (AB)
FLUX_Z          float32  nanomaggy Flux in the Legacy Survey z-band (AB)
FLUX_W1         float32  nanomaggy WISE flux in W1 (AB)
FLUX_W2         float32  nanomaggy WISE flux in W2 (AB)
FLUX_W3         float32            TODO: description needed
FLUX_W4         float32            TODO: description needed
=============== ======== ========= =====================================

HDU13
-----

EXTNAME = FIBERMAP

Map of which fibers are on which targets.
See See :doc:`DESI_SPECTRO_DATA/NIGHT/EXPID/fibermap-EXPID <../../../../DESI_SPECTRO_DATA/NIGHT/EXPID/fibermap-EXPID>`.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

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

.. rst-class:: columns

================= ======= =================== =========================================================================================================================
Name              Type    Units               Description
================= ======= =================== =========================================================================================================================
TARGETID          int64                       Unique DESI target ID
DESI_TARGET       int64                       DESI (dark time program) target selection bitmask
BGS_TARGET        int64                       BGS (Bright Galaxy Survey) target selection bitmask
MWS_TARGET        int64                       Milky Way Survey targeting bits
SECONDARY_TARGET  int64                       TODO: description needed
TARGET_RA         float64 deg                 Barycentric right ascension in ICRS
TARGET_DEC        float64 deg                 Barycentric declination in ICRS
TARGET_RA_IVAR    float64 deg-2               TODO: description needed
TARGET_DEC_IVAR   float64 deg-2               TODO: description needed
BRICKID           int64                       Brick ID from tractor input
BRICK_OBJID       int64                       Imaging Surveys OBJID on that brick
MORPHTYPE         char[4]                     Imaging Surveys morphological type from Tractor
PRIORITY          int32                       Target current priority
SUBPRIORITY       float64                     Random subpriority [0-1) to break assignment ties
REF_ID            int64                       Tyc1*1,000,000+Tyc2*10+Tyc3 for Tycho-2; ``sourceid`` for Gaia DR2
PMRA              float32 10**-3 arcsec yr-1  proper motion in the +RA direction (already including cos(dec))
PMDEC             float32 10**-3 arcsec yr-1  Proper motion in the +Dec direction
REF_EPOCH         float32 yr                  Reference epoch for Gaia/Tycho astrometry. Typically 2015.5 for Gaia
PMRA_IVAR         float32 10**+6 arcsec-2 yr2 Inverse variance of PMRA
PMDEC_IVAR        float32 10**+6 arcsec-2 yr2 Inverse variance of PMDEC
RELEASE           int16                       Imaging surveys release ID
FLUX_G            float32 nanomaggy           Flux in the Legacy Survey g-band (AB)
FLUX_R            float32 nanomaggy           Flux in the Legacy Survey r-band (AB)
FLUX_Z            float32 nanomaggy           Flux in the Legacy Survey z-band (AB)
FLUX_W1           float32 nanomaggy           WISE flux in W1 (AB)
FLUX_W2           float32 nanomaggy           WISE flux in W2 (AB)
FLUX_IVAR_G       float32 1/nanomaggies**2    Inverse variance of FLUX_G (AB)
FLUX_IVAR_R       float32 1/nanomaggies**2    Inverse variance of FLUX_R (AB)
FLUX_IVAR_Z       float32 1/nanomaggies**2    Inverse variance of FLUX_Z (AB)
FLUX_IVAR_W1      float32 1/nanomaggies**2    Inverse variance of FLUX_W1 (AB)
FLUX_IVAR_W2      float32 1/nanomaggies**2    Inverse variance of FLUX_W2 (AB)
FIBERFLUX_G       float32 nanomaggies         Predicted g-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERFLUX_R       float32 nanomaggies         Predicted r-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERFLUX_Z       float32 nanomaggies         Predicted z-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERFLUX_W1      float32 nanomaggies         TODO: description needed
FIBERFLUX_W2      float32 nanomaggies         TODO: description needed
FIBERTOTFLUX_G    float32 nanomaggies         Predicted g-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
FIBERTOTFLUX_R    float32 nanomaggies         Predicted r-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
FIBERTOTFLUX_Z    float32 nanomaggies         Predicted z-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
FIBERTOTFLUX_W1   float32 nanomaggies         TODO: description needed
FIBERTOTFLUX_W2   float32 nanomaggies         TODO: description needed
MW_TRANSMISSION_G float32                     Milky Way dust transmission in LS g-band
MW_TRANSMISSION_R float32                     Milky Way dust transmission in LS r-band
MW_TRANSMISSION_Z float32                     Milky Way dust transmission in LS z-band
EBV               float32 mag                 Galactic extinction E(B-V) reddening from SFD98
PHOTSYS           char[1]                     &#x27;N&#x27; for the MzLS/BASS photometric system, &#x27;S&#x27; for DECaLS
OBSCONDITIONS     int32                       Bitmask of allowed observing conditions
NUMOBS_INIT       int64                       Initial number of observations for target calculated across target selection bitmasks and OBSCONDITIONS
PRIORITY_INIT     int64                       Target initial priority from target selection bitmasks and OBSCONDITIONS
NUMOBS_MORE       int32                       Number of additional observations needed
HPXPIXEL          int64                       HEALPixel containing this location at NSIDE=64 in the NESTED scheme
FIBER             int32                       Fiber ID on the CCDs [0-4999]
PETAL_LOC         int32                       Petal location [0-9]
DEVICE_LOC        int32                       Device location on focal plane [0-523]
LOCATION          int32                       Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBERSTATUS       int32                       Fiber status mask. 0=good
OBJTYPE           char[3]                     Object type: TGT, SKY, NON, BAD
LAMBDA_REF        float32 Angstrom            Requested wavelength at which targets should be centered on fibers
FIBERASSIGN_X     float32 mm                  Fiberassign expected CS5 X location on focal plane
FIBERASSIGN_Y     float32 mm                  Fiberassign expected CS5 Y location on focal plane
FA_TARGET         int64                       Targeting bit internally used by fiberassign (linked with FA_TYPE)
FA_TYPE           byte                        Fiberassign internal target type (science, standard, sky, safe, suppsky)
NUMTARGET         int16                       TODO: description needed
FIBER_RA          float64 deg                 RA of actual fiber position
FIBER_DEC         float64 deg                 DEC of actual fiber position
FIBER_RA_IVAR     float32 deg-2               TODO: description needed
FIBER_DEC_IVAR    float32 deg-2               TODO: description needed
PLATEMAKER_X      float32 mm                  TODO: description needed
PLATEMAKER_Y      float32 mm                  TODO: description needed
PLATEMAKER_RA     float32 deg                 TODO: description needed
PLATEMAKER_DEC    float32 deg                 TODO: description needed
NUM_ITER          int32                       Number of positioner iterations
SPECTROID         int32                       TODO: description needed
BRICKNAME         char[8]                     Brick name from tractor input
LAMBDAREF         float64                     TODO: description needed
DELTA_X           float64 mm                  CS5 X requested minus actual position
DELTA_Y           float64 mm                  CS5 Y requested minus actual position
================= ======= =================== =========================================================================================================================

HDU14
-----

EXTNAME = OBSCONDITIONS

Table with a single row defining the observing conditions for this exposure,
e.g. SEEING, AIRMASS, lunar conditions.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =====================
    KEY    Example Value Type Comment
    ====== ============= ==== =====================
    NAXIS1 115           int  length of dimension 1
    NAXIS2 1             int  length of dimension 2
    ====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

======== ======= ====== ================================================
Name     Type    Units  Description
======== ======= ====== ================================================
EXPID    int32          Exposure ID
MJD      float64 d      Modified Julian Date
EXPTIME  float32 s      Exposure time
TILEID   int32          Tile ID
SNR2FRAC float32        TODO: description needed
AIRMASS  float32        Airmass
SEEING   float32 arcsec Atmospheric seeing FWHM
TRANSP   float32        Transparency [0-1]; 0=no photons
SKY      float32        TODO: description needed
PROGRAM  char[6]        DESI program name (e.g. DARK/GRAY/BRIGHT)
NIGHT    char[8]        Night 'YEARMMDD'
FLAVOR   char[7]        Exposure flavor (e.g. science or calib)
MOONFRAC float64        Moon illumination fraction [0-1]; 1=full moon
MOONALT  float64 deg    Moon altitude
MOONSEP  float64 deg    Separation angle between moon and center of tile
RA       float64 deg    Right ascension
DEC      float64 deg    Declination
PASS     int16          tiling pass number
======== ======= ====== ================================================

TODO: define if AIRMASS etc. are at middle of exposure, averaged, etc.

HDU15
-----

EXTNAME = TRUTH_BGS

Truth metadata that are specific to BGS targets.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =====================
    KEY    Example Value Type Comment
    ====== ============= ==== =====================
    NAXIS1 56            int  length of dimension 1
    NAXIS2 262           int  length of dimension 2
    ====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

=========== ======= ===== ========================
Name        Type    Units Description
=========== ======= ===== ========================
TARGETID    int64         Unique DESI target ID
OIIFLUX     float32       TODO: description needed
HBETAFLUX   float32       TODO: description needed
EWOII       float32       TODO: description needed
EWHBETA     float32       TODO: description needed
D4000       float32       TODO: description needed
VDISP       float32       TODO: description needed
OIIDOUBLET  float32       TODO: description needed
OIIIHBETA   float32       TODO: description needed
OIIHBETA    float32       TODO: description needed
NIIHBETA    float32       TODO: description needed
SIIHBETA    float32       TODO: description needed
TRUEZ_NORSD float32       TODO: description needed
=========== ======= ===== ========================

HDU16
-----

EXTNAME = TRUTH_ELG

Truth metadata that are specific to ELG targets.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =====================
    KEY    Example Value Type Comment
    ====== ============= ==== =====================
    NAXIS1 56            int  length of dimension 1
    NAXIS2 4225          int  length of dimension 2
    ====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

=========== ======= ===== ========================
Name        Type    Units Description
=========== ======= ===== ========================
TARGETID    int64         Unique DESI target ID
OIIFLUX     float32       TODO: description needed
HBETAFLUX   float32       TODO: description needed
EWOII       float32       TODO: description needed
EWHBETA     float32       TODO: description needed
D4000       float32       TODO: description needed
VDISP       float32       TODO: description needed
OIIDOUBLET  float32       TODO: description needed
OIIIHBETA   float32       TODO: description needed
OIIHBETA    float32       TODO: description needed
NIIHBETA    float32       TODO: description needed
SIIHBETA    float32       TODO: description needed
TRUEZ_NORSD float32       TODO: description needed
=========== ======= ===== ========================

HDU17
-----

EXTNAME = TRUTH_STAR

Truth metadata that are specific to STAR targets.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =====================
    KEY    Example Value Type Comment
    ====== ============= ==== =====================
    NAXIS1 20            int  length of dimension 1
    NAXIS2 106           int  length of dimension 2
    ====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

======== ======= ===== ========================
Name     Type    Units Description
======== ======= ===== ========================
TARGETID int64         Unique DESI target ID
TEFF     float32       TODO: description needed
LOGG     float32       TODO: description needed
FEH      float32       TODO: description needed
======== ======= ===== ========================

HDU18
-----

EXTNAME = TRUTH_WD

Truth metadata that are specific to White Dwarf targets.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =====================
    KEY    Example Value Type Comment
    ====== ============= ==== =====================
    NAXIS1 16            int  length of dimension 1
    NAXIS2 1             int  length of dimension 2
    ====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

======== ======= ===== ========================
Name     Type    Units Description
======== ======= ===== ========================
TARGETID int64         Unique DESI target ID
TEFF     float32       TODO: description needed
LOGG     float32       TODO: description needed
======== ======= ===== ========================
