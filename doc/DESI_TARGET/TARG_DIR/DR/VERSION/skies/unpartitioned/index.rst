=============
unpartitioned
=============

The ``unpartitioned`` directory will `not` be a useful data product for
most users. It exists because the sky locations are originally generated in
Legacy Surveys `bricks` before being re-partitioned into HEALPixels.
The unpartitioned sub-directory contains files assembled according to
which `bricks` occupy each HEALPixel rather than by which `sky locations`
occupy each HEALPixel. It is included for completeness.

.. toctree::
   :maxdepth: 1

    skies-hp-{hp}.fits-unpartitioned: catalogs of unpartitioned sky locations <skies-hp-HP.fits-unpartitioned>

