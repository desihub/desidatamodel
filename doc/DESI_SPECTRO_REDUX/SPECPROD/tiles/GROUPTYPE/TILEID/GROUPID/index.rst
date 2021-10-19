=======
GROUPID
=======

During commissioning and survey validation, per-tile spectra, coadds, and redshifts
are grouped in ``tiles/GROUPTYPE/TILEID/GROUPID``.

The ``GROUPID`` depends on the ``GROUPTYPE``.

* For ``[14]x_depth`` coadds, the ``GROUPID`` is the subset number.
* For ``cumulative`` coadds, the ``GROUPID`` is the last ``NIGHT`` in the set
  of nights being coadded.
* For ``perexp`` coadds, the ``GROUPID`` is simply the ``EXPID``.
* For ``pernight`` coadds, the ``GROUPID`` is simply the ``NIGHT``.

.. toctree::
   :maxdepth: 1

   coadd-SPECTROGRAPH-NIGHT-GROUPID
   qso_mgii-SPECTROGRAPH-NIGHT-GROUPID
   qso_qn-SPECTROGRAPH-NIGHT-GROUPID
   redrock-SPECTROGRAPH-NIGHT-GROUPID
   spectra-SPECTROGRAPH-NIGHT-GROUPID
   tile-qa-TILEID-GROUPID
