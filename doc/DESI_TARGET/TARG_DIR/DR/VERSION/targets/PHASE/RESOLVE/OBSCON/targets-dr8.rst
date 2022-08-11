===========
targets-dr8
===========

:Summary: DESI target selection files include a single binary table containing
    the targets in a (nested) HEALPixel. They contain the variables used by
    target selection (*e.g.* fluxes), variables needed by fiber assignment (*e.g.*
    RA, DEC), and variables needed for traceability (*e.g.* DESITARGET, TARGETID).
:Naming Convention: ``PHASEtargets-OBSCON-RESOLVE-hp-HP.fits``,
    where ``PHASE`` is a specific DESI observational phase (*e.g.* svX with X=1,2
    for iterations of Survey Validation), ``OBSCON`` is the observing condition
    (or "layer") for the targets (*e.g.* dark), ``RESOLVE`` is "noresolve" for
    targets that are not resolved, and ``HP`` is the HEALPixel covered by the file
    at the (nested) HEALPixel nside included in the file header as ``FILENSID``
    (*e.g.* 11). For targets that are *not* resolved ``RESOLVE`` is omitted from
    the filename. For targets that are part of the DESI Main Science Survey
    ``PHASE`` is omitted from the filename.
:Regex: ``.*?targets-.*?-hp-?[0-9]+\.fits``
:File Type: FITS, 2 GB

**Note**: this documents the target catalog format starting with DR8 /
desitarget 0.31.0 .  The previous format is documented in :doc:`targets-dr7`.

Examples
========

For research notes detailing early target selections for DESI, target files
are available at:

https://data.desi.lbl.gov/public/ets/target/catalogs/dr8 .


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

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ============= ==== ==================================
    KEY      Example Value Type Comment
    ======== ============= ==== ==================================
    NAXIS1   374           int  width of table in bytes
    NAXIS2   72660205      int  number of rows in table
    OBSCON   DARK|GRAY     str  observing layer for file
    HPXNSIDE 64            int  HEALPix nside for column `HPXPIXEL`
    HPXNEST  T             bool HEALPix nested (not ring) ordering
    SURVEY   main          str  sv1 for SV, main for Main Survey
    RESOLVE  T             bool ``True`` if from unique imaging
    MASKBITS T             bool ``True`` if masking cuts applied
    SUPP     F             bool ``True`` for supplemental targets
    TCNAMES  "QSO,LRG"     str  run for this target-class subset
    FILENSID 2             int  HEALPix nside covered by file
    FILENEST T             bool HEALPix nested (not ring) ordering
    FILEHPX  11            int  HEALPix pixel(s) covered by file
    ======== ============= ==== ==================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

================================= ========== ===================== ===================
Name                              Type       Units                 Description
================================= ========== ===================== ===================
RELEASE                           int16                            Legacy Surveys (`LS`_) `Release`_
BRICKID                           int32                            Brick ID from tractor input
BRICKNAME                         char[8]                          Brick name from tractor input
BRICK_OBJID                       int32                            OBJID (unique to brick, but not to file)
MORPHTYPE                         char[4]                          `Morphological Model`_ type
RA                                float64    deg                   Right ascension [degrees]
RA_IVAR                           float32    deg**-2               Right ascension inverse variance [1/degrees**2]
DEC                               float64    deg                   Declination [degrees]
DEC_IVAR                          float32    deg**-2               Declination inverse variance [1/degrees**2]
DCHISQ                            float32[5]                       Difference in chi-squared between model fits
EBV                               float32    mag                   Galactic extinction E(B-V) reddening from `SFD98`_
FLUX_G                            float32    nanomaggy             `LS`_ flux from tractor input (g)
FLUX_R                            float32    nanomaggy             `LS`_ flux from tractor input (r)
FLUX_Z                            float32    nanomaggy             `LS`_ flux from tractor input (z)
FLUX_IVAR_G                       float32    nanomaggy**-2         Inverse Variance of FLUX_G
FLUX_IVAR_R                       float32    nanomaggy**-2         Inverse Variance of FLUX_R
FLUX_IVAR_Z                       float32    nanomaggy**-2         Inverse Variance of FLUX_Z
MW_TRANSMISSION_G                 float32                          Milky Way dust transmission in `LS`_ g
MW_TRANSMISSION_R                 float32                          Milky Way dust transmission in `LS`_ r
MW_TRANSMISSION_Z                 float32                          Milky Way dust transmission in `LS`_ z
FRACFLUX_G                        float32                          Fraction of flux from other sources compared to this source in `LS`_ g
FRACFLUX_R                        float32                          Fraction of flux from other sources compared to this source in `LS`_ r
FRACFLUX_Z                        float32                          Fraction of flux from other sources compared to this source in `LS`_ z
FRACMASKED_G                      float32                          Fraction of pixels masked for this source in `LS`_ g
FRACMASKED_R                      float32                          Fraction of pixels masked for this source in `LS`_ r
FRACMASKED_Z                      float32                          Fraction of pixels masked for this source in `LS`_ z
FRACIN_G                          float32                          Fraction of a source's flux within a `LS`_ blob in g
FRACIN_R                          float32                          Fraction of a source's flux within a `LS`_ blob in r
FRACIN_Z                          float32                          Fraction of a source's flux within a `LS`_ blob in z
NOBS_G                            int16                            Number of images for central pixel in `LS`_ g
NOBS_R                            int16                            Number of images for central pixel in `LS`_ r
NOBS_Z                            int16                            Number of images for central pixel in `LS`_ z
PSFDEPTH_G                        float32    nanomaggy**-2         PSF-based depth in `LS`_ g
PSFDEPTH_R                        float32    nanomaggy**-2         PSF-based depth in `LS`_ r
PSFDEPTH_Z                        float32    nanomaggy**-2         PSF-based depth in `LS`_ z
GALDEPTH_G                        float32    nanomaggy**-2         Galaxy model-based depth in `LS`_ g
GALDEPTH_R                        float32    nanomaggy**-2         Galaxy model-based depth in `LS`_ r
GALDEPTH_Z                        float32    nanomaggy**-2         Galaxy model-based depth in `LS`_ z
FLUX_W1                           float32    nanomaggy             WISE flux in W1 (AB system)
FLUX_W2                           float32    nanomaggy             WISE flux in W2 (AB)
FLUX_W3                           float32    nanomaggy             WISE flux in W3 (AB)
FLUX_W4                           float32    nanomaggy             WISE flux in W4 (AB)
FLUX_IVAR_W1                      float32    nanomaggy**-2         Inverse Variance of FLUX_W1 (AB system)
FLUX_IVAR_W2                      float32    nanomaggy**-2         Inverse Variance of FLUX_W2 (AB)
FLUX_IVAR_W3                      float32    nanomaggy**-2         Inverse Variance of FLUX_W3 (AB)
FLUX_IVAR_W4                      float32    nanomaggy**-2         Inverse Variance of FLUX_W4 (AB)
MW_TRANSMISSION_W1                float32                          Milky Way dust transmission in WISE W1
MW_TRANSMISSION_W2                float32                          Milky Way dust transmission in WISE W2
MW_TRANSMISSION_W3                float32                          Milky Way dust transmission in WISE W3
MW_TRANSMISSION_W4                float32                          Milky Way dust transmission in WISE W4
ALLMASK_G                         int16                            Bitwise mask for central pixel in `LS`_ g
ALLMASK_R                         int16                            Bitwise mask for central pixel in `LS`_ r
ALLMASK_Z                         int16                            Bitwise mask for central pixel in `LS`_ z
FIBERFLUX_G                       float32    nanomaggy             g-band object model flux for 1 arcsec seeing and 1.5 arcsec diameter fiber
FIBERFLUX_R                       float32    nanomaggy             r-band object model flux for 1 arcsec seeing and 1.5 arcsec diameter fiber
FIBERFLUX_Z                       float32    nanomaggy             z-band object model flux for 1 arcsec seeing and 1.5 arcsec diameter fiber
FIBERTOTFLUX_G                    float32    nanomaggy             like FIBERFLUX_G but including all objects overlapping this location
FIBERTOTFLUX_R                    float32    nanomaggy             like FIBERFLUX_R but including all objects overlapping this location
FIBERTOTFLUX_Z                    float32    nanomaggy             like FIBERFLUX_Z but including all objects overlapping this location
REF_EPOCH                         float32    yr                    reference epoch for Gaia/Tycho astrometry. Typically 2015.5 for Gaia.
WISEMASK_W1                       byte                             W1 bitmask as cataloged on the `LS DR8 bitmasks page`_
WISEMASK_W2                       byte                             W2 bitmask as cataloged on the `LS DR8 bitmasks page`_
MASKBITS                          int16                            bitmask for ``coadd/*/*/*maskbits*`` maps, as on the `LS DR8 bitmasks page`_
FRACDEV                           float32                          Fraction of model in deVaucouleurs profile
FRACDEV_IVAR                      float32                          Inverse variance of FRACDEV
SHAPEDEV_R                        float32    arcsec                Half-light radius of deVaucouleurs model
SHAPEDEV_E1                       float32                          `Ellipticity component`_ 1 of deVaucouleurs model
SHAPEDEV_E2                       float32                          `Ellipticity component`_ 2 of deVaucouleurs model
SHAPEDEV_R_IVAR                   float32    arcsec**-2            Inverse variance of SHAPEDEV_R
SHAPEDEV_E1_IVAR                  float32                          Inverse variance of SHAPEDEV_E1
SHAPEDEV_E2_IVAR                  float32                          Inverse variance of SHAPEDEV_E2
SHAPEEXP_R                        float32    arcsec                Half-light radius of exponential model
SHAPEEXP_E1                       float32                          `Ellipticity component`_ 1 of exponential model
SHAPEEXP_E2                       float32                          `Ellipticity component`_ 2 of exponential model
SHAPEEXP_R_IVAR                   float32    arcsec**-2            Inverse variance of SHAPEEXP_R
SHAPEEXP_E1_IVAR                  float32                          Inverse variance of SHAPEEXP_E1
SHAPEEXP_E2_IVAR                  float32                          Inverse variance of SHAPEEXP_E2
REF_ID                            int64                            Tyc1*1,000,000+Tyc2*10+Tyc3 for `Tycho-2`_; "sourceid" for `Gaia`_ DR2
REF_CAT                           char[2]                          Reference catalog source for star: "T2" for `Tycho-2`_, "G2" for `Gaia`_ DR2, "L2" for the `SGA`_, empty otherwise
GAIA_PHOT_G_MEAN_MAG              float32    mag                   `Gaia`_ G band magnitude
GAIA_PHOT_G_MEAN_FLUX_OVER_ERROR  float32                          `Gaia`_ G band signal-to-noise
GAIA_PHOT_BP_MEAN_MAG             float32    mag                   `Gaia`_ BP band magnitude
GAIA_PHOT_BP_MEAN_FLUX_OVER_ERROR float32                          `Gaia`_ BP band signal-to-noise
GAIA_PHOT_RP_MEAN_MAG             float32    mag                   `Gaia`_ RP band magnitude
GAIA_PHOT_RP_MEAN_FLUX_OVER_ERROR float32                          `Gaia`_ RP band signal-to-noise
GAIA_PHOT_BP_RP_EXCESS_FACTOR     float32                          `Gaia`_ BP/RP excess factor
GAIA_ASTROMETRIC_EXCESS_NOISE     float32                          `Gaia`_ astrometric excess noise
GAIA_DUPLICATED_SOURCE            bool                             `Gaia`_ duplicated source flag
GAIA_ASTROMETRIC_SIGMA5D_MAX      float32    mas                   `Gaia`_ longest semi-major axis of the 5-d error ellipsoid
GAIA_ASTROMETRIC_PARAMS_SOLVED    int64                            which astrometric parameters were estimated for a `Gaia`_ source
PARALLAX                          float32    mas                   Reference catalog parallax
PARALLAX_IVAR                     float32    mas**-2               Inverse variance of parallax
PMRA                              float32    mas/yr                Reference catalog proper motion in the RA direction
PMRA_IVAR                         float32    mas/yr**-2            Inverse variance of PMRA
PMDEC                             float32    mas/yr                Reference catalog proper motion in the Dec direction
PMDEC_IVAR                        float32    mas/yr**-2            Inverse variance of PMDEC
PHOTSYS                           char[1]                          'N' for the MzLS/BASS photometric system, 'S' for DECaLS
TARGETID                          int64                            Unique targeting ID
DESI_TARGET                       int64                            DESI (dark time program) target selection bitmask
BGS_TARGET                        int64                            BGS (bright time program) target selection bitmask
MWS_TARGET                        int64                            MWS (bright time program) target selection bitmask
SUBPRIORITY                       float64                          Random subpriority [0-1] to break assignment ties
OBSCONDITIONS                     int64                            Flag target to be observed in combinations of dark/gray/bright observing layer
PRIORITY_INIT                     int64                            Initial priority for target calculated across target selection bitmasks and OBSCONDITIONS
NUMOBS_INIT                       int64                            Initial number of observations for target calculated across target selection bitmasks and OBSCONDITIONS
HPXPIXEL                          int64                            HEALPixel containing target at HPXNSIDE
================================= ========== ===================== ===================

.. _`LS`: https://www.legacysurvey.org/dr8/catalogs/
.. _`ellipticity component`: https://www.legacysurvey.org/dr8/catalogs/
.. _`Release`: https://www.legacysurvey.org/release/
.. _`Morphological Model`: https://www.legacysurvey.org/dr8/catalogs/
.. _`Tycho-2`: https://heasarc.nasa.gov/W3Browse/all/tycho2.html
.. _`Gaia`: https://gea.esac.esa.int/archive/documentation//GDR2/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html
.. _`SFD98`: http://ui.adsabs.harvard.edu/abs/1998ApJ...500..525S
.. _`LS DR8 bitmasks page`: https://www.legacysurvey.org/dr8/bitmasks/
.. _`SGA`: https://github.com/moustakas/SGA

Notes
=====

In general, the above format contains:

* Columns that were used by target selection (e.g. FLUX_G/R/Z).
* Columns needed by fiber assignment (e.g. RA, DEC).
* Columns needed for traceability (e.g. BRICKNAME, TARGETID, DESI_TARGET, BGS_TARGET, MWS_TARGET).

FRACFLUX and FRACMASKED are profile-weighted quantities.

SUBPRIORITY, OBSCONDITIONS, PRIORITY_INIT, NUMOBS_INIT, PHOTSYS, TARGETID,
DESI_TARGET, BGS_TARGET, MWS_TARGET and HPXPIXEL are created by target selection;
the rest are passed through from the original `LS`_ tractor or sweep files.

See https://www.legacysurvey.org for more details about columns in the data model.
