=======
sn-spec
=======

:Summary: Contains processed versions of the ``spec`` files in the same directory.
:Naming Convention: ``sn-spec-{target}-{type}.dat``, where ``{target}`` is, *e.g.*,
                    ``qso``, ``elg``, ``lrg``, etc.
:Regex: ``spec-(elg|lrg|lya|qso|sky)-.+\.dat``
:File Type: ASCII, 1 MB

Contents
========

These ASCII files typically contain several columns, Wavelength [Å], flux
[erg / cm2 sec Å], inverse variance, and signal-to-noise.  Additional
columns, such as electron counts, may also be present.
