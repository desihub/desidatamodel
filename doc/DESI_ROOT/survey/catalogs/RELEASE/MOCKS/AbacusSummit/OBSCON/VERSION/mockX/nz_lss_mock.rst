=====================================
nz mock for FFA and COMPLETE flavours
=====================================

:Summary: Contains target densities, as a function of redshift.
:Naming Convention: ``{TARGET}_{GALCAP}_nz.txt``, where ``{TARGET}`` is ``QSO``, ``ELG_LOPnotqso``, ``LRG``, for dark or ``BGS_ANY``, ``BGS_BRIGHT``, ``BGS_BRIGHT-21.5``, for bright. ``{GALCAP}`` is the Galactic hemisphere region NGC or SGC.
:Regex: ``[A-Za-z0-9._+-]+_(NGC|SGC|N|S|HPmapcut)_nz\.txt``
:File Type: ASCII

Contents
========

These ASCII files contain data in 6 columns. In the header the area is indicated.

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: columns

============= ======= ========== =========================================================================================
Name          Type    Units      Description
============= ======= ========== =========================================================================================
zmid          float64            Redshift center at the given redshift bin
zlow          float64            Lower limit at the given redshift bin
zhigh         float64            Upper limit at the given redshift bin
n(z)          float64 h^3 Mpc^-3 The comoving number density of the tracer at the given redshift, assuming complete sample
Number_in_bin float64            Number of tracers at the given redshift bin, including weights
Volume_of_bin float64 Mpc^3 h^-3 Comoving volumne at the given redshift bin
============= ======= ========== =========================================================================================
