=================
zcatalog-SPECPROD
=================

:Summary: This file concatenates all
    :doc:`zbest <./spectra-NSIDE/PIXGROUP/PIXNUM/zbest-NSIDE-PIXNUM>` files
    and then cross matches them with the input target catalog.
:Naming Convention: ``zcatalog-{SPECPROD}.fits``, where ``{SPECPROD}`` is the
    :envvar:`SPECPROD` name of the reduction run.
:Regex: ``zcatalog-[a-z0-9_-]+\.fits``
:File Type: FITS, 14 MB

Contents
========

====== ======== ======== ===========================================
Number EXTNAME  Type     Contents
====== ======== ======== ===========================================
HDU0_           IMAGE    Empty
HDU1_  ZCATALOG BINTABLE Redshift catalog joined with target catalog
====== ======== ======== ===========================================


FITS Header Units
=================

HDU0
----

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = ZCATALOG

The concatenated redshift data for all
:doc:`zbest <./spectra-NSIDE/PIXGROUP/PIXNUM/zbest-NSIDE-PIXNUM>` files,
cross matched with the original input target catalog.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============= ===== =================================
KEY      Example Value Type  Comment
======== ============= ===== =================================
NAXIS1   332           int   width of table in bytes
NAXIS2   44215         int   number of targets (rows) in table
RRVER    0.13.2        str   Redrock version
TEMNAM00 GALAXY        str
TEMVER00 2.6           float
TEMNAM01 QSO           str
TEMVER01 unknown       str
TEMNAM02 STAR:::A      str
TEMVER02 unknown       str
TEMNAM03 STAR:::B      str
TEMVER03 unknown       str
TEMNAM04 STAR:::CV     str
TEMVER04 unknown       str
TEMNAM05 STAR:::F      str
TEMVER05 unknown       str
TEMNAM06 STAR:::G      str
TEMVER06 unknown       str
TEMNAM07 STAR:::K      str
TEMVER07 unknown       str
TEMNAM08 STAR:::M      str
TEMVER08 unknown       str
TEMNAM09 STAR:::WD     str
TEMVER09 unknown       str
======== ============= ===== =================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

================================= =========== ======= ===================
Name                              Type        Units   Description
================================= =========== ======= ===================
TARGETID                          int64               ID (unique to file and the whole survey)
CHI2                              float64             *Description needed*
COEFF                             float64[10]         *Description needed*
Z                                 float64             *Description needed*
ZERR                              float64             *Description needed*
ZWARN                             int64               *Description needed*
NPIXELS                           int64               *Description needed*
SPECTYPE                          char[6]             *Description needed*
SUBTYPE                           char[20]            *Description needed*
NCOEFF                            int64               *Description needed*
DELTACHI2                         float64             *Description needed*
NUMEXP                            int32               *Description needed*
NUMTILE                           int32               *Description needed*
RELEASE                           int16               Legacy Surveys (`LS`_) `Release`_
BRICKID                           int32               Brick ID from tractor input
BRICKNAME                         char[8]             Brick name from tractor input
BRICK_OBJID                       int32               OBJID (unique to brick, but not to file)
MORPHTYPE                         char[4]             `Morphological Model`_ type
RA                                float64     deg     Right ascension [degrees]
DEC                               float64     deg     Declination [degrees]
RA_IVAR                           float32     deg**-2 Right ascension inverse variance [1/degrees**2]
DEC_IVAR                          float32     deg**-2 Declination inverse variance [1/degrees**2]
FLUX_G                            float32             `LS`_ flux from tractor input (g)
FLUX_R                            float32             `LS`_ flux from tractor input (r)
FLUX_Z                            float32             `LS`_ flux from tractor input (z)
FLUX_W1                           float32             WISE flux in W1
FLUX_W2                           float32             WISE flux in W2
FLUX_W3                           float32             WISE flux in W3
FLUX_W4                           float32             WISE flux in W4
FLUX_IVAR_G                       float32             Inverse Variance of FLUX_G
FLUX_IVAR_R                       float32             Inverse Variance of FLUX_R
FLUX_IVAR_Z                       float32             Inverse Variance of FLUX_Z
FLUX_IVAR_W1                      float32             Inverse Variance of FLUX_W1
FLUX_IVAR_W2                      float32             Inverse Variance of FLUX_W2
FLUX_IVAR_W3                      float32             Inverse Variance of FLUX_W3
FLUX_IVAR_W4                      float32             Inverse Variance of FLUX_W4
MW_TRANSMISSION_G                 float32             Milky Way dust transmission in `LS`_ g
MW_TRANSMISSION_R                 float32             Milky Way dust transmission in `LS`_ r
MW_TRANSMISSION_Z                 float32             Milky Way dust transmission in `LS`_ z
MW_TRANSMISSION_W1                float32             Milky Way dust transmission in WISE W1
MW_TRANSMISSION_W2                float32             Milky Way dust transmission in WISE W2
MW_TRANSMISSION_W3                float32             Milky Way dust transmission in WISE W3
MW_TRANSMISSION_W4                float32             Milky Way dust transmission in WISE W4
NOBS_G                            int16               Number of images for central pixel in `LS`_ g
NOBS_R                            int16               Number of images for central pixel in `LS`_ r
NOBS_Z                            int16               Number of images for central pixel in `LS`_ z
FRACFLUX_G                        float32             Fraction of flux from other sources compared to this source in `LS`_ g
FRACFLUX_R                        float32             Fraction of flux from other sources compared to this source in `LS`_ r
FRACFLUX_Z                        float32             Fraction of flux from other sources compared to this source in `LS`_ z
FRACMASKED_G                      float32             Fraction of pixels masked for this source in `LS`_ g
FRACMASKED_R                      float32             Fraction of pixels masked for this source in `LS`_ r
FRACMASKED_Z                      float32             Fraction of pixels masked for this source in `LS`_ z
FRACIN_G                          float32             *Description needed*
FRACIN_R                          float32             *Description needed*
FRACIN_Z                          float32             *Description needed*
ALLMASK_G                         int16               Bitwise mask for central pixel in `LS`_ g
ALLMASK_R                         int16               Bitwise mask for central pixel in `LS`_ r
ALLMASK_Z                         int16               Bitwise mask for central pixel in `LS`_ z
WISEMASK_W1                       byte                *Description needed*
WISEMASK_W2                       byte                *Description needed*
PSFDEPTH_G                        float32             PSF-based depth in `LS`_ g
PSFDEPTH_R                        float32             PSF-based depth in `LS`_ r
PSFDEPTH_Z                        float32             PSF-based depth in `LS`_ z
GALDEPTH_G                        float32             Galaxy model-based depth in `LS`_ g
GALDEPTH_R                        float32             Galaxy model-based depth in `LS`_ r
GALDEPTH_Z                        float32             Galaxy model-based depth in `LS`_ z
FRACDEV                           float32             Fraction of model in deVaucouleurs profile
FRACDEV_IVAR                      float32             Inverse variance of FRACDEV
SHAPEDEV_R                        float32             Half-light radius of deVaucouleurs model
SHAPEDEV_R_IVAR                   float32             Inverse variance of SHAPEDEV_R
SHAPEDEV_E1                       float32             `Ellipticity component`_ 1 of deVaucouleurs model
SHAPEDEV_E1_IVAR                  float32             Inverse variance of SHAPEDEV_E1
SHAPEDEV_E2                       float32             `Ellipticity component`_ 2 of deVaucouleurs model
SHAPEDEV_E2_IVAR                  float32             Inverse variance of SHAPEDEV_E2
SHAPEEXP_R                        float32             Half-light radius of exponential model
SHAPEEXP_R_IVAR                   float32             Inverse variance of SHAPEEXP_R
SHAPEEXP_E1                       float32             `Ellipticity component`_ 1 of exponential model
SHAPEEXP_E1_IVAR                  float32             Inverse variance of SHAPEEXP_E1
SHAPEEXP_E2                       float32             `Ellipticity component`_ 2 of exponential model
SHAPEEXP_E2_IVAR                  float32             Inverse variance of SHAPEEXP_E2
FIBERFLUX_G                       float32             g-band object model flux for 1 arcsec seeing and 1.5 arcsec diameter fiber
FIBERFLUX_R                       float32             r-band object model flux for 1 arcsec seeing and 1.5 arcsec diameter fiber
FIBERFLUX_Z                       float32             z-band object model flux for 1 arcsec seeing and 1.5 arcsec diameter fiber
FIBERTOTFLUX_G                    float32             like FIBERFLUX_G but including all objects overlapping this location
FIBERTOTFLUX_R                    float32             like FIBERFLUX_R but including all objects overlapping this location
FIBERTOTFLUX_Z                    float32             like FIBERFLUX_Z but including all objects overlapping this location
REF_CAT                           char[2]             *Description needed*
REF_ID                            int64               Tyc1*1,000,000+Tyc2*10+Tyc3 for `Tycho-2`_; "sourceid" for `Gaia`_ DR2
GAIA_PHOT_G_MEAN_MAG              float32             `Gaia`_ G band magnitude
GAIA_PHOT_G_MEAN_FLUX_OVER_ERROR  float32             `Gaia`_ G band signal-to-noise
GAIA_PHOT_BP_MEAN_MAG             float32             `Gaia`_ BP band magnitude
GAIA_PHOT_BP_MEAN_FLUX_OVER_ERROR float32             `Gaia`_ BP band signal-to-noise
GAIA_PHOT_RP_MEAN_MAG             float32             `Gaia`_ RP band magnitude
GAIA_PHOT_RP_MEAN_FLUX_OVER_ERROR float32             `Gaia`_ RP band signal-to-noise
GAIA_PHOT_BP_RP_EXCESS_FACTOR     float32             *Description needed*
GAIA_ASTROMETRIC_SIGMA5D_MAX      float32             *Description needed*
GAIA_ASTROMETRIC_PARAMS_SOLVED    int64               *Description needed*
GAIA_ASTROMETRIC_EXCESS_NOISE     float32             `Gaia`_ astrometric excess noise
GAIA_DUPLICATED_SOURCE            bool                `Gaia`_ duplicated source flag
PARALLAX                          float32             Reference catalog parallax
PARALLAX_IVAR                     float32             Inverse variance of parallax
PMRA                              float32             Reference catalog proper motion in the RA direction
PMRA_IVAR                         float32             Inverse variance of PMRA
PMDEC                             float32             Reference catalog proper motion in the Dec direction
PMDEC_IVAR                        float32             Inverse variance of PMDEC
MASKBITS                          int16               *Description needed*
EBV                               float32             *Description needed*
PHOTSYS                           char[1]             'N' for the MzLS/BASS photometric system, 'S' for DECaLS
DESI_TARGET                       int64               DESI (dark time program) target selection bitmask
BGS_TARGET                        int64               BGS (bright time program) target selection bitmask
MWS_TARGET                        int64               MWS (bright time program) target selection bitmask
SUBPRIORITY                       float64             Random subpriority [0-1] to break assignment ties
OBSCONDITIONS                     int64               Flag the target to be observed in graytime.
PRIORITY_INIT                     int64               *Description needed*
NUMOBS_INIT                       int64               *Description needed*
HPXPIXEL                          int64               HEALPixel containing target
================================= =========== ======= ===================

.. _`LS`: http://legacysurvey.org/dr7/catalogs/
.. _`ellipticity component`: http://legacysurvey.org/dr7/catalogs/
.. _`Release`: http://legacysurvey.org/release/
.. _`Morphological Model`: http://legacysurvey.org/dr7/catalogs/
.. _`Tycho-2`: https://heasarc.nasa.gov/W3Browse/all/tycho2.html
.. _`Gaia`: https://gea.esac.esa.int/archive/documentation//GDR2/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html

Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
