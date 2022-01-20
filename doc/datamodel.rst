=============================
Contributing to desidatamodel
=============================

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

Cross-referencing files
+++++++++++++++++++++++

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

You can also cross-reference sections within files, however the notation is
somewhat different. There are two methods.  The first involves creating
an explicit reference point in the target document.  For example, in the
spPlate file we referenced above, we can label HDU5::

    .. _spplate-hdu5-plugmap:

    HDU5
    ----

    EXTNAME = PLUGMAP

Then we use ``:ref:`` to cross-reference that label. Here's a link to that
:ref:`section of the spPlate file <spplate-hdu5-plugmap>`::

    :ref:`section of the spPlate file <spplate-hdu5-plugmap>`

Note however, that this label must be globally unique!

Alternatively, one can use "raw" ReStructuredText constructions. Here's a link
to another `section of the spPlate file`_ we already linked to above::

    link to another `section of the spPlate file`_

    .. _`section of the spPlate file`: examples/spPlate.html#hdu6

.. _`section of the spPlate file`: examples/spPlate.html#hdu6

Note this time that the section name may be upper case (``HDU6``), but the
HTML anchor is lower case ``#hdu6``.

Environment variables
+++++++++++++++++++++

Here is how to highlight an :envvar:`ENVIRONMENT_VARIABLE`::

    Here is how to highlight an :envvar:`ENVIRONMENT_VARIABLE`

Building the Documents
~~~~~~~~~~~~~~~~~~~~~~

To build the docs::

    sphinx-build -W --keep-going -b html doc doc/_build/html

Then view ``doc/_build/html/index.html`` in a web browser.  If you have
installed the `sphinx_rtd_theme Python package`_, the docs will be formatted
using the ReadTheDocs theme as they will appear at
https://desidatamodel.readthedocs.io

Sphinx will often print warnings and claim that the "build succeeded" when
in fact there were syntax errors that break the output. You must pay attention
to the warnings and fix them!

.. _`sphinx_rtd_theme Python package`: https://pypi.org/project/sphinx-rtd-theme/

desidatamodel Python Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The desidatamodel_ package on GitHub includes the datamodel input files
and some Python utility code for generating
and checking datamodel files.

.. _desidatamodel: https://github.com/desihub/desidatamodel

.. automodule:: desidatamodel
    :members:

.. automodule:: desidatamodel.check
    :members:

.. automodule:: desidatamodel.stub
    :members:

.. automodule:: desidatamodel.unit
    :members:
