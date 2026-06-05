=======
uniqpix
=======

:Summary: This file contains a summary of which uniqpix are covered by this survey and program.
:Naming Convention: ``uniqpix-SURVEY-PROGRAM.fits``,
    where SURVEY is main, sv1, sv2, sv3, special, or cmx;
    and PROGRAM is bright, dark, backup, or other.
:Regex: ``uniqpix-(cmx|main|special|sv1|sv2|sv3)-(backup|bright|dark|other).fits``
:File Type: FITS, 430 KB

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents
====== ======= ======== ===================
HDU0_          IMAGE    Blank
HDU1_  UNIQPIX BINTABLE Table with UNIQPIX, NTARGETS, NSPECTRA
====== ======= ======== ===================


FITS Header Units
=================

HDU0
----

This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = UNIQPIX

Table giving the number of targets and spectra for each uniqpix in this survey and program.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ======== ============= ==== =====================
    KEY      Example Value Type Comment
    ======== ============= ==== =====================
    NAXIS1   24            int  Size of each table row
    NAXIS2   17929         int  Number of table rows = number of uniqpix
    SURVEY   main          str  DESI survey name, e.g. main, sv1, sv2, sv3, special, or cmx
    PROGRAM  dark          str  DESI program name, e.g. bright, dark, backup, or other
    SPECPROD matterhorn    str  DESI spectro pipeline product name, e.g. matterhorn or nevis
    ======== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

======== ===== ===== ===========
Name     Type  Units Description
======== ===== ===== ===========
UNIQPIX  int64       Unique pixel identifier = healpix + 4*nside^2
NTARGETS int64       Number of unique TARGETIDs in this uniqpix for this survey and program
NSPECTRA int64       Number of input uncoadded spectra in this uniqpix for this survey and program
======== ===== ===== ===========


Notes and Examples
==================

Example usage::

    from astropy.table import Table
    import numpy as np
    import healpy

    survey = 'special'
    program = 'dark'
    upix_table = Table.read(f'spectra/{survey}/{program}/uniqpix-{survey}-{program}.fits')
    for upix, ntargets in upix_table['UNIQPIX', 'NTARGETS']:
        nside = 2**int(np.log2(upix//4)/2)
        hpix = upix - 4 * nside**2
        area = healpy.nside2pixarea(nside, degrees=True)
        density = ntargets / area

        pixgroup = upix//100
        coaddfile = f'spectra/special/dark/{pixgroup}/{upix}/coadd-special-dark-{upix}.fits'

        print(f'{coaddfile} at {nside=} has {ntargets} targets ({density:,.1f}/deg^2)')

Output for the matterhorn production::

    spectra/special/dark/0/5/coadd-special-dark-5.fits at nside=1 has 353 targets (0.1/deg^2)
    spectra/special/dark/0/7/coadd-special-dark-7.fits at nside=1 has 3965 targets (1.2/deg^2)
    spectra/special/dark/0/9/coadd-special-dark-9.fits at nside=1 has 1147 targets (0.3/deg^2)
    ...
    spectra/special/dark/6996/699669/coadd-special-dark-699669.fits at nside=256 has 2119 targets (40,395.9/deg^2)
    spectra/special/dark/6996/699670/coadd-special-dark-699670.fits at nside=256 has 2045 targets (38,985.2/deg^2)
    spectra/special/dark/6996/699671/coadd-special-dark-699671.fits at nside=256 has 1261 targets (24,039.3/deg^2)

Note that the vastly different target densities get covered by different nside pixels so
that each file has at most few thousand targets.


