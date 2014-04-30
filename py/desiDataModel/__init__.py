"""
=============
desiDataModel
=============

This package is a template for other DESI_ Python_ packages.

A Python package should have a `version()` method that returns the
version of the package.  This function should be used to set the ``__version__``
package variable.

.. _DESI: http://desi.lbl.gov
.. _Python: http://python.org
"""

def version():
    """Returns the version of the template package.

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

