========
SCND_DIR
========

:envvar:`SCND_DIR` is the root directory for secondary targets.
The canonical location is ``$DESI_ROOT/TS/target/secondary`` but the
environment variable :envvar:`SCND_DIR` can be set to point anywhere.
Here, ``TS`` is, e.g., `da/ets` for DESI early target selection.

Under :envvar:`SCND_DIR`, secondary targets are grouped according to
DESI observational phase. Observational phases include "mainX" for
iterations of the DESI Main Science Survey, "svX" for iterations of
Survey Validation and "cmx" for commissioning, where "X" is an integer.

:envvar:`SCND_DIR` may also contain a directory ``bespoke`` which
includes secondary programs that needed special handling to be
incorporated into DESI observations. The ``bespoke`` directory contains
simple text files with an accompanying README file that describes each
special program.

Finally, :envvar:`SCND_DIR` may include a README file outlining
the general nature of secondary targets.

Subdirectories:

.. toctree::
   :maxdepth: 1

   PHASE/index
   bespoke/index
