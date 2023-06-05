===================
randoms-seed-pixnum
===================

:Summary: DESI inside-the-footprint random catalogs contain a single binary table
    covering the entire Legacy Surveys footprint. They contain meta information
    (the number of observations, the depth, etc.) derived from pixels in Legacy
    Surveys CCDs at random RA/Dec coordinates.
:Naming Convention: ``randoms-seed-iteration-hp-pixnum.fits``, where ``seed`` represents
    the random seed used to generate the catalog, ``iteration`` lists the iteration
    number of the catalog (several iterations are typically conducted
    during a given run to generate random catalogs), and ``pixnum`` is the
    HEALPixel number.
:Regex: ``randoms-[0-9]+-hp-[0-9]+\.fits``
:File Type: FITS, 14 GB

These files contain the same data as a standard "randoms" file, but split by
HEALPixel, using the ``NSIDE=8``, ``NESTED`` scheme.  For example, given a
standard randoms file, ``randoms-1-15.fits``, ``randoms-1-15/randoms-1-hp-123.fits``
would contain the portion of the data that is in pixel number 123.

See :doc:`the standard randoms file description <../randoms-seed-iteration>`.
