==========
desi-EXPID
==========

General Description
===================

Summary
-------

This is a placeholder for documenting the DESI raw data format.

Nominally it will be a FITS file with one extension per camera, with each
data section compressed with a lossless format via fpack.

Naming Convention
-----------------

``desi-{EXPID}.fits``, where {EXPID} is the 8-digit exposure ID.

regex: ``desi-[0-9]{8}\.fits``

File Type
---------

FITS, 1 MB
