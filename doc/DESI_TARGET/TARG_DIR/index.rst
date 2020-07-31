========
TARG_DIR
========

:envvar:`TARG_DIR` is the root directory for catalogs of targets, gfas,
skies, randoms and pixweight files (files of quantities from the random
catalogs averaged across HEALPixels). The canonical location is
``$DESI_ROOT/target/catalogs``, but the environment variable
:envvar:`TARG_DIR` can be set to point anywhere. The catalogs, at this
level of the directory tree, are grouped by Data Release (DR) of imaging
from the Legacy Surveys as a drX.Y string. The X refers to the primary
Data Release integer and the Y is only rarely used for critical
reprocessing of a Data Release (*e.g.* dr7.1)

Subdirectories:

.. toctree::
   :maxdepth: 1

   DR/index
