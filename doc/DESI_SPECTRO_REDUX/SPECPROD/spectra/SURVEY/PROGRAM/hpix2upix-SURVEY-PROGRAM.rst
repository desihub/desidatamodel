=========
hpix2upix
=========

:Summary: This file contains a mapping of large nside healpix to adaptively size uniqpix.
:Naming Convention: ``hpix2upix-SURVEY-PROGRAM.fits``,
    where SURVEY is main, sv1, sv2, sv3, special, or cmx;
    and PROGRAM is bright, dark, backup, or other.
:Regex: ``hpix2upix-(cmx|main|special|sv1|sv2|sv3)-(backup|bright|dark|other).fits``
:File Type: FITS, 9 MB

Contents
========

====== ============= ===== ===================
Number EXTNAME       Type  Contents
====== ============= ===== ===================
HDU0_  HPIX2UPIX     IMAGE Mapping from healpix to uniqpix
HDU1_  HPIX_NTARGETS IMAGE Number of unique targets in each uniqpix
====== ============= ===== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = HPIX2UPIX

Mapping from healpix to uniqpix at the NSIDE given in the header.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ============= ==== =====================
    KEY      Example Value Type Comment
    ======== ============= ==== =====================
    NAXIS1   786432        int  Size of array: Number of healpixels at this NSIDE
    NSIDE    256           int  The nside used for the healpix calculation.
    HPXNSIDE 256           int  Same as NSIDE
    HPXNEST  T             bool Whether the healpix is in nested ordering (T) or ring ordering (F).
    SURVEY   main          str  DESI survey name: main, sv1, sv2, sv3, special, or cmx
    PROGRAM  dark          str  DESI program name: bright, dark, backup, or other
    SPECPROD matterhorn    str  DESI spectro production name, e.g. matterhorn, nevis
    ======== ============= ==== =====================

Data: FITS image [int64, 786432]

This array is indexed by the healpixel number, and the value is the corresponding uniqpix number.
The healpix number is calculated using the NSIDE header keyword, which is the largest NSIDE used
by any uniqpix in this production.  If a healpix is not covered by any uniqpix in this production,
then the value is -1.

HDU1
----

EXTNAME = HPIX_NTARGETS

The number of targets per healpix.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ============= ==== =====================
    KEY      Example Value Type Comment
    ======== ============= ==== =====================
    NAXIS1   786432        int  Size of array: Number of healpixels at this NSIDE
    NSIDE    256           int  The nside used for the healpix calculation.
    HPXNSIDE 256           int  Same as NSIDE
    HPXNEST  T             bool Whether the healpix is in nested ordering (T) or ring ordering (F).
    SURVEY   main          str  DESI survey name: main, sv1, sv2, sv3, special, or cmx
    PROGRAM  dark          str  DESI program name: bright, dark, backup, or other
    SPECPROD matterhorn    str  DESI spectro production name, e.g. matterhorn, nevis
    ======== ============= ==== =====================

Data: FITS image [int32, 786432]

Even if a healpix is covered by a uniqpix, it may not contain any targets.  This array gives the number of targets in each healpix, which can be used to quickly determine if a healpix contains any targets without having to read the corresponding uniqpix.

Notes and Examples
==================

Example usage::

    import healpy
    import fitsio

    with fitsio.FITS('spectra/main/dark/hpix2upix-main-dark.fits') as fx:
        header = fx['HPIX2UPIX'].read_header()
        hpix2upix = fx['HPIX2UPIX'].read()
        hpix_ntargets = fx['HPIX_NTARGETS'].read()

    nsidemax = header['NSIDE']
    hpix = healpy.ang2pix(nsidemax, ra, dec, lonlat=True, nest=True)
    upix = hpix2upix[hpix]
    ntargets = hpix_ntargets[hpix]
