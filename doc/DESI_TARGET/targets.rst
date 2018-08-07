=======
targets
=======

:Summary: DESI target selection files contain a single binary table covering the
    entire footprint.  They contain the variables used by target selection
    (*e.g.* fluxes), variables needed by fiber assignment (*e.g.* RA, DEC),
    and variables needed for traceability (*e.g.* TARGETFLAG, TARGETID).
:Naming Convention: ``targets-DRX-VERSION.fits``, where ``DRX`` is the
    imaging surveys data release name (e.g. dr7.1) and ``VERSION`` is the
    desitarget code version defining the cuts (e.g. 0.22.0).
:Regex: ``targets-dr[0.9]+\.[0-9]+-v?[0-9]+\.[0-9]+(\.[0-9]+|)\.fits``
:File Type: FITS, 30 GB


**Note**: this documents the target catalog format starting with DR7 /
desitarget 0.22.0 .  The previous format is documented in :doc:`targets-dr6`.

Contents
========

====== ======= ======== ============
Number EXTNAME Type     Contents
====== ======= ======== ============
HDU0_  PRIMARY IMAGE    Empty
HDU1_  TARGETS BINTABLE Target table
====== ======= ======== ============

FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = TARGETS

Target selection table

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============= ==== ==================================
KEY      Example Value Type Comment
======== ============= ==== ==================================
NAXIS1   374           int  width of table in bytes
NAXIS2   72660205      int  number of rows in table
ENCODING ascii         str
SEED     1028862084    int  initial random seed
HPXNSIDE 64            int  HEALPix nside
HPXNEST  T             bool HEALPix nested (not ring) ordering
======== ============= ==== ==================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

================================= ========== ===== ===================
Name                              Type       Units Description
================================= ========== ===== ===================
RELEASE                           int32            Legacy Surveys (`LS`_) `Release`_
BRICKID                           int32            Brick ID from tractor input
BRICKNAME                         char[8]          Brick name from tractor input
BRICK_OBJID                       int32            OBJID (unique to brick, but not to file)
TYPE                              char[4]          `Morphological Model`_
RA                                float64          Right ascension [degrees]
DEC                               float64          Declination [degrees]
RA_IVAR                           float32          Inverse Variance of RA [degrees]
DEC_IVAR                          float32          Inverse Variance of DEC [degrees]
DCHISQ                            float32[5]       Difference in chi-squared between model fits
FLUX_G                            float32          `LS`_ flux from tractor input (g)
FLUX_R                            float32          `LS`_ flux from tractor input (r)
FLUX_Z                            float32          `LS`_ flux from tractor input (z)
FLUX_W1                           float32          WISE flux in W1
FLUX_W2                           float32          WISE flux in W2
FLUX_W3                           float32          WISE flux in W3
FLUX_W4                           float32          WISE flux in W4
FLUX_IVAR_G                       float32          Inverse Variance of FLUX_G
FLUX_IVAR_R                       float32          Inverse Variance of FLUX_R
FLUX_IVAR_Z                       float32          Inverse Variance of FLUX_Z
FLUX_IVAR_W1                      float32          Inverse Variance of FLUX_W1
FLUX_IVAR_W2                      float32          Inverse Variance of FLUX_W2
FLUX_IVAR_W3                      float32          Inverse Variance of FLUX_W3
FLUX_IVAR_W4                      float32          Inverse Variance of FLUX_W4
MW_TRANSMISSION_G                 float32          Milky Way dust transmission in `LS`_ g
MW_TRANSMISSION_R                 float32          Milky Way dust transmission in `LS`_ r
MW_TRANSMISSION_Z                 float32          Milky Way dust transmission in `LS`_ z
MW_TRANSMISSION_W1                float32          Milky Way dust transmission in WISE W1
MW_TRANSMISSION_W2                float32          Milky Way dust transmission in WISE W2
MW_TRANSMISSION_W3                float32          Milky Way dust transmission in WISE W3
MW_TRANSMISSION_W4                float32          Milky Way dust transmission in WISE W4
NOBS_G                            int16            Number of images for central pixel in `LS`_ g
NOBS_R                            int16            Number of images for central pixel in `LS`_ r
NOBS_Z                            int16            Number of images for central pixel in `LS`_ z
FRACFLUX_G                        float32          Fraction of flux from other sources compared to this source in `LS`_ g
FRACFLUX_R                        float32          Fraction of flux from other sources compared to this source in `LS`_ r
FRACFLUX_Z                        float32          Fraction of flux from other sources compared to this source in `LS`_ z
FRACMASKED_G                      float32          Fraction of pixels masked for this source in `LS`_ g
FRACMASKED_R                      float32          Fraction of pixels masked for this source in `LS`_ r
FRACMASKED_Z                      float32          Fraction of pixels masked for this source in `LS`_ z
ALLMASK_G                         int16            Bitwise mask for central pixel in `LS`_ g
ALLMASK_R                         int16            Bitwise mask for central pixel in `LS`_ r
ALLMASK_Z                         int16            Bitwise mask for central pixel in `LS`_ z
PSFDEPTH_G                        float32          PSF-based depth in `LS`_ g
PSFDEPTH_R                        float32          PSF-based depth in `LS`_ r
PSFDEPTH_Z                        float32          PSF-based depth in `LS`_ z
GALDEPTH_G                        float32          Galaxy model-based depth in `LS`_ g
GALDEPTH_R                        float32          Galaxy model-based depth in `LS`_ r
GALDEPTH_Z                        float32          Galaxy model-based depth in `LS`_ z
FRACDEV                           float32          Fraction of model in deVaucouleurs profile
FRACDEV_IVAR                      float32          Inverse variance of FRACDEV
SHAPEDEV_R                        float32          Half-light radius of deVaucouleurs model
SHAPEDEV_R_IVAR                   float32          Inverse variance of SHAPEDEV_R
SHAPEDEV_E1                       float32          `Ellipticity component`_ 1 of deVaucouleurs model
SHAPEDEV_E1_IVAR                  float32          Inverse variance of SHAPEDEV_E1
SHAPEDEV_E2                       float32          `Ellipticity component`_ 2 of deVaucouleurs model
SHAPEDEV_E2_IVAR                  float32          Inverse variance of SHAPEDEV_E2
SHAPEEXP_R                        float32          Half-light radius of exponential model
SHAPEEXP_R_IVAR                   float32          Inverse variance of SHAPEEXP_R
SHAPEEXP_E1                       float32          `Ellipticity component`_ 1 of exponential model
SHAPEEXP_E1_IVAR                  float32          Inverse variance of SHAPEEXP_E1
SHAPEEXP_E2                       float32          `Ellipticity component`_ 2 of exponential model
SHAPEEXP_E2_IVAR                  float32          Inverse variance of SHAPEEXP_E2
REF_ID                            int64            Tyc1*1,000,000+Tyc2*10+Tyc3 for `Tycho2`_; "sourceid" for `Gaia`_ DR2 
GAIA_PHOT_G_MEAN_MAG              float32          `Gaia`_ G band magnitude
GAIA_PHOT_G_MEAN_FLUX_OVER_ERROR  float32          `Gaia`_ G band signal-to-noise
GAIA_PHOT_BP_MEAN_MAG             float32          `Gaia`_ BP band magnitude
GAIA_PHOT_BP_MEAN_FLUX_OVER_ERROR float32          `Gaia`_ BP band signal-to-noise
GAIA_PHOT_RP_MEAN_MAG             float32          `Gaia`_ RP band magnitude
GAIA_PHOT_RP_MEAN_FLUX_OVER_ERROR float32          `Gaia`_ RP band signal-to-noise
GAIA_ASTROMETRIC_EXCESS_NOISE     float32          `Gaia`_ astrometric excess noise
GAIA_DUPLICATED_SOURCE            logical          `Gaia`_ duplicated source flag
PARALLAX                          float32          Reference catalog parallax
PARALLAX_IVAR                     float32          Inverse variance of parallax
PMRA                              float32          Reference catalog proper motion in the RA direction
PMRA_IVAR                         float32          Inverse variance of PMRA
PMDEC                             float32          Reference catalog proper motion in the Dec direction
PMDEC_IVAR                        float32          Inverse variance of PMDEC
SUBPRIORITY                       float32          Priority that is used to break ties during fiber assignment
PHOTSYS                           char[1]          'N' for the MzLS/BASS photometric system, 'S' for DECaLS
TARGETID                          int64            ID (unique to file and the whole survey)
DESI_TARGET                       int64            DESI (dark time program) target selection bitmask
BGS_TARGET                        int64            BGS (bright time program) target selection bitmask
MWS_TARGET                        int64            MWS (bright time program) target selection bitmask
HPXPIXEL                          int64            HEALPixel containing target
================================= ========== ===== ===================


Notes and Examples
==================

In general, the above format contains:

* Columns that were used by target selection (e.g. FLUX_G/R/Z)
* Columns needed by fiber assignment (e.g. RA, DEC)
* Columns needed for traceability (e.g. BRICKNAME, TARGETID, DESI_TARGET, BGS_TARGET, MWS_TARGET)

FRACFLUX and FRACMASKED are profile-weighted quantities

SUBPRIORITY, PHOTSYS, TARGETID, DESI_TARGET, BGS_TARGET, MWS_TARGET and HPXPIXEL are created by target selection; the rest are passed through from the original input tractor or sweep files

See http://legacysurvey.org for more details about the columns from input tractor files

.. _`LS`: http://legacysurvey.org/dr7/catalogs/
.. _`ellipticity component`: http://legacysurvey.org/dr7/catalogs/
.. _`Release`: http://legacysurvey.org/release/
.. _`Morphological Model`: http://legacysurvey.org/dr7/catalogs/
.. _`Tycho2`: https://heasarc.nasa.gov/W3Browse/all/tycho2.html
.. _`Gaia`: https://gea.esac.esa.int/archive/documentation//GDR2/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html

