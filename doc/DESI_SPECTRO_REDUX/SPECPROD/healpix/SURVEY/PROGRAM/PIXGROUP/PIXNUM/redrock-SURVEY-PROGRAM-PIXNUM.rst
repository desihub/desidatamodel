==================================
redrock-SURVEY-PROGRAM-PIXNUM.fits
==================================

:Summary: Redshifts and spectral classifications from Redrock.
:Naming Convention: ``redrock-SURVEY-PROGRAM-PIXNUM.fits``, where ``SURVEY`` is
    *e.g.* ``main`` or ``sv1``, ``PROGRAM`` is *e.g.* ``bright or ``dark``
    and ``PIXNUM`` is the HEALPixel number.
:Regex: ``redrock-(cmx|main|special|sv1|sv2|sv3)-(backup|bright|dark|other)-[0-9]+\.fits``
:File Type: FITS, 354 KB

This file contains spectral classifications and redshifts for spectra
coadded across exposures and tiles covering a given HEALpix pixel.
For a similar file that only combines data across a single tile but
not across tiles, see
:doc:`tile-based Redrock files </DESI_SPECTRO_REDUX/SPECPROD/tiles/GROUPTYPE/TILEID/GROUPID/redrock-SPECTROGRAPH-TILEID-GROUPID>`.

Contents
========

====== ============ ======== ===================
Number EXTNAME      Type     Contents
====== ============ ======== ===================
HDU0_               IMAGE    Keywords only
HDU1_  REDSHIFTS    BINTABLE Table with redshifts and spectral classifications
HDU2_  FIBERMAP     BINTABLE Target photometry and metadata
HDU3_  EXP_FIBERMAP BINTABLE Per-exposure entries from input fibermaps
HDU4_  TSNR2        BINTABLE Template signal-to-noise values from input SCORES table
====== ============ ======== ===================


FITS Header Units
=================

HDU0
----

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ============= ==== ===============
    KEY      Example Value Type Comment
    ======== ============= ==== ===============
    LONGSTRN OGIP 1.0      str
    RRVER    0.15.0        str  Redrock version
    TEMNAM00 GALAXY        str  Redrock template 00 name
    TEMVER00 2.6           str  Redrock template 00 version
    TEMNAM01 QSO           str
    TEMVER01 0.1           str
    TEMNAM02 STAR:::A      str
    TEMVER02 0.1           str
    TEMNAM03 STAR:::B      str
    TEMVER03 0.1           str
    TEMNAM04 STAR:::CV     str
    TEMVER04 0.1           str
    TEMNAM05 STAR:::F      str
    TEMVER05 0.1           str
    TEMNAM06 STAR:::G      str
    TEMVER06 0.1           str
    TEMNAM07 STAR:::K      str
    TEMVER07 0.1           str
    TEMNAM08 STAR:::M      str
    TEMVER08 0.1           str
    TEMNAM09 STAR:::WD     str
    TEMVER09 0.1           str
    SPGRP    healpix       str  Grouping method
    SPGRPVAL 32637         int  Grouping value (same as HPXPIXEL)
    HPXPIXEL 36637         int  Healpix pixel
    HPXNSIDE 64            int  Healpix nside
    HPXNEST  True          str  Healpix nested (not ring)
    SURVEY   sv1           str  DESI survey (sv1, sv3, main, ...)
    PROGRAM  dark          str  DESI program (dark, bright, ...)
    ======== ============= ==== ===============

Empty HDU.

HDU1
----

EXTNAME = REDSHIFTS

Spectral classifications and redshifts from Redrock.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =====================
    KEY    Example Value Type Comment
    ====== ============= ==== =====================
    NAXIS1 170           int  Width of table in bytes
    NAXIS2 415           int  Number of targets in table
    ====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

========= =========== ===== =========================================================
Name      Type        Units Description
========= =========== ===== =========================================================
TARGETID  int64             Target ID for this row
CHI2      float64           Best fit :math:`\chi^2`
COEFF     float64[10]       Redrock template coefficients
Z         float64           Best fit redshift
ZERR      float64           Uncertainty on best fit redshift
ZWARN     int64             Warning flags; 0 is good
NPIXELS   int64             Number of unmasked pixels contributing to the Redrock fit
SPECTYPE  char[6]           Spectral type
SUBTYPE   char[20]          Spectral subtype (maybe blank)
NCOEFF    int64             Number of Redrock template coefficients
DELTACHI2 float64           :math:`\Delta \chi^2` to next best fit
========= =========== ===== =========================================================

HDU2
----

EXTNAME = FIBERMAP

Fibermap with target metadata such as photometry and target selection bits.
This table is row-matched to the REDSHIFTS table.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =====================
    KEY    Example Value Type Comment
    ====== ============= ==== =====================
    NAXIS1 317           int  Width of table in bytes
    NAXIS2 415           int  Number of targets in table.
    ====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

========================== ======= ============ ===============================================================================================================================
Name                       Type    Units        Description
========================== ======= ============ ===============================================================================================================================
TARGETID                   int64                Unique DESI target ID
COADD_FIBERSTATUS          int32                bitwise-AND of input FIBERSTATUS
TARGET_RA                  float64 deg          Barycentric right ascension in ICRS
TARGET_DEC                 float64 deg          Barycentric declination in ICRS
PMRA                       float32 mas yr^-1    proper motion in the +RA direction (already including cos(dec))
PMDEC                      float32 mas yr^-1    Proper motion in the +Dec direction
REF_EPOCH                  float32 yr           Reference epoch for Gaia/Tycho astrometry. Typically 2015.5 for Gaia
FA_TARGET                  int64                Targeting bit internally used by fiberassign (linked with FA_TYPE)
FA_TYPE                    binary               Fiberassign internal target type (science, standard, sky, safe, suppsky)
OBJTYPE                    char[3]              Object type: TGT, SKY, NON, BAD
SUBPRIORITY                float64              Random subpriority [0-1) to break assignment ties
OBSCONDITIONS              int32                Bitmask of allowed observing conditions
RELEASE                    int16                Imaging surveys release ID
BRICKID                    int32                Brick ID from tractor input
BRICK_OBJID                int32                Imaging Surveys OBJID on that brick
MORPHTYPE                  char[4]              Imaging Surveys morphological type from Tractor
FLUX_G                     float32 nanomaggy    Flux in the Legacy Survey g-band (AB)
FLUX_R                     float32 nanomaggy    Flux in the Legacy Survey r-band (AB)
FLUX_Z                     float32 nanomaggy    Flux in the Legacy Survey z-band (AB)
FLUX_IVAR_G                float32 nanomaggy^-2 Inverse variance of FLUX_G (AB)
FLUX_IVAR_R                float32 nanomaggy^-2 Inverse variance of FLUX_R (AB)
FLUX_IVAR_Z                float32 nanomaggy^-2 Inverse variance of FLUX_Z (AB)
MASKBITS                   int16                Bitwise mask from the imaging indicating potential issue or blending
REF_ID                     int64                Tyc1*1,000,000+Tyc2*10+Tyc3 for Tycho-2; “sourceid” for Gaia DR2
REF_CAT                    char[2]              Reference catalog source for star: “T2” for Tycho-2, “G2” for Gaia DR2, “L2” for the SGA, empty otherwise
GAIA_PHOT_G_MEAN_MAG       float32 mag          Gaia G band magnitude
GAIA_PHOT_BP_MEAN_MAG      float32 mag          Gaia BP band magnitude
GAIA_PHOT_RP_MEAN_MAG      float32 mag          Gaia RP band magnitude
PARALLAX                   float32 mas          Reference catalog parallax
BRICKNAME                  char[8]              Brick name from tractor input
EBV                        float32 mag          Galactic extinction E(B-V) reddening from SFD98
FLUX_W1                    float32 nanomaggy    WISE flux in W1 (AB)
FLUX_W2                    float32 nanomaggy    WISE flux in W2 (AB)
FLUX_IVAR_W1               float32 nanomaggy^-2 Inverse variance of FLUX_W1 (AB)
FLUX_IVAR_W2               float32 nanomaggy^-2 Inverse variance of FLUX_W2 (AB)
FIBERFLUX_G                float32 nanomaggy    Predicted g-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERFLUX_R                float32 nanomaggy    Predicted r-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERFLUX_Z                float32 nanomaggy    Predicted z-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERTOTFLUX_G             float32 nanomaggy    Predicted g-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
FIBERTOTFLUX_R             float32 nanomaggy    Predicted r-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
FIBERTOTFLUX_Z             float32 nanomaggy    Predicted z-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
SERSIC                     float32              Power-law index for the Sersic profile model (MORPHTYPE=”SER”)
SHAPE_R                    float32 arcsec       Half-light radius of galaxy model (&gt;0)
SHAPE_E1                   float32              Ellipticity component 1 of galaxy model for galaxy type MORPHTYPE
SHAPE_E2                   float32              Ellipticity component 2 of galaxy model for galaxy type MORPHTYPE
PHOTSYS                    char[1]              'N' for the MzLS/BASS photometric system, 'S' for DECaLS
PRIORITY_INIT              int64                Target initial priority from target selection bitmasks and OBSCONDITIONS
NUMOBS_INIT                int64                Initial number of observations for target calculated across target selection bitmasks and OBSCONDITIONS
DESI_TARGET                int64                DESI (dark time program) target selection bitmask
BGS_TARGET                 int64                BGS (Bright Galaxy Survey) target selection bitmask
MWS_TARGET                 int64                Milky Way Survey targeting bits
SCND_TARGET                int64                Target selection bitmask for secondary programs
PLATE_RA                   float64 deg          Barycentric Right Ascension in ICRS to be used by PlateMaker
PLATE_DEC                  float64 deg          Barycentric Declination in ICRS to be used by PlateMaker
COADD_NUMEXP               int16                Number of exposures in coadd
COADD_EXPTIME              float32 s            Summed exposure time for coadd
COADD_NUMNIGHT             int16                Number of nights in coadd
COADD_NUMTILE              int16                Number of tiles in coadd
MEAN_DELTA_X               float32 mm           Mean (over exposures) fiber difference requested - actual CS5 X location on focal plane
RMS_DELTA_X                float32 mm           RMS (over exposures) of the fiber difference between measured and requested CS5 X location on focal plane
MEAN_DELTA_Y               float32 mm           Mean (over exposures) fiber difference requested - actual CS5 Y location on focal plane
RMS_DELTA_Y                float32 mm           RMS (over exposures) of the fiber difference between measured and requested CS5 Y location on focal plane
MEAN_FIBER_RA              float64 deg          Mean (over exposures) RA of actual fiber position
STD_FIBER_RA               float32 arcsec       Standard deviation (over exposures) of RA of actual fiber position
MEAN_FIBER_DEC             float64 deg          Mean (over exposures) DEC of actual fiber position
STD_FIBER_DEC              float32 arcsec       Standard deviation (over exposures) of DEC of actual fiber position
MEAN_PSF_TO_FIBER_SPECFLUX float32              Mean of input exposures fraction of light from point-like source captured by 1.5 arcsec diameter fiber given atmospheric seeing
========================== ======= ============ ===============================================================================================================================

HDU3
----

EXTNAME = EXP_FIBERMAP

Fibermap entries that vary from exposure to exposure, e.g. what exposures
were include in the coadd and what focalplane (x,y) each target was located
at for each exposure.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =====================
    KEY    Example Value Type Comment
    ====== ============= ==== =====================
    NAXIS1 162           int  Width of table in bytes
    NAXIS2 415           int  Number of input target-exposures = rows in table
    ====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

===================== ======= ======== =======================================================================================================
Name                  Type    Units    Description
===================== ======= ======== =======================================================================================================
TARGETID              int64            Unique DESI target ID
PRIORITY              int32            Target current priority
SUBPRIORITY           float64          Random subpriority [0-1) to break assignment ties
NIGHT                 int32
EXPID                 int32            DESI Exposure ID number
MJD                   float64          Modified Julian Date when shutter was opened for this exposure
TILEID                int32            Unique DESI tile ID
EXPTIME               float64 s        Length of time shutter was open
PETAL_LOC             int16            Petal location [0-9]
DEVICE_LOC            int32            Device location on focal plane [0-523]
LOCATION              int64            Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBER                 int32            Fiber ID on the CCDs [0-4999]
FIBERSTATUS           int32            Fiber status mask. 0=good
FIBERASSIGN_X         float32 mm       Fiberassign expected CS5 X location on focal plane
FIBERASSIGN_Y         float32 mm       Fiberassign expected CS5 Y location on focal plane
LAMBDA_REF            float32 Angstrom Requested wavelength at which targets should be centered on fibers
PLATE_RA              float64 deg      Barycentric Right Ascension in ICRS to be used by PlateMaker
PLATE_DEC             float64 deg      Barycentric Declination in ICRS to be used by PlateMaker
NUM_ITER              int64            Number of positioner iterations
FIBER_X               float64 mm       CS5 X location requested by PlateMaker
FIBER_Y               float64 mm       CS5 Y location requested by PlateMaker
DELTA_X               float64 mm       CS5 X requested minus actual position
DELTA_Y               float64 mm       CS5 Y requested minus actual position
FIBER_RA              float64 deg      RA of actual fiber position
FIBER_DEC             float64 deg      DEC of actual fiber position
PSF_TO_FIBER_SPECFLUX float64          fraction of light from point-like source captured by 1.5 arcsec diameter fiber given atmospheric seeing
===================== ======= ======== =======================================================================================================

HDU4
----

EXTNAME = TSNR2

Template signal-to-noise squared.
These quantities weight the observed (S/N)^2 by which wavelengths matter
most for different target types, e.g. QSOs weight blue wavelengths more
while ELGs weight redder wavelengths more due to the wavelengths of the
observed emission lines.  For more details, see section 4.14 of
`Guy et al 2023 <https://ui.adsabs.harvard.edu/abs/2023AJ....165..144G/abstract>`_.

This table is row-matched to the REDSHIFTS table.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =====================
    KEY    Example Value Type Comment
    ====== ============= ==== =====================
    NAXIS1 136           int  Width of table in bytes.
    NAXIS2 415           int  Number of targets = number of table rows.
    ====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

================= ======= ===== ======================================
Name              Type    Units Description
================= ======= ===== ======================================
TARGETID          int64         Unique DESI target ID
TSNR2_GPBDARK_B   float32
TSNR2_ELG_B       float32       ELG B template (S/N)^2
TSNR2_GPBBRIGHT_B float32
TSNR2_LYA_B       float32       LYA B template (S/N)^2
TSNR2_BGS_B       float32       BGS B template (S/N)^2
TSNR2_GPBBACKUP_B float32
TSNR2_QSO_B       float32       QSO B template (S/N)^2
TSNR2_LRG_B       float32       LRG B template (S/N)^2
TSNR2_GPBDARK_R   float32
TSNR2_ELG_R       float32       ELG R template (S/N)^2
TSNR2_GPBBRIGHT_R float32
TSNR2_LYA_R       float32       LYA R template (S/N)^2
TSNR2_BGS_R       float32       BGS R template (S/N)^2
TSNR2_GPBBACKUP_R float32
TSNR2_QSO_R       float32       QSO R template (S/N)^2
TSNR2_LRG_R       float32       LRG R template (S/N)^2
TSNR2_GPBDARK_Z   float32
TSNR2_ELG_Z       float32       ELG Z template (S/N)^2
TSNR2_GPBBRIGHT_Z float32
TSNR2_LYA_Z       float32       LYA Z template (S/N)^2
TSNR2_BGS_Z       float32       BGS Z template (S/N)^2
TSNR2_GPBBACKUP_Z float32
TSNR2_QSO_Z       float32       QSO Z template (S/N)^2
TSNR2_LRG_Z       float32       LRG Z template (S/N)^2
TSNR2_GPBDARK     float32
TSNR2_ELG         float32       ELG template (S/N)^2 summed over B,R,Z
TSNR2_GPBBRIGHT   float32
TSNR2_LYA         float32       LYA template (S/N)^2 summed over B,R,Z
TSNR2_BGS         float32       BGS template (S/N)^2 summed over B,R,Z
TSNR2_GPBBACKUP   float32
TSNR2_QSO         float32       QSO template (S/N)^2 summed over B,R,Z
TSNR2_LRG         float32       LRG template (S/N)^2 summed over B,R,Z
================= ======= ===== ======================================


Notes and Examples
==================

The REDSHIFTS, FIBERMAP, and TSNR2 tables are row-matched with one row per
target.  They also include a TARGETID column for confirmation and
database-like joins with other tables.
The EXP_FIBERMAP HDU has one row per target-exposure, and thus will have
multiple entries per target when a target was observed on multiple
input exposures.

This file is for redshifts from an individual healpixel.
For a contatenation of all such files within a given survey and program, see the
:doc:`zpix file </DESI_SPECTRO_REDUX/SPECPROD/zcatalog/VERSION/zpix-SURVEY-PROGRAM>`.

For the SURVEY=cmx m33 tile (TILEID=80615) tile and all the SURVEY=sv1 tiles (except TILEID=80971-80976, the dc3r2 ones), proper-motion correction was applied at the :doc:`fiberassign </DESI_TARGET/fiberassign/tiles/TILES_VERSION/TILEXX/fiberassign-TILEID>` design step; thus the following columns can have different values than in the :doc:`desitarget products </DESI_TARGET/TARG_DIR/DR/VERSION/targets/PHASE/RESOLVE/OBSCON/PHASEtargets-OBSCON-RESOLVE-hp-HP>`: ``TARGET_RA``, ``TARGET_DEC``, ``REF_EPOCH``, ``PLATE_RA``, ``PLATE_DEC``, and ``PLATE_REF_EPOCH``.

For targets with a non-zero proper motion, ``FIBER_RA`` and ``FIBER_DEC`` refer to the position at the reference epoch (but note that the proper-motion correction has been applied at the time of the observation, it is just not recorded in ``FIBER_RA`` and ``FIBER_DEC``).
