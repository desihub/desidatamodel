==
nz
==

:Summary: Contains target densities, as a function of redshift.
:Naming Convention: ``{TARGET}_{PHOTSYS}_nz.txt``, where ``{TARGET}`` is ``QSO``, ``ELG``, ``ELGnotqso``, ``ELG_HIP``, ``ELG_HIPnotqso``, ``LRG``, ``LRG_main``,
                    for dark or ``BGS_ANY``, ``BGS_BRIGHT`` for bright. ``{PHOTSYS}`` is the photometric region 
                    N or S
:Regex: ``[a-zA-Z]{3,}_[NS].txt``
:File Type: ASCII

Contents
========

These ASCII files contain data in 6 columns. First, in the header the area is indicated.
Then, the columns are: zmid zlow zhigh n(z)(h^3/Mpc^3) Number_in_bin Volume_of_bin(Mpc^3/h^3)
