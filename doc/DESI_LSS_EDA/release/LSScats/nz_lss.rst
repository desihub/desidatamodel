==
nz
==

:Summary: Contains target densities, as a function of redshift.
:Naming Convention: ``{TARGET}_{PHOTSYS}_nz.txt``, where ``{TARGET}`` is ``QSO``, ``ELG``, ``LRG`` 
                    for dark or ``BGS_BRIGHT-21.5``, ``BGS_BRIGHT`` for bright. ``{PHOTSYS}`` is 
                    N or S
:Regex: ``(nzr?|dNdzdg)_[A-Za-z_]+\.dat``
:File Type: ASCII

Contents
========

These ASCII files contain data in 6 columns. First, in the header the area is indicated.
Then, the columns are: zmid zlow zhigh n(z)(h^3/Mpc^3) Number_in_bin Volume_of_bin(Mpc^3/h^3)
