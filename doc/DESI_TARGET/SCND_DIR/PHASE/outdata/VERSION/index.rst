=======
VERSION
=======

``VERSION`` is the release number (tag) of the desitarget code version
on GitHub in the format X.Y.Z.

Under each ``VERSION``, data are grouped according to
the observational conditions (or "layer") in which they will be observed,
typically "dark" or bright".

The ``VERSION`` directory also includes a subdirectory named
priminfo-{``DR``}-{``VERSION``} that stores matches between secondary
targets and DESI primary targets. Here, ``DR`` is the `Legacy Surveys`_
data release used to select the primary targets.

.. _`Legacy Surveys`: https://www.legacysurvey.org/

Subdirectories:

.. toctree::
   :maxdepth: 1

   OBSCON/index
   priminfo-DR-VERSION/index
