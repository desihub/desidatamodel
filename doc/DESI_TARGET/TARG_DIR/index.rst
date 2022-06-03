========
TARG_DIR
========

:envvar:`TARG_DIR` is the root directory for catalogs of targets, gfas,
skies, randoms and pixweight files (files of quantities from the random
catalogs averaged across HEALPixels). The canonical location is
``$DESI_ROOT/TS/target/catalogs`` but the environment variable
:envvar:`TARG_DIR` can be set to point anywhere. Here, ``TS`` is, e.g.,
`da/ets` for DESI early target selection.

Under :envvar:`TARG_DIR`:

- Target catalogs derived from DESI Legacy Surveys imaging are grouped by
  the imaging Data Release (DR) as a drX.Y string. The X refers to the
  primary Data Release integer and the Y is only rarely used for critical
  reprocessing of a Data Release (*e.g.* dr7.1).
- Target catalogs derived solely from Gaia are in the gaiadr2 directory.
- Fixed subpriorities assigned for the DESI Main Survey (see Section
  5.2 of the Myers et al. DESI Target Selection Pipeline paper) are
  stored in the subpriority directory.

Subdirectories:

.. toctree::
   :maxdepth: 1

   DR/index
   gaiadr2/index
   subpriority/index
