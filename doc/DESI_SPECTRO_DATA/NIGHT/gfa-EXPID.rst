==========
gfa-EXPID
==========

:Summary: Placeholder datamodel for the GFA data
:Naming Convention: ``gfa-EXPID.fits``, where EXPID is the zero-padded
    8-digit exposure ID.
:Regex: ``gfa-[0-9]{8}\.fits``
:File Type: FITS, 50 MB

Contents
========

TBD, not written yet.

e.g. 4D [ngfa, nreadout, npix_y, npix_x] image HDU plus a table HDU
with ngfa x nreadout rows defining the mapping between images, GFAs,
and readout times.