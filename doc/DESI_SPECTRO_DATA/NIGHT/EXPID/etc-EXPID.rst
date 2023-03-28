=========
etc-EXPID
=========

:Summary: JSON file containing details of the ETC analysis for one DESI spectrograph
    exposure.
:Naming Convention: ``etc-EXPID.json``, where EXPID is the zero-padded 8-digit
    exposure ID.
:Regex: etc-[0-9]{8}\.json
:File Type: JSON, 100 kB

Contents
========

Each file contains a dictionary with the following top-level keys:

================ ============================================
Key              Description
================ ============================================
``desietc``      Version number of the desietc_ package used.
``expinfo``      Information about this spectrograph exposure including a summary of the results of analyzing the initial GFA acquisition images.
``fassign``      Information about the fiber assignment for the tile to observe used by the ETC.
``acquisition``  Details from the analysis of the initial in-focus GFA acquisition images.
``-guide_stars`` Details of the guide stars used from each in-focus GFA.
``header``       List of the ETC summary keywords that also appear in the main spectrograph FITS file.
``shutter``      Tracking of successive cosmic-split exposures.
``thru``         Details of the per-GFA exposure analysis of fiber acceptance fraction and atmospheric transmission contributing to the signal throughput.
``sky``          Details of the per-SKYCAM exposure analysis of relative sky background levels.
``accum``        Details of the ETC model of accumulated of signal to noise after each GFA and SKYCAM exposure.
================ ============================================


.. _desietc: https://github.com/desihub/desietc
