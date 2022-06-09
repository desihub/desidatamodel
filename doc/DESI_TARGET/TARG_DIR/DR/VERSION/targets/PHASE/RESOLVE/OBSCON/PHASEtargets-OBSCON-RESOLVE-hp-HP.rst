=======
targets
=======

:Summary: DESI target selection files include a binary table containing
    the targets in a (nested) HEALPixel. They store the variables used by
    target selection (*e.g.* fluxes), variables needed by fiber assignment (*e.g.*
    RA, DEC), and variables needed for traceability (*e.g.* DESITARGET, TARGETID).
:Naming Convention: ``PHASEtargets-OBSCON-hp-HP.fits``,
    where ``PHASE`` is a specific DESI observational phase (*e.g.* svX with X=1,2,3
    for iterations of Survey Validation) ``OBSCON`` is the observing condition
    (or "layer") for the targets (*e.g.* dark), and ``HP`` is the HEALPixel covered
    at the (nested) HEALPixel nside included in the file header as ``FILENSID``
    (*e.g.* 11). For targets that are part of the DESI Main Science Survey
    ``PHASE`` is omitted from the filename.
:Regex: ``.*?targets-.*?-hp-?[0-9]+\.fits``
:File Type: FITS, 2 GB

**Note**: this documents the target catalog format starting with DR9 /
desitarget 0.47.0 .  The previous format is documented in :doc:`targets-dr8`.

Examples
========

DESI target selection files, based on DR9 of the Legacy Surveys, are available at:

https://data.desi.lbl.gov/public/ets/target/catalogs/dr9 .

Contents
========

====== ======= ======== ============
Number EXTNAME Type     Contents
====== ======= ======== ============
HDU0_  PRIMARY IMAGE    Empty
HDU1_  TARGETS BINTABLE Target table
HDU2_  INFILES BINTABLE Files used to produce target table
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
OBSCON   "DARK"        str  observing layer for file
HPXNSIDE 64            int  HEALPix nside for column `HPXPIXEL`
HPXNEST  T             bool HEALPix nested (not ring) ordering
SUBPSEED 1154          int  random seed used to generate `SUBPRIORITY` values
SURVEY   "main"        str  svX for SV, main for Main Survey
RESOLVE  T             bool ``True`` if from unique imaging
MASKBITS T             bool ``True`` if masking cuts applied
BACKUP   F             bool ``True`` for backup/supplemental targets
DR       9             int  Legacy Surveys Data Release used to find targets
TCNAMES  "QSO,LRG"     str  run for this target-class subset
GAIASUB  T             bool ``True`` if Gaia EDR3 astrometric values were substituted for Gaia DR2 quantities.
CMDLINE  "/global/"    str  command-line call used to generate target file
SCNDOUT  "/global/"    str  directory from which secondary targets were read
FILENSID 2             int  HEALPix nside covered by file
FILENEST T             bool HEALPix nested (not ring) ordering
FILEHPX  11            int  HEALPix pixel(s) covered by file
======== ============= ==== ==================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

================================= =========== ===================== ===================
Name                              Type        Units                 Description
================================= =========== ===================== ===================
RELEASE                           int16                             Legacy Surveys (`LS`_) `Release`_
BRICKID                           int32                             Brick ID from tractor input
BRICKNAME                         char[8]                           Brick name from tractor input
BRICK_OBJID                       int32                             OBJID (unique to brick, but not to file)
MORPHTYPE                         char[4]                           `Morphological Model`_ type
RA                                float64     deg                   Right ascension
RA_IVAR                           float32     1/deg^2               Right ascension inverse variance
DEC                               float64     deg                   Declination
DEC_IVAR                          float32     1/deg^2               Declination inverse variance
DCHISQ                            float32[5]                        Difference in chi-squared between model fits
EBV                               float32     mag                   Galactic extinction E(B-V) reddening from `SFD98`_
FLUX_G                            float32     nanomaggies           `LS`_ flux from tractor input (g)
FLUX_R                            float32     nanomaggies           `LS`_ flux from tractor input (r)
FLUX_Z                            float32     nanomaggies           `LS`_ flux from tractor input (z)
FLUX_IVAR_G                       float32     1/nanomaggy^2         Inverse Variance of FLUX_G
FLUX_IVAR_R                       float32     1/nanomaggy^2         Inverse Variance of FLUX_R
FLUX_IVAR_Z                       float32     1/nanomaggy^2         Inverse Variance of FLUX_Z
MW_TRANSMISSION_G                 float32                           Milky Way dust transmission in `LS`_ g
MW_TRANSMISSION_R                 float32                           Milky Way dust transmission in `LS`_ r
MW_TRANSMISSION_Z                 float32                           Milky Way dust transmission in `LS`_ z
FRACFLUX_G                        float32                           Fraction of flux from other sources compared to this source in `LS`_ g
FRACFLUX_R                        float32                           Fraction of flux from other sources compared to this source in `LS`_ r
FRACFLUX_Z                        float32                           Fraction of flux from other sources compared to this source in `LS`_ z
FRACMASKED_G                      float32                           Fraction of pixels masked for this source in `LS`_ g
FRACMASKED_R                      float32                           Fraction of pixels masked for this source in `LS`_ r
FRACMASKED_Z                      float32                           Fraction of pixels masked for this source in `LS`_ z
FRACIN_G                          float32                           Fraction of a source's flux within a `LS`_ blob in g
FRACIN_R                          float32                           Fraction of a source's flux within a `LS`_ blob in r
FRACIN_Z                          float32                           Fraction of a source's flux within a `LS`_ blob in z
NOBS_G                            int16                             Number of images for central pixel in `LS`_ g
NOBS_R                            int16                             Number of images for central pixel in `LS`_ r
NOBS_Z                            int16                             Number of images for central pixel in `LS`_ z
PSFDEPTH_G                        float32     1/nanomaggy^2         PSF-based depth in `LS`_ g
PSFDEPTH_R                        float32     1/nanomaggy^2         PSF-based depth in `LS`_ r
PSFDEPTH_Z                        float32     1/nanomaggy^2         PSF-based depth in `LS`_ z
GALDEPTH_G                        float32     1/nanomaggy^2         Galaxy model-based depth in `LS`_ g
GALDEPTH_R                        float32     1/nanomaggy^2         Galaxy model-based depth in `LS`_ r
GALDEPTH_Z                        float32     1/nanomaggy^2         Galaxy model-based depth in `LS`_ z
FLUX_W1                           float32     nanomaggies           WISE flux in W1 (AB system)
FLUX_W2                           float32     nanomaggies           WISE flux in W2 (AB)
FLUX_W3                           float32     nanomaggies           WISE flux in W3 (AB)
FLUX_W4                           float32     nanomaggies           WISE flux in W4 (AB)
FLUX_IVAR_W1                      float32     1/nanomaggy^2         Inverse Variance of FLUX_W1 (AB system)
FLUX_IVAR_W2                      float32     1/nanomaggy^2         Inverse Variance of FLUX_W2 (AB)
FLUX_IVAR_W3                      float32     1/nanomaggy^2         Inverse Variance of FLUX_W3 (AB)
FLUX_IVAR_W4                      float32     1/nanomaggy^2         Inverse Variance of FLUX_W4 (AB)
MW_TRANSMISSION_W1                float32                           Milky Way dust transmission in WISE W1
MW_TRANSMISSION_W2                float32                           Milky Way dust transmission in WISE W2
MW_TRANSMISSION_W3                float32                           Milky Way dust transmission in WISE W3
MW_TRANSMISSION_W4                float32                           Milky Way dust transmission in WISE W4
ALLMASK_G                         int16                             Bitwise mask for central pixel in `LS`_ g
ALLMASK_R                         int16                             Bitwise mask for central pixel in `LS`_ r
ALLMASK_Z                         int16                             Bitwise mask for central pixel in `LS`_ z
FIBERFLUX_G                       float32     nanomaggies           g-band object model flux for 1 arcsec seeing and 1.5 arcsec diameter fiber
FIBERFLUX_R                       float32     nanomaggies           r-band object model flux for 1 arcsec seeing and 1.5 arcsec diameter fiber
FIBERFLUX_Z                       float32     nanomaggies           z-band object model flux for 1 arcsec seeing and 1.5 arcsec diameter fiber
FIBERTOTFLUX_G                    float32     nanomaggies           like FIBERFLUX_G but including all objects overlapping this location
FIBERTOTFLUX_R                    float32     nanomaggies           like FIBERFLUX_R but including all objects overlapping this location
FIBERTOTFLUX_Z                    float32     nanomaggies           like FIBERFLUX_Z but including all objects overlapping this location
REF_EPOCH                         float32     yr                    reference epoch for Gaia/Tycho astrometry. Typically 2015.5 for Gaia.
WISEMASK_W1                       byte                              W1 bitmask as cataloged on the `LS DR9 bitmasks page`_
WISEMASK_W2                       byte                              W2 bitmask as cataloged on the `LS DR9 bitmasks page`_
MASKBITS                          int16                             bitmask for ``coadd/*/*/*maskbits*`` maps, as on the `LS DR9 bitmasks page`_
LC_FLUX_W1                        float32[15] nanomaggies           FLUX_W1 in each of up to fifteen unWISE coadd epochs (AB system; defaults to zero for unused entries)
LC_FLUX_W2                        float32[15] nanomaggies     	    FLUX_W2 in each of up to fifteen unWISE coadd epochs (AB system; defaults to zero for unused entries)
LC_FLUX_IVAR_W1                   float32[15] 1/nanomaggy^2         Inverse variance of LC_FLUX_W1 (AB system; defaults to zero for unused entries)
LC_FLUX_IVAR_W2	              	  float32[15] 1/nanomaggy^2         Inverse variance of LC_FLUX_W2 (AB system; defaults to zero for unused entries)
LC_NOBS_W1	              	  int16[15]                         NOBS_W1 in each of up to fifteen unWISE coadd epochs
LC_NOBS_W2                        int16[15]                         NOBS_W2 in each of up to fifteen unWISE coadd epochs
LC_MJD_W1                         float64[15]                       MJD_W1 in each of up to fifteen unWISE coadd epochs (defaults to zero for unused entries)
LC_MJD_W2                         float64[15]                       MJD_W2 in each of up to fifteen unWISE coadd epochs (defaults to zero for unused entries)
SHAPE_R                           float32     arcsec                Half-light radius of galaxy model for galaxy type MORPHTYPE (>0)
SHAPE_E1                          float32                           `Ellipticity component`_ 1 of galaxy model for galaxy type MORPHTYPE
SHAPE_E2                          float32                           `Ellipticity component`_ 2 of galaxy model for galaxy type MORPHTYPE
SHAPE_R_IVAR                      float32     1/arcsec^2            Inverse variance of SHAPE_R
SHAPE_E1_IVAR                     float32                           Inverse variance of SHAPE_E1
SHAPE_E2_IVAR                     float32                           Inverse variance of SHAPE_E2
SERSIC                            float32                           Power-law index for the Sersic profile model (MORPHTYPE="SER")
SERSIC_IVAR                       float32                           Inverse variance of SERSIC
REF_ID                            int64                             Tyc1*1,000,000+Tyc2*10+Tyc3 for `Tycho-2`_; "sourceid" for `Gaia`_ DR2
REF_CAT                           char[2]                           Reference catalog source for star: "T2" for `Tycho-2`_, "G2" for `Gaia`_ DR2, "L2" for the `SGA`_, empty otherwise
GAIA_PHOT_G_MEAN_MAG              float32     mag                   `Gaia`_ G band magnitude
GAIA_PHOT_G_MEAN_FLUX_OVER_ERROR  float32                           `Gaia`_ G band signal-to-noise
GAIA_PHOT_BP_MEAN_MAG             float32     mag                   `Gaia`_ BP band magnitude
GAIA_PHOT_BP_MEAN_FLUX_OVER_ERROR float32                           `Gaia`_ BP band signal-to-noise
GAIA_PHOT_RP_MEAN_MAG             float32     mag                   `Gaia`_ RP band magnitude
GAIA_PHOT_RP_MEAN_FLUX_OVER_ERROR float32                           `Gaia`_ RP band signal-to-noise
GAIA_PHOT_BP_RP_EXCESS_FACTOR     float32                           `Gaia`_ BP/RP excess factor
GAIA_ASTROMETRIC_EXCESS_NOISE     float32                           `Gaia`_ astrometric excess noise
GAIA_DUPLICATED_SOURCE            bool                              `Gaia`_ duplicated source flag
GAIA_ASTROMETRIC_SIGMA5D_MAX      float32     mas                   `Gaia`_ longest semi-major axis of the 5-d error ellipsoid
GAIA_ASTROMETRIC_PARAMS_SOLVED    int64                             which astrometric parameters were estimated for a `Gaia`_ source
PARALLAX                          float32     mas                   Reference catalog parallax
PARALLAX_IVAR                     float32     1/mas^2               Inverse variance of parallax
PMRA                              float32     mas / yr              Reference catalog proper motion in the RA direction
PMRA_IVAR                         float32     yr^2 / mas^2          Inverse variance of PMRA
PMDEC                             float32     mas / yr              Reference catalog proper motion in the Dec direction
PMDEC_IVAR                        float32     yr^2 / mas^2          Inverse variance of PMDEC
PHOTSYS                           char[1]                           'N' for the MzLS/BASS photometric system, 'S' for DECaLS
TARGETID                          int64                             Unique targeting ID
DESI_TARGET                       int64                             DESI (dark time program) target selection bitmask
BGS_TARGET                        int64                             BGS (bright time program) target selection bitmask
MWS_TARGET                        int64                             MWS (bright time program) target selection bitmask
SUBPRIORITY                       float64                           Random subpriority [0-1] to break assignment ties
OBSCONDITIONS                     int64                             Flag target to be observed in combinations of dark/bright observing layer
PRIORITY_INIT                     int64                             Initial priority for target calculated across target selection bitmasks and OBSCONDITIONS
NUMOBS_INIT                       int64                             Initial number of observations for target calculated across target selection bitmasks and OBSCONDITIONS
SCND_TARGET                       int64                             SCND (secondary program) target selection bitmask
HPXPIXEL                          int64                             HEALPixel containing target at HPXNSIDE
================================= =========== ===================== ===================

HDU2
----

EXTNAME = INFILES

Files used to produce target table

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============= ==== ==================================
KEY      Example Value Type Comment
======== ============= ==== ==================================
NAXIS1   152           int  width of table in bytes
NAXIS2   6             int  number of rows in table
======== ============= ==== ==================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

============= =========== ============ ===================
Name          Type        Units        Description
============= =========== ============ ===================
FILENAME      char[88]		       `LS`_ sweep files associated with this HEALPixel
SHASUM        char[64]		       Checksum	for each `LS`_ sweep file
============= =========== ============ ===================

.. _`LS`: https://www.legacysurvey.org/dr9/catalogs/
.. _`ellipticity component`: https://www.legacysurvey.org/dr9/catalogs/
.. _`Release`: https://www.legacysurvey.org/release/
.. _`Morphological Model`: https://www.legacysurvey.org/dr9/catalogs/
.. _`Tycho-2`: https://heasarc.nasa.gov/W3Browse/all/tycho2.html
.. _`Gaia`: https://gea.esac.esa.int/archive/documentation//GDR2/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html
.. _`SFD98`: http://ui.adsabs.harvard.edu/abs/1998ApJ...500..525S
.. _`LS DR9 bitmasks page`: https://www.legacysurvey.org/dr9/bitmasks/
.. _`SGA`: https://github.com/moustakas/SGA

Notes
=====

In general, the above format contains:

* Columns that were used by target selection (e.g. FLUX_G/R/Z).
* Columns needed by fiber assignment (e.g. RA, DEC).
* Columns needed for traceability (e.g. BRICKNAME, TARGETID, DESI_TARGET, BGS_TARGET, MWS_TARGET).

FRACFLUX and FRACMASKED are profile-weighted quantities.

SUBPRIORITY, OBSCONDITIONS, PRIORITY_INIT, NUMOBS_INIT, PHOTSYS, TARGETID,
DESI_TARGET, BGS_TARGET, MWS_TARGET, SCND_TARGET and HPXPIXEL are created by target selection;
the rest are passed through from the original `LS`_ tractor or sweep files.

See https://www.legacysurvey.org for more details about columns in the data model.
