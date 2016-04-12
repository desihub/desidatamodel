===============================
Welcome to the DESI Data Model!
===============================

The DESI Data Tree
==================

DESI data are grouped broadly by category, using environment variables to
define the base directory under which files of that category are kept.
These variables have a standard location relative to $DESI_ROOT, but code
uses these variables so that one can swap out different input/output locations
for testing.

.. toctree::
   :maxdepth: 1

   $DESI_SPECTRO_DATA : raw data <DESI_SPECTRO_DATA/index>
   $DESI_SPECTRO_REDUX : processed spectro data <DESI_SPECTRO_REDUX/index>
   $DESI_SPECTRO_SIM : simulated spectro data <DESI_SPECTRO_SIM/index>
   $DESI_TARGET : target selection and fiber assignment <DESI_TARGET/index>


Imaging data and their catalogs are documented separatedly by the
`Legacy Survey <http://legacysurvey.org/>`_.

To Do
=====

* LSS catalog
* DESIMODEL

-------------------------------------------------------------------------

The rest of the documentation on this page is about contributing to this
DESI data model documentation; it is not about the data model itself.

Directory Tree
==============

Please follow these rules when creating or updating directories within the
data model.

1. All directories must have an index.rst file.
2. The title of every index.rst file contains *only* the name of the directory it is in.
3. Each index.rst contains the following items in its toctree:

   a. Links to index.rst files in any subdirectories.
   b. Links to files in that directory.

4. Every file must have a title.  For example::

    ===================
    fibermap-EXPID.fits
    ===================

Tips and Tests
==============

You can browse some :doc:`examples <examples/index>`.

Here is how you make a :doc:`direct link to a file <examples/spPlate>`::

    Here is how you make a :doc:`direct link to a file <examples/spPlate>`

Note that the link must take into account the directory structure.
So for example, if you're in the directory ``DESI_SPECTRO_SIM/PIXPROD/NIGHT``
and want to refer to a file in ``DESI_SPECTRO_DATA/NIGHT``, the link has
to have the form::

    :doc:`link to real data <../../../DESI_SPECTRO_DATA/NIGHT/real_data_file>`

or::

    :doc:`link to real data </DESI_SPECTRO_DATA/NIGHT/real_data_file>`

That is, you can use a relative or absolute path.

Here is how to highlight an :envvar:`ENVIRONMENT_VARIABLE`::

    Here is how to highlight an :envvar:`ENVIRONMENT_VARIABLE`

desidatamodel Python Package
============================

.. automodule:: desidatamodel
   :members:

.. automodule:: desidatamodel.check
  :members:

.. automodule:: desidatamodel.stub
   :members:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
