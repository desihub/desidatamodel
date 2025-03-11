======================
zall-pix-SPECPROD.fits
======================

:Summary: Concatenation of all ``zpix-*.fits`` files.
:Naming Convention: ``zall-pix-{SPECPROD}.fits``, where ``{SPECPROD}`` is the
    official name of the full reduction, *e.g.* ``fuji``.
:Regex: ``zall-pix-[a-z0-9_-]+\.fits``
:File Type: FITS, 2 GB

This file contains a concatenation of all input :doc:`zpix-*.fits <./zpix-SURVEY-PROGRAM>` files, combining
redshift catalog entries across SURVEYs and PROGRAMs.  It additionally adds
a column ``SV_PRIMARY`` to indicate the best recommended redshift if the same
``TARGETID`` appears multiple times, and ``SV_NSPEC`` for how many times each
target appears.

e.g. if the same Survey Validation ``TARGETID`` was observed during
both Target Selection Validation (sv1) and the One-Percent Survey (sv3),
it will appear as separate redshifts in separate zpix files, and will
appear twice in this file with one of the entries having ``SV_PRIMARY==True``.
Any target that appears only once will also have ``SV_PRIMARY==True``.

Contents
========

====== ============ ======== ===================
Number EXTNAME      Type     Contents
====== ============ ======== ===================
HDU0_  PRIMARY      IMAGE    Empty
HDU1_  ZCATALOG     BINTABLE Redshift catalog joined with target catalog
====== ============ ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = PRIMARY

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Required Header Keywords Table

    .. rst-class:: keywords

    ============ ================ ==== =======================
    KEY          Example Value    Type Comment
    ============ ================ ==== =======================
    CHECKSUM     9aaGCVYE9aaECUYE str  HDU checksum
    DATASUM      0                str  data unit checksum
    ZCATVER      v1               str  Version of zcatalog files
    ============ ================ ==== =======================

Empty HDU.

HDU1
----

See `ZCATALOG HDU1 of zpix-SURVEY-PROGRAM.fits <zpix-SURVEY-PROGRAM.html#hdu1>`_.

