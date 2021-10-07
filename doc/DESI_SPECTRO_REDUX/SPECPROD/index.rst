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
        calibnight/{night}/
            fiberflatnight-{camera}-{night}.fits
            psfnight-{camera}-{night}.fits
        exposures/{night}/{expid}/
            cframe-{camera}-{expid}.fits
            exposure-qa-{expid}.fits
            fiberflat-{camera}-{expid}.fits
            fit-psf-*-{camera}-{expid}.fits
            fluxcalib-{camera}-{expid}.fits
            frame-{camera}-{expid}.fits
            psf-{camera}-{expid}.fits
            sframe-{camera}-{expid}.fits
            shifted-input-psf-{camera}-{expid}.fits
            sky-{camera}-{expid}.fits
            stdstars-{spectrograph}-{expid}.fits
        healpix/
            tilepix.fits
        healpix/{survey}/{program}/{group}/{pixnum}/
            coadd-{survey}-{program}-{pixnum}.fits
            qso_mgii-{survey}-{program}-{pixnum}.fits
            qso_qn-{survey}-{program}-{pixnum}.fits
            redrock-{survey}-{program}-{pixnum}.fits
            spectra-{survey}-{program}-{pixnum}.fits
        preproc/{night}/{expid}/
            fibermap-{expid}.fits
            preproc-{camera}-{expid}.fits
        tiles/
            TBD
        zcatalog/
            zpix-{survey}-{program}.fits
            ztile-{survey}-{program}-{tiletype}.fits


.. toctree::
   :maxdepth: 1

   calibnight/index
   exposures/index
   healpix/index
   preproc/index
   tiles/index
   zcatalog/index
   exposures-SPECPROD
