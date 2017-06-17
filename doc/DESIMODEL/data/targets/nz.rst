==
nz
==

:Summary: Contains target densities as a function of redshift and possibly
          other parameters.
:Naming Convention: ``nz_{target}.dat``, where ``{target}`` is, *e.g.*,
                    ``qso``, ``elg``, ``lrg``, etc.
:Regex: ``(nzr?|dNdzdg)_[A-Za-z_]+\.dat``
:File Type: ASCII


Contents
========

These ASCII files contain data in 2 to 3 columns.  The first column is
the redshift bin, the second column, if present, is a magnitude bin (*g* or *r*),
the third column is the target density in the bin defined by the other
column(s).
