==
v0
==

The v0 redshift catalogs are deprecated, and provided only as a reference
because they had been released internally to the DESI collaboration and were
in use prior to bugfixes in the :doc:`v1 <../v1/index>` catalogs.

The v0 catalogs follow the same format as :doc:`v1 <../v1/index>`,
except they do not have the columns
``DESINAME``, ``MIN_MJD``, ``MAX_MJD``, and ``MEAN_MJD``.
Additionally, they have bugs in the columns
``COADD_FIBERSTATUS``, ``MEAN_FIBER_{RA,DEC}``, ``STD_FIBER_{RA,DEC}``,
``MEAN_DELTA_{X,Y}``, ``RMS_DELTA_{X,Y}``, ``MEAN_PSF_TO_FIBER_SPECFLUX``,
and ``STD_FIBER_RA`` as described in the
`DR1 known issues <https://data.desi.lbl.gov/doc/releases/dr1/known-issues/>`_.

