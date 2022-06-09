=====
PHASE
=====

``PHASE`` is a specific DESI observational phase, which can include
"mainX" for iterations of the DESI Main Science Survey, "svX" for
iterations of Survey Validation and "cmx" for commissioning, where X
is an integer.

Under each survey phase, secondary targeting information is distributed
across 3 directories:

- ``indata`` contains a .txt or .fits file that includes the targets
  submitted by each researcher who proposed secondary targets for DESI
  observations.
- ``docs`` contains a .ipynb (Jupyter Notebook) or .txt file provided
  by the proposer describing how each secondary target class was constructed.
- ``outdata`` contains files from the ``indata`` directory with the added
  targeting information (`i.e.` IDs and bits) needed by the DESI pipeline.
  
The filename for a given secondary program is consistent across each of the
``indata``, ``docs`` and ``outdata`` directories, and corresponds to the name
of the secondary targeting bit used by the desitarget pipeline for a given
survey phase (see the desitarget GitHub repository for, `e.g.` `sv1`_ or
`main`_). The file `extension` can differ, though (`i.e.` some files in
``docs`` would have the extension .ipynb whereas the corresponding file in
``outdata`` would have the extension .fits).
 
The ``PHASE`` directory may also contain a ``notes`` file, which
includes working notes compiled by the run manager for secondary
targets (Adam D. Myers, University of Wyoming) while sifting
through the various files submitted as part of the DESI secondary
proposal process.

Subdirectories:

.. toctree::
   :maxdepth: 1

   indata/index
   docs/index
   outdata/index

.. _`sv1`: https://github.com/desihub/desitarget/blob/2.5.0/py/desitarget/sv1/data/sv1_targetmask.yaml#L155-L226
.. _`main`: https://github.com/desihub/desitarget/blob/2.5.0/py/desitarget/data/targetmask.yaml#L131-L182
