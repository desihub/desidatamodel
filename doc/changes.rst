========================
desidatamodel Change Log
========================

18.9 (unreleased)
-----------------

* Deprecate ``DESI_TARGET`` files (``sky``, ``stdstar``) that aren't in use (PR `#59`_).
* Describe apertures in the skies file as "radius" not "size" (PR `#59`_).
* Add randoms/gfas/skies/pixweight files to the ``DESI_TARGET`` model (PR `#57`_).
* Update the targets file in the ``DESI_TARGET`` model (PR `#57`_).
* Ensure that ``BUNIT`` and ``TUNIT*`` values obey the FITS standard (PR `#54`_).

.. _`#54`: https://github.com/desihub/desidatamodel/pull/54
.. _`#57`: https://github.com/desihub/desidatamodel/pull/57
.. _`#59`: https://github.com/desihub/desidatamodel/pull/59

18.6 (2018-07-20)
-----------------

Tag for 18.6 software release (with a slight delay).

* Updates for quicklook pipeline (PR `#48`_, `#50`_).
* Raw data now stored in ``NIGHT``/``EXPID`` directories (PR `#52`_)

.. _`#48`: https://github.com/desihub/desidatamodel/pull/48
.. _`#50`: https://github.com/desihub/desidatamodel/pull/50
.. _`#52`: https://github.com/desihub/desidatamodel/pull/52

18.3 (2018-05-09)
-----------------

Tag for 18.3 software release (albeit 1.5 months later).

* Switching to YY.[M]M versioning to match software releases.
* Fill in missing file summaries and HDU descriptions (PR `#47`_).
* Update data model to reflect reference run 18.3 (PR `#46`_).
* Drop support for Python 2.

.. _`#46`: https://github.com/desihub/desidatamodel/pull/46
.. _`#47`: https://github.com/desihub/desidatamodel/pull/47

1.2.0 (2018-03-23)
------------------

* Vet data model against reference run 18.2a.  Numerous changes to data
  model Python code to support, *e.g.* compressed HDUs (PR `#42`_).
* Many accumulated changes since 2015.

.. _`#42`: https://github.com/desihub/desidatamodel/pull/42

1.1.1 (2015-11-06)
------------------

* Some fixes for Python 3 tests (PR `#5`_).

.. _`#5`: https://github.com/desihub/desidatamodel/pull/5

1.1.0 (2015-11-06)
------------------

* Use :mod:`astropy.io.fits` consistently (PR `#4`_).

.. _`#4`: https://github.com/desihub/desidatamodel/pull/4

1.0.0 (2015-10-29)
------------------

* Support for ``desiInstall``, etc. (PR `#1`_).

.. _`#1`: https://github.com/desihub/desidatamodel/pull/1

0.2.0 (2015-05-22)
------------------

* See git log files.

0.1.0 (2015-01-16)
------------------

* See git log files.

0.0.4 (2015-01-12)
------------------

* See git log files.

0.0.3 (2014-07-21)
------------------

* See git log files.

0.0.2 (2014-06-10)
------------------

* See git log files.

0.0.1 (2014-05-29)
------------------

* See git log files.
