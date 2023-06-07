
=================
Bit Masks in DESI
=================

This page links to the URLs defining the bitmasks found in DESI files.
For details on working with these values, please see the tutorial_ on
that topic.

Redshift fitting (Redrock) masks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The **ZWARN** bitmask in redshift catalogs indicates known problems with a
particular redshift fit or associated QA.
ZWARN==0 is good; any non-zero value indicates a potential problem.
This mask will be described in more detail in the Redrock paper
(Bailey et al 2023 in prep), as well as Section 5.3.1 of the
Survey Operations Paper (Schlafly et al 2023 TODO: add link).

Bits 0-15 are set by Redrock itself (the redshift fitter),
while bits 16-19 are set by DESI-specific post-processing.

**ZWARN Bit Definitions**

==================== ========== ===========
Bit Name             Bit Number Description
==================== ========== ===========
SKY                           0 sky fiber
LITTLE_COVERAGE               1 too little wavelength coverage
SMALL_DELTA_CHI2              2 chi-squared of best fit is too close to that of second best
NEGATIVE_MODEL                3 synthetic spectrum is negative
MANY_OUTLIERS                 4 fraction of points more than 5 sigma away from best model is too large (>0.05)
Z_FITLIMIT                    5 chi-squared minimum at edge of the redshift fitting range
NEGATIVE_EMISSION             6 a QSO line exhibits negative emission, triggered only in QSO spectra, if  C_IV, C_III, Mg_II, H_beta, or H_alpha has LINEAREA + 3 * LINEAREA_ERR < 0
UNPLUGGED                     7 the fiber was unplugged/broken, so no spectrum obtained
BAD_TARGET                    8 catastrophically bad targeting data
NODATA                        9 No data for this fiber, e.g. because spectrograph was broken during this exposure (ivar=0 for all pixels)
BAD_MINFIT                   10 Bad parabola fit to the chi2 minimum
POORDATA                     11 Poor input data quality but try fitting anyway
LOW_DEL_CHI2                 16 DELTACHI2 is lower than 25 for a DESI SV3 target
LOW_DEL_CHI2_BGS             17 DELTACHI2 is lower than 40 for a DESI SV3 BGS target in bright time
BAD_SPECQA                   18 QA rejected due to spectrum-level problems
BAD_PETALQA                  19 QA rejected due to petal-level problems
==================== ========== ===========


Spectroscopic reduction masks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

=================================== ==================
BIT_MASK                            URL
=================================== ==================
QAFIBERSTATUS                       `MASKBITS_L55`_
FIBERSTATUS                         `MASKBITS_L55`_
COADD_FIBERSTATUS                   `MASKBITS_L55`_
MASK                                `MASKBITS_L84`_
=================================== ==================

The **FIBERSTATUS** bit mask is used to track the state of individual
fibers for issues that impact the entire spectrum, e.g. a broken fiber.
It is used in 

================ ============= ===========
File             HDU           Column
================ ============= ===========
`frame`_         FIBERMAP      FIBERSTATUS
`sframe`_        FIBERMAP      FIBERSTATUS
`cframe`_        FIBERMAP      FIBERSTATUS
`spectra`_       FIBERMAP      FIBERSTATUS
`coadd`_         EXP_FIBERMAP  FIBERSTATUS
`coadd`_         FIBERMAP      COADD_FIBERSTATUS
`exposure-qa`_   FIBERQA       QAFIBERSTATUS
`tile-qa`_       FIBERQA       QAFIBERSTATUS
================ ============= ===========

.. _`frame`: DESI_SPECTRO_REDUX/SPECPROD/exposures/NIGHT/EXPID/frame-CAMERA-EXPID.html
.. _`sframe`: DESI_SPECTRO_REDUX/SPECPROD/exposures/NIGHT/EXPID/sframe-CAMERA-EXPID.html
.. _`cframe`: DESI_SPECTRO_REDUX/SPECPROD/exposures/NIGHT/EXPID/cframe-CAMERA-EXPID.html
.. _`spectra`: DESI_SPECTRO_REDUX/SPECPROD/healpix/SURVEY/PROGRAM/PIXGROUP/PIXNUM/spectra-SURVEY-PROGRAM-PIXNUM.html
.. _`coadd`: DESI_SPECTRO_REDUX/SPECPROD/healpix/SURVEY/PROGRAM/PIXGROUP/PIXNUM/coadd-SURVEY-PROGRAM-PIXNUM.html
.. _`exposure-qa`: DESI_SPECTRO_REDUX/SPECPROD/exposures/NIGHT/EXPID/exposure-qa-EXPID.html
.. _`tile-qa`: DESI_SPECTRO_REDUX/SPECPROD/tiles/GROUPTYPE/TILEID/GROUPID/tile-qa-TILEID-GROUPID.html

**FIBERSTATUS Bit Definitions**

==================== ========== ===========
Bit Name             Bit Number Description
==================== ========== ===========
UNASSIGNED                    0 Fiber is not assigned to a known target or sky location
STUCKPOSITIONER               1 INFO: Stuck positioner (but could still be on a good sky location)
BROKENFIBER                   2 Broken fiber
RESTRICTED                    3 INFO: Positioner has restricted reach (but might still be on valid target)
MISSINGPOSITION               8 Fiber location information is missing
BADPOSITION                   9 Fiber >100 microns from target location
POORPOSITION                 10 Fiber >30 microns from target location
LOWTRANSMISSION              12 Low fiber transmission. Cannot use for sky.
LOWEFFTIME                   15 Effective time for this fiber is too low
BADFIBER                     16 Unusable fiber
BADTRACE                     17 Bad trace solution
BADFLAT                      18 Bad fiber flat
BADARC                       19 Bad arc solution
MANYBADCOL                   20 >10% of pixels are bad columns
MANYREJECTED                 21 >10% of pixels rejected in extraction
BADAMPB                      22 Issues in the amplifier readouts of camera B make this unusable
BADAMPR                      23 Issues in the amplifier readouts of camera R make this unusable
BADAMPZ                      24 Issues in the amplifier readouts of camera Z make this unusable
BADPETALPOS                  25 Too many fibers with bad positioning in petal
BADPETALSKY                  26 Bad sky model across petal
BADPETALSTDSTAR              27 To few standard stars or rms between stars too large in the petal
BADPETALFLUXCAL              28 Unphysical flux calibration for the petal (calib vector too high or too low)
BADPETALSNR                  29 TSNR is too low for this petal compared to the others
BADREADNOISE                 30 Bad read noise in one of the 3 cameras
RESERVED31                   31 Reserved sign bit; do not use
==================== ========== ===========


Target masks
~~~~~~~~~~~~

These masks are described in more detail in Appendix A and B of the
the DESI EDR paper (DESI Collaboration et al 2023 TODO: add link).

=================================== ==================
BIT_MASK                            URL
=================================== ==================
CMX_TARGET                          `CMX`_
SV1_DESI_TARGET                     `SV1`_
SV1_BGS_TARGET                      `SV1`_
SV1_MWS_TARGET                      `SV1`_
SV2_DESI_TARGET                     `SV2`_
SV2_BGS_TARGET                      `SV2`_
SV2_MWS_TARGET                      `SV2`_
SV2_SCND_TARGET                     `SV2`_
SV3_DESI_TARGET                     `SV3`_
SV3_BGS_TARGET                      `SV3`_
SV3_MWS_TARGET                      `SV3`_
SV3_SCND_TARGET                     `SV3`_
DESI_TARGET                         `TARGET`_
BGS_TARGET                          `TARGET`_
MWS_TARGET                          `TARGET`_
SCND_TARGET                         `TARGET`_
OBSCONDITIONS                       `TARGET_L188`_
=================================== ==================


Imaging masks
~~~~~~~~~~~~~

These masks were defined or used by the `DESI Legacy Imaging Surveys`_. Please
see their information on these masks at the links below.

=================================== ==================
BIT_MASK                            URL
=================================== ==================
WISEMASK_W1                         `BITMASKS_LEGACY`_
WISEMASK_W2                         `BITMASKS_LEGACY`_
MASKBITS                            `BITMASKS_LEGACY`_
=================================== ==================


.. _`CMX`: https://github.com/desihub/desitarget/blob/2.5.0/py/desitarget/cmx/data/cmx_targetmask.yaml
.. _`SV1`: https://github.com/desihub/desitarget/blob/2.5.0/py/desitarget/sv1/data/sv1_targetmask.yaml
.. _`SV2`: https://github.com/desihub/desitarget/blob/2.5.0/py/desitarget/sv2/data/sv2_targetmask.yaml
.. _`SV3`: https://github.com/desihub/desitarget/blob/2.5.0/py/desitarget/sv3/data/sv3_targetmask.yaml
.. _`TARGET`: https://github.com/desihub/desitarget/blob/2.5.0/py/desitarget/data/targetmask.yaml
.. _`MASKBITS_L55`: https://github.com/desihub/desispec/blob/0.55.0/py/desispec/maskbits.py#L55
.. _`TARGET_L188`: https://github.com/desihub/desitarget/blob/2.5.0/py/desitarget/data/targetmask.yaml#L188
.. _`MASKBITS_L84`: https://github.com/desihub/desispec/blob/0.55.0/py/desispec/maskbits.py#L84
.. _`ZWARN`: https://github.com/desihub/redrock/blob/0.16.0/py/redrock/zwarning.py#L14
.. _`BITMASKS_LEGACY`: https://www.legacysurvey.org/dr9/bitmasks/
.. _`DESI Legacy Imaging Surveys`: https://www.legacysurvey.org/
.. _tutorial: https://github.com/desihub/desitarget/blob/master/doc/nb/target-selection-bits-and-bitmasks.ipynb

