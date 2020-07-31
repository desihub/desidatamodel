=======
RESOLVE
=======

``RESOLVE`` refers to whether targets have been resolved to account for
duplicates in overlapping Legacy Surveys imaging. The northern and southern
imaging footprints overlap and are resolved to only retain targets in the
northern imaging that are both at Dec. > 32.375 degrees and north of the
Galactic Plane. Targets that have been resolved are in directories named
"resolve" and targets that have not been resolved are in directories
named "noresolve". Under each "resolve", data are grouped according to
the observational conditions (or "layer") in which they will be observed.

Subdirectories:

.. toctree::
   :maxdepth: 1

   OBSCON/index
