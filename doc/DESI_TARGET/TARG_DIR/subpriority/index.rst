===========
subpriority
===========

The subpriority directory includes files recording the ``desitarget/1.0.0``
``SUBPRIORITY`` values used by ``fiberassign/4.0.0`` for some initial DESI Main
Survey tiles. As of these versions of the DESI code, ``fiberassign`` was
overwriting the ``SUBPRIORITY`` column, meaning that that column recorded
different values to those originally populated by ``desitarget``.
Files in this directory were used to enforce consistent values of ``SUBPRIORITY``
for targets in the ``desitarget/1.1.1`` targeting run used for the
bulk of the DESI Main Survey.

The ``subpriority`` directory contains a sub-directory named ``fba-version-4.0.0``,
indicative of the ``fiberassign`` version.

Subdirectories:

.. toctree::
   :maxdepth: 1

   fba-version-4.0.0/index
