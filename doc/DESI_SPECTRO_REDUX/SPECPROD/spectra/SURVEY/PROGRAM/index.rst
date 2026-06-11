=======
PROGRAM
=======

This directory contains summary files for the uniqpix covered by this ``SURVEY`` and ``PROGRAM``,
and subdirectories grouping those uniqpix.  The ``PROGRAM`` is related to tile design.  The current allowed values are
``dark``, ``bright``, ``backup`` and ``other``.

The summary files are:

  * :doc:`hpix2upix-SURVEY-PROGRAM.fits <hpix2upix-SURVEY-PROGRAM>`: a mapping from healpix to uniqpix for this ``SURVEY`` and ``PROGRAM``.
  * :doc:`uniqpix-SURVEY-PROGRAM.fits <uniqpix-SURVEY-PROGRAM>`: a table of uniqpix covered by this ``SURVEY`` and ``PROGRAM`` with the number of unique targets and number of input uncoadded spectra.

Notes
-----

1. The value of ``PROGRAM`` actually comes from the ``FAPRGRM`` in fiberassign
   files.
2. The value of ``PROGRAM`` *does not* reflect the value of ``PROGRAM`` as
   obtained from the corresponding header keyword in raw data files.
3. For ``SURVEY = sv1``, the values of ``FAPRGRM`` had not stabilized, so
   for ``sv1``, the ``PROGRAM`` is assigned *post facto*.


.. toctree::
   :maxdepth: 1

   PIXGROUP/index
   hpix2upix-SURVEY-PROGRAM
   uniqpix-SURVEY-PROGRAM
