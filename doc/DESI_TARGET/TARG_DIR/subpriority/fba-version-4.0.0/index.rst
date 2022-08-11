=================
fba-version-4.0.0
=================

The subpriority/fba-version-4.0.0 directory holds files recording the ``desitarget/1.0.0``
``SUBPRIORITY`` values used by ``fiberassign/4.0.0`` for some initial DESI Main
Survey tiles. As of these versions of the DESI code, ``fiberassign`` was
overwriting the ``SUBPRIORITY`` column, meaning that that column recorded
different values to those originally populated by ``desitarget``.
Files in this directory were used to enforce consistent values of ``SUBPRIORITY``
for targets in the ``desitarget/1.1.1`` targeting run used for the
bulk of the DESI Main Survey.

The circumstances that led to the need to enforce ``SUBPRIORITY`` values is included
in a ``README`` file in this directory.

The subpriority files themselves have names that resemble subpriorities-<``TTYPE``>.fits, 
where ``TTYPE`` is one of ``bright``, ``dark`` or ``sky`` for bright-time and dark-time
targets and sky locations, respectively.

.. toctree::
   :maxdepth: 1

   subpriorities-{ttype}.fits: fixed subpriority files <subpriorities-TTYPE>
