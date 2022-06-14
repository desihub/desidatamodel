=======
VERSION
=======

``VERSION`` is the release number (tag) of the desitarget code version
on GitHub in the format X.Y.Z. Under each code version, data are grouped
according to the type of target.

Types of target include "targets", "skies"
"gfas", "randoms", "pixweight" files (files of quantities from the random
catalogs averaged across HEALPixels) and QA (quality assurance) files.
Not every target type is included in a given ``VERSION`` directory.

Subdirectories:

.. toctree::
   :maxdepth: 1

   gfas/index
   pixweight/index
   QA/index
   randoms/index
   skies/index
   targets/index
