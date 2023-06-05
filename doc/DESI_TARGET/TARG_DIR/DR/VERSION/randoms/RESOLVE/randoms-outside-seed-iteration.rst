===============
randoms-outside
===============

:Summary: DESI outside-the-footprint random catalogs contain a single binary
    table covering areas beyond the `Legacy Surveys`_ footprint.
    The columns in this file are simplified compared to the other random
    catalogs as entries in additional columns would be zeros.
:Naming Convention: ``randoms-outside-seed-iteration.fits``, where ``seed`` represents
    the random seed used to generate the catalog and ``iteration`` lists the iteration
    number of the catalog (several iterations are typically conducted
    during a given run to generate random catalogs).
:Regex: ``randoms-outside(-[0-9]+)?-[0-9]+\.fits``
:File Type: FITS, 2 GB

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

    ======== ============= ===== ========================================
    KEY      Example Value Type  Comment
    ======== ============= ===== ========================================
    NAXIS1   281           int   Width of table in bytes
    NAXIS2   1124357626    int   Number of rows in table
    DR       9             int   `Legacy Surveys`_ (LS) Data Release used to generate randoms
    DENSITY  45000         int   Number of random points generated per sq. deg.
    SEED     1             int   Seed used to generate supplemental random catalog
    ORIGSEED 3             int   Original seed used to generate associated `LS`_ random catalog
    SUPP     T             bool  ``True`` if randoms were generated without using `LS`_ pixels
    RESOLVE  T             bool  ``True`` if from unique imaging
    ======== ============= ===== ========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

============= ======== ============= ===================
Name          Type     Units         Description
============= ======== ============= ===================
BRICKID       int32                  A unique Brick ID
BRICKNAME     char[8]                Name of the brick
RA            float64  deg           Right ascension at pixel location
DEC           float64  deg           Declination at pixel location
NOBS_G        int16                  Number of images at pixel location in `LS`_ g (should be zero)
NOBS_R        int16                  Number of images at pixel location in `LS`_ r (should be zero)
NOBS_Z        int16                  Number of images at pixel location in `LS`_ z (should be zero)
EBV           float32                Galactic extinction E(B-V) reddening at pixel from `SFD98`_
============= ======== ============= ===================


.. _`SFD98`: http://adsabs.harvard.edu/abs/1998ApJ...500..525S
.. _`Legacy Surveys`: http://legacysurvey.org
.. _`LS`: http://legacysurvey.org/dr9/catalogs/
.. _`DR9 bitmasks page`: https://www.legacysurvey.org/dr9/bitmasks/
.. _`desitarget data model`: https://desidatamodel.readthedocs.io/en/latest/DESI_TARGET/index.html
.. _`DESI fiberassign code`: https://github.com/desihub/fiberassign
