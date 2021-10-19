=======
PROGRAM
=======

The ``PROGRAM`` is related to tile design.  The current allowed values are
``backup``, ``bright``, ``dark`` and ``other``.  ``bright`` and ``other``
currently only apply to the ``sv[123]`` surveys.

Caveats
-------

1. The value of ``PROGRAM`` actually comes from the ``FAPRGRM`` in fiberassign
   files.
2. The value of ``PROGRAM`` *does not* reflect the value of ``PROGRAM`` as
   obtained from the corresponding header keyword in raw data files.
3. For ``SURVEY = sv1``, the values of ``FAPRGRM`` had not stabilized, so
   for ``sv1``, the ``PROGRAM`` is assigned *post facto*.


.. toctree::
   :maxdepth: 1

   PIXGROUP/index
