======
indata
======

The ``indata`` directory contains one .txt or .fits file for each target class
submitted by each researcher who proposed secondary targets for DESI
observations.

Files in the ``indata`` directory resemble {``BITNAME``}.fits or {``BITNAME``}.txt,
where ``BITNAME`` is the name of the secondary targeting bit used by the desitarget
pipeline for a given survey phase (see the desitarget GitHub repository for, `e.g.`
the `sv1`_ or `main`_ secondary target bitmasks).

.. _`sv1`: https://github.com/desihub/desitarget/blob/2.5.0/py/desitarget/sv1/data/sv1_targetmask.yaml#L155-L226
.. _`main`: https://github.com/desihub/desitarget/blob/2.5.0/py/desitarget/data/targetmask.yaml#L131-L182


.. toctree::
   :maxdepth: 1

   {bitname}.fits or {bitname}.txt: input secondary targeting catalog <BITNAME>

