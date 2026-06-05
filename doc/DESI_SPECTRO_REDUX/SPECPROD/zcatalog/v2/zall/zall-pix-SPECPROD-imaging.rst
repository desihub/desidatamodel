==============================
zall-pix-SPECPROD-imaging.fits
==============================

:Summary: Concatenation of all ``zpix-*-imaging.fits`` files, combining Legacy
          Survey imaging photometry columns across all SURVEYs and PROGRAMs.
:Naming Convention: ``zcatalog/v2/zall/zall-pix-{SPECPROD}-imaging.fits``, where ``{SPECPROD}``
    is the official name of the full reduction, *e.g.* ``iron``.
:Regex: ``zall-pix-[a-z0-9_-]+-imaging\.fits``
:File Type: FITS, ~10 GB

This file is row-matched to :doc:`zall-pix-SPECPROD.fits <./zall-pix-SPECPROD>`
and contains the imaging photometry columns stacked from all
:doc:`zpix-*-imaging.fits <../SURVEY/zpix-SURVEY-PROGRAM-imaging>` files.

Contents
========

====== ================ ======== ============================================================
Number EXTNAME          Type     Contents
====== ================ ======== ============================================================
HDU0_  PRIMARY          IMAGE    Empty
HDU1_  ZCATALOG_IMAGING BINTABLE Legacy Survey imaging photometry columns
====== ================ ======== ============================================================


FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ============ ================ ==== =======================
    KEY          Example Value    Type Comment
    ============ ================ ==== =======================
    CHECKSUM     9aaGCVYE9aaECUYE str  HDU checksum
    DATASUM      0                str  data unit checksum
    ZCATVER      v2               str  Version of zcatalog files
    ============ ================ ==== =======================

Empty HDU.

HDU1
----

EXTNAME = ZCATALOG_IMAGING

Legacy Survey (`LS`_) imaging photometry columns stacked from all
:doc:`zpix-SURVEY-PROGRAM-imaging.fits <../SURVEY/zpix-SURVEY-PROGRAM-imaging>` files.
Column definitions are identical to that file; see it for descriptions.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ============ ================ ==== =======================
    KEY          Example Value    Type Comment
    ============ ================ ==== =======================
    NAXIS1       228              int  width of table in bytes
    NAXIS2       3000000          int  number of rows in table
    CHECKSUM     QA6lQ26iQ96iQ96i str  HDU checksum
    DATASUM      4284326946       str  data unit checksum
    ZCATVER      v2               str  Version of zcatalog files
    ============ ================ ==== =======================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

========================== =========== ============ =====================================================================================================================================
Name                       Type        Units        Description
========================== =========== ============ =====================================================================================================================================
TARGETID                   int64                    Unique DESI target ID
HEALPIX                    int32                    HEALPixel containing this location at NSIDE=64 in the NESTED scheme
PMRA                       float32     mas yr^-1    Reference catalog proper motion in the RA direction
PMDEC                      float32     mas yr^-1    Reference catalog proper motion in the Dec direction
REF_EPOCH                  float32     yr           Reference catalog reference epoch (*e.g.*, 2015.5 for `Gaia`_ DR2)
RELEASE                    int16                    Legacy Surveys (`LS`_) `Release`_
BRICKNAME                  char[8]                  Brick name from tractor input
BRICKID                    int32                    Brick ID from tractor input
BRICK_OBJID                int32                    OBJID (unique to brick, but not to file)
MORPHTYPE                  char[4]                  `Morphological Model`_ type
EBV                        float32     mag          Galactic extinction E(B-V) reddening from SFD98_
FLUX_G                     float32     nanomaggy    `LS`_ flux from tractor input (g)
FLUX_R                     float32     nanomaggy    `LS`_ flux from tractor input (r)
FLUX_Z                     float32     nanomaggy    `LS`_ flux from tractor input (z)
FLUX_W1                    float32     nanomaggy    WISE flux in W1
FLUX_W2                    float32     nanomaggy    WISE flux in W2
FLUX_IVAR_G                float32     nanomaggy^-2 Inverse Variance of FLUX_G
FLUX_IVAR_R                float32     nanomaggy^-2 Inverse Variance of FLUX_R
FLUX_IVAR_Z                float32     nanomaggy^-2 Inverse Variance of FLUX_Z
FLUX_IVAR_W1               float32     nanomaggy^-2 Inverse Variance of FLUX_W1
FLUX_IVAR_W2               float32     nanomaggy^-2 Inverse Variance of FLUX_W2
FIBERFLUX_G                float32     nanomaggy    Predicted g-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERFLUX_R                float32     nanomaggy    Predicted r-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERFLUX_Z                float32     nanomaggy    Predicted z-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing
FIBERTOTFLUX_G             float32     nanomaggy    Predicted g-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
FIBERTOTFLUX_R             float32     nanomaggy    Predicted r-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
FIBERTOTFLUX_Z             float32     nanomaggy    Predicted z-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing
MASKBITS                   int16                    Bitwise mask indicating that an object touches a pixel in the ``coadd/*/*/*maskbits*`` maps, as cataloged on the `DR9 bitmasks page`_
SERSIC                     float32                  Power-law index for the Sersic profile model (``type="SER"``)
SHAPE_R                    float32     arcsec       Half-light radius of galaxy model for galaxy type ``type`` (>0)
SHAPE_E1                   float32                  `Ellipticity component`_ 1 of galaxy model for galaxy type ``type``
SHAPE_E2                   float32                  `Ellipticity component`_ 2 of galaxy model for galaxy type ``type``
REF_ID                     int64                    Tyc1*1,000,000+Tyc2*10+Tyc3 for `Tycho-2`_; "sourceid" for `Gaia`_ DR2
REF_CAT                    char[2]                  Reference catalog source for this star: "T2" for `Tycho-2`_, "G2" for `Gaia`_ DR2, "L3" for the SGA_, empty otherwise
GAIA_PHOT_G_MEAN_MAG       float32     mag          `Gaia`_ G band magnitude
GAIA_PHOT_BP_MEAN_MAG      float32     mag          `Gaia`_ BP band magnitude
GAIA_PHOT_RP_MEAN_MAG      float32     mag          `Gaia`_ RP band magnitude
PARALLAX                   float32     mas          Reference catalog parallax
PHOTSYS                    char[1]                  'N' for the MzLS/BASS photometric system, 'S' for DECaLS
========================== =========== ============ =====================================================================================================================================

.. _`LS`: https://www.legacysurvey.org/
.. _`DR9 bitmasks page`: https://www.legacysurvey.org/dr9/bitmasks
.. _`ellipticity component`: https://www.legacysurvey.org/dr9/catalogs/#ellipticities
.. _`Release`: https://www.legacysurvey.org/release/
.. _`Morphological Model`: https://www.legacysurvey.org/dr9/catalogs/#goodness-of-fits-and-morphological-type
.. _`Tycho-2`: https://heasarc.gsfc.nasa.gov/W3Browse/all/tycho2.html
.. _`Gaia`: https://gea.esac.esa.int/archive/documentation//GDR2/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html
.. _SFD98: https://ui.adsabs.harvard.edu/abs/1998ApJ...500..525S/abstract
.. _SGA: https://www.legacysurvey.org/sga/sga2020
