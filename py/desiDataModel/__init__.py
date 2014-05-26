# License information goes here
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
# The line above will help with 2to3 support.
"""
=============
desiDataModel
=============

This package provides support for the DESI_ Data Model.

.. _DESI: http://desi.lbl.gov
"""

def version():
    """Returns the version of the desiDataModel package.

    Parameters
    ----------
    None

    Returns
    -------
    version : str
        A PEP386-compatible version string.

    Notes
    -----
    The version string should be compatible with PEP386_.

    .. _PEP386: http://www.python.org/dev/peps/pep-0386).
    """
    return '0.0.1.dev'

__version__ = version()
