=========================
fit-psf-CAMERA-EXPID.fits
=========================

:Summary: PSF (point spread function) files model the mapping of fibers and wavelengths
    to pixels on spectrograph CCDs.
:Naming Convention: ``fit-psf-CAMERA-EXPID.fits``, where ``CAMERA`` is
    *e.g.*, "b0", "r5", etc. and ``EXPID`` is 8-digit exposure number.
:Regex: ``fit-psf-[brz][0-9]-[0-9]{8}(_[0-9][0-9]|)\.fits``
:File Type: FITS, 998 KB

See :doc:`psfnight <../../../calibnight/NIGHT/psfnight-CAMERA-NIGHT>`.

Arc exposures have 4 different PSF files per camera:

1. :doc:`shifted-input-psf-CAMERA-EXPID.fits <shifted-input-psf-CAMERA-EXPID>`:
   Input PSF with spectral trace coordinates and wavelength calibration
   adjusted to the current CCD image, used as a starting guess for the PSF shape fit.
2. :doc:`fit-psf-before-listed-fix-CAMERA-EXPID.fits <fit-psf-before-listed-fix-CAMERA-EXPID>`: Result
   of the specex PSF fit before adjusting the PSF model of
   problematic fibers not included in the fit.
3. :doc:`fit-psf-fixed-listed-CAMERA-EXPID.fits <fit-psf-fixed-listed-CAMERA-EXPID>`:
   Result of the specex PSF fit with the PSF model of problematic fibers
   interpolated from neighboring fibers.
4. ``fit-psf-CAMERA-EXPID.fits``: Final PSF fit
   (which is the same as
   :doc:`fit-psf-fixed-listed-CAMERA-EXPID.fits <fit-psf-fixed-listed-CAMERA-EXPID>`
   if there are problematic fibers)

The ``fit-psf-*.fits`` files from individual exposures are combined into the
:doc:`psfnight <../../../calibnight/NIGHT/psfnight-CAMERA-NIGHT>` files for each night.

Flat and science exposures have a single PSF file per camera:

:doc:`psf-CAMERA-EXPID.fits <psf-CAMERA-EXPID>`: psfnight file with spectral trace coordinates
and wavelength solution adjusted to match this exposure.  Flat exposures
are adjusted only in x (cross dispersion = fiber direction),
while science exposures are adjusted in both x and y (wavelength direction).
