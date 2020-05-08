===========================================
fit-psf-fixed-blacklisted-CAMERA-EXPID.fits
===========================================

PSF (point spread function) files model the mapping of fibers and wavelengths
to pixels on spectrograph CCDs.  They all use the format as the
:doc:`psfnight files<../../../calibnight/NIGHT/psfnight>`.

Arc exposures have 4 different PSF files per camera:

  * ``shifted-input-psf-CAMERA-EXPID.fits```: Input PSF with spectral 
    trace coordinates
    and wavelength calibration adjusted to the current CCD image, used
    as a starting guess for the PSF shape fit.
  * ``fit-psf-before-blacklisted-fix-CAMERA-EXPID.fits``: Result
    of the specex PSF fit before
    ajusting the PSF model of problematic fibers not included in the fit.
  * ``fit-psf-fixed-blacklisted-CAMERA-EXPID.fits``: Result of
    the specex PSF fit with the PSF
    model of problematic fibers interpolated from neighboring fibers.
  * ``fit-psf-CAMERA-EXPID.fits``: Final PSF fit (which is the same as
    ``fit-psf-fixed-blacklisted-CAMERA-EXPID.fits``
    if there are problematic fibers)

The ``fit-psf`` files from individual exposures are combined into the
``calibnight/NIGHT/psfnight-CAMERA-NIGHT.fits`` files for each night.

Flat and science exposures have a single PSF file per camera:

  * ``psf-CAMERA-EXPID.fits``: psfnight file with spectral trace coordinates
    and wavelength solution adjusted to match this exposure.  Flat exposures
    are adjusted only in x (cross dispersion = fiber direction),
    while science exposures are adjusted in both x and y (wavelength direction).

:Regex: ``fit-psf-fixed-blacklisted-[brz][0-9]-[0-9]{8}\.fits``


