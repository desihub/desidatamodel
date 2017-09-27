============================
brick-CHANNEL-BRICKNAME.fits
============================

**Organization of spectra by brick is deprecated; see spectra/ instead.**

:Summary: Brick files hold the calibrated individual exposure spectra organized by
    location on the sky (brick).  This should contain the same information as
    cframe files, just differently organized.  They should be complete enough
    to generate a coadd based only on information in this file.
:Naming Convention: ``brick-{channel}-{brickname}.fits``, where
    ``{channel}`` is 'b', 'r', or 'z', and
    ``{brickname}`` is the brick name string as given by targeting, *e.g.* "1234p567".
:Regex: ``brick-[brz]-[0-9]{4}[pm][0-9]{3}\.fits``
:File Type: FITS, 31 MB

Inputs
======

Written by desi_make_bricks.py, using:

- cframe
- fibermap

Contents
========

====== ========== ======== ===================
Number EXTNAME    Type     Contents
====== ========== ======== ===================
HDU0_  FLUX       IMAGE    Spectral flux [nspec, nwave]
HDU1_  IVAR       IMAGE    Inverse variance of flux
HDU2_  WAVELENGTH IMAGE    1D common wavelength grid in Angstroms
HDU3_  RESOLUTION IMAGE    3D sparse resolution matrix data [nspec,ndiag,nwave]
HDU4_  FIBERMAP   BINTABLE Fibermap entries
====== ========== ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = FLUX

Spectral flux[nspec, nwave] in erg/s/cm^2/Angstrom

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============= ==== ============
KEY      Example Value Type Comment
======== ============= ==== ============
NAXIS1   3494          int  Number of wavelength bins
NAXIS2   51            int  Number of spectra
BRICKNAM 3321p125      str  Imaging brick name
CHANNEL  r             str  Spectrograph channel [b,r,z]
EXTNAME  FLUX          str  erg/s/cm^2/Angstrom
======== ============= ==== ============

Data: FITS image [float64]

HDU1
----

EXTNAME = IVAR

Inverse variance of the flux

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============= ==== ============
KEY      Example Value Type Comment
======== ============= ==== ============
NAXIS1   3494          int  Number of wavelength bins
NAXIS2   51            int  Number of spectra
BRICKNAM 3321p125      str  Imaging brick name
CHANNEL  r             str  Spectrograph channel [b,r,z]
EXTNAME  IVAR          str  1 / (erg/s/cm^2/A)^2
======== ============= ==== ============

Data: FITS image [float64]

HDU2
----

EXTNAME = WAVELENGTH

Common wavelength grid in Angstroms

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============= ==== ===========
KEY      Example Value Type Comment
======== ============= ==== ===========
NAXIS1   3494          int  wavelength [Angstroms]
BRICKNAM 3321p125      str  Imaging brick name
CHANNEL  r             str  Spectrograph channel [b,r,z]
EXTNAME  WAVELENGTH    str  [Angstroms]
======== ============= ==== ===========

Data: FITS image [float64]

HDU3
----

EXTNAME = RESOLUTION

Resolution matrix data.  TODO: define this.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============= ==== ============
KEY      Example Value Type Comment
======== ============= ==== ============
NAXIS1   3494          int  Number of wavelength bins
NAXIS2   21            int  Number of diagonals
NAXIS3   51            int  Number of spectra
BRICKNAM 3321p125      str  Imaging brick name
CHANNEL  r             str  Spectrograph channel [b,r,z]
EXTNAME  RESOLUTION    str  no dimension
======== ============= ==== ============

Data: FITS image [float64]

HDU4
----

EXTNAME = FIBERMAP

Fibermap data, copied here to allow the bricks to be self-contained.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============= ==== =====================
KEY      Example Value Type Comment
======== ============= ==== =====================
NAXIS1   224           int  length of dimension 1
NAXIS2   51            int  Number of spectra
BRICKNAM 3321p125      str  Imaging brick name
CHANNEL  r             str  Spectrograph channel [b,r,z]
EXTNAME  FIBERMAP      str
======== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

============ ========== ===== ===========
Name         Type       Units Description
============ ========== ===== ===========
OBJTYPE      char[10]
TARGETCAT    char[20]
BRICKNAME    char[8]
TARGETID     int64
DESI_TARGET  int64
BGS_TARGET   int64
MWS_TARGET   int64
MAG          float32[5]
FILTER       char[50]
SPECTROID    int64
POSITIONER   int64
FIBER        int32
LAMBDAREF    float32
RA_TARGET    float64
DEC_TARGET   float64
RA_OBS       float64
DEC_OBS      float64
X_TARGET     float64
Y_TARGET     float64
X_FVCOBS     float64
Y_FVCOBS     float64
Y_FVCERR     float32
X_FVCERR     float32
NIGHT        int32
EXPID        int32
INDEX        int32
============ ========== ===== ===========
