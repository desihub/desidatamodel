Contributing to desidatamodel
-----------------------------

Introduction
~~~~~~~~~~~~

This page is about contributing to the
DESI data model documentation; it is not about the data model itself.

Examples and Other Documents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. toctree::
    :maxdepth: 1

    examples/index

Directory Tree
~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~

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

To build the docs::

    python setup.py build_sphinx
    
Then view ``build/sphinx/html/index.html`` in a web browser.  If you have
installed the sphinx_rtd_theme python package, the docs will be formatted
using the ReadTheDocs theme as they will appear at
https://desidatamodel.readthedocs.org

sphinx will often print warnings and claim that the "build succeeded" when
in fact there were syntax errors that break the output.  i.e. pay attention
to the warnings and fix them.

-------------------------------------------------------------------------

desidatamodel Python Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The desidatamodel_ package on github includes the datamodel input files
and some python utility code for generating
and checking datamodel files.

.. _desidatamodel: https://github.com/desihub/desidatamodel

.. automodule:: desidatamodel
   :members:

.. automodule:: desidatamodel.check
  :members:

.. automodule:: desidatamodel.stub
   :members:

