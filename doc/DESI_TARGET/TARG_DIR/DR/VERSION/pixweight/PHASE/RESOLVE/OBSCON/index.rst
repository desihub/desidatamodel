======
OBSCON
======

``OBSCON`` designates the observational conditions (or "layer") in which targets
will be observed. Possible values include "dark" and "bright" for dark-time and
bright-time targets, respectively.

Under each observing condition, pixweight files are stored in files that are
grouped by the seed used to make the random catalog incorporated into the
pixweight file. They have filenames that resemble
{``PHASE``}pixweight-{``SEED``}-{``OBSCON``}.fits . Here, ``SEED`` is the
seed of the corresponding random catalog.

.. toctree::
   :maxdepth: 1

   {phase}pixweight-{seed}-{obscon}.fits: pixweight file <PHASEpixweight-SEED-OBSCON>
