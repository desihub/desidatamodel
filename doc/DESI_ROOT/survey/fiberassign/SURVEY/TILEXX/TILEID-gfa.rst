===============
TILEID-gfa.fits
===============

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``{TILEID}-gfa.fits``, where ``{TILEID}`` is the zero-padded,
    6-digit TILED.
:Regex: ``[0-9]{6}-gfa\.fits``
:File Type: FITS, 6 MB

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    Empty HDU
HDU1_  TARGETS BINTABLE *Brief Description*
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = TARGETS

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ============= ==== =======================
    KEY      Example Value Type Comment
    ======== ============= ==== =======================
    NAXIS1   164           int  width of table in bytes
    NAXIS2   43904         int  number of rows in table
    SURVEY   main          str
    RESOLVE  T             bool
    MASKBITS T             bool
    BACKUP   F             bool
    NOSEC    F             bool
    DR       9             int
    ======== ============= ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

================================= ======= ============ =======================================================================================================================================
Name                              Type    Units        Description
================================= ======= ============ =======================================================================================================================================
RELEASE                           int32                Imaging surveys release ID
TARGETID                          int64                Unique DESI target ID
BRICKID                           int32                Brick ID from tractor input
BRICK_OBJID                       int32                Imaging Surveys OBJID on that brick
RA                                float64 deg          Barycentric Right Ascension in ICRS
DEC                               float64 deg          Barycentric declination in ICRS
RA_IVAR                           float32 deg^-2       Inverse variance of RA (no cosine term!), excluding astrometric calibration errors
DEC_IVAR                          float32 deg^-2       Inverse variance of DEC, excluding astrometric calibration errors
MORPHTYPE                         char[4]              Imaging Surveys morphological type from Tractor
MASKBITS                          int16                Bitwise mask from the imaging indicating potential issue or blending
FLUX_G                            float32 nanomaggy    Flux in the Legacy Survey g-band (AB)
FLUX_R                            float32 nanomaggy    Flux in the Legacy Survey r-band (AB)
FLUX_Z                            float32 nanomaggy    Flux in the Legacy Survey z-band (AB)
FLUX_IVAR_G                       float32 nanomaggy^-2 Inverse variance of FLUX_G (AB)
FLUX_IVAR_R                       float32 nanomaggy^-2 Inverse variance of FLUX_R (AB)
FLUX_IVAR_Z                       float32 nanomaggy^-2 Inverse variance of FLUX_Z (AB)
REF_ID                            int64                Tyc1*1,000,000+Tyc2*10+Tyc3 for Tycho-2; ``sourceid`` for Gaia DR2
REF_CAT                           char[2]              Reference catalog source for star: &#x27;T2&#x27; for Tycho-2, &#x27;G2&#x27; for Gaia DR2, &#x27;L2&#x27; for the SGA, empty otherwise
REF_EPOCH                         float32 yr           Reference epoch for Gaia/Tycho astrometry. Typically 2015.5 for Gaia
PARALLAX                          float32 mas          Reference catalog parallax
PARALLAX_IVAR                     float32 mas^-2       Inverse variance of PARALLAX
PMRA                              float32 mas / yr     proper motion in the +RA direction (already including cos(dec))
PMDEC                             float32 mas / yr     Proper motion in the +Dec direction
PMRA_IVAR                         float32 yr^2 / mas^2 Inverse variance of PMRA
PMDEC_IVAR                        float32 yr^2 / mas^2 Inverse variance of PMDEC
GAIA_PHOT_G_MEAN_MAG              float32 mag          Gaia G band magnitude
GAIA_PHOT_G_MEAN_FLUX_OVER_ERROR  float32              Gaia G band signal-to-noise
GAIA_PHOT_BP_MEAN_MAG             float32 mag          Gaia BP band magnitude
GAIA_PHOT_BP_MEAN_FLUX_OVER_ERROR float32              Gaia BP band signal-to-noise
GAIA_PHOT_RP_MEAN_MAG             float32 mag          Gaia RP band magnitude
GAIA_PHOT_RP_MEAN_FLUX_OVER_ERROR float32              Gaia RP band signal-to-noise
GAIA_ASTROMETRIC_EXCESS_NOISE     float32              Gaia astrometric excess noise
URAT_ID                           int64                ID in the URAT catalog for sources where URAT supplemented missing Gaia astrometric information
URAT_SEP                          float32 arcsec       Separation between URAT and Gaia sources where URAT supplemented missing Gaia astrometric information
GAIA_PHOT_G_N_OBS                 int32                Gaia G band number of observations
HPXPIXEL                          int64                HEALPixel containing this location at NSIDE=64 in the NESTED scheme
================================= ======= ============ =======================================================================================================================================


Notes and Examples
==================

Some units in this file do not conform to the FITS standard:

* deg^-2 is incorrectly recorded as 1/deg^2
* nanomaggy^-2 is incorrectly recorded as 1/nanomaggy^2
* mas^-2 is incorrectly recorded as 1/mas^2

Such issues can typically be fixed by parsing the unit through astropy after reading in a Table, e.g.:

.. code-block:: python

    import astropy.units as u
    from astropy.table import Table
    objs = Table.read(filename, 1)
    u.Unit(str(objs["RA_IVAR"].unit))
