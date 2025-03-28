
=================
Bit Masks in DESI
=================

.. NOTE: this file is generated by desidatamodel/bin/update_bitmasks, e.g.
..   cd desidatamodel/doc
..   python ../bin/update_bitmasks > bitmasks.rst && make html

DESI uses bitmasks for both target selection (each bit representing a different
reason why a target is selected for observation) and quality flags (each bit
representing a different problem).
This page describes the bitmasks found in DESI files.
For details on working with these values, please see the tutorial_ on
that topic.

Summary of Bit Masks
--------------------

========================================== ===========
**Spectroscopic Pipeline**
:ref:`ZWARN <zwarn-bitmask>`               Redshift fitting quality flags
:ref:`FIBERSTATUS <fiberstatus-bitmask>`   Hardware-related quality flags per fiber
:ref:`SPECMASK <specmask-bitmask>`         Spectral quality flag per spectrum per wavelength
:ref:`CCDMASK <ccdmask-bitmask>`           Spectrograph 2D CCD image quality flags
**Target Selection**
:ref:`DESI_TARGET <target-bitmasks>`       Target selection for dark time targets and calibrators
:ref:`BGS_TARGET <target-bitmasks>`        Target selection for the Bright Galaxy Survey
:ref:`MWS_TARGET <target-bitmasks>`        Target selection for the Milky Way Survey
:ref:`SCND_TARGET <target-bitmasks>`       Target selection for secondary targets
:ref:`OBSCONDITIONS <target-bitmasks>`     Observing conditions for target classes
**Imaging for Target Selection Input**
:ref:`WISEMASK_W1 <imaging-bitmasks>`      WISE W1 quality mask
:ref:`WISEMASK_W2 <imaging-bitmasks>`      WISE W2 quality mask
:ref:`MASKBITS <imaging-bitmasks>`         Tractor input imaging quality mask
========================================== ===========

In addition to the above target selection bitmasks, there are also equivalent
Survey Validation masks SV1, SV2, and SV3; see :ref:`Target Selection Bitmasks <target-bitmasks>`.

Redshift Fitting (Redrock) Masks
--------------------------------

.. _zwarn-bitmask:

ZWARN
~~~~~

The **ZWARN** bitmask in redshift catalogs indicates known problems with a
particular redshift fit or associated QA.
ZWARN==0 is good; any non-zero value indicates a potential problem.
This mask will be described in more detail in the Redrock paper
(Bailey et al. 2023 in prep), as well as Section 5.3.1 of the
Survey Operations Paper (`Schlafly et al. 2023 <https://ui.adsabs.harvard.edu/abs/2023AJ....166..259S/abstract>`_).

The canonical code location defining these bits is
`desitarget targetmask.yaml <https://github.com/desihub/desitarget/blob/main/py/desitarget/data/targetmask.yaml#L230>`_.
Bits 0-15 are set by Redrock itself (the redshift fitter),
while bits 16-19 are set by DESI-specific post-processing.

ZWARN Mask Locations
^^^^^^^^^^^^^^^^^^^^

================ ============= ===========
File             Table HDU     Column
================ ============= ===========
|redrock|        REDSHIFTS     ZWARN
|emline|         EMLINEFIT     ZWARN
|zmtl|           ZMTL          ZWARN
|mtl|            MTL           ZWARN
|zpix|           ZCATALOG      ZWARN
|ztile|          ZCATALOG      ZWARN
|zall|           ZCATALOG      ZWARN
|lss|            LSS           ZWARN
================ ============= ===========

.. |redrock| replace:: :doc:`redrock <DESI_SPECTRO_REDUX/SPECPROD/tiles/GROUPTYPE/TILEID/GROUPID/redrock-SPECTROGRAPH-TILEID-GROUPID>`
.. |emline| replace:: :doc:`emline <DESI_SPECTRO_REDUX/SPECPROD/tiles/GROUPTYPE/TILEID/GROUPID/emline-SPECTROGRAPH-TILEID-GROUPID>`
.. |zmtl| replace:: :doc:`zmtl <DESI_SPECTRO_REDUX/SPECPROD/tiles/GROUPTYPE/TILEID/GROUPID/zmtl-SPECTROGRAPH-TILEID-GROUPID>`
.. |mtl| replace:: :doc:`mtl <DESI_SURVEYOPS/mtl/main/dark/mtl-dark-hp-HPX>`
.. |zpix| replace:: :doc:`zpix <DESI_SPECTRO_REDUX/SPECPROD/zcatalog/v1/zpix-SURVEY-PROGRAM>`
.. |ztile| replace:: :doc:`ztile <DESI_SPECTRO_REDUX/SPECPROD/zcatalog/v1/ztile-SURVEY-PROGRAM-GROUPTYPE>`
.. |zall| replace:: :doc:`zall <DESI_SPECTRO_REDUX/SPECPROD/zcatalog/v1/zall-pix-SPECPROD>`
.. |lss| replace:: :doc:`lss <DESI_ROOT/vac/RELEASE/lss/VERSION/LSScats/full/fullVETO_dat>`

ZWARN Bit Definitions
^^^^^^^^^^^^^^^^^^^^^


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


Spectroscopic Reduction Masks
-----------------------------

The **FIBERSTATUS** bit mask records the state of individual
fibers for issues that impact the entire spectrum, e.g. a broken fiber.
The **SPECMASK** bit mask tracks wavelength dependent isses per spectrum,
e.g. masks for cosmic rays.

.. _fiberstatus-bitmask:

FIBERSTATUS
~~~~~~~~~~~

The **FIBERSTATUS** mask is kept as a column in FIBERMAP and related HDUs.
Bits 0-7 are set by fiber assignment from focal plane information known
before observations; bits 8-24 are set by the spectroscopic pipeline;
bits 25-30 are set by the final QA step to set bits for all fibers in
a petal (e.g. because sky model noise makes all spectra questionable).

Unlike the other quality masks
(:ref:`ZWARN <zwarn-bitmask>`, :ref:`SPECMASK <specmask-bitmask>`, :ref:`CCDMASK <ccdmask-bitmask>`),
FIBERSTATUS contains informative bits that aren't necessarily bad.
See details in the "FIBERSTATUS Bit Definitions" section below.

The canonical code location defining FIBERSTATUS bits is
`desispec.maskbits L55 <https://github.com/desihub/desispec/blob/0.55.0/py/desispec/maskbits.py#L55>`_.

FIBERSTATUS Mask Locations
^^^^^^^^^^^^^^^^^^^^^^^^^^

================ ============= ===========
File             Table HDU     Column
================ ============= ===========
|frame|          FIBERMAP      FIBERSTATUS
|sframe|         FIBERMAP      FIBERSTATUS
|cframe|         FIBERMAP      FIBERSTATUS
|spectra|        FIBERMAP      FIBERSTATUS
|coadd|          EXP_FIBERMAP  FIBERSTATUS
|coadd|          FIBERMAP      COADD_FIBERSTATUS
|redrock|        FIBERMAP      COADD_FIBERSTATUS
|exposure-qa|    FIBERQA       QAFIBERSTATUS
|tile-qa|        FIBERQA       QAFIBERSTATUS
================ ============= ===========

.. |frame| replace:: :doc:`frame <DESI_SPECTRO_REDUX/SPECPROD/exposures/NIGHT/EXPID/frame-CAMERA-EXPID>`
.. |sframe| replace:: :doc:`sframe <DESI_SPECTRO_REDUX/SPECPROD/exposures/NIGHT/EXPID/sframe-CAMERA-EXPID>`
.. |cframe| replace:: :doc:`cframe <DESI_SPECTRO_REDUX/SPECPROD/exposures/NIGHT/EXPID/cframe-CAMERA-EXPID>`
.. |spectra| replace:: :doc:`spectra <DESI_SPECTRO_REDUX/SPECPROD/healpix/SURVEY/PROGRAM/PIXGROUP/PIXNUM/spectra-SURVEY-PROGRAM-PIXNUM>`
.. |coadd| replace:: :doc:`coadd <DESI_SPECTRO_REDUX/SPECPROD/healpix/SURVEY/PROGRAM/PIXGROUP/PIXNUM/coadd-SURVEY-PROGRAM-PIXNUM>`
.. |exposure-qa| replace:: :doc:`exposure-qa <DESI_SPECTRO_REDUX/SPECPROD/exposures/NIGHT/EXPID/exposure-qa-EXPID>`
.. |tile-qa| replace:: :doc:`tile-qa <DESI_SPECTRO_REDUX/SPECPROD/tiles/GROUPTYPE/TILEID/GROUPID/tile-qa-TILEID-GROUPID>`

FIBERSTATUS Bit Definitions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

==================== ========== ===========
Bit Name             Bit Number Description
==================== ========== ===========
UNASSIGNED                    0 Fiber is not assigned to a known target or sky location
STUCKPOSITIONER               1 INFO: Stuck positioner (but could still be on a valid sky location, though not a science target)
BROKENFIBER                   2 Broken fiber
RESTRICTED                    3 INFO: Positioner has restricted reach (but might still be on valid target)
MISSINGPOSITION               8 Fiber location information is missing
BADPOSITION                   9 Fiber >100 microns from target location
POORPOSITION                 10 Fiber >30 microns from target location
LOWTRANSMISSION              12 Low fiber transmission. Cannot use for sky.
NEARCHARGETRAP               13 INFO: Fiber trace near charge trap in one of the CCDs
VARIABLETHRU                 14 INFO: Fiber has throughput variations we cannot model well
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

**Notes**:

* Bit 3 (RESTRICTED) is informative and doesn't necessarily mean that the spectrum is bad,
  i.e. a FIBERSTATUS value of 0 or 8=2**3 is good.
* Bit 13 (NEARCHARGETRAP) is fine for most targets but indicates a potential problem for analyses
  that need consistent purity/completeness, especially for faint targets.
* Bit 14 (VARIABLETHRU) have questionable flux calibration, but typically the redshifts are ok.
* Bits 13 and 14 were added for DR2/Loa, but were not set at the time of DR1/Iron.

.. _specmask-bitmask:

SPECMASK
~~~~~~~~

The **SPECMASK** is stored as an image HDU in files with spectra,
matched to the FLUX HDU, i.e. specmask[i,j] is the mask for fiber i
wavelength j with flux value flux[i,j].  All bits in SPECMASK are bad,
i.e. non-zero values mean that the corresponding flux should not be used.

The canonical code location defining SPECMASK bits is
`desispec.maskbits L84 <https://github.com/desihub/desispec/blob/0.55.0/py/desispec/maskbits.py#L84>`_.

SPECMASK Mask Locations
^^^^^^^^^^^^^^^^^^^^^^^

Note: the FITS file HDU EXTNAME=MASK or B/R/Z_MASK, not "SPECMASK".

================ =============
File             Image HDU
================ =============
|frame|          MASK
|sframe|         MASK
|cframe|         MASK
|spectra|        B/R/Z_MASK
|coadd|          B/R/Z_MASK
================ =============

SPECMASK Bit Definitions
^^^^^^^^^^^^^^^^^^^^^^^^


==================== ========== ===========
Bit Name             Bit Number Description
==================== ========== ===========
SOMEBADPIX                    0 Some input pixels were masked or ivar=0
ALLBADPIX                     1 All input pixels were masked or ivar=0
COSMIC                        2 Input pixels included a masked cosmic
LOWFLAT                       3 Fiber flat < 0.5
BADFIBERFLAT                  4 Bad fiber flat solution
BRIGHTSKY                     5 Bright sky level (details TBD)
BADSKY                        6 Bad sky model
BAD2DFIT                      7 Bad fit of extraction 2D model to pixel data
NODATA                        8 No data exists
BADFIBER                      9 fibermask has a non-zero bit
BADCOLUMN                    10 Bad CCD column biases the flux
==================== ========== ===========

.. _ccdmask-bitmask:

CCDMASK
~~~~~~~

The **CCDMASK** is used for masking spectrograph CCD images during preprocessing,
prior to extracting the spectra.  It is stored in the MASK HDU of
:doc:`preproc <DESI_SPECTRO_REDUX/SPECPROD/preproc/NIGHT/EXPID/preproc-CAMERA-EXPID>` files.

The canonical code location defining CCDMASK bits is
`desispec.maskbits L42 <https://github.com/desihub/desispec/blob/0.55.0/py/desispec/maskbits.py#L42>`_.

CCDMASK Bit Definitions
^^^^^^^^^^^^^^^^^^^^^^^


==================== ========== ===========
Bit Name             Bit Number Description
==================== ========== ===========
BAD                           0 Pre-determined bad pixel (any reason)
HOT                           1 Hot pixel
DEAD                          2 Dead pixel
SATURATED                     3 Saturated pixel from object
COSMIC                        4 Cosmic ray
PIXFLATZERO                   5 pixflat is 0
PIXFLATLOW                    6 pixflat < 0.1
HIGHVAR                       7 High variability in pixel value
BADREADNOISE                  8 Very high CCD amplifier read noise
==================== ========== ===========


.. _target-bitmasks:

Target masks
------------

Target masks record the reasons why each target was selected for DESI
observations.  These are stored in the ``*_TARGET`` columns of the
TARGETS, FIBERASSIGN, and FIBERMAP tables in data files.

These masks are described in more detail in Section 2 of
`Myers et al. (2023) <https://ui.adsabs.harvard.edu/abs/2023AJ....165...50M/abstract>`_
and Appendices A and B of the the DESI EDR Overview paper
(`DESI Collaboration et al. 2024 <https://ui.adsabs.harvard.edu/abs/2024AJ....168...58D/abstract>`_).

The following table lists a subset of the most commonly used bits that maintained
the same definition throughout different phases of DESI observations.  For the
full definition of all bits, see the EDR Overview paper appendices and the
code links in the second table below.

==================== ========== ===========
Bit Name             Bit Number Description
==================== ========== ===========
LRG                  0          Luminous Red Galaxies
ELG                  1          Emission Line Galaxies
QSO                  2          Quasars
SKY                  32         Blank sky locations
(various STD_*)      33-35      Standard stars
BGS_ANY              60         Bright Galaxy Survey galaxies
MWS_ANY              61         Milky Way Survey stars
SCND_ANY             62         Secondary targets
==================== ========== ===========


Canonical code locations where targeting bits are defined:

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

.. _imaging-bitmasks:

Imaging masks
-------------

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
.. _tutorial: https://github.com/desihub/desitarget/blob/main/doc/nb/target-selection-bits-and-bitmasks.ipynb

