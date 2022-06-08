=======
RESOLVE
=======

``RESOLVE`` refers to whether targets have been resolved to account for
duplicates in overlapping Legacy Surveys imaging. The northern and southern
imaging footprints overlap and are *resolved* to only retain targets in the
northern imaging that are both at Dec. > 32.375 degrees and north of the
Galactic Plane.

The pixweight catalogs are typically always resolved, and will therefore
be in a directory named "resolve". Under "resolve", data are grouped according to
the observational conditions (or "layer") in which corresponding targets will
be observed.

Subdirectories:

.. toctree::
   :maxdepth: 1

   OBSCON/index
