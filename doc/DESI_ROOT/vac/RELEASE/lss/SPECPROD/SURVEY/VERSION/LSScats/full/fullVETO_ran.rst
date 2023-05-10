================================
'full' LSS catalogs for randoms
================================

:Summary: LSS catalogs containing information on all of the random targets identified as reachable by DESI fiberassign, for one of the input randoms. The files are split by target type, random file number, and whether of not vetos for angular positions have been applied.
:Naming Convention: ``{TARGET}_{RANN}_full{VETO}.ran.fits``, where ``{TARGET}`` is the target type: ``QSO``, ``ELG``, ``ELGnotqso``, ``ELG_HIP``, ``ELG_HIPnotqso``, ``LRG``, ``LRG_main``,
                    for dark or ``BGS_ANY``, ``BGS_BRIGHT`` for bright. ``{RANN}`` is the number between 0 and 17 designating the given random file, and ``{VETO}`` is _noveto if vetos have not been applied and blank otherwise.
:Regex: ``[a-zA-Z]{3,}_[0-17]_full[a-z]{0,7}.ran.fits``
:File Type: FITS, 1 GB  


Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    Empty HDU
HDU1_  LSS     BINTABLE Catalog data
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = LSS

Catalog of randoms

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =======================
    KEY    Example Value Type Comment
    ====== ============= ==== =======================
    NAXIS1 259           int  width of table in bytes
    NAXIS2 4469949       int  number of rows in table
    DESIDR edr           str  DESI Data Release
    ====== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns


========================== ========= ============ ===============================================================================================================================
Name                       Type      Units        Description
========================== ========= ============ ===============================================================================================================================
LOCATION                   int64                  Location on the focal plane PETAL_LOC*1000 + DEVICE_LOC
FIBER                      int32                  Fiber ID on the CCDs [0-4999]
TARGETID                   int64                  Unique DESI target ID
RA                         float64   deg          Target Right Ascension
DEC                        float64   deg          Target declination
TILEID                     int64                  Unique DESI tile ID
ZWARN                      int64                  Redshift warning bitmask from Redrock
COADD_FIBERSTATUS          int32                  bitwise-AND of input FIBERSTATUS
FIBERASSIGN_X              float32   mm           Fiberassign expected CS5 X location on focal plane
FIBERASSIGN_Y              float32   mm           Fiberassign expected CS5 Y location on focal plane
PRIORITY                   int32                  Target current priority
COADD_NUMEXP               int16                  Number of exposures in coadd
COADD_EXPTIME              float32   s            Summed exposure time for coadd
COADD_NUMNIGHT             int16                  Number of nights in coadd
MEAN_DELTA_X               float32   mm           Mean (over exposures) fiber difference requested - actual CS5 X location on focal plane
RMS_DELTA_X                float32   mm           RMS (over exposures) of the fiber difference between measured and requested CS5 X location on focal plane
MEAN_DELTA_Y               float32   mm           Mean (over exposures) fiber difference requested - actual CS5 Y location on focal plane
RMS_DELTA_Y                float32   mm           RMS (over exposures) of the fiber difference between measured and requested CS5 Y location on focal plane
MEAN_PSF_TO_FIBER_SPECFLUX float32                Mean of input exposures fraction of light from point-like source captured by 1.5 arcsec diameter fiber given atmospheric seeing
TSNR2_ELG_B                float32                ELG B template (S/N)^2
TSNR2_LYA_B                float32                LYA B template (S/N)^2
TSNR2_BGS_B                float32                BGS B template (S/N)^2
TSNR2_QSO_B                float32                QSO B template (S/N)^2
TSNR2_LRG_B                float32                LRG B template (S/N)^2
TSNR2_ELG_R                float32                ELG R template (S/N)^2
TSNR2_LYA_R                float32                LYA R template (S/N)^2
TSNR2_BGS_R                float32                BGS R template (S/N)^2
TSNR2_QSO_R                float32                QSO R template (S/N)^2
TSNR2_LRG_R                float32                LRG R template (S/N)^2
TSNR2_ELG_Z                float32                ELG Z template (S/N)^2
TSNR2_LYA_Z                float32                LYA Z template (S/N)^2
TSNR2_BGS_Z                float32                BGS Z template (S/N)^2
TSNR2_QSO_Z                float32                QSO Z template (S/N)^2
TSNR2_LRG_Z                float32                LRG Z template (S/N)^2
TSNR2_ELG                  float32                ELG template (S/N)^2 summed over B,R,Z
TSNR2_LYA                  float32                LYA template (S/N)^2 summed over B,R,Z
TSNR2_BGS                  float32                BGS template (S/N)^2 summed over B,R,Z
TSNR2_QSO                  float32                QSO template (S/N)^2 summed over B,R,Z
TSNR2_LRG                  float32                LRG template (S/N)^2 summed over B,R,Z
TILELOCID                  int64                  Is 10000*TILEID+LOCATION
GOODHARDLOC                logical                True/False whether the fiber had good hardware
ZPOSSLOC                   logical                True/False whether the location could have been assigned to the given target class
NTILE                      int64                  Number of tiles target was available on
TILES                      char[51]               TILEIDs of those tile, in string form separated by &#x27;-&#x27;
TILELOCIDS                 char[159]              TILELOCIDs that the target was available for, separated by &#x27;-&#x27;
RELEASE                    int16                  Imaging surveys release ID
BRICKID                    int32                  Brick ID from tractor input
BRICKNAME                  char[8]                Brick name from tractor input
BRICK_OBJID                int32                  Imaging Surveys OBJID on that brick
NOBS_G                     int16                  Number of images for central pixel in g-band
NOBS_R                     int16                  Number of images for central pixel in r-band
NOBS_Z                     int16                  Number of images for central pixel in z-band
PSFDEPTH_G                 float32   nanomaggy^-2 PSF-based depth in g-band
PSFDEPTH_R                 float32   nanomaggy^-2 PSF-based depth in r-band
PSFDEPTH_Z                 float32   nanomaggy^-2 PSF-based depth in z-band
GALDEPTH_G                 float32   nanomaggy^-2 Galaxy model-based depth in g-band
GALDEPTH_R                 float32   nanomaggy^-2 Galaxy model-based depth in r-band
GALDEPTH_Z                 float32   nanomaggy^-2 Galaxy model-based depth in z-band
PSFDEPTH_W1                float32   nanomaggy^-2 PSF-based depth in WISE W1
PSFDEPTH_W2                float32   nanomaggy^-2 PSF-based depth in WISE W2
PSFSIZE_G                  float32   arcsec       Median PSF size evaluated at the BRICK_PRIMARY objects in this brick in g-band
PSFSIZE_R                  float32   arcsec       Median PSF size evaluated at the BRICK_PRIMARY objects in this brick in r-band
PSFSIZE_Z                  float32   arcsec       Median PSF size evaluated at the BRICK_PRIMARY objects in this brick in z-band
APFLUX_G                   float32   nanomaggy    Total flux in nanomaggies extracted in a 0.75 arcsec radius in the g band at this location
APFLUX_R                   float32   nanomaggy    Total flux in nanomaggies extracted in a 0.75 arcsec radius in the r band at this location
APFLUX_Z                   float32   nanomaggy    Total flux in nanomaggies extracted in a 0.75 arcsec radius in the z band at this location
APFLUX_IVAR_G              float32   nanomaggy^-2 Inverse variance of APFLUX_G
APFLUX_IVAR_R              float32   nanomaggy^-2 Inverse variance of APFLUX_R
APFLUX_IVAR_Z              float32   nanomaggy^-2 Inverse variance of APFLUX_Z
MASKBITS                   int16                  Bitwise mask from the imaging indicating potential issue or blending
WISEMASK_W1                binary                 Bitwise mask for WISE W1 data
WISEMASK_W2                binary                 Bitwise mask for WISE W2 data
EBV                        float32   mag          Galactic extinction E(B-V) reddening from SFD98
PHOTSYS                    char[1]                &#x27;N&#x27; for the MzLS/BASS photometric system, &#x27;S&#x27; for DECaLS
HPXPIXEL                   int64                  HEALPixel containing this location at NSIDE=64 in the NESTED scheme
GOODPRI                    logical                True/False whether the priority of what was assigned to the location was &lt;= the base priority of the given target class
GOODTSNR                   logical                True/False whether the TSNR_&lt;class&gt; value used was above the minimum threshold for the given target class
ROSETTE_NUMBER             int64                  Rosette number ID [0-19]
ROSETTE_R                  float64   deg          Radius from the center of the rosette to the target
COMP_TILE                  float64                Assignment completeness for all targets of this type with the same value for TILES
LRG_MASK [1]_              binary                 Imaging mask bits relevant to LRG targets
========================== ========= ============ ===============================================================================================================================

.. [1] Only present in LRG samples

