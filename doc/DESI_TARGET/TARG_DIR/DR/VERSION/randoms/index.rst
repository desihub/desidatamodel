=======
randoms
=======

Random catalogs are grouped according to
whether the randoms have been resolved to account for duplicates in
overlapping Legacy Surveys imaging. The northern and southern imaging
footprints overlap and are *resolved* to only retain targets in the northern
imaging that are both at Dec. > 32.375 degrees and north of the Galactic Plane.

In addition, a ``randomsall`` directory may exist. The ``randomsall`` directory
contains larger random catalogs that have been assembled by concatenating
smaller catalogs, as described in ``randomsall/README``.

Subdirectories:

.. toctree::
   :maxdepth: 1

   RESOLVE/index
   randomsall/index
