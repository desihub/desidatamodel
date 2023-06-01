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
RCALIBFRAC  float Ratio of r-band spectro flux / model flux
EBV         float Galactic extinction E(B-V) reddening from SFD98
MODEL_COLOR float G-R color of best fit model
DATA_COLOR  float G-R color of data
X           float X location on focal plane [mm]
Y           float Y location on focal palne [mm]
VALID       int   stdstar selected as good
=========== ===== ========================

Standard stars are selected as valid to use by comparing the scatter of the
flux to the model fits for all stdstars across petals.  3-sigma outliers
in RCALIBFRAC are rejected, as are stars whose G-R color differs by more
than 0.2*EBV from their best fit model.