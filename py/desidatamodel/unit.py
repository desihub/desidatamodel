# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""
==================
desidatamodel.unit
==================

Shared code for dealing with units in files and data models.
"""
from warnings import warn
from astropy.units import Unit


class _FITSUnitWarning(UserWarning):
    """Warnings related to invalid FITS units.
    """
    pass


def _validate_unit(unit, error=False):
    """Check units for consistency with FITS standard, while allowing
    some special exceptions.

    Parameters
    ----------
    unit : :class:`str`
        The unit to parse.
    error : :class:`bool`, optional
        If ``True``, failure to interpret the unit raises an
        exception.

    Returns
    -------
    :class:`str`
        If a special exception is detected, the name of the unit
        is returned.  Otherwise, ``None``.

    Raises
    ------
    :exc:`ValueError`
        If `error` is set and the unit can't be parsed.
    """
    acceptable_units = ('maggie', 'maggy', 'mgy',
                        'electron/Angstrom',
                        'log(Angstrom)')
    try:
        au = Unit(unit, format='fits')
    except ValueError as e:
        bad_unit = str(e).split()[0]
        if any([u in bad_unit for u in acceptable_units]):
            return bad_unit
        else:
            if error:
                raise
            else:
                warn(str(e), FITSUnitWarning)
    return None


try:
    from desiutil.annotate import validate_unit, FITSUnitWarning
except ImportError:
    validate_unit = _validate_unit
    FITSUnitWarning = _FITSUnitWarning
