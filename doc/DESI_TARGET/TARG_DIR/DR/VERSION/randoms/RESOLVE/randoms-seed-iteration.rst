=======
randoms
=======

:Summary: DESI inside-the-footprint random catalogs contain a single binary table
    covering the entire Legacy Surveys footprint. They contain meta information
    (the number of observations, the depth, etc.) derived from pixels in Legacy
    Surveys CCDs at random RA/Dec coordinates.
:Naming Convention: ``randoms-seed-iteration.fits``, where ``seed`` represents
    the random seed used to generate the catalog and ``iteration`` lists the iteration
    number of the catalog (several iterations are typically conducted
    during a given run to generate random catalogs).
:Regex: ``randoms(-[0-9]+)?-[0-9]+\.fits``
:File Type: FITS, 14 GB

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    Empty
HDU1_  RANDOMS BINTABLE Random catalog table
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = RANDOMS

Random catalog table

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    =========== ================= ===== =============================================================================================
    KEY         Example Value     Type  Comment
    =========== ================= ===== =============================================================================================
    NAXIS1      281               int   Width of table in bytes
    NAXIS2      1124357626        int   Number of rows in table
    FILENSID    2                 int   HEALPix nside covered by file
    FILENEST    T                 bool  HEALPix nested (not ring) ordering
    FILEHPX     11,5,4            str   HEALPix pixel(s) covered by file
    DR          9                 int   `Legacy Surveys`_ (LS) Data Release used to generate randoms
    DENSITY     45000             int   Number of random points generated per sq. deg.
    APRAD       0.75              float Aperture radius used to calculate flux-related quantities (arcsec)
    SEED        1                 int   Seed used to generate random catalog
    ADDMTL      F                 bool  ``True`` if MTL-related columns were added to the parent catalog used to build this catalog
    HPXNSIDE    64                int   HEALPix nside
    HPXNEST     T                 bool  HEALPix nested (not ring) ordering
    SUPP        F                 bool  ``True`` if randoms were generated without using `LS`_ pixels
    RESOLVE     T                 bool  ``True`` if from unique imaging
    RESEED      626               int   Seed used to re-shuffle combined random catalogs to ensure randomness
    MTLSPLIT    T                 bool  ``True`` if MTL-related columns were added to this random catalog
    REGION [1]_ north             str   "noresolve" randoms may have this keyword set.  Values are 'north' or 'south'.
    INFILE [1]_ randoms-1-15.fits str   HEALPixel-split randoms may have this keyword set. Value is the original source randoms file.
    =========== ================= ===== =============================================================================================

.. [1] Optional

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

============= ======== ============== ===================
Name          Type     Units          Description
============= ======== ============== ===================
RELEASE       int16                   Integer denoting the camera and filter set used
BRICKID       int32                   A unique Brick ID
BRICKNAME     char[8]                 Name of the brick
BRICK_OBJID   int32                   Random catalog object number enumerated by increasing RA within each brick; a unique identifier hash is RELEASE,BRICKID,BRICK_OBJID
RA            float64  deg            Right ascension at pixel location
DEC           float64  deg            Declination at pixel location
NOBS_G        int16                   Number of images at pixel location in `LS`_ g
NOBS_R        int16                   Number of images at pixel location in `LS`_ r
NOBS_Z        int16                   Number of images at pixel location in `LS`_ z
PSFDEPTH_G    float32                 PSF-based depth at pixel location in `LS`_ g
PSFDEPTH_R    float32                 PSF-based depth at pixel location in `LS`_ r
PSFDEPTH_Z    float32                 PSF-based depth at pixel location in `LS`_ z
GALDEPTH_G    float32                 Galaxy model-based depth at pixel location in `LS`_ g
GALDEPTH_R    float32                 Galaxy model-based depth at pixel location in `LS`_ r
GALDEPTH_Z    float32                 Galaxy model-based depth at pixel location in `LS`_ z
PSFDEPTH_W1   float32                 PSF-based depth in WISE W1 (AB mag system)
PSFDEPTH_W2   float32                 PSF-based depth in WISE W2 (AB mag system)
PSFSIZE_G     float32  arcsec         Weighted average PSF FWHM in `LS`_ g
PSFSIZE_R     float32  arcsec         Weighted average PSF FWHM in `LS`_ r
PSFSIZE_Z     float32  arcsec         Weighted average PSF FWHM in `LS`_ z
APFLUX_G      float32  nanomaggy      Total flux extracted in a 0.75 arcsec radius in g
APFLUX_R      float32  nanomaggy      Total flux extracted in a 0.75 arcsec radius in r
APFLUX_Z      float32  nanomaggy      Total flux extracted in a 0.75 arcsec radius in z
APFLUX_IVAR_G float32  nanomaggy^-2   Inverse variance of APFLUX_G
APFLUX_IVAR_R float32  nanomaggy^-2   Inverse variance of APFLUX_R
APFLUX_IVAR_Z float32  nanomaggy^-2   Inverse variance of APFLUX_Z
MASKBITS      int16                   Bit mask of possible problems with pixel (see the LS `DR9 bitmasks page`_)
WISEMASK_W1   binary                  Bitwise mask for WISE W1 data (see the LS `DR9 bitmasks page`_)
WISEMASK_W2   binary                  Bitwise mask for WISE W2 data (see the LS `DR9 bitmasks page`_)
EBV           float32                 Galactic extinction E(B-V) reddening at pixel from `SFD98`_
PHOTSYS       char[1]                 'N' for an MzLS/BASS location, 'S' for a DECaLS location
HPXPIXEL      int64                   HEALPixel containing this location at NSIDE=64 in the NESTED scheme
TARGETID      int64                   See the `desitarget data model`_ (added to facilitate running randoms through the `DESI fiberassign code`_)
DESI_TARGET   int64                   See the `desitarget data model`_; set to 4, appropriate to a QSO, the highest-priority DESI dark-time target (added to facilitate running randoms through the `DESI fiberassign code`_)
BGS_TARGET    int64                   See the `desitarget data model`_; set to 0 (added to facilitate running randoms through the `DESI fiberassign code`_)
MWS_TARGET    int64                   See the `desitarget data model`_; set to 0 (added to facilitate running randoms through the `DESI fiberassign code`_)
SUBPRIORITY   float64                 See the `desitarget data model`_ (added to facilitate running randoms through the `DESI fiberassign code`_)
OBSCONDITIONS int32                   See the `desitarget data model`_; set to 511, which corresponds to all possible observing conditions (added to facilitate running randoms through the `DESI fiberassign code`_)
PRIORITY_INIT int64                   See the `desitarget data model`_; set to 3400, appropriate to a QSO, the highest-priority DESI dark-time target (added to facilitate running randoms through the `DESI fiberassign code`_)
NUMOBS_INIT   int64                   See the `desitarget data model`_; set to 4, appropriate to a QSO, the highest-priority DESI dark-time target (added to facilitate running randoms through the `DESI fiberassign code`_)
SCND_TARGET   int64                   See the `desitarget data model`_; set to 0 (added to facilitate running randoms through the `DESI fiberassign code`_)
NUMOBS_MORE   int64                   See the `desitarget data model`_; set to 4, appropriate to a QSO, the highest-priority DESI dark-time target (added to facilitate running randoms through the `DESI fiberassign code`_)
NUMOBS        int64                   See the `desitarget data model`_; set to 0 (added to facilitate running randoms through the `DESI fiberassign code`_)
Z             float64                 See the `desitarget data model`_; set to -1.0 (added to facilitate running randoms through the `DESI fiberassign code`_)
ZWARN         int64                   See the `desitarget data model`_; set to -1 (added to facilitate running randoms through the `DESI fiberassign code`_)
TARGET_STATE  char[15]                See the `desitarget data model`_; set to "QSO|UNOBS", denoting an unobserved QSO (added to facilitate running randoms through the `DESI fiberassign code`_)
TIMESTAMP     char[19]                See the `desitarget data model`_; time at which this random was processed (added to facilitate running randoms through the `DESI fiberassign code`_)
VERSION       char[14]                See the `desitarget data model`_; version of the desitarget code used to process this random (added to facilitate running randoms through the `DESI fiberassign code`_)
PRIORITY      int64                   See the `desitarget data model`_; set to 3400, appropriate to a QSO, the highest-priority DESI dark-time target (added to facilitate running randoms through the `DESI fiberassign code`_)
============= ======== ============== ===================


Notes and Examples
==================

See http://legacysurvey.org for more details about the corresponding columns for sources extracted by
the Tractor in the Legacy Surveys, e.g. the units of the depth quantities.

.. _`SFD98`: http://adsabs.harvard.edu/abs/1998ApJ...500..525S
.. _`Legacy Surveys`: http://legacysurvey.org
.. _`LS`: http://legacysurvey.org/dr9/catalogs/
.. _`DR9 bitmasks page`: https://www.legacysurvey.org/dr9/bitmasks/
.. _`desitarget data model`: https://desidatamodel.readthedocs.io/en/latest/DESI_TARGET/index.html
.. _`DESI fiberassign code`: https://github.com/desihub/fiberassign
