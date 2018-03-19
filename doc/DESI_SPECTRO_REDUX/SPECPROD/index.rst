========
SPECPROD
========

Input files for spectroscopic reduction::

    $DESI_SPECTRO_DATA/{night}/
        desi-{expid}.fits.fz
        fibermap-{expid}.fits

    $DESI_SPECTRO_SIM/{night}/
        desi-{expid}.fits.fz
        fibermap-{expid}.fits
        pix-{camera}-{expid}.fits
        simpix-{camera}-{expid}.fits
        simspec-{expid}.fits

Output files::

    $DESI_SPECTRO_REDUX/$SPECPROD/
        config-{expid}.json
        pix-{camera}-{expid}.fits               -- optional
        exposures/{night}/{expid}/
            frame-{camera}-{expid}.fits
            skymodel-{camera}-{expid}.fits
            fluxcalib-{camera}-{expid}.fits
            cframe-{camera}-{expid}.fits
        spectra-{nside}/{group}/{pixnum}/
            spectra-{nside}-{pixnum}.fits
            zbest-{nside}-{pixnum}.fits
            coadd-{nside}-{pixnum}.fits     -- does not yet exist
        calib1d/{night}/
            fiberflat-{camera}-{expid}.fits
        calib2d/{night}/
            psf/psf-{camera}-{expid}.fits

Deprecated::

    $DESI_SPECTRO_REDUX/$SPECPROD/
        bricks/{brickid}/brick-{b|r|z}-{brickid}.fits

.. toctree::
   :maxdepth: 1

   bricks/index
   calib1d/index
   calib2d/index
   exposures/index
   spectra-NSIDE/index
   zcatalog-SPECPROD
