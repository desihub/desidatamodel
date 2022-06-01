====================
nz
====================

:Summary:  Redshift distribution given a target clustering catalog 
:Naming Convention: ``{target}_{reg}_nz.txt``, where ``{target}`` is
                    the target type (LRG, ELG...) and ``{reg}`` can be S,N or non-exist
:Regex: ``[a-zA-Z]_[A-Z]_nz\.txt`` 
:File Type: ASCII, 5 KB


Contents
========

Histogram with N(z) distribution

ASCII Header
~~~~~~~~~~~~

First commented line summarize the effective area of the sample
given a density of randoms of 2500 sources/deg2


Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

========= ======== ===== ============================
Name      Type     Units Description
========= ======== ===== ============================
zmid      float64        Center value of redshift bin
zlow      float64        Lower limit of redshift bin 
zhigh     float64        Higher limit of redshift bin
n(z)      float64        N(z) value in given bin
Nbin      float64        Number of targets in bin
Vol_bin   float64  Mpc-3 Volume of bim
========= ======== ===== ============================


Notes and Examples
==================

