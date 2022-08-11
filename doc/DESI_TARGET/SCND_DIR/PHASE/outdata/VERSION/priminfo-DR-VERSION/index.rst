===================
priminfo-DR-VERSION
===================

The priminfo-{``DR``}-{``VERSION``} directory stores matches between secondary
targets and DESI primary targets. Here, ``DR`` is the `Legacy Surveys`_
data release used to select the primary targets, and ``VERSION`` is the release
number (tag) of the desitarget code version on GitHub in the format X.Y.Z.

Matches to primary targets are grouped by (nested) HEALPixel number in filenames that
resemble targets-no-obscon-hp-{``HP``}.fits.

.. _`Legacy Surveys`: https://www.legacysurvey.org/


.. toctree::
   :maxdepth: 1

   targets-no-obscon-hp-{hp}.fits: matches between secondary and primary targets <targets-no-obscon-hp-HP>
