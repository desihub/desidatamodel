=======
spPlate
=======

.. Add support for breadcrumb links

.. This is a comment!

General Description
===================

Summary
-------

Combined spectra for one plate.

The spPlate files contain the combined spectra for all exposures of
a given plate.  There are typically four 900s exposures which may
have been taken in a single night, or over multiple nights.  This page
is an updated summary of the `SDSS2 spPlate data model`_ .

.. _`SDSS2 spPlate data model`: http://spectro.astro.princeton.edu/#dm_spplate

Naming Convention
-----------------

``spPlate-PLATE4-MJD5.fits``, where ``PLATE4`` is the zero-padded, four-digit
plate number and ``MJD5`` is the five-digit MJD.


Contents
========

====== ======== ============================== ================================================================
Number EXTNAME  Type                           Contents
====== ======== ============================== ================================================================
HDU0_           NPIX x NFIBER float image      Flux in units of |flux|.
HDU1_  IVAR     NPIX x NFIBER float image      Inverse variance (\ :math:`1/\sigma^2`) for HDU 0
HDU2_  ANDMASK  NPIX x NFIBER 32-bit int image AND mask
HDU3_  ORMASK   NPIX x NFIBER 32-bit int image OR mask
HDU4_  WAVEDISP NPIX x NFIBER float image      Wavelength dispersion in pixels
HDU5_  PLUGMAP  binary table                   Plug-map structure from plPlugMapM file
HDU6_  SKY      NPIX x NFIBER float image      Average sky flux in units of |flux|.
====== ======== ============================== ================================================================

.. |flux| replace:: 10\ :sup:`-17` erg/s/cm\ :sup:`2`\ /Å


FITS Header Units
=================

HDU0
----

FITS Image: Spectra

HDU1
----

FITS Image: Inverse variance

HDU2
----

FITS Image: AND mask

HDU3
----

FITS Image: OR mask

HDU4
----

FITS Image: Wavelength dispersion

HDU5
----

FITS Binary Table: Plugmap information

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========= ==== ========================================
Header   Value     Type Comment
======== ========= ==== ========================================
XTENSION BINTABLE  str  Binary table written by MWRFITS v1.8
BITPIX   8         int  Required value
NAXIS    2         int  Required value
NAXIS1   250       int  Number of bytes per row
NAXIS2   NFIBER    int  Number of rows
PCOUNT   0         int  Normally 0 (no varying arrays)
GCOUNT   1         int  Required value
TFIELDS  34        int  Number of columns in table
======== ========= ==== ========================================

Required Columns
~~~~~~~~~~~~~~~~

================= ======== =======
Column            Type     Comment
================= ======== =======
OBJID             int32[5]
HOLETYPE          char[6]
RA                double
DEC               double
MAG               float[5]
STARL             float
EXPL              float
DEVAUCL           float
OBJTYPE           char[16]
XFOCAL            double
YFOCAL            double
SPECTROGRAPHID    int32
FIBERID           int32
THROUGHPUT        int32
PRIMTARGET        int32
SECTARGET         int32
OFFSETID          int32
SCI_EXPTIME       float
SOURCETYPE        char[7]
LAMBDA_EFF        float
ZOFFSET           float
BLUEFIBER         int32
BOSS_TARGET1      int64
BOSS_TARGET2      int64
ANCILLARY_TARGET1 int64
ANCILLARY_TARGET2 int64
RUN               int32
RERUN             char[5]
CAMCOL            int32
FIELD             int32
ID                int32
CALIBFLUX         float[5]
CALIBFLUX_IVAR    float[5]
SFD_EBV           float
================= ======== =======


HDU6
----

FITS Image: Average sky flux

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ====== ==== ========================================
Header   Value  Type Comment
======== ====== ==== ========================================
XTENSION IMAGE  str  Image Extension created by MWRFITS v1.4a
BITPIX   -32    int  Data is 32-bit float
NAXIS    2      int  Number of data axes
NAXIS1   NPIX   int  Width
NAXIS2   NFIBER int  Height
======== ====== ==== ========================================

Notes and Examples
==================

Additional HDUs may be present for engineering purposes,
but are not supported and are subject to change.
Users should refrain from using HDUs not listed here.

There are two masks, an "AND" mask and an "OR" mask.
The spectra are constructed from 3 or more 15-minute observations,
and the "AND" mask bits are set if that bit is set for each and
every input observation. The "OR" mask bits are set if that bit
is set for any of the observations.
Usually, only "AND" mask is of interest.

The mask bits are set as follows.
The authoritative definition of mask bits is in
`idlutils/data/sdss/sdssMaskbits.par`_, with an alternate parsing at the
`data release documentation`_.  They are included here for convenience:

.. _`idlutils/data/sdss/sdssMaskbits.par`: http://www.sdss3.org/svn/repo/idlutils/trunk/data/sdss/sdssMaskbits.par
.. _`data release documentation`: http://www.sdss3.org/dr10/algorithms/bitmasks.php

=== ============== =========================================================================================
Bit Name           Description
=== ============== =========================================================================================
  0 NOPLUG         Fiber not listed in plugmap file
  1 BADTRACE       Bad trace from routine TRACE320CRUDE
  2 BADFLAT        Low counts in fiberflat
  3 BADARC         Bad arc solution
  4 MANYBADCOLUMNS >10% pixels are bad columns
  5 MANYREJECTED   >10% pixels are rejected in extraction
  6 LARGESHIFT     Large spatial shift between flat and object pos'n
  7 BADSKYFIBER    Sky Fiber shows extreme residuals
  8 NEARWHOPPER    Within 2 fibers of a whopping fiber (deprecated)
 10 SMEARIMAGE     Smear available for red and blue cameras (deprecated)
 11 SMEARHIGHSN    S/N sufficient for full smear fit (deprecated)
 12 SMEARMEDSN     S/N only sufficient for scaled median fit (deprecated)
 16 NEARBADPIXEL   Bad pixel within 3 pixels of trace
 17 LOWFLAT        Flat field less than 0.5
 18 FULLREJECT     Pixel fully rejected in extraction (INVVAR=0)
 19 PARTIALREJECT  Some pixels rejected in extraction
 20 SCATTEREDLIGHT Scattered light significant
 21 CROSSTALK      Cross-talk significant
 22 NOSKY          Sky level unknown at this wavelength (INVVAR=0)
 23 BRIGHTSKY      Sky level > flux + 10*(flux error) AND sky > 2.0 * median(sky,99 pixels)
 24 NODATA         No data available in combine B-spline (deprecated; INVVAR=0)
 25 COMBINEREJ     Rejected in combine B-spline
 26 BADFLUXFACTOR  Low flux-calibration or flux-correction factor
 27 BADSKYCHI      Relative |chi2| > 3 in sky residuals at this wavelength
 28 REDMONSTER     Contiguous region of bad |chi2| in sky residuals (with threshhold of relative |chi2| > 3)
=== ============== =========================================================================================

.. |chi2| replace:: :math:`\chi^2`

When low numbered bits (<16) are set,
those will be set for half of the spectra:
either the blue or red spectrograph.
The higher-numbered bits (>=16) are set for individual pixels.

Which mask bits are important?
The conditions that are considered very bad are already
used to set the errors to infinity for the effected pixels
(specifically, the inverse variance is set to zero).
The most useful mask bit to look at is BRIGHTSKY,
which indicates when the sky is so bright relative to the
object that perhaps one shouldn't trust any of the object flux there.
Our reported errors are meant to include sky-subtraction errors,
but there are instances (particularly around 5577) where these
errors may be untrustworthy.

Dispersion and sky: The dispersion per pixel and the sky flux
are computed at each pixel by re-weighting the individual spectra
at each pixel according to their formal errors.
This re-weighting is only approximate.

Sky wavelengths: Note that the sky lines are slightly shifted
in the reductions because we transform the velocities to the
barycenter of the solar system.
Each exposure that contributes to the co-added spectra will have
slightly different barycenter correction, so the "average sky"
contains a superposition of these slightly-offset sky lines.
These shifts keep the object spectra as-measured at the barycenter,
regardless of the time of year or the Earth's rotation relative
to the spectroscopic targets.

Doodles
=======

See sdR_

.. _sdR: ./sdR.rst


Superscript\ :sup:`superscript`

Subscript\ :sub:`subscript`

Generate html with::

    rst2html.py -gdts datamodel_test.rst datamodel_test.html

With docutils installed by MacPorts_, I have to do::

    rst2html-2.7.py -gdts datamodel_test.rst datamodel_test.html

.. _MacPorts: http://www.macports.org
