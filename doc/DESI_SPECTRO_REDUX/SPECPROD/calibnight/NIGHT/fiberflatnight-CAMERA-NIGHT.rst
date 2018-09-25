===========================
fiberflatnight-CAMERA-NIGHT
===========================

:Summary: Relative fiber-to-fiber variations ("fiberflat") as measured by
    continuum lamp calibration spectra, combined across multiple exposures.
    Corrected flux = original flux / fiberflat.
:Naming Convention: ``fiberflatnight-CAMERA-NIGHT.fits``, where ``CAMERA`` is
    *e.g.*, "b0", "r5", etc. and ``NIGHT`` is the observation night in
    YYYYMMDD format.
:Regex: ``fiberflatnight-[brz][0-9]-[0-9]{8}.fits``
:File Type: FITS, 10 MB

Contents
========

====== ========== ======== =================================
Number EXTNAME    Type     Contents
====== ========== ======== =================================
HDU0_  FIBERFLAT  IMAGE    Relative fiber-to-fiber variation
HDU1_  IVAR       IMAGE    Inverse variance of fiberflat
HDU2_  MASK       BINTABLE Mask of fiberflat (0=good)
HDU3_  MEANSPEC   IMAGE    Average spectrum
HDU4_  WAVELENGTH IMAGE    Wavelength
====== ========== ======== =================================


FITS Header Units
=================

HDU0
----

EXTNAME = FIBERFLAT

Relative fiber-to-fiber variation.  Corrected flux = original flux / fiberflat.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================= ===== ==============================================
KEY      Example Value           Type  Comment
======== ======================= ===== ==============================================
NAXIS1   2645                    int
NAXIS2   500                     int
EXPID    25                      int
NIGHT    20200318                str
FLAVOR   flat                    str
DOSVER   SIM                     str
DATE-OBS 2020-03-18T22:00:00.000 str
EXPTIME  10.0                    float
FEEVER   SIM                     str
AIRORVAC vac                     str   Vacuum wavelengths
CAMERA   r6                      str
FIBERMIN 3000                    int
CHECKSUM 3GDaAE9W6ECaAE9U        str   HDU checksum updated 2018-03-29T21:38:41
DATASUM  2868401259              str   data unit checksum updated 2018-03-29T21:38:41
CHI2PDF  1.052080036564363       float
======== ======================= ===== ==============================================

Data: FITS image [float32, 2645x500]

HDU1
----

EXTNAME = IVAR

Inverse variance of fiberflat

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2645             int
NAXIS2   500              int
CHECKSUM QedlRcbkQcbkQcbk str  HDU checksum updated 2018-03-29T21:38:41
DATASUM  2161531188       str  data unit checksum updated 2018-03-29T21:38:41
======== ================ ==== ==============================================

Data: FITS image [float32, 2645x500]

HDU2
----

EXTNAME = MASK

Mask of fiberflat (0=good)

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   8                int  width of table in bytes
NAXIS2   500              int  number of rows in table
BSCALE   1                int
BZERO    2147483648       int
CHECKSUM LmE7NjE7LjE7LjE7 str  HDU checksum updated 2018-03-29T21:38:41
DATASUM  7014250          str  data unit checksum updated 2018-03-29T21:38:41
======== ================ ==== ==============================================

Data: FITS image [int32, 8x500]

HDU3
----

EXTNAME = MEANSPEC

Average continuum lamp spectrum

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2645             int
CHECKSUM 9bCFEZAF9bAFEZAF str  HDU checksum updated 2018-03-29T21:38:41
DATASUM  360710800        str  data unit checksum updated 2018-03-29T21:38:41
======== ================ ==== ==============================================

Data: FITS image [float32, 2645]

HDU4
----

EXTNAME = WAVELENGTH

Wavelengths at which the fiberflat is measured

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2645             int
BUNIT    Angstrom         str
CHECKSUM 7A46A9240A247724 str  HDU checksum updated 2018-03-29T21:38:41
DATASUM  1455388369       str  data unit checksum updated 2018-03-29T21:38:41
======== ================ ==== ==============================================

Data: FITS image [float32, 2645]


Notes and Examples
==================

Corrected flux = original flux / fiberflat.

.. code::

  fiberflat = desispec.fiberflat.compute_fiberflat(flatframe)
  desispec.fiberflat.apply_fiberflat(scienceframe, fiberflat)
