======
OBSCON
======

``OBSCON`` designates the observational conditions (or "layer") in which targets
will be observed. Possible values include "dark" and "bright" for dark-time and
bright-time targets, respectively.

Under each observing condition, secondary targets are stored in files that
resemble {``BITNAME``}.fits, where ``BITNAME`` is the name of the secondary
targeting bit used by the desitarget pipeline for a given survey phase (see
the desitarget GitHub repository for, `e.g.` the `sv1`_ or `main`_ secondary
target bitmasks).

.. _`sv1`: https://github.com/desihub/desitarget/blob/2.5.0/py/desitarget/sv1/data/sv1_targetmask.yaml#L155-L226
.. _`main`: https://github.com/desihub/desitarget/blob/2.5.0/py/desitarget/data/targetmask.yaml#L131-L182

.. toctree::
   :maxdepth: 1

   {bitname}.fits: output secondary targeting catalog <BITNAME>
