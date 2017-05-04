====
sdss
====

:Summary: Filter transmission curves for SDSS filters.
:Naming Convention: ``sdss_{date}_{filter}_atm.dat``, where ``{date}`` is
                    when the curves were measured, and ``{filter}`` is
                    *u*, *g*, *r*, *i*, *z*.
:Regex: ``sdss_jun2001_[ugriz]_atm\.dat``
:File Type: ASCII, 1 KB

Contents
========

*Derived from the comments in the files:*

The first column is the wavelength in Ångstroms.  The second column
(respt) is the quantum efficiency on the sky looking through 1.3
airmasses at APO for a point source.  The third column (resbig) is the
QE under these conditions for very large sources (size greater than
about 80 pixels) for which the infrared scattering is negligible.  The
only filters for which the infrared scattering has any effect are r and
i; the scattering in the bluer chips is negligible, and the z chips are
not thinned and the phenomenon does not exist.  The fourth column
(resnoa) is the response of the third column with *no* atmosphere,
and the fifth column is the assumed atmospheric transparency at
*one* airmass at APO.
