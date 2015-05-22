===============================
Welcome to the DESI Data Model!
===============================

The DESI Data Tree
==================

.. toctree::
   :maxdepth: 1

   imaging/index
   DESI_SPECTRO_DATA/index
   DESI_SPECTRO_SIM/index
   DESI_SPECTRO_REDUX/index


Examples
========

.. toctree::
   :maxdepth: 1

   examples/index


Directory Tree
==============

Please follow these rules when creating or updating directories within the
data model.

1. All directories have an index.rst file.
2. The title of every index.rst file contains *only* the name of the directory it is in.
3. Each index.rst contains the following items in its toctree:

   a. Links to index.rst files in any subdirectories.
   b. Links to files in that directory.


Tips and Tests
==============

Here is how you make a :doc:`direct link to a file <imaging/data/decam/YYYYMMDD/DECam>`::

    Here is how you make a :doc:`direct link to a file <imaging/data/decam/YYYYMMDD/DECam>`


desidatamodel Python Package
============================

.. automodule:: desidatamodel
   :members:

.. automodule:: desidatamodel.stub
   :members:
   :imported-members:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
