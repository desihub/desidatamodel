=================
randoms-noresolve
=================

:Summary: These files are identical to the standard randoms, but they have
    not been "resolved" with respect to imaging region.
:Naming Convention: ``randoms-noresolve-seed-iteration.fits``, where ``seed`` represents
    the random seed used to generate the catalog and ``iteration`` lists the iteration
    number of the catalog (several iterations are typically conducted
    during a given run to generate random catalogs).
:Regex: ``randoms-noresolve-[0-9]+-[0-9]+\.fits``
:File Type: FITS, 14 GB

These files have an additional header keyword in HDU1, *e.g.* ::

    REGION  = 'north   '

where ``REGION`` can be 'north' or 'south'.

See :doc:`the standard randoms file description <../randoms-seed-iteration>`.
