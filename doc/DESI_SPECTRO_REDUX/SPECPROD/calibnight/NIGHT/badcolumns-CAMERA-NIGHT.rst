=======================
badcolumns-CAMERA-NIGHT
=======================

:Summary: Auxilliary file listing bad columns.
:Naming Convention: ``badcolumns-CAMERA-NIGHT.csv``, where ``CAMERA`` is
    *e.g.*, "b0", "r5", etc. and ``NIGHT`` is the observation night in
    YYYYMMDD format.
:Regex: ``badcolumns-[brz][0-9]-[0-9]{8}\.csv``
:File Type: CSV, 1 KB

Contents
========

A list of unmasked bad columns identified from a 300 sec calibration dark frame.

Note: file may contain no data if all bad columns are already masked.

The file should have these columns:

============ ======= ================================================================================
Name         Type    Description
============ ======= ================================================================================
CAMERA       char[*] Camera identifier. Passband and SPECGRPH ([brz][0-9]).
COLUMN       int     CCD column number
ELEC_PER_SEC float   median electrons/sec in column
SIGMA        float   statistical significance as non-zero
============ ======= ================================================================================
