=========
pixweight
=========

The pixweight directory contains catalogs that combine useful quantities
from the imaging surveys used to select DESI targets with information about
the targets themselves. Quantities in the pixweight files are grouped by
HEALPixel to facilitate the production of sky maps and to help calculate
metrics related to imaging systematics.

The pixweight catalogs are grouped according to the specific DESI observational phase.
Observational phases include "mainX" for iterations of the DESI Main
Science Survey, "svX" for iterations of Survey Validation and "cmx" for
commissioning, where "X" is an integer.

This directory may also contain a README file indicating which target files
and random catalogs were used to assemble the pixweight files.

Subdirectories:

.. toctree::
   :maxdepth: 1

   PHASE/index
