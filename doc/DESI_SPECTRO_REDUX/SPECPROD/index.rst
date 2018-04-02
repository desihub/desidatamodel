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
        pix-{camera}-{expid}.fits               -- optional
        calibnight/{night}/
            fiberflatnight-{camera}-{night}.fits
        calibnight/psf/{night}/
            psf-{camera}.fits
        exposures/{night}/{expid}/
            calib-{camera}-{expid}.fits
            cframe-{camera}-{expid}.fits
            frame-{camera}-{expid}.fits
            psf-{camera}-{expid}.fits
            psfboot-{camera}-{expid}.fits
            sky-{camera}-{expid}.fits
            stdstars-{spectrograph}-{expid}.fits
        spectra-{nside}/{group}/{pixnum}/
            coadd-{nside}-{pixnum}.fits     -- does not yet exist
            spectra-{nside}-{pixnum}.fits
            zbest-{nside}-{pixnum}.fits
        zcatalog-{specprod}.fits


.. toctree::
   :maxdepth: 1

   calib1d/index
   calibnight/index
   exposures/index
   spectra-NSIDE/index
   zcatalog-SPECPROD
