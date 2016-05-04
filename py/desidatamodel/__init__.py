# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""
=============
desidatamodel
=============

This package provides support for the DESI_ Data Model.

.. _DESI: http://desi.lbl.gov
"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
# The line above will help with 2to3 support.
#
# Set version string.
#
from ._version import __version__

from sys import version_info

PY3 = version_info[0] > 2


class DataModelError(Exception):
    """Errors related to missing or malformed data model files, etc.
    """
    pass


class DataModelWarning(UserWarning):
    """Warnings related to missing or malformed data model files, etc.
    """
    pass

__all__ = ['__version__', 'PY3', 'DataModelError', 'DataModelWarning']
