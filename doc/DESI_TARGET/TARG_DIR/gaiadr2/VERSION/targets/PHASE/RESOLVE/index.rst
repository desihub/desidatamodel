=======
RESOLVE
=======

``RESOLVE`` refers to whether targets have been resolved to account for
duplicates in overlapping Legacy Surveys imaging. The northern and southern
imaging footprints overlap and are *resolved* to only retain targets in the
northern imaging that are both at Dec. > 32.375 degrees and north of the
Galactic Plane. Targets that have been resolved are in directories named
"resolve" and targets that have not been resolved are in directories
named "noresolve".

Under each "resolve", data are stored in a ``BACKUP`` directory named ``supp``
prior to version ``0.50.0`` of the ``desitarget`` code and ``backup`` for
``0.50.0``, or later, of the ``desitarget`` code. The choice of ``backup``
versus ``supp`` is semantic, and files in the ``BACKUP`` directory are
similarly constructed.

Subdirectories:

.. toctree::
   :maxdepth: 1

   BACKUP/index
