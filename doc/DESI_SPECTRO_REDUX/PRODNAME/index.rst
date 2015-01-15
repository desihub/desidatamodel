============================
DESI_SPECTRO_REDUX/PRODNAME/
============================

Input files for spectroscopic reduction::

    $DESI_SPECTRO_DATA/{night}/
    desi-{expid}.fits
    fibermap-{expid}.fits

    $DESI_SPECTRO_SIM/{night}/
    desi-{expid}.fits                           -- does not yet exist
    fibermap-{expid}.fits
    pix-{camera}-{expid}.fits
    simpix-{camera}-{expid}.fits
    simspec-{expid}.fits

Output files::

    $DESI_SPECTRO_REDUX/$PRODNAME/
    exposures/{night}/{expid}/
    pix-{camera}-{expid}.fits               -- optional
    frame-{camera}-{expid}.fits
    skymodel-{camera}-{expid}.fits
    fluxcalib-{camera}-{expid}.fits
    cframe-{camera}-{expid}.fits
    config-{expid}.json
    bricks/{brickid}/
    brick-{brickid}.fits
    coadd-{brickid}.fits
    z-{brickid}.fits                        -- zbest, zall?
    calib1d/{night}/
    fiberflat-{camera}-{expid}.fits
    calib2d/{night}/
    psf/psf-{camera}-{expid}.fits


.. toctree::
   :maxdepth: 1

   bricks/index
   calib1d/index
   calib2d/index
   exposures/index
   versions.json
