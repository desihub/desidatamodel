=======
UNIQPIX
=======

Default $DESI_ROOT/spectro/redux/SPECPROD/spectra/SURVEY/PROGRAM/PIXGROUP/UNIQPIX

  * SURVEY = sv1, sv3, main, ...
  * PROGRAM = dark,bright,backup,other
  * UNIQPIX = HEALPIX + 4*NSIDE^2 adaptively sided pixel
  * PIXGROUP = int(PIXNUM/100)

The available files and formats are the same as those in the
:doc:`healpix directory tree </DESI_SPECTRO_REDUX/SPECPROD/healpix/SURVEY/PROGRAM/PIXGROUP/PIXNUM/index>`
with the addition of a ``UNIQPIX`` header heyword.
