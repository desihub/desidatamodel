====
spec
====

:Summary: Contains "raw" spectra in some sense.
:Naming Convention: ``spec-{target}-{type}.dat``, where ``{target}`` is, *e.g.*,
                    ``qso``, ``elg``, ``lrg``, etc.
:Regex: ``spec-(elg|lrg|lya|qso|sky)-.+\.dat``
:File Type: ASCII, 1 MB

Contents
========

These ASCII files typically contain two columns, Wavelength [Å], and flux
in unknown units.
