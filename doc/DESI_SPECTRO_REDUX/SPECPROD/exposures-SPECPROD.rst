=======================
exposures-SPECPROD.fits
=======================

:Summary: File containing metadata about individual DESI exposures. There are two tables.
    The first is per-exposure and the second is per-camera per-exposure. The per-exposure table
    includes observational information as well as derived quantities
    estimating the observational depth for each target class, quoted
    in seconds of effective, idealized observing time. The second provides similar information on
    a per-camera basis.
:Naming Convention: ``exposures-{SPECPROD}.fits``, where ``{SPECPROD}`` is the
    official name of the full reduction, *e.g.* ``everest``.
:Regex: ``exposures-[a-z0-9_-]+\.fits``
:File Type: FITS, 19 MB

Contents
========

====== ========= ======== ===================
Number EXTNAME   Type     Contents
====== ========= ======== ===================
HDU0_            IMAGE    Empty
HDU1_  EXPOSURES BINTABLE Per-exposure metadata
HDU2_  FRAMES    BINTABLE Per-camera per-exposure metadata
====== ========= ======== ===================


FITS Header Units
=================

HDU0
----

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = EXPOSURES

Binary table containing metadata about individual DESI exposures. This
includes observational information as well as derived quantities
estimating the observational depth for each target class, quoted
in seconds of effective, idealized observing time.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =====================
    KEY    Example Value Type Comment
    ====== ============= ==== =====================
    NAXIS1 337           int  Number of columns
    NAXIS2 3912          int  Number of exposure rows
    ====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

====================== ======== ============= =================================
Name                   Type     Units         Description
====================== ======== ============= =================================
NIGHT                  int32                  Observing night
EXPID                  int32                  DESI Exposure number
TILEID                 int32                  DESI Tile ID
TILERA                 float64  deg           RA of tile given in fiberassign file
TILEDEC                float64  deg           DEC of tile given in fiberassign fileDEC of tile given in fiberassign file
MJD                    float64                Modified Julian Date when shutter was opened for this exposure.
SURVEY                 char[7]                Survey name
PROGRAM                char[6]                Program name
FAPRGRM                char[*]                Fiberassign program name
FAFLAVOR               char[*]                Fiberassign flavor name
EXPTIME                float64  s             Length of time shutter was open.
EFFTIME_SPEC           float64  s             Effective exposure time for nominal conditions derived from the TSNR2 fits to the spectroscopy
GOALTIME               float64  s             Goal for total effective exposure time for the tile
GOALTYPE               char[6]                The intended observing conditions for the tile
MINTFRAC               float64                Minimum fraction of GOALTIME acceptable for considering a tile complete
AIRMASS                float32                Average airmass during this exposure.
EBV                    float64                Galactic extinction E(B-V) reddening from SFD98_
SEEING_ETC             float64  arcsec        Average FWHM atmospheric seeing during this exposure as measured by ETC.
EFFTIME_ETC            float32  s             Effective exposure time for nominal conditions inferred from ETC data
TSNR2_ELG              float32                ELG template (S/N)^2 summed over B,R,Z
TSNR2_QSO              float32                QSO template (S/N)^2 summed over B,R,Z
TSNR2_LRG              float32                LRG template (S/N)^2 summed over B,R,Z
TSNR2_LYA              float64                LYA template (S/N)^2 summed over B,R,Z
TSNR2_BGS              float32                BGS template (S/N)^2 summed over B,R,Z
TSNR2_GPBDARK          float32                GPBDARK template (S/N)^2 summed over B,R,Z
TSNR2_GPBBRIGHT        float32                GPBBRIGHT template (S/N)^2 summed over B,R,Z
TSNR2_GPBBACKUP        float32                GPBBACKUP template (S/N)^2 summed over B,R,Z
LRG_EFFTIME_DARK       float32  s             Effective exposure time for nominal dark conditions inferred for LRG targets
ELG_EFFTIME_DARK       float32  s             Effective exposure time for nominal dark conditions inferred for ELG targets
BGS_EFFTIME_BRIGHT     float32  s             Effective exposure time for nominal bright conditions inferred for BGS targets
LYA_EFFTIME_DARK       float64  s             Effective exposure time for nominal dark conditions inferred for LYA targets
GPB_EFFTIME_DARK       float32  s             Effective exposure time for nominal dark conditions inferred for GPB targets
GPB_EFFTIME_BRIGHT     float32  s             Effective exposure time for nominal bright conditions inferred for GPB targets
GPB_EFFTIME_BACKUP     float32  s             Effective exposure time for nominal backup conditions inferred for GPB targets
TRANSPARENCY_GFA       float64                Average airmass during this exposure as measured by GFA.
SEEING_GFA             float64  arcsec        Average FWHM atmospheric seeing during this exposure as measured by GFA.
FIBER_FRACFLUX_GFA     float64                Fraction of the flux entering the fiber relative to nominal 1.1" seeing using the PSF inferred from the GFAs
FIBER_FRACFLUX_ELG_GFA float64                Fraction of the flux entering the fiber relative to nominal 1.1" seeing using the PSF inferred from the GFAs for a source with an ELG profile (0.45" exponential galaxy profile)
FIBER_FRACFLUX_BGS_GFA float64                Fraction of the flux entering the fiber relative to nominal 1.1" seeing using the PSF inferred from the GFAs for a source with a BGS profile (deV profile, half light radius of 1.5")
FIBERFAC_GFA           float64                Fraction of light entering a fiber relative to expectations for 1.1" seeing, transparency 1, for an object with a PSF profile, measured by comparing the flux integrated over a 107 micron diameter circle on the GFA images centered at the PlateMaker expectations for where stars should land.
FIBERFAC_ELG_GFA       float64                Same as FIBERFAC_GFA except for an ELG profile
FIBERFAC_BGS_GFA       float64                Same as FIBERFAC_GFA except for a BGS profile
AIRMASS_GFA            float64                Average airmass during this exposure as measured by GFA.
SKY_MAG_AB_GFA         float64  mag arcsec^-2 Sky background in the GFA passband, measured from the GFA backgrounds.
SKY_MAG_G_SPEC         float64  mag arcsec^-2 Sky background measured in the spectroscopy integrated over the DECam g passband, AB mags.
SKY_MAG_R_SPEC         float64  mag arcsec^-2 Sky background measured in the spectroscopy integrated over the DECam r passband, AB mags.
SKY_MAG_Z_SPEC         float64  mag arcsec^-2 Sky background measured in the spectroscopy integrated over the DECam z passband, AB mags.
EFFTIME_GFA            float64  s             Effective exposure time for nominal conditions inferred from GFA data
EFFTIME_DARK_GFA       float64  s             Effective exposure time for nominal dark conditions inferred from GFA data
EFFTIME_BRIGHT_GFA     float64  s             Effective exposure time for nominal bright conditions inferred from GFA data
EFFTIME_BACKUP_GFA     float64  s             Effective exposure time for nominal backup conditions inferred from GFA data
====================== ======== ============= =================================

.. _SFD98: https://ui.adsabs.harvard.edu/abs/1998ApJ...500..525S/abstract

HDU2
----

EXTNAME = FRAMES

Binary table containing metadata about individual DESI exposures per camera. This
includes observational information as well as derived quantities
estimating the observational depth for each target class, quoted
as TSNR2_*. TSNR2_* can be converted to EFFTIME using the desispec_ function
*desispec.tsnr.tsnr2_to_efftime(tsnr2,target_type)*.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ====== ============= ==== =====================
    KEY    Example Value Type Comment
    ====== ============= ==== =====================
    NAXIS1 167           int  Number of columns
    NAXIS2 111720        int  Number of per-camera per-exposure rows
    ====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: keywords

=============== ======== ====== ===========
Name            Type     Units  Description
=============== ======== ====== ===========
NIGHT           int32           Observing night
EXPID           int32           DESI Exposure number
TILEID          int32           DESI Tile ID
TILERA          float64  deg    RA of tile given in fiberassign file
TILEDEC         float64  deg    DEC of tile given in fiberassign file
MJD             float64         Modified Julian Date when shutter was opened for this exposure.
EXPTIME         float32  s      Length of time shutter was open.
AIRMASS         float32         Average airmass during this exposure.
EBV             float64         Galactic extinction E(B-V) reddening from SFD98_
SEEING_ETC      float64  arcsec Average FWHM atmospheric seeing during this exposure as measured by ETC.
EFFTIME_ETC     float32  s      Effective exposure time for nominal conditions derived from exposure ETC data
CAMERA          char[2]         Camera identifier. Passband and SPECGRPH ([brz][0-9]).
TSNR2_GPBDARK   float32         GPBDARK template (S/N)^2 summed over B,R,Z
TSNR2_ELG       float32         ELG template (S/N)^2 summed over B,R,Z
TSNR2_GPBBRIGHT float32         GPBBRIGHT template (S/N)^2 summed over B,R,Z
TSNR2_LYA       float64         LYA template (S/N)^2 summed over B,R,Z
TSNR2_BGS       float32         BGS template (S/N)^2 summed over B,R,Z
TSNR2_GPBBACKUP float32         GPBBACKUP template (S/N)^2 summed over B,R,Z
TSNR2_QSO       float32         QSO template (S/N)^2 summed over B,R,Z
TSNR2_LRG       float32         LRG template (S/N)^2 summed over B,R,Z
SURVEY          char[7]         Survey name
GOALTYPE        char[6]         The intended observing conditions for the tile
FAPRGRM         char[*]         PROGRAM in fiberassign file
FAFLAVOR        char[*]         FLAVOR in fiberassign file
MINTFRAC        float64         Minimum fraction of GOALTIME acceptable for considering a tile complete
GOALTIME        float64  s      Goal for total effective exposure time for the tile
=============== ======== ====== ===========

.. _SFD98: https://ui.adsabs.harvard.edu/abs/1998ApJ...500..525S/abstract
.. _desispec: https://github.com/desihub/desispec/blob/720153babcf85dd93530252b0c1f631d48edfc0d/py/desispec/tsnr.py#L1140

Notes and Examples
==================

This file is based on the ``guadalupe`` production.  There are minor
type differences for these columns in both HDU1 and HDU2: ``FAPRGRM``,
``FAFLAVOR``, ``EBV``, ``EFFTIME_ETC``.  Type warnings about these
columns should be ignored.
