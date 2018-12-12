# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""
==================
desidatamodel.unit
==================

Shared code for dealing with units in files and data models.
"""
from astropy.units import Unit
from desiutil.log import log
from . import DataModelError


class DataModelUnit(object):
    """Allow unit-handling code to be shared with several classes.
    """
    _acceptable_units = ('maggie', 'mgy')

    def check_unit(self, unit, error=False):
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
        try:
            au = Unit(unit, format='fits')
        except ValueError as e:
            bad_unit = str(e).split()[0]
            if any([u in bad_unit for u in self._acceptable_units]):
                return bad_unit
            else:
                if error:
                    log.critical(str(e))
                    raise
                else:
                    log.warning(str(e))
        return None
