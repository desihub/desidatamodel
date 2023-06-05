=======
RESOLVE
=======

``RESOLVE`` refers to whether targets have been resolved to account for
duplicates in overlapping `Legacy Surveys`_ (LS) imaging. The northern and southern
imaging footprints overlap and are *resolved* to only retain targets in the
northern imaging that are both at Dec. > 32.375 degrees and north of the
Galactic Plane. Randoms catalogs that have been resolved are in directories
named "resolve" and randoms that have not been resolved are in directories
named "noresolve". Under each "resolve", random catalogs can take several
different forms.


.. toctree::
   :maxdepth: 1

    REGION <REGION/index>
    Randoms split by HEALPixel <randoms-SEED-ITERATION/index>
    randoms-{seed}-{iteration}.fits: Random catalog in the LS footprint <randoms-seed-iteration>
    randoms-outside-{seed}-{iteration}.fits: Random catalog outside of the LS footprint <randoms-outside-seed-iteration>
    randoms-allsky-{seed}-{iteration}.fits: Random catalog combined across the entire sky <randoms-allsky-seed-iteration>

.. _`Legacy Surveys`: http://legacysurvey.org
.. _`LS`: http://legacysurvey.org/dr9/catalogs/
