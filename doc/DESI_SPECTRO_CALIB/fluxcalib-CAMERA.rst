=====================
fluxcalib-CAMERA.fits
=====================

:Summary: Flux calibration file contains an average calibration model for a
    given camera including airmass and seeing dependencies.
:Naming Convention: ``fluxcalib-{CAMERA}.fits``, where where ``{CAMERA}`` is
    one of the spectrograph cameras (*e.g.* ``z1``).
:Regex: ``fluxcalib-{brz][0-9].fits``
:File Type: FITS, 84 KB

The model is parameterized as

calibration_model(lambda) = average_cal(lambda) * 10^( -0.4*( (seeing-pivot_seeing)*seeing_term(lambda) + (airmass-pivot_airmass)*atm_ext(lambda) ))

calib_flux [1e-17 erg/s/cm2/Angstrom] = uncalib_flux [counts/Angstrom] / (calibration_model * exptime [s])

Contents
========

====== ================================== ===== ===================
Number EXTNAME                            Type  Contents
====== ================================== ===== ===================
HDU0_  FLUXCALIB                          IMAGE Average flux calibration
HDU1_  ATERM                              IMAGE Airmass dependent term
HDU2_  STERM                              IMAGE Seeing dependent term
HDU3_  WAVELENGTH                         IMAGE Wavelength grid
HDU4_  ATERM_ERR                          IMAGE Uncertainty on airmass dependent term
HDU5_  STERM_ERR                          IMAGE Uncertainty on seeing dependent term
====== ================================== ===== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = FLUXCALIB

Average flux calibration model such that calibrated flux = uncalibrated photons / model.


Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ==== ==============================================
KEY      Example Value             Type Comment
======== ========================= ==== ==============================================
NAXIS1   2380                      int
BUNIT    10**+17 cm2 count s / erg str  i.e. (elec/A) / (1e-17 erg/s/cm2/A)
CHECKSUM 2pfC2ofA2ofA2ofA          str  HDU checksum updated 2018-11-27T11:46:41
DATASUM  3135063907                str  data unit checksum updated 2018-11-27T11:46:41
======== ========================= ==== ==============================================

Data: FITS image [float32, 2380]

HDU1
----

EXTNAME = ATERM

Atmospheric extinction term

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================= ===== ==============================================
KEY      Example Value     Type  Comment
======== ================= ===== ==============================================
NAXIS1   2380              int
PAIRMASS 1.132032318244172 float pivot airmass (airmass of average calib.)
CHECKSUM Xd3dYd0bXd0bXd0b  str   HDU checksum updated 2018-11-27T11:46:41
DATASUM  1519080666        str   data unit checksum updated 2018-11-27T11:46:41
======== ================= ===== ==============================================

Data: FITS image [float32, 2380]

HDU2
----

EXTNAME = STERM

Seeing term

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================= ===== ==============================================
KEY      Example Value     Type  Comment
======== ================= ===== ==============================================
NAXIS1   2380              int
PSEEING  1.075342118740081 float pivot seeing (seeing of average calib.), FWHM arcsec
CHECKSUM IOTaKNRTINRZINRZ  str   HDU checksum updated 2018-11-27T11:46:41
DATASUM  1211437529        str   data unit checksum updated 2018-11-27T11:46:41
======== ================= ===== ==============================================

Data: FITS image [float32, 2380]

HDU3
----

EXTNAME = WAVELENGTH

Wavelengths at which the flux calibration model is evaluated.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2380             int
BUNIT    Angstrom         str
CHECKSUM CbCQFZ9OCaAOCY9O str  HDU checksum updated 2018-11-27T11:46:41
DATASUM  3517056679       str  data unit checksum updated 2018-11-27T11:46:41
======== ================ ==== ==============================================

Data: FITS image [float32, 2380]

HDU4
----

EXTNAME = ATERM_ERR

Uncertainty on atmospheric extinction term

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2380             int
CHECKSUM fCmKhBkHfBkHfBkH str  HDU checksum updated 2018-11-27T11:46:41
DATASUM  984665518        str  data unit checksum updated 2018-11-27T11:46:41
======== ================ ==== ==============================================

Data: FITS image [float32, 2380]

HDU5
----

EXTNAME = STERM_ERR

Uncertainty on seeing dependent term

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2380             int
CHECKSUM LaNJNZNJLaNJLYNJ str  HDU checksum updated 2018-11-27T11:46:41
DATASUM  803867299        str  data unit checksum updated 2018-11-27T11:46:41
======== ================ ==== ==============================================

Data: FITS image [float32, 2380]


Notes and Examples
==================

File produced by the desispec script desi_average_flux_calibration.
Used by QuickLook and the off-line calibration.
