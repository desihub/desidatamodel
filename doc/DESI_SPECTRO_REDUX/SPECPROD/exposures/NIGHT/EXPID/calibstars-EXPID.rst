================
calibstars-EXPID
================

:Summary: Auxilliary file with information on calibration stars.
:Naming Convention: ``calibstars-{EXPID}.csv``, where ``{EXPID}``
    is the 8-digit exposure ID.
:Regex: ``calibstars-[0-9]{8}\.csv``
:File Type: CSV, 50 KB

Contents
========

The file should have these columns:

=========== ===== ========================
Name        Type  Description
=========== ===== ========================
FIBER       int   Fiber ID on the CCDs [0-4999]
RCALIBFRAC  float TODO: description needed
EBV         float Galactic extinction E(B-V) reddening from SFD98
MODEL_COLOR float TODO: description needed
DATA_COLOR  float TODO: description needed
X           float TODO: description needed
Y           float TODO: description needed
VALID       int   TODO: description needed
=========== ===== ========================
