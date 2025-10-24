================
nz for FFA mocks
================

:Summary: Contains target densities, as a function of redshift.
:Naming Convention: ``{TARGET}_ffa_nz.txt``, where ``{TARGET}`` is ``QSO``, ``ELG_LOP``, ``LRG``, ``LRG+ELG_LOP`` for dark or ``BGS``, for bright. 
:Regex: ``[A-Za-z0-9._+-]+_ffa_nz\.txt``
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
