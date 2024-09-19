# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""
=============
desidatamodel
=============

This package provides support for the DESI_ Data Model.

.. _DESI: https://www.desi.lbl.gov
"""
#
# Set version string.
#
from ._version import __version__


class DataModelError(Exception):
    """Errors related to missing or malformed data model files, etc.
    """
    pass


class DataModelWarning(UserWarning):
    """Warnings related to missing or malformed data model files, etc.
    """
    pass
