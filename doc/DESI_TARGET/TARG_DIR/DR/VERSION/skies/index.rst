=====
skies
=====

The ``skies`` directory contains blank sky locations derived
at the pixel-level from the Legacy Surveys images. Sky locations
are stored in files that are grouped by (nested) HEALPixel number
in filenames that resemble skies-hp-{``HP``}.fits, where ``HP`` is
the HEALPixel number.

The ``skies`` directory may also contain an unpartitioned sub-directory.
This exists because the sky locations are originally generated in
Legacy Surveys `bricks` before being re-partitioned into HEALPixels.
The unpartitioned sub-directory contains files assembled according to
which `bricks` occupy each HEALPixel rather than by which `sky locations`
occupy each HEALPixel.

Subdirectories and files:
 
.. toctree::
   :maxdepth: 1

   unpartitioned/index
   skies-hp-{hp}.fits: catalogs of blank sky locations <skies-hp-HP>
